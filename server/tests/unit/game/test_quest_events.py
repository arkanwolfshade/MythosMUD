"""Unit tests for quest event subscriptions and handlers."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.events.event_types import NPCDied, PlayerEnteredRoom, PlayerLeftRoom
from server.game.quest import quest_events


def test_entity_id_for_quest_offer_strips_instance_prefix():
    """Instanced room ids map to stable quest offer entity id."""
    stable = "earth_arkhamcity_downtown_001"
    instance_id = f"instance_{uuid.uuid4()}_{stable}"
    assert quest_events._entity_id_for_quest_offer(instance_id) == stable


def test_entity_id_for_quest_offer_plain_room_unchanged():
    """Non-instanced room ids pass through unchanged."""
    room_id = "earth_arkhamcity_downtown_001"
    assert quest_events._entity_id_for_quest_offer(room_id) == room_id


def test_parse_player_id_valid_and_invalid():
    """UUID strings parse; invalid values return None."""
    pid = uuid.uuid4()
    assert quest_events._parse_player_id(str(pid)) == pid
    assert quest_events._parse_player_id("not-a-uuid") is None
    assert quest_events._parse_player_id(None) is None  # type: ignore[arg-type]


def test_subscribe_quest_events_no_op_without_dependencies():
    """Missing event_bus or quest_service skips subscription."""
    container = MagicMock()
    container.event_bus = None
    container.quest_service = MagicMock()
    quest_events.subscribe_quest_events(container)
    container.quest_service.assert_not_called()

    container.event_bus = MagicMock()
    container.quest_service = None
    quest_events.subscribe_quest_events(container)
    container.event_bus.subscribe.assert_not_called()


def test_subscribe_quest_events_registers_handlers():
    """All three quest handlers are subscribed when deps present."""
    container = MagicMock()
    event_bus = MagicMock()
    container.event_bus = event_bus
    container.quest_service = MagicMock()
    quest_events.subscribe_quest_events(container)
    assert event_bus.subscribe.call_count == 3


@pytest.mark.asyncio
async def test_player_entered_starts_quest_by_room_trigger():
    """PlayerEnteredRoom handler starts quests for stable room id."""
    quest_service = AsyncMock()
    handler = quest_events._make_on_player_entered(quest_service)
    player_id = uuid.uuid4()
    stable_room = "earth_arkhamcity_downtown_001"
    event = PlayerEnteredRoom(player_id=str(player_id), room_id=f"instance_{uuid.uuid4()}_{stable_room}")
    await handler(event)
    quest_service.start_quest_by_trigger.assert_awaited_once_with(player_id, "room", stable_room)


@pytest.mark.asyncio
async def test_player_entered_invalid_player_id_skips():
    """Invalid player_id does not call quest service."""
    quest_service = AsyncMock()
    handler = quest_events._make_on_player_entered(quest_service)
    event = PlayerEnteredRoom(player_id="bad-id", room_id="room_a")
    await handler(event)
    quest_service.start_quest_by_trigger.assert_not_awaited()


@pytest.mark.asyncio
async def test_player_left_records_exit_activity():
    """PlayerLeftRoom handler records exit_<stable_room_id> activity."""
    quest_service = AsyncMock()
    handler = quest_events._make_on_player_left(quest_service)
    player_id = uuid.uuid4()
    stable_room = "earth_arkhamcity_downtown_001"
    event = PlayerLeftRoom(player_id=str(player_id), room_id=f"instance_{uuid.uuid4()}_{stable_room}")
    await handler(event)
    quest_service.record_complete_activity.assert_awaited_once_with(player_id, f"exit_{stable_room}")


@pytest.mark.asyncio
async def test_npc_died_records_kill_for_player_killer():
    """NPCDied with player killer records kill progress."""
    quest_service = AsyncMock()
    handler = quest_events._make_on_npc_died(quest_service)
    killer_id = uuid.uuid4()
    event = NPCDied(npc_id="npc_goblin_1", room_id="room_a", killer_id=str(killer_id))
    await handler(event)
    quest_service.record_kill.assert_awaited_once_with(killer_id, "npc_goblin_1")


@pytest.mark.asyncio
async def test_npc_died_no_killer_skips():
    """NPCDied without killer_id does not record kill."""
    quest_service = AsyncMock()
    handler = quest_events._make_on_npc_died(quest_service)
    event = NPCDied(npc_id="npc_goblin_1", room_id="room_a", killer_id=None)
    await handler(event)
    quest_service.record_kill.assert_not_awaited()
