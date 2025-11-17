-- Migration: Add FastAPI Users required columns to users table
-- This migration adds is_active, is_superuser, and is_verified columns
-- PostgreSQL version

-- Add is_active column
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

-- Add is_superuser column
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

-- Add is_verified column
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
