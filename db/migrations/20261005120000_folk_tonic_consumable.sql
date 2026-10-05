-- Folk tonic consumable (#870): the first item usable via /use.
--
-- 1. Upsert the consumable.folk_tonic prototype (generated from
--    data/item_catalog/catalog/consumables_sanitarium.json, `--batch consumables`). Its
--    component.lucidity_recovery effect is dispatched by server/game/items/item_effects.py.
-- 2. Declare one tonic as a startup room drop in the Sanitarium nurses' station via
--    rooms.attributes.items; server/services/room_item_seeder.py places it in the room's floor
--    drops at every server start (drops are in-memory, so the world restocks on restart).
--
-- Idempotent: safe to replay against a database where any step already applied.

-- migrate:up
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
    'consumable.folk_tonic',
    'Folk Tonic',
    'a stoppered bottle of folk tonic',
    'A squat brown bottle sealed with wax and a twist of string, its label long since rubbed away. '
    || 'The apothecaries of Arkham swear it steadies frayed nerves; the smell suggests it does so by '
    || 'sheer unpleasantness.',
    'consumable',
    0.3,
    15,
    NULL,
    '["CONSUMABLE"]'::jsonb,
    '[]'::jsonb,
    '{"max_stack":5}'::jsonb,
    '{}'::jsonb,
    '["component.lucidity_recovery"]'::jsonb,
    '{"lucidity_recovery":{"cooldown_key":"folk_tonic","lcd_delta":3,"cooldown_minutes":30},'
    '"catalog":{"namespace":"consumables","canonical_id":"consumable.folk_tonic"}}'::jsonb,
    '["consumable","tonic","lucidity"]'::jsonb,
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
    'items',
    JSONB_BUILD_ARRAY(JSONB_BUILD_OBJECT(
        'prototype_id', 'consumable.folk_tonic',
        'quantity', 1
    ))
)
WHERE stable_id = 'earth_arkhamcity_sanitarium_room_nurses_001';

-- migrate:down
UPDATE rooms
SET attributes = attributes - 'items'
WHERE stable_id = 'earth_arkhamcity_sanitarium_room_nurses_001';

-- The prototype is left in place: item instances may still reference it.
