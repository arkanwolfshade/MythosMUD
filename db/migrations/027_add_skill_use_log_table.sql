-- Add skill_use_log table (character creation revamp 4.5)
-- Tracks successful skill use per character at current level for level-up improvement rolls.

CREATE TABLE IF NOT EXISTS skill_use_log (
    id BIGSERIAL PRIMARY KEY,
    player_id UUID NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
    skill_id BIGINT NOT NULL REFERENCES skills (id) ON DELETE CASCADE,
    character_level_at_use INTEGER NOT NULL CHECK (character_level_at_use >= 1),
    used_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT (NOW() AT TIME ZONE 'UTC')
);

CREATE INDEX IF NOT EXISTS idx_skill_use_log_player_level ON skill_use_log (player_id, character_level_at_use);
CREATE INDEX IF NOT EXISTS idx_skill_use_log_used_at ON skill_use_log (used_at);

COMMENT ON TABLE skill_use_log IS 'Successful skill uses per character at level; used for CoC-style improvement rolls on level-up.';
