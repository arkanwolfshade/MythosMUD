"""
Unit tests for connection event helpers.

Tests the connection_event_helpers module functions.
"""

from unittest.mock import MagicMock

import pytest

from server.realtime.connection_event_helpers import (
    subscribe_to_room_events_impl,
    unsubscribe_from_room_events_impl,
)


@pytest.mark.asyncio
async def test_subscribe_to_room_events_impl_success():
    """Test subscribe_to_room_events_impl() successfully subscribes to events."""
    mock_manager = MagicMock()
    mock_event_bus = MagicMock()
    mock_manager._get_event_bus.return_value = mock_event_bus

    await subscribe_to_room_events_impl(mock_manager)

    assert mock_event_bus.subscribe.call_count == 2
    mock_manager._get_event_bus.assert_called_once()


@pytest.mark.asyncio
async def test_subscribe_to_room_events_impl_no_event_bus():
    """Test subscribe_to_room_events_impl() handles missing event bus."""
    mock_manager = MagicMock()
    mock_manager._get_event_bus.return_value = None

    await subscribe_to_room_events_impl(mock_manager)

    mock_manager._get_event_bus.assert_called_once()


@pytest.mark.asyncio
async def test_subscribe_to_room_events_impl_database_error():
    """Test subscribe_to_room_events_impl() handles DatabaseError."""
    from server.exceptions import DatabaseError

    mock_manager = MagicMock()
    mock_event_bus = MagicMock()
    mock_event_bus.subscribe.side_effect = DatabaseError("Database error")
    mock_manager._get_event_bus.return_value = mock_event_bus

    await subscribe_to_room_events_impl(mock_manager)

    mock_manager._get_event_bus.assert_called_once()


@pytest.mark.asyncio
async def test_subscribe_to_room_events_impl_attribute_error():
    """Test subscribe_to_room_events_impl() handles AttributeError."""
    mock_manager = MagicMock()
    mock_event_bus = MagicMock()
    mock_event_bus.subscribe.side_effect = AttributeError("No subscribe method")
    mock_manager._get_event_bus.return_value = mock_event_bus

    await subscribe_to_room_events_impl(mock_manager)

    mock_manager._get_event_bus.assert_called_once()


@pytest.mark.asyncio
async def test_unsubscribe_from_room_events_impl_success():
    """Test unsubscribe_from_room_events_impl() successfully unsubscribes from events."""
    mock_manager = MagicMock()
    mock_event_bus = MagicMock()
    mock_manager._get_event_bus.return_value = mock_event_bus

    await unsubscribe_from_room_events_impl(mock_manager)

    assert mock_event_bus.unsubscribe.call_count == 2
    mock_manager._get_event_bus.assert_called_once()


@pytest.mark.asyncio
async def test_unsubscribe_from_room_events_impl_no_event_bus():
    """Test unsubscribe_from_room_events_impl() handles missing event bus."""
    mock_manager = MagicMock()
    mock_manager._get_event_bus.return_value = None

    await unsubscribe_from_room_events_impl(mock_manager)

    mock_manager._get_event_bus.assert_called_once()


@pytest.mark.asyncio
async def test_unsubscribe_from_room_events_impl_database_error():
    """Test unsubscribe_from_room_events_impl() handles DatabaseError."""
    from server.exceptions import DatabaseError

    mock_manager = MagicMock()
    mock_event_bus = MagicMock()
    mock_event_bus.unsubscribe.side_effect = DatabaseError("Database error")
    mock_manager._get_event_bus.return_value = mock_event_bus

    await unsubscribe_from_room_events_impl(mock_manager)

    mock_manager._get_event_bus.assert_called_once()


@pytest.mark.asyncio
async def test_unsubscribe_from_room_events_impl_attribute_error():
    """Test unsubscribe_from_room_events_impl() handles AttributeError."""
    mock_manager = MagicMock()
    mock_event_bus = MagicMock()
    mock_event_bus.unsubscribe.side_effect = AttributeError("No unsubscribe method")
    mock_manager._get_event_bus.return_value = mock_event_bus

    await unsubscribe_from_room_events_impl(mock_manager)

    mock_manager._get_event_bus.assert_called_once()
