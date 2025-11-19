-- Migration: Add hashed_password column to users table
-- This migration adds the missing hashed_password column required by FastAPI Users
-- PostgreSQL version
-- Status: ⚠️ DEPRECATED - This column already exists in db/authoritative_schema.sql
-- This migration is kept for historical reference only.

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
        -- Note: You may need to update existing rows with proper hashed passwords
        -- This default is only for schema migration - existing users should be updated separately
    END IF;
END $$;
