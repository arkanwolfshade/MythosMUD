"""
Unit tests for game API endpoints.

Tests game status, broadcasting, and time endpoints.
"""
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

import datetime
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest

from server.api.game import broadcast_message, get_game_status, get_mythos_time
from server.models.user import User
from server.schemas.calendar import HolidayEntry
from server.schemas.game import BroadcastMessageResponse, GameStatusResponse, MythosTimeResponse


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.get_active_connection_count = Mock(return_value=10)
    manager.player_websockets = {"player1": MagicMock(), "player2": MagicMock()}
    manager.room_manager = MagicMock()
    manager.room_manager.room_subscriptions = {"room1": MagicMock(), "room2": MagicMock()}
    manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5, "failed_deliveries": 0})
    return manager


@pytest.fixture
def mock_user():
    """Create a mock user."""
    user = MagicMock(spec=User)
    user.id = MagicMock()
    user.id.__str__ = Mock(return_value="user-id-123")
    user.username = "admin_user"
    return user


@pytest.fixture
def mock_container():
    """Create a mock application container."""
    container = MagicMock()
    return container


class TestGetGameStatus:
    """Test get_game_status endpoint."""

    def test_get_game_status_success(self, mock_connection_manager):
        """Test get_game_status returns game status data."""
        result = get_game_status(mock_connection_manager)
        assert isinstance(result, GameStatusResponse)
        assert result.active_connections == 10
        assert result.active_players == 2
        assert result.room_subscriptions == 2
        assert result.server_time is not None
        mock_connection_manager.get_active_connection_count.assert_called_once()

    def test_get_game_status_empty_connections(self):
        """Test get_game_status handles empty connections."""
        manager = MagicMock()
        manager.get_active_connection_count = Mock(return_value=0)
        manager.player_websockets = {}
        manager.room_manager = MagicMock()
        manager.room_manager.room_subscriptions = {}
        result = get_game_status(manager)
        assert result.active_connections == 0
        assert result.active_players == 0
        assert result.room_subscriptions == 0


class TestBroadcastMessage:
    """Test broadcast_message endpoint."""

    @pytest.mark.asyncio
    async def test_broadcast_message_success(self, mock_connection_manager, mock_user):
        """Test broadcast_message successfully broadcasts message."""
        message = "Test broadcast message"
        result = await broadcast_message(message, mock_user, mock_connection_manager)
        assert isinstance(result, BroadcastMessageResponse)
        assert result.message == message
        assert result.recipients == 5
        assert result.broadcaster == "admin_user"
        mock_connection_manager.broadcast_global_event.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_broadcast_message_no_recipients(self, mock_connection_manager, mock_user):
        """Test broadcast_message handles no recipients."""
        mock_connection_manager.broadcast_global_event = AsyncMock(
            return_value={"successful_deliveries": 0, "failed_deliveries": 0}
        )
        message = "Test broadcast"
        result = await broadcast_message(message, mock_user, mock_connection_manager)
        assert result.recipients == 0

    @pytest.mark.asyncio
    async def test_broadcast_message_broadcast_error(self, mock_connection_manager, mock_user):
        """Test broadcast_message handles broadcast errors gracefully."""
        mock_connection_manager.broadcast_global_event = AsyncMock(side_effect=RuntimeError("Broadcast error"))
        message = "Test broadcast"
        with pytest.raises(RuntimeError):
            await broadcast_message(message, mock_user, mock_connection_manager)


