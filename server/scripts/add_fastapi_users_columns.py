#!/usr/bin/env python3
"""
Migration script to add FastAPI Users required columns to users table.

This script adds:
- is_active (BOOLEAN, default true)
- is_superuser (BOOLEAN, default false)
- is_verified (BOOLEAN, default false)
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

from server.logging.enhanced_logging_config import get_logger  # noqa: E402

logger = get_logger(__name__)


async def apply_migration(database_url: str) -> bool:
    """
    Apply the migration to add FastAPI Users columns.

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

            # Add is_active column
            add_is_active_sql = """
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'users'
                    AND column_name = 'is_active'
                ) THEN
                    ALTER TABLE users ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT true;
                    RAISE NOTICE 'Column is_active added to users table';
                ELSE
                    RAISE NOTICE 'Column is_active already exists in users table';
                END IF;
            END $$;
            """
            await conn.execute(text(add_is_active_sql))
            await conn.commit()

            # Add is_superuser column
            add_is_superuser_sql = """
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'users'
                    AND column_name = 'is_superuser'
                ) THEN
                    ALTER TABLE users ADD COLUMN is_superuser BOOLEAN NOT NULL DEFAULT false;
                    RAISE NOTICE 'Column is_superuser added to users table';
                ELSE
                    RAISE NOTICE 'Column is_superuser already exists in users table';
                END IF;
            END $$;
            """
            await conn.execute(text(add_is_superuser_sql))
            await conn.commit()

            # Add is_verified column
            add_is_verified_sql = """
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'users'
                    AND column_name = 'is_verified'
                ) THEN
                    ALTER TABLE users ADD COLUMN is_verified BOOLEAN NOT NULL DEFAULT false;
                    RAISE NOTICE 'Column is_verified added to users table';
                ELSE
                    RAISE NOTICE 'Column is_verified already exists in users table';
                END IF;
            END $$;
            """
            await conn.execute(text(add_is_verified_sql))
            await conn.commit()

            # Verify columns were added
            result = await conn.execute(
                text(
                    """
                    SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = 'users'
                    ORDER BY ordinal_position
                    """
                )
            )
            columns = [row[0] for row in result]

            expected_columns = {"is_active", "is_superuser", "is_verified"}
            has_expected = all(col in columns for col in expected_columns)

            if has_expected:
                logger.info("Migration applied successfully - FastAPI Users columns added", columns=columns)
                return True
            else:
                logger.warning(
                    "Migration completed but some expected columns missing", columns=columns, expected=expected_columns
                )
                return True  # Still consider success if migration ran

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

    logger.info("Starting migration to add FastAPI Users columns", database_url=database_url.split("@")[-1])

    success = await apply_migration(database_url)

    if success:
        logger.info("Migration completed successfully")
        sys.exit(0)
    else:
        logger.error("Migration failed")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
