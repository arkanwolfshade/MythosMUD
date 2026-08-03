SET search_path TO mythos_dev;
SELECT id, npc_definition_id, definition->>'start' AS start
FROM upsert_dialogue_definition(
  'smoke_dialogue_test',
  '{"start":"greeting","nodes":{"greeting":{"text":"Hi","options":[]}}}'::jsonb,
  NULL
);
SELECT delete_dialogue_definition('smoke_dialogue_test');
