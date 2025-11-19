-- Migration: Add password_hash column to users table
-- This migration adds the legacy password_hash column for backward compatibility
-- PostgreSQL version
-- Check if column exists before adding (PostgreSQL specific)
DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_name = 'users'
        AND column_name = 'password_hash'
) THEN
ALTER TABLE users
ADD COLUMN password_hash VARCHAR(255) NULL;
RAISE NOTICE 'Column password_hash added to users table';
ELSE RAISE NOTICE 'Column password_hash already exists in users table';
END IF;
END $$;
