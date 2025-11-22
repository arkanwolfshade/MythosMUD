-- Migration 006: Migrate stats column from TEXT to JSONB
-- Date: 2025-11-17
-- Description: Convert players.stats column from TEXT to JSONB to enable JSONB operators
-- This fixes the issue where update_player_stat_field tries to use JSONB operators on TEXT column
-- Status: ⚠️ DEPRECATED - Stats column is already JSONB in db/authoritative_schema.sql
-- This migration is kept for historical reference only.
-- Check if stats column exists and is TEXT type
DO $$
DECLARE current_type TEXT;
BEGIN -- Get current column type
SELECT data_type INTO current_type
FROM information_schema.columns
WHERE table_name = 'players'
    AND column_name = 'stats';
-- Only migrate if column exists and is TEXT
IF current_type = 'text' THEN RAISE NOTICE 'Migrating stats column from TEXT to JSONB...';
-- Step 1: Add a temporary JSONB column
ALTER TABLE players
ADD COLUMN IF NOT EXISTS stats_jsonb JSONB;
-- Step 2: Convert existing TEXT data to JSONB
-- Handle valid JSON strings, invalid JSON, NULL, and empty strings
UPDATE players
SET stats_jsonb = CASE
        WHEN stats IS NULL
        OR stats = '' THEN '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "position": "standing"}'::jsonb
        WHEN stats::text ~ '^\s*\{' THEN -- Valid JSON object - cast to JSONB
        stats::jsonb
        ELSE -- Invalid JSON - use default
        '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "position": "standing"}'::jsonb
    END;
-- Step 3: Make the new column NOT NULL with default
ALTER TABLE players
ALTER COLUMN stats_jsonb
SET NOT NULL,
    ALTER COLUMN stats_jsonb
SET DEFAULT '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "position": "standing"}'::jsonb;
-- Step 4: Drop the old TEXT column
ALTER TABLE players DROP COLUMN stats;
-- Step 5: Rename the new column to stats
ALTER TABLE players
    RENAME COLUMN stats_jsonb TO stats;
RAISE NOTICE 'Successfully migrated stats column from TEXT to JSONB';
ELSIF current_type = 'jsonb' THEN RAISE NOTICE 'Stats column is already JSONB, skipping migration';
ELSE RAISE NOTICE 'Stats column type is %, expected TEXT or JSONB. Skipping migration.',
current_type;
END IF;
EXCEPTION
WHEN OTHERS THEN -- If migration fails, try to clean up temporary column
BEGIN
ALTER TABLE players DROP COLUMN IF EXISTS stats_jsonb;
EXCEPTION
WHEN OTHERS THEN NULL;
-- Ignore cleanup errors
END;
RAISE;
END $$;
