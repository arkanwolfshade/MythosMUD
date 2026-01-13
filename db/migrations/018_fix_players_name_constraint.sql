-- Migration: Fix Players Name Constraint
-- Description: Drops the old players_new_name_key constraint that prevents
-- deleted character names from being reused
-- Date: 2026-01-13
--
-- This migration fixes an issue where the old unique constraint
-- players_new_name_key was not dropped in migration 016, preventing
-- deleted character names from being reused. The partial unique index
-- idx_players_name_lower_unique_active already enforces uniqueness
-- correctly for active characters only.

-- Drop the old unique constraint on players.name if it exists
-- This constraint prevents deleted character names from being reused
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'players_new_name_key'
    ) THEN
        ALTER TABLE players
        DROP CONSTRAINT players_new_name_key;
        RAISE NOTICE 'Dropped constraint players_new_name_key';
    ELSE
        RAISE NOTICE 'Constraint players_new_name_key does not exist, skipping';
    END IF;
END $$;
