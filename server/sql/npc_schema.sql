-- NPC Subsystem Database Schema
-- SQLite DDL for NPC tables: npc_definitions, npc_spawn_rules, npc_relationships
-- This schema supports the NPC subsystem with sub-zone-based population management

-- NPC Definitions table
-- Stores static NPC data including stats, behaviors, and configuration
CREATE TABLE IF NOT EXISTS npc_definitions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    npc_type TEXT NOT NULL CHECK (
        npc_type IN (
            'shopkeeper',
            'quest_giver',
            'passive_mob',
            'aggressive_mob'
        )
    ),
    sub_zone_id TEXT NOT NULL,
    room_id TEXT,
    required_npc BOOLEAN DEFAULT FALSE,
    max_population INTEGER DEFAULT 1,
    spawn_probability REAL DEFAULT 1.0,
    base_stats TEXT NOT NULL DEFAULT '{}',
    behavior_config TEXT NOT NULL DEFAULT '{}',
    ai_integration_stub TEXT NOT NULL DEFAULT '{}',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- NPC Spawn Rules table
-- Defines conditions under which NPCs should be spawned
CREATE TABLE IF NOT EXISTS npc_spawn_rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npc_definition_id INTEGER NOT NULL,
    sub_zone_id TEXT NOT NULL,
    min_players INTEGER DEFAULT 0,
    max_players INTEGER DEFAULT 999,
    spawn_conditions TEXT NOT NULL DEFAULT '{}',
    FOREIGN KEY (npc_definition_id) REFERENCES npc_definitions(id) ON DELETE CASCADE
);

-- NPC Relationships table
-- Defines relationships between NPCs (alliances, enmities, etc.)
CREATE TABLE IF NOT EXISTS npc_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npc_id_1 INTEGER NOT NULL,
    npc_id_2 INTEGER NOT NULL,
    relationship_type TEXT NOT NULL CHECK (
        relationship_type IN ('ally', 'enemy', 'neutral', 'follower')
    ),
    relationship_strength REAL DEFAULT 0.5,
    FOREIGN KEY (npc_id_1) REFERENCES npc_definitions(id) ON DELETE CASCADE,
    FOREIGN KEY (npc_id_2) REFERENCES npc_definitions(id) ON DELETE CASCADE,
    UNIQUE(npc_id_1, npc_id_2)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_npc_definitions_sub_zone ON npc_definitions(sub_zone_id);
CREATE INDEX IF NOT EXISTS idx_npc_definitions_type ON npc_definitions(npc_type);
CREATE INDEX IF NOT EXISTS idx_npc_definitions_required ON npc_definitions(required_npc);
CREATE INDEX IF NOT EXISTS idx_npc_definitions_name ON npc_definitions(name);
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_sub_zone ON npc_spawn_rules(sub_zone_id);
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_npc_def ON npc_spawn_rules(npc_definition_id);
CREATE INDEX IF NOT EXISTS idx_npc_relationships_npc1 ON npc_relationships(npc_id_1);
CREATE INDEX IF NOT EXISTS idx_npc_relationships_npc2 ON npc_relationships(npc_id_2);

-- Create unique constraints
CREATE UNIQUE INDEX IF NOT EXISTS idx_npc_definitions_name_sub_zone ON npc_definitions(name, sub_zone_id);
