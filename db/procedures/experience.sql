-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f experience.sql
--
-- Experience procedures. Replaces raw SQL in ExperienceRepository.

-- update_player_xp: atomically add delta to experience_points
CREATE OR REPLACE FUNCTION :schema_name.update_player_xp( -- noqa: PRS
    p_player_id UUID,
    p_delta integer
)
RETURNS integer
LANGUAGE plpgsql
AS $$
DECLARE
    rows_updated integer;
BEGIN
    UPDATE players
    SET experience_points = experience_points + p_delta
    WHERE player_id = p_player_id;
    GET DIAGNOSTICS rows_updated = ROW_COUNT;
    RETURN rows_updated;
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
