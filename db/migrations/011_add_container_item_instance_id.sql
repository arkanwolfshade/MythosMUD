-- Migration 011: Add container_item_instance_id column and container_contents table
-- Date: 2025-11-26
-- Description: Adds container_item_instance_id column to containers table and creates container_contents table
-- This migration ensures the test database has the correct schema from normalize_container_schema Alembic migration.
-- Status: ✅ ACTIVE
SET client_min_messages = WARNING;
SET search_path = public;
-- Step 1: Verify containers table exists before modifying it
DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
        AND table_name = 'containers'
) THEN RAISE EXCEPTION 'containers table does not exist. Migration must run after authoritative_schema.sql or Alembic migrations';
END IF;
END $$;
-- Step 2: Add container_item_instance_id column to containers table if it doesn't exist
DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'containers'
        AND column_name = 'container_item_instance_id'
) THEN
ALTER TABLE containers
ADD COLUMN container_item_instance_id VARCHAR(64);
RAISE NOTICE 'Added container_item_instance_id column to containers table';
-- Verify the column was actually created
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'containers'
        AND column_name = 'container_item_instance_id'
) THEN RAISE EXCEPTION 'Failed to create container_item_instance_id column';
END IF;
ELSE RAISE NOTICE 'container_item_instance_id column already exists in containers table';
END IF;
END $$;
-- Step 3: Verify item_instances table exists before creating foreign key
DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
        AND table_name = 'item_instances'
) THEN RAISE EXCEPTION 'item_instances table does not exist. Migration must run after authoritative_schema.sql';
END IF;
END $$;
-- Step 4: Add foreign key constraint if it doesn't exist
DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_constraint
    WHERE conname = 'fk_containers_container_item_instance'
) THEN
ALTER TABLE containers
ADD CONSTRAINT fk_containers_container_item_instance FOREIGN KEY (container_item_instance_id) REFERENCES item_instances(item_instance_id) ON DELETE
SET NULL;
RAISE NOTICE 'Added foreign key constraint fk_containers_container_item_instance';
ELSE RAISE NOTICE 'Foreign key constraint fk_containers_container_item_instance already exists';
END IF;
END $$;
-- Step 5: Add index if it doesn't exist
CREATE INDEX IF NOT EXISTS ix_containers_container_item_instance_id ON containers(container_item_instance_id);
-- Step 6: Create container_contents table if it doesn't exist
DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
        AND table_name = 'container_contents'
) THEN CREATE TABLE container_contents (
    container_id UUID NOT NULL,
    item_instance_id VARCHAR(64) NOT NULL,
    position INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (container_id, item_instance_id),
    FOREIGN KEY (container_id) REFERENCES containers(container_instance_id) ON DELETE CASCADE,
    FOREIGN KEY (item_instance_id) REFERENCES item_instances(item_instance_id) ON DELETE CASCADE
);
RAISE NOTICE 'Created container_contents table';
-- Verify the table was actually created
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
        AND table_name = 'container_contents'
) THEN RAISE EXCEPTION 'Failed to create container_contents table';
END IF;
ELSE RAISE NOTICE 'container_contents table already exists';
END IF;
END $$;
-- Step 7: Create indexes for container_contents if they don't exist
CREATE INDEX IF NOT EXISTS ix_container_contents_container_id ON container_contents(container_id);
CREATE INDEX IF NOT EXISTS ix_container_contents_item_instance_id ON container_contents(item_instance_id);
CREATE INDEX IF NOT EXISTS ix_container_contents_position ON container_contents(container_id, position);
-- Step 8: Create stored procedures for container operations
-- Function to add item to container
CREATE OR REPLACE FUNCTION add_item_to_container(
        p_container_id UUID,
        p_item_instance_id VARCHAR(64),
        p_position INTEGER DEFAULT NULL
    ) RETURNS VOID AS $$
DECLARE v_max_position INTEGER;
BEGIN -- Get max position if not provided
IF p_position IS NULL THEN
SELECT COALESCE(MAX(position), -1) + 1 INTO v_max_position
FROM container_contents
WHERE container_id = p_container_id;
ELSE v_max_position := p_position;
END IF;
-- Insert or update (upsert)
INSERT INTO container_contents (container_id, item_instance_id, position)
VALUES (
        p_container_id,
        p_item_instance_id,
        v_max_position
    ) ON CONFLICT (container_id, item_instance_id) DO
UPDATE
SET position = v_max_position,
    updated_at = NOW();
END;
$$ LANGUAGE plpgsql;
-- Function to remove item from container
CREATE OR REPLACE FUNCTION remove_item_from_container(
        p_container_id UUID,
        p_item_instance_id VARCHAR(64)
    ) RETURNS BOOLEAN AS $$
DECLARE v_deleted INTEGER;
BEGIN
DELETE FROM container_contents
WHERE container_id = p_container_id
    AND item_instance_id = p_item_instance_id;
GET DIAGNOSTICS v_deleted = ROW_COUNT;
RETURN v_deleted > 0;
END;
$$ LANGUAGE plpgsql;
-- Function to clear all items from container
CREATE OR REPLACE FUNCTION clear_container_contents(p_container_id UUID) RETURNS INTEGER AS $$
DECLARE v_deleted INTEGER;
BEGIN
DELETE FROM container_contents
WHERE container_id = p_container_id;
GET DIAGNOSTICS v_deleted = ROW_COUNT;
RETURN v_deleted;
END;
$$ LANGUAGE plpgsql;
-- Final verification: Ensure all required objects exist
DO $$ BEGIN -- Verify column exists
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name = 'containers'
        AND column_name = 'container_item_instance_id'
) THEN RAISE EXCEPTION 'Migration failed: container_item_instance_id column does not exist after migration';
END IF;
-- Verify table exists
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
        AND table_name = 'container_contents'
) THEN RAISE EXCEPTION 'Migration failed: container_contents table does not exist after migration';
END IF;
-- Verify functions exist
IF NOT EXISTS (
    SELECT 1
    FROM pg_proc p
        JOIN pg_namespace n ON p.pronamespace = n.oid
    WHERE n.nspname = 'public'
        AND p.proname = 'add_item_to_container'
) THEN RAISE EXCEPTION 'Migration failed: add_item_to_container function does not exist after migration';
END IF;
RAISE NOTICE 'Migration 011 completed successfully: All objects verified';
END $$;
