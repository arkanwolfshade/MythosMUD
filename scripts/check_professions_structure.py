#!/usr/bin/env python3
"""Check actual professions table structure."""

import os
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL", "").replace("postgresql+asyncpg://", "postgresql://").replace("postgresql+psycopg2://", "postgresql://")
parsed = urlparse(database_url)

conn = psycopg2.connect(
    host=parsed.hostname or "localhost",
    port=parsed.port or 5432,
    user=parsed.username or "postgres",
    password=parsed.password,
    database=parsed.path.lstrip("/") if parsed.path else "mythos_dev"
)

cur = conn.cursor()

# Get all columns
cur.execute("""
    SELECT column_name, data_type, is_nullable, column_default
    FROM information_schema.columns
    WHERE table_name = 'professions'
    ORDER BY ordinal_position;
""")

print("=== Professions Table Structure ===")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]} (nullable: {row[2]}, default: {row[3]})")

# Check constraints
cur.execute("""
    SELECT constraint_name, constraint_type
    FROM information_schema.table_constraints
    WHERE table_name = 'professions';
""")

print("\n=== Constraints ===")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}")

cur.close()
conn.close()
