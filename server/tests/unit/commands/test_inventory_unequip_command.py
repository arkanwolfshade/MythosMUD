"""Unit tests for inventory_unequip_command module (the change commits through the player registry, ADR-029 4a)."""

from __future__ import annotations

import uuid
from collections.abc import AsyncGenerator, Mapping
from contextlib import asynccontextmanager
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.commands.inventory_unequip_command import handle_unequip_command
from server.services.equipment_service import SlotValidationError
from server.tests.fixtures.shared.player_registry import RegistryHarness, install_player_registry

SWORD_INSTANCE = str(uuid.uuid4())


def _sword(slot_type: str) -> dict[str, object]:
    return {
        "item_instance_id": SWORD_INSTANCE,
        "prototype_id": "sword_proto",
        "item_id": "sword_001",
        "item_name": "sword",
        "slot_type": slot_type,
        "quantity": 1,
    }


def _mutation_cm(should_apply: bool = True):
    @asynccontextmanager
    async def _cm() -> AsyncGenerator[MagicMock]:
        decision = MagicMock()
        decision.should_apply = should_apply
        yield decision

    return _cm()


def _player_with_equipped() -> MagicMock:
    """A MagicMock player whose setters change what its getters return, like the real Player."""
    player = MagicMock()
    player.name = "TestPlayer"
    player.player_id = uuid.uuid4()
    player.current_room_id = "room_001"
    get_inventory = MagicMock(return_value=[])
    get_equipped = MagicMock(return_value={"main_hand": _sword("main_hand")})
    player.get_inventory = get_inventory
    player.get_equipped_items = get_equipped

    def store_inventory(inventory: object) -> None:
        get_inventory.return_value = [dict(stack) for stack in cast(list[Mapping[str, object]], inventory)]

    def store_equipped(equipped: object) -> None:
        get_equipped.return_value = dict(cast(Mapping[str, object], equipped))

    player.set_inventory = MagicMock(side_effect=store_inventory)
    player.set_equipped_items = MagicMock(side_effect=store_equipped)
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


def _setup(monkeypatch: pytest.MonkeyPatch) -> tuple[MagicMock, MagicMock, MagicMock, RegistryHarness]:
    persistence = AsyncMock()
    connection_manager = MagicMock()
    player = _player_with_equipped()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request = _request_wiring(persistence, connection_manager, player)
    return player, connection_manager, request, install_player_registry(monkeypatch, player)


@pytest.mark.asyncio
async def test_handle_unequip_command_success(monkeypatch: pytest.MonkeyPatch) -> None:
    _player, _cm, request, harness = _setup(monkeypatch)

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(True))
    equipment_service = MagicMock()
    equipment_service.unequip_to_inventory = MagicMock(return_value=([_sword("inventory")], {}))

    with (
        patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services,
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

    assert "remove" in str(result["result"]).lower()
    assert result.get("room_message")
    assert harness.saved_equipped() == {}  # the sword left its slot in the committed write
    assert [stack["item_id"] for stack in harness.saved_carried() or []] == ["sword_001"]


@pytest.mark.asyncio
async def test_handle_unequip_command_emits_inventory_updated(monkeypatch: pytest.MonkeyPatch) -> None:
    """A successful unequip pushes inventory_updated so a GUI inventory panel stays in sync."""
    player, connection_manager, request, _harness = _setup(monkeypatch)

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(True))
    equipment_service = MagicMock()
    equipment_service.unequip_to_inventory = MagicMock(return_value=([_sword("inventory")], {}))

    with (
        patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services,
        patch(
            "server.commands.inventory_unequip_command.build_and_broadcast_inventory_event",
            new=AsyncMock(),
        ),
        patch(
            "server.commands.inventory_unequip_command.handle_wearable_container_on_unequip",
            new=AsyncMock(),
        ),
        patch("server.commands.inventory_unequip_command.emit_inventory_updated", new_callable=AsyncMock) as mock_emit,
    ):
        mock_services.return_value = (inventory_service, MagicMock(), equipment_service)
        result = await handle_unequip_command(
            {"slot": "main_hand"}, {"name": "TestPlayer"}, request, None, "TestPlayer"
        )

    assert "remove" in str(result["result"]).lower()
    player_id = cast(uuid.UUID, player.player_id)
    mock_emit.assert_awaited_once_with(connection_manager, player_id, player)


@pytest.mark.asyncio
async def test_handle_unequip_command_mutation_suppressed(monkeypatch: pytest.MonkeyPatch) -> None:
    _player, _cm, request, harness = _setup(monkeypatch)

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(False))
    equipment_service = MagicMock()

    with patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services:
        mock_services.return_value = (inventory_service, MagicMock(), equipment_service)
        result = await handle_unequip_command(
            {"slot": "main_hand"}, {"name": "TestPlayer"}, request, None, "TestPlayer"
        )

    assert "already being processed" in str(result["result"])
    assert harness.saved_carried() is None


@pytest.mark.asyncio
async def test_handle_unequip_command_slot_validation_error(monkeypatch: pytest.MonkeyPatch) -> None:
    _player, _cm, request, harness = _setup(monkeypatch)

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(True))
    equipment_service = MagicMock()
    equipment_service.unequip_to_inventory = MagicMock(side_effect=SlotValidationError("That slot is empty."))

    with patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services:
        mock_services.return_value = (inventory_service, MagicMock(), equipment_service)
        result = await handle_unequip_command(
            {"slot": "main_hand"}, {"name": "TestPlayer"}, request, None, "TestPlayer"
        )

    assert "empty" in str(result["result"]).lower()
    assert harness.saved_carried() is None


@pytest.mark.asyncio
async def test_handle_unequip_command_failed_save_rolls_back(monkeypatch: pytest.MonkeyPatch) -> None:
    player, _cm, request, harness = _setup(monkeypatch)
    harness.db.fail_commits = 1
    harness.db.commit_error = SQLAlchemyError("database unavailable")

    inventory_service = MagicMock()
    inventory_service.begin_mutation = MagicMock(return_value=_mutation_cm(True))
    equipment_service = MagicMock()
    equipment_service.unequip_to_inventory = MagicMock(return_value=([_sword("inventory")], {}))

    with patch("server.commands.inventory_unequip_command.get_shared_services") as mock_services:
        mock_services.return_value = (inventory_service, MagicMock(), equipment_service)
        result = await handle_unequip_command(
            {"slot": "main_hand"}, {"name": "TestPlayer"}, request, None, "TestPlayer"
        )

    assert result["result"] == "An error occurred while saving your inventory."
    view = harness.registry.peek(cast(uuid.UUID, player.player_id))
    assert view is not None and "main_hand" in view.inventory.equipped  # still equipped: rolled back
