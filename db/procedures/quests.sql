-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f quests.sql
--
-- Quest instance procedures (the player registry's quests part) and quest definition procedures
-- (QuestDefinitionRepository). Depends on players (quest_instances FK).

-- list_quest_instances_by_player: every quest instance of one player, in any state. The player registry loads them
-- with the rest of the player (ADR-029 step 5a); ordering for the quest log happens in memory.
CREATE OR REPLACE FUNCTION :schema_name.list_quest_instances_by_player(p_player_id UUID) -- noqa: PRS
RETURNS TABLE (
    id uuid,
    player_id uuid,
    quest_id text,
    state text,
    progress jsonb,
    accepted_at timestamp with time zone,
    completed_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        qi.id,
        qi.player_id,
        qi.quest_id,
        qi.state,
        qi.progress,
        qi.accepted_at,
        qi.completed_at
    FROM quest_instances qi
    WHERE qi.player_id = p_player_id;
END;
$$;


-- upsert_quest_instance: the player registry's quest write (ADR-029 step 5a). Inserts the instance or sets every
-- mutable column of the player's existing instance of that quest (a player holds at most one per quest). The id
-- comes from the registry, so a new instance is known before it commits.
CREATE OR REPLACE PROCEDURE :schema_name.upsert_quest_instance(
    p_id UUID,
    p_player_id UUID,
    p_quest_id TEXT,
    p_state TEXT,
    p_progress JSONB,
    p_accepted_at TIMESTAMP WITH TIME ZONE,
    p_completed_at TIMESTAMP WITH TIME ZONE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO quest_instances (id, player_id, quest_id, state, progress, accepted_at, completed_at)
    VALUES (
        p_id, p_player_id, p_quest_id, p_state, COALESCE(p_progress, '{}'::jsonb),
        COALESCE(p_accepted_at, now()), p_completed_at
    )
    ON CONFLICT (player_id, quest_id) DO UPDATE SET
        state = EXCLUDED.state,
        progress = EXCLUDED.progress,
        completed_at = EXCLUDED.completed_at;
END;
$$;


-- get_quest_definition_by_id: fetch quest definition by id
CREATE OR REPLACE FUNCTION :schema_name.get_quest_definition_by_id(p_quest_id TEXT) -- noqa: PRS
RETURNS TABLE (
    id text,
    definition jsonb,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        qd.id,
        qd.definition,
        qd.created_at,
        qd.updated_at
    FROM quest_definitions qd
    WHERE qd.id = p_quest_id;
END;
$$;


-- get_quest_definition_by_name: fetch by definition->>'name' (case-sensitive)
CREATE OR REPLACE FUNCTION :schema_name.get_quest_definition_by_name(p_name TEXT) -- noqa: PRS
RETURNS TABLE (
    id text,
    definition jsonb,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        qd.id,
        qd.definition,
        qd.created_at,
        qd.updated_at
    FROM quest_definitions qd
    WHERE qd.definition->>'name' = p_name;
END;
$$;


-- list_quest_ids_offered_by: return quest IDs offered by entity (npc or room)
CREATE OR REPLACE FUNCTION :schema_name.list_quest_ids_offered_by( -- noqa: PRS
    p_entity_type TEXT,
    p_entity_id TEXT
)
RETURNS TABLE (quest_id text)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT qo.quest_id
    FROM quest_offers qo
    WHERE qo.offer_entity_type = p_entity_type
      AND qo.offer_entity_id = p_entity_id;
END;
$$;
