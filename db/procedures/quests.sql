-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f quests.sql
--
-- Quest instance and definition procedures. Replaces ORM in QuestInstanceRepository
-- and QuestDefinitionRepository. Depends on players (quest_instances FK).

-- create_quest_instance: insert new quest instance, return full row
CREATE OR REPLACE FUNCTION :schema_name.create_quest_instance( -- noqa: PRS
    p_player_id UUID,
    p_quest_id TEXT,
    p_state TEXT DEFAULT 'active',
    p_progress JSONB DEFAULT '{}'
)
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
    INSERT INTO quest_instances (player_id, quest_id, state, progress)
    VALUES (p_player_id, p_quest_id, p_state, COALESCE(p_progress, '{}'::jsonb))
    RETURNING
        quest_instances.id,
        quest_instances.player_id,
        quest_instances.quest_id,
        quest_instances.state,
        quest_instances.progress,
        quest_instances.accepted_at,
        quest_instances.completed_at;
END;
$$;


-- get_quest_instance_by_player_and_quest: fetch single instance (any state)
CREATE OR REPLACE FUNCTION :schema_name.get_quest_instance_by_player_and_quest( -- noqa: PRS
    p_player_id UUID,
    p_quest_id TEXT
)
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
    WHERE qi.player_id = p_player_id
      AND qi.quest_id = p_quest_id;
END;
$$;


-- update_quest_instance_state_and_progress: update state, progress, completed_at
CREATE OR REPLACE FUNCTION :schema_name.update_quest_instance_state_and_progress( -- noqa: PRS
    p_instance_id UUID,
    p_state TEXT DEFAULT NULL,
    p_progress JSONB DEFAULT NULL,
    p_completed_at timestamp with time zone DEFAULT NULL
)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE quest_instances
    SET
        state = COALESCE(p_state, state),
        progress = COALESCE(p_progress, progress),
        completed_at = COALESCE(p_completed_at, completed_at)
    WHERE quest_instances.id = p_instance_id;
END;
$$;


-- list_active_quest_instances_by_player: list active quests ordered by accepted_at
CREATE OR REPLACE FUNCTION :schema_name.list_active_quest_instances_by_player(p_player_id UUID) -- noqa: PRS
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
    WHERE qi.player_id = p_player_id
      AND qi.state = 'active'
    ORDER BY qi.accepted_at;
END;
$$;


-- list_completed_quest_instances_by_player: list completed quests ordered by completed_at desc
CREATE OR REPLACE FUNCTION :schema_name.list_completed_quest_instances_by_player(p_player_id UUID) -- noqa: PRS
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
    WHERE qi.player_id = p_player_id
      AND qi.state = 'completed'
    ORDER BY qi.completed_at DESC NULLS LAST;
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
