-- Migration: Ensure zone_configurations only has zone-to-subzone mappings
-- Remove any zone-only entries (where subzone_id IS NULL)
-- Add NOT NULL constraint to subzone_id to prevent future zone-only entries

-- Delete zone-only entries
DELETE FROM zone_configurations WHERE subzone_id IS NULL;

-- Add NOT NULL constraint to subzone_id if it doesn't already exist
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns
               WHERE table_name = 'zone_configurations'
               AND column_name = 'subzone_id'
               AND is_nullable = 'YES') THEN
        ALTER TABLE zone_configurations ALTER COLUMN subzone_id SET NOT NULL;
    END IF;
END $$;

-- Ensure zone_id is also NOT NULL (should already be, but double-check)
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns
               WHERE table_name = 'zone_configurations'
               AND column_name = 'zone_id'
               AND is_nullable = 'YES') THEN
        ALTER TABLE zone_configurations ALTER COLUMN zone_id SET NOT NULL;
    END IF;
END $$;
