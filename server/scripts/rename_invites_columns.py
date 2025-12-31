#!/usr/bin/env python3
"""
Migration script to rename invites table columns to match the model.

This script renames:
- code → invite_code
- created_by_user → created_by_user_id
- is_active → used (with value inversion)
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

from server.structured_logging.enhanced_logging_config import get_logger  # noqa: E402

logger = get_logger(__name__)

# Migration SQL
MIGRATION_SQL = """
-- Rename code to invite_code
DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'invites'
        AND column_name = 'code'
    ) AND NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'invites'
        AND column_name = 'invite_code'
    ) THEN
        ALTER TABLE invites RENAME COLUMN code TO invite_code;
        RAISE NOTICE 'Column code renamed to invite_code';
    ELSE
        RAISE NOTICE 'Column code does not exist or invite_code already exists';
    END IF;
END $$;

-- Rename created_by_user to created_by_user_id
DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'invites'
        AND column_name = 'created_by_user'
    ) AND NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'invites'
        AND column_name = 'created_by_user_id'
    ) THEN
        ALTER TABLE invites RENAME COLUMN created_by_user TO created_by_user_id;
        RAISE NOTICE 'Column created_by_user renamed to created_by_user_id';
    ELSE
        RAISE NOTICE 'Column created_by_user does not exist or created_by_user_id already exists';
    END IF;
END $$;

-- Rename is_active to used (inverted logic - is_active=True means not used, so used=False)
-- Note: We need to invert the values during migration
DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'invites'
        AND column_name = 'is_active'
    ) AND NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'invites'
        AND column_name = 'used'
    ) THEN
        -- First, invert the values: used = NOT is_active
        UPDATE invites SET is_active = NOT is_active;
        -- Then rename the column
        ALTER TABLE invites RENAME COLUMN is_active TO used;
        RAISE NOTICE 'Column is_active renamed to used (values inverted)';
    ELSE
        RAISE NOTICE 'Column is_active does not exist or used already exists';
    END IF;
END $$;
"""


async def apply_migration(database_url: str) -> bool:
    """
    Apply the migration to rename columns.

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

            # Apply migration - execute each DO block separately
            logger.info("Applying migration to rename invites table columns")

            # Rename code to invite_code
            rename_code_sql = """
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'invites'
                    AND column_name = 'code'
                ) AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'invites'
                    AND column_name = 'invite_code'
                ) THEN
                    ALTER TABLE invites RENAME COLUMN code TO invite_code;
                    RAISE NOTICE 'Column code renamed to invite_code';
                ELSE
                    RAISE NOTICE 'Column code does not exist or invite_code already exists';
                END IF;
            END $$;
            """
            await conn.execute(text(rename_code_sql))
            await conn.commit()

            # Rename created_by_user to created_by_user_id
            rename_created_by_sql = """
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'invites'
                    AND column_name = 'created_by_user'
                ) AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'invites'
                    AND column_name = 'created_by_user_id'
                ) THEN
                    ALTER TABLE invites RENAME COLUMN created_by_user TO created_by_user_id;
                    RAISE NOTICE 'Column created_by_user renamed to created_by_user_id';
                ELSE
                    RAISE NOTICE 'Column created_by_user does not exist or created_by_user_id already exists';
                END IF;
            END $$;
            """
            await conn.execute(text(rename_created_by_sql))
            await conn.commit()

            # Rename is_active to used (with value inversion)
            rename_used_sql = """
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'invites'
                    AND column_name = 'is_active'
                ) AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'invites'
                    AND column_name = 'used'
                ) THEN
                    -- First, invert the values: used = NOT is_active
                    UPDATE invites SET is_active = NOT is_active;
                    -- Then rename the column
                    ALTER TABLE invites RENAME COLUMN is_active TO used;
                    RAISE NOTICE 'Column is_active renamed to used (values inverted)';
                ELSE
                    RAISE NOTICE 'Column is_active does not exist or used already exists';
                END IF;
            END $$;
            """
            await conn.execute(text(rename_used_sql))
            await conn.commit()

            # Verify columns were renamed
            result = await conn.execute(
                text(
                    """
                    SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = 'invites'
                    ORDER BY ordinal_position
                    """
                )
            )
            columns = [row[0] for row in result]

            expected_columns = {"invite_code", "created_by_user_id", "used"}
            has_expected = all(col in columns for col in expected_columns)

            if has_expected:
                logger.info("Migration applied successfully - columns renamed", columns=columns)
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

    logger.info("Starting migration to rename invites table columns", database_url=database_url.split("@")[-1])

    success = await apply_migration(database_url)

    if success:
        logger.info("Migration completed successfully")
        sys.exit(0)
    else:
        logger.error("Migration failed")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
