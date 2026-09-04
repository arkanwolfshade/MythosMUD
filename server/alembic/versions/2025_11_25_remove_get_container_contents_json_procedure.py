"""Remove deprecated get_container_contents_json stored procedure

Revision ID: remove_get_container_contents_json
Revises: remove_items_json_column
Create Date: 2025-11-25

This migration removes the deprecated get_container_contents_json stored procedure
since the persistence layer now queries the normalized tables directly.
"""

from __future__ import annotations

from alembic import op
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = "remove_get_container_contents_json"
down_revision = "remove_items_json_column"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Remove deprecated stored procedure."""
    op.execute(text("DROP FUNCTION IF EXISTS get_container_contents_json(UUID)"))


def downgrade() -> None:
    """Restore deprecated stored procedure."""
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
