-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f lucidity.sql
--
-- Passive lucidity flux rate-override reads (replacing raw SQL in
-- server/services/passive_lucidity_flux/rate_overrides.py, #633), the catatonia clock, and the player registry's
-- lucidity, cooldown and exposure parts (ADR-029 steps 5b-i, 5b-ii). Depends on players (the tables' FKs).

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

-- Replaced by get_player_lucidity_state (ADR-029 step 5b-ii).
DROP FUNCTION IF EXISTS :schema_name.get_player_lucidity(uuid); -- noqa: PRS

-- get_player_lucidity_state: everything the player registry holds about one player's lucidity, in one row (ADR-029
-- steps 5b-i and 5b-ii): the player_lucidity columns (NULL when the player has none yet; the registry then uses the
-- starting values), and their lucidity_cooldowns and lucidity_exposure_state rows as JSON arrays.
CREATE OR REPLACE FUNCTION :schema_name.get_player_lucidity_state(p_player_id UUID) -- noqa: PRS
RETURNS TABLE (
    current_lcd integer,
    current_tier character varying,
    liabilities text,
    last_updated_at timestamp with time zone,
    catatonia_entered_at timestamp with time zone,
    cooldowns jsonb,
    exposures jsonb
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        pl.current_lcd,
        pl.current_tier,
        pl.liabilities,
        pl.last_updated_at,
        pl.catatonia_entered_at,
        COALESCE(
            (
                SELECT jsonb_agg(jsonb_build_object('action_code', c.action_code, 'expires_at', c.cooldown_expires_at))
                FROM lucidity_cooldowns c
                WHERE c.player_id = p_player_id
            ),
            '[]'::jsonb
        ) AS cooldowns,
        COALESCE(
            (
                SELECT jsonb_agg(
                    jsonb_build_object(
                        'entity_archetype', e.entity_archetype,
                        'encounter_count', e.encounter_count,
                        'last_encounter_at', e.last_encounter_at
                    )
                )
                FROM lucidity_exposure_state e
                WHERE e.player_id = p_player_id
            ),
            '[]'::jsonb
        ) AS exposures
    FROM (SELECT p_player_id AS player_id) AS k
    LEFT JOIN player_lucidity pl ON pl.player_id = k.player_id;
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

-- replace_lucidity_cooldowns: the player registry's cooldown write (ADR-029 step 5b-ii). p_cooldowns is every
-- cooldown the player holds, as [{"action_code", "expires_at"}]: the rest are deleted, these are inserted or updated.
CREATE OR REPLACE PROCEDURE :schema_name.replace_lucidity_cooldowns(p_player_id UUID, p_cooldowns JSONB)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM lucidity_cooldowns c
    WHERE c.player_id = p_player_id
      AND c.action_code NOT IN (
          SELECT r.action_code FROM jsonb_to_recordset(COALESCE(p_cooldowns, '[]'::jsonb)) AS r (action_code text)
      );
    INSERT INTO lucidity_cooldowns (player_id, action_code, cooldown_expires_at)
    SELECT p_player_id, r.action_code, r.expires_at
    FROM jsonb_to_recordset(COALESCE(p_cooldowns, '[]'::jsonb)) AS r (action_code text, expires_at timestamptz)
    ON CONFLICT (player_id, action_code) DO UPDATE SET cooldown_expires_at = EXCLUDED.cooldown_expires_at;
END;
$$;

-- upsert_lucidity_exposures: the player registry's exposure write (ADR-029 step 5b-ii). p_exposures is every
-- archetype the player has met, as [{"entity_archetype", "encounter_count", "last_encounter_at"}]; exposure is
-- never forgotten, so rows are only inserted or updated.
CREATE OR REPLACE PROCEDURE :schema_name.upsert_lucidity_exposures(p_player_id UUID, p_exposures JSONB)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO lucidity_exposure_state (player_id, entity_archetype, encounter_count, last_encounter_at)
    SELECT p_player_id, r.entity_archetype, r.encounter_count, r.last_encounter_at
    FROM jsonb_to_recordset(COALESCE(p_exposures, '[]'::jsonb))
        AS r (entity_archetype text, encounter_count integer, last_encounter_at timestamptz)
    ON CONFLICT (player_id, entity_archetype) DO UPDATE SET
        encounter_count = EXCLUDED.encounter_count,
        last_encounter_at = EXCLUDED.last_encounter_at;
END;
$$;
