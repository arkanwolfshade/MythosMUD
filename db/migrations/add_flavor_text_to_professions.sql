-- Migration: Add flavor_text column to professions table if missing
-- Run this with: psql -d mythos_dev -f db/migrations/add_flavor_text_to_professions.sql

-- Check if column exists and add if missing
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'professions'
        AND column_name = 'flavor_text'
    ) THEN
        ALTER TABLE professions ADD COLUMN flavor_text TEXT NOT NULL DEFAULT '';
        RAISE NOTICE 'Added flavor_text column to professions table';

        -- Update existing rows with default flavor text
        UPDATE professions
        SET flavor_text = description
        WHERE flavor_text = '' OR flavor_text IS NULL;

        RAISE NOTICE 'Updated existing rows with default flavor text';
    ELSE
        RAISE NOTICE 'flavor_text column already exists in professions table';
    END IF;
END $$;
