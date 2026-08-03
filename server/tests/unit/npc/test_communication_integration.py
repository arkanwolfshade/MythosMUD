"""Unit tests for NPC communication integration."""

from unittest.mock import MagicMock, patch

from server.npc.communication_integration import NPCCommunicationIntegration


def test_send_message_to_room_publishes_event() -> None:
    bus = MagicMock()
    integration = NPCCommunicationIntegration(event_bus=bus)
    assert integration.send_message_to_room("npc-1", "room-1", "Hello", channel="say") is True
    bus.publish.assert_called_once()


def test_send_whisper_to_player_publishes_event() -> None:
    bus = MagicMock()
    integration = NPCCommunicationIntegration(event_bus=bus)
    assert integration.send_whisper_to_player("npc-1", "player-1", "Psst", "room-1") is True
    published = bus.publish.call_args[0][0]
    assert published.channel == "whisper"
    assert published.target_id == "player-1"


def test_handle_player_message_triggers_greeting_response() -> None:
    bus = MagicMock()
    integration = NPCCommunicationIntegration(event_bus=bus)
    assert integration.handle_player_message("npc-1", "player-1", "Hello there", "room-1") is True
    assert bus.publish.call_count >= 2


def test_process_message_question_response() -> None:
    integration = NPCCommunicationIntegration(event_bus=MagicMock())
    with patch.object(integration, "send_message_to_room", return_value=True) as send:
        integration._process_message_for_response("npc-1", "Where am I?", "room-1", "local")
    send.assert_called_once()
    assert "question" in send.call_args[0][2].lower()


def test_subscribe_and_unsubscribe_room_messages() -> None:
    integration = NPCCommunicationIntegration(event_bus=MagicMock())
    assert integration.subscribe_to_room_messages("npc-1", "room-1") is True
    assert integration.unsubscribe_from_room_messages("npc-1", "room-1") is True


def test_send_message_error_returns_false() -> None:
    bus = MagicMock()
    bus.publish.side_effect = RuntimeError("bus down")
    integration = NPCCommunicationIntegration(event_bus=bus)
    assert integration.send_message_to_room("npc-1", "room-1", "Hi") is False


def test_process_message_help_and_thanks_responses() -> None:
    integration = NPCCommunicationIntegration(event_bus=MagicMock())
    with patch.object(integration, "send_message_to_room", return_value=True) as send:
        integration._process_message_for_response("npc-1", "I need help", "room-1", "local")
        integration._process_message_for_response("npc-1", "thank you", "room-1", "local")
    assert send.call_count == 2
    assert "help" in send.call_args_list[0][0][2].lower()
    assert "welcome" in send.call_args_list[1][0][2].lower()


def test_process_message_default_response() -> None:
    integration = NPCCommunicationIntegration(event_bus=MagicMock())
    with patch.object(integration, "send_message_to_room", return_value=True) as send:
        integration._process_message_for_response("npc-1", "The stars align.", "room-1", "local")
    send.assert_called_once()


def test_whisper_error_returns_false() -> None:
    bus = MagicMock()
    bus.publish.side_effect = RuntimeError("whisper fail")
    integration = NPCCommunicationIntegration(event_bus=bus)
    assert integration.send_whisper_to_player("npc-1", "player-1", "Psst", "room-1") is False


def test_handle_player_message_error_returns_false() -> None:
    integration = NPCCommunicationIntegration(event_bus=MagicMock())
    with patch.object(integration, "_process_message_for_response", side_effect=RuntimeError("fail")):
        assert integration.handle_player_message("npc-1", "player-1", "Hi", "room-1") is False


def test_subscribe_error_returns_false() -> None:
    integration = NPCCommunicationIntegration(event_bus=MagicMock())
    with patch("server.npc.communication_integration.logger.debug", side_effect=RuntimeError("fail")):
        assert integration.subscribe_to_room_messages("npc-1", "room-1") is False


def test_unsubscribe_error_returns_false() -> None:
    integration = NPCCommunicationIntegration(event_bus=MagicMock())
    with patch("server.npc.communication_integration.logger.debug", side_effect=RuntimeError("fail")):
        assert integration.unsubscribe_from_room_messages("npc-1", "room-1") is False


def test_init_without_event_bus_uses_default() -> None:
    integration = NPCCommunicationIntegration()
    assert integration.event_bus is not None
