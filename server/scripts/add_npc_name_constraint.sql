-- Add constraint to prevent NPC names from containing hyphen-number pattern
-- This ensures disambiguation suffixes like "rat-1", "dr-2" work properly
-- First, check if any existing NPCs violate this constraint
SELECT name
FROM npc_definitions
WHERE name REGEXP '.*-[0-9]+$';
-- Add a check constraint to prevent hyphen-number patterns
-- SQLite requires recreating the table to add constraints
-- First, create a new table with the constraint
CREATE TABLE npc_definitions_new (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK (
        name NOT LIKE '%-%'
        OR name NOT LIKE '%-[0-9]%'
    ),
    description TEXT,
    npc_type TEXT NOT NULL,
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
-- Copy data from old table to new table
INSERT INTO npc_definitions_new
SELECT *
FROM npc_definitions;
-- Drop the old table
DROP TABLE npc_definitions;
-- Rename the new table
ALTER TABLE npc_definitions_new
    RENAME TO npc_definitions;
-- Verify the constraint was added
PRAGMA table_info(npc_definitions);
