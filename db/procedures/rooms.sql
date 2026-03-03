-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f rooms.sql
--
-- These replace raw SQL in async_persistence and map APIs.

-- get_rooms_with_exits: aggregate rooms and exits for cache warmup
CREATE OR REPLACE FUNCTION :schema_name.get_rooms_with_exits() -- noqa: PRS
RETURNS TABLE (
    room_uuid uuid,
    stable_id text,
    name text,
    description text,
    attributes jsonb,
    subzone_stable_id text,
    zone_stable_id text,
    plane text,
    zone text,
    exits jsonb
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        r.id AS room_uuid,
        r.stable_id,
        r.name,
        r.description,
        r.attributes,
        sz.stable_id AS subzone_stable_id,
        z.stable_id AS zone_stable_id,
        SPLIT_PART(z.stable_id, '/', 1) AS plane,
        SPLIT_PART(z.stable_id, '/', 2) AS zone,
        COALESCE(
            (
                json_agg(
                    json_build_object(
                        'from_room_stable_id', r.stable_id,
                        'to_room_stable_id', r2.stable_id,
                        'direction', rl.direction,
                        'from_subzone_stable_id', sz.stable_id,
                        'from_zone_stable_id', z.stable_id,
                        'to_subzone_stable_id', sz2.stable_id,
                        'to_zone_stable_id', z2.stable_id
                    )
                ) FILTER (WHERE rl.direction IS NOT NULL)
            )::jsonb,
            '[]'::jsonb
        ) AS exits
    FROM rooms r
    LEFT JOIN subzones sz ON r.subzone_id = sz.id
    LEFT JOIN zones z ON sz.zone_id = z.id
    LEFT JOIN room_links rl ON r.id = rl.from_room_id
    LEFT JOIN rooms r2 ON rl.to_room_id = r2.id
    LEFT JOIN subzones sz2 ON r2.subzone_id = sz2.id
    LEFT JOIN zones z2 ON sz2.zone_id = z2.id
    GROUP BY
        r.id,
        r.stable_id,
        r.name,
        r.description,
        r.attributes,
        sz.stable_id,
        z.stable_id
    ORDER BY z.stable_id, sz.stable_id, r.stable_id;
END;
$$ LANGUAGE plpgsql;


-- get_room_exits: return exits for a set of room stable_ids
CREATE OR REPLACE FUNCTION :schema_name.get_room_exits(p_stable_ids text[]) -- noqa: PRS
RETURNS TABLE (
    from_stable_id text,
    to_stable_id text,
    direction text
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        r1.stable_id AS from_stable_id,
        r2.stable_id AS to_stable_id,
        rl.direction
    FROM room_links rl
    JOIN rooms r1 ON rl.from_room_id = r1.id
    JOIN rooms r2 ON rl.to_room_id = r2.id
    WHERE r1.stable_id = ANY(p_stable_ids);
END;
$$ LANGUAGE plpgsql;


-- get_rooms_by_zone_pattern: rooms for a plane/zone/sub_zone pattern
CREATE OR REPLACE FUNCTION :schema_name.get_rooms_by_zone_pattern(p_pattern text) -- noqa: PRS
RETURNS TABLE (
    id uuid,
    stable_id text,
    name text,
    attributes jsonb,
    map_x numeric,
    map_y numeric,
    map_origin_zone boolean,
    map_symbol text,
    map_style text
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        r.id,
        r.stable_id,
        r.name,
        r.attributes,
        r.map_x,
        r.map_y,
        r.map_origin_zone,
        r.map_symbol,
        r.map_style
    FROM rooms r
    JOIN subzones sz ON r.subzone_id = sz.id
    JOIN zones z ON sz.zone_id = z.id
    WHERE r.stable_id LIKE p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- get_room_by_stable_id: single room by exact stable_id
CREATE OR REPLACE FUNCTION :schema_name.get_room_by_stable_id(p_stable_id text) -- noqa: PRS
RETURNS TABLE (
    id uuid,
    stable_id text,
    name text,
    attributes jsonb,
    map_x numeric,
    map_y numeric,
    map_origin_zone boolean,
    map_symbol text,
    map_style text
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        r.id,
        r.stable_id,
        r.name,
        r.attributes,
        r.map_x,
        r.map_y,
        r.map_origin_zone,
        r.map_symbol,
        r.map_style
    FROM rooms r
    JOIN subzones sz ON r.subzone_id = sz.id
    JOIN zones z ON sz.zone_id = z.id
    WHERE r.stable_id = p_stable_id;
END;
$$ LANGUAGE plpgsql;


-- clear_room_map_origins: clear map_origin_zone flag for a zone pattern
CREATE OR REPLACE FUNCTION :schema_name.clear_room_map_origins(p_pattern text) -- noqa: PRS
RETURNS void AS $$
BEGIN
    UPDATE rooms
    SET map_origin_zone = FALSE
    WHERE stable_id LIKE p_pattern || '%'
      AND map_origin_zone = TRUE;
END;
$$ LANGUAGE plpgsql;


-- set_room_map_origin: set map_origin_zone for a specific room
CREATE OR REPLACE FUNCTION :schema_name.set_room_map_origin(p_room_id text) -- noqa: PRS
RETURNS boolean AS $$
DECLARE
    v_updated integer;
BEGIN
    UPDATE rooms
    SET map_origin_zone = TRUE
    WHERE stable_id = p_room_id;

    GET DIAGNOSTICS v_updated = ROW_COUNT;
    RETURN v_updated > 0;
END;
$$ LANGUAGE plpgsql;
