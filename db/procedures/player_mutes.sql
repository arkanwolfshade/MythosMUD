-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f player_mutes.sql
--
-- Player mutes (#681). Table DDL: db/migrations/20260928120000_player_aliases_and_mutes.sql.
-- The server keeps an in-memory index (UserManager) loaded once from get_active_player_mutes()
-- at startup; these functions are its durable write path.
--
-- A mute is identified by:
--   player:  (muter_id, target_id)
--   channel: (muter_id, channel)
--   global:  (target_id)  -- at most one global mute per target, whoever applied it

CREATE OR REPLACE FUNCTION :schema_name.get_active_player_mutes() -- noqa: PRS
RETURNS TABLE(
    mute_type TEXT,
    muter_id UUID,
    muter_name VARCHAR,
    target_id UUID,
    target_name VARCHAR,
    channel VARCHAR,
    reason TEXT,
    muted_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        m.mute_type,
        m.muter_id,
        m.muter_name,
        m.target_id,
        m.target_name,
        m.channel,
        m.reason,
        m.muted_at,
        m.expires_at
    FROM player_mutes m
    WHERE m.expires_at IS NULL OR m.expires_at > now();
END;
$$;

CREATE OR REPLACE FUNCTION :schema_name.delete_player_mute( -- noqa: PRS
    p_mute_type TEXT,
    p_muter_id UUID,
    p_target_id UUID,
    p_channel TEXT
)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    v_deleted INTEGER;
BEGIN
    DELETE FROM player_mutes m
    WHERE m.mute_type = p_mute_type
      AND (
          (p_mute_type = 'player' AND m.muter_id = p_muter_id AND m.target_id = p_target_id)
          OR (p_mute_type = 'channel' AND m.muter_id = p_muter_id AND m.channel = p_channel)
          OR (p_mute_type = 'global' AND m.target_id = p_target_id)
      );

    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RETURN v_deleted > 0;
END;
$$;

-- Apply a mute, replacing any existing mute with the same identity (see header).
CREATE OR REPLACE FUNCTION :schema_name.upsert_player_mute( -- noqa: PRS
    p_mute_type TEXT,
    p_muter_id UUID,
    p_muter_name TEXT,
    p_target_id UUID,
    p_target_name TEXT,
    p_channel TEXT,
    p_reason TEXT,
    p_muted_at TIMESTAMPTZ,
    p_expires_at TIMESTAMPTZ
)
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
    PERFORM delete_player_mute(p_mute_type, p_muter_id, p_target_id, p_channel);

    INSERT INTO player_mutes (
        mute_type,
        muter_id,
        muter_name,
        target_id,
        target_name,
        channel,
        reason,
        muted_at,
        expires_at
    ) VALUES (
        p_mute_type,
        p_muter_id,
        p_muter_name,
        p_target_id,
        p_target_name,
        p_channel,
        coalesce(p_reason, ''),
        p_muted_at,
        p_expires_at
    );
END;
$$;
