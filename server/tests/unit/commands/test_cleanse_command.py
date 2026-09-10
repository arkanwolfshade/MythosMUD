"""Unit tests for the cleanse command handler (#804)."""

# pyright: reportAny=false
# TEST_MOCK: MagicMock's dynamic attribute chains (request.app.state.container.*) resolve to Any
# throughout this file, mirroring test_lucidity_recovery_commands.py's identical, already-
# baselined pattern for the same request/app/state/container shape -- this file is new, so it has
# no baseline entry of its own for the same, otherwise-unavoidable mock-typing noise.

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.cleanse_command import handle_cleanse_command
from server.services.corruption_service import CorruptionActionOnCooldownError


@pytest.fixture
def mock_request() -> MagicMock:
    """Create a mock request with app state and container."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.container = MagicMock()
    return request


@pytest.fixture
def mock_persistence() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def mock_player() -> MagicMock:
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    return player


@pytest.mark.asyncio
async def test_handle_cleanse_command_no_persistence(mock_request: MagicMock) -> None:
    mock_request.app.state.container.async_persistence = None
    mock_request.app.state.persistence = None

    result = await handle_cleanse_command({}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "ley lines are inaccessible" in result["result"]


@pytest.mark.asyncio
async def test_handle_cleanse_command_player_not_found(mock_request: MagicMock, mock_persistence: AsyncMock) -> None:
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_request.app.state.container.async_persistence = mock_persistence

    result = await handle_cleanse_command({}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "identity wavers" in result["result"]


@pytest.mark.asyncio
async def test_handle_cleanse_command_success(
    mock_request: MagicMock, mock_persistence: AsyncMock, mock_player: MagicMock
) -> None:
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.container.async_persistence = mock_persistence

    mock_result = MagicMock(delta=-8, new_value=12)
    with patch("server.commands.cleanse_command.CorruptionService") as mock_service_class:
        mock_service = AsyncMock()
        mock_service_class.return_value = mock_service
        mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

        result = await handle_cleanse_command({}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "cleansing rite" in result["result"]
    assert "8" in result["result"]
    assert "12/100" in result["result"]


@pytest.mark.asyncio
async def test_handle_cleanse_command_cooldown(
    mock_request: MagicMock, mock_persistence: AsyncMock, mock_player: MagicMock
) -> None:
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.container.async_persistence = mock_persistence

    mock_cooldown_expiry = datetime.now(UTC) + timedelta(hours=3)
    with patch("server.commands.cleanse_command.CorruptionService") as mock_service_class:
        mock_service = AsyncMock()
        mock_service_class.return_value = mock_service
        mock_service.perform_recovery_action = AsyncMock(side_effect=CorruptionActionOnCooldownError())
        mock_service.get_cooldown_expiry = AsyncMock(return_value=mock_cooldown_expiry)

        result = await handle_cleanse_command({}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "lingers in your blood" in result["result"]


@pytest.mark.asyncio
async def test_handle_cleanse_command_cooldown_no_expiry(
    mock_request: MagicMock, mock_persistence: AsyncMock, mock_player: MagicMock
) -> None:
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.container.async_persistence = mock_persistence

    with patch("server.commands.cleanse_command.CorruptionService") as mock_service_class:
        mock_service = AsyncMock()
        mock_service_class.return_value = mock_service
        mock_service.perform_recovery_action = AsyncMock(side_effect=CorruptionActionOnCooldownError())
        mock_service.get_cooldown_expiry = AsyncMock(return_value=None)

        result = await handle_cleanse_command({}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "residue has not yet faded" in result["result"]
