-- MythosMUD Database Schema
-- SQLite DDL for users, players, and invites tables
-- Users table for authentication (FastAPI Users v14 compatible)
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY NOT NULL,
    -- UUID as TEXT for SQLite compatibility
    email TEXT UNIQUE NOT NULL,
    username TEXT NOT NULL,
    hashed_password TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    is_superuser BOOLEAN NOT NULL DEFAULT 0,
    is_verified BOOLEAN NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- Professions table for character professions
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
-- Insert MVP professions (Tramp and Gutter Rat)
INSERT
    OR IGNORE INTO professions (
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
    ),
    (
        2,
        'Strongman',
        'A physically powerful individual with exceptional strength',
        'You have developed your body through years of physical training, making you capable of feats that would challenge lesser mortals.',
        '{"strength": 10}',
        '{}'
    );
-- Players table for game data
CREATE TABLE IF NOT EXISTS players (
    player_id TEXT PRIMARY KEY NOT NULL,
    user_id TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    stats TEXT NOT NULL DEFAULT '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100}',
    inventory TEXT NOT NULL DEFAULT '[]',
    status_effects TEXT NOT NULL DEFAULT '[]',
    current_room_id TEXT NOT NULL DEFAULT 'earth_arkhamcity_northside_intersection_derby_high',
    experience_points INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    is_admin INTEGER NOT NULL DEFAULT 0,
    profession_id INTEGER NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (profession_id) REFERENCES professions(id)
);
-- Invites table for invite-only registration
CREATE TABLE IF NOT EXISTS invites (
    id TEXT PRIMARY KEY NOT NULL,
    invite_code TEXT UNIQUE NOT NULL,
    created_by_user_id TEXT,
    used_by_user_id TEXT,
    used BOOLEAN NOT NULL DEFAULT 0,
    expires_at DATETIME,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by_user_id) REFERENCES users(id) ON DELETE
    SET NULL,
        FOREIGN KEY (used_by_user_id) REFERENCES users(id) ON DELETE
    SET NULL
);
-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_professions_available ON professions(is_available);
CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);
CREATE INDEX IF NOT EXISTS idx_players_is_admin ON players(is_admin);
CREATE INDEX IF NOT EXISTS idx_players_profession_id ON players(profession_id);
CREATE INDEX IF NOT EXISTS idx_invites_code ON invites(invite_code);
CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
-- Create case-insensitive unique constraints
CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username_unique ON users(username COLLATE NOCASE);
CREATE UNIQUE INDEX IF NOT EXISTS idx_players_name_unique ON players(name COLLATE NOCASE);
