"""Shared typing helpers for the async persistence facade."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Protocol, TypedDict

if TYPE_CHECKING:
    from .models.room import Room


class InstanceRoomLookup(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Minimal instance-manager surface used for instanced room lookup."""

    def get_room_by_id(self, room_id: str) -> Room | None: ...  # pylint: disable=missing-function-docstring  # Reason: Protocol stub


class ContainerCreateKwargs(TypedDict, total=False):
    """Backward-compatible kwargs for create_container when params is omitted."""

    owner_id: uuid.UUID | None
    room_id: str | None
    entity_id: uuid.UUID | None
    lock_state: str
    capacity_slots: int
    weight_limit: int | None
    decay_at: datetime | None
    allowed_roles: list[str] | None
    items_json: list[dict[str, object]] | None
    metadata_json: dict[str, object] | None


class PlayerEffectOptions(TypedDict, total=False):
    """Optional fields for add_player_effect beyond the required scalars."""

    intensity: int
    source: str | None
    visibility_level: str
