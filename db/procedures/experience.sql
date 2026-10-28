-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f experience.sql
--
-- Experience procedures. Replaces raw SQL in ExperienceRepository.

DROP FUNCTION IF EXISTS :schema_name.update_player_xp(uuid, integer); -- noqa: PRS

-- level_for_xp: level implied by total XP under the curve total(L) = 50*L*(L-1)
-- (L1 = 0 XP, L2 = 100, L3 = 300, L10 = 4500). Inverted via the quadratic formula;
-- every level boundary makes (1 + xp/12.5) a perfect square, so this is exact, not
-- an approximation that happens to round right. Placeholder curve -- see
-- docs/subsystems/SUBSYSTEM_SKILLS_LEVEL_DESIGN.md for tuning notes.
CREATE OR REPLACE FUNCTION :schema_name.level_for_xp(p_xp integer) -- noqa: PRS
RETURNS integer
LANGUAGE sql
IMMUTABLE
AS $$
    SELECT GREATEST(1, floor((1 + sqrt(1 + GREATEST(p_xp, 0) / 12.5)) / 2)::integer);
$$;

-- award_player_xp: atomically add delta to experience_points and recompute level
-- from level_for_xp. Level never decreases (GREATEST against the current value).
-- Row-locked so concurrent awards can't race the level recomputation.
CREATE OR REPLACE FUNCTION :schema_name.award_player_xp( -- noqa: PRS
    p_player_id UUID,
    p_delta integer
)
RETURNS TABLE(new_xp integer, old_level integer, new_level integer)
LANGUAGE plpgsql
AS $$
DECLARE
    v_old_level integer;
    v_new_xp integer;
    v_new_level integer;
BEGIN
    IF p_delta < 0 THEN
        RAISE EXCEPTION 'XP delta must be non-negative, got %', p_delta;
    END IF;

    SELECT level INTO v_old_level
    FROM players
    WHERE player_id = p_player_id
    FOR UPDATE;

    IF NOT FOUND THEN
        RETURN;
    END IF;

    UPDATE players
    SET experience_points = experience_points + p_delta,
        level = GREATEST(level, level_for_xp(experience_points + p_delta))
    WHERE player_id = p_player_id
    RETURNING experience_points, level INTO v_new_xp, v_new_level;

    RETURN QUERY SELECT v_new_xp, v_old_level, v_new_level;
END;
$$;


-- update_player_stat_field: atomically update a stat field in stats JSONB
-- p_path: JSONB path array, e.g. ARRAY['current_dp'] or ARRAY['strength']
-- Caller must validate field_name against whitelist before calling.
CREATE OR REPLACE FUNCTION :schema_name.update_player_stat_field( -- noqa: PRS
    p_player_id UUID,
    p_path text[],
    p_delta numeric
)
RETURNS integer
LANGUAGE plpgsql
AS $$
DECLARE
    rows_updated integer;
BEGIN
    UPDATE players
    SET stats = jsonb_set(
        COALESCE(stats, '{}'::jsonb),
        p_path,
        to_jsonb((COALESCE((stats #>> p_path)::numeric, 0) + p_delta)::numeric),
        true
    )
    WHERE player_id = p_player_id;
    GET DIAGNOSTICS rows_updated = ROW_COUNT;
    RETURN rows_updated;
END;
$$;
