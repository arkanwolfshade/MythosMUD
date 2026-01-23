"""
Unit tests for NATS message handler.

Tests the NATSMessageHandler class lifecycle, start/stop, and core message processing.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.circuit_breaker import CircuitBreakerOpen
from server.realtime.nats_retry_handler import NATSRetryHandler
from server.services.nats_exceptions import NATSError, NATSSubscribeError

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


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
        manager = nats_message_handler.connection_manager
        assert manager is not None


def test_connection_manager_setter(nats_message_handler):
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
    from server.services.nats_exceptions import NATSUnsubscribeError

    mock_nats_service.unsubscribe = AsyncMock(side_effect=NATSUnsubscribeError("Subscription not found"))
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
    nats_message_handler.dead_letter_queue.enqueue_async = AsyncMock()
    nats_message_handler.metrics.record_message_failed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        nats_message_handler.dead_letter_queue.enqueue_async.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_to_event_subjects_success(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_event_subjects() successfully subscribes."""
    mock_subject_manager.get_event_subscription_patterns.return_value = [
        "event.player_entered",
        "event.player_left",
    ]
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
    await nats_message_handler.subscribe_to_event_subjects()


@pytest.mark.asyncio
async def test_process_single_message_chat(nats_message_handler):
    """Test _process_single_message processes chat message."""
    message_data = {
        "channel": "say",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "TestPlayer",
        "content": "Hello",
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "room_id": "room_001",
    }
    nats_message_handler._extract_chat_message_fields = MagicMock(
        return_value={
            "channel": "say",
            "room_id": "room_001",
            "party_id": None,
            "sender_id": message_data["sender_id"],
            "sender_name": "TestPlayer",
            "content": "Hello",
            "target_player_id": None,
            "message_id": message_data["message_id"],
            "timestamp": message_data["timestamp"],
        }
    )
    nats_message_handler._validate_chat_message_fields = MagicMock()
    nats_message_handler._build_chat_event = MagicMock(return_value={"type": "chat_message"})
    nats_message_handler._convert_ids_to_uuids = MagicMock(return_value=(uuid.uuid4(), None))
    nats_message_handler._broadcast_by_channel_type = AsyncMock()
    await nats_message_handler._process_single_message(message_data)
    nats_message_handler._broadcast_by_channel_type.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_single_message_event(nats_message_handler):
    """Test _process_single_message processes event message."""
    message_data = {"event_type": "player_entered", "event_data": {}}
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_event_message = AsyncMock()
    await nats_message_handler._process_single_message(message_data)
    nats_message_handler._event_handler.handle_event_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_to_room(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_room subscribes to room."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.say.room_001")
    nats_message_handler._subscribe_to_subject = AsyncMock()
    await nats_message_handler.subscribe_to_room("room_001")
    nats_message_handler._subscribe_to_subject.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_to_room_no_subject_manager(nats_message_handler):
    """Test subscribe_to_room raises error when subject manager unavailable."""
    nats_message_handler.subject_manager = None
    with pytest.raises(RuntimeError, match="required"):
        await nats_message_handler.subscribe_to_room("room_001")


