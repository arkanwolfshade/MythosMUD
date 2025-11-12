"""Tests for the administrative summon command."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.admin_summon_command import handle_summon_command
from server.game.items.item_factory import ItemFactory
from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry
from server.models.player import Player
from server.realtime.room_subscription_manager import RoomSubscriptionManager


def _make_player(name: str = "Armitage", room_id: str = "earth_arkhamcity_test_room") -> Player:
    player = Player(
        player_id=f"player-{name}",
        user_id=f"user-{name}",
        name=name,
        current_room_id=room_id,
    )
    player.set_inventory([])
    player.set_equipped_items({})
    player.set_admin_status(True)
    return player


def _build_item_factory(
    prototype_id: str = "artifact.miskatonic.codex",
) -> tuple[ItemFactory, PrototypeRegistry]:
    prototype = ItemPrototypeModel(
        prototype_id=prototype_id,
        name="Codex of Whispered Secrets",
        short_description="a codex bound in eel-skin",
        long_description="A tome humming with whispers from the Outer Dark.",
        item_type="artifact",
        weight=3.5,
        base_value=1200,
        durability=100,
        flags=["MAGICAL"],
        wear_slots=["OFF_HAND"],
    )
    registry = PrototypeRegistry({prototype_id: prototype}, [])
    return ItemFactory(registry), registry


@pytest.fixture()
def summon_context(monkeypatch):
    """Create a request context with mocked app state and services."""
    item_factory, registry = _build_item_factory()

    persistence = MagicMock()
    connection_manager = MagicMock()
    connection_manager.room_manager = RoomSubscriptionManager()
    connection_manager.broadcast_to_room = AsyncMock()
    connection_manager.online_players = {}

    state = SimpleNamespace(
        persistence=persistence,
        connection_manager=connection_manager,
        item_factory=item_factory,
        prototype_registry=registry,
    )

    request = MagicMock()
    request.app = SimpleNamespace(state=state)

    admin_logger = MagicMock()
    admin_logger.log_admin_command = MagicMock()
    admin_logger.log_permission_check = MagicMock()
    monkeypatch.setattr(
        "server.commands.admin_summon_command.get_admin_actions_logger", lambda: admin_logger
    )
    monkeypatch.setattr("server.commands.admin_commands.get_admin_actions_logger", lambda: admin_logger)

    return request, persistence, connection_manager, admin_logger


@pytest.mark.asyncio
async def test_admin_summon_item_creates_room_drop(summon_context):
    request, persistence, connection_manager, admin_logger = summon_context
    player = _make_player()
    persistence.get_player_by_name.return_value = player

    command_data = {
        "command_type": "summon",
        "prototype_id": "artifact.miskatonic.codex",
        "quantity": 2,
        "target_type": "item",
    }
    current_user = {"username": player.name}

    result = await handle_summon_command(command_data, current_user, request, MagicMock(), player.name)

    drops = connection_manager.room_manager.list_room_drops(str(player.current_room_id))
    assert len(drops) == 1
    stack = drops[0]
    assert stack["prototype_id"] == "artifact.miskatonic.codex"
    assert stack["quantity"] == 2
    assert "admin_summon" in stack.get("origin", {}).get("source", "")

    connection_manager.broadcast_to_room.assert_awaited()
    admin_logger.log_admin_command.assert_called_once()
    assert "You summon" in result["result"]


@pytest.mark.asyncio
async def test_summon_command_npc_stub_response(summon_context):
    request, persistence, connection_manager, admin_logger = summon_context
    player = _make_player()
    persistence.get_player_by_name.return_value = player

    command_data = {
        "command_type": "summon",
        "prototype_id": "npc.eldritch_terror",
        "quantity": 1,
        "target_type": "npc",
    }
    current_user = {"username": player.name}

    result = await handle_summon_command(command_data, current_user, request, MagicMock(), player.name)

    drops = connection_manager.room_manager.list_room_drops(str(player.current_room_id))
    assert drops == []
    connection_manager.broadcast_to_room.assert_not_called()
    admin_logger.log_admin_command.assert_called_once()
    assert "npc spawn" in result["result"].lower()


@pytest.mark.asyncio
async def test_summon_command_requires_admin_privileges(summon_context):
    request, persistence, _connection_manager, admin_logger = summon_context
    player = _make_player()
    player.set_admin_status(False)
    persistence.get_player_by_name.return_value = player

    command_data = {
        "command_type": "summon",
        "prototype_id": "artifact.miskatonic.codex",
    }
    current_user = {"username": player.name}

    result = await handle_summon_command(command_data, current_user, request, MagicMock(), player.name)

    assert "do not currently possess" in result["result"].lower()
    admin_logger.log_permission_check.assert_called_once()
