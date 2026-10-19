-- First Exposure: the 12-room instanced tutorial (ADR-028, #1080).
--
-- Replaces the one-room Patient Bedroom tutorial. Adds the items, NPC definitions, sub-zone, 12 template rooms and
-- their links, four quests (Dusk, Burying Ground, Below chained by quest triggers, and the Sanitarium epilogue,
-- which has no prerequisites and is started by the ending), and the dialogue trees. Dr. Morgan's debrief now also
-- records the epilogue's goal. Retires the bedroom template and the leave_the_tutorial quest.
--
-- Item and NPC rows are the reviewed output of data/item_catalog and data/npc_catalog (batch first_exposure) with
-- the schema prefix removed. NPC definitions are inert (no room, no spawn): rooms spawn them into an instance by name.
--
-- Idempotent where it can be: upserts for catalog rows, quests and dialogue; guarded inserts for the sub-zone, rooms
-- and links. `down` removes the new content but cannot recreate the retired bedroom or leave_the_tutorial.

-- migrate:up
-- noqa: disable=LT05
INSERT INTO item_prototypes (
    prototype_id,
    name,
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
    'quest.first_exposure.jade_amulet',
    'Jade Amulet',
    'a jade amulet on a tarnished chain',
    'A palm-sized disc of green jade, cold in a way the evening is not, carved with a ring of figures too small to make out and too many to count. The chain is silver gone black. Look at it too long and the carving seems to have rearranged itself while your attention was elsewhere. Whatever it is, it was taken from someone who wants it back.',
    'quest',
    0.3,
    0,
    NULL,
    '["QUEST_ITEM","INSTANCE_BOUND"]'::jsonb,
    '[]'::jsonb,
    '{"max_stack":1}'::jsonb,
    '{}'::jsonb,
    '[]'::jsonb,
    '{"catalog":{"namespace":"first_exposure","canonical_id":"quest.first_exposure.jade_amulet"}}'::jsonb,
    '["quest","first_exposure"]'::jsonb,
    NOW()
)
ON CONFLICT (prototype_id) DO UPDATE SET
    name = EXCLUDED.name,
    short_description = EXCLUDED.short_description,
    long_description = EXCLUDED.long_description,
    item_type = EXCLUDED.item_type,
    weight = EXCLUDED.weight,
    base_value = EXCLUDED.base_value,
    durability = EXCLUDED.durability,
    flags = EXCLUDED.flags,
    wear_slots = EXCLUDED.wear_slots,
    stacking_rules = EXCLUDED.stacking_rules,
    usage_restrictions = EXCLUDED.usage_restrictions,
    effect_components = EXCLUDED.effect_components,
    metadata = EXCLUDED.metadata,
    tags = EXCLUDED.tags;

INSERT INTO item_prototypes (
    prototype_id,
    name,
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
    'quest.first_exposure.arkham_advertiser',
    'Arkham Advertiser',
    'a folded copy of the Arkham Advertiser',
    'An evening edition of the Arkham Advertiser, folded to a column that someone has underlined twice in pencil. The paper is damp at the edges, as though it had lain a while on the grass.',
    'quest',
    0.1,
    0,
    NULL,
    '["INSTANCE_BOUND"]'::jsonb,
    '[]'::jsonb,
    '{"max_stack":1}'::jsonb,
    '{}'::jsonb,
    '[]'::jsonb,
    '{"readable":{"text":"ARKHAM ADVERTISER - Evening Edition\n\nGRAVES OPENED AGAIN IN THE OLD BURYING GROUND\nPolice Blame Stray Dogs\n\nFor the third time this month the sexton of the old burying ground has found graves opened from below. Constable Haskell attributes the damage to ''a pack of strays''; the sexton, who has kept the ground for thirty years, observes that strays do not take the brass plates from the headstones, nor close the earth neatly behind them.\n\nThe Selectmen urge residents not to walk the ground after dark and remind them that its gates are locked at dusk. The gates, the sexton adds, were found standing open this morning."},"catalog":{"namespace":"first_exposure","canonical_id":"quest.first_exposure.arkham_advertiser"}}'::jsonb,
    '["quest","first_exposure","readable"]'::jsonb,
    NOW()
)
ON CONFLICT (prototype_id) DO UPDATE SET
    name = EXCLUDED.name,
    short_description = EXCLUDED.short_description,
    long_description = EXCLUDED.long_description,
    item_type = EXCLUDED.item_type,
    weight = EXCLUDED.weight,
    base_value = EXCLUDED.base_value,
    durability = EXCLUDED.durability,
    flags = EXCLUDED.flags,
    wear_slots = EXCLUDED.wear_slots,
    stacking_rules = EXCLUDED.stacking_rules,
    usage_restrictions = EXCLUDED.usage_restrictions,
    effect_components = EXCLUDED.effect_components,
    metadata = EXCLUDED.metadata,
    tags = EXCLUDED.tags;

INSERT INTO item_prototypes (
    prototype_id,
    name,
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
    'furniture.first_exposure.stone_coffin',
    'Stone Coffin',
    'a stone coffin with its lid ajar',
    'A coffin of grey stone, far too large for any man, set into the floor like a hearth. The lid has been slid back a hand''s breadth; the darkness inside is the dry, patient dark of something that has been waiting a very long time. A shallow dish worn into the lip seems made to receive an offering.',
    'container',
    900.0,
    0,
    NULL,
    '[]'::jsonb,
    '[]'::jsonb,
    '{}'::jsonb,
    '{}'::jsonb,
    '[]'::jsonb,
    '{"container":{"capacity_slots":10,"lock_state":"unlocked"},"catalog":{"namespace":"furniture","canonical_id":"furniture.first_exposure.stone_coffin"}}'::jsonb,
    '["furniture","first_exposure","container"]'::jsonb,
    NOW()
)
ON CONFLICT (prototype_id) DO UPDATE SET
    name = EXCLUDED.name,
    short_description = EXCLUDED.short_description,
    long_description = EXCLUDED.long_description,
    item_type = EXCLUDED.item_type,
    weight = EXCLUDED.weight,
    base_value = EXCLUDED.base_value,
    durability = EXCLUDED.durability,
    flags = EXCLUDED.flags,
    wear_slots = EXCLUDED.wear_slots,
    stacking_rules = EXCLUDED.stacking_rules,
    usage_restrictions = EXCLUDED.usage_restrictions,
    effect_components = EXCLUDED.effect_components,
    metadata = EXCLUDED.metadata,
    tags = EXCLUDED.tags;

INSERT INTO npc_definitions (
    name,
    description,
    npc_type,
    sub_zone_id,
    room_id,
    required_npc,
    max_population,
    spawn_probability,
    base_stats,
    behavior_config,
    ai_integration_stub,
    created_at,
    updated_at
) VALUES (
    'Lamplighter',
    'A stooped man in a patched coat, carrying a long brass-tipped pole and a tin of oil. He lights each gaslamp as though apologising to it.',
    'passive_mob',
    'arena',
    NULL,
    FALSE,
    0,
    0.0,
    '{"determination_points":30,"max_dp":30,"xp_value":0,"strength":40,"constitution":45,"size":50,"dexterity":50,"intelligence":55,"power":45,"catalog":{"namespace":"first_exposure","canonical_id":"first_exposure.npc.lamplighter","era":"1920s","source_key":"first_exposure_original"}}',
    '{"attack_damage":1,"aggression_level":"passive"}',
    '{}',
    NOW(),
    NOW()
)
ON CONFLICT (name, sub_zone_id) DO UPDATE SET
    description = EXCLUDED.description,
    npc_type = EXCLUDED.npc_type,
    room_id = EXCLUDED.room_id,
    required_npc = EXCLUDED.required_npc,
    max_population = EXCLUDED.max_population,
    spawn_probability = EXCLUDED.spawn_probability,
    base_stats = EXCLUDED.base_stats,
    behavior_config = EXCLUDED.behavior_config,
    ai_integration_stub = EXCLUDED.ai_integration_stub,
    updated_at = NOW();

INSERT INTO npc_definitions (
    name,
    description,
    npc_type,
    sub_zone_id,
    room_id,
    required_npc,
    max_population,
    spawn_probability,
    base_stats,
    behavior_config,
    ai_integration_stub,
    created_at,
    updated_at
) VALUES (
    'Ragged Ghoul',
    'It crouches among the leaning stones on knuckles and the balls of its feet, a hunched grey shape with a hound''s jaw and a man''s long, clever hands. Earth falls from it when it moves.',
    'aggressive_mob',
    'arena',
    NULL,
    FALSE,
    0,
    0.0,
    '{"determination_points":150,"max_dp":150,"xp_value":0,"strength":70,"constitution":80,"size":60,"dexterity":55,"intelligence":50,"power":50,"catalog":{"namespace":"first_exposure","canonical_id":"first_exposure.npc.ragged_ghoul","era":"1920s","source_key":"first_exposure_original"},"attacks":[{"name":"claws","damage_expr":"2d6+8","skill":"brawl","skill_pct":60,"min_damage":10,"max_damage":20}],"armor":{"armor_points":0,"coverage":"none"}}',
    '{"attack_damage":15,"lucidity_category":"disturbing","disengage_at_target_dp_ratio":0.25,"disengage_line":"stops mid-lunge, tilts its head as if at a call you cannot hear, and drops into the earth between the stones.","aggression_level":"aggressive"}',
    '{}',
    NOW(),
    NOW()
)
ON CONFLICT (name, sub_zone_id) DO UPDATE SET
    description = EXCLUDED.description,
    npc_type = EXCLUDED.npc_type,
    room_id = EXCLUDED.room_id,
    required_npc = EXCLUDED.required_npc,
    max_population = EXCLUDED.max_population,
    spawn_probability = EXCLUDED.spawn_probability,
    base_stats = EXCLUDED.base_stats,
    behavior_config = EXCLUDED.behavior_config,
    ai_integration_stub = EXCLUDED.ai_integration_stub,
    updated_at = NOW();

INSERT INTO npc_definitions (
    name,
    description,
    npc_type,
    sub_zone_id,
    room_id,
    required_npc,
    max_population,
    spawn_probability,
    base_stats,
    behavior_config,
    ai_integration_stub,
    created_at,
    updated_at
) VALUES (
    'Pale Ghoul',
    'Once a man, by the cut of what remains of its coat. It sits among the roots of the old yew with its hands folded, patient and ruined, and watches you with eyes that have not entirely forgotten how to be kind.',
    'passive_mob',
    'arena',
    NULL,
    FALSE,
    0,
    0.0,
    '{"determination_points":80,"max_dp":80,"xp_value":0,"strength":60,"constitution":70,"size":55,"dexterity":45,"intelligence":70,"power":65,"catalog":{"namespace":"first_exposure","canonical_id":"first_exposure.npc.pale_ghoul","era":"1920s","source_key":"first_exposure_original"}}',
    '{"initiates_dialogue":true,"attack_damage":1,"aggression_level":"passive"}',
    '{}',
    NOW(),
    NOW()
)
ON CONFLICT (name, sub_zone_id) DO UPDATE SET
    description = EXCLUDED.description,
    npc_type = EXCLUDED.npc_type,
    room_id = EXCLUDED.room_id,
    required_npc = EXCLUDED.required_npc,
    max_population = EXCLUDED.max_population,
    spawn_probability = EXCLUDED.spawn_probability,
    base_stats = EXCLUDED.base_stats,
    behavior_config = EXCLUDED.behavior_config,
    ai_integration_stub = EXCLUDED.ai_integration_stub,
    updated_at = NOW();
-- noqa: enable=LT05

INSERT INTO subzones (id, zone_id, stable_id, name, environment, description, special_rules)
SELECT
    GEN_RANDOM_UUID() AS id,
    z.id AS zone_id,
    'first_exposure' AS stable_id,
    'first_exposure' AS name, -- noqa: RF04
    'outdoors' AS environment,
    'The grounds and burial vaults of a nightmare that visits each new arrival alone. '
    || 'Template rooms only: every player walks their own copy, and no passive lucidity or '
    || 'corruption flux touches it.' AS description,
    $rules$
{
  "combat_modifier": 1.0,
  "exploration_bonus": 1.0,
  "npc_spawn_modifier": 0.0,
  "access_requirements": [],
  "lucidity_drain_rate": 0,
  "corruption_rate": 0
}
$rules$::jsonb AS special_rules
FROM zones AS z
WHERE
    z.stable_id = 'earth/arkhamcity'
    AND NOT EXISTS (
        SELECT 1 FROM subzones AS s
        WHERE s.zone_id = z.id AND s.stable_id = 'first_exposure'
    );

WITH base AS (
    SELECT $base$
{
  "no_death": true,
  "no_combat": true,
  "is_instanced": true,
  "instance_template_id": "first_exposure",
  "instance_exit_room_id": "earth_arkhamcity_sanitarium_room_recovery_ward_001",
  "corruption_rate": 0
}
$base$::jsonb AS attrs
)

INSERT INTO rooms (
    id, subzone_id, stable_id, name, description, attributes, map_x, map_y, map_origin_zone, map_symbol, map_style
)
SELECT
    GEN_RANDOM_UUID() AS id,
    s.id AS subzone_id,
    v.stable_id,
    v.name, -- noqa: RF04
    v.description,
    b.attrs || v.extra::jsonb AS attributes,
    v.map_x,
    v.map_y,
    FALSE AS map_origin_zone,
    NULL AS map_symbol,
    v.map_style
FROM subzones AS s
CROSS JOIN base AS b
CROSS JOIN (VALUES
        (
            'earth_arkhamcity_first_exposure_room_independence_square_001',
            'Independence Square, at Dusk',
            'Independence Square at the end of a mild October day. The last of the light lies '
            || 'along the roofs of Arkham in bands of copper and rust, and the gaslamps along the '
            || 'paths have not yet been lit. Dry leaves skate across the flagstones. A few people '
            || 'hurry home with their collars turned up, glancing at the sky the way people do when '
            || 'they are not sure why. East, a gravel walk leads off beneath the trees.',
            $room$
{
  "environment": "outdoors",
  "instance_start": true
}
$room$,
            NULL::text,
            200.00,
            0.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_gravel_walk_001',
            'The Gravel Walk',
            'A gravel walk curves between ranks of old limes, their branches thick against the '
            || 'darkening sky. Iron lampposts stand at intervals; at the nearest, a stooped figure '
            || 'is reaching up with a long pole. The gravel crunches loudly underfoot in the hush. '
            || 'The square lies west; the walk continues east beneath the trees.',
            $room$
{
  "environment": "outdoors",
  "instance_npcs": [
    "Lamplighter"
  ]
}
$room$,
            NULL::text,
            201.00,
            0.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_beneath_the_limes_001',
            'Beneath the Limes',
            'The limes close overhead here and the dusk comes early under them. A bench sits '
            || 'beside the path with a newspaper abandoned on its slats, one corner lifted by the '
            || 'breeze. From the east comes a smell of turned earth. The walk runs back to the west.',
            $room$
{
  "environment": "outdoors",
  "items": [
    {
      "prototype_id": "quest.first_exposure.arkham_advertiser",
      "quantity": 1
    }
  ]
}
$room$,
            NULL::text,
            202.00,
            0.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_lane_off_the_square_001',
            'A Lane off the Square',
            'The walk gives out into a narrow lane between blank brick walls that seem to lean '
            || 'toward one another. Somewhere in the last hundred feet the lamps stopped being lit; '
            || 'the dark has a texture here, and the corners of the buildings do not quite meet at '
            || 'the angles you expect. Ahead, an iron gate stands in a stone wall. Behind you, the '
            || 'walk.',
            $room$
{
  "environment": "outdoors"
}
$room$,
            NULL::text,
            203.00,
            0.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_burying_ground_gate_001',
            'Old Arkham Burying Ground, Gate',
            'The gate of the old burying ground hangs open on one hinge, its padlock lying in the'
            || ' grass, the chain cut clean through. Beyond it the stones rise out of the dusk in '
            || 'rows, tilted like bad teeth. A cold that has nothing to do with the evening breathes'
            || ' out of the grounds. The lane lies behind you to the west.',
            $room$
{
  "environment": "outdoors"
}
$room$,
            NULL::text,
            204.00,
            0.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_leaning_stones_001',
            'Among the Leaning Stones',
            'The headstones lean here at every angle, their inscriptions worn to rumour. The '
            || 'earth between them has been dug and dug again into soft, dark mounds. Something grey'
            || ' is hunched on the nearest, absolutely still, and as you come out into the open it '
            || 'raises a long jaw and looks at you.',
            $room$
{
  "environment": "outdoors",
  "no_combat": false,
  "instance_npcs": [
    "Ragged Ghoul"
  ]
}
$room$,
            NULL::text,
            205.00,
            0.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_old_yew_001',
            'Beneath the Old Yew',
            'A great yew has split the wall of the burying ground with its roots, and under it '
            || 'the ground is bare and dry and strangely clean. Someone sits against the trunk with '
            || 'hands folded, or something that was someone. The air smells of wet stone and old '
            || 'wool, and the dusk is gentler here than elsewhere, as if the tree were keeping it.',
            $room$
{
  "environment": "outdoors",
  "instance_npcs": [
    "Pale Ghoul"
  ]
}
$room$,
            NULL::text,
            206.00,
            0.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_robbed_grave_001',
            'The Robbed Grave',
            'A grave stands open here, its slab levered aside and its earth thrown in a fan '
            || 'across the grass. The man in it is not one of the buried: he lies on his back in a '
            || 'good coat, boots toward the sky, and the set of his face says he saw whatever came '
            || 'up out of the dark before it took him. One fist is clenched shut over a chain, and '
            || 'between the fingers hangs a green glint. The yew is back to the west. To the south, '
            || 'a stair of worn stone drops into a mausoleum.',
            $room$
{
  "environment": "outdoors",
  "items": [
    {
      "prototype_id": "quest.first_exposure.jade_amulet",
      "quantity": 1
    }
  ]
}
$room$,
            NULL::text,
            207.00,
            0.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_mausoleum_stair_001',
            'Mausoleum Stair',
            'A mausoleum of black stone, its door long since torn from the hinges. Inside, a '
            || 'stair spirals down into a darkness that smells of earth and old bone. Above the '
            || 'arch, letters worn almost to nothing spell a warning or a welcome; it is hard to say'
            || ' which. The open grave lies to the north.',
            $room$
{
  "environment": "indoors",
  "exit_requirements": {
    "down": {
      "item": "quest.first_exposure.jade_amulet",
      "refusal": "Something in the dark below stirs, and a voice like a dry hinge says, 'Not with empty hands.' You find that your feet will not take the next step."
    }
  }
}
$room$,
            'interior',
            207.00,
            1.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_the_warrens_001',
            'The Warrens',
            'The stair gives onto a tunnel that was never dug by any tool: round-walled, smooth, '
            || 'polished by the passage of countless bodies. Side-passages open off it in the dark '
            || 'like the mouths of an enormous burrow. Through gaps in the rock you glimpse spaces '
            || 'that cannot possibly lie under Arkham, a violet sky, a plain of pale towers, and '
            || 'then the stone closes and they are gone. The way up is behind you; the tunnel '
            || 'continues east.',
            $room$
{
  "environment": "indoors"
}
$room$,
            'interior',
            207.00,
            3.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_charnel_gallery_001',
            'Charnel Gallery',
            'A long gallery whose walls are built of bones, and built with care: femurs laid in '
            || 'herringbone, skulls set in niches like saints, each course finished as a mason '
            || 'finishes a cornice. Whoever made this loved it. Small lamps of fat burn in the '
            || 'niches, and in their light the skulls seem to be listening. The warrens lie west; '
            || 'the gallery ends in a vault to the east.',
            $room$
{
  "environment": "indoors"
}
$room$,
            'interior',
            208.00,
            3.00
        ),
        (
            'earth_arkhamcity_first_exposure_room_vault_of_the_owner_001',
            'Vault of the Owner',
            'A circular vault under a dome of fitted stone. In its centre a stone coffin lies set'
            || ' into the floor, its lid ajar. The air is still and very old. There is nowhere else '
            || 'to go from here, and you feel with some certainty that you were expected.',
            $room$
{
  "environment": "indoors",
  "furniture": [
    {
      "prototype_id": "furniture.first_exposure.stone_coffin",
      "role": "coffin",
      "on_put": [
        {
          "item": "quest.first_exposure.jade_amulet",
          "actions": [
            {
              "type": "narrate",
              "text": "The amulet settles into the worn dish at the lip of the coffin, and the lid slides shut by itself without a sound. For a moment there is only the dry dark and your own pulse. Then, very far away and very deep, something begins to bay."
            },
            {
              "type": "apply_effect",
              "effect": {
                "type": "lucidity_drain_over_time",
                "instance_scoped": true,
                "rate": 1,
                "accelerate_every": 60,
                "accelerate_by": 1,
                "floor": -10,
                "grants_liabilities": false,
                "narration": [
                  {
                    "at": 4,
                    "text": "The baying is nearer. It has the dull, sorrowful note of a hound on a trail, and it is not coming from any direction a sound should."
                  },
                  {
                    "at": 15,
                    "text": "You realise the sound is following something. Then you realise what: you."
                  },
                  {
                    "at": 30,
                    "text": "The bones in the walls rattle in their niches. Your thoughts come loose and drift, and you catch yourself counting the skulls and getting a different number each time."
                  },
                  {
                    "at": 45,
                    "text": "Something shapes itself at the edge of your sight: a long, narrow, bat-winged shadow with a hound's patient head. When you turn, it is behind you."
                  },
                  {
                    "at": 60,
                    "text": "The baying fills the vault. You can no longer tell whether you are listening to it, or whether it is the sound your mind makes when it comes apart."
                  },
                  {
                    "at": 75,
                    "text": "It is here. It has always been here. You understand that you are not being hunted; you are being collected."
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  ]
}
$room$,
            'interior',
            209.00,
            3.00
        )
) AS v (stable_id, name, description, extra, map_style, map_x, map_y)
WHERE
    s.stable_id = 'first_exposure'
    AND NOT EXISTS (
        SELECT 1 FROM rooms AS r
        WHERE r.subzone_id = s.id AND r.stable_id = v.stable_id
    );

-- links
INSERT INTO room_links (id, from_room_id, to_room_id, direction, attributes)
SELECT
    GEN_RANDOM_UUID() AS id,
    f.id AS from_room_id,
    t.id AS to_room_id,
    v.direction,
    '{}'::jsonb AS attributes
FROM (VALUES
    (
        'earth_arkhamcity_first_exposure_room_independence_square_001', 'east',
        'earth_arkhamcity_first_exposure_room_gravel_walk_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_gravel_walk_001', 'west',
        'earth_arkhamcity_first_exposure_room_independence_square_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_gravel_walk_001', 'east',
        'earth_arkhamcity_first_exposure_room_beneath_the_limes_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_beneath_the_limes_001', 'west',
        'earth_arkhamcity_first_exposure_room_gravel_walk_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_beneath_the_limes_001', 'east',
        'earth_arkhamcity_first_exposure_room_lane_off_the_square_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_lane_off_the_square_001', 'west',
        'earth_arkhamcity_first_exposure_room_beneath_the_limes_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_lane_off_the_square_001', 'east',
        'earth_arkhamcity_first_exposure_room_burying_ground_gate_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_burying_ground_gate_001', 'west',
        'earth_arkhamcity_first_exposure_room_lane_off_the_square_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_burying_ground_gate_001', 'east',
        'earth_arkhamcity_first_exposure_room_leaning_stones_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_leaning_stones_001', 'west',
        'earth_arkhamcity_first_exposure_room_burying_ground_gate_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_leaning_stones_001', 'east',
        'earth_arkhamcity_first_exposure_room_old_yew_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_old_yew_001', 'west',
        'earth_arkhamcity_first_exposure_room_leaning_stones_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_old_yew_001', 'east',
        'earth_arkhamcity_first_exposure_room_robbed_grave_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_robbed_grave_001', 'west',
        'earth_arkhamcity_first_exposure_room_old_yew_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_robbed_grave_001', 'south',
        'earth_arkhamcity_first_exposure_room_mausoleum_stair_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_mausoleum_stair_001', 'north',
        'earth_arkhamcity_first_exposure_room_robbed_grave_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_mausoleum_stair_001', 'down',
        'earth_arkhamcity_first_exposure_room_the_warrens_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_the_warrens_001', 'up',
        'earth_arkhamcity_first_exposure_room_mausoleum_stair_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_the_warrens_001', 'east',
        'earth_arkhamcity_first_exposure_room_charnel_gallery_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_charnel_gallery_001', 'west',
        'earth_arkhamcity_first_exposure_room_the_warrens_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_charnel_gallery_001', 'east',
        'earth_arkhamcity_first_exposure_room_vault_of_the_owner_001'
    ),
    (
        'earth_arkhamcity_first_exposure_room_vault_of_the_owner_001', 'west',
        'earth_arkhamcity_first_exposure_room_charnel_gallery_001'
    )
) AS v (from_stable, direction, to_stable)
INNER JOIN rooms AS f ON v.from_stable = f.stable_id
INNER JOIN rooms AS t ON v.to_stable = t.stable_id
WHERE
    NOT EXISTS (
        SELECT 1 FROM room_links AS l
        WHERE l.from_room_id = f.id AND l.direction = v.direction
    );

-- quests
INSERT INTO quest_definitions (id, definition, created_at, updated_at)
VALUES (
    'first_exposure_dusk',
    $quest$
{
  "name": "first_exposure_dusk",
  "title": "An Evening Walk",
  "description": "Dusk is settling over Arkham, and something is wrong in the old burying ground. Learn what you can before you go in. Type 'look' to take in your surroundings. Follow the gravel walk east ('go east'), speak with the lamplighter ('talk lamplighter'), pick up the newspaper under the limes ('get advertiser') and read it ('read advertiser'). Then take the lane to the burying ground gate. Type 'journal' at any time to see this again.",
  "goals": [
    {
      "type": "complete_activity",
      "target": "cmd_look"
    },
    {
      "type": "complete_activity",
      "target": "cmd_talk"
    },
    {
      "type": "complete_activity",
      "target": "cmd_read"
    },
    {
      "type": "complete_activity",
      "target": "exit_earth_arkhamcity_first_exposure_room_lane_off_the_square_001"
    }
  ],
  "rewards": [
    {
      "type": "xp",
      "config": {
        "amount": 20
      }
    }
  ],
  "triggers": [
    {
      "type": "room",
      "entity_id": "earth_arkhamcity_first_exposure_room_independence_square_001"
    }
  ],
  "requires_all": [],
  "requires_any": [],
  "auto_complete": true,
  "turn_in_entities": []
}
$quest$::jsonb,
    NOW(),
    NOW()
)
ON CONFLICT (id) DO UPDATE SET
    definition = excluded.definition,
    updated_at = NOW();

INSERT INTO quest_definitions (id, definition, created_at, updated_at)
VALUES (
    'first_exposure_burying_ground',
    $quest$
{
  "name": "first_exposure_burying_ground",
  "title": "What the Robbers Stole",
  "description": "Something in the burying ground has hurt you, and something else has mended you. The pale creature beneath the yew wants back what grave robbers took from its kind. Speak with it ('talk ghoul', then 'talk 1' to accept its help, then 'talk 1' again to ask what it wants), then recover the jade amulet from the open grave ('get amulet').",
  "goals": [
    {
      "type": "complete_activity",
      "target": "cmd_talk"
    },
    {
      "type": "collect_n",
      "target": "quest.first_exposure.jade_amulet",
      "config": {
        "count": 1
      }
    }
  ],
  "rewards": [
    {
      "type": "xp",
      "config": {
        "amount": 30
      }
    }
  ],
  "triggers": [
    {
      "type": "quest",
      "entity_id": "first_exposure_dusk"
    }
  ],
  "requires_all": [
    "first_exposure_dusk"
  ],
  "requires_any": [],
  "auto_complete": true,
  "turn_in_entities": []
}
$quest$::jsonb,
    NOW(),
    NOW()
)
ON CONFLICT (id) DO UPDATE SET
    definition = excluded.definition,
    updated_at = NOW();

INSERT INTO quest_definitions (id, definition, created_at, updated_at)
VALUES (
    'first_exposure_below',
    $quest$
{
  "name": "first_exposure_below",
  "title": "Not With Empty Hands",
  "description": "The ghouls' Owner keeps a vault below the mausoleum, and its stair will not admit you without the amulet. Go south into the mausoleum, then down ('go south', 'go down'), follow the warrens east to the vault, and return the amulet: 'put amulet in coffin'. Be ready for what answers.",
  "goals": [
    {
      "type": "complete_activity",
      "target": "exit_earth_arkhamcity_first_exposure_room_mausoleum_stair_001"
    },
    {
      "type": "complete_activity",
      "target": "cmd_put"
    }
  ],
  "rewards": [
    {
      "type": "xp",
      "config": {
        "amount": 40
      }
    }
  ],
  "triggers": [
    {
      "type": "quest",
      "entity_id": "first_exposure_burying_ground"
    }
  ],
  "requires_all": [
    "first_exposure_burying_ground"
  ],
  "requires_any": [],
  "auto_complete": true,
  "turn_in_entities": []
}
$quest$::jsonb,
    NOW(),
    NOW()
)
ON CONFLICT (id) DO UPDATE SET
    definition = excluded.definition,
    updated_at = NOW();

INSERT INTO quest_definitions (id, definition, created_at, updated_at)
VALUES (
    'first_exposure_sanitarium',
    $quest$
{
  "name": "first_exposure_sanitarium",
  "title": "Debrief",
  "description": "You have woken in the Recovery Ward of the Arkham Sanitarium. Dr. Morgan will tell you what the records say. Follow the exit signs: go south, then west twice to the stair ('go south', 'go west', 'go west'), go down to the Main Foyer ('go down'), and speak with Dr. Morgan ('talk morgan').",
  "goals": [
    {
      "type": "complete_activity",
      "target": "first_exposure_debrief"
    }
  ],
  "rewards": [
    {
      "type": "xp",
      "config": {
        "amount": 50
      }
    },
    {
      "type": "respawn_room",
      "config": {
        "room_id": "earth_arkhamcity_sanitarium_room_foyer_001"
      }
    }
  ],
  "triggers": [],
  "requires_all": [],
  "requires_any": [],
  "auto_complete": true,
  "turn_in_entities": []
}
$quest$::jsonb,
    NOW(),
    NOW()
)
ON CONFLICT (id) DO UPDATE SET
    definition = excluded.definition,
    updated_at = NOW();

-- offers
INSERT INTO quest_offers (quest_id, offer_entity_type, offer_entity_id)
VALUES
    ('first_exposure_dusk', 'room', 'earth_arkhamcity_first_exposure_room_independence_square_001'),
    ('first_exposure_burying_ground', 'quest', 'first_exposure_dusk'),
    ('first_exposure_below', 'quest', 'first_exposure_burying_ground')
ON CONFLICT DO NOTHING;

-- dialogue
INSERT INTO dialogue_definitions (id, definition, npc_definition_id, created_at, updated_at)
SELECT
    'first_exposure_lamplighter' AS id,
    $dialogue$
{
  "start": "greeting",
  "nodes": {
    "greeting": {
      "text": "Evening to you. Mind the gravel, it is loud tonight. It always is, when the dogs are about.",
      "options": [
        {
          "label": "The dogs?",
          "next": "dogs"
        },
        {
          "label": "Goodnight.",
          "next": null
        }
      ]
    },
    "dogs": {
      "text": "Strays, the constable says, digging up the old ground. Strays! I have lit these lamps thirty years and never met a stray that kept a tidy hole. You will want to be out of the grounds by dark. Though if you must go, know that the lanes by the east gate do not stay lit for me any more. I stopped trying.",
      "options": [
        {
          "label": "Thank you.",
          "next": null
        }
      ]
    }
  }
}
$dialogue$::jsonb AS definition,
    n.id AS npc_definition_id,
    NOW() AS created_at,
    NOW() AS updated_at
FROM npc_definitions AS n
WHERE n.name = 'Lamplighter'
ON CONFLICT (id) DO UPDATE SET
    definition = excluded.definition,
    npc_definition_id = excluded.npc_definition_id,
    updated_at = NOW();

INSERT INTO dialogue_definitions (id, definition, npc_definition_id, created_at, updated_at)
SELECT
    'first_exposure_pale_ghoul' AS id,
    $dialogue$
{
  "start": "greeting",
  "nodes": {
    "greeting": {
      "text": "It lifts one hand, slowly, the way you would to a startled animal. 'Hurt,' it says, in a voice like dry paper. 'The Ragged One was hungry and has no manners left. Sit. I can mend that.'",
      "options": [
        {
          "label": "Please. Help me.",
          "next": "mend"
        },
        {
          "label": "Stay away from me.",
          "next": null
        }
      ]
    },
    "mend": {
      "text": "Your flesh I can mend. The crack behind your eyes, never. That is the price of seeing us, and it is paid once and kept. Do not look so. It is only the truth, and I am old enough to be kind about it.",
      "actions": [
        {
          "type": "narrate",
          "text": "Its long fingers close over your wrist, and warmth floods in like a drink taken too fast."
        },
        {
          "type": "apply_effect",
          "effect": {
            "type": "heal_over_time",
            "healing": 5,
            "duration": 15
          }
        },
        {
          "type": "corruption_at_least",
          "value": 1,
          "reason": "first_exposure"
        }
      ],
      "options": [
        {
          "label": "What do you want from me?",
          "next": "amulet"
        },
        {
          "label": "Thank you.",
          "next": null
        }
      ]
    },
    "amulet": {
      "text": "There was a man with a spade who thought a grave was a strongbox. He took a green stone from one of ours, and the Owner below wants it back. He is lying in the open grave to the east with his fist closed on it. Bring it down the stair to the Owner's vault and put it where it belongs. The stair will not let you pass with empty hands; that much I can promise you.",
      "options": [
        {
          "label": "I will bring it.",
          "next": null
        }
      ]
    }
  }
}
$dialogue$::jsonb AS definition,
    n.id AS npc_definition_id,
    NOW() AS created_at,
    NOW() AS updated_at
FROM npc_definitions AS n
WHERE n.name = 'Pale Ghoul'
ON CONFLICT (id) DO UPDATE SET
    definition = excluded.definition,
    npc_definition_id = excluded.npc_definition_id,
    updated_at = NOW();

UPDATE dialogue_definitions
SET
    definition = $dialogue$
{
  "start": "greeting",
  "nodes": {
    "greeting": {
      "text": "Ah - upright, and lucid enough to stand. Good. The mind goes quiet after a spell like yours, and the body forgets it was ever frightened. Sit a moment, if you like. I can tell you what the records say of the last hours and, if you are willing, spend some time steadying you.",
      "options": [
        {
          "label": "Tell me what happened to me.",
          "next": "debrief"
        },
        {
          "label": "Tell me, and help me steady my mind.",
          "next": "debrief_therapy"
        },
        {
          "label": "Not now, doctor.",
          "next": null
        }
      ]
    },
    "debrief": {
      "text": "Then listen, and take your time with it.",
      "actions": [
        {
          "type": "debrief"
        },
        {
          "type": "quest_activity",
          "target": "first_exposure_debrief"
        }
      ],
      "options": [
        {
          "label": "Thank you, doctor.",
          "next": null
        }
      ]
    },
    "debrief_therapy": {
      "text": "Then we shall do both. Breathe. Keep your eyes on mine.",
      "actions": [
        {
          "type": "debrief",
          "therapy": true
        },
        {
          "type": "quest_activity",
          "target": "first_exposure_debrief"
        }
      ],
      "options": [
        {
          "label": "Thank you, doctor.",
          "next": null
        }
      ]
    }
  }
}
$dialogue$::jsonb,
    updated_at = NOW()
WHERE id = 'morgan_debrief';

-- retire the old tutorial
DELETE FROM quest_definitions
WHERE id = 'leave_the_tutorial';

UPDATE players
SET current_room_id = 'earth_arkhamcity_sanitarium_room_recovery_ward_001'
WHERE current_room_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001';

UPDATE players
SET respawn_room_id = 'earth_arkhamcity_sanitarium_room_foyer_001'
WHERE respawn_room_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001';

DELETE FROM room_links
WHERE
    from_room_id IN (
        SELECT id FROM rooms
        WHERE stable_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001'
    )
    OR to_room_id IN (
        SELECT id FROM rooms
        WHERE stable_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001'
    );

DELETE FROM rooms
WHERE stable_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001';

-- migrate:down
-- Not restored: the retired Patient Bedroom template and the leave_the_tutorial quest.
UPDATE dialogue_definitions
SET
    definition = $dialogue$
{
  "start": "greeting",
  "nodes": {
    "greeting": {
      "text": "Ah - upright, and lucid enough to stand. Good. The mind goes quiet after a spell like yours, and the body forgets it was ever frightened. Sit a moment, if you like. I can tell you what the records say of the last hours and, if you are willing, spend some time steadying you.",
      "options": [
        {
          "label": "Tell me what happened to me.",
          "next": "debrief"
        },
        {
          "label": "Tell me, and help me steady my mind.",
          "next": "debrief_therapy"
        },
        {
          "label": "Not now, doctor.",
          "next": null
        }
      ]
    },
    "debrief": {
      "text": "Then listen, and take your time with it.",
      "actions": [
        {
          "type": "debrief"
        }
      ],
      "options": [
        {
          "label": "Thank you, doctor.",
          "next": null
        }
      ]
    },
    "debrief_therapy": {
      "text": "Then we shall do both. Breathe. Keep your eyes on mine.",
      "actions": [
        {
          "type": "debrief",
          "therapy": true
        }
      ],
      "options": [
        {
          "label": "Thank you, doctor.",
          "next": null
        }
      ]
    }
  }
}
$dialogue$::jsonb,
    updated_at = NOW()
WHERE id = 'morgan_debrief';

DELETE FROM dialogue_definitions
WHERE id IN ('first_exposure_lamplighter', 'first_exposure_pale_ghoul');

DELETE FROM quest_definitions
WHERE id IN (
    'first_exposure_dusk', 'first_exposure_burying_ground',
    'first_exposure_below', 'first_exposure_sanitarium'
);

-- room_links.to_room_id is ON DELETE RESTRICT, so links into the template rooms go before the rooms do.
DELETE FROM room_links
WHERE
    from_room_id IN (
        SELECT r.id FROM rooms AS r
        INNER JOIN subzones AS s ON r.subzone_id = s.id
        WHERE s.stable_id = 'first_exposure'
    )
    OR to_room_id IN (
        SELECT r.id FROM rooms AS r
        INNER JOIN subzones AS s ON r.subzone_id = s.id
        WHERE s.stable_id = 'first_exposure'
    );

DELETE FROM rooms
WHERE subzone_id IN (
    SELECT id FROM subzones
    WHERE stable_id = 'first_exposure'
);

DELETE FROM subzones
WHERE stable_id = 'first_exposure';

DELETE FROM npc_definitions
WHERE name IN ('Lamplighter', 'Ragged Ghoul', 'Pale Ghoul') AND sub_zone_id = 'arena';

-- The item prototypes are left in place: stacks minted from them may still exist.
