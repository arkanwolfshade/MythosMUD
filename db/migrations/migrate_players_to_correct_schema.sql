-- Migration: Align players table with SQLAlchemy model
-- This migration transforms the players table from the old schema to match
-- the schema defined in db/authoritative_schema.sql and server/models/player.py
--
-- OLD SCHEMA:
--   id uuid PRIMARY KEY
--   user_id uuid
--   name text
--   profession_id uuid
--   sanity_score integer
--   attributes jsonb
--   created_at timestamptz
--   updated_at timestamptz
--
-- NEW SCHEMA:
--   player_id varchar(255) PRIMARY KEY
--   user_id uuid NOT NULL UNIQUE REFERENCES users(id)
--   name varchar(50) NOT NULL UNIQUE
--   stats text NOT NULL
--   inventory text NOT NULL DEFAULT '[]'
--   status_effects text NOT NULL DEFAULT '[]'
--   current_room_id varchar(50) NOT NULL DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001'
--   respawn_room_id varchar(100) DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001'
--   experience_points integer NOT NULL DEFAULT 0
--   level integer NOT NULL DEFAULT 1
--   is_admin integer NOT NULL DEFAULT 0
--   profession_id integer REFERENCES professions(id)
--   created_at timestamptz NOT NULL DEFAULT now()
--   last_active timestamptz NOT NULL DEFAULT now()
SET client_min_messages = WARNING;
SET search_path = public;
-- Check if migration is needed before starting transaction
DO $$
DECLARE has_old_schema boolean;
has_new_schema boolean;
table_exists boolean;
BEGIN -- Check if players table exists
SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
            AND table_name = 'players'
    ) INTO table_exists;
IF NOT table_exists THEN RAISE NOTICE 'Players table does not exist. Schema should be created by db/authoritative_schema.sql';
RETURN;
END IF;
-- Check for new schema (player_id varchar)
SELECT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'players'
            AND column_name = 'player_id'
    ) INTO has_new_schema;
IF has_new_schema THEN RAISE NOTICE 'Players table already has correct schema (player_id exists). Migration not needed.';
RETURN;
END IF;
-- Check for old schema (id uuid)
SELECT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'players'
            AND column_name = 'id'
    ) INTO has_old_schema;
IF NOT has_old_schema THEN RAISE EXCEPTION 'Players table exists but has neither old (id) nor new (player_id) schema. Manual investigation required.';
END IF;
END $$;
BEGIN;
-- Double-check we still need to migrate (in case schema was fixed between checks)
DO $$
DECLARE has_new_schema boolean;
has_old_schema boolean;
BEGIN
SELECT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'players'
            AND column_name = 'player_id'
    ) INTO has_new_schema;
SELECT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'players'
            AND column_name = 'id'
    ) INTO has_old_schema;
IF has_new_schema
AND NOT has_old_schema THEN RAISE NOTICE 'Schema already correct. Skipping migration steps.';
-- Set a flag to skip migration (we'll check this in each step)
END IF;
END $$;
-- Step 2: Create backup table with old data (only if old schema exists)
DO $$
DECLARE has_old_schema boolean;
BEGIN
SELECT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'players'
            AND column_name = 'id'
    ) INTO has_old_schema;
IF has_old_schema THEN EXECUTE 'CREATE TABLE IF NOT EXISTS players_backup_migration AS SELECT * FROM players';
END IF;
END $$;
-- Step 3: Create new players table with correct schema (only if old schema exists)
DO $$
DECLARE has_old_schema boolean;
BEGIN
SELECT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'players'
            AND column_name = 'id'
    ) INTO has_old_schema;
IF has_old_schema THEN EXECUTE $sql$ CREATE TABLE players_new (
    player_id varchar(255) PRIMARY KEY,
    user_id uuid NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    name varchar(50) NOT NULL UNIQUE,
    stats text NOT NULL DEFAULT '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "position": "standing"}',
    inventory text NOT NULL DEFAULT '[]',
    status_effects text NOT NULL DEFAULT '[]',
    current_room_id varchar(50) NOT NULL DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001',
    respawn_room_id varchar(100) DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001',
    experience_points integer NOT NULL DEFAULT 0,
    level integer NOT NULL DEFAULT 1,
    is_admin integer NOT NULL DEFAULT 0,
    profession_id integer,
    created_at timestamptz NOT NULL DEFAULT now(),
    last_active timestamptz NOT NULL DEFAULT now()
) $sql$;
-- Ensure professions table exists and has correct structure before adding foreign key
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
        AND table_name = 'professions'
) THEN -- Create professions table if it doesn't exist
EXECUTE $sql$ CREATE TABLE IF NOT EXISTS professions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    flavor_text TEXT NOT NULL,
    stat_requirements TEXT NOT NULL DEFAULT '{}',
    mechanical_effects TEXT NOT NULL DEFAULT '{}',
    is_available BOOLEAN NOT NULL DEFAULT true
) $sql$;
END IF;
-- Only add foreign key if professions table has integer id column
IF EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'professions'
        AND column_name = 'id'
        AND data_type IN ('integer', 'bigint', 'smallint')
) THEN BEGIN EXECUTE 'ALTER TABLE players_new ADD CONSTRAINT players_new_profession_id_fkey FOREIGN KEY (profession_id) REFERENCES professions(id)';
EXCEPTION
WHEN duplicate_object THEN -- Constraint already exists, ignore
NULL;
WHEN OTHERS THEN -- Log the error but don't fail migration
RAISE NOTICE 'Could not add foreign key constraint to professions: %',
SQLERRM;
END;
ELSE RAISE NOTICE 'Professions table does not have integer id column, skipping foreign key constraint';
END IF;
END IF;
END $$;
-- Step 4: Migrate data from old schema to new schema (only if old schema exists)
DO $$
DECLARE has_old_schema boolean;
BEGIN
SELECT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'players'
            AND column_name = 'id'
    ) INTO has_old_schema;
