"""
Unit tests for admin shutdown command handler.

Tests the shutdown command functionality.
"""

import time
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from _pytest.mark.structures import MarkDecorator

from ....alias_storage import AliasStorage
from ....commands.admin_shutdown_command import (
    broadcast_shutdown_notification,
    calculate_notification_times,
    cancel_shutdown_countdown,
    get_shutdown_blocking_message,
    handle_shutdown_command,
    initiate_shutdown_countdown,
    is_shutdown_pending,
    parse_shutdown_parameters,
    validate_shutdown_admin_permission,
)


async def _await_shutdown_result(
    command_data: Mapping[str, object],
    current_user: Mapping[str, object],
    request: object,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Await handle_shutdown_command; explicit return keeps test assertions typed as dict."""

    # Handler is annotated with dict[str, Any]; copies satisfy runtime and avoid explicit Any here.
    raw = await handle_shutdown_command(
        dict(command_data),
        dict(current_user),
        request,
        alias_storage,
        player_name,
    )
    # Cast: some analyzers infer this await as Generator; implementation returns dict[str, str].
    return cast(dict[str, str], raw)  # pyright: ignore[reportUnnecessaryCast]


# MarkGenerator has no static asyncio attribute; getattr + MarkDecorator avoids
# basedpyright Literal["asyncio"] vs Mark.__getattr__(name: str) mismatch.
_asyncio_mark: MarkDecorator = cast(
    MarkDecorator,
    getattr(pytest.mark, "asyncio"),  # noqa: B009 -- .asyncio trips pyright; getattr keeps name typed as str
)


@dataclass
class _ShutdownContainerStub:
    server_shutdown_pending: bool = False
    shutdown_data: dict[str, object] | None = None


@dataclass
class _PendingCheckStateStub:
    container: _ShutdownContainerStub


@dataclass
class _PendingCheckAppStub:
    state: _PendingCheckStateStub


class _AppWithoutState:
    """App double with no state attribute (is_shutdown_pending must return False)."""


@dataclass
class _ShutdownCancelStateStub:
    container: _ShutdownContainerStub
    connection_manager: AsyncMock


@dataclass
class _ShutdownCancelAppStub:
    state: _ShutdownCancelStateStub


@dataclass
class _InitiateStateStub:
    server_shutdown_pending: bool = False
    shutdown_data: dict[str, object] | None = None
    task_registry: MagicMock = field(default_factory=MagicMock)
    connection_manager: AsyncMock = field(default_factory=AsyncMock)


@dataclass
class _InitiateAppStub:
    state: _InitiateStateStub


@_asyncio_mark
async def test_handle_shutdown_command_no_player_service():
    """Test handle_shutdown_command() when player service is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"]


@_asyncio_mark
async def test_handle_shutdown_command_player_not_found():
    """Test handle_shutdown_command() when player is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.get_player_by_name = AsyncMock(return_value=None)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Unable to verify" in result["result"] or "credentials" in result["result"]


@_asyncio_mark
async def test_handle_shutdown_command_no_permission():
    """Test handle_shutdown_command() when player lacks admin permission."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = False
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=False):
        result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "authorization" in result["result"] or "permission" in result["result"]


@_asyncio_mark
async def test_handle_shutdown_command_invalid_parameters():
    """Test handle_shutdown_command() with invalid parameters."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("error", None)),
    ):
        result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Invalid shutdown parameters" in result["result"] or "Usage" in result["result"]


@_asyncio_mark
async def test_handle_shutdown_command_cancel():
    """Test handle_shutdown_command() with cancel action."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("cancel", None)),
        patch("server.commands.admin_shutdown_command.cancel_shutdown_countdown", return_value=True),
    ):
        result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "cancelled" in result["result"].lower() or "cancel" in result["result"].lower()


@_asyncio_mark
async def test_handle_shutdown_command_cancel_no_active():
    """Test handle_shutdown_command() with cancel when no active shutdown."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("cancel", None)),
        patch("server.commands.admin_shutdown_command.cancel_shutdown_countdown", return_value=False),
    ):
        result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "no active shutdown" in result["result"].lower()


@_asyncio_mark
async def test_handle_shutdown_command_initiate():
    """Test handle_shutdown_command() with initiate action."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_state.shutdown_data = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("initiate", 60)),
        patch("server.commands.admin_shutdown_command.initiate_shutdown_countdown", return_value=True),
    ):
        result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "shutdown" in result["result"].lower()


