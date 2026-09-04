-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f exploration.sql
--
-- Coordinate generation/validation and player-exploration-tracking procedures. Replaces raw SQL
-- in server/services/coordinate_generator.py, server/services/coordinate_validator.py, and
-- server/services/exploration_service.py (#633). Depends on rooms/subzones/zones (map coordinate
-- columns) and player_exploration.

-- get_rooms_for_coordinate_generation: rooms in a zone/subzone (matched by stable_id prefix),
-- joined to their zone/subzone stable_ids. Column order matches
-- CoordinateGenerator._room_dict_from_row's positional row access -- do not reorder.
CREATE OR REPLACE FUNCTION :schema_name.get_rooms_for_coordinate_generation(p_pattern text) -- noqa: PRS
RETURNS TABLE (
    id uuid,
    stable_id text,
    name text,
    attributes jsonb,
    map_x numeric,
    map_y numeric,
    map_origin_zone boolean,
    map_symbol text,
    map_style text,
    zone_stable_id text,
    subzone_stable_id text
)
LANGUAGE plpgsql
AS $$
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
        r.map_style,
        z.stable_id,
        sz.stable_id
    FROM rooms r
    JOIN subzones sz ON r.subzone_id = sz.id
    JOIN zones z ON sz.zone_id = z.id
    WHERE r.stable_id LIKE p_pattern || '%';
END;
$$;


-- get_room_exits_for_coordinate_generation: exits (room_links) originating from any room in the
-- given set, with both endpoints' stable_ids resolved. Column order matches
-- CoordinateGenerator._attach_room_exits's positional row access.
CREATE OR REPLACE FUNCTION :schema_name.get_room_exits_for_coordinate_generation(p_room_uuids uuid[]) -- noqa: PRS
RETURNS TABLE (
    from_stable_id text,
    to_stable_id text,
    direction text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        r1.stable_id,
        r2.stable_id,
        rl.direction
    FROM room_links rl
    JOIN rooms r1 ON rl.from_room_id = r1.id
    JOIN rooms r2 ON rl.to_room_id = r2.id
    WHERE rl.from_room_id = ANY(p_room_uuids);
END;
$$;


-- get_coordinate_conflicts: rooms sharing (map_x, map_y) within a zone/subzone, one row per
-- conflicting pair (r1.id < r2.id dedupes A-vs-B from B-vs-A). Shape preserved exactly from the
-- raw query it replaces -- CoordinateValidator._conflict_from_row maps it straight through to the
-- admin-facing conflict report (#633 judgment call).
CREATE OR REPLACE FUNCTION :schema_name.get_coordinate_conflicts(p_pattern text) -- noqa: PRS
RETURNS TABLE (
    room1_id text,
    room1_name text,
    room2_id text,
    room2_name text,
    map_x numeric,
    map_y numeric
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        r1.stable_id,
        r1.name,
        r2.stable_id,
        r2.name,
        r1.map_x,
        r1.map_y
    FROM rooms r1
    JOIN rooms r2 ON r1.map_x = r2.map_x AND r1.map_y = r2.map_y
    JOIN subzones sz1 ON r1.subzone_id = sz1.id
    JOIN zones z1 ON sz1.zone_id = z1.id
    JOIN subzones sz2 ON r2.subzone_id = sz2.id
    JOIN zones z2 ON sz2.zone_id = z2.id
    WHERE r1.stable_id LIKE p_pattern || '%'
      AND r2.stable_id LIKE p_pattern || '%'
      AND r1.id < r2.id
      AND r1.map_x IS NOT NULL
      AND r1.map_y IS NOT NULL
      AND r2.map_x IS NOT NULL
      AND r2.map_y IS NOT NULL;
END;
$$;


-- count_coordinated_rooms: number of rooms in a zone/subzone that already have map coordinates
CREATE OR REPLACE FUNCTION :schema_name.count_coordinated_rooms(p_pattern text) -- noqa: PRS
RETURNS bigint
LANGUAGE plpgsql
AS $$
DECLARE
    v_count bigint;
BEGIN
    SELECT count(*)
    INTO v_count
    FROM rooms r
    JOIN subzones sz ON r.subzone_id = sz.id
    JOIN zones z ON sz.zone_id = z.id
    WHERE r.stable_id LIKE p_pattern || '%'
      AND r.map_x IS NOT NULL
      AND r.map_y IS NOT NULL;
    RETURN v_count;
END;
$$;


-- get_room_id_by_stable_id: resolve a room's hierarchical stable_id to its UUID primary key
CREATE OR REPLACE FUNCTION :schema_name.get_room_id_by_stable_id(p_stable_id text) -- noqa: PRS
RETURNS uuid
LANGUAGE plpgsql
AS $$
DECLARE
    v_id uuid;
BEGIN
    SELECT id INTO v_id FROM rooms WHERE stable_id = p_stable_id;
    RETURN v_id;
END;
$$;


-- mark_room_explored: idempotently record that a player has explored a room. Returns whether the
-- row was NEWLY inserted (true) vs already existed (false) -- callers use this only to pick a log
-- line; mark_room_as_explored()'s own return contract stays "true" either way. #633 judgment call:
-- collapses the prior check-then-insert (a SELECT existed purely to choose the log line, then an
-- already-idempotent INSERT ... ON CONFLICT DO NOTHING) into one round trip.
CREATE OR REPLACE FUNCTION :schema_name.mark_room_explored(p_player_id uuid, p_room_id uuid) -- noqa: PRS
RETURNS boolean
LANGUAGE plpgsql
AS $$
DECLARE
    v_inserted boolean;
BEGIN
    INSERT INTO player_exploration (player_id, room_id, explored_at)
    VALUES (p_player_id, p_room_id, now())
    ON CONFLICT (player_id, room_id) DO NOTHING
    RETURNING true INTO v_inserted;

    RETURN COALESCE(v_inserted, false);
END;
$$;


-- get_explored_rooms: room_ids a player has explored, ordered by when they explored them
CREATE OR REPLACE FUNCTION :schema_name.get_explored_rooms(p_player_id uuid) -- noqa: PRS
RETURNS TABLE (room_id uuid)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT pe.room_id
    FROM player_exploration pe
    WHERE pe.player_id = p_player_id
    ORDER BY pe.explored_at ASC;
END;
$$;


-- is_room_explored: whether a player has explored a specific room
CREATE OR REPLACE FUNCTION :schema_name.is_room_explored(p_player_id uuid, p_room_id uuid) -- noqa: PRS
RETURNS boolean
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM player_exploration
        WHERE player_id = p_player_id AND room_id = p_room_id
    );
END;
$$;
