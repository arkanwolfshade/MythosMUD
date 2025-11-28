-- Migration 013: Add map_x and map_y columns to rooms table
-- Date: 2025-01-XX
-- Description: Add map_x and map_y columns to rooms table for admin layout positioning
-- These columns store the X and Y coordinates for room positions on the interactive map
-- Status: ✅ ACTIVE

SET client_min_messages = WARNING;
SET search_path = public;

BEGIN;

-- Add map_x column if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'rooms'
            AND column_name = 'map_x'
    ) THEN
        ALTER TABLE public.rooms
        ADD COLUMN map_x NUMERIC(10, 2) NULL;

        COMMENT ON COLUMN public.rooms.map_x IS
            'X coordinate for room position on the interactive map (admin layout). NULL if not set.';

        RAISE NOTICE 'Added map_x column to rooms table';
    ELSE
        RAISE NOTICE 'map_x column already exists in rooms table';
    END IF;
END $$;

-- Add map_y column if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'rooms'
            AND column_name = 'map_y'
    ) THEN
        ALTER TABLE public.rooms
        ADD COLUMN map_y NUMERIC(10, 2) NULL;

        COMMENT ON COLUMN public.rooms.map_y IS
            'Y coordinate for room position on the interactive map (admin layout). NULL if not set.';

        RAISE NOTICE 'Added map_y column to rooms table';
    ELSE
        RAISE NOTICE 'map_y column already exists in rooms table';
    END IF;
END $$;

-- Create index on (map_x, map_y) for efficient spatial queries
-- Only index non-null values since most rooms may not have coordinates initially
CREATE INDEX IF NOT EXISTS idx_rooms_map_coordinates
ON public.rooms(map_x, map_y)
WHERE map_x IS NOT NULL AND map_y IS NOT NULL;

COMMENT ON INDEX idx_rooms_map_coordinates IS
    'Index for efficient spatial queries on rooms with map coordinates';

COMMIT;
