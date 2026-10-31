"""Markdown startup pages, acknowledgement dialog, and startup result."""
from dataclasses import dataclass
from pathlib import Path

from markdown_it import MarkdownIt
import tkinter as tk
from tkinter import ttk, messagebox
from tkinterweb import HtmlFrame

ENTRY_TITLE = "Enter the app"
ACKNOWLEDGEMENT = "I red and understand"
STYLE = """
body { margin: 0; color: #202830; background: #fff; font: 16px 'Segoe UI', sans-serif; }
article { max-width: 820px; margin: auto; padding: 26px 32px; line-height: 1.65; }
h1,h2,h3,h4,h5,h6 { line-height: 1.25; color: #17232d; }
h1 { font-size: 28px; } h2 { font-size: 22px; }
table { border-collapse: collapse; width: 100%; margin: 18px 0; }
td,th { padding: 9px 12px; border: 1px solid #d7dde2; text-align: left; }
th { background: #f1f4f6; } pre,code { background: #f1f4f6; border-radius: 4px; }
pre { padding: 14px; overflow-x: auto; } code { font-family: Consolas, monospace; }
blockquote { margin-left: 0; padding-left: 18px; border-left: 3px solid #b8c6d1; }
hr { border: 0; border-top: 1px solid #d7dde2; margin: 24px 0; }
"""


@dataclass(frozen=True)
class OpeningPage:
    title: str
    html: str


def parse_pages(source):
    parser = MarkdownIt("commonmark", {"html": False}).enable("table")
    tokens = parser.parse(source)
    lines = source.splitlines(keepends=True)
    headings = []
    for index, token in enumerate(tokens):
        if token.type == "heading_open" and token.tag == "h1" and token.level == 0:
            inline = tokens[index + 1]
            title = "".join(child.content for child in inline.children or [] if child.type in ("text", "code_inline"))
            headings.append((token.map[0], title.strip() or "Untitled"))
    sections = []
    first = headings[0][0] if headings else len(lines)
    if "".join(lines[:first]).strip():
        sections.append(("Introduction", "".join(lines[:first])))
    for index, (start, title) in enumerate(headings):
        end = headings[index + 1][0] if index + 1 < len(headings) else len(lines)
        sections.append((title, "".join(lines[start:end])))
    entry = [section for section in sections if section[0].casefold() == ENTRY_TITLE.casefold()]
    if len(entry) > 1:
        raise ValueError("opening.md must contain only one Enter the app heading.")
    sections = [section for section in sections if section[0].casefold() != ENTRY_TITLE.casefold()]
    sections.append(entry[0] if entry else (ENTRY_TITLE, ""))
    pages = []
    for title, markdown in sections:
        html = ("<!doctype html><html><head><meta charset='utf-8'>"
                "<meta http-equiv='Content-Security-Policy' content=\"default-src 'none'; "
                "style-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'\">"
                f"<style>{STYLE}</style></head><body><article>{parser.render(markdown)}</article></body></html>")
        pages.append(OpeningPage(title, html))
    return pages


def load_pages(path):
    return parse_pages(Path(path).read_text(encoding="utf-8-sig"))


class OpeningDialog:
    def __init__(self, pages):
        self.pages = pages
        self.accepted = False
        self.closed = False
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.title("Ajarise")
        available_width, available_height = self.root.maxsize()
        width = min(1000, int(available_width * .9))
        height = min(730, int(available_height * .9))
        x = (self.root.winfo_screenwidth() - width) // 2
        y = (self.root.winfo_screenheight() - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.tabs = ttk.Notebook(self.root, height=1)
        for page in pages:
            self.tabs.add(ttk.Frame(self.tabs), text=page.title)
        self.tabs.grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 0))
        self.view = HtmlFrame(
            self.root, messages_enabled=False, javascript_enabled=False,
            events_enabled=False, forms_enabled=False, objects_enabled=False,
            images_enabled=False, threading_enabled=False,
            on_link_click=lambda url: None, on_form_submit=lambda *args: None,
            request_func=self.block_resource,
        )
        self.view.grid(row=1, column=0, sticky="nsew", padx=12)
        footer = ttk.Frame(self.root, padding=12)
        footer.grid(row=2, column=0, sticky="ew")
        footer.columnconfigure(1, weight=1)
        self.previous = ttk.Button(footer, text="Previous", command=lambda: self.select_page(self.selected - 1))
        self.previous.grid(row=0, column=0)
        self.acknowledged = tk.BooleanVar(self.root, value=False)
        self.acknowledgement = ttk.Checkbutton(footer, text=ACKNOWLEDGEMENT,
                                              variable=self.acknowledged, command=self.update_controls)
        self.acknowledgement.grid(row=0, column=2, padx=14)
        self.forward = ttk.Button(footer, text="Forward", command=lambda: self.select_page(self.selected + 1))
        self.forward.grid(row=0, column=3)
        self.continue_button = ttk.Button(footer, text="Continue", command=self.accept)
        self.continue_button.grid(row=0, column=4)
        self.tabs.bind("<<NotebookTabChanged>>", self.show_page)
        self.root.bind("<Return>", self.on_enter)
        self.root.bind("<Escape>", lambda event: self.reject())
        self.root.protocol("WM_DELETE_WINDOW", self.reject)
        self.update_controls()
        self.initial_load = self.root.after_idle(self.show_page)
        self.root.deiconify()

    @staticmethod
    def block_resource(*args, **kwargs):
        raise OSError("External resources are disabled on the opening screen.")

    @property
    def selected(self):
        return self.tabs.index(self.tabs.select())

    def select_page(self, index):
        self.tabs.select(max(0, min(index, len(self.pages) - 1)))
        self.show_page()

    def show_page(self, event=None):
        if not self.closed:
            self.view.load_html(self.pages[self.selected].html, base_url="about:blank")
            self.update_controls()

    def update_controls(self):
        entry = self.selected == len(self.pages) - 1
        self.previous.state(["!disabled" if self.selected > 0 else "disabled"])
        if entry:
            self.forward.grid_remove()
            self.acknowledgement.grid()
            self.continue_button.grid()
        else:
            self.forward.grid()
            self.acknowledgement.grid_remove()
            self.continue_button.grid_remove()
        self.continue_button.state(["!disabled" if entry and self.acknowledged.get() else "disabled"])

    def accept(self):
        if self.selected == len(self.pages) - 1 and self.acknowledged.get():
            self.accepted = True
            self.dispose()

    def reject(self):
        self.dispose()

    def on_enter(self, event=None):
        if self.selected == len(self.pages) - 1:
            self.accept()
        else:
            self.select_page(self.selected + 1)
        return "break"

    def dispose(self):
        if not self.closed:
            self.closed = True
            self.root.after_cancel(self.initial_load)
            self.root.destroy()

    def run(self):
        self.root.mainloop()
        return self.accepted


def show_opening_screen(path):
    try:
        pages = load_pages(path)
    except (OSError, ValueError) as error:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Ajarise", str(error), parent=root)
        root.destroy()
        return False
    dialog = OpeningDialog(pages)
    try:
        return dialog.run()
    finally:
        dialog.dispose()
