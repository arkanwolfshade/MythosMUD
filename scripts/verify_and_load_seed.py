#!/usr/bin/env python3
"""Verify and load seed data - shows output clearly."""

import sys
from pathlib import Path

from anyio import run

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import text
from sqlalchemy.exc import DatabaseError, SQLAlchemyError

from server.config import get_config
from server.database import get_async_session


async def main():
    """Load seed data and verify."""
    print("=" * 60)
    print("MYTHOSMUD SEED DATA LOADER")
    print("=" * 60)

    config = get_config()
    print(f"Database URL: {config.database.url[:50]}...")

    async for session in get_async_session():
        try:
            # Check current counts
            print("\nCurrent table counts:")
            prof_result = await session.execute(text("SELECT COUNT(*) FROM professions"))
            prof_count = prof_result.scalar()
            print(f"  Professions: {prof_count}")

            item_result = await session.execute(text("SELECT COUNT(*) FROM item_prototypes"))
            item_count = item_result.scalar()
            print(f"  Item Prototypes: {item_count}")

            npc_result = await session.execute(text("SELECT COUNT(*) FROM npc_definitions"))
            npc_count = npc_result.scalar()
            print(f"  NPC Definitions: {npc_count}")

            # Load seed files
            seed_files = [
                ("data/db/01_professions.sql", "Professions"),
                ("data/db/02_item_prototypes.sql", "Item Prototypes"),
                ("data/db/03_npc_definitions.sql", "NPC Definitions"),
            ]

            print("\nLoading seed data...")
            for seed_file, name in seed_files:
                file_path = Path(seed_file)
                if not file_path.exists():
                    print(f"  [X] {name}: File not found ({seed_file})")
                    continue

                sql = file_path.read_text(encoding="utf-8")
                try:
                    await session.execute(text(sql))
                    await session.commit()
                    print(f"  [OK] {name}: Loaded successfully")
                except SQLAlchemyError as e:
                    print(f"  [X] {name}: ERROR - {e}")
                    await session.rollback()

            # Verify final counts
            print("\nFinal table counts:")
            prof_result = await session.execute(text("SELECT COUNT(*) FROM professions"))
            prof_count = prof_result.scalar()
            print(f"  Professions: {prof_count}")

            item_result = await session.execute(text("SELECT COUNT(*) FROM item_prototypes"))
            item_count = item_result.scalar()
            print(f"  Item Prototypes: {item_count}")

            npc_result = await session.execute(text("SELECT COUNT(*) FROM npc_definitions"))
            npc_count = npc_result.scalar()
            print(f"  NPC Definitions: {npc_count}")

            print("\n" + "=" * 60)
            print("SEED DATA LOADING COMPLETE")
            print("=" * 60)

            break

        except (DatabaseError, SQLAlchemyError) as e:
            print(f"\nERROR: {e}")
            import traceback

            traceback.print_exc()
            await session.rollback()
            sys.exit(1)


if __name__ == "__main__":
    run(main)
