#!/usr/bin/env python3
"""Fix missing flavor_text column in professions table."""

import os
import sys
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
if not database_url:
    print("ERROR: DATABASE_URL environment variable not set", file=sys.stderr)
    sys.exit(1)

url = database_url.replace("postgresql+asyncpg://", "postgresql://").replace("postgresql+psycopg2://", "postgresql://")
parsed = urlparse(url)

print("=== Checking Professions Table Schema ===\n")

conn = psycopg2.connect(
    host=parsed.hostname or "localhost",
    port=parsed.port or 5432,
    user=parsed.username or "postgres",
    password=parsed.password,
    database=parsed.path.lstrip("/") if parsed.path else "mythos_dev"
)

cur = conn.cursor()

# Check current columns
cur.execute("""
    SELECT column_name, data_type, is_nullable
    FROM information_schema.columns
    WHERE table_name = 'professions'
    ORDER BY ordinal_position;
""")

cols = cur.fetchall()
print("Current columns in professions table:")
for col in cols:
    print(f"  - {col[0]} ({col[1]}, nullable: {col[2]})")

# Check if flavor_text exists
has_flavor_text = any(col[0] == "flavor_text" for col in cols)

if not has_flavor_text:
    print("\n✗ flavor_text column is MISSING")
    print("Adding flavor_text column...")

    try:
        # Add the column
        cur.execute("ALTER TABLE professions ADD COLUMN flavor_text TEXT NOT NULL DEFAULT '';")
        conn.commit()
        print("✓ Successfully added flavor_text column")

        # Update existing rows with default flavor text if needed
        cur.execute("""
            UPDATE professions
            SET flavor_text = description
            WHERE flavor_text = '' OR flavor_text IS NULL;
        """)
        conn.commit()
        print("✓ Updated existing rows with default flavor text")

    except Exception as e:
        print(f"✗ ERROR adding column: {e}", file=sys.stderr)
        conn.rollback()
        sys.exit(1)
else:
    print("\n✓ flavor_text column EXISTS")

# Verify final state
cur.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'professions' AND column_name = 'flavor_text';
""")
result = cur.fetchone()
if result:
    print("\n=== Verification ===")
    print("✓ flavor_text column confirmed in database")

cur.close()
conn.close()

print("\n=== Complete ===")
