"""
Unit tests for NATS message handler chat and messaging.

Tests chat field extraction, validation, broadcast, dampening, and lucidity.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.nats_exceptions import NATSError

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


def test_extract_chat_message_fields(nats_message_handler):
    """Test _extract_chat_message_fields extracts fields."""
    message_data = {
        "channel": "whisper",
        "target_id": "player_002",
        "sender_id": "player_001",
        "sender_name": "Player1",
        "content": "Hello",
        "message_id": "msg_001",
        "timestamp": "2024-01-01T00:00:00Z",
        "room_id": "room_001",
    }
    result = nats_message_handler._extract_chat_message_fields(message_data)
    assert result["channel"] == "whisper"
    assert result["target_player_id"] == "player_002"


def test_validate_chat_message_fields(nats_message_handler):
    """Test _validate_chat_message_fields validates fields."""
    chat_fields = {
        "channel": "say",
        "sender_id": "player_001",
        "sender_name": "Player1",
        "content": "Hello",
        "message_id": "msg_001",
    }
    message_data = chat_fields.copy()
    nats_message_handler._validate_chat_message_fields(chat_fields, message_data)


def test_validate_chat_message_fields_missing(nats_message_handler):
    """Test _validate_chat_message_fields raises error when fields missing."""
    chat_fields = {"channel": "say"}
    message_data = chat_fields.copy()
    with pytest.raises((KeyError, ValueError)):
        nats_message_handler._validate_chat_message_fields(chat_fields, message_data)


def test_build_chat_event(nats_message_handler):
    """Test _build_chat_event builds event."""
    chat_fields = {
        "sender_id": "player_001",
        "sender_name": "Player1",
        "channel": "say",
        "message_id": "msg_001",
        "timestamp": "2024-01-01T00:00:00Z",
        "target_id": None,
        "target_name": None,
        "content": "Hello",
    }
    result = nats_message_handler._build_chat_event(chat_fields, "Player1 says: Hello")
    assert isinstance(result, dict)
    assert result["data"]["channel"] == "say"


def test_convert_ids_to_uuids(nats_message_handler):
    """Test _convert_ids_to_uuids converts IDs."""
    sender_id_str = str(uuid.uuid4())
    target_id_str = str(uuid.uuid4())
    sender_id_uuid, target_uuid = nats_message_handler._convert_ids_to_uuids(sender_id_str, target_id_str)
    assert isinstance(sender_id_uuid, uuid.UUID)
    assert isinstance(target_uuid, uuid.UUID)


def test_convert_ids_to_uuids_none_target(nats_message_handler):
    """Test _convert_ids_to_uuids handles None target."""
    sender_id_str = str(uuid.uuid4())
    sender_id_uuid, target_uuid = nats_message_handler._convert_ids_to_uuids(sender_id_str, None)
    assert isinstance(sender_id_uuid, uuid.UUID)
    assert target_uuid is None


def test_format_message_for_receiver(nats_message_handler):
    """Test _format_message_for_receiver formats message."""
    result = nats_message_handler._format_message_for_receiver("say", "Player1", "Hello")
    assert isinstance(result, str)
    assert "Player1" in result


@pytest.mark.asyncio
async def test_get_player_lucidity_tier(nats_message_handler):
    """Test _get_player_lucidity_tier gets tier."""
    with patch("server.database.get_async_session") as mock_session:
        mock_session.return_value.__aiter__.return_value = [AsyncMock()]
        result = await nats_message_handler._get_player_lucidity_tier("player_001")
        assert isinstance(result, str)


@pytest.mark.asyncio
async def test_get_player_lucidity_tier_default(nats_message_handler):
    """Test _get_player_lucidity_tier returns default on error."""
    with patch("server.database.get_async_session", side_effect=Exception("Error")):
        result = await nats_message_handler._get_player_lucidity_tier("player_001")
        assert result == "lucid"


def test_validate_chat_message_fields_type_errors(nats_message_handler):
    """Test _validate_chat_message_fields raises TypeError for invalid types."""
    chat_fields = {
        "channel": 123,
        "sender_id": "sender_001",
        "sender_name": "TestPlayer",
        "content": "Hello",
        "message_id": "msg_001",
    }
    with pytest.raises(TypeError, match="channel must be str"):
        nats_message_handler._validate_chat_message_fields(chat_fields, {})


def test_validate_chat_message_fields_sender_name_type_error(nats_message_handler):
    """Test _validate_chat_message_fields raises TypeError for invalid sender_name type."""
    chat_fields = {
        "channel": "say",
        "sender_id": "sender_001",
        "sender_name": 123,
        "content": "Hello",
        "message_id": "msg_001",
    }
    with pytest.raises(TypeError, match="sender_name must be str"):
        nats_message_handler._validate_chat_message_fields(chat_fields, {})


def test_validate_chat_message_fields_content_type_error(nats_message_handler):
    """Test _validate_chat_message_fields raises TypeError for invalid content type."""
    chat_fields = {
        "channel": "say",
        "sender_id": "sender_001",
        "sender_name": "TestPlayer",
        "content": 123,
        "message_id": "msg_001",
    }
    with pytest.raises(TypeError, match="content must be str"):
        nats_message_handler._validate_chat_message_fields(chat_fields, {})


def test_validate_chat_message_fields_sender_id_type_error(nats_message_handler):
    """Test _validate_chat_message_fields raises TypeError for invalid sender_id type."""
    chat_fields = {
        "channel": "say",
        "sender_id": 123,
        "sender_name": "TestPlayer",
        "content": "Hello",
        "message_id": "msg_001",
    }
    with pytest.raises(TypeError, match="sender_id must be str"):
        nats_message_handler._validate_chat_message_fields(chat_fields, {})


def test_extract_chat_message_fields_whisper_target_id(nats_message_handler):
    """Test _extract_chat_message_fields handles whisper target_id."""
    message_data = {
        "channel": "whisper",
        "target_id": "target_001",
        "sender_id": "sender_001",
        "sender_name": "TestPlayer",
        "content": "Hello",
        "message_id": "msg_001",
    }
    result = nats_message_handler._extract_chat_message_fields(message_data)
    assert result["target_player_id"] == "target_001"


def test_convert_ids_to_uuids_uuid_objects(nats_message_handler):
    """Test _convert_ids_to_uuids handles UUID objects."""
    sender_uuid = uuid.uuid4()
    target_uuid = uuid.uuid4()
    result_sender, result_target = nats_message_handler._convert_ids_to_uuids(sender_uuid, target_uuid)
    assert result_sender == sender_uuid
    assert result_target == target_uuid


@pytest.mark.asyncio
async def test_process_message_with_retry_failure(nats_message_handler):
    """Test _process_message_with_retry adds to DLQ on failure."""
    message_data = {"channel": "say", "content": "Hello"}
    nats_message_handler.retry_handler.retry_with_backoff = AsyncMock(return_value=(False, ValueError("Error")))
    nats_message_handler.dead_letter_queue.enqueue_async = AsyncMock()
    nats_message_handler.metrics.record_message_dlq = MagicMock()
    nats_message_handler.metrics.record_message_failed = MagicMock()
    with pytest.raises(ValueError):
        await nats_message_handler._process_message_with_retry(message_data)
    nats_message_handler.dead_letter_queue.enqueue_async.assert_awaited_once()
    nats_message_handler.metrics.record_message_dlq.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_by_channel_type_exception(nats_message_handler):
    """Test _broadcast_by_channel_type handles exceptions."""
    chat_event = {"type": "chat_message", "data": {}}
    nats_message_handler._event_handler = MagicMock()
    with patch(
        "server.realtime.channel_broadcasting_strategies.channel_strategy_factory.get_strategy",
        side_effect=ValueError("Error"),
    ):
        await nats_message_handler._broadcast_by_channel_type("say", chat_event, "room_001", "", None, uuid.uuid4())


@pytest.mark.asyncio
async def test_send_messages_to_players_no_original_content(nats_message_handler):
    """Test _send_messages_to_players handles missing original_content."""
    chat_event = {
        "type": "chat_message",
        "data": {"message": "Player1 says: Hello", "player_name": "Player1"},
    }
    sender_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    filtered_targets = [target_id]
    nats_message_handler._get_player_lucidity_tier = AsyncMock(return_value="lucid")
    nats_message_handler.connection_manager.send_personal_message = AsyncMock()
    with patch(
        "server.services.lucidity_communication_dampening.apply_communication_dampening",
        return_value={"blocked": False, "message": "Hello"},
    ):
        await nats_message_handler._send_messages_to_players(filtered_targets, chat_event, "room_001", sender_id, "say")
        nats_message_handler.connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_messages_to_players_blocked(nats_message_handler):
    """Test _send_messages_to_players skips blocked messages."""
    chat_event = {
        "type": "chat_message",
        "data": {"original_content": "Hello", "player_name": "Player1"},
    }
    sender_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    filtered_targets = [target_id]
    nats_message_handler._get_player_lucidity_tier = AsyncMock(return_value="lucid")
    nats_message_handler.connection_manager.send_personal_message = AsyncMock()
    with patch(
        "server.services.lucidity_communication_dampening.apply_communication_dampening",
        return_value={"blocked": True, "message": "Hello"},
    ):
        await nats_message_handler._send_messages_to_players(filtered_targets, chat_event, "room_001", sender_id, "say")
        nats_message_handler.connection_manager.send_personal_message.assert_not_awaited()


@pytest.mark.asyncio
async def test_send_messages_to_players_with_tags(nats_message_handler):
    """Test _send_messages_to_players adds tags from dampening."""
    chat_event = {
        "type": "chat_message",
        "data": {"original_content": "Hello", "player_name": "Player1"},
    }
    sender_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    filtered_targets = [target_id]
    nats_message_handler._get_player_lucidity_tier = AsyncMock(return_value="lucid")
    nats_message_handler.connection_manager.send_personal_message = AsyncMock()
    with patch(
        "server.services.lucidity_communication_dampening.apply_communication_dampening",
        return_value={"blocked": False, "message": "Hello", "tags": ["strained"]},
    ):
        await nats_message_handler._send_messages_to_players(filtered_targets, chat_event, "room_001", sender_id, "say")
        call_args = nats_message_handler.connection_manager.send_personal_message.call_args
        assert call_args[0][1]["data"]["tags"] == ["strained"]


@pytest.mark.asyncio
async def test_send_messages_to_players_invalid_player_id(nats_message_handler):
    """Test _send_messages_to_players handles invalid player_id."""
    chat_event = {
        "type": "chat_message",
        "data": {"original_content": "Hello", "player_name": "Player1"},
    }
    sender_id = str(uuid.uuid4())
    filtered_targets = ["invalid-uuid"]
    nats_message_handler._get_player_lucidity_tier = AsyncMock(return_value="lucid")
    with patch(
        "server.services.lucidity_communication_dampening.apply_communication_dampening",
        return_value={"blocked": False, "message": "Hello"},
    ):
        await nats_message_handler._send_messages_to_players(filtered_targets, chat_event, "room_001", sender_id, "say")


def test_should_echo_to_sender_not_echo_channel(nats_message_handler):
    """Test _should_echo_to_sender returns False for non-echo channels."""
    result = nats_message_handler._should_echo_to_sender("global", "chat_message", "msg_001", [], False)
    assert result is False


def test_should_echo_to_sender_not_chat_message(nats_message_handler):
    """Test _should_echo_to_sender returns False for non-chat messages."""
    result = nats_message_handler._should_echo_to_sender("say", "other_type", "msg_001", ["target"], False)
    assert result is False


def test_should_echo_to_sender_no_message_id(nats_message_handler):
    """Test _should_echo_to_sender returns False when message_id is None."""
    result = nats_message_handler._should_echo_to_sender("say", "chat_message", None, ["target"], False)
    assert result is False


def test_should_echo_to_sender_with_targets(nats_message_handler):
    """Test _should_echo_to_sender returns True when targets exist."""
    result = nats_message_handler._should_echo_to_sender("say", "chat_message", "msg_001", ["target"], False)
    assert result is True


def test_should_echo_to_sender_no_targets_not_notified(nats_message_handler):
    """Test _should_echo_to_sender returns True when no targets but not notified."""
    result = nats_message_handler._should_echo_to_sender("say", "chat_message", "msg_001", [], False)
    assert result is True


def test_should_echo_to_sender_no_targets_already_notified(nats_message_handler):
    """Test _should_echo_to_sender returns False when no targets and already notified."""
    result = nats_message_handler._should_echo_to_sender("say", "chat_message", "msg_001", [], True)
    assert result is False


@pytest.mark.asyncio
async def test_echo_message_to_sender_success(nats_message_handler):
    """Test _echo_message_to_sender echoes message."""
    chat_event = {"type": "chat_message", "data": {}}
    sender_id = str(uuid.uuid4())
    nats_message_handler.connection_manager.send_personal_message = AsyncMock()
    await nats_message_handler._echo_message_to_sender(sender_id, chat_event, "room_001", "say", {}, "msg_001")
    nats_message_handler.connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_echo_message_to_sender_exception(nats_message_handler):
    """Test _echo_message_to_sender handles exceptions."""
    chat_event = {"type": "chat_message", "data": {}}
    sender_id = str(uuid.uuid4())
    nats_message_handler.connection_manager.send_personal_message = AsyncMock(side_effect=NATSError("Error"))
    await nats_message_handler._echo_message_to_sender(sender_id, chat_event, "room_001", "say", {}, "msg_001")


@pytest.mark.asyncio
async def test_broadcast_to_room_with_filtering_exception(nats_message_handler):
    """Test _broadcast_to_room_with_filtering handles exceptions."""
    chat_event = {"type": "chat_message", "data": {}}
    sender_id = str(uuid.uuid4())
    nats_message_handler._collect_room_targets = MagicMock(return_value=set())
    nats_message_handler._get_user_manager = MagicMock(return_value=MagicMock())
    nats_message_handler._preload_receiver_mute_data = AsyncMock(side_effect=NATSError("Error"))
    await nats_message_handler._broadcast_to_room_with_filtering("room_001", chat_event, sender_id, "say")


@pytest.mark.asyncio
async def test_apply_dampening_and_send_message_blocked(nats_message_handler):
    """Test _apply_dampening_and_send_message handles blocked messages."""
    chat_event = {
        "type": "chat_message",
        "data": {"original_content": "Hello", "player_name": "Player1"},
    }
    sender_id = str(uuid.uuid4())
    receiver_id = str(uuid.uuid4())
    nats_message_handler._get_player_lucidity_tier = AsyncMock(return_value="lucid")
    nats_message_handler.connection_manager.send_personal_message = AsyncMock()
    with patch(
        "server.services.lucidity_communication_dampening.apply_communication_dampening",
        return_value={"blocked": True, "message": "Hello"},
    ):
        await nats_message_handler._apply_dampening_and_send_message(chat_event, sender_id, receiver_id, "say")
        nats_message_handler.connection_manager.send_personal_message.assert_not_awaited()


@pytest.mark.asyncio
async def test_apply_dampening_and_send_message_no_original_content(nats_message_handler):
    """Test _apply_dampening_and_send_message handles missing original_content."""
    chat_event = {
        "type": "chat_message",
        "data": {"message": "Player1 says: Hello", "player_name": "Player1"},
    }
    sender_id = str(uuid.uuid4())
    receiver_id = str(uuid.uuid4())
    nats_message_handler._get_player_lucidity_tier = AsyncMock(return_value="lucid")
    nats_message_handler.connection_manager.send_personal_message = AsyncMock()
    with patch(
        "server.services.lucidity_communication_dampening.apply_communication_dampening",
        return_value={"blocked": False, "message": "Hello"},
    ):
        await nats_message_handler._apply_dampening_and_send_message(chat_event, sender_id, receiver_id, "say")
        nats_message_handler.connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_apply_dampening_and_send_message_exception(nats_message_handler):
    """Test _apply_dampening_and_send_message handles exceptions."""
    chat_event = {
        "type": "chat_message",
        "data": {"original_content": "Hello", "player_name": "Player1"},
    }
    sender_id = str(uuid.uuid4())
    receiver_id = str(uuid.uuid4())
    nats_message_handler._get_player_lucidity_tier = AsyncMock(return_value="lucid")
    with patch(
        "server.services.lucidity_communication_dampening.apply_communication_dampening",
        side_effect=ValueError("Error"),
    ):
        await nats_message_handler._apply_dampening_and_send_message(chat_event, sender_id, receiver_id, "say")


@pytest.mark.asyncio
async def test_get_player_lucidity_tier_with_uuid(nats_message_handler):
    """Test _get_player_lucidity_tier handles UUID objects."""
    player_uuid = uuid.uuid4()
    with patch("server.database.get_async_session") as mock_session:
        mock_session.return_value.__aiter__.return_value = [AsyncMock()]
        result = await nats_message_handler._get_player_lucidity_tier(player_uuid)
        assert isinstance(result, str)


@pytest.mark.asyncio
async def test_get_player_lucidity_tier_exception_in_processing(nats_message_handler):
    """Test _get_player_lucidity_tier handles exceptions during processing."""
    with patch("server.database.get_async_session") as mock_session:
        mock_session_obj = AsyncMock()
        mock_session_obj.__aenter__ = AsyncMock(return_value=mock_session_obj)
        mock_session_obj.__aexit__ = AsyncMock(return_value=None)
        mock_session.return_value.__aiter__.return_value = [mock_session_obj]
        with patch("server.services.lucidity_service.LucidityService") as mock_service:
            mock_service.return_value.get_player_lucidity = AsyncMock(side_effect=Exception("Error"))
            result = await nats_message_handler._get_player_lucidity_tier("player_001")
            assert result == "lucid"
