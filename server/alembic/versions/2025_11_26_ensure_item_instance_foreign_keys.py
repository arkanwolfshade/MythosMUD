"""Ensure foreign key constraints exist for item_instances

Revision ID: ensure_item_instance_fks
Revises: remove_get_container_contents_json_procedure
Create Date: 2025-11-26

This migration ensures that all foreign key constraints referencing item_instances
are properly set up. This is a safety check to ensure referential integrity.
"""

from __future__ import annotations

from alembic import op
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = "ensure_item_instance_fks"
down_revision = "remove_get_container_contents_json_procedure"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Ensure foreign key constraints exist for item_instances."""

    # Verify and create foreign key constraint for container_contents.item_instance_id
    # This should already exist from normalize_container_schema, but we ensure it's there
    op.execute(
        text("""
        DO $$
        BEGIN
            -- Check if the foreign key constraint exists
            IF NOT EXISTS (
                SELECT 1
                FROM information_schema.table_constraints
                WHERE constraint_name = 'container_contents_item_instance_id_fkey'
                AND table_name = 'container_contents'
            ) THEN
                -- Create the foreign key constraint if it doesn't exist
                ALTER TABLE container_contents
                ADD CONSTRAINT container_contents_item_instance_id_fkey
                FOREIGN KEY (item_instance_id)
                REFERENCES item_instances(item_instance_id)
                ON DELETE CASCADE;

                RAISE NOTICE 'Created foreign key constraint: container_contents_item_instance_id_fkey';
            ELSE
                RAISE NOTICE 'Foreign key constraint already exists: container_contents_item_instance_id_fkey';
            END IF;
        END $$;
    """)
    )

    # Verify and create foreign key constraint for containers.container_item_instance_id
    op.execute(
        text("""
        DO $$
        BEGIN
            -- Check if the foreign key constraint exists
            IF NOT EXISTS (
                SELECT 1
                FROM information_schema.table_constraints
                WHERE constraint_name = 'fk_containers_container_item_instance'
                AND table_name = 'containers'
            ) THEN
                -- Create the foreign key constraint if it doesn't exist
                ALTER TABLE containers
                ADD CONSTRAINT fk_containers_container_item_instance
                FOREIGN KEY (container_item_instance_id)
                REFERENCES item_instances(item_instance_id)
                ON DELETE SET NULL;

                RAISE NOTICE 'Created foreign key constraint: fk_containers_container_item_instance';
            ELSE
                RAISE NOTICE 'Foreign key constraint already exists: fk_containers_container_item_instance';
            END IF;
        END $$;
    """)
    )


def downgrade() -> None:
    """This migration only ensures constraints exist - no downgrade needed."""
    # Constraints should remain - this is a safety check migration
    pass
