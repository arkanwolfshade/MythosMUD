-- Migration 008: Increase current_room_id column length from VARCHAR(50) to VARCHAR(255)
-- Date: 2025-11-19
-- Description: Fix database error "value too long for type character varying(50)"
-- Room IDs like "earth_arkhamcity_sanitarium_room_foyer_entrance_001" are 54 characters
-- This migration increases the column size to 255 to accommodate hierarchical room IDs
-- As noted in the Pnakotic Manuscripts, proper dimensional mapping requires sufficient identifier space

DO $$
BEGIN
    -- Check if column exists and has the old length constraint
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'players'
            AND column_name = 'current_room_id'
            AND character_maximum_length = 50
    ) THEN
        RAISE NOTICE 'Migrating current_room_id column from VARCHAR(50) to VARCHAR(255)...';

        -- Alter the column to increase length
        ALTER TABLE players
        ALTER COLUMN current_room_id TYPE VARCHAR(255);

        RAISE NOTICE 'Successfully increased current_room_id column length to 255';
    ELSIF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'players'
            AND column_name = 'current_room_id'
            AND character_maximum_length >= 255
    ) THEN
        RAISE NOTICE 'current_room_id column is already VARCHAR(255) or larger, skipping migration';
    ELSE
        RAISE NOTICE 'current_room_id column not found or has unexpected type. Skipping migration.';
    END IF;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Migration failed: %', SQLERRM;
END $$;
