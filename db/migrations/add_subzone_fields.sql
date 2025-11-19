-- Migration: Add environment, description, and special_rules columns to subzones table
-- This migration adds the missing fields that exist in subzone_config.json files

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'subzones' AND column_name = 'environment') THEN
        ALTER TABLE subzones ADD COLUMN environment text;
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'subzones' AND column_name = 'description') THEN
        ALTER TABLE subzones ADD COLUMN description text;
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'subzones' AND column_name = 'special_rules') THEN
        ALTER TABLE subzones ADD COLUMN special_rules jsonb DEFAULT '{}'::jsonb;
    END IF;
END $$;

-- Add CHECK constraint for environment values
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'chk_subzones_environment' AND conrelid = 'subzones'::regclass) THEN
        ALTER TABLE subzones
        ADD CONSTRAINT chk_subzones_environment
        CHECK (environment IS NULL OR environment IN ('indoors', 'outdoors', 'underwater', 'void'));
    END IF;
END $$;