@pytest.mark.asyncio
async def test_unsubscribe_from_room(nats_message_handler, mock_subject_manager):
    """Test unsubscribe_from_room unsubscribes from room."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.say.room_001")
    nats_message_handler.subscriptions = {"chat.say.room_001": True}
    nats_message_handler._unsubscribe_from_subject = AsyncMock(return_value=True)
    await nats_message_handler.unsubscribe_from_room("room_001")
    nats_message_handler._unsubscribe_from_subject.assert_awaited_once()


def test_get_subscription_count(nats_message_handler):
    """Test get_subscription_count returns count."""
    nats_message_handler.subscriptions = {"sub1": True, "sub2": True}
    count = nats_message_handler.get_subscription_count()
    assert count == 2


def test_get_active_subjects(nats_message_handler):
    """Test get_active_subjects returns subjects."""
    nats_message_handler.subscriptions = {"sub1": True, "sub2": True}
    subjects = nats_message_handler.get_active_subjects()
    assert len(subjects) == 2
    assert "sub1" in subjects


@pytest.mark.asyncio
async def test_subscribe_to_subzone(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_subzone subscribes to subzone."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.local.subzone_001")
    nats_message_handler._subscribe_to_subject = AsyncMock()
    result = await nats_message_handler.subscribe_to_subzone("subzone_001")
    assert result is True
    nats_message_handler._subscribe_to_subject.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_to_subzone_already_subscribed(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_subzone increments count when already subscribed."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.local.subzone_001")
    nats_message_handler.subscriptions = {"chat.local.subzone_001": True}
    nats_message_handler.subzone_subscriptions = {"subzone_001": 1}
    result = await nats_message_handler.subscribe_to_subzone("subzone_001")
    assert result is True
    assert nats_message_handler.subzone_subscriptions["subzone_001"] == 2


@pytest.mark.asyncio
async def test_unsubscribe_from_subzone(nats_message_handler, mock_subject_manager):
    """Test unsubscribe_from_subzone unsubscribes from subzone."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.local.subzone_001")
    nats_message_handler.subscriptions = {"chat.local.subzone_001": True}
    nats_message_handler.subzone_subscriptions = {"subzone_001": 1}
    nats_message_handler._unsubscribe_from_subject = AsyncMock(return_value=True)
    result = await nats_message_handler.unsubscribe_from_subzone("subzone_001")
    assert result is True


def test_track_player_subzone_subscription(nats_message_handler):
    """Test track_player_subzone_subscription tracks subscription."""
    nats_message_handler.track_player_subzone_subscription("player_001", "subzone_001")
    assert nats_message_handler.player_subzone_subscriptions["player_001"] == "subzone_001"


@pytest.mark.asyncio
async def test_process_message_with_retry_exhaustion(nats_message_handler):
    """Test _process_message_with_retry adds to DLQ and re-raises when all retries exhausted."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "channel": "say",
        "content": "Hello",
    }
    test_error = ValueError("Processing failed")
    nats_message_handler.retry_handler.retry_with_backoff = AsyncMock(return_value=(False, test_error))
    nats_message_handler.dead_letter_queue.enqueue_async = AsyncMock()
    nats_message_handler.metrics.record_message_dlq = MagicMock()
    nats_message_handler.metrics.record_message_failed = MagicMock()

    with pytest.raises(ValueError, match="Processing failed"):
        await nats_message_handler._process_message_with_retry(message_data)

    nats_message_handler.dead_letter_queue.enqueue_async.assert_awaited_once()
    nats_message_handler.metrics.record_message_dlq.assert_called_once_with("say")
    nats_message_handler.metrics.record_message_failed.assert_called_once_with("say", "ValueError")


@pytest.mark.asyncio
async def test_process_single_message_validation_error_missing_fields(nats_message_handler):
    """Test _process_single_message raises ValueError when required fields are missing."""
    message_data = {
        "channel": "say",
        # Missing sender_id, sender_name, content, message_id
    }
    nats_message_handler._extract_chat_message_fields = MagicMock(
        return_value={
            "channel": "say",
            "sender_id": None,  # Missing required field
            "sender_name": None,
            "content": None,
            "message_id": None,
        }
    )

    with pytest.raises(ValueError, match="Missing required message fields"):
        await nats_message_handler._process_single_message(message_data)


@pytest.mark.asyncio
async def test_process_single_message_validation_error_type_error(nats_message_handler):
    """Test _process_single_message raises TypeError when field types are invalid."""
    message_data = {"channel": "say"}
    nats_message_handler._extract_chat_message_fields = MagicMock(
        return_value={
            "channel": 123,  # Wrong type - should be str
            "sender_id": str(uuid.uuid4()),
            "sender_name": "TestPlayer",
            "content": "Hello",
            "message_id": str(uuid.uuid4()),
        }
    )

    with pytest.raises(TypeError, match="channel must be str"):
        await nats_message_handler._process_single_message(message_data)


@pytest.mark.asyncio
async def test_handle_nats_message_runtime_error(nats_message_handler):
    """Test _handle_nats_message handles RuntimeError and adds to DLQ."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
    }
    nats_message_handler.circuit_breaker.call = AsyncMock(side_effect=RuntimeError("Runtime error"))
    nats_message_handler.dead_letter_queue.enqueue_async = AsyncMock()
    nats_message_handler.metrics.record_message_failed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        nats_message_handler.dead_letter_queue.enqueue_async.assert_awaited_once()
        nats_message_handler.metrics.record_message_failed.assert_called_once_with("say", "RuntimeError")


