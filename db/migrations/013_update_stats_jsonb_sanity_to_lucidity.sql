-- Migration: Update stats JSONB data from sanity to lucidity
-- Date: 2025-12-02
-- Description: Update the DEFAULT value and existing player records to use "lucidity" instead of "sanity"
-- Companion to migration 012 which renamed tables/columns/constraints

BEGIN;

-- ============================================================================
-- STEP 1: Update DEFAULT value on players.stats column
-- ============================================================================

-- Update the default stats JSONB to use "lucidity" instead of "sanity"
ALTER TABLE players ALTER COLUMN stats SET DEFAULT
    '{"fear": 0, "lucidity": 100, "wisdom": 10, "charisma": 10, "position": "standing", "strength": 10, "dexterity": 10, "corruption": 0, "constitution": 10, "intelligence": 10, "current_health": 100, "cult_affiliation": 0, "occult_knowledge": 0}'::jsonb;

-- ============================================================================
-- STEP 2: Update existing player records
-- ============================================================================

-- Update all player records to rename "sanity" → "lucidity" in stats JSONB
UPDATE players
SET stats = stats - 'sanity' || jsonb_build_object('lucidity', COALESCE((stats->>'sanity')::integer, 100))
WHERE stats ? 'sanity';

-- Update all player records to rename "max_sanity" → "max_lucidity" in stats JSONB
UPDATE players
SET stats = stats - 'max_sanity' || jsonb_build_object('max_lucidity', COALESCE((stats->>'max_sanity')::integer, 100))
WHERE stats ? 'max_sanity';

-- ============================================================================
-- STEP 3: Verification
-- ============================================================================

-- Verify no more "sanity" keys in player stats
DO $$
DECLARE
    sanity_count integer;
    max_sanity_count integer;
BEGIN
    SELECT COUNT(*) INTO sanity_count FROM players WHERE stats ? 'sanity';
    SELECT COUNT(*) INTO max_sanity_count FROM players WHERE stats ? 'max_sanity';

    IF sanity_count > 0 THEN
        RAISE WARNING 'Found % players with "sanity" key still in stats', sanity_count;
    END IF;

    IF max_sanity_count > 0 THEN
        RAISE WARNING 'Found % players with "max_sanity" key still in stats', max_sanity_count;
    END IF;

    IF sanity_count = 0 AND max_sanity_count = 0 THEN
        RAISE NOTICE 'All player stats successfully updated to use "lucidity"';
    END IF;
END $$;

COMMIT;
