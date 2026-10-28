-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f player_effects.sql
--
-- Player effect procedures (ADR-019, ADR-029 step 3b-i). Replaces ORM in PlayerEffectRepository.
-- remaining_seconds counts game seconds left while the player is online (NULL = until removed); payload holds the
-- effect's parameters and mutable state.

-- Signatures from the tick-based schema: drop them so the reapply leaves no stale overloads behind.
DROP FUNCTION IF EXISTS :schema_name.add_player_effect( -- noqa: PRS
    uuid, character varying, character varying, integer, integer, integer, character varying, character varying
);
DROP FUNCTION IF EXISTS :schema_name.get_active_effects_for_player(uuid, integer); -- noqa: PRS
DROP FUNCTION IF EXISTS :schema_name.get_effects_expiring_this_tick(integer); -- noqa: PRS
DROP FUNCTION IF EXISTS :schema_name.expire_effects_for_tick(integer); -- noqa: PRS
DROP FUNCTION IF EXISTS :schema_name.get_active_effects_for_player(uuid); -- noqa: PRS

-- add_player_effect: insert effect, return effect id
CREATE OR REPLACE FUNCTION :schema_name.add_player_effect( -- noqa: PRS
    p_player_id UUID,
    p_effect_type character varying,
    p_category character varying,
    p_remaining_seconds integer,
    p_payload jsonb DEFAULT '{}'::jsonb,
    p_instance_scoped boolean DEFAULT false,
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
        player_id, effect_type, category, remaining_seconds, payload, instance_scoped,
        intensity, source, visibility_level
    )
    VALUES (
        p_player_id, p_effect_type, p_category, p_remaining_seconds, COALESCE(p_payload, '{}'::jsonb),
        COALESCE(p_instance_scoped, false), COALESCE(p_intensity, 1), p_source,
        COALESCE(p_visibility_level, 'visible')
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


-- delete_player_effects_by_type: delete every effect of one type on a player; returns how many
CREATE OR REPLACE FUNCTION :schema_name.delete_player_effects_by_type( -- noqa: PRS
    p_player_id uuid,
    p_effect_type character varying
)
RETURNS integer
LANGUAGE plpgsql
AS $$
DECLARE
    rows_deleted integer;
BEGIN
    DELETE FROM player_effects
    WHERE player_effects.player_id = p_player_id AND player_effects.effect_type = p_effect_type;
    GET DIAGNOSTICS rows_deleted = ROW_COUNT;
    RETURN rows_deleted;
END;
$$;


-- delete_instance_scoped_effects: delete a player's instance-scoped effects (instance lost); returns how many
CREATE OR REPLACE FUNCTION :schema_name.delete_instance_scoped_effects(p_player_id uuid) -- noqa: PRS
RETURNS integer
LANGUAGE plpgsql
AS $$
DECLARE
    rows_deleted integer;
BEGIN
    DELETE FROM player_effects
    WHERE player_effects.player_id = p_player_id AND player_effects.instance_scoped;
    GET DIAGNOSTICS rows_deleted = ROW_COUNT;
    RETURN rows_deleted;
END;
$$;


-- get_active_effects_for_player: effects with time left (or no limit), oldest first
CREATE OR REPLACE FUNCTION :schema_name.get_active_effects_for_player(p_player_id uuid) -- noqa: PRS
RETURNS TABLE (
    id uuid,
    player_id uuid,
    effect_type character varying(64),
    category character varying(64),
    remaining_seconds integer,
    payload jsonb,
    instance_scoped boolean,
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
        pe.remaining_seconds,
        pe.payload,
        pe.instance_scoped,
        pe.intensity,
        pe.source,
        pe.visibility_level,
        pe.created_at
    FROM player_effects AS pe
    WHERE
        pe.player_id = p_player_id
        AND (pe.remaining_seconds IS NULL OR pe.remaining_seconds > 0)
    ORDER BY pe.created_at, pe.id;
END;
$$;


-- update_player_effect_payload: replace an effect's payload (its mutable state, e.g. the drain's elapsed)
CREATE OR REPLACE FUNCTION :schema_name.update_player_effect_payload( -- noqa: PRS
    p_effect_id uuid,
    p_payload jsonb
)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE player_effects SET payload = COALESCE(p_payload, '{}'::jsonb) WHERE player_effects.id = p_effect_id;
END;
$$;


-- advance_player_effects: one game second passes for these (online) players. Timed effects lose a second; the ones
-- that run out are deleted and returned, so the caller can react (e.g. ending a login ward).
CREATE OR REPLACE FUNCTION :schema_name.advance_player_effects(p_player_ids uuid []) -- noqa: PRS
RETURNS TABLE (player_id uuid, effect_type character varying(64))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE player_effects AS pe
    SET remaining_seconds = pe.remaining_seconds - 1
    WHERE pe.player_id = ANY(p_player_ids) AND pe.remaining_seconds IS NOT NULL;

    RETURN QUERY
    DELETE FROM player_effects AS pe
    WHERE pe.player_id = ANY(p_player_ids) AND pe.remaining_seconds <= 0
    RETURNING pe.player_id, pe.effect_type;
END;
$$;
