#!/usr/bin/env python3
"""
Migration script to add hashed_password column to users table.

This script adds the missing hashed_password column required by FastAPI Users
to the PostgreSQL database.
"""

import os
import sys
from pathlib import Path

from anyio import run
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

# Add server directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Load environment variables from .env.local
project_root = Path(__file__).parent.parent.parent
env_file = project_root / ".env.local"
if env_file.exists():
    load_dotenv(env_file)
else:
    # Try .env as fallback
    env_file = project_root / ".env"
    if env_file.exists():
        load_dotenv(env_file)

from server.structured_logging.enhanced_logging_config import (  # noqa: E402  # pylint: disable=wrong-import-position
    get_logger,
)

logger = get_logger(__name__)

# Migration SQL
MIGRATION_SQL = """
-- Check if column exists before adding (PostgreSQL specific)
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'users'
        AND column_name = 'hashed_password'
    ) THEN
        ALTER TABLE users ADD COLUMN hashed_password VARCHAR(255) NOT NULL DEFAULT '';
        RAISE NOTICE 'Column hashed_password added to users table';
    ELSE
        RAISE NOTICE 'Column hashed_password already exists in users table';
    END IF;
END $$;
"""


async def apply_migration(database_url: str) -> bool:
    """
    Apply the migration to add hashed_password column.

    Args:
        database_url: PostgreSQL database URL

    Returns:
        True if migration succeeded, False otherwise
    """
    try:
        # Create async engine
        engine = create_async_engine(database_url, echo=False)

        async with engine.connect() as conn:
            # Check if users table exists
            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables
                        WHERE table_name = 'users'
                    );
                    """
                )
            )
            table_exists = result.scalar()

            if not table_exists:
                logger.error("Users table does not exist in database")
                return False

            # Check if column already exists
            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_name = 'users'
                        AND column_name = 'hashed_password'
                    );
                    """
                )
            )
            column_exists = result.scalar()

            if column_exists:
                logger.info("Column hashed_password already exists, skipping migration")
                return True

            # Apply migration (use begin() for transaction)
            logger.info("Applying migration to add hashed_password column")
            async with conn.begin():
                await conn.execute(text(MIGRATION_SQL))

            # Verify column was added
            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_name = 'users'
                        AND column_name = 'hashed_password'
                    );
                    """
                )
            )
            column_exists = result.scalar()

            if column_exists:
                logger.info("Migration applied successfully - hashed_password column added")
                return True
            else:
                logger.error("Migration failed - column was not added")
                return False

    except Exception as e:
        logger.error("Error applying migration", error=str(e), error_type=type(e).__name__)
        return False
    finally:
        await engine.dispose()


async def main() -> None:
    """Main entry point for the migration script."""
    # Get database URL from environment or config
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        logger.error("DATABASE_URL environment variable not set")
        sys.exit(1)

    # Verify it's a PostgreSQL URL
    if not database_url.startswith("postgresql"):
        logger.error("DATABASE_URL must be a PostgreSQL connection string", database_url=database_url)
        sys.exit(1)

    logger.info("Starting migration to add hashed_password column", database_url=database_url.split("@")[-1])

    success = await apply_migration(database_url)

    if success:
        logger.info("Migration completed successfully")
        sys.exit(0)
    else:
        logger.error("Migration failed")
        sys.exit(1)


if __name__ == "__main__":
    run(main)
