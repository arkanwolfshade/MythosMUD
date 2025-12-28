"""
Unit tests for time command handlers.

Tests the time command functionality.
"""

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest

from server.commands.time_commands import handle_time_command


@pytest.mark.asyncio
async def test_handle_time_command_success():
    """Test handle_time_command() returns time information."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_chronicle = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "October"
    mock_components.day_of_month = 31
    mock_components.year = 1926
    mock_components.week_of_month = 5
    mock_components.daypart = "afternoon"
    mock_components.season = "autumn"
    mock_mythos_dt = datetime(1926, 10, 31, 14, 30, 0, tzinfo=UTC)
    mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
    mock_chronicle.get_calendar_components.return_value = mock_components
    mock_chronicle.format_clock.return_value = "14:30:00"
    mock_state.holiday_service = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "MYTHOS TIME" in result["result"]
    assert "1926" in result["result"]


@pytest.mark.asyncio
async def test_handle_time_command_with_holidays():
    """Test handle_time_command() includes active holidays."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_chronicle = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "October"
    mock_components.day_of_month = 31
    mock_components.year = 1926
    mock_components.week_of_month = 5
    mock_components.daypart = "afternoon"
    mock_components.season = "autumn"
    mock_mythos_dt = datetime(1926, 10, 31, 14, 30, 0, tzinfo=UTC)
    mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
    mock_chronicle.get_calendar_components.return_value = mock_components
    mock_chronicle.format_clock.return_value = "14:30:00"
    mock_holiday_service = MagicMock()
    mock_holiday_service.get_active_holiday_names.return_value = ["Halloween"]
    mock_state.holiday_service = mock_holiday_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "TestPlayer")

    assert "Halloween" in result["result"]


@pytest.mark.asyncio
async def test_handle_time_command_no_holidays():
    """Test handle_time_command() handles no active holidays."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_chronicle = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "October"
    mock_components.day_of_month = 31
    mock_components.year = 1926
    mock_components.week_of_month = 5
    mock_components.daypart = "afternoon"
    mock_components.season = "autumn"
    mock_mythos_dt = datetime(1926, 10, 31, 14, 30, 0, tzinfo=UTC)
    mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
    mock_chronicle.get_calendar_components.return_value = mock_components
    mock_chronicle.format_clock.return_value = "14:30:00"
    mock_holiday_service = MagicMock()
    mock_holiday_service.get_active_holiday_names.return_value = []
    mock_state.holiday_service = mock_holiday_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "TestPlayer")

    assert "Active Holidays: None" in result["result"]


@pytest.mark.asyncio
async def test_handle_time_command_holiday_service_error():
    """Test handle_time_command() handles holiday service errors."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_chronicle = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "October"
    mock_components.day_of_month = 31
    mock_components.year = 1926
    mock_components.week_of_month = 5
    mock_components.daypart = "afternoon"
    mock_components.season = "autumn"
    mock_mythos_dt = datetime(1926, 10, 31, 14, 30, 0, tzinfo=UTC)
    mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
    mock_chronicle.get_calendar_components.return_value = mock_components
    mock_chronicle.format_clock.return_value = "14:30:00"
    mock_holiday_service = MagicMock()
    mock_holiday_service.refresh_active.side_effect = Exception("Test error")
    mock_state.holiday_service = mock_holiday_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "TestPlayer")

    # Should still return time info even if holiday service fails
    assert "MYTHOS TIME" in result["result"]


@pytest.mark.asyncio
async def test_handle_time_command_no_holiday_service():
    """Test handle_time_command() handles missing holiday service."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_chronicle = MagicMock()
    mock_components = MagicMock()
    mock_components.day_name = "Monday"
    mock_components.month_name = "October"
    mock_components.day_of_month = 31
    mock_components.year = 1926
    mock_components.week_of_month = 5
    mock_components.daypart = "afternoon"
    mock_components.season = "autumn"
    mock_mythos_dt = datetime(1926, 10, 31, 14, 30, 0, tzinfo=UTC)
    mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
    mock_chronicle.get_calendar_components.return_value = mock_components
    mock_chronicle.format_clock.return_value = "14:30:00"
    mock_state.holiday_service = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_time_command({}, {}, mock_request, None, "TestPlayer")

    assert "MYTHOS TIME" in result["result"]
    assert "Active Holidays: None" in result["result"]
