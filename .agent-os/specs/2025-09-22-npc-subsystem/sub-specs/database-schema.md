# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-09-22-npc-subsystem/spec.md

## Database Changes

### New Tables

#### npc_definitions

```sql
CREATE TABLE npc_definitions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    npc_type TEXT NOT NULL CHECK (npc_type IN ('shopkeeper', 'quest_giver', 'passive_mob', 'aggressive_mob')),
    zone_id TEXT NOT NULL,
    room_id TEXT,
    required_npc BOOLEAN DEFAULT FALSE,
    max_population INTEGER DEFAULT 1,
    spawn_probability REAL DEFAULT 1.0,
    base_stats JSON, -- HP, MP, STR, DEX, etc.
    behavior_config JSON, -- Behavior-specific configuration
    ai_integration_stub JSON, -- Future AI configuration
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### npc_spawn_rules

```sql
CREATE TABLE npc_spawn_rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npc_definition_id INTEGER NOT NULL,
    zone_id TEXT NOT NULL,
    min_players INTEGER DEFAULT 0,
    max_players INTEGER DEFAULT 999,
    spawn_conditions JSON, -- Time-based, event-based conditions
    FOREIGN KEY (npc_definition_id) REFERENCES npc_definitions(id) ON DELETE CASCADE
);
```

#### npc_relationships

```sql
CREATE TABLE npc_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npc_id_1 INTEGER NOT NULL,
    npc_id_2 INTEGER NOT NULL,
    relationship_type TEXT NOT NULL CHECK (relationship_type IN ('ally', 'enemy', 'neutral', 'follower')),
    relationship_strength REAL DEFAULT 0.5,
    FOREIGN KEY (npc_id_1) REFERENCES npc_definitions(id) ON DELETE CASCADE,
    FOREIGN KEY (npc_id_2) REFERENCES npc_definitions(id) ON DELETE CASCADE,
    UNIQUE(npc_id_1, npc_id_2)
);
```

### Indexes and Constraints

```sql
-- Performance indexes
CREATE INDEX idx_npc_definitions_zone ON npc_definitions(zone_id);
CREATE INDEX idx_npc_definitions_type ON npc_definitions(npc_type);
CREATE INDEX idx_npc_definitions_required ON npc_definitions(required_npc);
CREATE INDEX idx_npc_spawn_rules_zone ON npc_spawn_rules(zone_id);
CREATE INDEX idx_npc_relationships_npc1 ON npc_relationships(npc_id_1);
CREATE INDEX idx_npc_relationships_npc2 ON npc_relationships(npc_id_2);

-- Unique constraints
CREATE UNIQUE INDEX idx_npc_definitions_name_zone ON npc_definitions(name, zone_id);
```

## Rationale

### npc_definitions Table

**Purpose**: Central repository for all NPC static data and configuration

**JSON Fields**: Flexible configuration for stats and behaviors without schema changes

**Required NPC Flag**: Ensures critical NPCs (shopkeepers) always spawn
- **Population Control**: Max population and spawn probability for zone management

### npc_spawn_rules Table

**Purpose**: Fine-grained control over NPC spawning based on player count and conditions

**Scalability**: Allows dynamic NPC population based on server load

**Flexibility**: JSON conditions field supports complex spawning logic

### npc_relationships Table

**Purpose**: Enables NPC-to-NPC interactions and social dynamics

**Performance**: Indexed for fast relationship lookups during NPC decision making

**Extensibility**: Relationship strength allows for nuanced NPC behaviors

### Performance Considerations

**Zone-based Indexes**: Fast lookups for zone-specific NPC operations

**Type-based Indexes**: Efficient filtering by NPC type for behavior processing

**Relationship Indexes**: Quick access to NPC relationships for social behaviors
- **JSON Storage**: Balances flexibility with query performance for configuration data

### Data Integrity Rules

**Foreign Key Constraints**: Ensures referential integrity between related tables

**Check Constraints**: Validates NPC types and relationship types at database level

**Unique Constraints**: Prevents duplicate NPC names within zones
- **Cascade Deletes**: Maintains data consistency when NPCs are removed
