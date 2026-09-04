#!/usr/bin/env python3
"""Load seed data using project's database connection."""

import sys
from pathlib import Path

from anyio import run

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import text

from server.database import get_async_session


async def load_seed_data():
    """Load all seed data files."""
    print("=== Loading MythosMUD Seed Data ===\n")

    # Get database session
    async for session in get_async_session():
        try:
            seed_files = [
                "data/db/01_professions.sql",
                "data/db/02_item_prototypes.sql",
                "data/db/03_npc_definitions.sql",
                "data/db/04_skills.sql",
                "data/db/05_profession_modifiers.sql",
            ]

            for seed_file in seed_files:
                file_path = Path(seed_file)
                if not file_path.exists():
                    print(f"ERROR: {seed_file} not found")
                    continue

                print(f"Loading {seed_file}...")
                sql = file_path.read_text(encoding="utf-8")

                try:
                    # Execute SQL file
                    await session.execute(text(sql))
                    await session.commit()
                    print(f"  ✓ Successfully loaded {seed_file}")
                except Exception as e:
                    print(f"  ✗ ERROR loading {seed_file}: {e}")
                    await session.rollback()
                    raise

            # Verify counts
            print("\n=== Verification ===")
            prof_result = await session.execute(text("SELECT COUNT(*) FROM professions"))
            prof_count = prof_result.scalar()
            print(f"Professions: {prof_count}")

            item_result = await session.execute(text("SELECT COUNT(*) FROM item_prototypes"))
            item_count = item_result.scalar()
            print(f"Item Prototypes: {item_count}")

            npc_result = await session.execute(text("SELECT COUNT(*) FROM npc_definitions"))
            npc_count = npc_result.scalar()
            print(f"NPC Definitions: {npc_count}")

            skill_result = await session.execute(text("SELECT COUNT(*) FROM skills"))
            skill_count = skill_result.scalar()
            print(f"Skills: {skill_count}")

            print("\n=== Complete ===")
            break  # Only run once

        except Exception as e:
            print(f"ERROR: {e}")
            await session.rollback()
            raise


if __name__ == "__main__":
    run(load_seed_data)
