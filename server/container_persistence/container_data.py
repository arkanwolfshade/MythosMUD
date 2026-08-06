"""Container data class for the unified container system."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass
class ContainerData:  # pylint: disable=too-many-instance-attributes,too-few-public-methods  # Reason: Data class requires many fields to capture complete container state
    """Data class for container information."""

    container_instance_id: UUID
    source_type: str
    owner_id: UUID | None = None
    room_id: str | None = None
    entity_id: UUID | None = None
    lock_state: str = "unlocked"
    capacity_slots: int = 20
    weight_limit: int | None = None
    decay_at: datetime | None = None
    allowed_roles: list[str] = field(default_factory=list)
    items_json: list[dict[str, object]] = field(default_factory=list)
    metadata_json: dict[str, object] = field(default_factory=dict)
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __post_init__(self) -> None:
        # Coerce None from callers that still pass optional collections as null
        self.allowed_roles = self.allowed_roles or []
        self.items_json = self.items_json or []
        self.metadata_json = self.metadata_json or {}

    def to_dict(self) -> dict[str, object]:
        """Convert container data to dictionary for ContainerComponent."""

        # Map database field names to ContainerComponent field names
        result: dict[str, object] = {
            "container_id": UUID(str(self.container_instance_id)),
            "source_type": self.source_type,
            "owner_id": UUID(str(self.owner_id)) if self.owner_id else None,
            "room_id": self.room_id,
            "entity_id": UUID(str(self.entity_id)) if self.entity_id else None,
            "lock_state": self.lock_state,
            "capacity_slots": self.capacity_slots,
            "weight_limit": self.weight_limit,
            "decay_at": self.decay_at,
            "allowed_roles": self.allowed_roles,
            "items": self.items_json,
            "metadata": self.metadata_json,
        }
        return result
