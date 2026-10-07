-- Player bank deposit boxes (#977): owner-only storage reached at Arkham Savings & Trust.
--
-- 1. Allow containers.source_type = 'bank' (one box per player, owner_id = the player, room_id NULL;
--    created lazily by server/services/bank_service.py).
-- 2. Unique index so a get-or-create race cannot give one player two boxes.
-- 3. The bank room (attributes.bank = true gates the bank/deposit/withdraw commands), reached by a
--    north exit from Main Street - Near Garrison Street, plus its banker NPC (atmosphere only:
--    banking does not depend on the banker being present).
--
-- World content normally lives in the data/ seed, but a seed only loads on first provisioning;
-- a migration also reaches databases that already exist. Every step is idempotent, and the room
-- steps quietly do nothing on a database that lacks the Main Street room (e.g. a minimal test seed).

-- migrate:up
ALTER TABLE containers DROP CONSTRAINT IF EXISTS containers_source_type_check;
ALTER TABLE containers ADD CONSTRAINT containers_source_type_check
CHECK (source_type IN ('environment', 'equipment', 'corpse', 'bank'));

CREATE UNIQUE INDEX IF NOT EXISTS uq_containers_bank_owner
ON containers (owner_id) WHERE source_type = 'bank';

INSERT INTO rooms (
    id, subzone_id, stable_id, name, description, attributes,
    map_x, map_y, map_origin_zone, map_symbol, map_style
)
SELECT
    'a8e3f1c4-5b2d-5c97-9e41-7d0b6f2a3c58'::uuid AS id,
    street.subzone_id,
    'earth_arkhamcity_downtown_room_arkham_savings_001' AS stable_id,
    'Arkham Savings & Trust' AS room_name,
    'A hushed banking hall of dark oak and brass grilles, where the tellers speak in lowered voices '
    || 'as though the money might overhear. Rows of numbered deposit boxes line the vault wall behind '
    || 'the clerk''s desk; each opens, the clerks insist, only to the name engraved upon it.' AS description,
    '{"environment": "indoors", "bank": true}'::jsonb AS attributes,
    10.00 AS map_x,
    19.00 AS map_y,
    false AS map_origin_zone,
    '#' AS map_symbol,
    'city' AS map_style
FROM rooms AS street
WHERE
    street.stable_id = 'earth_arkhamcity_downtown_room_main_st_006'
    AND NOT EXISTS (
        SELECT 1 FROM rooms AS r
        WHERE r.stable_id = 'earth_arkhamcity_downtown_room_arkham_savings_001'
    );

INSERT INTO room_links (id, from_room_id, to_room_id, direction, attributes)
SELECT
    GEN_RANDOM_UUID() AS id,
    f.id AS from_room_id,
    t.id AS to_room_id,
    'north' AS direction,
    '{}'::jsonb AS attributes
FROM rooms AS f, rooms AS t
WHERE
    f.stable_id = 'earth_arkhamcity_downtown_room_main_st_006'
    AND t.stable_id = 'earth_arkhamcity_downtown_room_arkham_savings_001'
    AND NOT EXISTS (
        SELECT 1 FROM room_links AS l
        WHERE l.from_room_id = f.id AND l.to_room_id = t.id AND l.direction = 'north'
    );

INSERT INTO room_links (id, from_room_id, to_room_id, direction, attributes)
SELECT
    GEN_RANDOM_UUID() AS id,
    f.id AS from_room_id,
    t.id AS to_room_id,
    'south' AS direction,
    '{}'::jsonb AS attributes
FROM rooms AS f, rooms AS t
WHERE
    f.stable_id = 'earth_arkhamcity_downtown_room_arkham_savings_001'
    AND t.stable_id = 'earth_arkhamcity_downtown_room_main_st_006'
    AND NOT EXISTS (
        SELECT 1 FROM room_links AS l
        WHERE l.from_room_id = f.id AND l.to_room_id = t.id AND l.direction = 'south'
    );

INSERT INTO npc_definitions (
    name, description, npc_type, sub_zone_id, room_id, required_npc,
    max_population, spawn_probability, base_stats, behavior_config, ai_integration_stub
)
SELECT
    'Josiah Fenwick' AS npc_name,
    'A precise, colourless clerk in a high collar who has never been seen to blink. He keeps the '
    || 'ledger of every box in the vault and, it is said, has never once misplaced a deposit - or a '
    || 'depositor.' AS description,
    'shopkeeper' AS npc_type,
    'downtown' AS sub_zone_id,
    'earth_arkhamcity_downtown_room_arkham_savings_001' AS room_id,
    true AS required_npc,
    1 AS max_population,
    1 AS spawn_probability,
    '{"health": 70, "lucidity": 60, "intelligence": 16, "charisma": 11, "strength": 8, "dexterity": 10}' AS base_stats,
    '{"shop_type": "bank", "greeting": "Your box is in order, as always.", '
    || '"farewell": "Arkham Savings & Trust thanks you for your continued confidence."}' AS behavior_config,
    '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_shopkeeper"}' AS ai_integration_stub
WHERE
    EXISTS (
        SELECT 1 FROM rooms AS r
        WHERE r.stable_id = 'earth_arkhamcity_downtown_room_arkham_savings_001'
    )
    AND NOT EXISTS (
        SELECT 1 FROM npc_definitions AS n
        WHERE n.name = 'Josiah Fenwick' AND n.room_id = 'earth_arkhamcity_downtown_room_arkham_savings_001'
    );

-- migrate:down
DELETE FROM npc_definitions
WHERE name = 'Josiah Fenwick' AND room_id = 'earth_arkhamcity_downtown_room_arkham_savings_001';

DELETE FROM room_links AS l
USING rooms AS r
WHERE
    r.stable_id = 'earth_arkhamcity_downtown_room_arkham_savings_001'
    AND (l.from_room_id = r.id OR l.to_room_id = r.id);

DELETE FROM rooms
WHERE stable_id = 'earth_arkhamcity_downtown_room_arkham_savings_001';

-- CONCURRENTLY cannot run inside dbmate's transaction, and this rollback block is never reached through
-- scripts/migrate.ps1 (it only exposes up/status), so the brief table lock is acceptable.
DROP INDEX IF EXISTS uq_containers_bank_owner; -- noqa: PG01

-- Deliberately no DELETE of bank containers: re-adding the narrower CHECK below fails while any
-- player still has a box, so a rollback can never silently destroy deposited items.
ALTER TABLE containers DROP CONSTRAINT IF EXISTS containers_source_type_check;
ALTER TABLE containers ADD CONSTRAINT containers_source_type_check
CHECK (source_type IN ('environment', 'equipment', 'corpse'));
