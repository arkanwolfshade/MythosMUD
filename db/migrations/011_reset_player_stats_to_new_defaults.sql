-- Migration 011: Reset player stats to new defaults (1-100 range)
-- Date: 2025-11-17
-- Description: Reset all existing player stats to new defaults (50 for core attributes)
-- This migration is part of the player stats migration from 1-20 to 1-100 range
-- Status: Active
DO $$ BEGIN RAISE NOTICE 'Resetting player stats to new defaults (50 for core attributes)...';
-- Update all existing player stats to new defaults
-- Preserve other stats (sanity, occult_knowledge, fear, corruption, cult_affiliation, current_dp, position)
UPDATE players
SET stats = jsonb_set(
        jsonb_set(
            jsonb_set(
                jsonb_set(
                    jsonb_set(
                        jsonb_set(
                            COALESCE(stats, '{}'::jsonb),
                            '{strength}',
                            '50'::jsonb
                        ),
                        '{dexterity}',
                        '50'::jsonb
                    ),
                    '{constitution}',
                    '50'::jsonb
                ),
                '{intelligence}',
                '50'::jsonb
            ),
            '{wisdom}',
            '50'::jsonb
        ),
        '{charisma}',
        '50'::jsonb
    )
WHERE stats IS NOT NULL;
-- Ensure all players have the required stats structure
-- If stats is NULL or missing fields, set complete default structure
UPDATE players
SET stats = jsonb_build_object(
        'strength',
        COALESCE(stats->>'strength', '50'),
        'dexterity',
        COALESCE(stats->>'dexterity', '50'),
        'constitution',
        COALESCE(stats->>'constitution', '50'),
        'intelligence',
        COALESCE(stats->>'intelligence', '50'),
        'wisdom',
        COALESCE(stats->>'wisdom', '50'),
        'charisma',
        COALESCE(stats->>'charisma', '50'),
        'sanity',
        COALESCE(stats->>'sanity', '100'),
        'occult_knowledge',
        COALESCE(stats->>'occult_knowledge', '0'),
        'fear',
        COALESCE(stats->>'fear', '0'),
        'corruption',
        COALESCE(stats->>'corruption', '0'),
        'cult_affiliation',
        COALESCE(stats->>'cult_affiliation', '0'),
        'current_dp',
        COALESCE(stats->>'current_dp', '100'),
        'position',
        COALESCE(stats->>'position', 'standing')
    )
WHERE stats IS NULL
    OR stats->>'strength' IS NULL
    OR stats->>'dexterity' IS NULL
    OR stats->>'constitution' IS NULL
    OR stats->>'intelligence' IS NULL
    OR stats->>'wisdom' IS NULL
    OR stats->>'charisma' IS NULL;
RAISE NOTICE 'Successfully reset player stats to new defaults';
EXCEPTION
WHEN OTHERS THEN RAISE WARNING 'Error resetting player stats: %',
SQLERRM;
RAISE;
END $$;
