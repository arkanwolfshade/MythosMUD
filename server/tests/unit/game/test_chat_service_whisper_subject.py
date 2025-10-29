"""
Test whisper subject construction to prevent regression.

This test was created in response to a critical bug discovered during E2E testing
where whisper messages failed to deliver due to incorrect NATS subject construction.

Bug Report: e2e-tests/WHISPER_SYSTEM_INVESTIGATION_REPORT.md
Date Discovered: 2025-10-29
"""

from unittest.mock import AsyncMock, Mock

import pytest

from server.game.chat_service import ChatMessage, ChatService


@pytest.mark.asyncio
async def test_whisper_subject_includes_player_segment():
    """
    CRITICAL: Ensure whisper subjects include 'player.' segment.

    This test prevents regression of the bug where whisper subjects
    were constructed as 'chat.whisper.<UUID>' instead of the correct
    'chat.whisper.player.<UUID>' pattern, causing NATS validation failure.

    The bug caused:
    - 100% whisper functionality failure
    - Subject validation errors in NATS
    - Generic "Chat system temporarily unavailable" errors for users

    Correct Pattern: chat.whisper.player.<player_uuid>
    Incorrect Pattern: chat.whisper.<player_uuid>
    """
    # Arrange - Create mock dependencies
    mock_persistence = Mock()
    mock_room_service = Mock()
    mock_player_service = AsyncMock()

    chat_service = ChatService(mock_persistence, mock_room_service, mock_player_service)

    target_id = "12aed7c5-dc99-488f-a979-28b9d227e858"
    room_id = "test_room_id"  # Room ID for NATS subject construction
    chat_message = ChatMessage(
        "sender-id", "TestUser", "whisper", "Test whisper", target_id=target_id, target_name="TargetUser"
    )

    # Act
    subject = chat_service._build_nats_subject(chat_message, room_id)

    # Assert
    expected_subject = f"chat.whisper.player.{target_id}"
    assert subject == expected_subject, (
        f"Whisper subject must include 'player.' segment. Expected: {expected_subject}, Got: {subject}"
    )

    # Verify it matches subscription pattern
    assert subject.startswith("chat.whisper.player."), (
        "Whisper subject must match subscription pattern 'chat.whisper.player.*'"
    )


@pytest.mark.asyncio
async def test_whisper_subject_without_target_id():
    """
    Test whisper subject construction when target_id is missing.

    This is an edge case that should return a generic whisper subject.
    """
    # Arrange - Create mock dependencies
    mock_persistence = Mock()
    mock_room_service = Mock()
    mock_player_service = AsyncMock()

    chat_service = ChatService(mock_persistence, mock_room_service, mock_player_service)

    room_id = "test_room_id"  # Room ID for NATS subject construction
    chat_message = ChatMessage("sender-id", "TestUser", "whisper", "Test whisper")

    # Act
    subject = chat_service._build_nats_subject(chat_message, room_id)

    # Assert
    assert subject == "chat.whisper", f"Whisper subject without target should be 'chat.whisper'. Got: {subject}"
