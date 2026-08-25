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


-- update_room_map_position: set map_x/map_y for a single room (admin position edit)
CREATE OR REPLACE FUNCTION :schema_name.update_room_map_position(p_room_id text, p_map_x numeric, p_map_y numeric) -- noqa: PRS
RETURNS boolean AS $$
DECLARE
    v_updated integer;
BEGIN
    UPDATE rooms
    SET map_x = p_map_x, map_y = p_map_y
    WHERE stable_id = p_room_id;

    GET DIAGNOSTICS v_updated = ROW_COUNT;
    RETURN v_updated > 0;
END;
$$ LANGUAGE plpgsql;


-- update_room_map_positions: bulk set map_x/map_y from a jsonb array of
-- {stable_id, map_x, map_y} objects; returns the number of rows updated
CREATE OR REPLACE FUNCTION :schema_name.update_room_map_positions(p_positions jsonb) -- noqa: PRS
RETURNS integer AS $$
DECLARE
    v_updated integer;
BEGIN
    UPDATE rooms AS r
    SET map_x = p.map_x, map_y = p.map_y
    FROM jsonb_to_recordset(p_positions) AS p(stable_id text, map_x numeric, map_y numeric)
    WHERE r.stable_id = p.stable_id;

    GET DIAGNOSTICS v_updated = ROW_COUNT;
    RETURN v_updated;
END;
$$ LANGUAGE plpgsql;


-- get_room_stable_ids_by_uuids: resolve room UUIDs to stable_ids (exploration filtering)
CREATE OR REPLACE FUNCTION :schema_name.get_room_stable_ids_by_uuids(p_room_ids uuid[]) -- noqa: PRS
RETURNS TABLE (stable_id text) AS $$
BEGIN
    RETURN QUERY
    SELECT r.stable_id FROM rooms r WHERE r.id = ANY(p_room_ids);
END;
$$ LANGUAGE plpgsql;


-- update_room_properties: update name/description/environment for the room editor.
-- NULL means "leave alone" for p_name/p_description; p_set_environment distinguishes
-- "leave environment alone" (false) from "clear environment to NULL" (true, p_environment NULL).
CREATE OR REPLACE FUNCTION :schema_name.update_room_properties( -- noqa: PRS
    p_room_id text,
    p_name text,
    p_description text,
    p_environment text,
    p_set_environment boolean
)
RETURNS boolean AS $$
DECLARE
    v_updated integer;
BEGIN
    UPDATE rooms
    SET
        name = COALESCE(p_name, name),
        description = COALESCE(p_description, description),
        attributes = CASE
            WHEN NOT p_set_environment THEN attributes
            WHEN p_environment IS NULL THEN attributes - 'environment'
            ELSE jsonb_set(attributes, '{environment}', to_jsonb(p_environment), TRUE)
        END
    WHERE stable_id = p_room_id;

    GET DIAGNOSTICS v_updated = ROW_COUNT;
    RETURN v_updated > 0;
END;
$$ LANGUAGE plpgsql;


-- create_room_link: create a single directed exit (room_links row). Resolves stable_ids to
-- UUIDs internally. Room existence is the caller's responsibility (API layer checks both rooms
-- via RoomService before calling, matching update_room_position's existing pattern) -- this
-- procedure returns FALSE if either stable_id doesn't resolve, and lets a genuine
-- unique_violation (SQLSTATE 23505, from room_links_from_room_id_direction_key) propagate as a
-- real Postgres error for the API layer to map to 409.
CREATE OR REPLACE FUNCTION :schema_name.create_room_link( -- noqa: PRS
    p_from_room_id text,
    p_direction text,
    p_to_room_id text,
    p_attributes jsonb
)
RETURNS boolean AS $$
DECLARE
    v_from_uuid uuid;
    v_to_uuid uuid;
BEGIN
    SELECT id INTO v_from_uuid FROM rooms WHERE stable_id = p_from_room_id;
    SELECT id INTO v_to_uuid FROM rooms WHERE stable_id = p_to_room_id;

    IF v_from_uuid IS NULL OR v_to_uuid IS NULL THEN
        RETURN FALSE;
    END IF;

    INSERT INTO room_links (id, from_room_id, to_room_id, direction, attributes)
    VALUES (gen_random_uuid(), v_from_uuid, v_to_uuid, p_direction, COALESCE(p_attributes, '{}'::jsonb));

    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;


-- update_room_link: update the target room and/or attributes of an existing exit.
-- NULL p_to_room_id leaves the target unchanged; NULL p_attributes leaves attributes unchanged.
-- Returns FALSE if the source room, target room (when given), or the exit itself isn't found.
CREATE OR REPLACE FUNCTION :schema_name.update_room_link( -- noqa: PRS
    p_from_room_id text,
    p_direction text,
    p_to_room_id text,
    p_attributes jsonb
)
RETURNS boolean AS $$
DECLARE
    v_from_uuid uuid;
    v_to_uuid uuid;
    v_updated integer;
BEGIN
    SELECT id INTO v_from_uuid FROM rooms WHERE stable_id = p_from_room_id;
    IF v_from_uuid IS NULL THEN
        RETURN FALSE;
    END IF;

    IF p_to_room_id IS NOT NULL THEN
        SELECT id INTO v_to_uuid FROM rooms WHERE stable_id = p_to_room_id;
        IF v_to_uuid IS NULL THEN
            RETURN FALSE;
        END IF;
    END IF;

    UPDATE room_links
    SET
        to_room_id = COALESCE(v_to_uuid, to_room_id),
        attributes = COALESCE(p_attributes, attributes)
    WHERE from_room_id = v_from_uuid AND direction = p_direction;

    GET DIAGNOSTICS v_updated = ROW_COUNT;
    RETURN v_updated > 0;
END;
$$ LANGUAGE plpgsql;


-- delete_room_link: delete a single directed exit by (from_room stable_id, direction).
CREATE OR REPLACE FUNCTION :schema_name.delete_room_link(p_from_room_id text, p_direction text) -- noqa: PRS
RETURNS boolean AS $$
DECLARE
    v_from_uuid uuid;
    v_deleted integer;
BEGIN
    SELECT id INTO v_from_uuid FROM rooms WHERE stable_id = p_from_room_id;
    IF v_from_uuid IS NULL THEN
        RETURN FALSE;
    END IF;

    DELETE FROM room_links
    WHERE from_room_id = v_from_uuid AND direction = p_direction;

    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RETURN v_deleted > 0;
END;
$$ LANGUAGE plpgsql;
