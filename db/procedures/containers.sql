-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f containers.sql
--
-- Suppress NOTICEs (e.g. "function does not exist, skipping") so apply script does not fail on stderr.
SET client_min_messages = WARNING;
--
-- Container procedures and functions for MythosMUD.
-- Moved from DDL files: add_item_to_container, clear_container_contents,
-- get_container_contents_json, remove_item_from_container.
-- Also: fetch_container_items, get_container, create_container, update_container,
-- delete_container, get_containers_by_room_id, get_containers_by_entity_id,
-- get_decayed_containers.

-- Drop all get_container overloads in any user schema so return type can change (same session).
DO $$
DECLARE
  r record;
BEGIN
  FOR r IN
    SELECT n.nspname, p.proname, pg_get_function_identity_arguments(p.oid) AS args
    FROM pg_proc p
    JOIN pg_namespace n ON p.pronamespace = n.oid
    WHERE p.proname = 'get_container'
      AND n.nspname NOT IN ('pg_catalog', 'information_schema')
  LOOP
    EXECUTE format('DROP FUNCTION IF EXISTS %I.%I(%s) CASCADE', r.nspname, r.proname, r.args);
  END LOOP;
END $$;
-- Static drop in case DO block missed (e.g. schema name); exact signature.
DROP FUNCTION IF EXISTS :schema_name.get_container(uuid); -- noqa: PRS
DROP FUNCTION IF EXISTS public.get_container(uuid);

-- add_item_to_container: insert or update item in container (moved from DDL)
CREATE OR REPLACE FUNCTION :schema_name.add_item_to_container( -- noqa: PRS
    p_container_id uuid,
    p_item_instance_id character varying,
    p_position integer DEFAULT NULL::integer
) RETURNS void AS $$
DECLARE
    v_max_position integer;
BEGIN
    IF p_position IS NULL THEN
        SELECT COALESCE(MAX("position"), -1) + 1
        INTO v_max_position
        FROM container_contents
        WHERE container_id = p_container_id;
    ELSE
        v_max_position := p_position;
    END IF;

    INSERT INTO container_contents (container_id, item_instance_id, "position")
    VALUES (p_container_id, p_item_instance_id, v_max_position)
    ON CONFLICT (container_id, item_instance_id)
    DO UPDATE SET "position" = v_max_position, updated_at = NOW();
END;
$$ LANGUAGE plpgsql;


-- clear_container_contents: delete all items from container (moved from DDL)
CREATE OR REPLACE FUNCTION :schema_name.clear_container_contents(p_container_id uuid) -- noqa: PRS
RETURNS integer AS $$
DECLARE
    v_deleted integer;
BEGIN
    DELETE FROM container_contents
    WHERE container_id = p_container_id;

    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RETURN v_deleted;
END;
$$ LANGUAGE plpgsql;


-- get_container_contents_json: return items as JSONB (moved from DDL)
CREATE OR REPLACE FUNCTION :schema_name.get_container_contents_json(p_container_id uuid) -- noqa: PRS
RETURNS jsonb AS $$
DECLARE
    v_result jsonb;
BEGIN
    SELECT COALESCE(
        jsonb_agg(
            jsonb_build_object(
                'item_instance_id', cc.item_instance_id,
                'item_id', ii.prototype_id,
                'item_name', COALESCE(ii.custom_name, ip.name),
                'quantity', ii.quantity,
                'condition', ii.condition,
                'metadata', ii.metadata,
                'position', cc."position"
            )
            ORDER BY cc."position"
        ),
        '[]'::jsonb
    )
    INTO v_result
    FROM container_contents cc
    JOIN item_instances ii ON cc.item_instance_id = ii.item_instance_id
    JOIN item_prototypes ip ON ii.prototype_id = ip.prototype_id
    WHERE cc.container_id = p_container_id;

    RETURN v_result;
END;
$$ LANGUAGE plpgsql;


