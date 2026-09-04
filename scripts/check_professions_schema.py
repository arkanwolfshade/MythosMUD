#!/usr/bin/env python3
"""Check professions table schema."""

import os
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise ValueError("DATABASE_URL environment variable not set")

url = database_url.replace("postgresql+asyncpg://", "postgresql://").replace("postgresql+psycopg2://", "postgresql://")
parsed = urlparse(url)

conn = psycopg2.connect(
    host=parsed.hostname or "localhost",
    port=parsed.port or 5432,
    user=parsed.username or "postgres",
    password=parsed.password,
    database=parsed.path.lstrip("/") if parsed.path else "mythos_dev"
)

cur = conn.cursor()

print("=== Professions Table Schema ===\n")
cur.execute("""
    SELECT column_name, data_type, is_nullable, column_default
    FROM information_schema.columns
    WHERE table_name = 'professions'
    ORDER BY ordinal_position;
""")

cols = cur.fetchall()
print("Columns:")
for col in cols:
    print(f"  {col[0]}: {col[1]} (nullable: {col[2]}, default: {col[3]})")

print("\n=== Checking for flavor_text ===")
has_flavor_text = any(col[0] == "flavor_text" for col in cols)
if has_flavor_text:
    print("✓ flavor_text column EXISTS")
else:
    print("✗ flavor_text column MISSING")
    print("\nAdding flavor_text column...")
    try:
        cur.execute("ALTER TABLE professions ADD COLUMN flavor_text TEXT NOT NULL DEFAULT '';")
        conn.commit()
        print("✓ Added flavor_text column")
    except Exception as e:
        print(f"✗ ERROR: {e}")
        conn.rollback()

cur.close()
conn.close()
