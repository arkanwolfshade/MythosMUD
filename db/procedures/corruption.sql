-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f corruption.sql
--
-- The player registry's corruption cooldown and ledger reads and writes (ADR-029 step 5c). The value itself is
-- stats.corruption, written through update_player_row. Both tables store naive UTC timestamps; these take and
-- return timestamptz and convert at the boundary. Depends on players (the tables' FKs).

-- get_player_corruption_cooldowns: every corruption cooldown the player holds, as [{"action_code", "expires_at"}]
-- (an empty array when there are none). The registry loads it with the rest of the player.
CREATE OR REPLACE FUNCTION :schema_name.get_player_corruption_cooldowns(p_player_id UUID) -- noqa: PRS
RETURNS JSONB
LANGUAGE plpgsql
STABLE
AS $$
BEGIN
    RETURN (
        SELECT COALESCE(
            jsonb_agg(
                jsonb_build_object(
                    'action_code', c.action_code,
                    'expires_at', c.cooldown_expires_at AT TIME ZONE 'UTC'
                )
                ORDER BY c.action_code
            ),
            '[]'::jsonb
        )
        FROM corruption_cooldowns AS c
        WHERE c.player_id = p_player_id
    );
END;
$$;

-- replace_corruption_cooldowns: the registry's corruption cooldown write. p_cooldowns is every cooldown the player
-- holds, as [{"action_code", "expires_at"}]: the rest are deleted, these are inserted or updated.
CREATE OR REPLACE PROCEDURE :schema_name.replace_corruption_cooldowns(p_player_id UUID, p_cooldowns JSONB)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM corruption_cooldowns c
    WHERE c.player_id = p_player_id
      AND c.action_code NOT IN (
          SELECT r.action_code FROM jsonb_to_recordset(COALESCE(p_cooldowns, '[]'::jsonb)) AS r (action_code text)
      );
    INSERT INTO corruption_cooldowns (player_id, action_code, cooldown_expires_at)
    SELECT p_player_id, r.action_code, r.expires_at AT TIME ZONE 'UTC'
    FROM jsonb_to_recordset(COALESCE(p_cooldowns, '[]'::jsonb)) AS r (action_code text, expires_at timestamptz)
    ON CONFLICT (player_id, action_code) DO UPDATE SET cooldown_expires_at = EXCLUDED.cooldown_expires_at;
END;
$$;

-- add_corruption_adjustment_log: append one ledger row, in the same transaction as the stats.corruption change it
-- records (ADR-029 §3.2).
CREATE OR REPLACE PROCEDURE :schema_name.add_corruption_adjustment_log(
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
    INSERT INTO corruption_adjustment_log (player_id, delta, reason_code, metadata, location_id, created_at)
    VALUES (
        p_player_id, p_delta, p_reason_code, COALESCE(p_metadata, '{}'), p_location_id,
        COALESCE(p_created_at, now()) AT TIME ZONE 'UTC'
    );
END;
$$;
