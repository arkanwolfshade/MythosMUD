"""
Unit tests for lucidity event dispatcher.

Tests the lucidity event broadcasting functions.
"""

import uuid
from unittest.mock import AsyncMock, patch

import pytest

from server.services.lucidity_event_dispatcher import (
    send_catatonia_event,
    send_lucidity_change_event,
    send_rescue_update_event,
)


@pytest.fixture
def mock_send_game_event():
    """Create a mock send_game_event function."""
    return AsyncMock()


def test_format_liabilities_empty():
    """Test _format_liabilities with empty input."""
    from server.services.lucidity_event_dispatcher import _format_liabilities

    result = _format_liabilities(None)
    assert result == []

    result = _format_liabilities([])
    assert result == []


def test_format_liabilities_single():
    """Test _format_liabilities with single liability."""
    from server.services.lucidity_event_dispatcher import _format_liabilities

    liabilities = [{"code": "nightmare", "stacks": 1}]
    result = _format_liabilities(liabilities)
    assert result == ["nightmare"]


def test_format_liabilities_multiple_stacks():
    """Test _format_liabilities with multiple stacks."""
    from server.services.lucidity_event_dispatcher import _format_liabilities

    liabilities = [{"code": "nightmare", "stacks": 3}]
    result = _format_liabilities(liabilities)
    assert result == ["nightmare (x3)"]


def test_format_liabilities_multiple_entries():
    """Test _format_liabilities with multiple entries."""
    from server.services.lucidity_event_dispatcher import _format_liabilities

    liabilities = [
        {"code": "nightmare", "stacks": 2},
        {"code": "hallucination", "stacks": 1},
        {"code": "paranoia", "stacks": 5},
    ]
    result = _format_liabilities(liabilities)
    assert len(result) == 3
    assert "nightmare (x2)" in result
    assert "hallucination" in result
    assert "paranoia (x5)" in result


def test_format_liabilities_invalid_stacks():
    """Test _format_liabilities with invalid stack values."""
    from server.services.lucidity_event_dispatcher import _format_liabilities

    liabilities = [
        {"code": "nightmare", "stacks": "invalid"},
        {"code": "hallucination"},  # Missing stacks key
    ]
    result = _format_liabilities(liabilities)
    assert len(result) == 2
    assert "nightmare" in result  # Defaults to 1 stack
    assert "hallucination" in result


def test_format_liabilities_empty_code():
    """Test _format_liabilities skips entries with empty code."""
    from server.services.lucidity_event_dispatcher import _format_liabilities

    liabilities = [
        {"code": "", "stacks": 1},
        {"code": "  ", "stacks": 1},  # Whitespace only
        {"code": "nightmare", "stacks": 1},
    ]
    result = _format_liabilities(liabilities)
    assert result == ["nightmare"]


