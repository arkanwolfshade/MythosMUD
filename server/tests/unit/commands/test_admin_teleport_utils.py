"""Unit tests for admin_teleport_utils."""

from unittest.mock import AsyncMock, MagicMock
from uuid import UUID

import pytest

from server.commands.admin_teleport_utils import (
    broadcast_teleport_effects,
    create_teleport_effect_message,
    get_online_player_by_display_name,
    notify_player_of_teleport,
)

PLAYER_ID = UUID("11111111-1111-1111-1111-111111111111")


@pytest.mark.asyncio
async def test_get_online_player_no_connection_manager() -> None:
    assert await get_online_player_by_display_name("Bob", None) is None


@pytest.mark.asyncio
async def test_get_online_player_found() -> None:
    cm = MagicMock()
    cm.get_online_player_by_display_name.return_value = {"player_id": str(PLAYER_ID)}
    result = await get_online_player_by_display_name("Bob", cm)
    assert result is not None
    assert result["player_id"] == str(PLAYER_ID)


@pytest.mark.parametrize(
    ("teleport_type", "effect_type", "direction", "arrival", "expected_fragment"),
    [
        ("teleport", "departure", "north", None, "heading north"),
        ("teleport", "departure", None, None, "distorted air"),
        ("teleport", "arrival", None, "south", "from the south"),
        ("teleport", "arrival", None, None, "eldritch energy"),
        ("goto", "departure", None, None, "pale light"),
        ("goto", "arrival", None, "east", "from the east"),
        ("goto", "arrival", None, None, "displaced air"),
    ],
)
def test_create_teleport_effect_message(
    teleport_type: str,
    effect_type: str,
    direction: str | None,
    arrival: str | None,
    expected_fragment: str,
) -> None:
    msg = create_teleport_effect_message(
        "Alice",
        effect_type,
        teleport_type=teleport_type,
        direction=direction,
        arrival_direction=arrival,
    )
    assert expected_fragment in msg


def test_create_teleport_effect_message_fallback() -> None:
    msg = create_teleport_effect_message("Alice", "unknown", teleport_type="warp")
    assert "mysterious forces" in msg


@pytest.mark.asyncio
async def test_broadcast_teleport_effects_success() -> None:
    cm = MagicMock()
    cm.broadcast_to_room = AsyncMock()
    await broadcast_teleport_effects(
        cm,
        "Alice",
        "room-a",
        "room-b",
        "teleport",
        direction="north",
        target_player_id=str(PLAYER_ID),
    )
    assert cm.broadcast_to_room.await_count == 2
    first_call = cm.broadcast_to_room.await_args_list[0]
    assert first_call.args[0] == "room-a"
    assert first_call.kwargs["exclude_player"] == str(PLAYER_ID)


@pytest.mark.asyncio
async def test_broadcast_teleport_effects_handles_error() -> None:
    cm = MagicMock()
    cm.broadcast_to_room = AsyncMock(side_effect=ValueError("fail"))
    await broadcast_teleport_effects(cm, "Alice", "room-a", "room-b", "goto")


@pytest.mark.asyncio
async def test_notify_player_teleported_to() -> None:
    cm = MagicMock()
    cm.get_online_player_by_display_name.return_value = {"player_id": PLAYER_ID}
    cm.send_personal_message = AsyncMock()
    await notify_player_of_teleport(cm, "Bob", "Admin", "teleported_to")
    cm.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_notify_player_custom_message() -> None:
    cm = MagicMock()
    cm.get_online_player_by_display_name.return_value = {"player_id": str(PLAYER_ID)}
    cm.send_personal_message = AsyncMock()
    await notify_player_of_teleport(cm, "Bob", "Admin", "teleported_from", message="Custom msg")
    cm.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_notify_player_not_online() -> None:
    cm = MagicMock()
    cm.get_online_player_by_display_name.return_value = None
    await notify_player_of_teleport(cm, "Bob", "Admin", "teleported_to")


@pytest.mark.asyncio
async def test_broadcast_teleport_effects_no_broadcast_method() -> None:
    cm = object()
    await broadcast_teleport_effects(cm, "Alice", "room-a", "room-b", "teleport")


@pytest.mark.asyncio
async def test_notify_player_teleported_from_default_message() -> None:
    cm = MagicMock()
    cm.get_online_player_by_display_name.return_value = {"player_id": PLAYER_ID}
    cm.send_personal_message = AsyncMock()
    await notify_player_of_teleport(cm, "Bob", "Admin", "teleported_from")
    cm.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_notify_player_handles_error() -> None:
    cm = MagicMock()
    cm.get_online_player_by_display_name.side_effect = TypeError("bad")
    await notify_player_of_teleport(cm, "Bob", "Admin", "teleported_to")
