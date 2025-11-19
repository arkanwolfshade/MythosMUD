#!/usr/bin/env python3
"""Load seed data into PostgreSQL database."""

import os
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise ValueError("DATABASE_URL environment variable not set")

# Parse database URL
url = database_url.replace("postgresql+asyncpg://", "postgresql://").replace("postgresql+psycopg2://", "postgresql://")
parsed = urlparse(url)

# Database connection info from environment
PGPASSWORD = parsed.password
DB_HOST = parsed.hostname or "localhost"
DB_USER = parsed.username or "postgres"
DB_NAME = parsed.path.lstrip("/") if parsed.path else "mythos_dev"
PSQL_PATH = r"E:\Program Files\PostgreSQL\18\bin\psql.exe"

# Seed files to load
SEED_FILES = [
    "data/db/01_professions.sql",
    "data/db/02_item_prototypes.sql",
    "data/db/03_npc_definitions.sql",
]


def run_psql_command(args, description):
    """Run a psql command and return the result."""
    env = os.environ.copy()
    env["PGPASSWORD"] = PGPASSWORD

    cmd = [PSQL_PATH, "-h", DB_HOST, "-U", DB_USER, "-d", DB_NAME] + args

    print(f"\n{description}...")
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"STDERR: {result.stderr}", file=sys.stderr)

    if result.returncode != 0:
        print(f"ERROR: Command failed with return code {result.returncode}", file=sys.stderr)
        return False

    return True


def main():
    """Load all seed data files."""
    print("=== Loading MythosMUD Seed Data ===")
    print(f"Database: {DB_NAME}")

    # Load each seed file
    for seed_file in SEED_FILES:
        if not Path(seed_file).exists():
            print(f"ERROR: Seed file not found: {seed_file}", file=sys.stderr)
            sys.exit(1)

        if not run_psql_command(["-f", seed_file], f"Loading {seed_file}"):
            print(f"ERROR: Failed to load {seed_file}", file=sys.stderr)
            sys.exit(1)

    # Verify data was loaded
    print("\n=== Verifying Data ===")
    verify_query = """
        SELECT 'professions' as table_name, COUNT(*)::text as count FROM professions
        UNION ALL
        SELECT 'item_prototypes', COUNT(*)::text FROM item_prototypes
        UNION ALL
        SELECT 'npc_definitions', COUNT(*)::text FROM npc_definitions
        ORDER BY table_name;
    """

    if not run_psql_command(["-c", verify_query], "Verifying seed data"):
        print("ERROR: Failed to verify data", file=sys.stderr)
        sys.exit(1)

    print("\n=== Seed data loading complete! ===")


if __name__ == "__main__":
    main()
