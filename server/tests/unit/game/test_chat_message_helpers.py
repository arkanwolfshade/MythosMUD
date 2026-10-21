"""Unit tests for chat_message_helpers."""

import uuid
from unittest.mock import ANY, MagicMock, patch

from server.game.chat_message import ChatMessage
from server.game.chat_message_helpers import (
    create_and_log_chat_message,
    create_and_log_say_message,
    store_global_message_in_history,
    store_message_in_room_history,
)


def test_create_and_log_chat_message() -> None:
    player_id = str(uuid.uuid4())
    with patch("server.game.chat_message_helpers.chat_logger.log_chat_message") as mock_log:
        with patch.object(ChatMessage, "log_message") as mock_msg_log:
            msg = create_and_log_chat_message(player_id, "Armitage", "  hello  ", "room-1", "say")
    assert msg.content == "hello"
    assert msg.channel == "say"
    mock_log.assert_called_once()
    mock_msg_log.assert_called_once()


def test_create_and_log_say_message() -> None:
    player_id = str(uuid.uuid4())
    with patch("server.game.chat_message_helpers.create_and_log_chat_message") as mock_create:
        mock_create.return_value = MagicMock()
        create_and_log_say_message(player_id, "Armitage", "hi", "room-1")
    mock_create.assert_called_once_with(player_id, "Armitage", "hi", "room-1", "say")


def test_store_message_in_room_history_creates_and_trims() -> None:
    room_messages: dict[str, list[ChatMessage]] = {}
    messages = [ChatMessage(str(uuid.uuid4()), "A", "say", "m") for _ in range(3)]
    for msg in messages:
        store_message_in_room_history(room_messages, msg, "room-1", max_messages=2)
    assert len(room_messages["room-1"]) == 2
    assert room_messages["room-1"][-1] is messages[-1]


def test_store_global_message_in_history_trims() -> None:
    room_messages: dict[str, list[ChatMessage]] = {}
    messages = [ChatMessage(str(uuid.uuid4()), "A", "global", "m") for _ in range(4)]
    for msg in messages:
        store_global_message_in_history(room_messages, msg, max_messages=2)
    assert len(room_messages["global"]) == 2


def test_a_private_message_is_created_and_logged_with_its_target() -> None:
    """#1107: logging it first and setting the target afterwards recorded a private line as public room chat."""
    player_id, target = str(uuid.uuid4()), str(uuid.uuid4())
    with (
        patch("server.game.chat_message_helpers.chat_logger.log_chat_message") as mock_log,
        patch.object(ChatMessage, "log_message", autospec=True) as mock_msg_log,
    ):
        msg = create_and_log_chat_message(player_id, "Ghoul", "Sit.", "room-1", "say", target_id=target)

    assert msg.target_id == target
    mock_log.assert_called_once_with(
        {
            "message_id": ANY,
            "channel": "say",
            "sender_id": player_id,
            "sender_name": "Ghoul",
            "content": "Sit.",
            "room_id": "room-1",
            "target_player_id": target,
            "filtered": False,
            "moderation_notes": None,
        }
    )
    mock_msg_log.assert_called_once_with(msg)


def test_a_public_message_is_logged_without_a_target() -> None:
    with patch("server.game.chat_message_helpers.chat_logger.log_chat_message") as mock_log:
        msg = create_and_log_chat_message(str(uuid.uuid4()), "Armitage", "hi", "room-1", "say")

    assert msg.target_id is None
    mock_log.assert_called_once()
