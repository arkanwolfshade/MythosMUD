-- Tutorial bedroom leaks + Sanitarium lost-and-found chest.
--
-- 1. Raise the global container capacity ceiling from 20 to 200 slots (each container's real
--    size comes from its prototype; see MAX_CONTAINER_CAPACITY_SLOTS in server/models/container.py).
-- 2. Upsert the furniture.sanitarium.lost_and_found_chest prototype (generated from
--    data/item_catalog/catalog/furniture_sanitarium.json, `--batch furniture`).
-- 3. Place that chest in the Sanitarium Main Foyer via rooms.attributes.furniture; the server's
--    furniture loader creates the matching environment container at startup.
-- 4. Remove the foyer `up` exit into the tutorial bedroom. That room is an instance template and
--    must only be entered through per-player instances; the bedroom's own `down` link stays, as
--    instances remap it to their exit room.
--
-- Idempotent: safe to replay against a database where any step already applied.

-- migrate:up
ALTER TABLE containers DROP CONSTRAINT IF EXISTS containers_capacity_slots_check;
ALTER TABLE containers ADD CONSTRAINT containers_capacity_slots_check
CHECK (capacity_slots > 0 AND capacity_slots <= 200);

INSERT INTO item_prototypes (
    prototype_id,
    name, -- noqa: RF04
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags,
    created_at
) VALUES (
    'furniture.sanitarium.lost_and_found_chest',
    'Lost-and-Found Chest',
    'a battered lost-and-found chest',
    'A dented steamer trunk bolted to the foyer floor, its lid stenciled LOST PROPERTY in flaking '
    || 'institutional paint. Whatever patients leave behind in their rooms ends up here, and anyone '
    || 'may rummage through it.',
    'container',
    80.0,
    0,
    NULL,
    '[]'::jsonb,
    '[]'::jsonb,
    '{}'::jsonb,
    '{}'::jsonb,
    '[]'::jsonb,
    '{"container":{"capacity_slots":200,"lock_state":"unlocked"},'
    '"catalog":{"namespace":"furniture","canonical_id":"furniture.sanitarium.lost_and_found_chest"}}'::jsonb,
    '["furniture","sanitarium","container"]'::jsonb,
    NOW()
)
ON CONFLICT (prototype_id) DO UPDATE SET
    name = excluded.name,
    short_description = excluded.short_description,
    long_description = excluded.long_description,
    item_type = excluded.item_type,
    weight = excluded.weight,
    base_value = excluded.base_value,
    durability = excluded.durability,
    flags = excluded.flags,
    wear_slots = excluded.wear_slots,
    stacking_rules = excluded.stacking_rules,
    usage_restrictions = excluded.usage_restrictions,
    effect_components = excluded.effect_components,
    metadata = excluded.metadata,
    tags = excluded.tags;

UPDATE rooms
SET attributes = COALESCE(attributes, '{}'::jsonb) || JSONB_BUILD_OBJECT(
    'furniture',
    JSONB_BUILD_ARRAY(JSONB_BUILD_OBJECT(
        'prototype_id', 'furniture.sanitarium.lost_and_found_chest',
        'role', 'lost_and_found'
    ))
)
WHERE stable_id = 'earth_arkhamcity_sanitarium_room_foyer_001';

DELETE FROM room_links AS l
USING rooms AS f, rooms AS t
WHERE
    l.from_room_id = f.id
    AND l.to_room_id = t.id
    AND l.direction = 'up'
    AND f.stable_id = 'earth_arkhamcity_sanitarium_room_foyer_001'
    AND t.stable_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001';

-- migrate:down
INSERT INTO room_links (id, from_room_id, to_room_id, direction, attributes)
SELECT
    GEN_RANDOM_UUID() AS id,
    f.id AS from_room_id,
    t.id AS to_room_id,
    'up' AS direction,
    '{}'::jsonb AS attributes
FROM rooms AS f, rooms AS t
WHERE
    f.stable_id = 'earth_arkhamcity_sanitarium_room_foyer_001'
    AND t.stable_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001'
    AND NOT EXISTS (
        SELECT 1 FROM room_links AS l
        WHERE l.from_room_id = f.id AND l.to_room_id = t.id AND l.direction = 'up'
    );

UPDATE rooms
SET attributes = attributes - 'furniture'
WHERE stable_id = 'earth_arkhamcity_sanitarium_room_foyer_001';

-- The prototype is left in place: containers created from it may still reference it.

ALTER TABLE containers DROP CONSTRAINT IF EXISTS containers_capacity_slots_check;
ALTER TABLE containers ADD CONSTRAINT containers_capacity_slots_check
CHECK (capacity_slots > 0 AND capacity_slots <= 20);
