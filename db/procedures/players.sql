-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f players.sql
--
-- Python maps these rows to Player domain objects.

-- get_player_by_id: fetch single player by UUID (includes inventory)
CREATE OR REPLACE FUNCTION :schema_name.get_player_by_id(p_id UUID) -- noqa: PRS
RETURNS TABLE (
    player_id uuid,
    user_id uuid,
    name character varying(50),
    inventory text,
    status_effects text,
    current_room_id character varying(255),
    respawn_room_id character varying(100),
    experience_points integer,
    level integer,
    is_admin integer,
    profession_id bigint,
    created_at timestamp with time zone,
    last_active timestamp with time zone,
    stats jsonb,
    is_deleted boolean,
    deleted_at timestamp with time zone,
    tutorial_instance_id character varying(255),
    inventory_json text,
    equipped_json text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.player_id,
        p.user_id,
        p.name,
        p.inventory,
        p.status_effects,
        p.current_room_id,
        p.respawn_room_id,
        p.experience_points,
        p.level,
        p.is_admin,
        p.profession_id,
        p.created_at,
        p.last_active,
        p.stats,
        p.is_deleted,
        p.deleted_at,
        p.tutorial_instance_id,
        COALESCE(pi.inventory_json, '[]'),
        COALESCE(pi.equipped_json, '{}')
    FROM players p
    LEFT JOIN player_inventories pi ON pi.player_id = p.player_id
    WHERE p.player_id = p_id;
END;
$$;

-- get_player_by_name: fetch active player by name (case-insensitive, excludes deleted)
CREATE OR REPLACE FUNCTION :schema_name.get_player_by_name(p_name TEXT)
RETURNS TABLE (
    player_id uuid,
    user_id uuid,
    name character varying(50),
    inventory text,
    status_effects text,
    current_room_id character varying(255),
    respawn_room_id character varying(100),
    experience_points integer,
    level integer,
    is_admin integer,
    profession_id bigint,
    created_at timestamp with time zone,
    last_active timestamp with time zone,
    stats jsonb,
    is_deleted boolean,
    deleted_at timestamp with time zone,
    tutorial_instance_id character varying(255),
    inventory_json text,
    equipped_json text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.player_id,
        p.user_id,
        p.name,
        p.inventory,
        p.status_effects,
        p.current_room_id,
        p.respawn_room_id,
        p.experience_points,
        p.level,
        p.is_admin,
        p.profession_id,
        p.created_at,
        p.last_active,
        p.stats,
        p.is_deleted,
        p.deleted_at,
        p.tutorial_instance_id,
        COALESCE(pi.inventory_json, '[]'),
        COALESCE(pi.equipped_json, '{}')
    FROM players p
    LEFT JOIN player_inventories pi ON pi.player_id = p.player_id
    WHERE LOWER(p.name) = LOWER(p_name)
      AND p.is_deleted = false;
END;
$$;

-- get_players_by_user_id: fetch all players for a user (including deleted)
CREATE OR REPLACE FUNCTION :schema_name.get_players_by_user_id(p_user_id UUID)
RETURNS TABLE (
    player_id uuid,
    user_id uuid,
    name character varying(50),
    inventory text,
    status_effects text,
    current_room_id character varying(255),
    respawn_room_id character varying(100),
    experience_points integer,
    level integer,
    is_admin integer,
    profession_id bigint,
    created_at timestamp with time zone,
    last_active timestamp with time zone,
    stats jsonb,
    is_deleted boolean,
    deleted_at timestamp with time zone,
    tutorial_instance_id character varying(255),
    inventory_json text,
    equipped_json text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.player_id,
        p.user_id,
        p.name,
        p.inventory,
        p.status_effects,
        p.current_room_id,
        p.respawn_room_id,
        p.experience_points,
        p.level,
        p.is_admin,
        p.profession_id,
        p.created_at,
        p.last_active,
        p.stats,
        p.is_deleted,
        p.deleted_at,
        p.tutorial_instance_id,
        COALESCE(pi.inventory_json, '[]'),
        COALESCE(pi.equipped_json, '{}')
    FROM players p
    LEFT JOIN player_inventories pi ON pi.player_id = p.player_id
    WHERE p.user_id = p_user_id;
END;
$$;

-- get_active_players_by_user_id: fetch active (non-deleted) players for a user
CREATE OR REPLACE FUNCTION :schema_name.get_active_players_by_user_id(p_user_id UUID)
RETURNS TABLE (
    player_id uuid,
    user_id uuid,
    name character varying(50),
    inventory text,
    status_effects text,
    current_room_id character varying(255),
    respawn_room_id character varying(100),
    experience_points integer,
    level integer,
    is_admin integer,
    profession_id bigint,
    created_at timestamp with time zone,
    last_active timestamp with time zone,
    stats jsonb,
    is_deleted boolean,
    deleted_at timestamp with time zone,
    tutorial_instance_id character varying(255),
    inventory_json text,
    equipped_json text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.player_id,
        p.user_id,
        p.name,
        p.inventory,
        p.status_effects,
        p.current_room_id,
        p.respawn_room_id,
        p.experience_points,
        p.level,
        p.is_admin,
        p.profession_id,
        p.created_at,
        p.last_active,
        p.stats,
        p.is_deleted,
        p.deleted_at,
        p.tutorial_instance_id,
        COALESCE(pi.inventory_json, '[]'),
        COALESCE(pi.equipped_json, '{}')
    FROM players p
    LEFT JOIN player_inventories pi ON pi.player_id = p.player_id
    WHERE p.user_id = p_user_id
      AND p.is_deleted = false;
END;
$$;

-- list_players: fetch all players
CREATE OR REPLACE FUNCTION :schema_name.list_players()
RETURNS TABLE (
    player_id uuid,
    user_id uuid,
    name character varying(50),
    inventory text,
    status_effects text,
    current_room_id character varying(255),
    respawn_room_id character varying(100),
    experience_points integer,
    level integer,
    is_admin integer,
    profession_id bigint,
    created_at timestamp with time zone,
    last_active timestamp with time zone,
    stats jsonb,
    is_deleted boolean,
    deleted_at timestamp with time zone,
    tutorial_instance_id character varying(255),
    inventory_json text,
    equipped_json text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.player_id,
        p.user_id,
        p.name,
        p.inventory,
        p.status_effects,
        p.current_room_id,
        p.respawn_room_id,
        p.experience_points,
        p.level,
        p.is_admin,
        p.profession_id,
        p.created_at,
        p.last_active,
        p.stats,
        p.is_deleted,
        p.deleted_at,
        p.tutorial_instance_id,
        COALESCE(pi.inventory_json, '[]'),
        COALESCE(pi.equipped_json, '{}')
    FROM players p
    LEFT JOIN player_inventories pi ON pi.player_id = p.player_id;
END;
$$;

-- get_players_in_room: fetch players in a room
CREATE OR REPLACE FUNCTION :schema_name.get_players_in_room(p_room_id TEXT)
RETURNS TABLE (
    player_id uuid,
    user_id uuid,
    name character varying(50),
    inventory text,
    status_effects text,
    current_room_id character varying(255),
    respawn_room_id character varying(100),
    experience_points integer,
    level integer,
    is_admin integer,
    profession_id bigint,
    created_at timestamp with time zone,
    last_active timestamp with time zone,
    stats jsonb,
    is_deleted boolean,
    deleted_at timestamp with time zone,
    tutorial_instance_id character varying(255),
    inventory_json text,
    equipped_json text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.player_id,
        p.user_id,
        p.name,
        p.inventory,
        p.status_effects,
        p.current_room_id,
        p.respawn_room_id,
        p.experience_points,
        p.level,
        p.is_admin,
        p.profession_id,
        p.created_at,
        p.last_active,
        p.stats,
        p.is_deleted,
        p.deleted_at,
        p.tutorial_instance_id,
        COALESCE(pi.inventory_json, '[]'),
        COALESCE(pi.equipped_json, '{}')
    FROM players p
    LEFT JOIN player_inventories pi ON pi.player_id = p.player_id
    WHERE p.current_room_id = p_room_id;
END;
$$;

-- get_players_batch: fetch multiple players by IDs
CREATE OR REPLACE FUNCTION :schema_name.get_players_batch(p_ids UUID[])
RETURNS TABLE (
    player_id uuid,
    user_id uuid,
    name character varying(50),
    inventory text,
    status_effects text,
    current_room_id character varying(255),
    respawn_room_id character varying(100),
    experience_points integer,
    level integer,
    is_admin integer,
    profession_id bigint,
    created_at timestamp with time zone,
    last_active timestamp with time zone,
    stats jsonb,
    is_deleted boolean,
    deleted_at timestamp with time zone,
    tutorial_instance_id character varying(255),
    inventory_json text,
    equipped_json text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.player_id,
        p.user_id,
        p.name,
        p.inventory,
        p.status_effects,
        p.current_room_id,
        p.respawn_room_id,
        p.experience_points,
        p.level,
        p.is_admin,
        p.profession_id,
        p.created_at,
        p.last_active,
        p.stats,
        p.is_deleted,
        p.deleted_at,
        p.tutorial_instance_id,
        COALESCE(pi.inventory_json, '[]'),
        COALESCE(pi.equipped_json, '{}')
    FROM players p
    LEFT JOIN player_inventories pi ON pi.player_id = p.player_id
    WHERE p.player_id = ANY(p_ids);
END;
$$;

-- update_player_current_room: update current_room_id (for room validation fix)
CREATE OR REPLACE FUNCTION :schema_name.update_player_current_room(p_id UUID, p_room_id VARCHAR(255))
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE players SET current_room_id = p_room_id WHERE player_id = p_id;
END;
$$;

-- update_player_last_active: update last_active timestamp
CREATE OR REPLACE FUNCTION :schema_name.update_player_last_active(
    p_id UUID,
    p_ts timestamp with time zone DEFAULT NULL
)
RETURNS VOID
LANGUAGE plpgsql
AS $$
DECLARE
    v_ts timestamp with time zone;
BEGIN
    v_ts := COALESCE(p_ts, now());
    UPDATE players SET last_active = v_ts WHERE player_id = p_id;
END;
$$;

-- soft_delete_player: set is_deleted=true, deleted_at=now()
-- Idempotent: a repeat call against an already-deleted row no-ops (returns false) rather
-- than reporting success again -- see issue #777.
CREATE OR REPLACE FUNCTION :schema_name.soft_delete_player(p_id UUID)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    v_updated integer;
BEGIN
    UPDATE players
    SET is_deleted = true, deleted_at = now()
    WHERE player_id = p_id
      AND is_deleted = false;
    GET DIAGNOSTICS v_updated = ROW_COUNT;
    RETURN v_updated > 0;
END;
$$;

-- player_is_deleted: cheap single-column read used by save_player's stale-object guard
-- (issue #777) to avoid resurrecting a soft-deleted row via upsert_player. Returns NULL
-- for a non-existent player id -- callers must treat only TRUE as "deleted".
-- plpgsql (not LANGUAGE sql) to match every other function in this file: a plain SQL
-- function body is parsed and bound to "players" at CREATE FUNCTION time, which fails
-- unless the applying session's search_path already resolves the target schema.
CREATE OR REPLACE FUNCTION :schema_name.player_is_deleted(p_id UUID)
RETURNS BOOLEAN
LANGUAGE plpgsql
STABLE
AS $$
DECLARE
    v_deleted boolean;
BEGIN
    SELECT is_deleted INTO v_deleted FROM players WHERE player_id = p_id;
    RETURN v_deleted;
END;
$$;

-- delete_player: hard delete player and inventory
CREATE OR REPLACE FUNCTION :schema_name.delete_player(p_id UUID)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    v_deleted integer;
BEGIN
    DELETE FROM player_inventories WHERE player_id = p_id;
    DELETE FROM players WHERE player_id = p_id;
    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RETURN v_deleted > 0;
END;
$$;

-- upsert_player: insert or update player and player_inventories
-- All params required for full upsert; Python prepares data before calling.
CREATE OR REPLACE PROCEDURE :schema_name.upsert_player(
    p_player_id UUID,
    p_user_id UUID,
    p_name VARCHAR(50),
    p_inventory TEXT,
    p_status_effects TEXT,
    p_current_room_id VARCHAR(255),
    p_respawn_room_id VARCHAR(100),
    p_experience_points INT,
    p_level INT,
    p_is_admin INT,
    p_profession_id BIGINT,
    p_created_at TIMESTAMP WITH TIME ZONE,
    p_last_active TIMESTAMP WITH TIME ZONE,
    p_stats JSONB,
    p_is_deleted BOOLEAN,
    p_deleted_at TIMESTAMP WITH TIME ZONE,
    p_tutorial_instance_id VARCHAR(255),
    p_inventory_json TEXT,
    p_equipped_json TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO players (
        player_id, user_id, name, inventory, status_effects,
        current_room_id, respawn_room_id, experience_points, level, is_admin,
        profession_id, created_at, last_active, stats, is_deleted, deleted_at,
        tutorial_instance_id
    ) VALUES (
        p_player_id, p_user_id, p_name, p_inventory, p_status_effects,
        p_current_room_id, p_respawn_room_id, p_experience_points, p_level, p_is_admin,
        p_profession_id, p_created_at, p_last_active, p_stats, p_is_deleted, p_deleted_at,
        p_tutorial_instance_id
    )
    ON CONFLICT (player_id) DO UPDATE SET
        user_id = EXCLUDED.user_id,
        name = EXCLUDED.name,
        inventory = EXCLUDED.inventory,
        status_effects = EXCLUDED.status_effects,
        current_room_id = EXCLUDED.current_room_id,
        respawn_room_id = EXCLUDED.respawn_room_id,
        experience_points = EXCLUDED.experience_points,
        level = EXCLUDED.level,
        is_admin = EXCLUDED.is_admin,
        profession_id = EXCLUDED.profession_id,
        last_active = EXCLUDED.last_active,
        stats = EXCLUDED.stats,
        is_deleted = EXCLUDED.is_deleted,
        deleted_at = EXCLUDED.deleted_at,
        tutorial_instance_id = EXCLUDED.tutorial_instance_id;

    INSERT INTO player_inventories (player_id, inventory_json, equipped_json)
    VALUES (p_player_id, p_inventory_json, p_equipped_json)
    ON CONFLICT (player_id) DO UPDATE SET
        inventory_json = EXCLUDED.inventory_json,
        equipped_json = EXCLUDED.equipped_json;
END;
$$;

-- get_user_id_by_username_ci: case-insensitive username -> user id lookup (#633). Backs both
-- the registration existence check and the login lookup in server/auth/endpoints.py -- callers
-- that need the mapped User ORM entity follow up with session.get(User, id) to keep identity-map
-- tracking, rather than hydrating User from this row directly.
CREATE OR REPLACE FUNCTION :schema_name.get_user_id_by_username_ci(p_username text) -- noqa: PRS
RETURNS UUID
LANGUAGE plpgsql
AS $$
DECLARE
    v_id uuid;
BEGIN
    SELECT id INTO v_id FROM users WHERE lower(username) = lower(p_username);
    RETURN v_id;
END;
$$;

-- reserve_invite / capture_invite: auth-and-capture pair for invite-only registration (#733),
-- mirroring a payment auth hold. Both calls MUST run in the same caller transaction/session:
--
--   reserve_invite  (AUTH)    - takes a row lock on the invite and reports whether it is
--                                currently claimable, without consuming it. The lock is held
--                                until the caller's transaction ends, so no other session can
--                                also reserve or capture the same code until then.
--   capture_invite  (CAPTURE) - finalizes a reservation: marks the invite inactive and records
--                                the consuming user. Safe to call only after a successful
--                                reserve_invite() in the same transaction.
--
-- If the caller's work between reserve and capture fails (e.g. duplicate username) and the
-- transaction rolls back, the row lock releases and the invite is left untouched - an implicit
-- void, the same way an unrouted auth hold expires. No separate void procedure is needed.
CREATE OR REPLACE FUNCTION :schema_name.reserve_invite(p_invite_code text) -- noqa: PRS
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    v_is_active boolean;
BEGIN
    SELECT is_active INTO v_is_active
    FROM invites
    WHERE invite_code = p_invite_code
    FOR UPDATE;

    RETURN COALESCE(v_is_active, false);
END;
$$;

CREATE OR REPLACE FUNCTION :schema_name.capture_invite(p_invite_code text, p_used_by_user_id UUID) -- noqa: PRS
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    v_updated integer;
BEGIN
    -- is_active = true here is defense-in-depth, not the primary guard - reserve_invite's row
    -- lock is what makes this race-free. It still protects a caller that (incorrectly) calls
    -- capture_invite() without a preceding reserve_invite() in the same transaction.
    UPDATE invites
    SET is_active = false, used_by_user_id = p_used_by_user_id
    WHERE invite_code = p_invite_code
      AND is_active = true;
    GET DIAGNOSTICS v_updated = ROW_COUNT;
    RETURN v_updated > 0;
END;
$$;
