-- MythosMUD Schema: Identity (users/players), Professions, Invites, Muting, and ID maps
-- Runtime domains use v4 UUIDs assigned during migration; static (professions/invites if static) use v5 via loader.
SET client_min_messages = WARNING;
SET search_path = public;
-- Professions (static reference)
-- NOTE: SQLAlchemy uses Integer primary key, not UUID
CREATE TABLE IF NOT EXISTS professions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    flavor_text TEXT NOT NULL,
    stat_requirements TEXT NOT NULL DEFAULT '{}',
    -- JSON
    mechanical_effects TEXT NOT NULL DEFAULT '{}',
    -- JSON
    is_available BOOLEAN NOT NULL DEFAULT true
);
-- Users (runtime)
-- NOTE: Created in 04_runtime_tables.sql
-- Users table uses UUID id (from FastAPI Users SQLAlchemyBaseUserTableUUID)
-- Players (runtime)
-- NOTE: Created in 04_runtime_tables.sql
-- Players table uses player_id (VARCHAR(255)) as primary key
-- Invites (runtime)
-- NOTE: Created in 04_runtime_tables.sql
-- Muting rules (admin moderation)
CREATE TABLE IF NOT EXISTS muting_rules (
    id uuid PRIMARY KEY,
    target_type text NOT NULL,
    -- 'user' | 'player'
    target_id uuid NOT NULL,
    -- users.id or players.id
    reason text,
    created_by_user uuid REFERENCES users(id) ON DELETE
    SET NULL,
        is_active boolean NOT NULL DEFAULT true,
        created_at timestamptz NOT NULL DEFAULT now(),
        expires_at timestamptz
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_muting_active_per_target ON muting_rules(target_type, target_id)
WHERE is_active;
CREATE INDEX IF NOT EXISTS idx_muting_expires_at ON muting_rules(expires_at);
-- ID maps for migration from SQLite IDs (text UUIDs) to UUIDs
CREATE TABLE IF NOT EXISTS id_map_users (
    old_sqlite_id text PRIMARY KEY,
    new_uuid uuid NOT NULL UNIQUE,
    username text
);
CREATE TABLE IF NOT EXISTS id_map_players (
    old_sqlite_id text PRIMARY KEY,
    new_uuid uuid NOT NULL UNIQUE,
    user_uuid uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name text
);
