#!/usr/bin/env python3
"""Apply player_skills table migration (025) using DATABASE_URL.

Creates the player_skills table if missing. Run once per database (e.g. mythos_dev).
Uses psycopg2 and .env DATABASE_URL; safe to run multiple times (CREATE TABLE IF NOT EXISTS).
"""

import os
from pathlib import Path
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set")

# Sync driver URL for psycopg2
url = DATABASE_URL.replace("postgresql+asyncpg://", "postgresql://").replace("postgresql+psycopg2://", "postgresql://")
parsed = urlparse(url)

conn = psycopg2.connect(
    host=parsed.hostname or "localhost",
    port=parsed.port or 5432,
    user=parsed.username or "postgres",
    password=parsed.password,
    database=parsed.path.lstrip("/") if parsed.path else "mythos_dev",
)

migration_path = Path(__file__).resolve().parent.parent / "db" / "migrations" / "025_add_player_skills_table.sql"
if not migration_path.exists():
    raise FileNotFoundError(f"Migration file not found: {migration_path}")

sql = migration_path.read_text(encoding="utf-8")
cur = conn.cursor()
cur.execute(sql)
conn.commit()
cur.close()
conn.close()

print("[OK] Applied 025_add_player_skills_table.sql (player_skills table)")
