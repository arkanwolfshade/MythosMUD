#!/usr/bin/env python3
"""Load seed data directly using psycopg2."""

import os
from pathlib import Path
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise ValueError("DATABASE_URL environment variable not set")

# Parse database URL
# Format: postgresql+asyncpg://user:password@host:port/database
url = database_url.replace("postgresql+asyncpg://", "postgresql://").replace("postgresql+psycopg2://", "postgresql://")
parsed = urlparse(url)

# Database connection using parsed URL components
conn = psycopg2.connect(
    host=parsed.hostname or "localhost",
    port=parsed.port or 5432,
    user=parsed.username or "postgres",
    password=parsed.password,
    database=parsed.path.lstrip("/") if parsed.path else "mythos_dev",
)

cur = conn.cursor()

# Fix missing profession columns if needed (character creation revamp 4.3/4.4)
print("=== Checking Professions Table Schema ===\n")
for col, default in [
    ("flavor_text", "''"),
    ("stat_modifiers", "'[]'"),
    ("skill_modifiers", "'[]'"),
]:
    cur.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'professions' AND column_name = %s;
        """,
        (col,),
    )
    if not cur.fetchone():
        print(f"Adding missing {col} column to professions table...")
        cur.execute(f"ALTER TABLE professions ADD COLUMN {col} TEXT NOT NULL DEFAULT {default};")
        conn.commit()
        print(f"  [OK] Added {col} column")
    else:
        print(f"  [OK] {col} column exists")
print()

# Load seed files
seed_files = [
    "data/db/01_professions.sql",
    "data/db/02_item_prototypes.sql",
    "data/db/03_npc_definitions.sql",
    "data/db/04_skills.sql",
    "data/db/05_profession_modifiers.sql",
]

print("=== Loading MythosMUD Seed Data ===\n")

for seed_file in seed_files:
    file_path = Path(seed_file)
    if not file_path.exists():
        print(f"ERROR: {seed_file} not found")
        continue

    print(f"Loading {seed_file}...")
    sql = file_path.read_text(encoding="utf-8")

    try:
        cur.execute(sql)
        conn.commit()
        print(f"  [OK] Successfully loaded {seed_file}")
    except Exception as e:
        print(f"  ✗ ERROR loading {seed_file}: {e}")
        conn.rollback()

# Verify counts
print("\n=== Verification ===")
cur.execute("SELECT COUNT(*) FROM professions")
prof_count = cur.fetchone()[0]
print(f"Professions: {prof_count}")

cur.execute("SELECT COUNT(*) FROM item_prototypes")
item_count = cur.fetchone()[0]
print(f"Item Prototypes: {item_count}")

cur.execute("SELECT COUNT(*) FROM npc_definitions")
npc_count = cur.fetchone()[0]
print(f"NPC Definitions: {npc_count}")

cur.close()
conn.close()

print("\n=== Complete ===")
