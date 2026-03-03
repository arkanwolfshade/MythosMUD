-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f items.sql
--
-- Item instance procedures and functions for MythosMUD.
-- Replaces raw SQL/ORM in item_instance_persistence_async and ItemRepository.

-- upsert_item_instance: insert or update item instance (ON CONFLICT DO UPDATE)
CREATE OR REPLACE FUNCTION :schema_name.upsert_item_instance( -- noqa: PRS
    p_item_instance_id character varying,
    p_prototype_id character varying,
    p_owner_type character varying DEFAULT 'room',
    p_owner_id character varying DEFAULT NULL,
    p_location_context character varying DEFAULT NULL,
    p_quantity integer DEFAULT 1,
    p_condition integer DEFAULT NULL,
    p_flags_override jsonb DEFAULT '[]',
    p_binding_state character varying DEFAULT NULL,
    p_attunement_state jsonb DEFAULT '{}',
    p_custom_name character varying DEFAULT NULL,
    p_metadata jsonb DEFAULT '{}',
    p_origin_source character varying DEFAULT NULL,
    p_origin_metadata jsonb DEFAULT '{}'
) RETURNS void AS $$
BEGIN
    INSERT INTO item_instances (
        item_instance_id,
        prototype_id,
        owner_type,
        owner_id,
        location_context,
        quantity,
        condition,
        flags_override,
        binding_state,
        attunement_state,
        custom_name,
        metadata,
        origin_source,
        origin_metadata,
        created_at,
        updated_at
    ) VALUES (
        p_item_instance_id,
        p_prototype_id,
        COALESCE(p_owner_type, 'room'),
        p_owner_id,
        p_location_context,
        COALESCE(p_quantity, 1),
        p_condition,
        COALESCE(p_flags_override, '[]'::jsonb),
        p_binding_state,
        COALESCE(p_attunement_state, '{}'::jsonb),
        p_custom_name,
        COALESCE(p_metadata, '{}'::jsonb),
        p_origin_source,
        COALESCE(p_origin_metadata, '{}'::jsonb),
        NOW(),
        NOW()
    )
    ON CONFLICT (item_instance_id) DO UPDATE SET
        prototype_id = EXCLUDED.prototype_id,
        owner_type = EXCLUDED.owner_type,
        owner_id = EXCLUDED.owner_id,
        location_context = EXCLUDED.location_context,
        quantity = EXCLUDED.quantity,
        condition = EXCLUDED.condition,
        flags_override = EXCLUDED.flags_override,
        binding_state = EXCLUDED.binding_state,
        attunement_state = EXCLUDED.attunement_state,
        custom_name = EXCLUDED.custom_name,
        metadata = EXCLUDED.metadata,
        origin_source = EXCLUDED.origin_source,
        origin_metadata = EXCLUDED.origin_metadata,
        updated_at = NOW();
END;
$$ LANGUAGE plpgsql;


-- item_instance_exists: return true if item instance exists
CREATE OR REPLACE FUNCTION :schema_name.item_instance_exists(p_item_instance_id character varying) -- noqa: PRS
RETURNS boolean AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1
        FROM item_instances
        WHERE item_instance_id = p_item_instance_id
    );
END;
$$ LANGUAGE plpgsql;


-- get_item_instance: return single item instance row by id (optional, for future use)
CREATE OR REPLACE FUNCTION :schema_name.get_item_instance(p_item_instance_id character varying) -- noqa: PRS
RETURNS TABLE (
    item_instance_id character varying,
    prototype_id character varying,
    owner_type character varying,
    owner_id character varying,
    location_context character varying,
    quantity integer,
    condition integer,
    flags_override jsonb,
    binding_state character varying,
    attunement_state jsonb,
    custom_name character varying,
    metadata jsonb,
    origin_source character varying,
    origin_metadata jsonb,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        ii.item_instance_id,
        ii.prototype_id,
        ii.owner_type,
        ii.owner_id,
        ii.location_context,
        ii.quantity,
        ii.condition,
        ii.flags_override,
        ii.binding_state,
        ii.attunement_state,
        ii.custom_name,
        ii.metadata,
        ii.origin_source,
        ii.origin_metadata,
        ii.created_at,
        ii.updated_at
    FROM item_instances ii
    WHERE ii.item_instance_id = p_item_instance_id;
END;
$$ LANGUAGE plpgsql;
