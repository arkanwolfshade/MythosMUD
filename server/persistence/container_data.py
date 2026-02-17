"""Container data class for persistence operations."""

from datetime import datetime
from typing import Any
from uuid import UUID


class ContainerData:  # pylint: disable=too-many-instance-attributes,too-few-public-methods  # Reason: Container data requires many fields to capture complete container state
    """Data class for container information."""

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container data initialization requires many parameters to capture complete container state
        self,
        container_instance_id: UUID,
        source_type: str,
        owner_id: UUID | None = None,
        room_id: str | None = None,
        entity_id: UUID | None = None,
        lock_state: str = "unlocked",
        capacity_slots: int = 20,
        weight_limit: int | None = None,
        decay_at: datetime | None = None,
        allowed_roles: list[str] | None = None,
        items_json: list[dict[str, Any]] | None = None,
        metadata_json: dict[str, Any] | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        self.container_instance_id = container_instance_id
        self.source_type = source_type
        self.owner_id = owner_id
        self.room_id = room_id
        self.entity_id = entity_id
        self.lock_state = lock_state
        self.capacity_slots = capacity_slots
        self.weight_limit = weight_limit
        self.decay_at = decay_at
        self.allowed_roles = allowed_roles or []
        self.items_json = items_json or []
        self.metadata_json = metadata_json or {}
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self) -> dict[str, Any]:
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