@_asyncio_mark
async def test_handle_shutdown_command_initiate_superseding():
    """Test handle_shutdown_command() with initiate action superseding existing shutdown."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_state.shutdown_data = {"seconds": 30}
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("initiate", 60)),
        patch("server.commands.admin_shutdown_command.initiate_shutdown_countdown", return_value=True),
    ):
        result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "previous shutdown cancelled" in result["result"].lower() or "superseding" in result["result"].lower()


@_asyncio_mark
async def test_handle_shutdown_command_initiate_no_seconds():
    """Test handle_shutdown_command() with initiate action but no seconds."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("initiate", None)),
    ):
        result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Invalid shutdown configuration" in result["result"] or "seconds" in result["result"]


@_asyncio_mark
async def test_handle_shutdown_command_initiate_failure():
    """Test handle_shutdown_command() with initiate action that fails."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("initiate", 60)),
        patch("server.commands.admin_shutdown_command.initiate_shutdown_countdown", return_value=False),
    ):
        result: dict[str, str] = await _await_shutdown_result({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "error" in result["result"].lower() or "failed" in result["result"].lower()


def test_is_shutdown_pending_true():
    """Test is_shutdown_pending() returns True when shutdown is pending."""
    container = _ShutdownContainerStub(server_shutdown_pending=True)
    app = _PendingCheckAppStub(state=_PendingCheckStateStub(container=container))
    assert is_shutdown_pending(app) is True


def test_is_shutdown_pending_false():
    """Test is_shutdown_pending() returns False when shutdown is not pending."""
    container = _ShutdownContainerStub(server_shutdown_pending=False)
    app = _PendingCheckAppStub(state=_PendingCheckStateStub(container=container))
    assert is_shutdown_pending(app) is False


def test_is_shutdown_pending_no_state():
    """Test is_shutdown_pending() returns False when app has no state."""
    app = _AppWithoutState()
    assert is_shutdown_pending(app) is False


def test_get_shutdown_blocking_message_login():
    """Test get_shutdown_blocking_message() returns login message."""
    result = get_shutdown_blocking_message("login")
    assert "shutting down" in result.lower() or "try again" in result.lower()


def test_get_shutdown_blocking_message_character_creation():
    """Test get_shutdown_blocking_message() returns character creation message."""
    result = get_shutdown_blocking_message("character_creation")
    assert "character creation" in result.lower()


def test_get_shutdown_blocking_message_default():
    """Test get_shutdown_blocking_message() returns default message for unknown context."""
    result = get_shutdown_blocking_message("unknown_context")
    assert "shutting down" in result.lower()


@_asyncio_mark
async def test_validate_shutdown_admin_permission_no_player():
    """Test validate_shutdown_admin_permission() returns False when player is None."""
    result = await validate_shutdown_admin_permission(None, "TestPlayer")
    assert result is False


@_asyncio_mark
async def test_validate_shutdown_admin_permission_not_admin():
    """Test validate_shutdown_admin_permission() returns False when player is not admin."""
    mock_player = MagicMock()
    mock_player.is_admin = False
    result = await validate_shutdown_admin_permission(mock_player, "TestPlayer")
    assert result is False


@_asyncio_mark
async def test_validate_shutdown_admin_permission_admin():
    """Test validate_shutdown_admin_permission() returns True when player is admin."""
    mock_player = MagicMock()
    mock_player.is_admin = True
    result = await validate_shutdown_admin_permission(mock_player, "TestPlayer")
    assert result is True


def test_calculate_notification_times_short():
    """Test calculate_notification_times() for short countdown."""
    result = calculate_notification_times(5)
    assert 5 in result
    assert 4 in result
    assert 3 in result
    assert 2 in result
    assert 1 in result
    assert len(result) == 5


def test_calculate_notification_times_long():
    """Test calculate_notification_times() for long countdown."""
    result = calculate_notification_times(60)
    # Should have final 10 seconds (1-10)
    assert all(i in result for i in range(1, 11))
    # Should have 10-second intervals (10, 20, 30, 40, 50, 60)
    assert 60 in result
    assert 50 in result
    assert 40 in result
    assert 30 in result
    assert 20 in result
    assert 10 in result


def test_calculate_notification_times_sorted():
    """Test calculate_notification_times() returns sorted descending."""
    result = calculate_notification_times(25)
    assert result == sorted(result, reverse=True)


@_asyncio_mark
async def test_broadcast_shutdown_notification_success():
    """Test broadcast_shutdown_notification() successfully broadcasts."""
    broadcast_event: AsyncMock = AsyncMock()
    mock_connection_manager: AsyncMock = AsyncMock()
    mock_connection_manager.broadcast_global_event = broadcast_event
    result = await broadcast_shutdown_notification(mock_connection_manager, 10)
    assert result is True
    broadcast_event.assert_awaited_once()


@_asyncio_mark
async def test_broadcast_shutdown_notification_failure():
    """Test broadcast_shutdown_notification() handles errors."""
    mock_connection_manager = AsyncMock()
    mock_connection_manager.broadcast_global_event = AsyncMock(side_effect=OSError("Network error"))
    result = await broadcast_shutdown_notification(mock_connection_manager, 10)
    assert result is False


def test_parse_shutdown_parameters_no_args():
    """Test parse_shutdown_parameters() with no args defaults to 10 seconds."""
    action, seconds = parse_shutdown_parameters({})
    assert action == "initiate"
    assert seconds == 10


def test_parse_shutdown_parameters_cancel():
    """Test parse_shutdown_parameters() with cancel action."""
    action, seconds = parse_shutdown_parameters({"args": ["cancel"]})
    assert action == "cancel"
    assert seconds is None


def test_parse_shutdown_parameters_seconds():
    """Test parse_shutdown_parameters() with seconds."""
    action, seconds = parse_shutdown_parameters({"args": ["30"]})
    assert action == "initiate"
    assert seconds == 30


def test_parse_shutdown_parameters_invalid_negative():
    """Test parse_shutdown_parameters() with negative seconds."""
    action, seconds = parse_shutdown_parameters({"args": ["-5"]})
    assert action == "error"
    assert seconds is None


def test_parse_shutdown_parameters_invalid_zero():
    """Test parse_shutdown_parameters() with zero seconds."""
    action, seconds = parse_shutdown_parameters({"args": ["0"]})
    assert action == "error"
    assert seconds is None


def test_parse_shutdown_parameters_invalid_string():
    """Test parse_shutdown_parameters() with invalid string."""
    action, seconds = parse_shutdown_parameters({"args": ["invalid"]})
    assert action == "error"
    assert seconds is None


@_asyncio_mark
async def test_cancel_shutdown_countdown_no_active():
    """Test cancel_shutdown_countdown() when no shutdown is active."""
    container = _ShutdownContainerStub(server_shutdown_pending=False, shutdown_data=None)
    connection_manager: AsyncMock = AsyncMock()
    app = _ShutdownCancelAppStub(
        state=_ShutdownCancelStateStub(container=container, connection_manager=connection_manager)
    )
    result = await cancel_shutdown_countdown(app, "ArkanWolfshade")
    assert result is False


@_asyncio_mark
async def test_cancel_shutdown_countdown_success():
    """Test cancel_shutdown_countdown() successfully cancels shutdown."""
    mock_task = MagicMock()
    mock_task.done = MagicMock(return_value=False)
    shutdown_data: dict[str, object] = {
        "task": mock_task,
        "end_time": time.time() + 60,
    }
    container = _ShutdownContainerStub(server_shutdown_pending=True, shutdown_data=shutdown_data)
    connection_manager: AsyncMock = AsyncMock()
    connection_manager.broadcast_global_event = AsyncMock()
    app = _ShutdownCancelAppStub(
        state=_ShutdownCancelStateStub(container=container, connection_manager=connection_manager)
    )
    result = await cancel_shutdown_countdown(app, "ArkanWolfshade")
    assert result is True
    assert container.server_shutdown_pending is False


@_asyncio_mark
async def test_initiate_shutdown_countdown_success():
    """Test initiate_shutdown_countdown() successfully initiates shutdown."""
    mock_task = MagicMock()
    task_registry = MagicMock()
    task_registry.register_task = MagicMock(return_value=mock_task)
    state = _InitiateStateStub(server_shutdown_pending=False, task_registry=task_registry)
    app = _InitiateAppStub(state=state)
    result = await initiate_shutdown_countdown(app, 60, "ArkanWolfshade")
    assert result is True
    assert state.server_shutdown_pending is True


@_asyncio_mark
async def test_initiate_shutdown_countdown_supersedes():
    """Test initiate_shutdown_countdown() cancels existing shutdown."""
    mock_existing_task: MagicMock = MagicMock()
    mock_existing_task.done = MagicMock(return_value=False)
    cancel_mock: MagicMock = MagicMock()
    mock_existing_task.cancel = cancel_mock
    mock_new_task = MagicMock()
    task_registry = MagicMock()
    task_registry.register_task = MagicMock(return_value=mock_new_task)
    state = _InitiateStateStub(
        server_shutdown_pending=True,
        shutdown_data={"task": mock_existing_task},
        task_registry=task_registry,
    )
    app = _InitiateAppStub(state=state)
    result = await initiate_shutdown_countdown(app, 60, "ArkanWolfshade")
    assert result is True
    cancel_mock.assert_called_once()
