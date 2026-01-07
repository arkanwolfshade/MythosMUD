"""
SQLAlchemy models for MythosMUD item prototypes, instances, and component state.

These models back the new item system, mirroring the JSON prototype schema defined
for authoring tools while providing runtime storage for instantiated items and
component-specific metadata.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict, MutableList
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    pass


JSON = JSONB  # PostgreSQL JSONB type for JSON data


class ItemPrototype(Base):
    """Immutable catalog entry describing a canonical item."""

    __tablename__ = "item_prototypes"

    prototype_id: Mapped[str] = mapped_column(String(120), primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    short_description: Mapped[str] = mapped_column(String(255), nullable=False)
    long_description: Mapped[str] = mapped_column(Text, nullable=False)
    item_type: Mapped[str] = mapped_column(String(32), nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    base_value: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    durability: Mapped[int | None] = mapped_column(Integer, nullable=True)
    flags: Mapped[list[str]] = mapped_column(MutableList.as_mutable(JSON), nullable=False, default=list)
    wear_slots: Mapped[list[str]] = mapped_column(MutableList.as_mutable(JSON), nullable=False, default=list)
    stacking_rules: Mapped[dict[str, int | str | float]] = mapped_column(
        MutableDict.as_mutable(JSON), nullable=False, default=dict
    )
    usage_restrictions: Mapped[dict[str, object]] = mapped_column(
        MutableDict.as_mutable(JSON), nullable=False, default=dict
    )
    effect_components: Mapped[list[str]] = mapped_column(MutableList.as_mutable(JSON), nullable=False, default=list)
    metadata_payload: Mapped[dict[str, object]] = mapped_column(
        "metadata",
        MutableDict.as_mutable(JSON),
        nullable=False,
        default=dict,
    )
    tags: Mapped[list[str]] = mapped_column(MutableList.as_mutable(JSON), nullable=False, default=list)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        server_default=func.now(),  # pylint: disable=not-callable  # SQLAlchemy func is callable at runtime  # pylint: disable=not-callable  # SQLAlchemy func is callable at runtime
    )

    item_instances: Mapped[list[ItemInstance]] = relationship(
        back_populates="prototype",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def primary_slot(self) -> str | None:
        """Return the first configured wear slot, if any."""
        return self.wear_slots[0] if self.wear_slots else None


class ItemInstance(Base):
    """Runtime representation of an item spawned from a prototype."""

    __tablename__ = "item_instances"

    item_instance_id: Mapped[str] = mapped_column(String(64), primary_key=True)
    prototype_id: Mapped[str] = mapped_column(
        String(120),
        ForeignKey("item_prototypes.prototype_id", ondelete="CASCADE"),
        nullable=False,
    )
    owner_type: Mapped[str] = mapped_column(String(32), nullable=False, default="room")
    owner_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    location_context: Mapped[str | None] = mapped_column(String(255), nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    condition: Mapped[int | None] = mapped_column(Integer, nullable=True)
    flags_override: Mapped[list[str]] = mapped_column(MutableList.as_mutable(JSON), nullable=False, default=list)
    binding_state: Mapped[str | None] = mapped_column(String(32), nullable=True)
    attunement_state: Mapped[dict[str, object]] = mapped_column(
        MutableDict.as_mutable(JSON), nullable=False, default=dict
    )
    custom_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    metadata_payload: Mapped[dict[str, object]] = mapped_column(
        "metadata",
        MutableDict.as_mutable(JSON),
        nullable=False,
        default=dict,
    )
    origin_source: Mapped[str | None] = mapped_column(String(64), nullable=True)
    origin_metadata: Mapped[dict[str, object]] = mapped_column(
        MutableDict.as_mutable(JSON), nullable=False, default=dict
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        server_default=func.now(),  # pylint: disable=not-callable  # SQLAlchemy func is callable at runtime  # pylint: disable=not-callable  # SQLAlchemy func is callable at runtime
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        server_default=func.now(),  # pylint: disable=not-callable  # SQLAlchemy func is callable at runtime
    )

    prototype: Mapped[ItemPrototype] = relationship(back_populates="item_instances")
    component_states: Mapped[list[ItemComponentState]] = relationship(
        back_populates="item_instance",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def apply_flag(self, flag: str) -> None:
        """Idempotently apply a runtime-only flag override."""
        if flag not in self.flags_override:
            self.flags_override.append(flag)


class ItemComponentState(Base):
    """Per-instance persisted state for modular item components."""

    __tablename__ = "item_component_states"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    item_instance_id: Mapped[str] = mapped_column(
        String(64),
        ForeignKey("item_instances.item_instance_id", ondelete="CASCADE"),
        nullable=False,
    )
    component_id: Mapped[str] = mapped_column(String(120), nullable=False)
    state_payload: Mapped[dict[str, object]] = mapped_column(
        MutableDict.as_mutable(JSON),
        nullable=False,
        default=dict,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        server_default=func.now(),  # pylint: disable=not-callable  # SQLAlchemy func is callable at runtime
    )

    item_instance: Mapped[ItemInstance] = relationship(back_populates="component_states")

    __table_args__ = (
        Index(
            "ix_component_states_instance_component",
            "item_instance_id",
            "component_id",
            unique=True,
        ),
    )

    @staticmethod
    def unique_key(instance_id: str, component_id: str) -> tuple[str, str]:
        """Convenience helper for composing uniqueness checks in higher layers."""
        return instance_id, component_id
