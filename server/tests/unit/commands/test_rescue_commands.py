"""
Unit tests for rescue command handlers.

Tests the rescue command functionality.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.rescue_commands import handle_ground_command, handle_rescue_command
from server.models.lucidity import PlayerLucidity


@pytest.mark.asyncio
@patch("server.commands.rescue_commands.RescueService")
async def test_handle_rescue_command(mock_rescue_service_cls):
    """Test handle_rescue_command() delegates to RescueService."""
    mock_service = AsyncMock()
    mock_service.rescue.return_value = {"result": "rescued"}
    mock_rescue_service_cls.return_value = mock_service

    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock(), catatonia_registry=None)

    result = await handle_rescue_command(
        {"target": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    mock_rescue_service_cls.assert_called_once()
    mock_service.rescue.assert_awaited_once_with("OtherPlayer", {"name": "TestPlayer"}, "TestPlayer")
    assert result == {"result": "rescued"}


@pytest.mark.asyncio
async def test_handle_rescue_command_no_target():
    """Test handle_rescue_command() handles missing target."""
    result = await handle_rescue_command({}, {}, MagicMock(), None, "TestPlayer")
    assert "result" in result
    assert "target" in result["result"].lower() or "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rescue_command_no_persistence():
    """Test handle_rescue_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_rescue_command({"target": "OtherPlayer"}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rescue_command_target_player_key():
    """Test handle_rescue_command() accepts target_player key."""
    mock_service = AsyncMock()
    mock_service.rescue.return_value = {"result": "rescued"}
    with patch("server.commands.rescue_commands.RescueService", return_value=mock_service):
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = MagicMock(persistence=MagicMock(), catatonia_registry=None)
        result = await handle_rescue_command(
            {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )
        mock_service.rescue.assert_awaited_once_with("OtherPlayer", {"name": "TestPlayer"}, "TestPlayer")
        assert result == {"result": "rescued"}


@pytest.mark.asyncio
async def test_handle_rescue_command_no_app():
    """Test handle_rescue_command() handles missing app."""
    mock_request = MagicMock()
    mock_request.app = None
    result = await handle_rescue_command({"target": "OtherPlayer"}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rescue_command_no_state():
    """Test handle_rescue_command() handles missing app.state."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = None
    result = await handle_rescue_command({"target": "OtherPlayer"}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_no_persistence():
    """Test handle_ground_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None
    result = await handle_ground_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "anchor to reality" in result["result"].lower() or "falters" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_no_target():
    """Test handle_ground_command() handles missing target."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_persistence.get_player_by_name = AsyncMock(return_value=MagicMock())
    result = await handle_ground_command({}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "whom" in result["result"].lower() or "target" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_rescuer_not_found():
    """Test handle_ground_command() handles rescuer not found."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "identity drifts" in result["result"].lower() or "bearings" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_target_not_found():
    """Test handle_ground_command() handles target not found."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, None])
    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "echoes" in result["result"].lower() or "not found" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_different_rooms():
    """Test handle_ground_command() handles different rooms."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.current_room_id = uuid.uuid4()  # Different room
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not within reach" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_no_rescuer_room():
    """Test handle_ground_command() handles rescuer with no room."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.current_room_id = None
    mock_target = MagicMock()
    mock_target.current_room_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not within reach" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_lucidity_record_not_found():
    """Test handle_ground_command() handles missing lucidity record."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.player_id = uuid.uuid4()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.player_id = uuid.uuid4()
    mock_target.current_room_id = mock_rescuer.current_room_id
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=None)
    with patch("server.commands.rescue_commands.get_async_session") as mock_session_factory:

        async def session_gen():
            yield mock_session

        mock_session_factory.return_value = session_gen()
        result = await handle_ground_command(
            {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
        )
        assert "result" in result
        assert "aura cannot be located" in result["result"].lower() or "lucidity" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_not_catatonic():
    """Test handle_ground_command() handles target not catatonic."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.player_id = uuid.uuid4()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.player_id = uuid.uuid4()
    mock_target.current_room_id = mock_rescuer.current_room_id
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    mock_lucidity_record = MagicMock(spec=PlayerLucidity)
    mock_lucidity_record.current_tier = "stable"  # Not catatonic
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=mock_lucidity_record)
    with patch("server.commands.rescue_commands.get_async_session") as mock_session_factory:

        async def session_gen():
            yield mock_session

        mock_session_factory.return_value = session_gen()
        result = await handle_ground_command(
            {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
        )
        assert "result" in result
        assert "isn't catatonic" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_success():
    """Test handle_ground_command() successfully grounds target."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock(), catatonia_registry=None)
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.player_id = uuid.uuid4()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.player_id = uuid.uuid4()
    mock_target.current_room_id = mock_rescuer.current_room_id
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    mock_lucidity_record = MagicMock(spec=PlayerLucidity)
    mock_lucidity_record.current_tier = "catatonic"
    mock_lucidity_record.current_lcd = 0.0
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=mock_lucidity_record)
    mock_session.commit = AsyncMock()
    mock_lucidity_service = MagicMock()
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    with patch("server.commands.rescue_commands.get_async_session") as mock_session_factory:
        with patch("server.commands.rescue_commands.LucidityService", return_value=mock_lucidity_service):
            with patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock):

                async def session_gen():
                    yield mock_session

                mock_session_factory.return_value = session_gen()
                result = await handle_ground_command(
                    {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
                )
                assert "result" in result
                assert "kneel" in result["result"].lower() or "anchor" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_target_player_key():
    """Test handle_ground_command() accepts target_player key."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.player_id = uuid.uuid4()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.player_id = uuid.uuid4()
    mock_target.current_room_id = mock_rescuer.current_room_id
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    mock_lucidity_record = MagicMock(spec=PlayerLucidity)
    mock_lucidity_record.current_tier = "catatonic"
    mock_lucidity_record.current_lcd = 0.0
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=mock_lucidity_record)
    mock_session.commit = AsyncMock()
    mock_lucidity_service = MagicMock()
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    with patch("server.commands.rescue_commands.get_async_session") as mock_session_factory:
        with patch("server.commands.rescue_commands.LucidityService", return_value=mock_lucidity_service):
            with patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock):

                async def session_gen():
                    yield mock_session

                mock_session_factory.return_value = session_gen()
                result = await handle_ground_command(
                    {"target_player": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
                )
                assert "result" in result
                mock_persistence.get_player_by_name.assert_any_call("OtherPlayer")


@pytest.mark.asyncio
async def test_handle_ground_command_apply_lucidity_error():
    """Test handle_ground_command() handles errors during lucidity adjustment."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.player_id = uuid.uuid4()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.player_id = uuid.uuid4()
    mock_target.current_room_id = mock_rescuer.current_room_id
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    mock_lucidity_record = MagicMock(spec=PlayerLucidity)
    mock_lucidity_record.current_tier = "catatonic"
    mock_lucidity_record.current_lcd = 0.0
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=mock_lucidity_record)
    mock_session.commit = AsyncMock()
    mock_session.rollback = AsyncMock()
    mock_lucidity_service = MagicMock()
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(side_effect=Exception("Database error"))
    with patch("server.commands.rescue_commands.get_async_session") as mock_session_factory:
        with patch("server.commands.rescue_commands.LucidityService", return_value=mock_lucidity_service):
            with patch("server.commands.rescue_commands.send_rescue_update_event", new_callable=AsyncMock):

                async def session_gen():
                    yield mock_session

                mock_session_factory.return_value = session_gen()
                result = await handle_ground_command(
                    {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
                )
                assert "result" in result
                assert "interference" in result["result"].lower() or "fails" in result["result"].lower()
                mock_session.rollback.assert_awaited_once()
