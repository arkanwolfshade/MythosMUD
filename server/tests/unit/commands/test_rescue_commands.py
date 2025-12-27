"""
Unit tests for rescue commands.

Tests the /ground command for rescuing catatonic players.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.rescue_commands import handle_ground_command
from server.models.lucidity import PlayerLucidity


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    app = MagicMock()
    app.state = MagicMock()
    request = MagicMock()
    request.app = app
    return request


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def mock_rescuer():
    """Create a mock rescuer player."""
    rescuer = MagicMock()
    rescuer.player_id = uuid.uuid4()
    rescuer.current_room_id = "room_001"
    return rescuer


@pytest.fixture
def mock_target():
    """Create a mock target player."""
    target = MagicMock()
    target.player_id = uuid.uuid4()
    target.current_room_id = "room_001"
    return target


@pytest.fixture
def mock_lucidity_record():
    """Create a mock lucidity record."""
    record = MagicMock(spec=PlayerLucidity)
    record.current_tier = "catatonic"
    record.current_lcd = 0.0
    return record


@pytest.mark.asyncio
async def test_handle_ground_command_no_persistence(mock_request):
    """Test ground command when persistence is not available."""
    mock_request.app.state.persistence = None
    result = await handle_ground_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
    assert "no anchor to reality can be found" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_no_rescuer(mock_request, mock_persistence):
    """Test ground command when rescuer is not found."""
    mock_request.app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.return_value = None
    result = await handle_ground_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
    assert "Your identity drifts" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_no_target_name(mock_request, mock_persistence, mock_rescuer):
    """Test ground command when no target is specified."""
    mock_request.app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.return_value = mock_rescuer
    result = await handle_ground_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
    assert "Ground whom?" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_target_not_found(mock_request, mock_persistence, mock_rescuer):
    """Test ground command when target is not found."""
    mock_request.app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, None]
    result = await handle_ground_command(
        {"target_player": "Nonexistent"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "No echoes of" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_different_rooms(mock_request, mock_persistence, mock_rescuer, mock_target):
    """Test ground command when rescuer and target are in different rooms."""
    mock_request.app.state.persistence = mock_persistence
    mock_target.current_room_id = "room_002"
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, mock_target]
    result = await handle_ground_command(
        {"target_player": "TargetPlayer"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "not within reach" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_no_lucidity_record(mock_request, mock_persistence, mock_rescuer, mock_target):
    """Test ground command when lucidity record is not found."""
    mock_request.app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, mock_target]

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=None)
        yield mock_session

    with patch("server.commands.rescue_commands.get_async_session", return_value=async_gen()):
        result = await handle_ground_command(
            {"target_player": "TargetPlayer"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
        )
        assert "aura cannot be located" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_not_catatonic(mock_request, mock_persistence, mock_rescuer, mock_target, mock_lucidity_record):
    """Test ground command when target is not catatonic."""
    mock_request.app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, mock_target]
    mock_lucidity_record.current_tier = "stable"

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=mock_lucidity_record)
        yield mock_session

    with patch("server.commands.rescue_commands.get_async_session", return_value=async_gen()):
        result = await handle_ground_command(
            {"target_player": "TargetPlayer"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
        )
        assert "isn't catatonic" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_success(mock_request, mock_persistence, mock_rescuer, mock_target, mock_lucidity_record):
    """Test ground command success."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.catatonia_registry = None
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, mock_target]

    mock_lucidity_service = AsyncMock()
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=mock_lucidity_record)
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.rescue_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.rescue_commands.LucidityService", return_value=mock_lucidity_service):
            with patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock) as mock_send_event:
                result = await handle_ground_command(
                    {"target_player": "TargetPlayer"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
                )
                assert "anchor their mind" in result["result"]
                assert "1.0/100" in result["result"]
                # Verify rescue update events were sent
                assert mock_send_event.await_count >= 4  # channeling (2) + success (2)


@pytest.mark.asyncio
async def test_handle_ground_command_service_error(mock_request, mock_persistence, mock_rescuer, mock_target, mock_lucidity_record):
    """Test ground command when service raises an error."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.catatonia_registry = None
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, mock_target]

    mock_lucidity_service = AsyncMock()
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(side_effect=ValueError("Service error"))

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=mock_lucidity_record)
        mock_session.rollback = AsyncMock()
        yield mock_session

    with patch("server.commands.rescue_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.rescue_commands.LucidityService", return_value=mock_lucidity_service):
            with patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock):
                result = await handle_ground_command(
                    {"target_player": "TargetPlayer"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
                )
                assert "Eldritch interference" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_target_uses_target_key(mock_request, mock_persistence, mock_rescuer, mock_target, mock_lucidity_record):
    """Test ground command when target is specified using 'target' key."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.catatonia_registry = None
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, mock_target]

    mock_lucidity_service = AsyncMock()
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=mock_lucidity_record)
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.rescue_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.rescue_commands.LucidityService", return_value=mock_lucidity_service):
            with patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock):
                result = await handle_ground_command(
                    {"target": "TargetPlayer"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
                )
                assert "anchor their mind" in result["result"]


@pytest.mark.asyncio
async def test_handle_ground_command_delta_calculation(mock_request, mock_persistence, mock_rescuer, mock_target, mock_lucidity_record):
    """Test ground command delta calculation."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.catatonia_registry = None
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, mock_target]
    mock_lucidity_record.current_lcd = 0.5  # Already at 0.5, should get 0.5 delta

    mock_lucidity_service = AsyncMock()
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=mock_lucidity_record)
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.rescue_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.rescue_commands.LucidityService", return_value=mock_lucidity_service):
            with patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock):
                result = await handle_ground_command(
                    {"target_player": "TargetPlayer"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
                )
                # Verify service was called with correct delta
                call_args = mock_lucidity_service.apply_lucidity_adjustment.call_args
                assert call_args[0][1] == 0.5  # delta is second positional argument
                assert result["result"] is not None


@pytest.mark.asyncio
async def test_handle_ground_command_delta_minimum(mock_request, mock_persistence, mock_rescuer, mock_target, mock_lucidity_record):
    """Test ground command ensures minimum delta of 1."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.catatonia_registry = None
    mock_persistence.get_player_by_name.side_effect = [mock_rescuer, mock_target]
    mock_lucidity_record.current_lcd = 1.0  # Already at 1.0, should still get delta of 1

    mock_lucidity_service = AsyncMock()
    mock_result = MagicMock()
    mock_result.new_lcd = 2.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    async def async_gen():
        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=mock_lucidity_record)
        mock_session.commit = AsyncMock()
        yield mock_session

    with patch("server.commands.rescue_commands.get_async_session", return_value=async_gen()):
        with patch("server.commands.rescue_commands.LucidityService", return_value=mock_lucidity_service):
            with patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock):
                result = await handle_ground_command(
                    {"target_player": "TargetPlayer"}, {"username": "testuser"}, mock_request, None, "TestPlayer"
                )
                # Verify service was called with minimum delta of 1
                call_args = mock_lucidity_service.apply_lucidity_adjustment.call_args
                assert call_args[0][1] == 1.0  # delta is second positional argument
                assert result["result"] is not None