@pytest.mark.asyncio
async def test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled(
    nats_message_handler, mock_subject_manager
):
    """Test _subscribe_to_standardized_chat_subjects handles NATSSubscribeError and continues."""
    mock_subject_manager.get_chat_subscription_patterns.return_value = ["chat.say", "chat.global"]
    # First pattern raises NATSSubscribeError, second succeeds
    nats_message_handler._subscribe_to_subject = AsyncMock(
        side_effect=[NATSSubscribeError("Subscribe error", subject="chat.say"), None]
    )

    # Should not raise - error is caught and method continues
    await nats_message_handler._subscribe_to_standardized_chat_subjects()
    # Both patterns should have been attempted
    assert nats_message_handler._subscribe_to_subject.await_count == 2


@pytest.mark.asyncio
async def test_subscribe_to_subject_no_nats_service(nats_message_handler):
    """Test _subscribe_to_subject returns False when nats_service is None."""
    nats_message_handler.nats_service = None
    result = await nats_message_handler._subscribe_to_subject("test.subject")
    assert result is False
    assert "test.subject" not in nats_message_handler.subscriptions


@pytest.mark.asyncio
async def test_handle_nats_message_validation_error(nats_message_handler):
    """Test _handle_nats_message handles validation errors and adds to DLQ."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
    }
    validation_error = ValueError("Invalid message format")
    nats_message_handler.dead_letter_queue.enqueue_async = AsyncMock()
    nats_message_handler.metrics.record_message_failed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", side_effect=validation_error):
        await nats_message_handler._handle_nats_message(message_data)
        nats_message_handler.dead_letter_queue.enqueue_async.assert_awaited_once()
        nats_message_handler.metrics.record_message_failed.assert_called_once_with("say", "ValueError")


@pytest.mark.asyncio
async def test_subscribe_to_standardized_chat_subjects_runtime_error_handled(
    nats_message_handler, mock_subject_manager
):
    """Test _subscribe_to_standardized_chat_subjects handles RuntimeError and continues."""
    mock_subject_manager.get_chat_subscription_patterns.return_value = ["chat.say", "chat.global"]
    # First pattern raises RuntimeError, second succeeds
    nats_message_handler._subscribe_to_subject = AsyncMock(side_effect=[RuntimeError("Runtime error"), None])

    # Should not raise - error is caught and method continues
    await nats_message_handler._subscribe_to_standardized_chat_subjects()
    # Both patterns should have been attempted
    assert nats_message_handler._subscribe_to_subject.await_count == 2


@pytest.mark.asyncio
async def test_subscribe_to_standardized_chat_subjects_nats_error_handled(nats_message_handler, mock_subject_manager):
    """Test _subscribe_to_standardized_chat_subjects handles NATSError and continues."""
    mock_subject_manager.get_chat_subscription_patterns.return_value = ["chat.say", "chat.global"]
    # First pattern raises NATSError, second succeeds
    nats_message_handler._subscribe_to_subject = AsyncMock(side_effect=[NATSError("NATS error"), None])

    # Should not raise - error is caught and method continues
    await nats_message_handler._subscribe_to_standardized_chat_subjects()
    # Both patterns should have been attempted
    assert nats_message_handler._subscribe_to_subject.await_count == 2


@pytest.mark.asyncio
async def test_subscribe_to_subject_nats_error_returns_false(nats_message_handler):
    """Test _subscribe_to_subject returns False on NATSError."""
    nats_message_handler.nats_service.subscribe = AsyncMock(side_effect=NATSError("NATS error"))
    result = await nats_message_handler._subscribe_to_subject("test.subject")
    assert result is False
    assert "test.subject" not in nats_message_handler.subscriptions


@pytest.mark.asyncio
async def test_subscribe_to_subject_runtime_error_returns_false(nats_message_handler):
    """Test _subscribe_to_subject returns False on RuntimeError."""
    nats_message_handler.nats_service.subscribe = AsyncMock(side_effect=RuntimeError("Runtime error"))
    result = await nats_message_handler._subscribe_to_subject("test.subject")
    assert result is False
    assert "test.subject" not in nats_message_handler.subscriptions


def test_connection_manager_property_resolution_error(nats_message_handler):
    """Test connection_manager property handles resolution errors gracefully."""
    nats_message_handler._connection_manager = None
    with patch(
        "server.realtime.nats_message_handler._resolve_connection_manager", side_effect=RuntimeError("Resolution error")
    ):
        # Should fall back to legacy stub, not raise
        manager = nats_message_handler.connection_manager
        assert manager is not None


@pytest.mark.asyncio
async def test_process_single_message_event_handler_error(nats_message_handler):
    """Test _process_single_message raises exception when event handler fails."""
    message_data = {"event_type": "player_entered", "event_data": {}}
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_event_message = AsyncMock(
        side_effect=RuntimeError("Event handler error")
    )

    with pytest.raises(RuntimeError, match="Event handler error"):
        await nats_message_handler._process_single_message(message_data)


@pytest.mark.asyncio
async def test_process_single_message_broadcast_error(nats_message_handler):
    """Test _process_single_message raises exception when broadcast fails."""
    message_data = {
        "channel": "say",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "TestPlayer",
        "content": "Hello",
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "room_id": "room_001",
    }
    nats_message_handler._extract_chat_message_fields = MagicMock(
        return_value={
            "channel": "say",
            "room_id": "room_001",
            "party_id": None,
            "sender_id": message_data["sender_id"],
            "sender_name": "TestPlayer",
            "content": "Hello",
            "target_player_id": None,
            "message_id": message_data["message_id"],
            "timestamp": message_data["timestamp"],
        }
    )
    nats_message_handler._validate_chat_message_fields = MagicMock()
    nats_message_handler._build_chat_event = MagicMock(return_value={"type": "chat_message"})
    nats_message_handler._convert_ids_to_uuids = MagicMock(return_value=(uuid.uuid4(), None))
    nats_message_handler._broadcast_by_channel_type = AsyncMock(side_effect=RuntimeError("Broadcast error"))

    with pytest.raises(RuntimeError, match="Broadcast error"):
        await nats_message_handler._process_single_message(message_data)


@pytest.mark.asyncio
async def test_process_single_message_uuid_conversion_error(nats_message_handler):
    """Test _process_single_message raises exception when UUID conversion fails."""
    message_data = {
        "channel": "say",
        "sender_id": "invalid-uuid",
        "sender_name": "TestPlayer",
        "content": "Hello",
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "room_id": "room_001",
    }
    nats_message_handler._extract_chat_message_fields = MagicMock(
        return_value={
            "channel": "say",
            "room_id": "room_001",
            "party_id": None,
            "sender_id": "invalid-uuid",
            "sender_name": "TestPlayer",
            "content": "Hello",
            "target_player_id": None,
            "message_id": message_data["message_id"],
            "timestamp": message_data["timestamp"],
        }
    )
    nats_message_handler._validate_chat_message_fields = MagicMock()
    nats_message_handler._build_chat_event = MagicMock(return_value={"type": "chat_message"})
    nats_message_handler._convert_ids_to_uuids = MagicMock(side_effect=ValueError("Invalid UUID format"))

    with pytest.raises(ValueError, match="Invalid UUID format"):
        await nats_message_handler._process_single_message(message_data)


@pytest.mark.asyncio
async def test_handle_nats_message_connection_manager_resolution_error(nats_message_handler):
    """Test _handle_nats_message handles connection manager resolution errors."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "TestPlayer",
    }
    nats_message_handler._connection_manager = None
    nats_message_handler.circuit_breaker.call = AsyncMock(side_effect=AttributeError("Connection manager not found"))
    nats_message_handler.dead_letter_queue.enqueue_async = AsyncMock()
    nats_message_handler.metrics.record_message_failed = MagicMock()

    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        with patch("server.realtime.nats_message_handler._resolve_connection_manager", return_value=None):
            await nats_message_handler._handle_nats_message(message_data)
            # Should handle the error and add to DLQ
            nats_message_handler.dead_letter_queue.enqueue_async.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_nats_message_success_path_metrics(nats_message_handler):
    """Test _handle_nats_message records metrics on successful processing."""
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
        nats_message_handler.metrics.record_message_processed.assert_called_once_with("say")


