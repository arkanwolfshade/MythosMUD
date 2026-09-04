-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f player_effects.sql
--
-- Player effect procedures. Replaces ORM in PlayerEffectRepository.

-- add_player_effect: insert effect, return effect id
CREATE OR REPLACE FUNCTION :schema_name.add_player_effect( -- noqa: PRS
    p_player_id UUID,
    p_effect_type character varying,
    p_category character varying,
    p_duration integer,
    p_applied_at_tick integer,
    p_intensity integer DEFAULT 1,
    p_source character varying DEFAULT NULL,
    p_visibility_level character varying DEFAULT 'visible'
)
RETURNS uuid
LANGUAGE plpgsql
AS $$
DECLARE
    out_id uuid;
BEGIN
    INSERT INTO player_effects (
        player_id, effect_type, category, duration, applied_at_tick,
        intensity, source, visibility_level
    )
    VALUES (
        p_player_id, p_effect_type, p_category, p_duration, p_applied_at_tick,
        COALESCE(p_intensity, 1), p_source, COALESCE(p_visibility_level, 'visible')
    )
    RETURNING id INTO out_id;
    RETURN out_id;
END;
$$;


-- delete_player_effect: delete by effect id
CREATE OR REPLACE FUNCTION :schema_name.delete_player_effect(p_effect_id uuid) -- noqa: PRS
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM player_effects WHERE player_effects.id = p_effect_id;
END;
$$;


-- get_active_effects_for_player: effects where duration - (current_tick - applied_at_tick) > 0
CREATE OR REPLACE FUNCTION :schema_name.get_active_effects_for_player( -- noqa: PRS
    p_player_id UUID,
    p_current_tick integer
)
RETURNS TABLE (
    id uuid,
    player_id uuid,
    effect_type character varying(64),
    category character varying(64),
    duration integer,
    applied_at_tick integer,
    intensity integer,
    source character varying(128),
    visibility_level character varying(32),
    created_at timestamp without time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        pe.id,
        pe.player_id,
        pe.effect_type,
        pe.category,
        pe.duration,
        pe.applied_at_tick,
        pe.intensity,
        pe.source,
        pe.visibility_level,
        pe.created_at
    FROM player_effects pe
    WHERE pe.player_id = p_player_id
      AND (pe.duration - (p_current_tick - pe.applied_at_tick)) > 0
    ORDER BY pe.applied_at_tick;
END;
$$;


-- get_effects_expiring_this_tick: (player_id, effect_type) where remaining <= 0
CREATE OR REPLACE FUNCTION :schema_name.get_effects_expiring_this_tick(p_current_tick integer) -- noqa: PRS
RETURNS TABLE (player_id uuid, effect_type character varying(64))
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT pe.player_id, pe.effect_type
    FROM player_effects pe
    WHERE (pe.duration - (p_current_tick - pe.applied_at_tick)) <= 0;
END;
$$;


-- expire_effects_for_tick: delete effects where applied_at_tick + duration <= current_tick
CREATE OR REPLACE FUNCTION :schema_name.expire_effects_for_tick(p_current_tick integer) -- noqa: PRS
RETURNS integer
LANGUAGE plpgsql
AS $$
DECLARE
    rows_deleted integer;
BEGIN
    DELETE FROM player_effects
    WHERE player_effects.applied_at_tick + player_effects.duration <= p_current_tick;
    GET DIAGNOSTICS rows_deleted = ROW_COUNT;
    RETURN rows_deleted;
END;
$$;
