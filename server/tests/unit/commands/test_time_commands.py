"""
Unit tests for time command handlers.

Tests handlers for the time command.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.commands.time_commands import handle_time_command


@pytest.mark.asyncio
async def test_handle_time_command_success():
    """Test handle_time_command returns time information successfully."""
    mock_mythos_dt = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "January"
    mock_components.day_of_month = 1
    mock_components.year = 1928
    mock_components.week_of_month = 1
    mock_components.daypart = "Morning"
    mock_components.season = "Winter"
    
    mock_chronicle = MagicMock()
    mock_chronicle.get_current_mythos_datetime = MagicMock(return_value=mock_mythos_dt)
    mock_chronicle.get_calendar_components = MagicMock(return_value=mock_components)
    mock_chronicle.format_clock = MagicMock(return_value="08:00")
    
    mock_request = MagicMock()
    mock_request.app = None
    
    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "testplayer")
    
    assert "result" in result
    assert "MYTHOS TIME" in result["result"]
    assert "Monday" in result["result"]
    assert "January" in result["result"]
    assert "1928" in result["result"]


@pytest.mark.asyncio
async def test_handle_time_command_with_holidays():
    """Test handle_time_command includes active holidays."""
    mock_mythos_dt = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "January"
    mock_components.day_of_month = 1
    mock_components.year = 1928
    mock_components.week_of_month = 1
    mock_components.daypart = "Morning"
    mock_components.season = "Winter"
    
    mock_chronicle = MagicMock()
    mock_chronicle.get_current_mythos_datetime = MagicMock(return_value=mock_mythos_dt)
    mock_chronicle.get_calendar_components = MagicMock(return_value=mock_components)
    mock_chronicle.format_clock = MagicMock(return_value="08:00")
    
    mock_holiday_service = MagicMock()
    mock_holiday_service.refresh_active = MagicMock()
    mock_holiday_service.get_active_holiday_names = MagicMock(return_value=["New Year", "Winter Solstice"])
    
    mock_state = MagicMock()
    mock_state.holiday_service = mock_holiday_service
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "testplayer")
    
    assert "result" in result
    assert "New Year" in result["result"]
    assert "Winter Solstice" in result["result"]


@pytest.mark.asyncio
async def test_handle_time_command_no_holidays():
    """Test handle_time_command shows None when no active holidays."""
    mock_mythos_dt = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "January"
    mock_components.day_of_month = 1
    mock_components.year = 1928
    mock_components.week_of_month = 1
    mock_components.daypart = "Morning"
    mock_components.season = "Winter"
    
    mock_chronicle = MagicMock()
    mock_chronicle.get_current_mythos_datetime = MagicMock(return_value=mock_mythos_dt)
    mock_chronicle.get_calendar_components = MagicMock(return_value=mock_components)
    mock_chronicle.format_clock = MagicMock(return_value="08:00")
    
    mock_holiday_service = MagicMock()
    mock_holiday_service.refresh_active = MagicMock()
    mock_holiday_service.get_active_holiday_names = MagicMock(return_value=[])
    
    mock_state = MagicMock()
    mock_state.holiday_service = mock_holiday_service
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "testplayer")
    
    assert "result" in result
    assert "Active Holidays: None" in result["result"]


@pytest.mark.asyncio
async def test_handle_time_command_holiday_service_error():
    """Test handle_time_command handles holiday service errors gracefully."""
    mock_mythos_dt = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "January"
    mock_components.day_of_month = 1
    mock_components.year = 1928
    mock_components.week_of_month = 1
    mock_components.daypart = "Morning"
    mock_components.season = "Winter"
    
    mock_chronicle = MagicMock()
    mock_chronicle.get_current_mythos_datetime = MagicMock(return_value=mock_mythos_dt)
    mock_chronicle.get_calendar_components = MagicMock(return_value=mock_components)
    mock_chronicle.format_clock = MagicMock(return_value="08:00")
    
    mock_holiday_service = MagicMock()
    mock_holiday_service.refresh_active = MagicMock(side_effect=Exception("Test error"))
    
    mock_state = MagicMock()
    mock_state.holiday_service = mock_holiday_service
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "testplayer")
    
    # Should still return time information even if holiday service fails
    assert "result" in result
    assert "MYTHOS TIME" in result["result"]


@pytest.mark.asyncio
async def test_handle_time_command_no_holiday_service():
    """Test handle_time_command works when no holiday service."""
    mock_mythos_dt = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "January"
    mock_components.day_of_month = 1
    mock_components.year = 1928
    mock_components.week_of_month = 1
    mock_components.daypart = "Morning"
    mock_components.season = "Winter"
    
    mock_chronicle = MagicMock()
    mock_chronicle.get_current_mythos_datetime = MagicMock(return_value=mock_mythos_dt)
    mock_chronicle.get_calendar_components = MagicMock(return_value=mock_components)
    mock_chronicle.format_clock = MagicMock(return_value="08:00")
    
    mock_state = MagicMock()
    del mock_state.holiday_service  # No holiday service
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "testplayer")
    
    assert "result" in result
    assert "MYTHOS TIME" in result["result"]
    assert "Active Holidays: None" in result["result"]
