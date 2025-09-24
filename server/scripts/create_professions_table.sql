-- Create Professions Table DDL Script
-- This script creates the professions table and related indexes for the profession system
-- Create the professions table
CREATE TABLE IF NOT EXISTS professions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    flavor_text TEXT NOT NULL,
    stat_requirements TEXT NOT NULL,
    -- JSON: {"strength": 12, "intelligence": 10}
    mechanical_effects TEXT NOT NULL,
    -- JSON: future bonuses/penalties
    is_available BOOLEAN NOT NULL DEFAULT 1
);
-- Create index for efficient filtering by availability
CREATE INDEX IF NOT EXISTS idx_professions_available ON professions(is_available);
-- Insert MVP professions (Tramp and Gutter Rat)
INSERT INTO professions (
        id,
        name,
        description,
        flavor_text,
        stat_requirements,
        mechanical_effects
    )
VALUES (
        0,
        'Tramp',
        'A wandering soul with no fixed abode',
        'You have learned to survive on the streets, finding shelter where you can and making do with what you have.',
        '{}',
        '{}'
    ),
    (
        1,
        'Gutter Rat',
        'A street-smart survivor of the urban underbelly',
        'You know the hidden passages and dark corners of the city, where others fear to tread.',
        '{}',
        '{}'
    );
-- Add profession_id column to players table
ALTER TABLE players
ADD COLUMN profession_id INTEGER NOT NULL DEFAULT 0;
-- Add foreign key constraint after seeding professions
ALTER TABLE players
ADD CONSTRAINT fk_players_profession FOREIGN KEY (profession_id) REFERENCES professions(id);
-- Create index on players.profession_id for efficient lookups
CREATE INDEX IF NOT EXISTS idx_players_profession_id ON players(profession_id);