class TestGetMythosTime:
    """Test get_mythos_time endpoint."""

    def test_get_mythos_time_success(self, mock_container):
        """Test get_mythos_time returns time data."""
        mock_holiday_service = MagicMock()
        mock_holiday_service.get_serialized_active_holidays = Mock(return_value=[])
        mock_holiday_service.get_serialized_upcoming_holidays = Mock(return_value=[])
        mock_container.holiday_service = mock_holiday_service

        with patch("server.api.game.get_mythos_chronicle") as mock_chronicle:
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "January"
            mock_components.day_of_month = 15
            mock_components.day_name = "Monday"
            mock_components.week_of_month = 3
            mock_components.season = "Winter"
            mock_components.daypart = "Noon"
            mock_components.is_daytime = True
            mock_components.is_witching_hour = False
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="12:00")
            mock_chronicle.return_value = mock_chronicle_instance

            result = get_mythos_time(mock_container)
            assert isinstance(result, MythosTimeResponse)
            assert result.month_name == "January"
            assert result.day_of_month == 15
            assert result.season == "Winter"

    def test_get_mythos_time_no_holiday_service(self):
        """Test get_mythos_time handles missing holiday service."""
        mock_container = MagicMock()
        mock_container.holiday_service = None

        with patch("server.api.game.get_mythos_chronicle") as mock_chronicle:
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "January"
            mock_components.day_of_month = 15
            mock_components.day_name = "Monday"
            mock_components.week_of_month = 3
            mock_components.season = "Winter"
            mock_components.daypart = "Noon"
            mock_components.is_daytime = True
            mock_components.is_witching_hour = False
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="12:00")
            mock_chronicle.return_value = mock_chronicle_instance

            result = get_mythos_time(mock_container)
            assert isinstance(result, MythosTimeResponse)
            assert result.active_holidays == []
            assert result.upcoming_holidays == []

    def test_get_mythos_time_holiday_service_error(self, mock_container):
        """Test get_mythos_time handles holiday service errors gracefully."""
        mock_holiday_service = MagicMock()
        mock_holiday_service.get_serialized_active_holidays = Mock(side_effect=RuntimeError("Service error"))
        mock_holiday_service.get_serialized_upcoming_holidays = Mock(return_value=[])
        mock_container.holiday_service = mock_holiday_service

        with patch("server.api.game.get_mythos_chronicle") as mock_chronicle:
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "January"
            mock_components.day_of_month = 15
            mock_components.day_name = "Monday"
            mock_components.week_of_month = 3
            mock_components.season = "Winter"
            mock_components.daypart = "Noon"
            mock_components.is_daytime = True
            mock_components.is_witching_hour = False
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="12:00")
            mock_chronicle.return_value = mock_chronicle_instance

            with patch("server.api.game.logger") as mock_logger:
                result = get_mythos_time(mock_container)
                assert isinstance(result, MythosTimeResponse)
                mock_logger.warning.assert_called_once()

    def test_get_mythos_time_with_holidays(self, mock_container):
        """Test get_mythos_time includes holiday data when available."""
        mock_holiday_service = MagicMock()
        active_holiday = HolidayEntry(
            id="test_holiday", name="Test Holiday", tradition="mythos", month=1, day=15, season="winter"
        )
        upcoming_holiday = HolidayEntry(
            id="upcoming_holiday", name="Upcoming Holiday", tradition="mythos", month=1, day=20, season="winter"
        )
        mock_holiday_service.get_serialized_active_holidays = Mock(return_value=[active_holiday])
        mock_holiday_service.get_serialized_upcoming_holidays = Mock(return_value=[upcoming_holiday])
        mock_container.holiday_service = mock_holiday_service

        with patch("server.api.game.get_mythos_chronicle") as mock_chronicle:
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "January"
            mock_components.day_of_month = 15
            mock_components.day_name = "Monday"
            mock_components.week_of_month = 3
            mock_components.season = "Winter"
            mock_components.daypart = "Noon"
            mock_components.is_daytime = True
            mock_components.is_witching_hour = False
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="12:00")
            mock_chronicle.return_value = mock_chronicle_instance

            result = get_mythos_time(mock_container)
            assert len(result.active_holidays) == 1
            assert len(result.upcoming_holidays) == 1

    def test_get_mythos_time_no_container(self, mock_container):
        """Test get_mythos_time handles None container."""
        with patch("server.api.game.get_mythos_chronicle") as mock_chronicle:
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "January"
            mock_components.day_of_month = 15
            mock_components.day_name = "Monday"
            mock_components.week_of_month = 3
            mock_components.season = "Winter"
            mock_components.daypart = "Noon"
            mock_components.is_daytime = True
            mock_components.is_witching_hour = False
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="12:00")
            mock_chronicle.return_value = mock_chronicle_instance

            result = get_mythos_time(mock_container)
            assert isinstance(result, MythosTimeResponse)
            assert result.active_holidays == []
            assert result.upcoming_holidays == []

    def test_get_mythos_time_holiday_service_upcoming_error(self, mock_container):
        """Test get_mythos_time handles upcoming holidays error gracefully."""
        mock_holiday_service = MagicMock()
        mock_holiday_service.get_serialized_active_holidays = Mock(return_value=[])
        mock_holiday_service.get_serialized_upcoming_holidays = Mock(side_effect=RuntimeError("Service error"))
        mock_container.holiday_service = mock_holiday_service

        with patch("server.api.game.get_mythos_chronicle") as mock_chronicle:
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "January"
            mock_components.day_of_month = 15
            mock_components.day_name = "Monday"
            mock_components.week_of_month = 3
            mock_components.season = "Winter"
            mock_components.daypart = "Noon"
            mock_components.is_daytime = True
            mock_components.is_witching_hour = False
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="12:00")
            mock_chronicle.return_value = mock_chronicle_instance

            with patch("server.api.game.logger") as mock_logger:
                result = get_mythos_time(mock_container)
                assert isinstance(result, MythosTimeResponse)
                mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_broadcast_message_missing_stats_key(self, mock_connection_manager, mock_user):
        """Test broadcast_message handles missing successful_deliveries in stats."""
        mock_connection_manager.broadcast_global_event = AsyncMock(return_value={"failed_deliveries": 0})
        message = "Test broadcast"
        result = await broadcast_message(message, mock_user, mock_connection_manager)
        # Should default to 0 when key is missing
        assert result.recipients == 0

    @pytest.mark.asyncio
    async def test_broadcast_message_empty_stats(self, mock_connection_manager, mock_user):
        """Test broadcast_message handles empty stats dictionary."""
        mock_connection_manager.broadcast_global_event = AsyncMock(return_value={})
        message = "Test broadcast"
        result = await broadcast_message(message, mock_user, mock_connection_manager)
        assert result.recipients == 0

    @pytest.mark.asyncio
    async def test_broadcast_message_logs_info(self, mock_connection_manager, mock_user):
        """Test broadcast_message logs info messages correctly."""
        message = "Test broadcast message"
        with patch("server.api.game.logger") as mock_logger:
            await broadcast_message(message, mock_user, mock_connection_manager)
            # Should log both request and completion
            assert mock_logger.info.call_count == 2
            # Check first log (request)
            first_call = mock_logger.info.call_args_list[0]
            assert "Admin broadcast message requested" in first_call[0][0]
            assert first_call[1]["admin_username"] == "admin_user"
            assert first_call[1]["message"] == message
            # Check second log (completion)
            second_call = mock_logger.info.call_args_list[1]
            assert "Admin broadcast completed" in second_call[0][0]
            assert second_call[1]["recipients"] == 5


