#!/usr/bin/env python3
"""Apply flavor_text fix to professions table."""

import os
import sys
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
if not database_url:
    sys.exit("ERROR: DATABASE_URL not set")

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

# Check if column exists
cur.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'professions' AND column_name = 'flavor_text';
""")

if cur.fetchone():
    print("flavor_text column already exists")
else:
    print("Adding flavor_text column...")
    cur.execute("ALTER TABLE professions ADD COLUMN flavor_text TEXT NOT NULL DEFAULT '';")
    conn.commit()
    print("Added flavor_text column")

    # Update existing rows
    cur.execute("UPDATE professions SET flavor_text = description WHERE flavor_text = '';")
    conn.commit()
    print("Updated existing rows")

cur.close()
conn.close()
print("Done")
