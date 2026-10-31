from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import *

class Browser():
    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Medula Browser")
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        #self.urlBar = QTextEdit()
        #self.urlBar.setMaximumHeight(30)
        #self.goButton = QPushButton("Go")
        #self.goButton.setMinimumHeight(30)
        #self.goButton.clicked.connect(lambda: self.navigate(self.urlBar.toPlainText()))
        self.backButton = QPushButton("<-")
        self.backButton.setMinimumHeight(30)
        self.forwardButton = QPushButton("->")
        self.forwardButton.setMinimumHeight(30)
        #self.horizontal.addWidget(self.urlBar)
        #self.horizontal.addWidget(self.goButton)
        self.horizontal.addWidget(self.backButton)
        self.horizontal.addWidget(self.forwardButton)
        
        self.browser = QWebEngineView()
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        self.browser.setUrl(QUrl("https://medeczane.sgk.gov.tr/eczane/login.jsp"))
        self.backButton.clicked.connect(self.browser.back)
        self.forwardButton.clicked.connect(self.browser.forward)

        self.window.setLayout(self.layout)
        self.window.show()
        
        if True:
            '''def navigate(self,url):
            if not url.startswith("https://"):
            #https://www.google.com/search?q=else+if+in
            newUrl = url.split(" ")
            url = "https://google.com/search?q="
            for item in newUrl:
            url += item + "+"
            self.browser.setUrl(QUrl(url))'''
            pass
    


app = QApplication([])
Qwindow = Browser()
app.exec()