IF has_old_schema THEN EXECUTE $sql$
INSERT INTO players_new (
        player_id,
        user_id,
        name,
        stats,
        inventory,
        status_effects,
        current_room_id,
        respawn_room_id,
        experience_points,
        level,
        is_admin,
        profession_id,
        created_at,
        last_active
    )
SELECT -- Convert uuid id to varchar player_id
    id::text AS player_id,
    user_id,
    name,
    -- Migrate attributes jsonb to stats text, merge sanity_score if present
    CASE
        WHEN attributes IS NOT NULL
        AND attributes != '{}'::jsonb THEN -- Merge attributes with sanity_score if it exists
        CASE
            WHEN sanity_score IS NOT NULL THEN (
                attributes || jsonb_build_object('sanity', sanity_score)
            )::text
            ELSE attributes::text
        END
        WHEN sanity_score IS NOT NULL THEN -- Create stats from sanity_score
        jsonb_build_object(
            'strength',
            10,
            'dexterity',
            10,
            'constitution',
            10,
            'intelligence',
            10,
            'wisdom',
            10,
            'charisma',
            10,
            'sanity',
            sanity_score,
            'occult_knowledge',
            0,
            'fear',
            0,
            'corruption',
            0,
            'cult_affiliation',
            0,
            'current_health',
            100,
            'position',
            'standing'
        )::text
        ELSE -- Default stats
        '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "position": "standing"}'
    END AS stats,
    '[]' AS inventory,
    -- Default, no migration path from old schema
    '[]' AS status_effects,
    -- Default, no migration path from old schema
    'earth_arkhamcity_sanitarium_room_foyer_001' AS current_room_id,
    -- Default, no migration path
    'earth_arkhamcity_sanitarium_room_foyer_001' AS respawn_room_id,
    -- Default, no migration path
    0 AS experience_points,
    -- Default, no migration path
    1 AS level,
    -- Default, no migration path
    0 AS is_admin,
    -- Default, no migration path
    -- Convert profession_id from uuid to integer if possible
    -- Since old schema has UUID and new schema has integer, set to NULL
    -- (UUID profession_ids cannot be automatically mapped to integer IDs)
    NULL::integer AS profession_id,
    created_at,
    COALESCE(updated_at, created_at) AS last_active
FROM players
WHERE user_id IS NOT NULL $sql$;
-- Only migrate valid players
ELSE RAISE NOTICE 'No old schema data to migrate. New table will be empty.';
END IF;
END $$;
-- Step 5: Create indexes on new table (only if it exists)
DO $$
DECLARE table_exists boolean;
BEGIN
SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
            AND table_name = 'players_new'
    ) INTO table_exists;
IF table_exists THEN CREATE INDEX IF NOT EXISTS idx_players_name_new ON players_new(name);
CREATE INDEX IF NOT EXISTS idx_players_user_id_new ON players_new(user_id);
CREATE INDEX IF NOT EXISTS idx_players_is_admin_new ON players_new(is_admin);
CREATE INDEX IF NOT EXISTS idx_players_profession_id_new ON players_new(profession_id);
END IF;
END $$;
-- Step 6: Drop old table and rename new table (only if we created players_new)
DO $$
DECLARE has_old_schema boolean;
table_exists boolean;
BEGIN -- Check if players_new exists (we created it)
SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
            AND table_name = 'players_new'
    ) INTO table_exists;
IF table_exists THEN -- Check if old players table still exists
SELECT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'players'
            AND column_name = 'id'
    ) INTO has_old_schema;
IF has_old_schema THEN DROP TABLE IF EXISTS players CASCADE;
END IF;
ALTER TABLE players_new
    RENAME TO players;
END IF;
END $$;
-- Step 7: Rename indexes to match standard naming
ALTER INDEX IF EXISTS idx_players_name_new
RENAME TO idx_players_name;
ALTER INDEX IF EXISTS idx_players_user_id_new
RENAME TO idx_players_user_id;
ALTER INDEX IF EXISTS idx_players_is_admin_new
RENAME TO idx_players_is_admin;
ALTER INDEX IF EXISTS idx_players_profession_id_new
RENAME TO idx_players_profession_id;
-- Step 8: Verify migration
DO $$
DECLARE row_count integer;
expected_columns text [];
actual_columns text [];
BEGIN -- Check row count
SELECT COUNT(*) INTO row_count
FROM players;
RAISE NOTICE 'Migration complete. Players table now has % rows.',
row_count;
-- Verify schema
SELECT array_agg(
        column_name
        ORDER BY ordinal_position
    ) INTO expected_columns
FROM information_schema.columns
WHERE table_schema = 'public'
    AND table_name = 'players';
RAISE NOTICE 'Players table columns: %',
array_to_string(expected_columns, ', ');
-- Verify player_id exists
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'players'
        AND column_name = 'player_id'
) THEN RAISE EXCEPTION 'Migration failed: player_id column not found after migration';
END IF;
-- Verify id column is gone
IF EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'players'
        AND column_name = 'id'
) THEN RAISE EXCEPTION 'Migration failed: old id column still exists';
END IF;
END $$;
COMMIT;
-- Note: The backup table players_backup_migration can be dropped after verifying the migration
-- DROP TABLE IF EXISTS players_backup_migration;
