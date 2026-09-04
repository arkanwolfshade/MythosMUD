"""
Unit tests for admin_commands helper functions.

Tests helper functions in admin_commands.py module.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_teleport_commands import DIRECTION_OPPOSITES
from server.commands.admin_teleport_utils import (
    broadcast_teleport_effects,
    create_teleport_effect_message,
    get_online_player_by_display_name,
    notify_player_of_teleport,
)


def test_direction_opposites():
    """Test DIRECTION_OPPOSITES dictionary contains correct mappings."""
    assert DIRECTION_OPPOSITES["north"] == "south"
    assert DIRECTION_OPPOSITES["south"] == "north"
    assert DIRECTION_OPPOSITES["east"] == "west"
    assert DIRECTION_OPPOSITES["west"] == "east"
    assert DIRECTION_OPPOSITES["up"] == "down"
    assert DIRECTION_OPPOSITES["down"] == "up"
    assert DIRECTION_OPPOSITES["northeast"] == "southwest"
    assert DIRECTION_OPPOSITES["southwest"] == "northeast"
    assert DIRECTION_OPPOSITES["northwest"] == "southeast"
    assert DIRECTION_OPPOSITES["southeast"] == "northwest"


def test_create_teleport_effect_message_teleport_departure():
    """Test create_teleport_effect_message() for teleport departure."""
    result = create_teleport_effect_message("TestPlayer", "departure", teleport_type="teleport")
    assert "TestPlayer" in result
    assert "disappears" in result.lower() or "leaves" in result.lower()


def test_create_teleport_effect_message_teleport_departure_with_direction():
    """Test create_teleport_effect_message() for teleport departure with direction."""
    result = create_teleport_effect_message("TestPlayer", "departure", teleport_type="teleport", direction="north")
    assert "TestPlayer" in result
    assert "north" in result.lower()


def test_create_teleport_effect_message_teleport_arrival():
    """Test create_teleport_effect_message() for teleport arrival."""
    result = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="teleport")
    assert "TestPlayer" in result
    assert "arrives" in result.lower()


def test_create_teleport_effect_message_teleport_arrival_with_direction():
    """Test create_teleport_effect_message() for teleport arrival with direction."""
    result = create_teleport_effect_message(
        "TestPlayer", "arrival", teleport_type="teleport", arrival_direction="north"
    )
    assert "TestPlayer" in result
    assert "north" in result.lower()


def test_create_teleport_effect_message_goto_departure():
    """Test create_teleport_effect_message() for goto departure."""
    result = create_teleport_effect_message("TestPlayer", "departure", teleport_type="goto")
    assert "TestPlayer" in result
    assert "vanishes" in result.lower()


def test_create_teleport_effect_message_goto_arrival():
    """Test create_teleport_effect_message() for goto arrival."""
    result = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="goto")
    assert "TestPlayer" in result
    assert "appears" in result.lower() or "arrives" in result.lower()


def test_create_teleport_effect_message_goto_arrival_with_direction():
    """Test create_teleport_effect_message() for goto arrival with direction."""
    result = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="goto", arrival_direction="south")
    assert "TestPlayer" in result
    assert "south" in result.lower()


def test_create_teleport_effect_message_unknown_type():
    """Test create_teleport_effect_message() for unknown teleport type."""
    result = create_teleport_effect_message("TestPlayer", "departure", teleport_type="unknown")
    assert "TestPlayer" in result
    assert "mysterious" in result.lower()


@pytest.mark.asyncio
async def test_get_online_player_by_display_name_no_manager() -> None:
    assert await get_online_player_by_display_name("Bob", None) is None


@pytest.mark.asyncio
async def test_get_online_player_by_display_name_found() -> None:
    cm = MagicMock()
    cm.get_online_player_by_display_name.return_value = {"player_id": str(uuid.uuid4())}
    result = await get_online_player_by_display_name("Bob", cm)
    assert result is not None


@pytest.mark.asyncio
async def test_broadcast_teleport_effects() -> None:
    cm = MagicMock()
    cm.broadcast_to_room = AsyncMock()
    with patch("server.commands.admin_teleport_utils.build_event", return_value={"event": "x"}):
        await broadcast_teleport_effects(cm, "Alice", "room_a", "room_b", "teleport", direction="north")
    assert cm.broadcast_to_room.await_count == 2


@pytest.mark.asyncio
async def test_notify_player_of_teleport_custom_message() -> None:
    player_id = uuid.uuid4()
    cm = MagicMock()
    cm.get_online_player_by_display_name.return_value = {"player_id": str(player_id)}
    cm.send_personal_message = AsyncMock()
    with patch("server.commands.admin_teleport_utils.build_event", return_value={"event": "x"}):
        await notify_player_of_teleport(cm, "Bob", "Admin", "teleported_to", message="Custom msg")
    cm.send_personal_message.assert_awaited_once()
