-- Migration 010: Migrate player_id from VARCHAR(255) to UUID
-- Date: 2025-01-XX
-- Description: Convert players.player_id and all dependent tables from VARCHAR(255) to UUID type
-- This migration implements the clean cutover to UUID type for player_id with no backward compatibility
-- Status: ✅ ACTIVE

SET client_min_messages = WARNING;
SET search_path = public;

BEGIN;

-- Step 1: Verify current state and prepare for migration
DO $$
DECLARE
    current_type text;
    table_name_var text;
    tables_to_migrate text[] := ARRAY[
        'player_inventories',
        'player_sanity',
        'sanity_adjustment_log',
        'sanity_exposure_state',
        'sanity_cooldowns',
        'player_channel_preferences'
    ];
BEGIN
    -- Check current type of players.player_id
    SELECT data_type INTO current_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'players'
        AND column_name = 'player_id';

    IF current_type = 'uuid' THEN
        RAISE NOTICE 'Players.player_id is already UUID type. Migration not needed.';
        RETURN;
    ELSIF current_type IS NULL THEN
        RAISE EXCEPTION 'Players table does not have player_id column. Manual investigation required.';
    ELSIF current_type NOT IN ('character varying', 'varchar', 'text') THEN
        RAISE EXCEPTION 'Players.player_id has unexpected type: %. Expected VARCHAR/TEXT. Manual investigation required.', current_type;
    END IF;

    RAISE NOTICE 'Starting migration: Converting player_id from % to UUID', current_type;

    -- Step 2: Drop foreign key constraints from dependent tables
    RAISE NOTICE 'Step 2: Dropping foreign key constraints from dependent tables...';
    FOREACH table_name_var IN ARRAY tables_to_migrate
    LOOP
        IF EXISTS (
            SELECT 1 FROM information_schema.tables
            WHERE table_schema = 'public' AND table_name = table_name_var
        ) THEN
            -- Drop foreign key constraint if it exists
            EXECUTE format('ALTER TABLE %I DROP CONSTRAINT IF EXISTS %I_player_id_fkey',
                table_name_var, table_name_var);
            EXECUTE format('ALTER TABLE %I DROP CONSTRAINT IF EXISTS fk_%I_player_id',
                table_name_var, table_name_var);
            RAISE NOTICE 'Dropped foreign key constraints from %', table_name_var;
        END IF;
    END LOOP;

    -- Step 3: Convert dependent tables first (before players table)
    RAISE NOTICE 'Step 3: Converting dependent tables to UUID...';
    FOREACH table_name_var IN ARRAY tables_to_migrate
    LOOP
        IF EXISTS (
            SELECT 1 FROM information_schema.tables
            WHERE table_schema = 'public' AND table_name = table_name_var
        ) THEN
            -- Check if table has player_id column
            IF EXISTS (
                SELECT 1 FROM information_schema.columns
                WHERE table_schema = 'public'
                    AND table_name = table_name_var
                    AND column_name = 'player_id'
            ) THEN
                -- Get current type
                SELECT data_type INTO current_type
                FROM information_schema.columns
                WHERE table_schema = 'public'
                    AND table_name = table_name_var
                    AND column_name = 'player_id';

                IF current_type IN ('character varying', 'varchar', 'text') THEN
                    RAISE NOTICE 'Converting %.player_id from % to UUID...', table_name_var, current_type;

                    -- Convert column type: VARCHAR -> UUID
                    -- PostgreSQL can convert valid UUID strings to UUID type
                    EXECUTE format('
                        ALTER TABLE %I
                        ALTER COLUMN player_id TYPE uuid
                        USING player_id::uuid
                    ', table_name_var);

                    RAISE NOTICE 'Successfully converted %.player_id to UUID', table_name_var;
                ELSIF current_type = 'uuid' THEN
                    RAISE NOTICE '%.player_id is already UUID (skipping)', table_name_var;
                ELSE
                    RAISE WARNING '%.player_id has unexpected type: % (skipping)', table_name_var, current_type;
                END IF;
            END IF;
        END IF;
    END LOOP;

    -- Step 4: Convert players.player_id to UUID
    RAISE NOTICE 'Step 4: Converting players.player_id to UUID...';

    -- Validate that all player_id values are valid UUIDs before conversion
    IF EXISTS (
        SELECT 1 FROM players
        WHERE player_id !~ '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    ) THEN
        RAISE EXCEPTION 'Found invalid UUID format in players.player_id. Cannot proceed with migration.';
    END IF;

    -- Convert players.player_id from VARCHAR to UUID
    ALTER TABLE players
    ALTER COLUMN player_id TYPE uuid
    USING player_id::uuid;

    RAISE NOTICE 'Successfully converted players.player_id to UUID';

    -- Step 5: Re-add foreign key constraints to dependent tables
    RAISE NOTICE 'Step 5: Re-adding foreign key constraints...';
    FOREACH table_name_var IN ARRAY tables_to_migrate
    LOOP
        IF EXISTS (
            SELECT 1 FROM information_schema.tables
            WHERE table_schema = 'public' AND table_name = table_name_var
        ) THEN
            IF EXISTS (
                SELECT 1 FROM information_schema.columns
                WHERE table_schema = 'public'
                    AND table_name = table_name_var
                    AND column_name = 'player_id'
            ) THEN
                -- Re-add foreign key constraint
                EXECUTE format('
                    ALTER TABLE %I
                    ADD CONSTRAINT %I_player_id_fkey
                    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
                ', table_name_var, table_name_var);

                RAISE NOTICE 'Re-added foreign key constraint to %', table_name_var;
            END IF;
        END IF;
    END LOOP;

    RAISE NOTICE 'Migration completed successfully: All player_id columns are now UUID type';
END $$;

COMMIT;
