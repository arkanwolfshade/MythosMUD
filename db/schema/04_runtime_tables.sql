-- MythosMUD Schema: Runtime Tables
-- All runtime tables are created via DDL in this file and applied using database management scripts (e.g., psql).
-- SQLAlchemy models are used for ORM relationships only, not for table creation.
SET client_min_messages = WARNING;
SET search_path = public;
-- Users table (FastAPI Users v14+ compatible with UUID primary keys)
CREATE TABLE IF NOT EXISTS users (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    email varchar(255) NOT NULL UNIQUE,
    hashed_password varchar(1024) NOT NULL,
    is_active boolean NOT NULL DEFAULT true,
    is_superuser boolean NOT NULL DEFAULT false,
    is_verified boolean NOT NULL DEFAULT false,
    username varchar(255) NOT NULL UNIQUE,
    display_name varchar(255) NOT NULL DEFAULT '',
    password_hash varchar(255) NULL,
    is_admin boolean NOT NULL DEFAULT false,
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
-- Players table (runtime game data)
CREATE TABLE IF NOT EXISTS players (
    player_id varchar(255) PRIMARY KEY,
    user_id uuid NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    name varchar(50) NOT NULL UNIQUE,
    stats text NOT NULL DEFAULT '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10, "lucidity": 100, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "position": "standing"}',
    inventory text NOT NULL DEFAULT '[]',
    status_effects text NOT NULL DEFAULT '[]',
    current_room_id varchar(50) NOT NULL DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001',
    respawn_room_id varchar(100) DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001',
    experience_points integer NOT NULL DEFAULT 0,
    level integer NOT NULL DEFAULT 1,
    is_admin integer NOT NULL DEFAULT 0,
    profession_id integer REFERENCES professions(id),
    created_at timestamptz NOT NULL DEFAULT now(),
    last_active timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);
CREATE INDEX IF NOT EXISTS idx_players_is_admin ON players(is_admin);
CREATE INDEX IF NOT EXISTS idx_players_profession_id ON players(profession_id);
CREATE INDEX IF NOT EXISTS idx_players_current_room_id ON players(current_room_id);
CREATE INDEX IF NOT EXISTS idx_players_respawn_room_id ON players(respawn_room_id);
-- Player inventories table (JSON payload storage)
CREATE TABLE IF NOT EXISTS player_inventories (
    player_id varchar(255) PRIMARY KEY REFERENCES players(player_id) ON DELETE CASCADE,
    inventory_json text NOT NULL DEFAULT '[]',
    equipped_json text NOT NULL DEFAULT '{}',
    created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_player_inventories_player_id ON player_inventories(player_id);
-- Invites table (invite-only registration)
CREATE TABLE IF NOT EXISTS invites (
    id varchar(255) PRIMARY KEY,
    invite_code varchar(255) NOT NULL UNIQUE,
    created_by_user_id uuid REFERENCES users(id) ON DELETE
    SET NULL,
        used_by_user_id uuid REFERENCES users(id) ON DELETE
    SET NULL,
        used boolean NOT NULL DEFAULT false,
        expires_at timestamptz,
        created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_invites_code ON invites(invite_code);
CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
-- Player lucidity tables
CREATE TABLE IF NOT EXISTS player_lucidity (
    player_id varchar(255) PRIMARY KEY REFERENCES players(player_id) ON DELETE CASCADE,
    current_luc integer NOT NULL DEFAULT 100 CHECK (
        current_luc BETWEEN -100 AND 100
    ),
    current_tier varchar(32) NOT NULL DEFAULT 'lucid' CHECK (
        current_tier IN (
            'lucid',
            'uneasy',
            'fractured',
            'deranged',
            'catatonic'
        )
    ),
    liabilities text NOT NULL DEFAULT '[]',
    last_updated_at timestamptz NOT NULL DEFAULT now(),
    catatonia_entered_at timestamptz
);
CREATE INDEX IF NOT EXISTS idx_player_sanity_tier ON player_sanity(current_tier);
CREATE TABLE IF NOT EXISTS sanity_adjustment_log (
    id serial PRIMARY KEY,
    player_id varchar(255) NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    delta integer NOT NULL,
    reason_code varchar(64) NOT NULL,
    metadata text NOT NULL DEFAULT '{}',
    location_id varchar(255),
    created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_sanity_adjustment_player_created ON sanity_adjustment_log(player_id, created_at);
CREATE INDEX IF NOT EXISTS idx_sanity_adjustment_player_id ON sanity_adjustment_log(player_id);
CREATE TABLE IF NOT EXISTS sanity_exposure_state (
    id serial PRIMARY KEY,
    player_id varchar(255) NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    entity_archetype varchar(128) NOT NULL,
    encounter_count integer NOT NULL DEFAULT 0,
    last_encounter_at timestamptz NOT NULL DEFAULT now(),
    UNIQUE (player_id, entity_archetype)
);
CREATE INDEX IF NOT EXISTS idx_sanity_exposure_player_id ON sanity_exposure_state(player_id);
CREATE TABLE IF NOT EXISTS sanity_cooldowns (
    id serial PRIMARY KEY,
    player_id varchar(255) NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    action_code varchar(64) NOT NULL,
    cooldown_expires_at timestamptz NOT NULL,
    UNIQUE (player_id, action_code)
);
CREATE INDEX IF NOT EXISTS idx_sanity_cooldowns_player_id ON sanity_cooldowns(player_id);
-- Item system tables
CREATE TABLE IF NOT EXISTS item_prototypes (
    prototype_id varchar(120) PRIMARY KEY,
    name varchar(120) NOT NULL,
    short_description varchar(255) NOT NULL,
    long_description text NOT NULL,
    item_type varchar(32) NOT NULL,
    weight double precision NOT NULL DEFAULT 0.0,
    base_value integer NOT NULL DEFAULT 0,
    durability integer,
    flags jsonb NOT NULL DEFAULT '[]'::jsonb,
    wear_slots jsonb NOT NULL DEFAULT '[]'::jsonb,
    stacking_rules jsonb NOT NULL DEFAULT '{}'::jsonb,
    usage_restrictions jsonb NOT NULL DEFAULT '{}'::jsonb,
    effect_components jsonb NOT NULL DEFAULT '[]'::jsonb,
    metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
    tags jsonb NOT NULL DEFAULT '[]'::jsonb,
    created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS item_instances (
    item_instance_id varchar(64) PRIMARY KEY,
    prototype_id varchar(120) NOT NULL REFERENCES item_prototypes(prototype_id) ON DELETE CASCADE,
    owner_type varchar(32) NOT NULL DEFAULT 'room',
    owner_id varchar(255),
    location_context varchar(255),
    quantity integer NOT NULL DEFAULT 1,
    condition integer,
    flags_override jsonb NOT NULL DEFAULT '[]'::jsonb,
    binding_state varchar(32),
    attunement_state jsonb NOT NULL DEFAULT '{}'::jsonb,
    custom_name varchar(255),
    metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
    origin_source varchar(64),
    origin_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_item_instances_prototype_id ON item_instances(prototype_id);
CREATE INDEX IF NOT EXISTS idx_item_instances_owner ON item_instances(owner_type, owner_id);
CREATE TABLE IF NOT EXISTS item_component_states (
    id serial PRIMARY KEY,
    item_instance_id varchar(64) NOT NULL REFERENCES item_instances(item_instance_id) ON DELETE CASCADE,
    component_id varchar(120) NOT NULL,
    state_payload jsonb NOT NULL DEFAULT '{}'::jsonb,
    updated_at timestamptz NOT NULL DEFAULT now(),
    UNIQUE (item_instance_id, component_id)
);
CREATE INDEX IF NOT EXISTS idx_item_component_states_instance_id ON item_component_states(item_instance_id);
-- NPC Definitions (runtime) - matches SQLAlchemy model
CREATE TABLE IF NOT EXISTS npc_definitions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    npc_type VARCHAR(20) NOT NULL CHECK (
        npc_type IN (
            'shopkeeper',
            'quest_giver',
            'passive_mob',
            'aggressive_mob'
        )
    ),
    sub_zone_id VARCHAR(50) NOT NULL,
    room_id VARCHAR(50),
    required_npc BOOLEAN NOT NULL DEFAULT FALSE,
    max_population INTEGER NOT NULL DEFAULT 1,
    spawn_probability REAL NOT NULL DEFAULT 1.0,
    base_stats TEXT NOT NULL DEFAULT '{}',
    behavior_config TEXT NOT NULL DEFAULT '{}',
    ai_integration_stub TEXT NOT NULL DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_npc_definitions_sub_zone ON npc_definitions(sub_zone_id);
CREATE INDEX IF NOT EXISTS idx_npc_definitions_type ON npc_definitions(npc_type);
CREATE INDEX IF NOT EXISTS idx_npc_definitions_required ON npc_definitions(required_npc);
CREATE INDEX IF NOT EXISTS idx_npc_definitions_name ON npc_definitions(name);
CREATE UNIQUE INDEX IF NOT EXISTS idx_npc_definitions_name_sub_zone ON npc_definitions(name, sub_zone_id);
-- NPC Spawn Rules (runtime)
CREATE TABLE IF NOT EXISTS npc_spawn_rules (
    id SERIAL PRIMARY KEY,
    npc_definition_id INTEGER NOT NULL REFERENCES npc_definitions(id) ON DELETE CASCADE,
    sub_zone_id VARCHAR(50) NOT NULL,
    min_population INTEGER DEFAULT 0,
    max_population INTEGER DEFAULT 999,
    spawn_conditions TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_sub_zone ON npc_spawn_rules(sub_zone_id);
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_npc_def ON npc_spawn_rules(npc_definition_id);
-- NPC Relationships (runtime)
CREATE TABLE IF NOT EXISTS npc_relationships (
    id SERIAL PRIMARY KEY,
    npc_id_1 INTEGER NOT NULL REFERENCES npc_definitions(id) ON DELETE CASCADE,
    npc_id_2 INTEGER NOT NULL REFERENCES npc_definitions(id) ON DELETE CASCADE,
    relationship_type VARCHAR(20) NOT NULL CHECK (
        relationship_type IN ('ally', 'enemy', 'neutral', 'follower')
    ),
    relationship_strength REAL DEFAULT 0.5,
    UNIQUE(npc_id_1, npc_id_2)
);
CREATE INDEX IF NOT EXISTS idx_npc_relationships_npc1 ON npc_relationships(npc_id_1);
CREATE INDEX IF NOT EXISTS idx_npc_relationships_npc2 ON npc_relationships(npc_id_2);
