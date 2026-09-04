"""Remove items_json column from containers table

Revision ID: remove_items_json_column
Revises: normalize_container_schema
Create Date: 2025-11-25

This migration removes the items_json column from the containers table
since all items are now stored in the container_contents junction table.
"""

from __future__ import annotations

from alembic import op

# revision identifiers, used by Alembic.
revision = "remove_items_json_column"
down_revision = "normalize_container_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Remove items_json column from containers table."""
    # Drop the items_json column - all data has been migrated to container_contents
    op.drop_column("containers", "items_json")


def downgrade() -> None:
    """Restore items_json column (data will be empty)."""
    from sqlalchemy import Column
    from sqlalchemy.dialects.postgresql import JSONB

    # Re-add items_json column with default empty array
    op.add_column(
        "containers",
        Column(
            "items_json",
            JSONB(),
            nullable=False,
            server_default="'[]'::jsonb",
        ),
    )
