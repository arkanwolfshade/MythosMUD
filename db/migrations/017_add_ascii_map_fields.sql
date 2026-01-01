-- Migration: Add ASCII map fields to rooms table
-- Date: 2025-01-01
-- Description: Adds map_origin_zone, map_symbol, and map_style columns for ASCII map system

-- Add map_origin_zone column (marks origin room for coordinate system)
ALTER TABLE rooms
ADD COLUMN IF NOT EXISTS map_origin_zone BOOLEAN NOT NULL DEFAULT FALSE;

-- Add map_symbol column (admin-configurable ASCII symbol)
ALTER TABLE rooms
ADD COLUMN IF NOT EXISTS map_symbol TEXT;

-- Add map_style column (style override: 'world', 'city', 'interior', etc.)
ALTER TABLE rooms
ADD COLUMN IF NOT EXISTS map_style TEXT;

-- Add comments to document the columns
COMMENT ON COLUMN rooms.map_origin_zone IS 'Marks this room as the origin for coordinate generation in its zone/subzone. Only one room per zone/subzone should be marked.';
COMMENT ON COLUMN rooms.map_symbol IS 'Admin-configurable ASCII symbol for this room on the map. If NULL, symbol is auto-assigned based on environment/type.';
COMMENT ON COLUMN rooms.map_style IS 'Style override for map rendering (e.g., "world", "city", "interior"). If NULL, style is determined from environment.';

-- Create index on map_origin_zone for faster lookups
CREATE INDEX IF NOT EXISTS idx_rooms_map_origin_zone ON rooms(map_origin_zone) WHERE map_origin_zone = TRUE;
