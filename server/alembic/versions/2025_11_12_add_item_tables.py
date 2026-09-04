"""Create item prototype and instance tables

Revision ID: item_system_schema
Revises: rename_players_to_population
Create Date: 2025-11-12
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "item_system_schema"
down_revision = "rename_players_to_population"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "item_prototypes",
        sa.Column("prototype_id", sa.String(length=120), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("short_description", sa.String(length=255), nullable=False),
        sa.Column("long_description", sa.Text(), nullable=False),
        sa.Column("item_type", sa.String(length=32), nullable=False),
        sa.Column("weight", sa.Float(), nullable=False, server_default=sa.text("0")),
        sa.Column("base_value", sa.Integer(), nullable=False, server_default=sa.text("0")),
        sa.Column("durability", sa.Integer(), nullable=True),
        sa.Column("flags", sa.JSON(), nullable=False, server_default=sa.text("'[]'")),
        sa.Column("wear_slots", sa.JSON(), nullable=False, server_default=sa.text("'[]'")),
        sa.Column("stacking_rules", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
        sa.Column("usage_restrictions", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
        sa.Column("effect_components", sa.JSON(), nullable=False, server_default=sa.text("'[]'")),
        sa.Column("metadata", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
        sa.Column("tags", sa.JSON(), nullable=False, server_default=sa.text("'[]'")),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    op.create_table(
        "item_instances",
        sa.Column("item_instance_id", sa.String(length=64), primary_key=True),
        sa.Column("prototype_id", sa.String(length=120), nullable=False),
        sa.Column("owner_type", sa.String(length=32), nullable=False, server_default="room"),
        sa.Column("owner_id", sa.String(length=255), nullable=True),
        sa.Column("location_context", sa.String(length=255), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=False, server_default=sa.text("1")),
        sa.Column("condition", sa.Integer(), nullable=True),
        sa.Column("flags_override", sa.JSON(), nullable=False, server_default=sa.text("'[]'")),
        sa.Column("binding_state", sa.String(length=32), nullable=True),
        sa.Column("attunement_state", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
        sa.Column("custom_name", sa.String(length=255), nullable=True),
        sa.Column("metadata", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
        sa.Column("origin_source", sa.String(length=64), nullable=True),
        sa.Column("origin_metadata", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
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
        sa.ForeignKeyConstraint(
            ("prototype_id",),
            ("item_prototypes.prototype_id",),
            ondelete="CASCADE",
        ),
    )
    op.create_index(
        "ix_item_instances_owner",
        "item_instances",
        ["owner_type", "owner_id"],
    )
    op.create_index(
        "ix_item_instances_prototype_id",
        "item_instances",
        ["prototype_id"],
    )

    op.create_table(
        "item_component_states",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("item_instance_id", sa.String(length=64), nullable=False),
        sa.Column("component_id", sa.String(length=120), nullable=False),
        sa.Column("state_payload", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.ForeignKeyConstraint(
            ("item_instance_id",),
            ("item_instances.item_instance_id",),
            ondelete="CASCADE",
        ),
    )
    op.create_index(
        "ix_component_states_instance_component",
        "item_component_states",
        ["item_instance_id", "component_id"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_component_states_instance_component", table_name="item_component_states")
    op.drop_table("item_component_states")
    op.drop_index("ix_item_instances_prototype_id", table_name="item_instances")
    op.drop_index("ix_item_instances_owner", table_name="item_instances")
    op.drop_table("item_instances")
    op.drop_table("item_prototypes")
