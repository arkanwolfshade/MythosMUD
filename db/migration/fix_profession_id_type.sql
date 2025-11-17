-- Fix profession_id column type in players table
-- Change from UUID to INTEGER to match expected schema

SET client_min_messages = WARNING;
SET search_path = public;

BEGIN;

-- Check current type
DO $$
DECLARE
    current_type text;
BEGIN
    SELECT data_type INTO current_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'players'
        AND column_name = 'profession_id';

    IF current_type = 'uuid' THEN
        RAISE NOTICE 'Converting profession_id from UUID to INTEGER';

        -- Drop foreign key constraint if it exists
        ALTER TABLE players DROP CONSTRAINT IF EXISTS players_profession_id_fkey;

        -- Convert column type (set to NULL first since we can't convert UUID to integer)
        ALTER TABLE players ALTER COLUMN profession_id TYPE integer USING NULL;

        -- Re-add foreign key constraint if professions table exists with integer id
        IF EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_schema = 'public'
                AND table_name = 'professions'
                AND column_name = 'id'
                AND data_type IN ('integer', 'bigint', 'smallint')
        ) THEN
            ALTER TABLE players
            ADD CONSTRAINT players_profession_id_fkey
            FOREIGN KEY (profession_id) REFERENCES professions(id);
        END IF;

        RAISE NOTICE 'Conversion complete';
    ELSE
        RAISE NOTICE 'profession_id is already % (no conversion needed)', current_type;
    END IF;
END $$;

COMMIT;
