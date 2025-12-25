"""
Tests for time command handler.

This module tests the handle_time_command function.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from datetime import datetime
from typing import Any
from unittest.mock import MagicMock, Mock, patch

import pytest

from server.commands.time_commands import handle_time_command


class TestHandleTimeCommand:
    """Test handle_time_command function."""

    @pytest.mark.asyncio
    async def test_handle_time_command_success(self):
        """Test successful time command."""
        command_data: dict[str, Any] = {}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()

        mock_mythos_dt = datetime(1928, 10, 31, 14, 30, 0)
        mock_components = Mock()
        mock_components.day_name = "Wednesday"
        mock_components.month_name = "October"
        mock_components.day_of_month = 31
        mock_components.year = 1928
        mock_components.week_of_month = 5
        mock_components.daypart = "Afternoon"
        mock_components.season = "Autumn"

        mock_chronicle = Mock()
        mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
        mock_chronicle.get_calendar_components.return_value = mock_components
        mock_chronicle.format_clock.return_value = "14:30"

        mock_holiday_service = Mock()
        mock_holiday_service.get_active_holiday_names.return_value = ["Halloween"]

        mock_app = MagicMock()
        mock_app.state.holiday_service = mock_holiday_service
        mock_request.app = mock_app

        with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
            with patch("server.commands.time_commands.logger"):
                result = await handle_time_command(command_data, current_user, mock_request, None, "testuser")

                assert "result" in result
                assert "MYTHOS TIME" in result["result"]
                assert "14:30" in result["result"]
                assert "Wednesday" in result["result"]
                assert "October 31, 1928" in result["result"]
                assert "Week 5" in result["result"]
                assert "Halloween" in result["result"]
                mock_holiday_service.refresh_active.assert_called_once_with(mock_mythos_dt)

    @pytest.mark.asyncio
    async def test_handle_time_command_no_holidays(self):
        """Test time command when no holidays are active."""
        command_data: dict[str, Any] = {}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()

        mock_mythos_dt = datetime(1928, 6, 15, 12, 0, 0)
        mock_components = Mock()
        mock_components.day_name = "Friday"
        mock_components.month_name = "June"
        mock_components.day_of_month = 15
        mock_components.year = 1928
        mock_components.week_of_month = 3
        mock_components.daypart = "Noon"
        mock_components.season = "Summer"

        mock_chronicle = Mock()
        mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
        mock_chronicle.get_calendar_components.return_value = mock_components
        mock_chronicle.format_clock.return_value = "12:00"

        mock_holiday_service = Mock()
        mock_holiday_service.get_active_holiday_names.return_value = []

        mock_app = MagicMock()
        mock_app.state.holiday_service = mock_holiday_service
        mock_request.app = mock_app

        with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
            with patch("server.commands.time_commands.logger"):
                result = await handle_time_command(command_data, current_user, mock_request, None, "testuser")

                assert "Active Holidays: None" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_time_command_no_request(self):
        """Test time command when request is None."""
        command_data: dict[str, Any] = {}
        current_user = {"username": "testuser"}

        mock_mythos_dt = datetime(1928, 10, 31, 14, 30, 0)
        mock_components = Mock()
        mock_components.day_name = "Wednesday"
        mock_components.month_name = "October"
        mock_components.day_of_month = 31
        mock_components.year = 1928
        mock_components.week_of_month = 5
        mock_components.daypart = "Afternoon"
        mock_components.season = "Autumn"

        mock_chronicle = Mock()
        mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
        mock_chronicle.get_calendar_components.return_value = mock_components
        mock_chronicle.format_clock.return_value = "14:30"

        with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
            with patch("server.commands.time_commands.logger"):
                result = await handle_time_command(command_data, current_user, None, None, "testuser")

                assert "result" in result
                assert "MYTHOS TIME" in result["result"]
                assert "Active Holidays: None" in result["result"]  # No holiday service when request is None

    @pytest.mark.asyncio
    async def test_handle_time_command_no_holiday_service(self):
        """Test time command when holiday service is not available."""
        command_data: dict[str, Any] = {}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()

        mock_mythos_dt = datetime(1928, 10, 31, 14, 30, 0)
        mock_components = Mock()
        mock_components.day_name = "Wednesday"
        mock_components.month_name = "October"
        mock_components.day_of_month = 31
        mock_components.year = 1928
        mock_components.week_of_month = 5
        mock_components.daypart = "Afternoon"
        mock_components.season = "Autumn"

        mock_chronicle = Mock()
        mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
        mock_chronicle.get_calendar_components.return_value = mock_components
        mock_chronicle.format_clock.return_value = "14:30"

        mock_app = MagicMock()
        mock_app.state.holiday_service = None  # No holiday service
        mock_request.app = mock_app

        with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
            with patch("server.commands.time_commands.logger"):
                result = await handle_time_command(command_data, current_user, mock_request, None, "testuser")

                assert "result" in result
                assert "MYTHOS TIME" in result["result"]
                assert "Active Holidays: None" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_time_command_holiday_service_error(self):
        """Test time command when holiday service raises an exception."""
        command_data: dict[str, Any] = {}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()

        mock_mythos_dt = datetime(1928, 10, 31, 14, 30, 0)
        mock_components = Mock()
        mock_components.day_name = "Wednesday"
        mock_components.month_name = "October"
        mock_components.day_of_month = 31
        mock_components.year = 1928
        mock_components.week_of_month = 5
        mock_components.daypart = "Afternoon"
        mock_components.season = "Autumn"

        mock_chronicle = Mock()
        mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
        mock_chronicle.get_calendar_components.return_value = mock_components
        mock_chronicle.format_clock.return_value = "14:30"

        mock_holiday_service = Mock()
        mock_holiday_service.refresh_active.side_effect = ValueError("Holiday service error")

        mock_app = MagicMock()
        mock_app.state.holiday_service = mock_holiday_service
        mock_request.app = mock_app

        with patch("server.commands.time_commands.get_mythos_chronicle", return_value=mock_chronicle):
            with patch("server.commands.time_commands.logger"):
                result = await handle_time_command(command_data, current_user, mock_request, None, "testuser")

                assert "result" in result
                assert "MYTHOS TIME" in result["result"]
                assert "Active Holidays: None" in result["result"]  # Should default to None on error
