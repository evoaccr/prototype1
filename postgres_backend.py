"""Connect to Old Portfolio using the same endpoint/account as Portfolio."""
from pathlib import Path
import json

import psycopg
from psycopg import sql

BASE = Path(__file__).resolve().parent


def get_settings():
    return json.loads((BASE / "postgres-credentials.json").read_text(encoding="utf-8"))


def query(schema, statement):
    return sql.SQL(statement).format(schema=sql.Identifier(schema))


def connect(user=None, password=None, *, autocommit=False):
    settings = get_settings()
    return psycopg.connect(
        host=settings["host"], port=settings["port"], dbname=settings["dbname"],
        user=user or settings["user"],
        password=settings["password"] if password is None else password,
        connect_timeout=5, application_name="Ajarise Old Portfolio",
        autocommit=autocommit,
    )
