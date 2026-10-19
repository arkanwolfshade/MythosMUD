-- First Exposure: the Pale Ghoul speaks first.
--
-- behavior_config.initiates_dialogue makes an NPC open its dialogue when a player enters its room, instead of
-- waiting for `talk <npc>` (NPCOpensDialogue). The tutorial's healer under the yew is the first to use it.
-- Mirrors data/npc_catalog (batch first_exposure). The tutorial migration now carries the flag too; this one brings
-- databases that ran it before the flag existed up to date, and is a no-op otherwise. behavior_config is JSON in text.

-- migrate:up
UPDATE npc_definitions
SET behavior_config = (behavior_config::jsonb || '{"initiates_dialogue": true}'::jsonb)::text
WHERE name = 'Pale Ghoul' AND sub_zone_id = 'arena';

-- migrate:down
UPDATE npc_definitions
SET behavior_config = (behavior_config::jsonb - 'initiates_dialogue')::text
WHERE name = 'Pale Ghoul' AND sub_zone_id = 'arena';
