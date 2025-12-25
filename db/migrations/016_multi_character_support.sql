-- Migration: Multi-Character Support System
-- Description: Enables multiple characters per user, case-insensitive uniqueness, and soft deletion
-- Date: 2025-01-XX
--
-- This migration:
-- 1. Removes unique constraint on players.user_id to allow multiple characters per user
-- 2. Adds is_deleted and deleted_at columns for soft deletion
-- 3. Replaces unique constraints with case-insensitive unique indexes for usernames and character names
-- 4. Creates indexes for efficient queries

-- Step 1: Drop unique constraint on players.user_id
-- Handle both possible constraint names: players_user_id_key and players_new_user_id_key
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'players_user_id_key'
    ) THEN
        ALTER TABLE players
        DROP CONSTRAINT players_user_id_key;
    END IF;

    IF EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'players_new_user_id_key'
    ) THEN
        ALTER TABLE players
        DROP CONSTRAINT players_new_user_id_key;
    END IF;
END $$;

-- Step 2: Drop unique constraint on users.username (will be replaced with case-insensitive index)
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'users_username_key'
    ) THEN
        ALTER TABLE users
        DROP CONSTRAINT users_username_key;
    END IF;
END $$;

-- Step 3: Drop unique constraint on players.name (will be replaced with case-insensitive partial index)
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'players_name_key'
    ) THEN
        ALTER TABLE players
        DROP CONSTRAINT players_name_key;
    END IF;
END $$;

-- Step 4: Add is_deleted column to players table
ALTER TABLE players
ADD COLUMN IF NOT EXISTS is_deleted BOOLEAN NOT NULL DEFAULT FALSE;

-- Step 5: Add deleted_at column to players table
ALTER TABLE players
ADD COLUMN IF NOT EXISTS deleted_at TIMESTAMPTZ;

-- Step 6: Update existing records to ensure is_deleted is False
UPDATE players
SET is_deleted = FALSE
WHERE is_deleted IS NULL;

-- Step 7: Create index on (user_id, is_deleted) for efficient queries
CREATE INDEX IF NOT EXISTS idx_players_user_id_is_deleted
ON players(user_id, is_deleted);

-- Step 8: Create case-insensitive unique index on users.username
-- This enforces uniqueness case-insensitively (e.g., "ithaqua" and "Ithaqua" are mutually exclusive)
CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username_lower_unique
ON users(LOWER(username));

-- Step 9: Create case-insensitive partial unique index on players.name
-- This enforces uniqueness case-insensitively only for active (non-deleted) characters
-- Deleted character names can be reused
CREATE UNIQUE INDEX IF NOT EXISTS idx_players_name_lower_unique_active
ON players(LOWER(name))
WHERE is_deleted = FALSE;

-- Step 10: Add comments to document the new columns
COMMENT ON COLUMN players.is_deleted IS 'Soft delete flag - deleted characters are hidden but not removed from database';
COMMENT ON COLUMN players.deleted_at IS 'Timestamp when character was soft-deleted (NULL for active characters)';
