-- Migration 012: Create containers table for unified container system
-- Date: 2025-11-15
-- Description: Create containers table to support environmental props, wearable gear, and corpses as storage containers
-- Status: ✅ ACTIVE
SET client_min_messages = WARNING;
SET search_path = public;
BEGIN;
-- Create containers table (if it doesn't exist)
CREATE TABLE IF NOT EXISTS containers (
    container_instance_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_type TEXT NOT NULL CHECK (
        source_type IN ('environment', 'equipment', 'corpse')
    ),
    owner_id UUID NULL,
    room_id VARCHAR(255) NULL,
    entity_id UUID NULL,
    lock_state TEXT NOT NULL DEFAULT 'unlocked' CHECK (lock_state IN ('unlocked', 'locked', 'sealed')),
    capacity_slots INTEGER NOT NULL CHECK (
        capacity_slots > 0
        AND capacity_slots <= 20
    ),
    weight_limit INTEGER NULL CHECK (
        weight_limit IS NULL
        OR weight_limit > 0
    ),
    decay_at TIMESTAMPTZ NULL,
    allowed_roles JSONB NULL,
    items_json JSONB NOT NULL DEFAULT '[]'::jsonb,
    metadata_json JSONB NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Add items_json column if it doesn't exist (for tables created from authoritative_schema.sql)
DO $$ BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'containers'
            AND column_name = 'items_json'
    ) THEN
        ALTER TABLE containers
        ADD COLUMN items_json JSONB NOT NULL DEFAULT '[]'::jsonb;
    END IF;
END $$;
-- Create indexes for common lookup patterns
CREATE INDEX IF NOT EXISTS idx_containers_room_id ON containers(room_id)
WHERE room_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_containers_entity_id ON containers(entity_id)
WHERE entity_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_containers_owner_id ON containers(owner_id)
WHERE owner_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_containers_source_type ON containers(source_type);
CREATE INDEX IF NOT EXISTS idx_containers_decay_at ON containers(decay_at)
WHERE decay_at IS NOT NULL;
-- Add foreign key constraints if referenced tables exist
DO $$ BEGIN -- Add foreign key to players table if it exists and has UUID player_id
IF EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
        AND table_name = 'players'
)
AND EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'players'
        AND column_name = 'player_id'
        AND data_type = 'uuid'
) THEN -- Add foreign key constraint for owner_id referencing players
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.table_constraints
    WHERE constraint_schema = 'public'
        AND constraint_name = 'containers_owner_id_fkey'
) THEN
ALTER TABLE containers
ADD CONSTRAINT containers_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES players(player_id) ON DELETE
SET NULL;
END IF;
-- Add foreign key constraint for entity_id referencing players
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.table_constraints
    WHERE constraint_schema = 'public'
        AND constraint_name = 'containers_entity_id_fkey'
) THEN
ALTER TABLE containers
ADD CONSTRAINT containers_entity_id_fkey FOREIGN KEY (entity_id) REFERENCES players(player_id) ON DELETE CASCADE;
END IF;
END IF;
END $$;
-- Add comment to table
COMMENT ON TABLE containers IS 'Unified container system for environmental props, wearable gear, and corpses';
COMMENT ON COLUMN containers.container_instance_id IS 'Unique identifier for container instance';
COMMENT ON COLUMN containers.source_type IS 'Type of container: environment (room objects), equipment (wearable), or corpse';
COMMENT ON COLUMN containers.owner_id IS 'UUID of player/NPC who owns the container (NULL for shared environmental containers)';
COMMENT ON COLUMN containers.room_id IS 'Room identifier for environmental and corpse containers';
COMMENT ON COLUMN containers.entity_id IS 'Player/NPC UUID when container is wearable equipment';
COMMENT ON COLUMN containers.lock_state IS 'Lock state: unlocked, locked, or sealed';
COMMENT ON COLUMN containers.capacity_slots IS 'Maximum number of inventory slots (1-20)';
COMMENT ON COLUMN containers.weight_limit IS 'Optional maximum weight capacity';
COMMENT ON COLUMN containers.decay_at IS 'Timestamp when corpse container should decay and be cleaned up';
COMMENT ON COLUMN containers.allowed_roles IS 'JSONB array of role names allowed to access container';
-- Add comment only if column exists
DO $$ BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND table_name = 'containers'
            AND column_name = 'items_json'
    ) THEN
        COMMENT ON COLUMN containers.items_json IS 'JSONB array of InventoryStack items stored in container';
    END IF;
END $$;
COMMENT ON COLUMN containers.metadata_json IS 'Optional JSONB metadata for container-specific configuration';
COMMIT;
