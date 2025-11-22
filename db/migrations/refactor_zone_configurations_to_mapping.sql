-- Migration: Refactor zone_configurations to be a mapping table only
-- Remove all configuration fields - zones and subzones tables are now authoritative

-- Drop the old unique constraint that included configuration_type
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'zone_configurations_zone_id_subzone_id_configuration_type_key' AND conrelid = 'zone_configurations'::regclass) THEN
        ALTER TABLE zone_configurations DROP CONSTRAINT zone_configurations_zone_id_subzone_id_configuration_type_key;
    END IF;
END $$;

-- Drop configuration columns
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zone_configurations' AND column_name = 'configuration_type') THEN
        ALTER TABLE zone_configurations DROP COLUMN configuration_type;
    END IF;
END $$;

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zone_configurations' AND column_name = 'zone_type') THEN
        ALTER TABLE zone_configurations DROP COLUMN zone_type;
    END IF;
END $$;

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zone_configurations' AND column_name = 'environment') THEN
        ALTER TABLE zone_configurations DROP COLUMN environment;
    END IF;
END $$;

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zone_configurations' AND column_name = 'description') THEN
        ALTER TABLE zone_configurations DROP COLUMN description;
    END IF;
END $$;

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zone_configurations' AND column_name = 'weather_patterns') THEN
        ALTER TABLE zone_configurations DROP COLUMN weather_patterns;
    END IF;
END $$;

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'zone_configurations' AND column_name = 'special_rules') THEN
        ALTER TABLE zone_configurations DROP COLUMN special_rules;
    END IF;
END $$;

-- Add new unique constraint on (zone_id, subzone_id)
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'zone_configurations_zone_id_subzone_id_key' AND conrelid = 'zone_configurations'::regclass) THEN
        ALTER TABLE zone_configurations ADD CONSTRAINT zone_configurations_zone_id_subzone_id_key UNIQUE(zone_id, subzone_id);
    END IF;
END $$;
