-- player_effects holds every player status effect (ADR-029 step 3b-i, amending ADR-019).
--
-- The tick-driven effects (heal/damage over time, the lucidity drain) and spell effects move here from
-- players.status_effects, so a row needs:
--   * payload: the effect's parameters and mutable state (healing, damage, the drain's rate, beats and elapsed);
--   * instance_scoped: cleared when the player's instance is lost (see game/instance_state.py);
--   * remaining_seconds: game seconds left, counted down only while the player is online; NULL = until removed.
--
-- remaining_seconds replaces the tick arithmetic (duration - (current_tick - applied_at_tick)): the tick counter
-- restarts at 0 in every server process, so tick-based rows outlived restarts. Existing rows get 0, so the first
-- sweep expires them, which is right: their remaining time could not be computed. Idempotent: safe to replay.

-- migrate:up
ALTER TABLE player_effects ADD COLUMN IF NOT EXISTS payload jsonb NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE player_effects ADD COLUMN IF NOT EXISTS instance_scoped boolean NOT NULL DEFAULT false;
ALTER TABLE player_effects ADD COLUMN IF NOT EXISTS remaining_seconds integer DEFAULT 0;
ALTER TABLE player_effects ALTER COLUMN remaining_seconds DROP DEFAULT;
ALTER TABLE player_effects DROP COLUMN IF EXISTS duration;
ALTER TABLE player_effects DROP COLUMN IF EXISTS applied_at_tick;

-- migrate:down
ALTER TABLE player_effects ADD COLUMN IF NOT EXISTS duration integer NOT NULL DEFAULT 0;
ALTER TABLE player_effects ADD COLUMN IF NOT EXISTS applied_at_tick integer NOT NULL DEFAULT 0;
ALTER TABLE player_effects DROP COLUMN IF EXISTS remaining_seconds;
ALTER TABLE player_effects DROP COLUMN IF EXISTS instance_scoped;
ALTER TABLE player_effects DROP COLUMN IF EXISTS payload;
