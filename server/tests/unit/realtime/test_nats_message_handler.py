"""
Unit tests for NATS message handler.

Tests the NATSMessageHandler class.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.circuit_breaker import CircuitBreakerOpen
from server.realtime.nats_message_handler import NATSMessageHandler
from server.realtime.nats_retry_handler import NATSRetryHandler
from server.services.nats_exceptions import NATSError, NATSSubscribeError


@pytest.fixture
def mock_nats_service():
    """Create a mock NATS service."""
    return MagicMock()


@pytest.fixture
def mock_subject_manager():
    """Create a mock subject manager."""
    return MagicMock()


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    return MagicMock()


@pytest.fixture
def mock_user_manager():
    """Create a mock user manager."""
    return MagicMock()


@pytest.fixture
def nats_message_handler(mock_nats_service, mock_subject_manager, mock_connection_manager, mock_user_manager):
    """Create a NATSMessageHandler instance."""
    return NATSMessageHandler(
        nats_service=mock_nats_service,
        subject_manager=mock_subject_manager,
        connection_manager=mock_connection_manager,
        user_manager=mock_user_manager,
    )


def test_nats_message_handler_init(nats_message_handler, mock_nats_service, mock_subject_manager):
    """Test NATSMessageHandler initialization."""
    assert nats_message_handler.nats_service == mock_nats_service
    assert nats_message_handler.subject_manager == mock_subject_manager
    assert nats_message_handler.subscriptions == {}
    assert isinstance(nats_message_handler.retry_handler, NATSRetryHandler)
    assert hasattr(nats_message_handler, "dead_letter_queue")
    assert hasattr(nats_message_handler, "circuit_breaker")


def test_connection_manager_property_injected(nats_message_handler, mock_connection_manager):
    """Test connection_manager property returns injected manager."""
    assert nats_message_handler.connection_manager == mock_connection_manager


def test_connection_manager_property_fallback(nats_message_handler):
    """Test connection_manager property falls back when not injected."""
    nats_message_handler._connection_manager = None
    with patch("server.realtime.nats_message_handler._resolve_connection_manager", return_value=None):
        # Should return stub
        manager = nats_message_handler.connection_manager
        assert manager is not None


def test_connection_manager_setter(nats_message_handler, mock_connection_manager):
    """Test connection_manager setter updates references."""
    new_manager = MagicMock()
    nats_message_handler.connection_manager = new_manager
    assert nats_message_handler._connection_manager == new_manager


@pytest.mark.asyncio
async def test_start_success(nats_message_handler):
    """Test start() successfully starts handler."""
    nats_message_handler._subscribe_to_chat_subjects = AsyncMock()
    nats_message_handler.subscribe_to_event_subjects = AsyncMock()
    result = await nats_message_handler.start()
    assert result is True
    nats_message_handler._subscribe_to_chat_subjects.assert_awaited_once()
    nats_message_handler.subscribe_to_event_subjects.assert_awaited_once()


@pytest.mark.asyncio
async def test_start_without_event_subscriptions(nats_message_handler):
    """Test start() works without event subscriptions."""
    nats_message_handler._subscribe_to_chat_subjects = AsyncMock()
    nats_message_handler.subscribe_to_event_subjects = AsyncMock()
    result = await nats_message_handler.start(enable_event_subscriptions=False)
    assert result is True
    nats_message_handler._subscribe_to_chat_subjects.assert_awaited_once()
    nats_message_handler.subscribe_to_event_subjects.assert_not_awaited()


@pytest.mark.asyncio
async def test_start_failure(nats_message_handler):
    """Test start() handles failure."""
    nats_message_handler._subscribe_to_chat_subjects = AsyncMock(side_effect=NATSError("Subscribe error"))
    result = await nats_message_handler.start()
    assert result is False


@pytest.mark.asyncio
async def test_stop_success(nats_message_handler):
    """Test stop() successfully stops handler."""
    nats_message_handler.subscriptions = {"sub1": True, "sub2": True}
    nats_message_handler._unsubscribe_from_subject = AsyncMock(return_value=True)
    result = await nats_message_handler.stop()
    assert result is True
    assert nats_message_handler._unsubscribe_from_subject.await_count == 2


@pytest.mark.asyncio
async def test_stop_failure(nats_message_handler):
    """Test stop() handles failure."""
    nats_message_handler.subscriptions = {"sub1": True}
    nats_message_handler._unsubscribe_from_subject = AsyncMock(side_effect=NATSError("Unsubscribe error"))
    result = await nats_message_handler.stop()
    assert result is False


@pytest.mark.asyncio
async def test_subscribe_to_chat_subjects_no_subject_manager(nats_message_handler):
    """Test _subscribe_to_chat_subjects() raises error when subject manager not available."""
    nats_message_handler.subject_manager = None
    with pytest.raises(RuntimeError, match="NATSSubjectManager is required"):
        await nats_message_handler._subscribe_to_chat_subjects()


@pytest.mark.asyncio
async def test_subscribe_to_standardized_chat_subjects_success(nats_message_handler, mock_subject_manager):
    """Test _subscribe_to_standardized_chat_subjects() successfully subscribes."""
    mock_subject_manager.get_chat_subscription_patterns.return_value = ["chat.say", "chat.global"]
    nats_message_handler._subscribe_to_subject = AsyncMock()
    await nats_message_handler._subscribe_to_standardized_chat_subjects()
    assert nats_message_handler._subscribe_to_subject.await_count == 2


@pytest.mark.asyncio
async def test_subscribe_to_standardized_chat_subjects_partial_failure(nats_message_handler, mock_subject_manager):
    """Test _subscribe_to_standardized_chat_subjects() continues on partial failure."""
    mock_subject_manager.get_chat_subscription_patterns.return_value = ["chat.say", "chat.global", "chat.tell"]
    nats_message_handler._subscribe_to_subject = AsyncMock(side_effect=[None, NATSError("Error"), None])
    await nats_message_handler._subscribe_to_standardized_chat_subjects()
    # Should attempt all 3 subscriptions
    assert nats_message_handler._subscribe_to_subject.await_count == 3


@pytest.mark.asyncio
async def test_subscribe_to_subject_success(nats_message_handler, mock_nats_service):
    """Test _subscribe_to_subject() successfully subscribes."""
    mock_nats_service.subscribe = AsyncMock()
    await nats_message_handler._subscribe_to_subject("test.subject")
    mock_nats_service.subscribe.assert_awaited_once_with("test.subject", nats_message_handler._handle_nats_message)
    assert "test.subject" in nats_message_handler.subscriptions


@pytest.mark.asyncio
async def test_subscribe_to_subject_failure(nats_message_handler, mock_nats_service):
    """Test _subscribe_to_subject() raises error on failure."""
    mock_nats_service.subscribe = AsyncMock(side_effect=NATSSubscribeError("Subscribe error", subject="test.subject"))
    with pytest.raises(NATSSubscribeError):
        await nats_message_handler._subscribe_to_subject("test.subject")
    assert "test.subject" not in nats_message_handler.subscriptions


@pytest.mark.asyncio
async def test_unsubscribe_from_subject_success(nats_message_handler, mock_nats_service):
    """Test _unsubscribe_from_subject() successfully unsubscribes."""
    nats_message_handler.subscriptions = {"test.subject": True}
    mock_nats_service.unsubscribe = AsyncMock(return_value=True)
    result = await nats_message_handler._unsubscribe_from_subject("test.subject")
    assert result is True
    assert "test.subject" not in nats_message_handler.subscriptions


@pytest.mark.asyncio
async def test_unsubscribe_from_subject_not_found(nats_message_handler, mock_nats_service):
    """Test _unsubscribe_from_subject() handles subscription not found."""
    nats_message_handler.subscriptions = {}
    mock_nats_service.unsubscribe = AsyncMock(return_value=False)
    result = await nats_message_handler._unsubscribe_from_subject("test.subject")
    assert result is False


@pytest.mark.asyncio
async def test_unsubscribe_from_subject_error(nats_message_handler, mock_nats_service):
    """Test _unsubscribe_from_subject() handles errors."""
    nats_message_handler.subscriptions = {"test.subject": True}
    mock_nats_service.unsubscribe = AsyncMock(side_effect=NATSError("Unsubscribe error"))
    result = await nats_message_handler._unsubscribe_from_subject("test.subject")
    assert result is False


@pytest.mark.asyncio
async def test_handle_nats_message_success(nats_message_handler):
    """Test _handle_nats_message() successfully processes message."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "TestPlayer",
    }
    nats_message_handler.circuit_breaker.call = AsyncMock()
    nats_message_handler.metrics.record_message_processed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        nats_message_handler.circuit_breaker.call.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_nats_message_circuit_breaker_open(nats_message_handler):
    """Test _handle_nats_message() handles circuit breaker open."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
    }
    nats_message_handler.circuit_breaker.call = AsyncMock(side_effect=CircuitBreakerOpen("Circuit open"))
    nats_message_handler.dead_letter_queue.enqueue = MagicMock()
    nats_message_handler.metrics.record_message_dlq = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        # Should add to DLQ when circuit is open
        nats_message_handler.dead_letter_queue.enqueue.assert_called_once()


@pytest.mark.asyncio
async def test_handle_nats_message_retry_on_failure(nats_message_handler):
    """Test _handle_nats_message() uses circuit breaker which handles retries."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
    }
    nats_message_handler.circuit_breaker.call = AsyncMock()
    nats_message_handler.metrics.record_message_processed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        # Circuit breaker handles retries internally
        nats_message_handler.circuit_breaker.call.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_nats_message_dlq_on_final_failure(nats_message_handler):
    """Test _handle_nats_message() adds to DLQ on unhandled error."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
    }
    nats_message_handler.circuit_breaker.call = AsyncMock(side_effect=NATSError("Unhandled error"))
    nats_message_handler.dead_letter_queue.enqueue = MagicMock()
    nats_message_handler.metrics.record_message_failed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        # Should add to DLQ on unhandled error
        nats_message_handler.dead_letter_queue.enqueue.assert_called_once()


@pytest.mark.asyncio
async def test_subscribe_to_event_subjects_success(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_event_subjects() successfully subscribes."""
    mock_subject_manager.get_event_subscription_patterns.return_value = ["event.player_entered", "event.player_left"]
    nats_message_handler._subscribe_to_subject = AsyncMock()
    await nats_message_handler.subscribe_to_event_subjects()
    assert nats_message_handler._subscribe_to_subject.await_count == 2


@pytest.mark.asyncio
async def test_subscribe_to_event_subjects_no_subject_manager(nats_message_handler):
    """Test subscribe_to_event_subjects() raises error when subject manager not available."""
    nats_message_handler.subject_manager = None
    with pytest.raises(RuntimeError, match="NATSSubjectManager is required for event subscriptions"):
        await nats_message_handler.subscribe_to_event_subjects()


@pytest.mark.asyncio
async def test_subscribe_to_event_subjects_error(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_event_subjects() handles errors."""
    mock_subject_manager.get_event_subscription_patterns.return_value = ["event.player_entered"]
    nats_message_handler._subscribe_to_subject = AsyncMock(side_effect=NATSError("Error"))
    # Should not raise, just log error
    await nats_message_handler.subscribe_to_event_subjects()
