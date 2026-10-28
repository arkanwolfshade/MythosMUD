"""Unit tests for inventory_websocket_events.emit_inventory_updated."""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.inventory_websocket_events import emit_inventory_updated


def _async_attr(obj: MagicMock, name: str) -> AsyncMock:
    """Typed access to a MagicMock's async-mocked attribute (avoids reportAny at call sites)."""
    return cast(AsyncMock, getattr(obj, name))


class _Owner:
    """Minimal _InventoryOwner stand-in."""

    def __init__(self, inventory: list[dict[str, object]], equipped: dict[str, object]) -> None:
        self._inventory: list[dict[str, object]] = inventory
        self._equipped: dict[str, object] = equipped

    def get_inventory(self) -> list[dict[str, object]]:
        return self._inventory

    def get_equipped_items(self) -> dict[str, object]:
        return self._equipped


@pytest.fixture
def mock_connection_manager() -> MagicMock:
    manager = MagicMock()
    manager.sequence_counter = 0
    manager.send_personal_message = AsyncMock(return_value={"sent": True})
    return manager


@pytest.mark.asyncio
async def test_emit_inventory_updated_sends_personal_message(mock_connection_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    inventory: list[dict[str, object]] = [{"item_id": "torch", "quantity": 1}]
    equipped: dict[str, object] = {"main_hand": {"item_id": "sword"}}
    player = _Owner(inventory, equipped)

    await emit_inventory_updated(mock_connection_manager, player_id, player)

    send = _async_attr(mock_connection_manager, "send_personal_message")
    send.assert_awaited_once()
    call_args = send.call_args
    assert call_args is not None
    sent_player_id, event = cast("tuple[uuid.UUID, dict[str, object]]", call_args.args)
    assert sent_player_id == player_id
    assert event["event_type"] == "inventory_updated"
    data = cast(dict[str, object], event["data"])
    assert data["inventory"] == inventory
    assert data["equipped"] == equipped


@pytest.mark.asyncio
async def test_emit_inventory_updated_no_connection_manager_is_noop() -> None:
    """None connection_manager must not raise."""
    await emit_inventory_updated(None, uuid.uuid4(), _Owner([], {}))


@pytest.mark.asyncio
async def test_emit_inventory_updated_emission_error_is_swallowed(mock_connection_manager: MagicMock) -> None:
    """A broken connection_manager must not fail the caller's mutation."""
    mock_connection_manager.send_personal_message = AsyncMock(side_effect=RuntimeError("boom"))

    await emit_inventory_updated(mock_connection_manager, uuid.uuid4(), _Owner([], {}))
