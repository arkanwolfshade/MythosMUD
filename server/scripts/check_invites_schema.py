#!/usr/bin/env python3
"""Check invites table schema."""

import os
import sys
from pathlib import Path

from anyio import run
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

# Load environment variables
project_root = Path(__file__).parent.parent.parent
env_file = project_root / ".env.local"
if env_file.exists():
    load_dotenv(env_file)


async def main() -> None:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        print("ERROR: DATABASE_URL not set")
        sys.exit(1)

    engine = create_async_engine(database_url, echo=False)
    try:
        async with engine.connect() as conn:
            result = await conn.execute(
                text("""
                    SELECT column_name, data_type, is_nullable
                    FROM information_schema.columns
                    WHERE table_name = 'invites'
                    ORDER BY ordinal_position
                """)
            )
            print("Invites table columns:")
            for row in result:
                print(f"  {row[0]}: {row[1]} (nullable: {row[2]})")
    finally:
        await engine.dispose()


if __name__ == "__main__":
    run(main)
