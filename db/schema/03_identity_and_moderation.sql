-- MythosMUD Schema: Identity (users/players), Professions, Invites, Muting, and ID maps
-- Runtime domains use v4 UUIDs assigned during migration; static (professions/invites if static) use v5 via loader.

SET client_min_messages = WARNING;
SET search_path = public;

-- Professions (static reference)
CREATE TABLE IF NOT EXISTS professions (
    id              uuid PRIMARY KEY,
    stable_id       text NOT NULL UNIQUE,  -- e.g., 'occultist', 'investigator'
    name            text NOT NULL,
    description     text,
    attributes      jsonb NOT NULL DEFAULT '{}'::jsonb
);

-- Users (runtime)
CREATE TABLE IF NOT EXISTS users (
    id              uuid PRIMARY KEY,
    username        text NOT NULL UNIQUE,      -- login handle; server should enforce policy
    display_name    text NOT NULL,
    email           text,                      -- stored as bogus/derived per project privacy rules
    password_hash   text,                      -- if applicable to server auth
    is_admin        boolean NOT NULL DEFAULT false,
    created_at      timestamptz NOT NULL DEFAULT now(),
    updated_at      timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_users_is_admin ON users(is_admin);

-- Players (runtime, associated with Users)
CREATE TABLE IF NOT EXISTS players (
    id              uuid PRIMARY KEY,
    user_id         uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name            text NOT NULL UNIQUE,      -- character name
    profession_id   uuid REFERENCES professions(id) ON DELETE SET NULL,
    sanity_score    integer NOT NULL DEFAULT 100,
    attributes      jsonb NOT NULL DEFAULT '{}'::jsonb,
    created_at      timestamptz NOT NULL DEFAULT now(),
    updated_at      timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_players_user ON players(user_id);
CREATE INDEX IF NOT EXISTS idx_players_profession ON players(profession_id);

-- Invites (can be treated as static seed data or runtime; stored for server use)
CREATE TABLE IF NOT EXISTS invites (
    id              uuid PRIMARY KEY,
    stable_id       text UNIQUE,               -- present if seeded from static JSON
    code            text NOT NULL UNIQUE,      -- human-entered invite code
    description     text,
    created_by_user uuid REFERENCES users(id) ON DELETE SET NULL,
    is_active       boolean NOT NULL DEFAULT true,
    created_at      timestamptz NOT NULL DEFAULT now(),
    expires_at      timestamptz
);
CREATE INDEX IF NOT EXISTS idx_invites_active ON invites(is_active);
CREATE INDEX IF NOT EXISTS idx_invites_expires_at ON invites(expires_at);

-- Muting rules (admin moderation)
CREATE TABLE IF NOT EXISTS muting_rules (
    id              uuid PRIMARY KEY,
    target_type     text NOT NULL,             -- 'user' | 'player'
    target_id       uuid NOT NULL,             -- users.id or players.id
    reason          text,
    created_by_user uuid REFERENCES users(id) ON DELETE SET NULL,
    is_active       boolean NOT NULL DEFAULT true,
    created_at      timestamptz NOT NULL DEFAULT now(),
    expires_at      timestamptz
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_muting_active_per_target
    ON muting_rules(target_type, target_id)
    WHERE is_active;
CREATE INDEX IF NOT EXISTS idx_muting_expires_at ON muting_rules(expires_at);

-- ID maps for migration from SQLite IDs (text UUIDs) to UUIDs
CREATE TABLE IF NOT EXISTS id_map_users (
    old_sqlite_id   text PRIMARY KEY,
    new_uuid        uuid NOT NULL UNIQUE,
    username        text
);

CREATE TABLE IF NOT EXISTS id_map_players (
    old_sqlite_id   text PRIMARY KEY,
    new_uuid        uuid NOT NULL UNIQUE,
    user_uuid       uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name            text
);
