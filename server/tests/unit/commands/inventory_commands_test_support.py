"""Shared helpers for inventory command unit tests."""

from __future__ import annotations

import typing
import uuid
from collections.abc import Mapping
from typing import cast
from unittest.mock import AsyncMock, MagicMock


def command_result_text(payload: Mapping[str, object]) -> str:
    """Normalize handler result message for assertions."""
    raw = payload.get("result")
    return str(raw) if raw is not None else ""


def inventory_has_named_item(inv: object, name: str) -> bool:
    """True if inv is a sequence of dict rows containing item_name == name."""
    rows = cast(list[object], inv)
    return any(isinstance(r, dict) and cast(dict[str, object], r).get("item_name") == name for r in rows)


def sample_floor_item_stack() -> dict[str, object]:
    """Single sword stack as returned by list_room_drops / take_room_drop."""
    return {
        "item_name": "sword",
        "item_id": "sword_001",
        "item_instance_id": str(uuid.uuid4()),
        "prototype_id": "sword_proto",
        "slot_type": "inventory",
        "quantity": 1,
    }


@typing.final
class PickupTestWiring:
    """Standard app.state wiring for handle_pickup_command tests (typed mock surface for pyright)."""

    def __init__(self) -> None:
        self.request = MagicMock()
        app: MagicMock = MagicMock()
        state: MagicMock = MagicMock()
        self.persistence = MagicMock()
        self.connection_manager = MagicMock()
        self.room_manager = MagicMock()
        self.player = MagicMock()
        container: MagicMock = MagicMock()

        self.list_room_drops: MagicMock = MagicMock(return_value=[])
        self.take_room_drop: MagicMock = MagicMock(return_value=None)
        self.add_room_drop: MagicMock = MagicMock()
        self.room_manager.list_room_drops = self.list_room_drops
        self.room_manager.take_room_drop = self.take_room_drop
        self.room_manager.add_room_drop = self.add_room_drop

        self.set_inventory: MagicMock = MagicMock()
        self.player.name = "TestPlayer"
        self.player.player_id = uuid.uuid4()
        self.player.current_room_id = "room_001"
        self.player.get_inventory = MagicMock(return_value=[])
        self.player.set_inventory = self.set_inventory

        self.persistence.get_player_by_name = AsyncMock(return_value=self.player)
        self.persistence.ensure_item_instance = MagicMock()
        self.connection_manager.room_manager = self.room_manager
        state.persistence = self.persistence
        state.connection_manager = self.connection_manager
        container.async_persistence = self.persistence
        state.container = container
        app.state = state
        self.request.app = app

    def set_floor_stack(self, stack: dict[str, object]) -> None:
        self.list_room_drops.return_value = [stack]
        self.take_room_drop.return_value = stack

    def set_listed_drops(self, drops: list[dict[str, object]]) -> None:
        self.list_room_drops.return_value = drops

    def set_player_inventory(self, rows: list[dict[str, object]]) -> None:
        self.player.get_inventory = MagicMock(return_value=rows)
