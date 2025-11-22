#!/usr/bin/env python3
"""Load seed data using asyncpg through project database connection."""

import asyncio
import os
from pathlib import Path

import asyncpg
from dotenv import load_dotenv

load_dotenv()

async def load_seed_data():
    """Load all seed data files."""
    # Get database URL from environment
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        print("ERROR: DATABASE_URL not set")
        return

    # Convert asyncpg URL to connection params
    # Format: postgresql+asyncpg://user:pass@host:port/db
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")

    print("=== Loading MythosMUD Seed Data ===\n")

    conn = await asyncpg.connect(url)

    try:
        seed_files = [
            "data/db/01_professions.sql",
            "data/db/02_item_prototypes.sql",
            "data/db/03_npc_definitions.sql",
        ]

        for seed_file in seed_files:
            file_path = Path(seed_file)
            if not file_path.exists():
                print(f"ERROR: {seed_file} not found")
                continue

            print(f"Loading {seed_file}...")
            sql = file_path.read_text(encoding='utf-8')

            try:
                await conn.execute(sql)
                print(f"  ✓ Successfully loaded {seed_file}")
            except Exception as e:
                print(f"  ✗ ERROR loading {seed_file}: {e}")

        # Verify counts
        print("\n=== Verification ===")
        prof_count = await conn.fetchval("SELECT COUNT(*) FROM professions")
        print(f"Professions: {prof_count}")

        item_count = await conn.fetchval("SELECT COUNT(*) FROM item_prototypes")
        print(f"Item Prototypes: {item_count}")

        npc_count = await conn.fetchval("SELECT COUNT(*) FROM npc_definitions")
        print(f"NPC Definitions: {npc_count}")

        print("\n=== Complete ===")

    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(load_seed_data())
