-- Add player_skills table (character creation revamp 4.3)
-- Run with: psql -h <host> -p <port> -U <user> -d <database> -f 025_add_player_skills_table.sql

CREATE TABLE IF NOT EXISTS player_skills (
    player_id UUID NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
    skill_id BIGINT NOT NULL REFERENCES skills (id) ON DELETE CASCADE,
    value INTEGER NOT NULL CHECK (value >= 0 AND value <= 100),
    PRIMARY KEY (player_id, skill_id)
);

CREATE INDEX IF NOT EXISTS idx_player_skills_player_id ON player_skills (player_id);
CREATE INDEX IF NOT EXISTS idx_player_skills_skill_id ON player_skills (skill_id);

COMMENT ON TABLE player_skills IS 'Per-character skill values; created at character creation and updated on level-up improvement.';
COMMENT ON COLUMN player_skills.value IS 'Skill percentage 0-100; max 99 for improvement cap.';