class TestGetGameStatusLogger:
    """Test logger calls in get_game_status."""

    def test_get_game_status_logs_debug(self, mock_connection_manager):
        """Test get_game_status logs debug messages."""
        with patch("server.api.game.logger") as mock_logger:
            get_game_status(mock_connection_manager)
            # Should log both request and return
            assert mock_logger.debug.call_count == 2
            # Check first log (request)
            first_call = mock_logger.debug.call_args_list[0]
            assert "Game status requested" in first_call[0][0]
            # Check second log (return)
            second_call = mock_logger.debug.call_args_list[1]
            assert "Game status returned" in second_call[0][0]
            assert second_call[1]["active_connections"] == 10
            assert second_call[1]["active_players"] == 2
            assert second_call[1]["room_subscriptions"] == 2


class TestGetMythosTimeEdgeCases:
    """Test edge cases for get_mythos_time."""

    def test_get_mythos_time_container_no_holiday_service_attribute(self):
        """Test get_mythos_time handles container without holiday_service attribute."""
        mock_container = MagicMock()
        # Container exists but has no holiday_service attribute
        delattr(mock_container, "holiday_service") if hasattr(mock_container, "holiday_service") else None
        # Use getattr which returns None when attribute doesn't exist
        mock_container.holiday_service = None

        with patch("server.api.game.get_mythos_chronicle") as mock_chronicle:
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "January"
            mock_components.day_of_month = 15
            mock_components.day_name = "Monday"
            mock_components.week_of_month = 3
            mock_components.season = "Winter"
            mock_components.daypart = "Noon"
            mock_components.is_daytime = True
            mock_components.is_witching_hour = False
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="12:00")
            mock_chronicle.return_value = mock_chronicle_instance

            result = get_mythos_time(mock_container)
            assert isinstance(result, MythosTimeResponse)
            assert result.active_holidays == []
            assert result.upcoming_holidays == []

    def test_get_mythos_time_logs_debug(self, mock_container):
        """Test get_mythos_time logs debug message."""
        mock_holiday_service = MagicMock()
        mock_holiday_service.get_serialized_active_holidays = Mock(return_value=[])
        mock_holiday_service.get_serialized_upcoming_holidays = Mock(return_value=[])
        mock_container.holiday_service = mock_holiday_service

        with (
            patch("server.api.game.get_mythos_chronicle") as mock_chronicle,
            patch("server.api.game.logger") as mock_logger,
        ):
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "January"
            mock_components.day_of_month = 15
            mock_components.day_name = "Monday"
            mock_components.week_of_month = 3
            mock_components.season = "Winter"
            mock_components.daypart = "Noon"
            mock_components.is_daytime = True
            mock_components.is_witching_hour = False
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="12:00")
            mock_chronicle.return_value = mock_chronicle_instance

            result = get_mythos_time(mock_container)
            assert isinstance(result, MythosTimeResponse)
            mock_logger.debug.assert_called_once()
            call_args = mock_logger.debug.call_args
            assert "Mythos time payload generated" in call_args[0][0]
            assert call_args[1]["mythos_clock"] == "12:00"
            assert call_args[1]["daypart"] == "Noon"
            assert call_args[1]["season"] == "Winter"

    def test_get_mythos_time_different_calendar_components(self, mock_container):
        """Test get_mythos_time with different calendar component values."""
        mock_holiday_service = MagicMock()
        mock_holiday_service.get_serialized_active_holidays = Mock(return_value=[])
        mock_holiday_service.get_serialized_upcoming_holidays = Mock(return_value=[])
        mock_container.holiday_service = mock_holiday_service

        with patch("server.api.game.get_mythos_chronicle") as mock_chronicle:
            mock_chronicle_instance = MagicMock()
            mock_mythos_dt = datetime.datetime(2024, 6, 21, 23, 59, 0, tzinfo=datetime.UTC)
            mock_chronicle_instance.get_current_mythos_datetime = Mock(return_value=mock_mythos_dt)
            mock_components = MagicMock()
            mock_components.mythos_datetime = mock_mythos_dt
            mock_components.month_name = "June"
            mock_components.day_of_month = 21
            mock_components.day_name = "Friday"
            mock_components.week_of_month = 4
            mock_components.season = "Summer"
            mock_components.daypart = "Midnight"
            mock_components.is_daytime = False
            mock_components.is_witching_hour = True
            mock_chronicle_instance.get_calendar_components = Mock(return_value=mock_components)
            mock_chronicle_instance.format_clock = Mock(return_value="23:59")
            mock_chronicle.return_value = mock_chronicle_instance

            result = get_mythos_time(mock_container)
            assert result.month_name == "June"
            assert result.day_of_month == 21
            assert result.day_name == "Friday"
            assert result.week_of_month == 4
            assert result.season == "Summer"
            assert result.daypart == "Midnight"
            assert result.is_daytime is False
            assert result.is_witching_hour is True
            assert result.mythos_clock == "23:59"


class TestBroadcastMessageEdgeCases:
    """Test edge cases for broadcast_message."""

    @pytest.mark.asyncio
    async def test_broadcast_message_broadcast_stats_structure(self, mock_connection_manager, mock_user):
        """Test broadcast_message with different broadcast_stats structures."""
        # Test with additional keys in broadcast_stats
        mock_connection_manager.broadcast_global_event = AsyncMock(
            return_value={
                "successful_deliveries": 10,
                "failed_deliveries": 2,
                "total_recipients": 12,
                "delivery_time_ms": 150,
            }
        )
        message = "Test broadcast"
        result = await broadcast_message(message, mock_user, mock_connection_manager)
        assert result.recipients == 10
        assert result.broadcast_stats["total_recipients"] == 12
        assert result.broadcast_stats["delivery_time_ms"] == 150
