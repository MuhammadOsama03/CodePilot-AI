"""SQLite review metadata history. Source text and AI responses are never persisted."""
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

def database_path() -> Path:
    default_path = "/tmp/codepilot-history.sqlite3" if os.environ.get("VERCEL") == "1" else "codepilot-history.sqlite3"
    return Path(os.environ.get("CODEPILOT_DB_PATH", default_path))

def connect():
    path = database_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=5)
    connection.execute("PRAGMA busy_timeout=5000")
    connection.execute("""CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TEXT NOT NULL,
        language TEXT NOT NULL,
        engine TEXT NOT NULL,
        finding_count INTEGER NOT NULL,
        source_characters INTEGER NOT NULL
    )""")
    return connection

def save_review(language: str, engine: str, finding_count: int, source_characters: int) -> int:
    with connect() as db:
        cursor = db.execute(
            "INSERT INTO reviews(created_at,language,engine,finding_count,source_characters) VALUES(?,?,?,?,?)",
            (datetime.now(timezone.utc).isoformat(), language, engine, finding_count, source_characters),
        )
        return int(cursor.lastrowid)

def list_reviews(limit: int = 20) -> list[dict]:
    if not 1 <= limit <= 100:
        raise ValueError("History limit must be between 1 and 100")
    with connect() as db:
        rows = db.execute(
            "SELECT id,created_at,language,engine,finding_count,source_characters FROM reviews ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    keys = ("id", "created_at", "language", "engine", "finding_count", "source_characters")
    return [dict(zip(keys, row)) for row in rows]
