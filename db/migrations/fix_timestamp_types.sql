-- Fix timestamp column types to use timezone-aware timestamps

SET client_min_messages = WARNING;
SET search_path = public;

BEGIN;

-- Convert created_at and last_active to timestamp with time zone
DO $$
DECLARE
    created_type text;
    last_active_type text;
BEGIN
    SELECT data_type INTO created_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'players'
        AND column_name = 'created_at';

    SELECT data_type INTO last_active_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'players'
        AND column_name = 'last_active';

    IF created_type = 'timestamp without time zone' THEN
        RAISE NOTICE 'Converting created_at to timestamp with time zone';
        ALTER TABLE players
        ALTER COLUMN created_at TYPE timestamp with time zone
        USING created_at AT TIME ZONE 'UTC';
    END IF;

    IF last_active_type = 'timestamp without time zone' THEN
        RAISE NOTICE 'Converting last_active to timestamp with time zone';
        ALTER TABLE players
        ALTER COLUMN last_active TYPE timestamp with time zone
        USING last_active AT TIME ZONE 'UTC';
    END IF;
END $$;

COMMIT;
