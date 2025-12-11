-- Migration: Convert stats system to new stats structure
-- This migration wipes all players (not in production) and resets NPC stats to new CoC structure
-- Date: 2025-01-XX

SET client_min_messages = WARNING;
SET search_path = public;

BEGIN;

-- Wipe all players (not in production)
DELETE FROM players;

-- Reset all NPC stats to new stats structure
-- Convert hp/max_hp to determination_points/max_determination_points
-- Add new stats: size, power, education, luck, magic_points, max_magic_points
-- Remove old stats: fear, cult_affiliation
-- Rename: wisdom -> education, occult_knowledge -> occult
UPDATE npc_definitions
SET base_stats = (
    SELECT jsonb_build_object(
        'strength', COALESCE((stats_json->>'strength')::integer, 50),
        'dexterity', COALESCE((stats_json->>'dexterity')::integer, 50),
        'constitution', COALESCE((stats_json->>'constitution')::integer, 50),
        'size', COALESCE((stats_json->>'size')::integer, 50),
        'intelligence', COALESCE((stats_json->>'intelligence')::integer, 50),
        'power', COALESCE((stats_json->>'power')::integer, 50),
        'education', COALESCE((stats_json->>'education')::integer, (stats_json->>'wisdom')::integer, 50),
        'charisma', COALESCE((stats_json->>'charisma')::integer, 50),
        'luck', COALESCE((stats_json->>'luck')::integer, 50),

        -- Derived stats: DP and MP
        'determination_points', COALESCE((stats_json->>'determination_points')::integer, (stats_json->>'hp')::integer, 20),
        'max_determination_points', COALESCE(
            (stats_json->>'max_determination_points')::integer,
            (stats_json->>'max_hp')::integer,
            -- Calculate from CON + SIZ if available, otherwise default
            CASE
                WHEN (stats_json->>'constitution')::integer IS NOT NULL AND (stats_json->>'size')::integer IS NOT NULL
                THEN ((stats_json->>'constitution')::integer + (stats_json->>'size')::integer) / 5
                ELSE 20
            END
        ),
        'magic_points', COALESCE((stats_json->>'magic_points')::integer, 10),
        'max_magic_points', COALESCE(
            (stats_json->>'max_magic_points')::integer,
            -- Calculate from POW if available, otherwise default
            CASE
                WHEN (stats_json->>'power')::integer IS NOT NULL
                THEN CEIL((stats_json->>'power')::integer * 0.2)
                ELSE 10
            END
        ),

        -- Horror stats
        'occult', COALESCE((stats_json->>'occult')::integer, (stats_json->>'occult_knowledge')::integer, 0),
        'corruption', COALESCE((stats_json->>'corruption')::integer, 0),

        -- Keep xp_value if it exists
        'xp_value', COALESCE((stats_json->>'xp_value')::integer, 1)
    )::text
    FROM (SELECT base_stats::jsonb as stats_json) AS s
    WHERE base_stats IS NOT NULL AND base_stats != '{}'
)
WHERE base_stats IS NOT NULL AND base_stats != '{}';

-- For NPCs with empty or null base_stats, set defaults
UPDATE npc_definitions
SET base_stats = '{
    "strength": 50,
    "dexterity": 50,
    "constitution": 50,
    "size": 50,
    "intelligence": 50,
    "power": 50,
    "education": 50,
    "charisma": 50,
    "luck": 50,
    "determination_points": 20,
    "max_determination_points": 20,
    "magic_points": 10,
    "max_magic_points": 10,
    "occult": 0,
    "corruption": 0,
    "xp_value": 1
}'::jsonb::text
WHERE base_stats IS NULL OR base_stats = '{}';

COMMIT;
