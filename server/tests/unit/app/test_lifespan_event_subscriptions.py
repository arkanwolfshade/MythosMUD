"""Unit tests for lifespan event subscription producers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.app.lifespan_event_subscriptions import subscribe_quest_events
from server.events.event_types import QuestCompleted
from server.tests.unit.realtime.envelope_assertions import assert_event_envelope


@pytest.mark.asyncio
async def test_quest_log_updated_event_envelope_shape():
    """quest_log_updated producer emits a build_event-shaped envelope with player_id."""
    handlers: list = []
    event_bus = MagicMock()
    event_bus.subscribe = lambda event_type, handler, service_id=None: handlers.append(handler)

    conn_mgr = MagicMock()
    conn_mgr.send_personal_message = AsyncMock()
    quest_service = MagicMock()
    quest_service.get_quest_log = AsyncMock(return_value=[])

    container = MagicMock()
    container.event_bus = event_bus
    container.quest_service = quest_service
    container.connection_manager = conn_mgr

    with patch("server.game.quest.quest_events.subscribe_quest_events"):
        subscribe_quest_events(container)

    assert len(handlers) == 1
    player_id = str(uuid.uuid4())
    await handlers[0](QuestCompleted(player_id=player_id, quest_id="quest-1"))

    conn_mgr.send_personal_message.assert_awaited_once()
    event = conn_mgr.send_personal_message.await_args.args[1]
    assert_event_envelope(event, event_type="quest_log_updated", require_player_id=True)
