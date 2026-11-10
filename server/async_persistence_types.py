"""Shared typing helpers for the async persistence facade."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
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


class CorruptionAdjustOptions(TypedDict, total=False):
    """Optional keywords of a corruption adjustment (CorruptionService.apply_corruption_adjustment)."""

    metadata: Mapping[str, object] | str | None
    location_id: str | None
    bypass_permanence_floor: bool


class PlayerEffectOptions(TypedDict, total=False):
    """Optional fields for add_player_effect beyond the required scalars."""

    payload: Mapping[str, object]
    instance_scoped: bool
    intensity: int
    source: str | None
    visibility_level: str


class PlayerEffectsWriting(Protocol):
    """Starting and ending a player's status effects, as the persistence layer delegates them (PlayerEffects).

    Injected at startup like the health service: the implementation sits on the player registry, which this module
    cannot import without a cycle.
    """

    async def add(
        self,
        player_id: uuid.UUID | str,
        effect_type: str,
        category: str,
        remaining_seconds: int | None,
        options: PlayerEffectOptions | None = None,
    ) -> str:
        """Start an effect lasting ``remaining_seconds`` online game seconds (None = until removed); returns its id."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    async def remove_by_type(self, player_id: uuid.UUID | str, effect_type: str) -> int:
        """End every effect of one type on the player; returns how many."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type
