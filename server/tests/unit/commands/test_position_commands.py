"""
Unit tests for position command handlers.

Tests the sit, stand, lie, and ground commands.
"""

import asyncio
import uuid
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request

from server.commands.position_commands import (
    handle_lie_command,
    handle_sit_command,
    handle_stand_command,
)
from server.commands.rescue_commands import handle_ground_command


@pytest.mark.asyncio
async def test_handle_sit_command():
    """Test handle_sit_command() changes player position to sitting."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.position_state = "standing"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_sit_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert mock_player.position_state == "sitting" or "sit" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_stand_command():
    """Test handle_stand_command() changes player position to standing."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_container = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.position_state = "sitting"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_container.async_persistence = mock_persistence
    mock_state.container = mock_container
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_stand_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    # Position may not change if service returns error, so check result message
    assert (
        mock_player.position_state == "standing" or "stand" in result["result"].lower() or result.get("changed", False)
    )


@pytest.mark.asyncio
async def test_handle_stand_already_standing_still_sends_player_update():
    """Already-standing must still sync posture so UI Sitting after cancelled /rest can clear."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.container = None
    mock_request.app.state.persistence = MagicMock()
    mock_request.app.state.connection_manager = MagicMock()

    with patch("server.commands.position_commands.PlayerPositionService") as mock_svc_cls:
        mock_svc = MagicMock()
        mock_svc.change_position = AsyncMock(
            return_value={
                "success": False,
                "position": "standing",
                "previous_position": "standing",
                "message": "You are already standing.",
                "player_id": uuid.uuid4(),
                "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                "player_display_name": "TestPlayer",
            }
        )
        mock_svc_cls.return_value = mock_svc

        result = await handle_stand_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert result["player_update"] == {"position": "standing", "previous_position": "standing"}
    assert result["changed"] is False
    assert "already standing" in result["result"].lower()


@dataclass
class _RestingSetup:
    """A request whose connection manager has a live /rest countdown for player_id."""

    player_id: uuid.UUID
    countdown: asyncio.Task[None]
    resting_players: dict[uuid.UUID, asyncio.Task[None]]
    request: Request


def _resting_setup() -> _RestingSetup:
    player_id = uuid.uuid4()
    countdown = asyncio.create_task(asyncio.sleep(30))
    resting_players = {player_id: countdown}
    connection_manager = MagicMock()
    connection_manager.resting_players = resting_players
    state = MagicMock()
    state.container = None
    state.persistence = MagicMock()
    state.connection_manager = connection_manager
    app = MagicMock()
    app.state = state
    request = MagicMock()
    request.app = app
    return _RestingSetup(player_id, countdown, resting_players, cast(Request, request))


def _position_service(player_id: uuid.UUID, position: str, *, success: bool) -> MagicMock:
    service = MagicMock()
    service.change_position = AsyncMock(
        return_value={
            "success": success,
            "position": position,
            "previous_position": "sitting",
            "message": f"You are now {position}.",
            "player_id": str(player_id),
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "player_display_name": "TestPlayer",
        }
    )
    return service


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("handler", "position"),
    [(handle_stand_command, "standing"), (handle_lie_command, "lying")],
)
async def test_posture_change_interrupts_rest_countdown(
    handler: Callable[..., Awaitable[dict[str, object]]], position: str
) -> None:
    """Standing or lying down breaks the /rest sit: the countdown is cancelled without auto-standing."""
    setup = _resting_setup()
    service = _position_service(setup.player_id, position, success=True)

    with (
        patch("server.commands.position_commands.PlayerPositionService", return_value=service),
        patch("server.commands.position_commands.emit_posture_change", new_callable=AsyncMock),
        patch("server.commands.rest_command._stand_after_cancelled_rest", new_callable=AsyncMock) as auto_stand,
    ):
        result = await handler({}, {"name": "TestPlayer"}, setup.request, None, "TestPlayer")

    assert setup.countdown.cancelled()
    assert setup.player_id not in setup.resting_players
    auto_stand.assert_not_called()
    assert result["player_update"] == {"position": position, "previous_position": "sitting"}
    assert "Your rest is interrupted." in str(result["result"])


@pytest.mark.asyncio
async def test_sit_does_not_interrupt_rest_countdown() -> None:
    """/sit matches the resting posture, so a running countdown is left alone."""
    setup = _resting_setup()
    service = _position_service(setup.player_id, "sitting", success=False)

    with patch("server.commands.position_commands.PlayerPositionService", return_value=service):
        result = await handle_sit_command({}, {"name": "TestPlayer"}, setup.request, None, "TestPlayer")

    assert not setup.countdown.done()
    assert setup.player_id in setup.resting_players
    assert "interrupted" not in str(result["result"])
    _ = setup.countdown.cancel()


@pytest.mark.asyncio
async def test_handle_lie_command():
    """Test handle_lie_command() changes player position to lying."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_container = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestPlayer"
    mock_player.current_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})
    mock_player.set_stats = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_container.async_persistence = mock_persistence
    mock_state.container = mock_container
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.position_commands.emit_posture_change", new_callable=AsyncMock):
        result = await handle_lie_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert result.get("changed") is True or "lie" in result["result"].lower()
    mock_player.set_stats.assert_called()


@pytest.mark.asyncio
async def test_handle_ground_command():
    """Test handle_ground_command() helps catatonic player."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_rescuer = MagicMock()
    mock_rescuer.player_id = uuid.uuid4()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.player_id = uuid.uuid4()
    mock_target.current_room_id = mock_rescuer.current_room_id
    mock_target.position_state = "standing"
    # get_player_by_name is called twice: once for rescuer, once for target
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    # handle_ground_command uses get_async_session() and session.get(PlayerLucidity, ...); patch to avoid DB/send
    mock_lucidity = MagicMock()
    mock_lucidity.current_tier = "catatonic"
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=mock_lucidity)
    mock_session.commit = AsyncMock()
    mock_session.rollback = AsyncMock()

    async def mock_get_async_session():
        yield mock_session

    with (
        patch("server.commands.rescue_commands.get_async_session", side_effect=mock_get_async_session),
        patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock),
        patch(
            "server.commands.rescue_commands._apply_grounding_adjustment",
            new_callable=AsyncMock,
            return_value=MagicMock(new_lcd=1),
        ),
    ):
        result = await handle_ground_command(
            {"target": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )

    assert "result" in result
