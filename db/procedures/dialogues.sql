-- Dialogue definition procedures for MythosMUD (issue #583).
-- Table: dialogue_definitions (id, definition JSONB, npc_definition_id, timestamps).
-- :schema_name is replaced by apply_procedures.ps1.

-- list_dialogue_definitions: all dialogue rows
CREATE OR REPLACE FUNCTION :schema_name.list_dialogue_definitions() -- noqa: PRS
RETURNS TABLE (
    id text,
    definition jsonb,
    npc_definition_id bigint,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        dd.id,
        dd.definition,
        dd.npc_definition_id,
        dd.created_at,
        dd.updated_at
    FROM dialogue_definitions dd
    ORDER BY dd.id;
END;
$$;


-- get_dialogue_definition_by_id
CREATE OR REPLACE FUNCTION :schema_name.get_dialogue_definition_by_id(p_id TEXT) -- noqa: PRS
RETURNS TABLE (
    id text,
    definition jsonb,
    npc_definition_id bigint,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        dd.id,
        dd.definition,
        dd.npc_definition_id,
        dd.created_at,
        dd.updated_at
    FROM dialogue_definitions dd
    WHERE dd.id = p_id;
END;
$$;


-- get_dialogue_definition_by_npc_definition_id
CREATE OR REPLACE FUNCTION :schema_name.get_dialogue_definition_by_npc_definition_id( -- noqa: PRS
    p_npc_definition_id BIGINT
)
RETURNS TABLE (
    id text,
    definition jsonb,
    npc_definition_id bigint,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        dd.id,
        dd.definition,
        dd.npc_definition_id,
        dd.created_at,
        dd.updated_at
    FROM dialogue_definitions dd
    WHERE dd.npc_definition_id = p_npc_definition_id;
END;
$$;


-- upsert_dialogue_definition: insert or update by id
CREATE OR REPLACE FUNCTION :schema_name.upsert_dialogue_definition( -- noqa: PRS
    p_id TEXT,
    p_definition JSONB,
    p_npc_definition_id BIGINT DEFAULT NULL
)
RETURNS TABLE (
    id text,
    definition jsonb,
    npc_definition_id bigint,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    INSERT INTO dialogue_definitions AS dd (id, definition, npc_definition_id, created_at, updated_at)
    VALUES (p_id, p_definition, p_npc_definition_id, now(), now())
    ON CONFLICT ON CONSTRAINT dialogue_definitions_pkey DO UPDATE SET
        definition = EXCLUDED.definition,
        npc_definition_id = EXCLUDED.npc_definition_id,
        updated_at = now()
    RETURNING
        dd.id,
        dd.definition,
        dd.npc_definition_id,
        dd.created_at,
        dd.updated_at;
END;
$$;


-- delete_dialogue_definition: returns true if a row was deleted
CREATE OR REPLACE FUNCTION :schema_name.delete_dialogue_definition(p_id TEXT) -- noqa: PRS
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    DELETE FROM dialogue_definitions dd WHERE dd.id = p_id;
    GET DIAGNOSTICS deleted_count = ROW_COUNT;
    RETURN deleted_count > 0;
END;
$$;