@pytest.mark.asyncio
async def test_handle_nats_message_event_type_detection(nats_message_handler):
    """Test _handle_nats_message detects event messages by event_type."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "event_type": "player_entered",
        "event_data": {},
    }
    nats_message_handler.circuit_breaker.call = AsyncMock()
    nats_message_handler.metrics.record_message_processed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message") as mock_validate:
        await nats_message_handler._handle_nats_message(message_data)
        # Should call validate_message with message_type="event"
        mock_validate.assert_called_once_with(message_data, message_type="event")


@pytest.mark.asyncio
async def test_handle_nats_message_event_data_detection(nats_message_handler):
    """Test _handle_nats_message detects event messages by event_data."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "event_data": {"type": "player_entered"},
    }
    nats_message_handler.circuit_breaker.call = AsyncMock()
    nats_message_handler.metrics.record_message_processed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message") as mock_validate:
        await nats_message_handler._handle_nats_message(message_data)
        # Should call validate_message with message_type="event"
        mock_validate.assert_called_once_with(message_data, message_type="event")


@pytest.mark.asyncio
async def test_process_message_with_retry_success_path(nats_message_handler):
    """Test _process_message_with_retry succeeds when retry handler succeeds."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "channel": "say",
        "content": "Hello",
    }
    nats_message_handler.retry_handler.retry_with_backoff = AsyncMock(return_value=(True, None))
    # Should not raise and should not add to DLQ
    await nats_message_handler._process_message_with_retry(message_data)
    # Verify retry was called
    nats_message_handler.retry_handler.retry_with_backoff.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_single_message_event_data_only(nats_message_handler):
    """Test _process_single_message handles event messages with only event_data."""
    message_data = {"event_data": {"type": "player_entered", "player_id": "player_001"}}
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_event_message = AsyncMock()
    await nats_message_handler._process_single_message(message_data)
    nats_message_handler._event_handler.handle_event_message.assert_awaited_once_with(message_data)


@pytest.mark.asyncio
async def test_connection_manager_setter_updates_helpers(nats_message_handler):
    """Test connection_manager setter updates filtering_helper and event_handler references."""
    new_manager = MagicMock()
    nats_message_handler._filtering_helper = MagicMock()
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler.connection_manager = new_manager
    assert nats_message_handler._connection_manager == new_manager
    assert nats_message_handler._filtering_helper.connection_manager == new_manager
    assert nats_message_handler._event_handler.connection_manager == new_manager


@pytest.mark.asyncio
async def test_connection_manager_property_injected_returns_none(nats_message_handler):
    """Test connection_manager property falls back when injected manager resolves to None."""
    injected_manager = MagicMock()
    nats_message_handler._connection_manager = injected_manager
    with patch("server.realtime.nats_message_handler._resolve_connection_manager") as mock_resolve:
        # First call (for injected) returns None, second call (fallback) returns a manager
        mock_manager = MagicMock()
        mock_resolve.side_effect = [None, mock_manager]
        result = nats_message_handler.connection_manager
        assert result == mock_manager
        assert mock_resolve.call_count == 2


@pytest.mark.asyncio
async def test_process_single_message_event_type_empty_string(nats_message_handler):
    """Test _process_single_message handles event_type as empty string (falsy)."""
    # Empty string is falsy, so should not trigger event handler
    message_data = {
        "event_type": "",
        "channel": "say",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "TestPlayer",
        "content": "Hello",
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
    }
    nats_message_handler._extract_chat_message_fields = MagicMock(
        return_value={
            "channel": "say",
            "room_id": None,
            "party_id": None,
            "sender_id": message_data["sender_id"],
            "sender_name": "TestPlayer",
            "content": "Hello",
            "target_player_id": None,
            "message_id": message_data["message_id"],
            "timestamp": message_data["timestamp"],
        }
    )
    nats_message_handler._validate_chat_message_fields = MagicMock()
    nats_message_handler._build_chat_event = MagicMock(return_value={"type": "chat_message"})
    nats_message_handler._convert_ids_to_uuids = MagicMock(return_value=(uuid.uuid4(), None))
    nats_message_handler._broadcast_by_channel_type = AsyncMock()
    await nats_message_handler._process_single_message(message_data)
    # Should process as chat message, not event
    nats_message_handler._broadcast_by_channel_type.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_nats_message_unknown_channel_defaults(nats_message_handler):
    """Test _handle_nats_message uses 'unknown' as default channel when missing."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        # No channel field
        "content": "Hello",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "TestPlayer",
    }
    nats_message_handler.circuit_breaker.call = AsyncMock()
    nats_message_handler.metrics.record_message_processed = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        # Should record metrics with "unknown" channel
        nats_message_handler.metrics.record_message_processed.assert_called_once_with("unknown")


