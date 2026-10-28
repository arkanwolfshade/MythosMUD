"""
Unit tests for the rest countdown task helpers.

Covers send_intentional_disconnect_notice, the event that tells the client a /rest socket close is
deliberate so it returns to login instead of reconnecting.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.rest_countdown_task import send_intentional_disconnect_notice
from server.constants.message_category import MessageCategory


@pytest.mark.asyncio
async def test_send_intentional_disconnect_notice_sends_event_to_player() -> None:
    """The notice is an intentional_disconnect event addressed to the resting player."""
    player_id = uuid.uuid4()
    sent: list[tuple[uuid.UUID, dict[str, object]]] = []

    async def record_send(target: uuid.UUID, event: dict[str, object]) -> dict[str, object]:
        sent.append((target, event))
        return {}

    manager = MagicMock()
    manager.sequence_counter = 0
    manager.send_personal_message = AsyncMock(side_effect=record_send)

    await send_intentional_disconnect_notice(player_id, manager)

    assert len(sent) == 1
    target, event = sent[0]
    assert target == player_id
    assert event["event_type"] == "intentional_disconnect"
    assert event["player_id"] == player_id
    assert "rested" in str(event["data"])


@pytest.mark.asyncio
async def test_send_intentional_disconnect_notice_swallows_send_failure() -> None:
    """A dead socket must not stop the disconnect that follows the notice."""
    manager = MagicMock()
    manager.sequence_counter = 0
    manager.send_personal_message = AsyncMock(side_effect=RuntimeError("socket closed"))

    await send_intentional_disconnect_notice(uuid.uuid4(), manager)


@pytest.mark.asyncio
async def test_send_intentional_disconnect_notice_can_be_silent() -> None:
    """The instant /rest path already replies "You rest peacefully..."; an empty message avoids a duplicate line."""
    sent: list[dict[str, object]] = []

    async def record_send(_target: uuid.UUID, event: dict[str, object]) -> dict[str, object]:
        sent.append(event)
        return {}

    manager = MagicMock()
    manager.sequence_counter = 0
    manager.send_personal_message = AsyncMock(side_effect=record_send)

    await send_intentional_disconnect_notice(uuid.uuid4(), manager, message="")

    assert len(sent) == 1
    assert sent[0]["event_type"] == "intentional_disconnect"
    assert sent[0]["data"] == {"message": "", "category": MessageCategory.SYSTEM_INFO}
