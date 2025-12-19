"""
Tests for connection event helpers.

This module tests event subscription helpers for connection manager.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_event_helpers import (
    subscribe_to_room_events_impl,
    unsubscribe_from_room_events_impl,
)


class TestSubscribeToRoomEventsImpl:
    """Test subscribe_to_room_events_impl function."""

    @pytest.mark.asyncio
    async def test_subscribe_to_room_events_impl_success(self) -> None:
        """Test successful subscription to room events."""
        mock_manager = MagicMock()
        mock_event_bus = MagicMock()
        mock_manager._get_event_bus.return_value = mock_event_bus
        mock_manager._handle_player_entered_room = AsyncMock()
        mock_manager._handle_player_left_room = AsyncMock()

        with patch("server.realtime.connection_event_helpers.logger") as mock_logger:
            await subscribe_to_room_events_impl(mock_manager)

            mock_event_bus.subscribe.assert_called()
            assert mock_event_bus.subscribe.call_count == 2
            mock_logger.info.assert_called_once()
            mock_logger.warning.assert_not_called()
            mock_logger.error.assert_not_called()

    @pytest.mark.asyncio
    async def test_subscribe_to_room_events_impl_no_event_bus(self) -> None:
        """Test subscription when event bus is not available."""
        mock_manager = MagicMock()
        mock_manager._get_event_bus.return_value = None

        with patch("server.realtime.connection_event_helpers.logger") as mock_logger:
            await subscribe_to_room_events_impl(mock_manager)

            mock_logger.warning.assert_called_once()
            mock_logger.info.assert_not_called()
            mock_logger.error.assert_not_called()

    @pytest.mark.asyncio
    async def test_subscribe_to_room_events_impl_database_error(self) -> None:
        """Test subscription when DatabaseError occurs."""
        from server.exceptions import DatabaseError

        mock_manager = MagicMock()
        mock_event_bus = MagicMock()
        mock_manager._get_event_bus.return_value = mock_event_bus
        mock_event_bus.subscribe.side_effect = DatabaseError("Database error")

        with patch("server.realtime.connection_event_helpers.logger") as mock_logger:
            await subscribe_to_room_events_impl(mock_manager)

            mock_logger.error.assert_called_once()
            assert "Error subscribing to room events" in str(mock_logger.error.call_args)

    @pytest.mark.asyncio
    async def test_subscribe_to_room_events_impl_attribute_error(self) -> None:
        """Test subscription when AttributeError occurs."""
        mock_manager = MagicMock()
        mock_event_bus = MagicMock()
        mock_manager._get_event_bus.return_value = mock_event_bus
        mock_event_bus.subscribe.side_effect = AttributeError("Attribute error")

        with patch("server.realtime.connection_event_helpers.logger") as mock_logger:
            await subscribe_to_room_events_impl(mock_manager)

            mock_logger.error.assert_called_once()
            assert "Error subscribing to room events" in str(mock_logger.error.call_args)

    @pytest.mark.asyncio
    async def test_subscribe_to_room_events_impl_subscribes_both_events(self) -> None:
        """Test that both PlayerEnteredRoom and PlayerLeftRoom are subscribed."""
        from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom

        mock_manager = MagicMock()
        mock_event_bus = MagicMock()
        mock_manager._get_event_bus.return_value = mock_event_bus
        mock_manager._handle_player_entered_room = AsyncMock()
        mock_manager._handle_player_left_room = AsyncMock()

        await subscribe_to_room_events_impl(mock_manager)

        # Check that subscribe was called with correct event types
        call_args_list = mock_event_bus.subscribe.call_args_list
        assert len(call_args_list) == 2

        # Check that both event types are subscribed
        event_types_subscribed = [call[0][0] for call in call_args_list]
        assert PlayerEnteredRoom in event_types_subscribed
        assert PlayerLeftRoom in event_types_subscribed

        # Check that correct handlers are subscribed
        handlers_subscribed = [call[0][1] for call in call_args_list]
        assert mock_manager._handle_player_entered_room in handlers_subscribed
        assert mock_manager._handle_player_left_room in handlers_subscribed


class TestUnsubscribeFromRoomEventsImpl:
    """Test unsubscribe_from_room_events_impl function."""

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room_events_impl_success(self) -> None:
        """Test successful unsubscription from room events."""
        mock_manager = MagicMock()
        mock_event_bus = MagicMock()
        mock_manager._get_event_bus.return_value = mock_event_bus
        mock_manager._handle_player_entered_room = AsyncMock()
        mock_manager._handle_player_left_room = AsyncMock()

        with patch("server.realtime.connection_event_helpers.logger") as mock_logger:
            await unsubscribe_from_room_events_impl(mock_manager)

            mock_event_bus.unsubscribe.assert_called()
            assert mock_event_bus.unsubscribe.call_count == 2
            mock_logger.info.assert_called_once()
            mock_logger.error.assert_not_called()

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room_events_impl_no_event_bus(self) -> None:
        """Test unsubscription when event bus is not available."""
        mock_manager = MagicMock()
        mock_manager._get_event_bus.return_value = None

        with patch("server.realtime.connection_event_helpers.logger") as mock_logger:
            await unsubscribe_from_room_events_impl(mock_manager)

            # Should return silently without logging
            mock_logger.info.assert_not_called()
            mock_logger.error.assert_not_called()

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room_events_impl_database_error(self) -> None:
        """Test unsubscription when DatabaseError occurs."""
        from server.exceptions import DatabaseError

        mock_manager = MagicMock()
        mock_event_bus = MagicMock()
        mock_manager._get_event_bus.return_value = mock_event_bus
        mock_event_bus.unsubscribe.side_effect = DatabaseError("Database error")

        with patch("server.realtime.connection_event_helpers.logger") as mock_logger:
            await unsubscribe_from_room_events_impl(mock_manager)

            mock_logger.error.assert_called_once()
            assert "Error unsubscribing from room events" in str(mock_logger.error.call_args)

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room_events_impl_attribute_error(self) -> None:
        """Test unsubscription when AttributeError occurs."""
        mock_manager = MagicMock()
        mock_event_bus = MagicMock()
        mock_manager._get_event_bus.return_value = mock_event_bus
        mock_event_bus.unsubscribe.side_effect = AttributeError("Attribute error")

        with patch("server.realtime.connection_event_helpers.logger") as mock_logger:
            await unsubscribe_from_room_events_impl(mock_manager)

            mock_logger.error.assert_called_once()
            assert "Error unsubscribing from room events" in str(mock_logger.error.call_args)

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room_events_impl_unsubscribes_both_events(self) -> None:
        """Test that both PlayerEnteredRoom and PlayerLeftRoom are unsubscribed."""
        from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom

        mock_manager = MagicMock()
        mock_event_bus = MagicMock()
        mock_manager._get_event_bus.return_value = mock_event_bus
        mock_manager._handle_player_entered_room = AsyncMock()
        mock_manager._handle_player_left_room = AsyncMock()

        await unsubscribe_from_room_events_impl(mock_manager)

        # Check that unsubscribe was called with correct event types
        call_args_list = mock_event_bus.unsubscribe.call_args_list
        assert len(call_args_list) == 2

        # Check that both event types are unsubscribed
        event_types_unsubscribed = [call[0][0] for call in call_args_list]
        assert PlayerEnteredRoom in event_types_unsubscribed
        assert PlayerLeftRoom in event_types_unsubscribed

        # Check that correct handlers are unsubscribed
        handlers_unsubscribed = [call[0][1] for call in call_args_list]
        assert mock_manager._handle_player_entered_room in handlers_unsubscribed
        assert mock_manager._handle_player_left_room in handlers_unsubscribed