@pytest.mark.asyncio
async def test_handle_nats_message_unknown_message_id_defaults(nats_message_handler):
    """Test _handle_nats_message uses 'unknown' as default message_id when missing."""
    message_data = {
        # No message_id field
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "TestPlayer",
    }
    nats_message_handler.circuit_breaker.call = AsyncMock(side_effect=CircuitBreakerOpen("Circuit open"))
    nats_message_handler.dead_letter_queue.enqueue = MagicMock()
    nats_message_handler.metrics.record_message_dlq = MagicMock()
    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        # Should handle with "unknown" message_id
        nats_message_handler.dead_letter_queue.enqueue.assert_called_once()
        call_args = nats_message_handler.dead_letter_queue.enqueue.call_args[0][0]
        assert call_args.subject == "say"


@pytest.mark.asyncio
async def test_subscribe_to_standardized_chat_subjects_no_subject_manager(nats_message_handler):
    """Test _subscribe_to_standardized_chat_subjects raises RuntimeError when subject_manager is None."""
    nats_message_handler.subject_manager = None
    with pytest.raises(RuntimeError, match="NATSSubjectManager is required"):
        await nats_message_handler._subscribe_to_standardized_chat_subjects()


@pytest.mark.asyncio
async def test_handle_nats_message_attribute_error_handled(nats_message_handler):
    """Test _handle_nats_message handles AttributeError and adds to DLQ."""
    message_data = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "channel": "say",
        "content": "Hello",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "TestPlayer",
    }
    nats_message_handler.circuit_breaker.call = AsyncMock(side_effect=AttributeError("Missing attribute"))
    nats_message_handler.dead_letter_queue.enqueue_async = AsyncMock()
    nats_message_handler.metrics.record_message_failed = MagicMock()

    with patch("server.realtime.nats_message_handler.validate_message", return_value=message_data):
        await nats_message_handler._handle_nats_message(message_data)
        # Should handle AttributeError and add to DLQ
        nats_message_handler.dead_letter_queue.enqueue_async.assert_awaited_once()
        nats_message_handler.metrics.record_message_failed.assert_called_once_with("say", "AttributeError")
