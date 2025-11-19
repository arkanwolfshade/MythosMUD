-- Migration: Add zone_type column to zone_configurations table
-- This migration adds the missing zone_type field that exists in zone_config.json files
-- zone_type is zone-specific and should be NULL for subzone configurations

-- Add zone_type column (nullable, since subzone configs don't have this field)
ALTER TABLE zone_configurations
ADD COLUMN IF NOT EXISTS zone_type TEXT;

-- Add CHECK constraint to validate zone_type values
-- zone_type can be NULL (for subzone configs) or one of the valid zone types
ALTER TABLE zone_configurations
ADD CONSTRAINT chk_zone_type_values
CHECK (zone_type IS NULL OR zone_type IN ('city', 'countryside', 'mountains', 'swamp', 'tundra', 'desert'));

-- Note: zone_type should only be populated for configuration_type = 'zone' rows
-- This is enforced at the application level, but could also be enforced with a trigger if needed
