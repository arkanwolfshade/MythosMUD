-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f lucidity.sql
--
-- Passive lucidity flux rate-override reads. Replaces raw SQL in
-- server/services/passive_lucidity_flux/rate_overrides.py (#633).

-- get_lucidity_rate_overrides: fetch zone- and subzone-level special_rules overrides in one
-- polymorphic result set. subzone_stable_id IS NULL marks a zone-level row; callers already key
-- on that sentinel (server/services/passive_lucidity_flux/rate_overrides.py's
-- _process_override_row). Preserves the original single-round-trip UNION ALL shape.
CREATE OR REPLACE FUNCTION :schema_name.get_lucidity_rate_overrides() -- noqa: PRS
RETURNS TABLE (
    zone_stable_id text,
    subzone_stable_id text,
    special_rules jsonb
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        z.stable_id AS zone_stable_id,
        NULL::text AS subzone_stable_id,
        z.special_rules
    FROM zones z
    WHERE z.special_rules IS NOT NULL
    UNION ALL
    SELECT
        z.stable_id AS zone_stable_id,
        sz.stable_id AS subzone_stable_id,
        sz.special_rules
    FROM subzones sz
    JOIN zones z ON sz.zone_id = z.id
    WHERE sz.special_rules IS NOT NULL
    ORDER BY zone_stable_id, subzone_stable_id;
END;
$$;

-- get_catatonic_player_ids: players inside the catatonia countdown, 0 >= LCD > -10 (#1148).
-- Per-tick source for server/app/game_tick_catatonia.py; mirrors get_players_not_clearly_alive for the DP
-- bleed-out clock, so it covers offline players too. LCD <= -10 is delirium's, not the clock's. Soft-deleted
-- players are skipped. In the normal case nobody is catatonic and this returns no rows.
CREATE OR REPLACE FUNCTION :schema_name.get_catatonic_player_ids()
RETURNS TABLE (
    player_id uuid
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT pl.player_id
    FROM player_lucidity pl
    JOIN players p ON p.player_id = pl.player_id
    WHERE pl.current_lcd <= 0
      AND pl.current_lcd > -10
      AND p.is_deleted IS NOT TRUE;
END;
$$;
