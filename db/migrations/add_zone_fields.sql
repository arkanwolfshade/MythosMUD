-- Migration: Add zone_type, environment, description, weather_patterns, and special_rules columns to zones table
-- This migration adds the missing fields that exist in zone_config.json files

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zones' AND column_name = 'zone_type') THEN
        ALTER TABLE zones ADD COLUMN zone_type text;
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zones' AND column_name = 'environment') THEN
        ALTER TABLE zones ADD COLUMN environment text;
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zones' AND column_name = 'description') THEN
        ALTER TABLE zones ADD COLUMN description text;
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zones' AND column_name = 'weather_patterns') THEN
        ALTER TABLE zones ADD COLUMN weather_patterns jsonb DEFAULT '[]'::jsonb;
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zones' AND column_name = 'special_rules') THEN
        ALTER TABLE zones ADD COLUMN special_rules jsonb DEFAULT '{}'::jsonb;
    END IF;
END $$;

-- Add CHECK constraint for zone_type values
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'chk_zones_zone_type' AND conrelid = 'zones'::regclass) THEN
        ALTER TABLE zones
        ADD CONSTRAINT chk_zones_zone_type
        CHECK (zone_type IS NULL OR zone_type IN ('city', 'countryside', 'mountains', 'swamp', 'tundra', 'desert', 'death'));
    END IF;
END $$;

-- Add CHECK constraint for environment values
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'chk_zones_environment' AND conrelid = 'zones'::regclass) THEN
        ALTER TABLE zones
        ADD CONSTRAINT chk_zones_environment
        CHECK (environment IS NULL OR environment IN ('indoors', 'outdoors', 'underwater', 'void'));
    END IF;
END $$;