@pytest.mark.asyncio
async def test_send_lucidity_change_event_basic(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_lucidity_change_event with basic parameters."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_lucidity_change_event(player_id, current_lcd=50, delta=-5, tier="stable")
        mock_send_game_event.assert_awaited_once()
        call_args = mock_send_game_event.call_args
        assert call_args[0][0] == str(player_id)
        assert call_args[0][1] == "lucidity_change"
        payload = call_args[0][2]
        assert payload["current_lcd"] == 50
        assert payload["delta"] == -5
        assert payload["tier"] == "stable"
        assert payload["max_lcd"] == 100  # Default


@pytest.mark.asyncio
async def test_send_lucidity_change_event_with_max_lcd(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_lucidity_change_event with custom max_lcd."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_lucidity_change_event(player_id, current_lcd=75, delta=10, tier="stable", max_lcd=150)
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert payload["max_lcd"] == 150


@pytest.mark.asyncio
async def test_send_lucidity_change_event_with_liabilities(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_lucidity_change_event with liabilities."""
    player_id = uuid.uuid4()
    liabilities = [{"code": "nightmare", "stacks": 2}, {"code": "hallucination", "stacks": 1}]
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_lucidity_change_event(player_id, current_lcd=30, delta=-10, tier="unstable", liabilities=liabilities)
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert "liabilities" in payload
        assert "nightmare (x2)" in payload["liabilities"]
        assert "hallucination" in payload["liabilities"]


@pytest.mark.asyncio
async def test_send_lucidity_change_event_with_reason_and_source(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_lucidity_change_event with reason and source."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_lucidity_change_event(
            player_id,
            current_lcd=40,
            delta=-5,
            tier="unstable",
            reason="combat_damage",
            source="spell_cast",
        )
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert payload["reason"] == "combat_damage"
        assert payload["source"] == "spell_cast"


@pytest.mark.asyncio
async def test_send_lucidity_change_event_with_metadata(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_lucidity_change_event with metadata."""
    player_id = uuid.uuid4()
    metadata = {"spell_id": "spell_001", "caster": "TestPlayer"}
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_lucidity_change_event(player_id, current_lcd=35, delta=-8, tier="unstable", metadata=metadata)
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert payload["metadata"] == metadata


@pytest.mark.asyncio
async def test_send_lucidity_change_event_string_player_id(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_lucidity_change_event with string player_id."""
    player_id_str = str(uuid.uuid4())
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_lucidity_change_event(player_id_str, current_lcd=50, delta=5, tier="stable")
        call_args = mock_send_game_event.call_args
        assert call_args[0][0] == player_id_str


@pytest.mark.asyncio
async def test_send_lucidity_change_event_dispatch_error(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_lucidity_change_event handles dispatch errors gracefully."""
    player_id = uuid.uuid4()
    mock_send_game_event.side_effect = ConnectionError("Connection error")
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        # Should not raise an exception
        await send_lucidity_change_event(player_id, current_lcd=50, delta=-5, tier="stable")
        mock_send_game_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_catatonia_event_basic(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_catatonia_event with basic parameters."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_catatonia_event(player_id, status="catatonic")
        mock_send_game_event.assert_awaited_once()
        call_args = mock_send_game_event.call_args
        assert call_args[0][0] == str(player_id)
        assert call_args[0][1] == "catatonia"
        payload = call_args[0][2]
        assert payload["status"] == "catatonic"


@pytest.mark.asyncio
async def test_send_catatonia_event_with_current_lcd(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_catatonia_event with current_lcd."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_catatonia_event(player_id, status="catatonic", current_lcd=0)
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert payload["current_lcd"] == 0


@pytest.mark.asyncio
async def test_send_catatonia_event_with_message(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_catatonia_event with message."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_catatonia_event(player_id, status="catatonic", message="Your mind shatters")
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert payload["message"] == "Your mind shatters"


@pytest.mark.asyncio
async def test_send_catatonia_event_with_rescuer_and_target(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_catatonia_event with rescuer and target names."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_catatonia_event(player_id, status="channeling", rescuer_name="Rescuer", target_name="Target")
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert payload["rescuer_name"] == "Rescuer"
        assert payload["target_name"] == "Target"


@pytest.mark.asyncio
async def test_send_catatonia_event_dispatch_error(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_catatonia_event handles dispatch errors gracefully."""
    player_id = uuid.uuid4()
    mock_send_game_event.side_effect = ConnectionError("Connection error")
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        # Should not raise an exception
        await send_catatonia_event(player_id, status="catatonic")
        mock_send_game_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_rescue_update_event_basic(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_rescue_update_event with basic parameters."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_rescue_update_event(player_id, status="channeling")
        mock_send_game_event.assert_awaited_once()
        call_args = mock_send_game_event.call_args
        assert call_args[0][0] == str(player_id)
        assert call_args[0][1] == "rescue_update"
        payload = call_args[0][2]
        assert payload["status"] == "channeling"


@pytest.mark.asyncio
async def test_send_rescue_update_event_with_all_fields(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_rescue_update_event with all optional fields."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_rescue_update_event(
            player_id,
            status="channeling",
            current_lcd=1,
            message="Rescue in progress",
            rescuer_name="Rescuer",
            target_name="Target",
            progress=50.0,
            eta_seconds=30.0,
        )
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert payload["status"] == "channeling"
        assert payload["current_lcd"] == 1
        assert payload["message"] == "Rescue in progress"
        assert payload["rescuer_name"] == "Rescuer"
        assert payload["target_name"] == "Target"
        assert payload["progress"] == 50.0
        assert payload["eta_seconds"] == 30.0


@pytest.mark.asyncio
async def test_send_rescue_update_event_with_progress_only(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_rescue_update_event with progress only."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        await send_rescue_update_event(player_id, status="channeling", progress=25.0)
        call_args = mock_send_game_event.call_args
        payload = call_args[0][2]
        assert payload["progress"] == 25.0
        assert "current_lcd" not in payload
        assert "message" not in payload


@pytest.mark.asyncio
async def test_send_rescue_update_event_dispatch_error(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test send_rescue_update_event handles dispatch errors gracefully."""
    player_id = uuid.uuid4()
    mock_send_game_event.side_effect = ConnectionError("Connection error")
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        # Should not raise an exception
        await send_rescue_update_event(player_id, status="channeling")
        mock_send_game_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_dispatch_player_event_import_error():  # pylint: disable=redefined-outer-name  # Reason: Function has no fixture parameters, but suppression applied at module level for consistency with other test functions
    """Test _dispatch_player_event handles import errors gracefully."""
    player_id = uuid.uuid4()
    # The function imports send_game_event inside, so we need to patch the import
    # Use a context manager that makes the import fail
    original_import = __import__

    def failing_import(name, *args, **kwargs):
        if name == "server.realtime.connection_manager_api":
            raise ImportError("Module not found")
        return original_import(name, *args, **kwargs)

    with patch("builtins.__import__", side_effect=failing_import):
        from server.services.lucidity_event_dispatcher import _dispatch_player_event

        # Should not raise an exception, should handle gracefully
        await _dispatch_player_event(player_id, "test_event", {"test": "data"})


@pytest.mark.asyncio
async def test_dispatch_player_event_uuid_conversion(mock_send_game_event):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _dispatch_player_event converts UUID to string."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_manager_api.send_game_event", mock_send_game_event):
        from server.services.lucidity_event_dispatcher import _dispatch_player_event

        await _dispatch_player_event(player_id, "test_event", {"test": "data"})
        call_args = mock_send_game_event.call_args
        assert call_args[0][0] == str(player_id)
        assert isinstance(call_args[0][0], str)
