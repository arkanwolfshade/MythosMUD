-- Fix stats JSON structure in players table
-- This script flattens the nested stats structure and ensures all stats keys are present

SET client_min_messages = WARNING;
SET search_path = public;

BEGIN;

-- Update players where stats has nested structure
UPDATE players
SET stats = (
    SELECT jsonb_build_object(
        'strength', COALESCE((stats_json->'stats'->>'strength')::integer, (stats_json->>'strength')::integer, 10),
        'dexterity', COALESCE((stats_json->'stats'->>'dexterity')::integer, (stats_json->>'dexterity')::integer, 10),
        'constitution', COALESCE((stats_json->'stats'->>'constitution')::integer, (stats_json->>'constitution')::integer, 10),
        'intelligence', COALESCE((stats_json->'stats'->>'intelligence')::integer, (stats_json->>'intelligence')::integer, 10),
        'wisdom', COALESCE((stats_json->'stats'->>'wisdom')::integer, (stats_json->>'wisdom')::integer, 10),
        'charisma', COALESCE((stats_json->'stats'->>'charisma')::integer, (stats_json->>'charisma')::integer, 10),
        'sanity', COALESCE((stats_json->'stats'->>'sanity')::integer, (stats_json->>'sanity')::integer, (stats_json->>'sanity')::integer, 100),
        'occult_knowledge', COALESCE((stats_json->'stats'->>'occult_knowledge')::integer, (stats_json->>'occult_knowledge')::integer, 0),
        'fear', COALESCE((stats_json->'stats'->>'fear')::integer, (stats_json->>'fear')::integer, 0),
        'corruption', COALESCE((stats_json->'stats'->>'corruption')::integer, (stats_json->>'corruption')::integer, 0),
        'cult_affiliation', COALESCE((stats_json->'stats'->>'cult_affiliation')::integer, (stats_json->>'cult_affiliation')::integer, 0),
        'current_dp', COALESCE((stats_json->'stats'->>'current_dp')::integer, (stats_json->>'current_dp')::integer, 100),
        'position', COALESCE(stats_json->'stats'->>'position', stats_json->>'position', 'standing')
    )::text
    FROM (SELECT stats::jsonb as stats_json) AS s
    WHERE (stats_json ? 'stats' OR stats_json ? 'level')
)
WHERE stats::jsonb ? 'stats' OR stats::jsonb ? 'level';

-- Verify the update
DO $$
DECLARE
    fixed_count integer;
    remaining_count integer;
BEGIN
    SELECT COUNT(*) INTO fixed_count
    FROM players
    WHERE stats::jsonb ? 'stats' OR stats::jsonb ? 'level';

    SELECT COUNT(*) INTO remaining_count
    FROM players
    WHERE NOT (
        stats::jsonb ? 'strength' AND
        stats::jsonb ? 'dexterity' AND
        stats::jsonb ? 'constitution' AND
        stats::jsonb ? 'intelligence' AND
        stats::jsonb ? 'wisdom' AND
        stats::jsonb ? 'charisma' AND
        stats::jsonb ? 'sanity'
    );

    RAISE NOTICE 'Fixed % rows with nested stats structure', fixed_count;

    IF remaining_count > 0 THEN
        RAISE WARNING '% rows still have incorrect stats structure', remaining_count;
    ELSE
        RAISE NOTICE 'All stats structures are now correct';
    END IF;
END $$;

COMMIT;
