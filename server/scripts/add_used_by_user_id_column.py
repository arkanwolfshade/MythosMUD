#!/usr/bin/env python3
"""
Migration script to add used_by_user_id column to invites table.

This script adds the used_by_user_id column to track which user consumed which invite.
"""

import os
import sys
from pathlib import Path

from anyio import run
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

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

# Add server directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

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
        WHERE table_name = 'invites'
        AND column_name = 'used_by_user_id'
    ) THEN
        ALTER TABLE invites ADD COLUMN used_by_user_id UUID REFERENCES users(id) ON DELETE SET NULL;
        CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
        RAISE NOTICE 'Column used_by_user_id added to invites table';
    ELSE
        RAISE NOTICE 'Column used_by_user_id already exists in invites table';
    END IF;
END $$;
"""


async def apply_migration(database_url: str) -> bool:
    """
    Apply the migration to add used_by_user_id column.

    Args:
        database_url: PostgreSQL database URL

    Returns:
        True if migration succeeded, False otherwise
    """
    try:
        # Create async engine
        engine = create_async_engine(database_url, echo=False)

        async with engine.connect() as conn:
            # Check if invites table exists
            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables
                        WHERE table_name = 'invites'
                    );
                    """
                )
            )
            table_exists = result.scalar()

            if not table_exists:
                logger.error("Invites table does not exist in database")
                return False

            # Check if column already exists
            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_name = 'invites'
                        AND column_name = 'used_by_user_id'
                    );
                    """
                )
            )
            column_exists = result.scalar()

            if column_exists:
                logger.info("Column used_by_user_id already exists, skipping migration")
                return True

            # Apply migration
            logger.info("Applying migration to add used_by_user_id column")
            await conn.execute(text(MIGRATION_SQL))
            await conn.commit()

            # Verify column was added
            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_name = 'invites'
                        AND column_name = 'used_by_user_id'
                    );
                    """
                )
            )
            column_exists = result.scalar()

            if column_exists:
                logger.info("Migration applied successfully - used_by_user_id column added")
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

    logger.info("Starting migration to add used_by_user_id column", database_url=database_url.split("@")[-1])

    success = await apply_migration(database_url)

    if success:
        logger.info("Migration completed successfully")
        sys.exit(0)
    else:
        logger.error("Migration failed")
        sys.exit(1)


if __name__ == "__main__":
    run(main)
