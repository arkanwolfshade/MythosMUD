-- players.status_effects is gone (ADR-029 step 3b-ii). Since step 3b-i every status effect is a player_effects
-- row, and this column was unread and written as '[]'.
--
-- No data moves: anything still in it predates 3b-i and was transient tick state nothing reads. Reapply
-- db/procedures/players.sql with this migration; the row readers and upsert_player no longer name the column.
-- Idempotent: safe to replay.

-- migrate:up
ALTER TABLE players DROP COLUMN IF EXISTS status_effects;

-- migrate:down
ALTER TABLE players ADD COLUMN IF NOT EXISTS status_effects text NOT NULL DEFAULT '[]';
