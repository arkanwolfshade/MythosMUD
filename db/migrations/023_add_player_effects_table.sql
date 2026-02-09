-- Add player_effects table (ADR-009 effects system)
-- Equivalent to Alembic revision add_player_effects_table (2026_02_09).
-- Run with: psql -h <host> -p <port> -U <user> -d <database> -f 023_add_player_effects_table.sql

CREATE TABLE IF NOT EXISTS player_effects (
    id UUID NOT NULL PRIMARY KEY,
    player_id UUID NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
    effect_type VARCHAR(64) NOT NULL,
    category VARCHAR(64) NOT NULL,
    duration INTEGER NOT NULL,
    applied_at_tick INTEGER NOT NULL,
    intensity INTEGER NOT NULL DEFAULT 1,
    source VARCHAR(128),
    visibility_level VARCHAR(32) NOT NULL DEFAULT 'visible',
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS ix_player_effects_player_id ON player_effects (player_id);
CREATE INDEX IF NOT EXISTS ix_player_effects_effect_type ON player_effects (effect_type);
CREATE INDEX IF NOT EXISTS ix_player_effects_category ON player_effects (category);
