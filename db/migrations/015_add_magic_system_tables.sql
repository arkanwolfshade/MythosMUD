-- Migration: Add Magic System Tables
-- Description: Creates the spells and player_spells tables for the
-- magic/spellcasting system
-- Date: 2025-01-XX

-- Create spells table (global spell registry)
create table if not exists spells (
    spell_id varchar(255) primary key,
    name varchar(100) not null unique,
    description text not null,
    school varchar(50) not null check (
        school in ('mythos', 'clerical', 'elemental', 'other')
    ),
    mp_cost integer not null check (mp_cost >= 0),
    lucidity_cost integer not null default 0
    check (lucidity_cost >= 0),
    corruption_on_learn integer not null default 0
    check (corruption_on_learn >= 0),
    corruption_on_cast integer not null default 0
    check (corruption_on_cast >= 0),
    casting_time_seconds integer not null default 0
    check (casting_time_seconds >= 0),
    target_type varchar(50) not null check (
        target_type in ('self', 'entity', 'location', 'area', 'all')
    ),
    range_type varchar(50) not null check (
        range_type in (
            'touch', 'same_room', 'adjacent_room', 'unlimited'
        )
    ),
    effect_type varchar(50) not null,
    effect_data jsonb not null default '{}',
    materials jsonb not null default '[]',
    created_at timestamptz not null default now()
);

-- Create indexes for common queries
create index if not exists idx_spells_school on spells (school);
create index if not exists idx_spells_name on spells (name);

-- Create player_spells table (learned spells)
create table if not exists player_spells (
    id bigint generated always as identity primary key,
    player_id uuid not null references players (player_id)
        on delete cascade,
    spell_id varchar(255) not null references spells (spell_id)
        on delete cascade,
    mastery integer not null default 0
        check (mastery >= 0 and mastery <= 100),
    learned_at timestamptz not null default now(),
    last_cast_at timestamptz,
    times_cast integer not null default 0,
    unique (player_id, spell_id)
);

-- Create indexes for player_spells
create index if not exists idx_player_spells_player_id
on player_spells (player_id);
create index if not exists idx_player_spells_spell_id
on player_spells (spell_id);

-- ============================================================================
-- Table and Column Comments
-- ============================================================================

-- Table comments
comment on table spells is 'Global spell registry with spell definitions and properties.';
comment on table player_spells is 'Tracks spells learned by players and their mastery levels.';

-- Column comments
comment on column spells.spell_id is 'Primary key: Unique identifier for the spell.';
comment on column spells.name is 'Spell name (must be unique).';
comment on column spells.school is 'Spell school: mythos, clerical, elemental, or other.';
comment on column player_spells.id is 'Primary key: bigint generated always as identity.';
comment on column player_spells.mastery is 'Spell mastery level (0-100).';
