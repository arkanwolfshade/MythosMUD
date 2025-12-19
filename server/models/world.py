"""
SQLAlchemy models for world data (zones, subzones, rooms, and links).
"""

from sqlalchemy import CheckConstraint, ForeignKey, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Zone(Base):
    """Represent a major area or plane of existence."""

    __tablename__ = "zones"
    __table_args__ = (
        CheckConstraint(
            "(environment IS NULL) OR (environment IN ('indoors', 'outdoors', 'underwater', 'void'))",
            name="chk_zones_environment",
        ),
        CheckConstraint(
            "(zone_type IS NULL) OR (zone_type IN ('city', 'countryside', 'mountains', 'swamp', 'tundra', 'desert', 'death'))",
            name="chk_zones_zone_type",
        ),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    stable_id: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    zone_type: Mapped[str | None] = mapped_column(Text, nullable=True)
    environment: Mapped[str | None] = mapped_column(Text, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    weather_patterns: Mapped[list | None] = mapped_column(JSONB, nullable=True, default=list)
    special_rules: Mapped[dict | None] = mapped_column(JSONB, nullable=True, default=dict)

    subzones: Mapped[list["Subzone"]] = relationship("Subzone", back_populates="zone", cascade="all, delete-orphan")


class Subzone(Base):
    """Represent a specific region within a zone."""

    __tablename__ = "subzones"
    __table_args__ = (
        CheckConstraint(
            "(environment IS NULL) OR (environment IN ('indoors', 'outdoors', 'underwater', 'void'))",
            name="chk_subzones_environment",
        ),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    zone_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("zones.id", ondelete="CASCADE"), nullable=False
    )
    stable_id: Mapped[str] = mapped_column(Text, nullable=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    environment: Mapped[str | None] = mapped_column(Text, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    special_rules: Mapped[dict | None] = mapped_column(JSONB, nullable=True, default=dict)

    zone: Mapped["Zone"] = relationship("Zone", back_populates="subzones")
    rooms: Mapped[list["RoomModel"]] = relationship("RoomModel", back_populates="subzone", cascade="all, delete-orphan")


class ZoneConfigurationMapping(Base):
    """Represent a mapping between zones and subzones for configuration."""

    __tablename__ = "zone_configurations"
    __table_args__ = (UniqueConstraint("zone_id", "subzone_id", name="idx_zone_configurations_zone_id_subzone_id"),)

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    zone_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("zones.id", ondelete="CASCADE"), nullable=False
    )
    subzone_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("subzones.id", ondelete="CASCADE"), nullable=False
    )


class RoomModel(Base):
    """
    SQLAlchemy model for room data.

    Named RoomModel to avoid conflict with the plain Room class in server.models.room.
    """

    __tablename__ = "rooms"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    subzone_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("subzones.id", ondelete="CASCADE"), nullable=False
    )
    stable_id: Mapped[str] = mapped_column(Text, nullable=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    attributes: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)

    subzone: Mapped["Subzone"] = relationship("Subzone", back_populates="rooms")
    exits: Mapped[list["RoomLink"]] = relationship(
        "RoomLink", primaryjoin="RoomModel.id == RoomLink.from_room_id", cascade="all, delete-orphan"
    )


class RoomLink(Base):
    """Represent a directional link between two rooms."""

    __tablename__ = "room_links"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    from_room_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False
    )
    to_room_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("rooms.id", ondelete="RESTRICT"), nullable=False
    )
    direction: Mapped[str] = mapped_column(Text, nullable=False)
    attributes: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)
