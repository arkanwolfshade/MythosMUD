-- Migration 011: Add container_item_instance_id column and container_contents table
-- Date: 2025-11-26
-- Description: Adds container_item_instance_id column to containers table and creates container_contents table
-- This migration ensures the test database has the correct schema from normalize_container_schema Alembic migration.
-- Status: ✅ ACTIVE
SET client_min_messages = WARNING;
SET search_path = public;
BEGIN;
-- Step 1: Add container_item_instance_id column to containers table if it doesn't exist
ALTER TABLE containers
ADD COLUMN IF NOT EXISTS container_item_instance_id VARCHAR(64);
-- Step 2: Add foreign key constraint if it doesn't exist
DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_constraint
    WHERE conname = 'fk_containers_container_item_instance'
) THEN
ALTER TABLE containers
ADD CONSTRAINT fk_containers_container_item_instance FOREIGN KEY (container_item_instance_id) REFERENCES item_instances(item_instance_id) ON DELETE
SET NULL;
END IF;
END $$;
-- Step 3: Add index if it doesn't exist
CREATE INDEX IF NOT EXISTS ix_containers_container_item_instance_id ON containers(container_item_instance_id);
-- Step 4: Create container_contents table if it doesn't exist
CREATE TABLE IF NOT EXISTS container_contents (
    container_id UUID NOT NULL,
    item_instance_id VARCHAR(64) NOT NULL,
    position INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (container_id, item_instance_id),
    FOREIGN KEY (container_id) REFERENCES containers(container_instance_id) ON DELETE CASCADE,
    FOREIGN KEY (item_instance_id) REFERENCES item_instances(item_instance_id) ON DELETE CASCADE
);
-- Step 5: Create indexes for container_contents if they don't exist
CREATE INDEX IF NOT EXISTS ix_container_contents_container_id ON container_contents(container_id);
CREATE INDEX IF NOT EXISTS ix_container_contents_item_instance_id ON container_contents(item_instance_id);
CREATE INDEX IF NOT EXISTS ix_container_contents_position ON container_contents(container_id, position);
COMMIT;
