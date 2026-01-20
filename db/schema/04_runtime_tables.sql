-- MythosMUD Schema: Runtime Tables
-- All runtime tables are created via DDL in this file and applied
-- using database management scripts (e.g., psql).
-- SQLAlchemy models are used for ORM relationships only, not for
-- table creation.
set client_min_messages = warning;
set search_path = public;
-- Users table (FastAPI Users v14+ compatible with UUID primary keys)
create table if not exists users (
    id uuid primary key default gen_random_uuid(),
    email varchar(255) not null unique,
    hashed_password varchar(1024) not null,
    is_active boolean not null default true,
    is_superuser boolean not null default false,
    is_verified boolean not null default false,
    username varchar(255) not null unique,
    display_name text not null default '',
    password_hash text null,
    is_admin boolean not null default false,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);
create index if not exists idx_users_username on users (username);
create index if not exists idx_users_email on users (email);
-- Players table (runtime game data)
create table if not exists players (
    player_id varchar(255) primary key,
    user_id uuid not null unique references users (id)
        on delete cascade,
    name varchar(50) not null unique,
    stats text not null default
        '{"strength": 50, "dexterity": 50, "constitution": 50,'
        ' "size": 50, "intelligence": 50, "power": 50,'
        ' "education": 50, "charisma": 50, "luck": 50,'
        ' "lucidity": 100, "occult": 0, "corruption": 0,'
        ' "current_dp": 20, "magic_points": 10,'
        ' "position": "standing"}',
    inventory text not null default '[]',
    status_effects text not null default '[]',
    current_room_id varchar(50) not null default
        'earth_arkhamcity_sanitarium_room_foyer_001',
    respawn_room_id varchar(100) default
        'earth_arkhamcity_sanitarium_room_foyer_001',
    experience_points integer not null default 0,
    level integer not null default 1,
    is_admin integer not null default 0,
    profession_id bigint references professions (id),
    created_at timestamptz not null default now(),
    last_active timestamptz not null default now()
);
create index if not exists idx_players_name on players (name);
create index if not exists idx_players_user_id on players (user_id);
create index if not exists idx_players_is_admin on players (is_admin);
create index if not exists idx_players_profession_id
on players (profession_id);
create index if not exists idx_players_current_room_id
on players (current_room_id);
create index if not exists idx_players_respawn_room_id
on players (respawn_room_id);
-- Player inventories table (JSON payload storage)
create table if not exists player_inventories (
    player_id varchar(255) primary key references players (player_id)
        on delete cascade,
    inventory_json text not null default '[]',
    equipped_json text not null default '{}',
    created_at timestamptz not null default now()
);
create index if not exists idx_player_inventories_player_id
on player_inventories (player_id);
-- Invites table (invite-only registration)
create table if not exists invites (
    id varchar(255) primary key,
    invite_code varchar(255) not null unique,
    created_by_user_id uuid references users (id)
        on delete set null,
    used_by_user_id uuid references users (id)
        on delete set null,
    used boolean not null default false,
    expires_at timestamptz,
    created_at timestamptz not null default now()
);
create index if not exists idx_invites_code on invites (invite_code);
create index if not exists idx_invites_used_by_user_id
on invites (used_by_user_id);
-- Player lucidity tables
create table if not exists player_lucidity (
    player_id varchar(255) primary key references players (player_id)
        on delete cascade,
    current_luc integer not null default 100 check (
        current_luc >= -100 and current_luc <= 100
    ),
    current_tier varchar(32) not null default 'lucid' check (
        current_tier in (
            'lucid',
            'uneasy',
            'fractured',
            'deranged',
            'catatonic'
        )
    ),
    liabilities text not null default '[]',
    last_updated_at timestamptz not null default now(),
    catatonia_entered_at timestamptz
);
create index if not exists idx_player_sanity_tier
on player_lucidity (current_tier);
create table if not exists sanity_adjustment_log (
    id bigint generated always as identity primary key,
    player_id varchar(255) not null references players (player_id)
        on delete cascade,
    delta integer not null,
    reason_code text not null,
    metadata text not null default '{}',
    location_id varchar(255),
    created_at timestamptz not null default now()
);
create index if not exists idx_sanity_adjustment_player_created
on sanity_adjustment_log (player_id, created_at);
create index if not exists idx_sanity_adjustment_player_id
on sanity_adjustment_log (player_id);
create table if not exists sanity_exposure_state (
    id bigint generated always as identity primary key,
    player_id varchar(255) not null references players (player_id)
        on delete cascade,
    entity_archetype text not null,
    encounter_count integer not null default 0,
    last_encounter_at timestamptz not null default now(),
    unique (player_id, entity_archetype)
);
create index if not exists idx_sanity_exposure_player_id
on sanity_exposure_state (player_id);
create table if not exists sanity_cooldowns (
    id bigint generated always as identity primary key,
    player_id varchar(255) not null references players (player_id)
        on delete cascade,
    action_code text not null,
    cooldown_expires_at timestamptz not null,
    unique (player_id, action_code)
);
create index if not exists idx_sanity_cooldowns_player_id
on sanity_cooldowns (player_id);
-- Item system tables
create table if not exists item_prototypes (
    prototype_id varchar(120) primary key,
    name varchar(120) not null,
    short_description varchar(255) not null,
    long_description text not null,
    item_type varchar(32) not null,
    weight double precision not null default 0.0,
    base_value integer not null default 0,
    durability integer,
    flags jsonb not null default '[]'::jsonb,
    wear_slots jsonb not null default '[]'::jsonb,
    stacking_rules jsonb not null default '{}'::jsonb,
    usage_restrictions jsonb not null default '{}'::jsonb,
    effect_components jsonb not null default '[]'::jsonb,
    metadata jsonb not null default '{}'::jsonb,
    tags jsonb not null default '[]'::jsonb,
    created_at timestamptz not null default now()
);
create table if not exists item_instances (
    item_instance_id varchar(64) primary key,
    prototype_id varchar(120) not null references item_prototypes (
        prototype_id
    )
        on delete cascade,
    owner_type varchar(32) not null default 'room',
    owner_id varchar(255),
    location_context varchar(255),
    quantity integer not null default 1,
    condition integer,
    flags_override jsonb not null default '[]'::jsonb,
    binding_state varchar(32),
    attunement_state jsonb not null default '{}'::jsonb,
    custom_name varchar(255),
    metadata jsonb not null default '{}'::jsonb,
    origin_source varchar(64),
    origin_metadata jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);
