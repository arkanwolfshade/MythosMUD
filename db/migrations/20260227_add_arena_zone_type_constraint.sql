-- Add 'arena' to zones.zone_type CHECK (Gladiator Ring).
-- Run with search_path set to target schema (mythos_unit, mythos_e2e, or mythos_dev).
-- Idempotent: safe to run multiple times.

ALTER TABLE zones DROP CONSTRAINT IF EXISTS chk_zones_zone_type;
ALTER TABLE zones ADD CONSTRAINT chk_zones_zone_type CHECK (
    (zone_type IS NULL) OR (zone_type = ANY(ARRAY[
        'city'::text, 'countryside'::text, 'mountains'::text,
        'swamp'::text, 'tundra'::text, 'desert'::text, 'death'::text, 'arena'::text
    ]))
);
