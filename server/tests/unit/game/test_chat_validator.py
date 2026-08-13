"""Unit tests for chat message validation helpers."""

import uuid
from unittest.mock import MagicMock

import pytest

from server.game.chat_message import ChatMessage
from server.game.chat_validator import (
    contains_malicious_content,
    validate_chat_message,
    validate_room_access,
)


def _message(content: str = "Hello", **kwargs) -> ChatMessage:
    return ChatMessage(uuid.uuid4(), "TestPlayer", "say", content, **kwargs)


def test_validate_chat_message_accepts_valid_message():
    assert validate_chat_message(_message("Hello world")) is True


def test_validate_chat_message_rejects_empty_content():
    assert validate_chat_message(_message("   ")) is False


def test_validate_chat_message_rejects_too_long_content():
    assert validate_chat_message(_message("x" * 1001)) is False


def test_validate_chat_message_rejects_missing_sender():
    message = _message()
    message.sender_id = ""
    assert validate_chat_message(message) is False


def test_validate_chat_message_rejects_malicious_script():
    assert validate_chat_message(_message("<script>alert(1)</script>")) is False


def test_validate_chat_message_handles_invalid_object():
    bad = MagicMock()
    bad.content = None
    bad.id = "bad"
    type(bad).sender_id = property(lambda _self: (_ for _ in ()).throw(AttributeError("boom")))
    assert validate_chat_message(bad) is False


def test_validate_room_access_allows_none_room_for_system():
    assert validate_room_access(str(uuid.uuid4()), None) is True


def test_validate_room_access_rejects_empty_sender():
    assert validate_room_access("", "room_1") is False


def test_validate_room_access_rejects_blank_room_id():
    assert validate_room_access(str(uuid.uuid4()), "   ") is False


def test_validate_room_access_accepts_valid_room():
    assert validate_room_access(str(uuid.uuid4()), "earth_arkham_downtown_001") is True


@pytest.mark.parametrize(
    "content",
    [
        "javascript:alert(1)",
        "data:text/html,<script>",
        "vbscript:msgbox(1)",
        '<img src=x onerror="alert(1)">',
    ],
)
def test_contains_malicious_content_detects_patterns(content: str):
    assert contains_malicious_content(content) is True


def test_contains_malicious_content_allows_safe_text():
    assert contains_malicious_content("The stars are right.") is False


def test_contains_malicious_content_fails_safe_on_type_error():
    assert contains_malicious_content(None) is True  # type: ignore[arg-type]
