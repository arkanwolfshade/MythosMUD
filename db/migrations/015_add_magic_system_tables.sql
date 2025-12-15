-- Migration: Add Magic System Tables
-- Description: Creates the spells and player_spells tables for the magic/spellcasting system
-- Date: 2025-01-XX

-- Create spells table (global spell registry)
CREATE TABLE IF NOT EXISTS spells (
    spell_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    school VARCHAR(50) NOT NULL CHECK (school IN ('mythos', 'clerical', 'elemental', 'other')),
    mp_cost INTEGER NOT NULL CHECK (mp_cost >= 0),
    lucidity_cost INTEGER NOT NULL DEFAULT 0 CHECK (lucidity_cost >= 0),
    corruption_on_learn INTEGER NOT NULL DEFAULT 0 CHECK (corruption_on_learn >= 0),
    corruption_on_cast INTEGER NOT NULL DEFAULT 0 CHECK (corruption_on_cast >= 0),
    casting_time_seconds INTEGER NOT NULL DEFAULT 0 CHECK (casting_time_seconds >= 0),
    target_type VARCHAR(50) NOT NULL CHECK (target_type IN ('self', 'entity', 'location', 'area', 'all')),
    range_type VARCHAR(50) NOT NULL CHECK (range_type IN ('touch', 'same_room', 'adjacent_room', 'unlimited')),
    effect_type VARCHAR(50) NOT NULL,
    effect_data JSONB NOT NULL DEFAULT '{}',
    materials JSONB NOT NULL DEFAULT '[]',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create indexes for common queries
CREATE INDEX IF NOT EXISTS idx_spells_school ON spells(school);
CREATE INDEX IF NOT EXISTS idx_spells_name ON spells(name);

-- Create player_spells table (learned spells)
CREATE TABLE IF NOT EXISTS player_spells (
    id SERIAL PRIMARY KEY,
    player_id UUID NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    spell_id VARCHAR(255) NOT NULL REFERENCES spells(spell_id) ON DELETE CASCADE,
    mastery INTEGER NOT NULL DEFAULT 0 CHECK (mastery >= 0 AND mastery <= 100),
    learned_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_cast_at TIMESTAMPTZ,
    times_cast INTEGER NOT NULL DEFAULT 0,
    UNIQUE(player_id, spell_id)
);

-- Create indexes for player_spells
CREATE INDEX IF NOT EXISTS idx_player_spells_player_id ON player_spells(player_id);
CREATE INDEX IF NOT EXISTS idx_player_spells_spell_id ON player_spells(spell_id);
