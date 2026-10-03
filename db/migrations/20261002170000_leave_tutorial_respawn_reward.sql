-- leave_the_tutorial: completing it moves the player's respawn to the Sanitarium Main Foyer
-- (new respawn_room reward), so nobody keeps respawning into the tutorial bedroom template.
--
-- Also fixes the existing XP reward, which was stored as {"type": "xp", "amount": 10}: the quest
-- service reads amounts from reward.config, so the top-level "amount" was ignored and the tutorial
-- never granted its XP.
--
-- Idempotent: sets the whole rewards array.

-- migrate:up
UPDATE quest_definitions
SET definition = JSONB_SET(
    definition,
    '{rewards}',
    '[{"type": "xp", "config": {"amount": 10}},
      {"type": "respawn_room", "config": {"room_id": "earth_arkhamcity_sanitarium_room_foyer_001"}}]'::jsonb
)
WHERE id = 'leave_the_tutorial';

-- migrate:down
UPDATE quest_definitions
SET definition = JSONB_SET(definition, '{rewards}', '[{"type": "xp", "amount": 10}]'::jsonb)
WHERE id = 'leave_the_tutorial';
