-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f lucidity.sql
--
-- Passive lucidity flux rate-override reads (replacing raw SQL in
-- server/services/passive_lucidity_flux/rate_overrides.py, #633), the catatonia clock, and the player registry's
-- lucidity part (ADR-029 step 5b-i). Depends on players (player_lucidity and lucidity_adjustment_log FKs).

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

-- get_player_lucidity: one player's player_lucidity row, or no row if they have none yet (the registry then uses the
-- starting values). Read with the rest of the player by the player registry (ADR-029 step 5b-i).
CREATE OR REPLACE FUNCTION :schema_name.get_player_lucidity(p_player_id UUID) -- noqa: PRS
RETURNS TABLE (
    current_lcd integer,
    current_tier character varying,
    liabilities text,
    last_updated_at timestamp with time zone,
    catatonia_entered_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT pl.current_lcd, pl.current_tier, pl.liabilities, pl.last_updated_at, pl.catatonia_entered_at
    FROM player_lucidity pl
    WHERE pl.player_id = p_player_id;
END;
$$;

-- upsert_player_lucidity: the player registry's lucidity write (ADR-029 step 5b-i). Creates the row on a player's
-- first change, else sets every column from the registry's copy.
CREATE OR REPLACE PROCEDURE :schema_name.upsert_player_lucidity(
    p_player_id UUID,
    p_current_lcd INTEGER,
    p_current_tier TEXT,
    p_liabilities TEXT,
    p_last_updated_at TIMESTAMP WITH TIME ZONE,
    p_catatonia_entered_at TIMESTAMP WITH TIME ZONE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO player_lucidity (
        player_id, current_lcd, current_tier, liabilities, last_updated_at, catatonia_entered_at
    )
    VALUES (
        p_player_id, p_current_lcd, p_current_tier, COALESCE(p_liabilities, '[]'),
        COALESCE(p_last_updated_at, now()), p_catatonia_entered_at
    )
    ON CONFLICT (player_id) DO UPDATE SET
        current_lcd = EXCLUDED.current_lcd,
        current_tier = EXCLUDED.current_tier,
        liabilities = EXCLUDED.liabilities,
        last_updated_at = EXCLUDED.last_updated_at,
        catatonia_entered_at = EXCLUDED.catatonia_entered_at;
END;
$$;

-- add_lucidity_adjustment_log: append one ledger row. The registry writes it in the same transaction as the
-- player_lucidity change it records (ADR-029 §3.2).
CREATE OR REPLACE PROCEDURE :schema_name.add_lucidity_adjustment_log(
    p_player_id UUID,
    p_delta INTEGER,
    p_reason_code TEXT,
    p_metadata TEXT,
    p_location_id TEXT,
    p_created_at TIMESTAMP WITH TIME ZONE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO lucidity_adjustment_log (player_id, delta, reason_code, metadata, location_id, created_at)
    VALUES (p_player_id, p_delta, p_reason_code, COALESCE(p_metadata, '{}'), p_location_id, COALESCE(p_created_at, now()));
END;
$$;
