#!/usr/bin/env python3
"""Add flavor_text column to professions table using project database connection."""

import sys
from pathlib import Path

from anyio import run

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import text

from server.database import get_async_session


async def add_flavor_text_column():
    """Add flavor_text column if missing."""
    async for session in get_async_session():
        try:
            # Check if column exists
            result = await session.execute(
                text("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = 'professions' AND column_name = 'flavor_text';
            """)
            )

            if result.fetchone():
                print("✓ flavor_text column already exists")
            else:
                print("Adding flavor_text column...")
                await session.execute(
                    text("""
                    ALTER TABLE professions
                    ADD COLUMN flavor_text TEXT NOT NULL DEFAULT '';
                """)
                )
                await session.commit()
                print("✓ Added flavor_text column")

                # Update existing rows with default values
                await session.execute(
                    text("""
                    UPDATE professions
                    SET flavor_text = description
                    WHERE flavor_text = '' OR flavor_text IS NULL;
                """)
                )
                await session.commit()
                print("✓ Updated existing rows")

            break
        except Exception as e:
            print(f"ERROR: {e}")
            await session.rollback()
            sys.exit(1)


if __name__ == "__main__":
    run(add_flavor_text_column)