create index if not exists idx_item_instances_prototype_id
on item_instances (prototype_id);
create index if not exists idx_item_instances_owner
on item_instances (owner_type, owner_id);
create table if not exists item_component_states (
    id bigint generated always as identity primary key,
    item_instance_id varchar(64) not null
        references item_instances (item_instance_id)
        on delete cascade,
    component_id varchar(120) not null,
    state_payload jsonb not null default '{}'::jsonb,
    updated_at timestamptz not null default now(),
    unique (item_instance_id, component_id)
);
create index if not exists idx_item_component_states_instance_id
on item_component_states (item_instance_id);
-- NPC Definitions (runtime) - matches SQLAlchemy model
create table if not exists npc_definitions (
    id bigint generated always as identity primary key,
    name varchar(100) not null,
    description text,
    npc_type varchar(20) not null check (
        npc_type in (
            'shopkeeper',
            'quest_giver',
            'passive_mob',
            'aggressive_mob'
        )
    ),
    sub_zone_id varchar(50) not null,
    room_id varchar(50),
    required_npc boolean not null default false,
    max_population integer not null default 1,
    spawn_probability real not null default 1.0,
    base_stats text not null default '{}',
    behavior_config text not null default '{}',
    ai_integration_stub text not null default '{}',
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);
create index if not exists idx_npc_definitions_sub_zone
on npc_definitions (sub_zone_id);
create index if not exists idx_npc_definitions_type
on npc_definitions (npc_type);
create index if not exists idx_npc_definitions_required
on npc_definitions (required_npc);
create index if not exists idx_npc_definitions_name
on npc_definitions (name);
create unique index if not exists idx_npc_definitions_name_sub_zone
on npc_definitions (name, sub_zone_id);
-- NPC Spawn Rules (runtime)
create table if not exists npc_spawn_rules (
    id bigint generated always as identity primary key,
    npc_definition_id bigint not null
        references npc_definitions (id)
        on delete cascade,
    sub_zone_id varchar(50) not null,
    min_population integer default 0,
    max_population integer default 999,
    spawn_conditions text not null default '{}'
);
create index if not exists idx_npc_spawn_rules_sub_zone
on npc_spawn_rules (sub_zone_id);
create index if not exists idx_npc_spawn_rules_npc_def
on npc_spawn_rules (npc_definition_id);
-- NPC Relationships (runtime)
create table if not exists npc_relationships (
    id bigint generated always as identity primary key,
    npc_id_1 bigint not null references npc_definitions (id)
        on delete cascade,
    npc_id_2 bigint not null references npc_definitions (id)
        on delete cascade,
    relationship_type varchar(20) not null check (
        relationship_type in ('ally', 'enemy', 'neutral', 'follower')
    ),
    relationship_strength real default 0.5,
    unique (npc_id_1, npc_id_2)
);
create index if not exists idx_npc_relationships_npc1
on npc_relationships (npc_id_1);
create index if not exists idx_npc_relationships_npc2
on npc_relationships (npc_id_2);

