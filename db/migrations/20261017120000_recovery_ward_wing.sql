-- Sanitarium Recovery Ward wing (ADR-028, #1079).
--
-- A second-floor wing of the Arkham Sanitarium where players wake after delirium or a sanitarium failover: a recovery
-- ward and its annex, two corridors with exit signs, and a staircase down to the Main Foyer, where Dr. Morgan waits.
-- The wing is ordinary world content (not an instance). The map has no z axis, so the second floor sits at y = 7..8,
-- clear of the ground floor (y = -3..2).
--
-- Also gives Dr. Morgan (npc_definitions id 54) a dialogue tree whose nodes run the `debrief` scripted action:
-- the recap, with or without an immediate therapy session.
--
-- Idempotent: rooms and links are inserted only when missing, the foyer sentence is appended once, and the dialogue
-- is upserted, so replaying the migration against a database where a step already applied is safe.

-- migrate:up
INSERT INTO rooms (
    id, subzone_id, stable_id, name, description, attributes, map_x, map_y, map_origin_zone, map_symbol, map_style
)
SELECT
    GEN_RANDOM_UUID() AS id,
    s.id AS subzone_id,
    v.stable_id,
    v.name, -- noqa: RF04
    v.description,
    v.attributes::jsonb AS attributes,
    v.map_x,
    v.map_y,
    FALSE AS map_origin_zone,
    NULL AS map_symbol,
    'interior' AS map_style
FROM subzones AS s,
    (VALUES
        (
            'earth_arkhamcity_sanitarium_room_recovery_ward_001',
            'Recovery Ward',
            'A long, narrow ward of eight iron cots under a ceiling stained the colour of weak tea. '
            || 'Most of them are empty; the one you woke in still holds the shape of you. The sheets smell of '
            || 'carbolic and of something sweeter, like lilies left too long in water. Above the door, in the same '
            || 'flat institutional green as everything else, a small painted sign reads EXIT, with an arrow '
            || 'pointing south to the corridor.',
            '{"environment": "indoors", "rest_location": true}',
            102.00,
            7.00
        ),
        (
            'earth_arkhamcity_sanitarium_room_recovery_ward_002',
            'Recovery Ward Annex',
            'A smaller bay holding four cots, two of them occupied by patients who lie very still and watch '
            || 'the ceiling. A chart hangs at the foot of each bed, the handwriting on them drifting from neat to '
            || 'frantic and back again. Whatever the patients are looking at, it is not the plaster. A painted '
            || 'sign by the door points the way out: EXIT, and an arrow to the south.',
            '{"environment": "indoors", "rest_location": true}',
            101.00,
            7.00
        ),
        (
            'earth_arkhamcity_sanitarium_room_recovery_hall_001',
            'Recovery Wing Corridor',
            'A bare corridor of green-painted brick, lit by a single gas jet behind a wire cage that gutters '
            || 'when nothing is moving the air. The doors of the recovery ward stand on the north side. '
            || 'Stencilled on the wall in white paint: EXIT - STAIRS, with an arrow pointing west.',
            '{"environment": "indoors"}',
            102.00,
            8.00
        ),
        (
            'earth_arkhamcity_sanitarium_room_recovery_hall_002',
            'Recovery Wing Landing',
            'The corridor widens into a landing where the wing meets the main stair. A brass plate on the wall '
            || 'reads RECOVERY WING - QUIET, PLEASE; beneath it a hand-painted sign says EXIT - STAIRS - MAIN '
            || 'FLOOR, with a white arrow pointing west. The annex door is to the north.',
            '{"environment": "indoors"}',
            101.00,
            8.00
        ),
        (
            'earth_arkhamcity_sanitarium_room_main_staircase_001',
            'Main Staircase',
            'A broad staircase of worn marble with a cast-iron balustrade, descending to the foyer below. '
            || 'The treads are hollowed in the middle by decades of tired feet. A sign bolted to the newel post '
            || 'reads MAIN FLOOR - FOYER - EXIT, and from below you can hear the faint tick of the reception '
            || 'desk clock. The recovery wing lies to the east.',
            '{"environment": "indoors"}',
            100.00,
            8.00
        )
    ) AS v (stable_id, name, description, attributes, map_x, map_y)
WHERE
    s.stable_id = 'sanitarium'
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
        'earth_arkhamcity_sanitarium_room_recovery_ward_001', 'south',
        'earth_arkhamcity_sanitarium_room_recovery_hall_001'
    ),
    (
        'earth_arkhamcity_sanitarium_room_recovery_hall_001', 'north',
        'earth_arkhamcity_sanitarium_room_recovery_ward_001'
    ),
    (
        'earth_arkhamcity_sanitarium_room_recovery_ward_002', 'south',
        'earth_arkhamcity_sanitarium_room_recovery_hall_002'
    ),
    (
        'earth_arkhamcity_sanitarium_room_recovery_hall_002', 'north',
        'earth_arkhamcity_sanitarium_room_recovery_ward_002'
    ),
    (
        'earth_arkhamcity_sanitarium_room_recovery_hall_001', 'west',
        'earth_arkhamcity_sanitarium_room_recovery_hall_002'
    ),
    (
        'earth_arkhamcity_sanitarium_room_recovery_hall_002', 'east',
        'earth_arkhamcity_sanitarium_room_recovery_hall_001'
    ),
    (
        'earth_arkhamcity_sanitarium_room_recovery_hall_002', 'west',
        'earth_arkhamcity_sanitarium_room_main_staircase_001'
    ),
    (
        'earth_arkhamcity_sanitarium_room_main_staircase_001', 'east',
        'earth_arkhamcity_sanitarium_room_recovery_hall_002'
    ),
    (
        'earth_arkhamcity_sanitarium_room_main_staircase_001', 'down',
        'earth_arkhamcity_sanitarium_room_foyer_001'
    ),
    (
        'earth_arkhamcity_sanitarium_room_foyer_001', 'up',
        'earth_arkhamcity_sanitarium_room_main_staircase_001'
    )
) AS v (from_stable, direction, to_stable)
INNER JOIN rooms AS f ON v.from_stable = f.stable_id
INNER JOIN rooms AS t ON v.to_stable = t.stable_id
WHERE
    NOT EXISTS (
        SELECT 1 FROM room_links AS l
        WHERE l.from_room_id = f.id AND l.direction = v.direction
    );

