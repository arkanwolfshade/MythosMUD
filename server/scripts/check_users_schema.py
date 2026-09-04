#!/usr/bin/env python3
"""Check the schema of the users table."""

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
else:
    env_file = project_root / ".env"
    if env_file.exists():
        load_dotenv(env_file)


async def main() -> None:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        print("DATABASE_URL not set")
        sys.exit(1)

    engine = create_async_engine(database_url, echo=False)
    async with engine.connect() as conn:
        result = await conn.execute(
            text("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_name = 'users'
                ORDER BY ordinal_position
            """)
        )
        print("Users table columns:")
        for row in result:
            print(f"  {row[0]}: {row[1]} (nullable: {row[2]})")
    await engine.dispose()


if __name__ == "__main__":
    run(main)
