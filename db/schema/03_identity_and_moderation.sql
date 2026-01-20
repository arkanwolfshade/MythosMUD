-- MythosMUD Schema: Identity (users/players), Professions, Invites,
-- Muting, and ID maps
-- Runtime domains use v4 UUIDs assigned during migration; static
-- (professions/invites if static) use v5 via loader.
set client_min_messages = warning;
set search_path = public;
-- Professions (static reference)
-- NOTE: SQLAlchemy uses Integer primary key, not UUID
create table if not exists professions (
    id bigint generated always as identity primary key,
    name text not null unique,
    description text not null,
    flavor_text text not null,
    stat_requirements text not null default '{}',
    -- JSON
    mechanical_effects text not null default '{}',
    -- JSON
    is_available boolean not null default true
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
create table if not exists muting_rules (
    id uuid primary key,
    target_type text not null,
    -- 'user' | 'player'
    target_id uuid not null,
    -- users.id or players.id
    reason text,
    created_by_user uuid references users (id)
        on delete set null,
    is_active boolean not null default true,
    created_at timestamptz not null default now(),
    expires_at timestamptz
);
create unique index if not exists uq_muting_active_per_target
on muting_rules (target_type, target_id)
where is_active;
create index if not exists idx_muting_expires_at
on muting_rules (expires_at);
-- ID maps for migration from SQLite IDs (text UUIDs) to UUIDs
create table if not exists id_map_users (
    old_sqlite_id text primary key,
    new_uuid uuid not null unique,
    username text
);
create table if not exists id_map_players (
    old_sqlite_id text primary key,
    new_uuid uuid not null unique,
    user_uuid uuid not null references users (id)
        on delete cascade,
    name text
);

-- ============================================================================
-- Table and Column Comments
-- ============================================================================

-- Table comments
comment on table professions is 'Static reference data for character professions and their requirements.';
comment on table muting_rules is 'Admin moderation rules for muting users or players.';
comment on table id_map_users is 'Migration mapping table: maps old SQLite user IDs to new UUIDs.';
comment on table id_map_players is 'Migration mapping table: maps old SQLite player IDs to new UUIDs.';

-- Column comments
comment on column professions.id is 'Primary key: bigint generated always as identity.';
comment on column professions.name is 'Profession name (must be unique).';
comment on column professions.stat_requirements is 'JSON object defining minimum stat requirements for the profession.';
comment on column professions.mechanical_effects is 'JSON object defining mechanical bonuses/penalties for the profession.';
