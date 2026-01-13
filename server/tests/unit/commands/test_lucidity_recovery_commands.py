"""
Unit tests for lucidity recovery command handlers.

Tests the pray, meditate, group_solace, therapy, and folk_tonic commands.
"""

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which pylint incorrectly flags as redefining names from outer scope, this is standard pytest usage and cannot be avoided

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.lucidity_recovery_commands import (
    handle_folk_tonic_command,
    handle_group_solace_command,
    handle_meditate_command,
    handle_pray_command,
    handle_therapy_command,
)
from server.services.active_lucidity_service import LucidityActionOnCooldownError, UnknownLucidityActionError


@pytest.fixture
def mock_request():
    """Create a mock request with app state."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_persistence():
    """Create a mock persistence."""
    persistence = AsyncMock()
    return persistence


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    return player


@pytest.mark.asyncio
async def test_handle_pray_command_no_persistence(mock_request):
    """Test handle_pray_command when persistence is not available."""
    mock_request.app.state.persistence = None

    result = await handle_pray_command(
        command_data={},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        alias_storage=None,
        player_name="TestPlayer",
    )

    assert "ley lines are inaccessible" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_player_not_found(mock_request, mock_persistence):
    """Test handle_pray_command when player is not found."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_request.app.state.persistence = mock_persistence

    result = await handle_pray_command(
        command_data={},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        alias_storage=None,
        player_name="TestPlayer",
    )

    assert "identity wavers" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_no_room(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command when player has no room."""
    mock_player.current_room_id = None
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    result = await handle_pray_command(
        command_data={},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        alias_storage=None,
        player_name="TestPlayer",
    )

    assert "locus in space" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_success(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command successful execution."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    # Explicitly set mp_regeneration_service to None (MagicMock returns MagicMock for any attribute)
    mock_request.app.state.mp_regeneration_service = None

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "pray rite" in result["result"]
            assert "+5" in result["result"]
            assert "55/100" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_cooldown(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command when action is on cooldown."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_cooldown = MagicMock()
    mock_cooldown.cooldown_expires_at = datetime.now(UTC) + timedelta(minutes=5)

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(side_effect=LucidityActionOnCooldownError())
            mock_service.get_action_cooldown = AsyncMock(return_value=mock_cooldown)

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "sigils are still cooling" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_unknown_action(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command with unknown action."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(side_effect=UnknownLucidityActionError())

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "uncharted" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_with_mp_restoration(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command with MP restoration."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_mp_service = AsyncMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={"mp_restored": 10})
    mock_request.app.state.mp_regeneration_service = mock_mp_service

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "magic points" in result["result"]
            assert "10" in result["result"]
            mock_mp_service.restore_mp_from_rest.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_meditate_command_delegates(mock_request, mock_persistence, mock_player):
    """Test handle_meditate_command delegates to _perform_recovery_action."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    # Explicitly set mp_regeneration_service to None (MagicMock returns MagicMock for any attribute)
    mock_request.app.state.mp_regeneration_service = None

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_meditate_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "meditate rite" in result["result"]


@pytest.mark.asyncio
async def test_handle_group_solace_command_delegates(mock_request, mock_persistence, mock_player):
    """Test handle_group_solace_command delegates to _perform_recovery_action."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_group_solace_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "group solace" in result["result"]


@pytest.mark.asyncio
async def test_handle_therapy_command_delegates(mock_request, mock_persistence, mock_player):
    """Test handle_therapy_command delegates to _perform_recovery_action."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_therapy_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "therapy" in result["result"]


@pytest.mark.asyncio
async def test_handle_folk_tonic_command_delegates(mock_request, mock_persistence, mock_player):
    """Test handle_folk_tonic_command delegates to _perform_recovery_action."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_folk_tonic_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "folk tonic" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_os_error(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command handles OSError."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_session = AsyncMock()
    mock_session.rollback = AsyncMock()

    async def async_gen():
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(side_effect=OSError("File system error"))

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "Anomalous interference" in result["result"]
            mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_pray_command_cooldown_no_expiry(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command when cooldown has no expiry time."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_cooldown = MagicMock()
    mock_cooldown.cooldown_expires_at = None

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(side_effect=LucidityActionOnCooldownError())
            mock_service.get_action_cooldown = AsyncMock(return_value=mock_cooldown)

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "ritual pathways are still resonating" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_cooldown_no_cooldown_object(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command when get_action_cooldown returns None."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(side_effect=LucidityActionOnCooldownError())
            mock_service.get_action_cooldown = AsyncMock(return_value=None)

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "ritual pathways are still resonating" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_negative_delta(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command with negative delta."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.mp_regeneration_service = None

    mock_result = MagicMock()
    mock_result.delta = -5  # Negative delta
    mock_result.new_lcd = 45

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "-5" in result["result"]
            assert "45/100" in result["result"]


@pytest.mark.asyncio
async def test_handle_meditate_command_with_mp_restoration(mock_request, mock_persistence, mock_player):
    """Test handle_meditate_command with MP restoration."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_mp_service = AsyncMock()
    mock_mp_service.restore_mp_from_meditation = AsyncMock(return_value={"mp_restored": 15})
    mock_request.app.state.mp_regeneration_service = mock_mp_service

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_meditate_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "magic points" in result["result"]
            assert "15" in result["result"]
            mock_mp_service.restore_mp_from_meditation.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_pray_command_mp_restored_zero(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command when MP restoration returns 0."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_mp_service = AsyncMock()
    mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={"mp_restored": 0})
    mock_request.app.state.mp_regeneration_service = mock_mp_service

    mock_result = MagicMock()
    mock_result.delta = 5
    mock_result.new_lcd = 55

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(return_value=mock_result)

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            # Should not include MP message when mp_restored is 0
            assert "magic points" not in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_no_app(mock_request):
    """Test handle_pray_command when app is None."""
    mock_request.app = None

    result = await handle_pray_command(
        command_data={},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        alias_storage=None,
        player_name="TestPlayer",
    )

    assert "ley lines are inaccessible" in result["result"]


@pytest.mark.asyncio
async def test_handle_pray_command_cooldown_naive_datetime(mock_request, mock_persistence, mock_player):
    """Test handle_pray_command when cooldown expiry is naive datetime."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_cooldown = MagicMock()
    # Naive datetime (no timezone)
    mock_cooldown.cooldown_expires_at = datetime.now() + timedelta(minutes=5)

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(side_effect=LucidityActionOnCooldownError())
            mock_service.get_action_cooldown = AsyncMock(return_value=mock_cooldown)

            result = await handle_pray_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "sigils are still cooling" in result["result"]


@pytest.mark.asyncio
async def test_handle_meditate_command_cooldown(mock_request, mock_persistence, mock_player):
    """Test handle_meditate_command when action is on cooldown."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_cooldown = MagicMock()
    mock_cooldown.cooldown_expires_at = datetime.now(UTC) + timedelta(minutes=3)

    async def async_gen():
        mock_session = AsyncMock()
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(side_effect=LucidityActionOnCooldownError())
            mock_service.get_action_cooldown = AsyncMock(return_value=mock_cooldown)

            result = await handle_meditate_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "sigils are still cooling" in result["result"]


@pytest.mark.asyncio
async def test_handle_group_solace_command_unknown_action(mock_request, mock_persistence, mock_player):
    """Test handle_group_solace_command with unknown action."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence

    mock_session = AsyncMock()
    mock_session.rollback = AsyncMock()

    async def async_gen():
        yield mock_session

    with patch("server.commands.lucidity_recovery_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.lucidity_recovery_commands.ActiveLucidityService") as mock_service_class:
            mock_service = AsyncMock()
            mock_service_class.return_value = mock_service
            mock_service.perform_recovery_action = AsyncMock(side_effect=UnknownLucidityActionError())

            result = await handle_group_solace_command(
                command_data={},
                current_user={"username": "TestPlayer"},
                request=mock_request,
                alias_storage=None,
                player_name="TestPlayer",
            )

            assert "uncharted" in result["result"]
            mock_session.rollback.assert_awaited_once()
