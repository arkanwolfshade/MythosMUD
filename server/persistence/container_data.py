"""Container data class for persistence operations."""

from dataclasses import dataclass
from datetime import datetime
from typing import final
from uuid import UUID


@dataclass(frozen=True)
class ContainerDataCore:
    """Identity and placement fields for a container row."""

    container_instance_id: UUID
    source_type: str
    owner_id: UUID | None = None
    room_id: str | None = None
    entity_id: UUID | None = None
    lock_state: str = "unlocked"
    capacity_slots: int = 20


@dataclass(frozen=True)
class ContainerDataExtras:
    """Optional payload and timestamps for a container row."""

    weight_limit: int | None = None
    decay_at: datetime | None = None
    allowed_roles: list[str] | None = None
    items_json: list[dict[str, object]] | None = None
    metadata_json: dict[str, object] | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


@final
class ContainerData:  # pylint: disable=too-many-instance-attributes,too-few-public-methods  # Reason: Container data requires many fields to capture complete container state
    """Data class for container information."""

    def __init__(self, core: ContainerDataCore, extras: ContainerDataExtras | None = None) -> None:
        e = extras or ContainerDataExtras()
        self.container_instance_id = core.container_instance_id
        self.source_type = core.source_type
        self.owner_id = core.owner_id
        self.room_id = core.room_id
        self.entity_id = core.entity_id
        self.lock_state = core.lock_state
        self.capacity_slots = core.capacity_slots
        self.weight_limit = e.weight_limit
        self.decay_at = e.decay_at
        self.allowed_roles = e.allowed_roles or []
        self.items_json = e.items_json or []
        self.metadata_json = e.metadata_json or {}
        self.created_at = e.created_at
        self.updated_at = e.updated_at

    def to_dict(self) -> dict[str, object]:
        """
        Convert container data to dictionary.

        Returns dictionary with model field names (container_id, items, metadata)
        to match ContainerComponent model expectations.
        """
        return {
            "container_id": str(self.container_instance_id),
            "source_type": self.source_type,
            "owner_id": str(self.owner_id) if self.owner_id else None,
            "room_id": self.room_id,
            "entity_id": str(self.entity_id) if self.entity_id else None,
            "lock_state": self.lock_state,
            "capacity_slots": self.capacity_slots,
            "weight_limit": self.weight_limit,
            "decay_at": self.decay_at.isoformat() if self.decay_at else None,
            "allowed_roles": self.allowed_roles,
            "items": self.items_json,
            "metadata": self.metadata_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
