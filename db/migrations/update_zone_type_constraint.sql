-- Migration: Update zone_type constraint to include all actual zone types
-- This updates the constraint to allow 'death' and other zone types

-- Drop the existing constraint if it exists
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_zone_type_values'
        AND conrelid = 'zone_configurations'::regclass
    ) THEN
        ALTER TABLE zone_configurations DROP CONSTRAINT chk_zone_type_values;
    END IF;
END $$;

-- Add the updated constraint with all zone types
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_zone_type_values'
        AND conrelid = 'zone_configurations'::regclass
    ) THEN
        ALTER TABLE zone_configurations
        ADD CONSTRAINT chk_zone_type_values
        CHECK (zone_type IS NULL OR zone_type IN ('city', 'countryside', 'mountains', 'swamp', 'tundra', 'desert', 'death'));
    END IF;
END $$;
