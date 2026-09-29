-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f player_aliases.sql
--
-- Player command aliases (#680). Table DDL: db/migrations/20260928120000_player_aliases_and_mutes.sql.
-- Callers address players by name (the command pipeline only carries the name); rows are keyed
-- by player_id, resolved against the active (non-deleted) player with that name.

CREATE OR REPLACE FUNCTION :schema_name.get_player_aliases(p_player_name TEXT) -- noqa: PRS
RETURNS TABLE(
    id UUID,
    name VARCHAR,
    command VARCHAR,
    created_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        a.id,
        a.name,
        a.command,
        a.created_at,
        a.updated_at
    FROM player_aliases a
    JOIN players p ON p.player_id = a.player_id
    WHERE lower(p.name) = lower(p_player_name)
      AND p.is_deleted = false
    ORDER BY a.created_at, a.name;
END;
$$;

CREATE OR REPLACE FUNCTION :schema_name.get_player_alias(p_player_name TEXT, p_alias_name TEXT) -- noqa: PRS
RETURNS TABLE(
    id UUID,
    name VARCHAR,
    command VARCHAR,
    created_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        a.id,
        a.name,
        a.command,
        a.created_at,
        a.updated_at
    FROM player_aliases a
    JOIN players p ON p.player_id = a.player_id
    WHERE lower(p.name) = lower(p_player_name)
      AND p.is_deleted = false
      AND lower(a.name) = lower(p_alias_name);
END;
$$;

-- Insert, or replace the command of the same-named (case-insensitive) alias.
-- Returns no rows when no active player has that name.
CREATE OR REPLACE FUNCTION :schema_name.upsert_player_alias( -- noqa: PRS
    p_player_name TEXT,
    p_alias_name TEXT,
    p_command TEXT
)
RETURNS TABLE(
    id UUID,
    name VARCHAR,
    command VARCHAR,
    created_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ
)
LANGUAGE plpgsql
AS $$
#variable_conflict use_column
DECLARE
    v_player_id UUID;
BEGIN
    SELECT p.player_id INTO v_player_id
    FROM players p
    WHERE lower(p.name) = lower(p_player_name)
      AND p.is_deleted = false;

    IF v_player_id IS NULL THEN
        RETURN;
    END IF;

    RETURN QUERY
    INSERT INTO player_aliases AS a (player_id, name, command)
    VALUES (v_player_id, p_alias_name, p_command)
    ON CONFLICT (player_id, lower(name)) DO UPDATE
        SET name = EXCLUDED.name,
            command = EXCLUDED.command,
            updated_at = now()
    RETURNING a.id, a.name, a.command, a.created_at, a.updated_at;
END;
$$;

CREATE OR REPLACE FUNCTION :schema_name.delete_player_alias(p_player_name TEXT, p_alias_name TEXT) -- noqa: PRS
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    v_deleted INTEGER;
BEGIN
    DELETE FROM player_aliases a
    USING players p
    WHERE p.player_id = a.player_id
      AND lower(p.name) = lower(p_player_name)
      AND p.is_deleted = false
      AND lower(a.name) = lower(p_alias_name);

    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RETURN v_deleted > 0;
END;
$$;

-- Players are soft-deleted, so ON DELETE CASCADE never fires; the delete-character flow calls this.
CREATE OR REPLACE FUNCTION :schema_name.delete_player_aliases_by_id(p_player_id UUID) -- noqa: PRS
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
DECLARE
    v_deleted INTEGER;
BEGIN
    DELETE FROM player_aliases WHERE player_id = p_player_id;
    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RETURN v_deleted;
END;
$$;
