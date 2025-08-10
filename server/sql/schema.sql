-- MythosMUD Database Schema
-- SQLite DDL for users, players, and invites tables
-- Users table for authentication
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY NOT NULL,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    is_superuser BOOLEAN NOT NULL DEFAULT 0,
    is_verified BOOLEAN NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- Players table for game data
CREATE TABLE IF NOT EXISTS players (
    player_id TEXT PRIMARY KEY NOT NULL,
    user_id TEXT NOT NULL UNIQUE,
    name TEXT UNIQUE NOT NULL,
    stats TEXT NOT NULL DEFAULT '{"health": 100, "sanity": 100, "strength": 10}',
    inventory TEXT NOT NULL DEFAULT '[]',
    status_effects TEXT NOT NULL DEFAULT '[]',
    current_room_id TEXT NOT NULL DEFAULT 'earth_arkham_city_intersection_derby_high',
    experience_points INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
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
    FOREIGN KEY (created_by_user_id) REFERENCES users(user_id) ON DELETE
    SET NULL,
        FOREIGN KEY (used_by_user_id) REFERENCES users(user_id) ON DELETE
    SET NULL
);
-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);
CREATE INDEX IF NOT EXISTS idx_invites_code ON invites(invite_code);
CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
