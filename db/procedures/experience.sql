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

-- XP is awarded by the player registry (ADR-029 step 7b), which holds the same curve in models/player_xp.py;
-- an integration test checks that the two agree. The stored award_player_xp function is gone.
DROP FUNCTION IF EXISTS :schema_name.award_player_xp(uuid, integer); -- noqa: PRS


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