-- ============================================================================
-- Table and Column Comments
-- ============================================================================

-- Table comments
comment on table users is 'Stores user account information for authentication and authorization.';
comment on table players is 'Stores runtime game data for player characters.';
comment on table player_inventories is 'Stores JSON payloads for player inventory and equipped items.';
comment on table invites is 'Manages invite-only registration system with expiration tracking.';
comment on table player_lucidity is 'Tracks player lucidity (sanity) state and tier.';
comment on table sanity_adjustment_log is 'Immutable ledger for every lucidity gain or loss event.';
comment on table sanity_exposure_state is 'Tracks repeated exposure to particular eldritch archetypes.';
comment on table sanity_cooldowns is 'Cooldown tracker for recovery rituals and hallucination timers.';
comment on table item_prototypes is 'Static reference data for item types and their properties.';
comment on table item_instances is 'Runtime instances of items in the game world.';
comment on table item_component_states is 'Component-specific state data for item instances.';
comment on table npc_definitions is 'Static reference data for NPC types and their configurations.';
comment on table npc_spawn_rules is 'Rules governing NPC spawning behavior in subzones.';
comment on table npc_relationships is 'Relationship mappings between NPCs (ally, enemy, neutral, follower).';

-- Column comments for critical columns
comment on column users.id is 'Primary key: UUID generated automatically.';
comment on column users.email is 'User email address (must be unique).';
comment on column users.username is 'User login name (must be unique).';
comment on column players.player_id is 'Primary key: Unique identifier for the player character.';
comment on column players.user_id is 'Foreign key to users table. Links player to user account.';
comment on column players.name is 'Character name (must be unique, case-sensitive).';
comment on column players.stats is 'JSON object containing character statistics (strength, dexterity, etc.).';
comment on column players.inventory is 'JSON array of inventory items.';
comment on column players.status_effects is 'JSON array of active status effects.';
comment on column player_lucidity.current_luc is 'Current lucidity value (-100 to +100).';
comment on column player_lucidity.current_tier is 'Current lucidity tier: lucid, uneasy, fractured, deranged, or catatonic.';
comment on column sanity_adjustment_log.delta is 'Change in lucidity value (positive for gain, negative for loss).';
comment on column sanity_adjustment_log.reason_code is 'Code identifying the reason for the lucidity adjustment.';