-- remove_item_from_container: delete one item from container (moved from DDL)
CREATE OR REPLACE FUNCTION :schema_name.remove_item_from_container( -- noqa: PRS
    p_container_id uuid,
    p_item_instance_id character varying
) RETURNS boolean AS $$
DECLARE
    v_deleted integer;
BEGIN
    DELETE FROM container_contents
    WHERE container_id = p_container_id
      AND item_instance_id = p_item_instance_id;

    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RETURN v_deleted > 0;
END;
$$ LANGUAGE plpgsql;


-- fetch_container_items: return item rows for a container (replaces raw SELECT)
CREATE OR REPLACE FUNCTION :schema_name.fetch_container_items(p_container_id uuid) -- noqa: PRS
RETURNS TABLE (
    item_instance_id character varying,
    item_id character varying,
    item_name text,
    quantity integer,
    condition integer,
    metadata jsonb,
    "position" integer
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        cc.item_instance_id::character varying,
        ii.prototype_id::character varying AS item_id,
        COALESCE(ii.custom_name, ip.name)::text AS item_name,
        ii.quantity,
        ii.condition,
        ii.metadata,
        cc."position"
    FROM container_contents cc
    JOIN item_instances ii ON cc.item_instance_id = ii.item_instance_id
    JOIN item_prototypes ip ON ii.prototype_id = ip.prototype_id
    WHERE cc.container_id = p_container_id
    ORDER BY cc.position;
END;
$$ LANGUAGE plpgsql;


-- get_container: single container row by id (replaces raw SELECT)
CREATE OR REPLACE FUNCTION :schema_name.get_container(p_container_id uuid) -- noqa: PRS
RETURNS TABLE (
    container_instance_id uuid,
    source_type text,
    owner_id uuid,
    room_id character varying,
    entity_id uuid,
    lock_state text,
    capacity_slots integer,
    weight_limit integer,
    decay_at timestamp with time zone,
    allowed_roles jsonb,
    metadata_json jsonb,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    container_item_instance_id character varying
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.container_instance_id,
        c.source_type,
        c.owner_id,
        c.room_id,
        c.entity_id,
        c.lock_state,
        c.capacity_slots,
        c.weight_limit,
        c.decay_at,
        c.allowed_roles,
        c.metadata_json,
        c.created_at,
        c.updated_at,
        c.container_item_instance_id
    FROM containers c
    WHERE c.container_instance_id = p_container_id;
END;
$$ LANGUAGE plpgsql;


-- create_container: INSERT container, return id and timestamps
CREATE OR REPLACE FUNCTION :schema_name.create_container( -- noqa: PRS
    p_source_type text,
    p_owner_id uuid,
    p_room_id character varying,
    p_entity_id uuid,
    p_lock_state text,
    p_capacity_slots integer,
    p_weight_limit integer,
    p_decay_at timestamp with time zone,
    p_allowed_roles jsonb,
    p_metadata_json jsonb,
    p_container_item_instance_id character varying
) RETURNS TABLE (
    container_instance_id uuid,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
) AS $$
BEGIN
    RETURN QUERY
    INSERT INTO containers (
        source_type, owner_id, room_id, entity_id, lock_state,
        capacity_slots, weight_limit, decay_at, allowed_roles,
        metadata_json, container_item_instance_id, created_at, updated_at
    ) VALUES (
        p_source_type, p_owner_id, p_room_id, p_entity_id, p_lock_state,
        p_capacity_slots, p_weight_limit, p_decay_at, p_allowed_roles,
        p_metadata_json, p_container_item_instance_id, NOW(), NOW()
    )
    RETURNING
        containers.container_instance_id,
        containers.created_at,
        containers.updated_at;
END;
$$ LANGUAGE plpgsql;


-- update_container: update lock_state and/or metadata_json
CREATE OR REPLACE FUNCTION :schema_name.update_container( -- noqa: PRS
    p_container_id uuid,
    p_lock_state text,
    p_metadata_json jsonb
) RETURNS void AS $$
BEGIN
    UPDATE containers
    SET
        updated_at = NOW(),
        lock_state = COALESCE(p_lock_state, lock_state),
        metadata_json = COALESCE(p_metadata_json, metadata_json)
    WHERE container_instance_id = p_container_id;
END;
$$ LANGUAGE plpgsql;


-- delete_container: delete by id, return true if row deleted
CREATE OR REPLACE FUNCTION :schema_name.delete_container(p_container_id uuid) -- noqa: PRS
RETURNS boolean AS $$
DECLARE
    v_deleted integer;
BEGIN
    DELETE FROM containers
    WHERE container_instance_id = p_container_id;

    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RETURN v_deleted > 0;
END;
$$ LANGUAGE plpgsql;


-- get_containers_by_room_id: containers in a room
CREATE OR REPLACE FUNCTION :schema_name.get_containers_by_room_id(p_room_id text) -- noqa: PRS
RETURNS TABLE (
    container_instance_id uuid,
    source_type text,
    owner_id uuid,
    room_id character varying,
    entity_id uuid,
    lock_state text,
    capacity_slots integer,
    weight_limit integer,
    decay_at timestamp with time zone,
    allowed_roles jsonb,
    metadata_json jsonb,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    container_item_instance_id character varying
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.container_instance_id,
        c.source_type,
        c.owner_id,
        c.room_id,
        c.entity_id,
        c.lock_state,
        c.capacity_slots,
        c.weight_limit,
        c.decay_at,
        c.allowed_roles,
        c.metadata_json,
        c.created_at,
        c.updated_at,
        c.container_item_instance_id
    FROM containers c
    WHERE c.room_id = p_room_id
    ORDER BY c.created_at;
END;
$$ LANGUAGE plpgsql;


-- get_containers_by_entity_id: containers owned by entity
CREATE OR REPLACE FUNCTION :schema_name.get_containers_by_entity_id(p_entity_id uuid) -- noqa: PRS
RETURNS TABLE (
    container_instance_id uuid,
    source_type text,
    owner_id uuid,
    room_id character varying,
    entity_id uuid,
    lock_state text,
    capacity_slots integer,
    weight_limit integer,
    decay_at timestamp with time zone,
    allowed_roles jsonb,
    metadata_json jsonb,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    container_item_instance_id character varying
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.container_instance_id,
        c.source_type,
        c.owner_id,
        c.room_id,
        c.entity_id,
        c.lock_state,
        c.capacity_slots,
        c.weight_limit,
        c.decay_at,
        c.allowed_roles,
        c.metadata_json,
        c.created_at,
        c.updated_at,
        c.container_item_instance_id
    FROM containers c
    WHERE c.entity_id = p_entity_id
    ORDER BY c.created_at;
END;
$$ LANGUAGE plpgsql;


-- get_decayed_containers: containers with decay_at < current_time
CREATE OR REPLACE FUNCTION :schema_name.get_decayed_containers(p_current_time timestamp with time zone) -- noqa: PRS
RETURNS TABLE (
    container_instance_id uuid,
    source_type text,
    owner_id uuid,
    room_id character varying,
    entity_id uuid,
    lock_state text,
    capacity_slots integer,
    weight_limit integer,
    decay_at timestamp with time zone,
    allowed_roles jsonb,
    metadata_json jsonb,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    container_item_instance_id character varying
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.container_instance_id,
        c.source_type,
        c.owner_id,
        c.room_id,
        c.entity_id,
        c.lock_state,
        c.capacity_slots,
        c.weight_limit,
        c.decay_at,
        c.allowed_roles,
        c.metadata_json,
        c.created_at,
        c.updated_at,
        c.container_item_instance_id
    FROM containers c
    WHERE c.decay_at IS NOT NULL AND c.decay_at < p_current_time
    ORDER BY c.decay_at;
END;
$$ LANGUAGE plpgsql;
