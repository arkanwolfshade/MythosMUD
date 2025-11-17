-- Fix player_id column type in dependent tables
-- These tables were created with UUID player_id but should be VARCHAR(255) to match players table

SET client_min_messages = WARNING;
SET search_path = public;

BEGIN;

-- List of tables that reference players.player_id
-- These should all have player_id as VARCHAR(255), not UUID

DO $$
DECLARE
    table_name_var text;
    current_type text;
    tables_to_fix text[] := ARRAY[
        'player_inventories',
        'player_sanity',
        'sanity_adjustment_log',
        'sanity_exposure_state',
        'sanity_cooldowns'
    ];
BEGIN
    FOREACH table_name_var IN ARRAY tables_to_fix
    LOOP
        -- Check if table exists
        IF EXISTS (
            SELECT 1 FROM information_schema.tables
            WHERE table_schema = 'public' AND table_name = table_name_var
        ) THEN
            -- Check current type of player_id column
            SELECT data_type INTO current_type
            FROM information_schema.columns
            WHERE table_schema = 'public'
                AND table_name = table_name_var
                AND column_name = 'player_id';

            IF current_type = 'uuid' THEN
                RAISE NOTICE 'Fixing %: converting player_id from UUID to VARCHAR(255)', table_name_var;

                -- Drop foreign key constraint if it exists
                EXECUTE format('ALTER TABLE %I DROP CONSTRAINT IF EXISTS %I_player_id_fkey',
                    table_name_var, table_name_var);

                -- Drop any indexes that might depend on the column
                -- (PostgreSQL will recreate them automatically if needed)

                -- Convert column type
                -- First, we need to convert UUID values to text
                -- Since player_id in players is now VARCHAR, we need to match those values
                EXECUTE format('
                    ALTER TABLE %I
                    ALTER COLUMN player_id TYPE varchar(255)
                    USING player_id::text
                ', table_name_var);

                -- Re-add foreign key constraint
                EXECUTE format('
                    ALTER TABLE %I
                    ADD CONSTRAINT %I_player_id_fkey
                    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
                ', table_name_var, table_name_var);

                RAISE NOTICE 'Fixed %', table_name_var;
            ELSIF current_type IS NULL THEN
                RAISE NOTICE 'Table % does not have player_id column (skipping)', table_name_var;
            ELSE
                RAISE NOTICE 'Table % already has player_id as % (no change needed)', table_name_var, current_type;
            END IF;
        ELSE
            RAISE NOTICE 'Table % does not exist (will be created with correct schema)', table_name_var;
        END IF;
    END LOOP;
END $$;

COMMIT;
