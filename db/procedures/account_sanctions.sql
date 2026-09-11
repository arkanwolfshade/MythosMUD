-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f account_sanctions.sql
--
-- Account-level moderation sanctions (bans and kick cooldowns). Table DDL lives in
-- server/alembic/versions/2026_09_11_add_account_sanctions_table.py.
--
-- apply_ban_sanction / apply_kick_sanction: issue a new sanction, automatically lifting any
-- still-active sanction of the same type for the user first (a user has at most one active ban
-- and one active kick_cooldown at a time).
-- get_active_sanction: the caller's single current-most-severe active sanction (ban ranks above
-- kick_cooldown), or no rows if none.
-- lift_ban_sanction: manually lift an active ban early (e.g. an admin pardon).

CREATE OR REPLACE FUNCTION :schema_name.apply_ban_sanction( -- noqa: PRS
    p_user_id UUID,
    p_tier TEXT,
    p_reason TEXT,
    p_issued_by_player_id UUID
)
RETURNS UUID
LANGUAGE plpgsql
AS $$
DECLARE
    v_id UUID;
    v_expires_at TIMESTAMPTZ;
BEGIN
    IF p_reason IS NULL OR btrim(p_reason) = '' THEN
        RAISE EXCEPTION 'ban reason is required';
    END IF;

    IF p_tier NOT IN ('1h', '24h', '7d', 'permanent') THEN
        RAISE EXCEPTION 'invalid ban tier: %', p_tier;
    END IF;

    v_expires_at := CASE p_tier
        WHEN '1h' THEN now() + interval '1 hour'
        WHEN '24h' THEN now() + interval '24 hours'
        WHEN '7d' THEN now() + interval '7 days'
        ELSE NULL
    END;

    UPDATE account_sanctions
    SET lifted_at = now(),
        lifted_by_player_id = p_issued_by_player_id
    WHERE user_id = p_user_id
      AND sanction_type = 'ban'
      AND lifted_at IS NULL
      AND (expires_at IS NULL OR expires_at > now());

    v_id := gen_random_uuid();

    INSERT INTO account_sanctions (
        id,
        user_id,
        sanction_type,
        tier,
        reason,
        issued_by_player_id,
        issued_at,
        expires_at
    ) VALUES (
        v_id,
        p_user_id,
        'ban',
        p_tier,
        btrim(p_reason),
        p_issued_by_player_id,
        now(),
        v_expires_at
    );

    RETURN v_id;
END;
$$;

CREATE OR REPLACE FUNCTION :schema_name.apply_kick_sanction( -- noqa: PRS
    p_user_id UUID,
    p_reason TEXT,
    p_issued_by_player_id UUID,
    p_cooldown_minutes INTEGER
)
RETURNS UUID
LANGUAGE plpgsql
AS $$
DECLARE
    v_id UUID;
    v_expires_at TIMESTAMPTZ;
BEGIN
    IF p_reason IS NULL OR btrim(p_reason) = '' THEN
        RAISE EXCEPTION 'kick reason is required';
    END IF;

    IF p_cooldown_minutes IS NULL OR p_cooldown_minutes < 1 THEN
        RAISE EXCEPTION 'kick cooldown minutes must be at least 1';
    END IF;

    v_expires_at := now() + make_interval(mins => p_cooldown_minutes);

    UPDATE account_sanctions
    SET lifted_at = now(),
        lifted_by_player_id = p_issued_by_player_id
    WHERE user_id = p_user_id
      AND sanction_type = 'kick_cooldown'
      AND lifted_at IS NULL
      AND (expires_at IS NULL OR expires_at > now());

    v_id := gen_random_uuid();

    INSERT INTO account_sanctions (
        id,
        user_id,
        sanction_type,
        tier,
        reason,
        issued_by_player_id,
        issued_at,
        expires_at
    ) VALUES (
        v_id,
        p_user_id,
        'kick_cooldown',
        NULL,
        btrim(p_reason),
        p_issued_by_player_id,
        now(),
        v_expires_at
    );

    RETURN v_id;
END;
$$;

CREATE OR REPLACE FUNCTION :schema_name.get_active_sanction(p_user_id UUID) -- noqa: PRS
RETURNS TABLE(
    sanction_id UUID,
    user_id UUID,
    sanction_type TEXT,
    tier TEXT,
    reason TEXT,
    issued_by_player_id UUID,
    issued_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.id,
        s.user_id,
        s.sanction_type,
        s.tier,
        s.reason,
        s.issued_by_player_id,
        s.issued_at,
        s.expires_at
    FROM account_sanctions s
    WHERE s.user_id = p_user_id
      AND s.lifted_at IS NULL
      AND (s.expires_at IS NULL OR s.expires_at > now())
    ORDER BY
        CASE s.sanction_type
            WHEN 'ban' THEN 1
            WHEN 'kick_cooldown' THEN 2
            ELSE 3
        END,
        s.issued_at DESC
    LIMIT 1;
END;
$$;

CREATE OR REPLACE FUNCTION :schema_name.lift_ban_sanction(p_user_id UUID, p_lifted_by_player_id UUID) -- noqa: PRS
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    v_updated INTEGER;
BEGIN
    UPDATE account_sanctions
    SET lifted_at = now(),
        lifted_by_player_id = p_lifted_by_player_id
    WHERE user_id = p_user_id
      AND sanction_type = 'ban'
      AND lifted_at IS NULL
      AND (expires_at IS NULL OR expires_at > now());

    GET DIAGNOSTICS v_updated = ROW_COUNT;
    RETURN v_updated > 0;
END;
$$;
