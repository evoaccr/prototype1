"""One-time migration and synthetic data setup. Never resets data on launch."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import argparse
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "edited"))

from psycopg import sql

from postgres_backend import connect, get_settings

MEDICINES = (
    ("parol", "9000000000001"),
    ("arveles", "9000000000002"),
    ("iburamin cold", "9000000000003"),
)


def replace_sample_conversation(connection, primary):
    now = datetime.now(timezone(timedelta(hours=3)))
    conversation = (
        (primary, "pharmacy2", "Hi, do you have any arveles in stock?"),
        ("pharmacy2", primary, "Yes, we have some available. How many do you need?"),
        (primary, "pharmacy2", "One box, please. Could you send it over?"),
        ("pharmacy2", primary, "#give/200000000005"),
    )
    with connection.cursor() as cursor:
        for schema in (primary, "pharmacy2"):
            cursor.execute(sql.SQL("DELETE FROM {}.messages WHERE toM <> 'x'").format(sql.Identifier(schema)))
        for index, (sender, recipient, content) in enumerate(conversation):
            timestamp = (now - timedelta(minutes=3 - index)).strftime("%y%m%d%H%M%S")
            cursor.execute(sql.SQL("INSERT INTO {}.messages VALUES (%s,%s,%s,%s)").format(sql.Identifier(sender)),
                           (timestamp, content, recipient, sender))


def populate(backup_path=None):
    settings = get_settings()
    primary = settings["schema"]
    backup = json.loads(Path(backup_path).read_text(encoding="utf-8")) if backup_path else {schema: {table: [] for table in ("stok", "messages", "takas")} for schema in ("demo", "eczane2")}
    now = datetime.now(timezone(timedelta(hours=3)))
    summary = {}
    with connect(autocommit=False) as connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS public.ajarise_setup (version TEXT PRIMARY KEY, details JSONB NOT NULL)")
            cursor.execute("SELECT 1 FROM public.ajarise_setup WHERE version='postgres-v1'")
            if cursor.fetchone():
                print("PostgreSQL migration and population already completed; existing data left intact.")
                return
            for original, schema, total, prefix in (("demo", primary, 180, 1), ("eczane2", "pharmacy2", 90, 2)):
                cursor.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(schema)))
                for ddl in (
                    "CREATE TABLE IF NOT EXISTS {}.stok (karekod TEXT PRIMARY KEY, ad TEXT NOT NULL, barkod TEXT NOT NULL, almaTarih TEXT, satmaTarih TEXT, satmaHasta TEXT, almaYer TEXT)",
                    "CREATE TABLE IF NOT EXISTS {}.messages (messageTime TEXT PRIMARY KEY, content TEXT, toM TEXT, fromM TEXT)",
                    "CREATE TABLE IF NOT EXISTS {}.takas (karekod TEXT PRIMARY KEY, ad TEXT, toT TEXT, fromT TEXT, verTarih TEXT, alTarih TEXT)",
                ):
                    cursor.execute(sql.SQL(ddl).format(sql.Identifier(schema)))
                for index, old in enumerate(backup[original]["stok"]):
                    record = list(old)
                    if record[1].startswith("DEMO İLAÇ"):
                        record[1], record[2] = MEDICINES[index % 3]
                    if record[5] == "DEMO MİSAFİR":
                        record[5] = "Demo guest"
                    if record[6] == "DEMO DEPO":
                        record[6] = "Demo supplier"
                    cursor.execute(sql.SQL("INSERT INTO {}.stok VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING").format(sql.Identifier(schema)), record)
                for old in backup[original]["messages"]:
                    record = list(old)
                    record[0] = primary if record[0] == "demo" else "pharmacy2" if record[0] == "eczane2" else record[0]
                    record[2] = primary if record[2] == "demo" else "pharmacy2" if record[2] == "eczane2" else record[2]
                    record[3] = primary if record[3] == "demo" else "pharmacy2" if record[3] == "eczane2" else record[3]
                    if record[2] != "x":
                        continue
                    cursor.execute(sql.SQL("INSERT INTO {}.messages VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING").format(sql.Identifier(schema)), record)
                for old in backup[original]["takas"]:
                    record = [primary if value == "demo" else value for value in old]
                    cursor.execute(sql.SQL("INSERT INTO {}.takas VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING").format(sql.Identifier(schema)), record)
                for index in range(1, total + 1):
                    name, barcode = MEDICINES[(index - 1) % 3]
                    acquired = (now - timedelta(days=index % 28)).strftime("%y%m%d%H%M")
                    sold = index % 12 == 0
                    record = (str(prefix * 100000000000 + index), name, barcode, acquired,
                              now.strftime("%y%m%d%H%M") if sold else None,
                              f"Demo guest {index}" if sold else None, "Demo supplier")
                    cursor.execute(sql.SQL("INSERT INTO {}.stok VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING").format(sql.Identifier(schema)), record)
                cursor.execute(sql.SQL("CREATE INDEX IF NOT EXISTS stok_name_idx ON {}.stok (ad)").format(sql.Identifier(schema)))
                cursor.execute(sql.SQL("CREATE INDEX IF NOT EXISTS messages_recipient_idx ON {}.messages (toM)").format(sql.Identifier(schema)))
            replace_sample_conversation(connection, primary)
            for schema in (primary, "pharmacy2"):
                cursor.execute(sql.SQL("SELECT COUNT(*) FROM {}.stok").format(sql.Identifier(schema)))
                stocks = cursor.fetchone()[0]
                cursor.execute(sql.SQL("SELECT COUNT(*) FROM {}.messages WHERE toM <> 'x'").format(sql.Identifier(schema)))
                messages = cursor.fetchone()[0]
                summary[schema] = {"stock": stocks, "messages": messages}
            cursor.execute("INSERT INTO public.ajarise_setup VALUES ('postgres-v1', %s::jsonb)", (json.dumps(summary),))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--backup")
    populate(parser.parse_args().backup)
