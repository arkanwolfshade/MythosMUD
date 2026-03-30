"""Shared types for inventory command handlers (Lizard: keep main module small)."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol

# Handler responses are JSON-shaped; Mapping covariant values avoid dict[str, str] return errors.
CommandResponse = Mapping[str, object]


class RoomDropManager(Protocol):
    """Narrows room managers for floor drop operations (pickup / get room)."""

    def list_room_drops(self, room_id: str) -> list[dict[str, object]]: ...

    def take_room_drop(self, room_id: str, index: int, quantity: int) -> dict[str, object] | None: ...

    def add_room_drop(self, room_id: str, stack: dict[str, object]) -> None: ...
