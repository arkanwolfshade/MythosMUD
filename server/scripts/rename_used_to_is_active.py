#!/usr/bin/env python3
"""
Migration script to rename 'used' column back to 'is_active' in invites table.

This corrects the previous migration - we want is_active in the database to match the model.
"""

import asyncio
import os
import sys
from pathlib import Path

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


async def apply_migration(database_url: str) -> bool:
    """
    Apply the migration to rename used back to is_active.

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

            # Check if 'used' column exists and 'is_active' doesn't
            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_name = 'invites'
                        AND column_name = 'used'
                    );
                    """
                )
            )
            has_used = result.scalar()

            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_name = 'invites'
                        AND column_name = 'is_active'
                    );
                    """
                )
            )
            has_is_active = result.scalar()

            if has_is_active:
                logger.info("Column is_active already exists, skipping migration")
                return True

            if not has_used:
                logger.warning("Column 'used' does not exist, cannot rename")
                return False

            # Rename used to is_active (values are already correct - used=False means inactive, is_active=False means inactive)
            logger.info("Renaming 'used' column to 'is_active'")
            await conn.execute(text("ALTER TABLE invites RENAME COLUMN used TO is_active"))
            await conn.commit()

            # Verify column was renamed
            result = await conn.execute(
                text(
                    """
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_name = 'invites'
                        AND column_name = 'is_active'
                    );
                    """
                )
            )
            column_exists = result.scalar()

            if column_exists:
                logger.info("Migration applied successfully - column renamed to is_active")
                return True
            else:
                logger.error("Migration failed - column was not renamed")
                return False

    except Exception as e:
        logger.error("Error applying migration", error=str(e), error_type=type(e).__name__)
        return False
    finally:
        await engine.dispose()


async def main():
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

    logger.info("Starting migration to rename 'used' to 'is_active'", database_url=database_url.split("@")[-1])

    success = await apply_migration(database_url)

    if success:
        logger.info("Migration completed successfully")
        sys.exit(0)
    else:
        logger.error("Migration failed")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
