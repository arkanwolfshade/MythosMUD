-- Migration: Add zone_type column to zone_configurations table (safe version)
-- This version checks if column/constraint already exists before adding

-- Add zone_type column if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'zone_configurations'
        AND column_name = 'zone_type'
    ) THEN
        ALTER TABLE zone_configurations ADD COLUMN zone_type TEXT;
    END IF;
END $$;

-- Add CHECK constraint if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'chk_zone_type_values'
    ) THEN
        ALTER TABLE zone_configurations
        ADD CONSTRAINT chk_zone_type_values
        CHECK (zone_type IS NULL OR zone_type IN ('city', 'countryside', 'mountains', 'swamp', 'tundra', 'desert'));
    END IF;
END $$;
