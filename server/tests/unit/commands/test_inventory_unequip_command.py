"""Unit tests for inventory_unequip_command module."""

from __future__ import annotations

import uuid
from contextlib import contextmanager
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.inventory_unequip_command import handle_unequip_command
from server.services.equipment_service import SlotValidationError


def _mutation_cm(should_apply: bool = True):
    @contextmanager
    def _cm():
        decision = MagicMock()
        decision.should_apply = should_apply
        yield decision

    return _cm()


def _player_with_equipped():
    player = MagicMock()
    player.name = "TestPlayer"
    player.player_id = uuid.uuid4()
    player.current_room_id = "room_001"
    player.get_inventory = MagicMock(return_value=[])
    player.get_equipped_items = MagicMock(return_value={"main_hand": {"item_name": "sword", "item_id": "sword_001"}})
    player.set_inventory = MagicMock()
    player.set_equipped_items = MagicMock()
    return player


def _request_wiring(persistence, connection_manager, player):
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.persistence = persistence
    mock_state.connection_manager = connection_manager
    mock_container = MagicMock()
    mock_container.async_persistence = persistence
    mock_state.container = mock_container
    mock_app.state = mock_state
    mock_request.app = mock_app
    return mock_request


@pytest.mark.asyncio
async def test_handle_unequip_command_success():
    persistence = AsyncMock()
    connection_manager = MagicMock()
    player = _player_with_equipped()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request = _request_wiring(persistence, connection_manager, player)

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(True))
    equipment_service = MagicMock()
    equipment_service.unequip_to_inventory = MagicMock(return_value=([{"item_id": "sword_001"}], {}))

    with (
        patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services,
        patch("server.commands.inventory_unequip_command.persist_player", new=AsyncMock(return_value=None)),
        patch(
            "server.commands.inventory_unequip_command.build_and_broadcast_inventory_event",
            new=AsyncMock(),
        ),
        patch(
            "server.commands.inventory_unequip_command.handle_wearable_container_on_unequip",
            new=AsyncMock(),
        ),
    ):
        mock_services.return_value = (inventory_service, MagicMock(), equipment_service)
        result = await handle_unequip_command(
            {"slot": "main_hand"}, {"name": "TestPlayer"}, request, None, "TestPlayer"
        )

    assert "remove" in result["result"].lower()
    assert result.get("room_message")


@pytest.mark.asyncio
async def test_handle_unequip_command_mutation_suppressed():
    persistence = AsyncMock()
    player = _player_with_equipped()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request = _request_wiring(persistence, MagicMock(), player)

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(False))
    equipment_service = MagicMock()

    with patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services:
        mock_services.return_value = (inventory_service, MagicMock(), equipment_service)
        result = await handle_unequip_command(
            {"slot": "main_hand"}, {"name": "TestPlayer"}, request, None, "TestPlayer"
        )

    assert "already being processed" in result["result"]


@pytest.mark.asyncio
async def test_handle_unequip_command_slot_validation_error():
    persistence = AsyncMock()
    player = _player_with_equipped()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request = _request_wiring(persistence, MagicMock(), player)

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(True))
    equipment_service = MagicMock()
    equipment_service.unequip_to_inventory = MagicMock(side_effect=SlotValidationError("That slot is empty."))

    with patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services:
        mock_services.return_value = (inventory_service, MagicMock(), equipment_service)
        result = await handle_unequip_command(
            {"slot": "main_hand"}, {"name": "TestPlayer"}, request, None, "TestPlayer"
        )

    assert "empty" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_unequip_command_persist_rollback():
    persistence = AsyncMock()
    player = _player_with_equipped()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request = _request_wiring(persistence, MagicMock(), player)

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(True))
    equipment_service = MagicMock()
    equipment_service.unequip_to_inventory = MagicMock(return_value=([{"item_id": "sword_001"}], {}))

    with (
        patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services,
        patch(
            "server.commands.inventory_unequip_command.persist_player",
            new=AsyncMock(return_value={"result": "Save failed."}),
        ),
    ):
        mock_services.return_value = (inventory_service, MagicMock(), equipment_service)
        result = await handle_unequip_command(
            {"slot": "main_hand"}, {"name": "TestPlayer"}, request, None, "TestPlayer"
        )

    assert result["result"] == "Save failed."
    player.set_inventory.assert_called()
    player.set_equipped_items.assert_called()