UPDATE rooms
SET description = description || ' A staircase rises beside the reception desk.'
WHERE
    stable_id = 'earth_arkhamcity_sanitarium_room_foyer_001'
    AND description NOT LIKE '%A staircase rises beside the reception desk.%';

INSERT INTO dialogue_definitions (id, definition, npc_definition_id, created_at, updated_at)
VALUES (
    'morgan_debrief',
    $dialogue$
{"start": "greeting", "nodes": {
  "greeting": {
    "text": "Ah - upright, and lucid enough to stand. Good. The mind goes quiet after a spell like yours, and the body forgets it was ever frightened. Sit a moment, if you like. I can tell you what the records say of the last hours and, if you are willing, spend some time steadying you.",
    "options": [
      {"label": "Tell me what happened to me.", "next": "debrief"},
      {"label": "Tell me, and help me steady my mind.", "next": "debrief_therapy"},
      {"label": "Not now, doctor.", "next": null}
    ]
  },
  "debrief": {
    "text": "Then listen, and take your time with it.",
    "actions": [{"type": "debrief"}],
    "options": [{"label": "Thank you, doctor.", "next": null}]
  },
  "debrief_therapy": {
    "text": "Then we shall do both. Breathe. Keep your eyes on mine.",
    "actions": [{"type": "debrief", "therapy": true}],
    "options": [{"label": "Thank you, doctor.", "next": null}]
  }
}}
    $dialogue$::jsonb,
    54,
    NOW(),
    NOW()
)
ON CONFLICT (id) DO UPDATE SET
    definition = excluded.definition,
    npc_definition_id = excluded.npc_definition_id,
    updated_at = NOW();

-- migrate:down
DELETE FROM dialogue_definitions
WHERE id = 'morgan_debrief';

UPDATE rooms
SET description = REPLACE(description, ' A staircase rises beside the reception desk.', '')
WHERE stable_id = 'earth_arkhamcity_sanitarium_room_foyer_001';

-- room_links.to_room_id is ON DELETE RESTRICT, so every link into the wing (from its own rooms and the foyer's `up`)
-- must go before the rooms do; links out of a room would cascade, but both directions are removed here for clarity.
DELETE FROM room_links
WHERE
    from_room_id IN (
        SELECT id FROM rooms
        WHERE stable_id IN (
            'earth_arkhamcity_sanitarium_room_recovery_ward_001',
            'earth_arkhamcity_sanitarium_room_recovery_ward_002',
            'earth_arkhamcity_sanitarium_room_recovery_hall_001',
            'earth_arkhamcity_sanitarium_room_recovery_hall_002',
            'earth_arkhamcity_sanitarium_room_main_staircase_001'
        )
    )
    OR to_room_id IN (
        SELECT id FROM rooms
        WHERE stable_id IN (
            'earth_arkhamcity_sanitarium_room_recovery_ward_001',
            'earth_arkhamcity_sanitarium_room_recovery_ward_002',
            'earth_arkhamcity_sanitarium_room_recovery_hall_001',
            'earth_arkhamcity_sanitarium_room_recovery_hall_002',
            'earth_arkhamcity_sanitarium_room_main_staircase_001'
        )
    );

DELETE FROM rooms
WHERE stable_id IN (
    'earth_arkhamcity_sanitarium_room_recovery_ward_001',
    'earth_arkhamcity_sanitarium_room_recovery_ward_002',
    'earth_arkhamcity_sanitarium_room_recovery_hall_001',
    'earth_arkhamcity_sanitarium_room_recovery_hall_002',
    'earth_arkhamcity_sanitarium_room_main_staircase_001'
);
