-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f item_catalog.sql
--
-- Paginated item_prototypes listing for /catalog slash and Catalog ESC page.

-- list_item_prototypes_page: filtered page of item prototypes with total_count
CREATE OR REPLACE FUNCTION :schema_name.list_item_prototypes_page( -- noqa: PRS
    p_item_type character varying DEFAULT NULL,
    p_namespace character varying DEFAULT NULL,
    p_search character varying DEFAULT NULL,
    p_limit integer DEFAULT 25,
    p_offset integer DEFAULT 0
)
RETURNS TABLE (
    prototype_id character varying,
    name character varying,
    short_description character varying,
    long_description text,
    item_type character varying,
    weight double precision,
    base_value integer,
    durability integer,
    flags jsonb,
    wear_slots jsonb,
    stacking_rules jsonb,
    usage_restrictions jsonb,
    effect_components jsonb,
    metadata jsonb,
    tags jsonb,
    created_at timestamp with time zone,
    total_count bigint
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        ip.prototype_id,
        ip.name,
        ip.short_description,
        ip.long_description,
        ip.item_type,
        ip.weight,
        ip.base_value,
        ip.durability,
        ip.flags,
        ip.wear_slots,
        ip.stacking_rules,
        ip.usage_restrictions,
        ip.effect_components,
        ip.metadata,
        ip.tags,
        ip.created_at,
        COUNT(*) OVER() AS total_count
    FROM item_prototypes ip
    WHERE
        (p_item_type IS NULL OR ip.item_type = p_item_type)
        AND (
            p_namespace IS NULL
            OR ip.metadata->>'namespace' = p_namespace
        )
        AND (
            p_search IS NULL
            OR ip.name ILIKE '%' || p_search || '%'
            OR ip.short_description ILIKE '%' || p_search || '%'
            OR ip.prototype_id ILIKE '%' || p_search || '%'
        )
    ORDER BY ip.name ASC
    LIMIT GREATEST(p_limit, 1)
    OFFSET GREATEST(p_offset, 0);
END;
$$;
