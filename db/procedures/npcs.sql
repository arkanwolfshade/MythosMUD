-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f npcs.sql
--
-- NPC definition and spawn rule procedures. Replaces ORM in NpcService.
-- Depends on subzones (npc_definitions.sub_zone_id).

-- get_npc_definitions: fetch all NPC definitions ordered by name, sub_zone_id
CREATE OR REPLACE FUNCTION :schema_name.get_npc_definitions() -- noqa: PRS
RETURNS TABLE (
    id bigint,
    name character varying(100),
    description text,
    npc_type character varying(20),
    sub_zone_id character varying(50),
    room_id character varying(50),
    required_npc boolean,
    max_population integer,
    spawn_probability real,
    base_stats text,
    behavior_config text,
    ai_integration_stub text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        nd.id,
        nd.name,
        nd.description,
        nd.npc_type,
        nd.sub_zone_id,
        nd.room_id,
        nd.required_npc,
        nd.max_population,
        nd.spawn_probability,
        nd.base_stats,
        nd.behavior_config,
        nd.ai_integration_stub,
        nd.created_at,
        nd.updated_at
    FROM npc_definitions nd
    ORDER BY nd.name, nd.sub_zone_id;
END;
$$;


-- get_npc_definition: fetch single NPC definition by id
CREATE OR REPLACE FUNCTION :schema_name.get_npc_definition(p_definition_id bigint) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    name character varying(100),
    description text,
    npc_type character varying(20),
    sub_zone_id character varying(50),
    room_id character varying(50),
    required_npc boolean,
    max_population integer,
    spawn_probability real,
    base_stats text,
    behavior_config text,
    ai_integration_stub text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        nd.id,
        nd.name,
        nd.description,
        nd.npc_type,
        nd.sub_zone_id,
        nd.room_id,
        nd.required_npc,
        nd.max_population,
        nd.spawn_probability,
        nd.base_stats,
        nd.behavior_config,
        nd.ai_integration_stub,
        nd.created_at,
        nd.updated_at
    FROM npc_definitions nd
    WHERE nd.id = p_definition_id;
END;
$$;


-- get_spawn_rules: fetch all NPC spawn rules
CREATE OR REPLACE FUNCTION :schema_name.get_spawn_rules() -- noqa: PRS
RETURNS TABLE (
    id bigint,
    npc_definition_id bigint,
    sub_zone_id character varying(50),
    min_population integer,
    max_population integer,
    spawn_conditions text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        nsr.id,
        nsr.npc_definition_id,
        nsr.sub_zone_id,
        nsr.min_population,
        nsr.max_population,
        nsr.spawn_conditions
    FROM npc_spawn_rules nsr
    ORDER BY nsr.sub_zone_id, nsr.min_population;
END;
$$;


-- get_spawn_rule: fetch single spawn rule by id
CREATE OR REPLACE FUNCTION :schema_name.get_spawn_rule(p_rule_id bigint) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    npc_definition_id bigint,
    sub_zone_id character varying(50),
    min_population integer,
    max_population integer,
    spawn_conditions text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        nsr.id,
        nsr.npc_definition_id,
        nsr.sub_zone_id,
        nsr.min_population,
        nsr.max_population,
        nsr.spawn_conditions
    FROM npc_spawn_rules nsr
    WHERE nsr.id = p_rule_id;
END;
$$;


-- create_npc_definition: insert NPC definition, return created row
CREATE OR REPLACE FUNCTION :schema_name.create_npc_definition( -- noqa: PRS
    p_name character varying,
    p_description text,
    p_npc_type character varying,
    p_sub_zone_id character varying,
    p_room_id character varying DEFAULT NULL,
    p_required_npc boolean DEFAULT false,
    p_max_population integer DEFAULT 1,
    p_spawn_probability real DEFAULT 1.0,
    p_base_stats text DEFAULT '{}',
    p_behavior_config text DEFAULT '{}',
    p_ai_integration_stub text DEFAULT '{}'
)
RETURNS TABLE (
    id bigint,
    name character varying(100),
    description text,
    npc_type character varying(20),
    sub_zone_id character varying(50),
    room_id character varying(50),
    required_npc boolean,
    max_population integer,
    spawn_probability real,
    base_stats text,
    behavior_config text,
    ai_integration_stub text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    INSERT INTO npc_definitions (
        name, description, npc_type, sub_zone_id, room_id,
        required_npc, max_population, spawn_probability,
        base_stats, behavior_config, ai_integration_stub
    )
    VALUES (
        p_name, p_description, p_npc_type, p_sub_zone_id, p_room_id,
        COALESCE(p_required_npc, false), COALESCE(p_max_population, 1),
        COALESCE(p_spawn_probability, 1.0),
        COALESCE(p_base_stats, '{}'), COALESCE(p_behavior_config, '{}'),
        COALESCE(p_ai_integration_stub, '{}')
    )
    RETURNING
        npc_definitions.id,
        npc_definitions.name,
        npc_definitions.description,
        npc_definitions.npc_type,
        npc_definitions.sub_zone_id,
        npc_definitions.room_id,
        npc_definitions.required_npc,
        npc_definitions.max_population,
        npc_definitions.spawn_probability,
        npc_definitions.base_stats,
        npc_definitions.behavior_config,
        npc_definitions.ai_integration_stub,
        npc_definitions.created_at,
        npc_definitions.updated_at;
END;
$$;


-- update_npc_definition: partial update by id (NULL params mean no change)
CREATE OR REPLACE FUNCTION :schema_name.update_npc_definition( -- noqa: PRS
    p_id bigint,
    p_name character varying DEFAULT NULL,
    p_description text DEFAULT NULL,
    p_npc_type character varying DEFAULT NULL,
    p_sub_zone_id character varying DEFAULT NULL,
    p_room_id character varying DEFAULT NULL,
    p_required_npc boolean DEFAULT NULL,
    p_max_population integer DEFAULT NULL,
    p_spawn_probability real DEFAULT NULL,
    p_base_stats text DEFAULT NULL,
    p_behavior_config text DEFAULT NULL,
    p_ai_integration_stub text DEFAULT NULL
)
RETURNS TABLE (
    id bigint,
    name character varying(100),
    description text,
    npc_type character varying(20),
    sub_zone_id character varying(50),
    room_id character varying(50),
    required_npc boolean,
    max_population integer,
    spawn_probability real,
    base_stats text,
    behavior_config text,
    ai_integration_stub text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    UPDATE npc_definitions nd
    SET
        name = COALESCE(p_name, nd.name),
        description = COALESCE(p_description, nd.description),
        npc_type = COALESCE(p_npc_type, nd.npc_type),
        sub_zone_id = COALESCE(p_sub_zone_id, nd.sub_zone_id),
        room_id = COALESCE(p_room_id, nd.room_id),
        required_npc = COALESCE(p_required_npc, nd.required_npc),
        max_population = COALESCE(p_max_population, nd.max_population),
        spawn_probability = COALESCE(p_spawn_probability, nd.spawn_probability),
        base_stats = COALESCE(p_base_stats, nd.base_stats),
        behavior_config = COALESCE(p_behavior_config, nd.behavior_config),
        ai_integration_stub = COALESCE(p_ai_integration_stub, nd.ai_integration_stub),
        updated_at = now()
    WHERE nd.id = p_id
    RETURNING
        nd.id, nd.name, nd.description, nd.npc_type, nd.sub_zone_id, nd.room_id,
        nd.required_npc, nd.max_population, nd.spawn_probability,
        nd.base_stats, nd.behavior_config, nd.ai_integration_stub,
        nd.created_at, nd.updated_at;
END;
$$;


-- delete_npc_definition: delete by id, return true if row deleted
CREATE OR REPLACE FUNCTION :schema_name.delete_npc_definition(p_id bigint) -- noqa: PRS
RETURNS boolean
LANGUAGE plpgsql
AS $$
DECLARE
    rows_deleted integer;
BEGIN
    DELETE FROM npc_definitions WHERE npc_definitions.id = p_id;
    GET DIAGNOSTICS rows_deleted = ROW_COUNT;
    RETURN rows_deleted > 0;
END;
$$;


-- create_spawn_rule: insert spawn rule, return created row
CREATE OR REPLACE FUNCTION :schema_name.create_spawn_rule( -- noqa: PRS
    p_npc_definition_id bigint,
    p_sub_zone_id character varying,
    p_min_population integer DEFAULT 0,
    p_max_population integer DEFAULT 999,
    p_spawn_conditions text DEFAULT '{}'
)
RETURNS TABLE (
    id bigint,
    npc_definition_id bigint,
    sub_zone_id character varying(50),
    min_population integer,
    max_population integer,
    spawn_conditions text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    INSERT INTO npc_spawn_rules (
        npc_definition_id, sub_zone_id, min_population, max_population, spawn_conditions
    )
    VALUES (
        p_npc_definition_id, p_sub_zone_id,
        COALESCE(p_min_population, 0), COALESCE(p_max_population, 999),
        COALESCE(p_spawn_conditions, '{}')
    )
    RETURNING
        npc_spawn_rules.id,
        npc_spawn_rules.npc_definition_id,
        npc_spawn_rules.sub_zone_id,
        npc_spawn_rules.min_population,
        npc_spawn_rules.max_population,
        npc_spawn_rules.spawn_conditions;
END;
$$;


-- delete_spawn_rule: delete by id, return true if row deleted
CREATE OR REPLACE FUNCTION :schema_name.delete_spawn_rule(p_id bigint) -- noqa: PRS
RETURNS boolean
LANGUAGE plpgsql
AS $$
DECLARE
    rows_deleted integer;
BEGIN
    DELETE FROM npc_spawn_rules WHERE npc_spawn_rules.id = p_id;
    GET DIAGNOSTICS rows_deleted = ROW_COUNT;
    RETURN rows_deleted > 0;
END;
$$;


-- get_npc_definitions_by_type: filter by npc_type
CREATE OR REPLACE FUNCTION :schema_name.get_npc_definitions_by_type(p_npc_type character varying) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    name character varying(100),
    description text,
    npc_type character varying(20),
    sub_zone_id character varying(50),
    room_id character varying(50),
    required_npc boolean,
    max_population integer,
    spawn_probability real,
    base_stats text,
    behavior_config text,
    ai_integration_stub text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        nd.id, nd.name, nd.description, nd.npc_type, nd.sub_zone_id, nd.room_id,
        nd.required_npc, nd.max_population, nd.spawn_probability,
        nd.base_stats, nd.behavior_config, nd.ai_integration_stub,
        nd.created_at, nd.updated_at
    FROM npc_definitions nd
    WHERE nd.npc_type = p_npc_type
    ORDER BY nd.name, nd.sub_zone_id;
END;
$$;


-- get_npc_definitions_by_sub_zone: filter by sub_zone_id
CREATE OR REPLACE FUNCTION :schema_name.get_npc_definitions_by_sub_zone(p_sub_zone_id character varying) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    name character varying(100),
    description text,
    npc_type character varying(20),
    sub_zone_id character varying(50),
    room_id character varying(50),
    required_npc boolean,
    max_population integer,
    spawn_probability real,
    base_stats text,
    behavior_config text,
    ai_integration_stub text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        nd.id, nd.name, nd.description, nd.npc_type, nd.sub_zone_id, nd.room_id,
        nd.required_npc, nd.max_population, nd.spawn_probability,
        nd.base_stats, nd.behavior_config, nd.ai_integration_stub,
        nd.created_at, nd.updated_at
    FROM npc_definitions nd
    WHERE nd.sub_zone_id = p_sub_zone_id
    ORDER BY nd.name;
END;
$$;


-- get_npc_system_statistics: aggregate counts for admin/stats
CREATE OR REPLACE FUNCTION :schema_name.get_npc_system_statistics() -- noqa: PRS
RETURNS TABLE (
    total_npc_definitions bigint,
    npc_definitions_by_type jsonb,
    total_spawn_rules bigint
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_by_type jsonb;
BEGIN
    SELECT jsonb_object_agg(npc_type, cnt)
    INTO v_by_type
    FROM (
        SELECT nd.npc_type, count(*)::bigint AS cnt
        FROM npc_definitions nd
        GROUP BY nd.npc_type
    ) t;
    RETURN QUERY
    SELECT
        (SELECT count(*)::bigint FROM npc_definitions),
        COALESCE(v_by_type, '{}'::jsonb),
        (SELECT count(*)::bigint FROM npc_spawn_rules);
END;
$$;
