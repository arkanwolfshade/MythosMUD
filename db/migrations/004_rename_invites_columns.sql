-- Migration: Rename invites table columns to match model
-- This migration renames database columns to match the SQLAlchemy model
-- PostgreSQL version
-- Status: ⚠️ DEPRECATED - Column names already match in db/authoritative_schema.sql
-- This migration is kept for historical reference only.

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
