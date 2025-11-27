"""Normalize container schema: add container_contents table and reference item_instance

Revision ID: normalize_container_schema
Revises: item_system_schema
Create Date: 2025-11-25

This migration normalizes the container schema by:
1. Adding container_item_instance_id to containers table (references item_instances)
2. Creating container_contents junction table for one-to-many relationship
3. Migrating data from items_json to container_contents
4. Creating stored procedures to abstract schema changes
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = "normalize_container_schema"
down_revision = "item_system_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Normalize container schema with proper relational structure."""

    # Step 1: Add container_item_instance_id column to containers table
    # This references the item_instance that IS the container (e.g., backpack instance)
    op.add_column(
        "containers",
        sa.Column(
            "container_item_instance_id",
            sa.String(length=64),
            nullable=True,  # Nullable initially for migration
            comment="References item_instances.item_instance_id - the item instance that is this container",
        ),
    )

    # Add foreign key constraint
    op.create_foreign_key(
        "fk_containers_container_item_instance",
        "containers",
        "item_instances",
        ["container_item_instance_id"],
        ["item_instance_id"],
        ondelete="SET NULL",  # If item instance is deleted, set to NULL
    )

    # Add index for performance
    op.create_index(
        "ix_containers_container_item_instance_id",
        "containers",
        ["container_item_instance_id"],
    )

    # Step 2: Create container_contents junction table
    op.create_table(
        "container_contents",
        sa.Column(
            "container_id",
            sa.dialects.postgresql.UUID(as_uuid=False),
            nullable=False,
            comment="References containers.container_instance_id",
        ),
        sa.Column(
            "item_instance_id",
            sa.String(length=64),
            nullable=False,
            comment="References item_instances.item_instance_id - item stored in container",
        ),
        sa.Column(
            "position",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
            comment="Position/order of item in container (for display ordering)",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        # Composite primary key
        sa.PrimaryKeyConstraint("container_id", "item_instance_id", name="pk_container_contents"),
        # Foreign keys
        sa.ForeignKeyConstraint(
            ["container_id"],
            ["containers.container_instance_id"],
            ondelete="CASCADE",  # If container is deleted, delete all contents
        ),
        sa.ForeignKeyConstraint(
            ["item_instance_id"],
            ["item_instances.item_instance_id"],
            ondelete="CASCADE",  # If item instance is deleted, remove from container
        ),
    )

    # Add indexes for performance
    op.create_index(
        "ix_container_contents_container_id",
        "container_contents",
        ["container_id"],
    )
    op.create_index(
        "ix_container_contents_item_instance_id",
        "container_contents",
        ["item_instance_id"],
    )
    op.create_index(
        "ix_container_contents_position",
        "container_contents",
        ["container_id", "position"],
    )

    # Step 3: Create stored procedures/functions to abstract schema changes

    # Function to get container contents as JSON array (for backward compatibility)
    op.execute(
        text("""
        CREATE OR REPLACE FUNCTION get_container_contents_json(p_container_id UUID)
        RETURNS JSONB AS $$
        DECLARE
            v_result JSONB;
        BEGIN
            SELECT COALESCE(
                jsonb_agg(
                    jsonb_build_object(
                        'item_instance_id', cc.item_instance_id,
                        'item_id', ii.prototype_id,
                        'item_name', COALESCE(ii.custom_name, ip.name),
                        'quantity', ii.quantity,
                        'condition', ii.condition,
                        'metadata', ii.metadata,
                        'position', cc.position
                    )
                    ORDER BY cc.position
                ),
                '[]'::jsonb
            )
            INTO v_result
            FROM container_contents cc
            JOIN item_instances ii ON cc.item_instance_id = ii.item_instance_id
            JOIN item_prototypes ip ON ii.prototype_id = ip.prototype_id
            WHERE cc.container_id = p_container_id;

            RETURN v_result;
        END;
        $$ LANGUAGE plpgsql;
    """)
    )

    # Function to add item to container
    op.execute(
        text("""
        CREATE OR REPLACE FUNCTION add_item_to_container(
            p_container_id UUID,
            p_item_instance_id VARCHAR(64),
            p_position INTEGER DEFAULT NULL
        )
        RETURNS VOID AS $$
        DECLARE
            v_max_position INTEGER;
        BEGIN
            -- Get max position if not provided
            IF p_position IS NULL THEN
                SELECT COALESCE(MAX(position), -1) + 1
                INTO v_max_position
                FROM container_contents
                WHERE container_id = p_container_id;
            ELSE
                v_max_position := p_position;
            END IF;

            -- Insert or update (upsert)
            INSERT INTO container_contents (container_id, item_instance_id, position)
            VALUES (p_container_id, p_item_instance_id, v_max_position)
            ON CONFLICT (container_id, item_instance_id)
            DO UPDATE SET position = v_max_position, updated_at = NOW();
        END;
        $$ LANGUAGE plpgsql;
    """)
    )

    # Function to remove item from container
    op.execute(
        text("""
        CREATE OR REPLACE FUNCTION remove_item_from_container(
            p_container_id UUID,
            p_item_instance_id VARCHAR(64)
        )
        RETURNS BOOLEAN AS $$
        DECLARE
            v_deleted INTEGER;
        BEGIN
            DELETE FROM container_contents
            WHERE container_id = p_container_id
              AND item_instance_id = p_item_instance_id;

            GET DIAGNOSTICS v_deleted = ROW_COUNT;
            RETURN v_deleted > 0;
        END;
        $$ LANGUAGE plpgsql;
    """)
    )

    # Function to clear all items from container
    op.execute(
        text("""
        CREATE OR REPLACE FUNCTION clear_container_contents(p_container_id UUID)
        RETURNS INTEGER AS $$
        DECLARE
            v_deleted INTEGER;
        BEGIN
            DELETE FROM container_contents
            WHERE container_id = p_container_id;

            GET DIAGNOSTICS v_deleted = ROW_COUNT;
            RETURN v_deleted;
        END;
        $$ LANGUAGE plpgsql;
    """)
    )

    # Step 4: Migrate existing data from items_json to container_contents
    # This is a complex migration that needs to:
    # 1. Parse items_json for each container
    # 2. Create item_instances for items that don't exist
    # 3. Insert into container_contents

    op.execute(
        text("""
        DO $$
        DECLARE
            v_container RECORD;
            v_item JSONB;
            v_item_instance_id VARCHAR(64);
            v_position INTEGER := 0;
            v_item_exists BOOLEAN;
        BEGIN
            -- Loop through all containers with items_json
            FOR v_container IN
                SELECT container_instance_id, items_json
                FROM containers
                WHERE items_json IS NOT NULL
                  AND jsonb_array_length(items_json) > 0
            LOOP
                v_position := 0;

                -- Loop through items in items_json
                FOR v_item IN SELECT * FROM jsonb_array_elements(v_container.items_json)
                LOOP
                    -- Get item_instance_id from JSON (may be item_instance_id or item_id)
                    v_item_instance_id := COALESCE(
                        v_item->>'item_instance_id',
                        v_item->>'item_id',
                        NULL
                    );

                    -- Skip if no item_instance_id
                    IF v_item_instance_id IS NULL THEN
                        CONTINUE;
                    END IF;

                    -- Check if item_instance exists
                    SELECT EXISTS(
                        SELECT 1 FROM item_instances
                        WHERE item_instance_id = v_item_instance_id
                    ) INTO v_item_exists;

                    -- If item_instance doesn't exist, we need to create it
                    -- This is a simplified migration - in production you'd want more robust handling
                    IF NOT v_item_exists THEN
                        -- Try to create a minimal item_instance
                        -- This assumes we have at least item_id (prototype_id) in the JSON
                        INSERT INTO item_instances (
                            item_instance_id,
                            prototype_id,
                            owner_type,
                            quantity,
                            metadata
                        )
                        VALUES (
                            v_item_instance_id,
                            COALESCE(v_item->>'item_id', v_item->>'prototype_id', 'unknown'),
                            'container',
                            COALESCE((v_item->>'quantity')::INTEGER, 1),
                            COALESCE(v_item->'metadata', '{}'::jsonb)
                        )
                        ON CONFLICT (item_instance_id) DO NOTHING;
                    END IF;

                    -- Insert into container_contents
                    INSERT INTO container_contents (container_id, item_instance_id, position)
                    VALUES (v_container.container_instance_id, v_item_instance_id, v_position)
                    ON CONFLICT (container_id, item_instance_id) DO NOTHING;

                    v_position := v_position + 1;
                END LOOP;
            END LOOP;
        END;
        $$;
    """)
    )

    # Step 5: Make container_item_instance_id NOT NULL after migration
    # (We'll keep it nullable for now to allow containers without item instances)
    # This can be made NOT NULL in a future migration once all containers have item instances


def downgrade() -> None:
    """Revert to denormalized schema with items_json."""

    # Drop stored procedures
    op.execute(text("DROP FUNCTION IF EXISTS clear_container_contents(UUID)"))
    op.execute(text("DROP FUNCTION IF EXISTS remove_item_from_container(UUID, VARCHAR)"))
    op.execute(text("DROP FUNCTION IF EXISTS add_item_to_container(UUID, VARCHAR, INTEGER)"))
    op.execute(text("DROP FUNCTION IF EXISTS get_container_contents_json(UUID)"))

    # Drop container_contents table
    op.drop_index("ix_container_contents_position", table_name="container_contents")
    op.drop_index("ix_container_contents_item_instance_id", table_name="container_contents")
    op.drop_index("ix_container_contents_container_id", table_name="container_contents")
    op.drop_table("container_contents")

    # Drop container_item_instance_id column
    op.drop_index("ix_containers_container_item_instance_id", table_name="containers")
    op.drop_constraint("fk_containers_container_item_instance", table_name="containers", type_="foreignkey")
    op.drop_column("containers", "container_item_instance_id")

    # Note: We don't restore items_json data from container_contents
    # as that would require complex reverse migration logic
