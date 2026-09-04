"""Shared parameters for container creation (sync DB and async repository paths)."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class ContainerCreateParams:  # pylint: disable=too-many-instance-attributes  # Reason: mirrors full create_container procedure inputs
    """Optional fields for creating a container row (beyond source_type)."""

    owner_id: uuid.UUID | None = None
    room_id: str | None = None
    entity_id: uuid.UUID | None = None
    lock_state: str = "unlocked"
    capacity_slots: int = 20
    weight_limit: int | None = None
    decay_at: datetime | None = None
    allowed_roles: list[str] | None = None
    items_json: list[dict[str, Any]] | None = None
    metadata_json: dict[str, Any] | None = None
    container_item_instance_id: str | None = None
