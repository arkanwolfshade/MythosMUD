"""Unit tests for MessageBuilder."""

import uuid
from unittest.mock import MagicMock

from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.realtime.message_builders import MessageBuilder


def _builder(seq_start: int = 1) -> MessageBuilder:
    counter = MagicMock(side_effect=lambda: seq_start)
    return MessageBuilder(counter)


def test_get_next_sequence_uses_callable():
    """Sequence counter callable is invoked."""
    seq = {"n": 0}

    def next_seq() -> int:
        seq["n"] += 1
        return seq["n"]

    builder = MessageBuilder(next_seq)
    assert builder.get_next_sequence() == 1
    assert builder.get_next_sequence() == 2


def test_get_next_sequence_non_callable_returns_zero():
    """Non-callable sequence counter returns 0."""
    builder = MessageBuilder(42)
    assert builder.get_next_sequence() == 0


def test_create_player_entered_message():
    """Player entered message includes ids and player name."""
    player_id = uuid.uuid4()
    event = PlayerEnteredRoom(player_id=str(player_id), room_id="room_a", from_room_id="room_b")
    msg = _builder().create_player_entered_message(event, "Armitage")
    assert msg["event_type"] == "player_entered"
    assert msg["room_id"] == "room_a"
    assert msg["data"]["player_id"] == str(player_id)
    assert msg["data"]["player_name"] == "Armitage"
    assert "enters the room" in msg["data"]["message"]


def test_create_player_left_message():
    """Player left message includes ids and player name."""
    player_id = uuid.uuid4()
    event = PlayerLeftRoom(player_id=str(player_id), room_id="room_a")
    msg = _builder().create_player_left_message(event, "Ward")
    assert msg["event_type"] == "player_left"
    assert msg["data"]["message"] == "Ward leaves the room."


def test_create_npc_movement_message_variants():
    """NPC movement messages cover direction and movement type branches."""
    builder = _builder()
    assert builder.create_npc_movement_message("Rat", "north", "left") == "Rat left north."
    assert builder.create_npc_movement_message("Rat", None, "left") == "Rat left the room."
    assert builder.create_npc_movement_message("Rat", "south", "entered") == "Rat entered from south."
    assert builder.create_npc_movement_message("Rat", None, "entered") == "Rat entered the room."
    assert builder.create_npc_movement_message("Rat", None, "teleport") == "Rat moved."


def test_build_occupants_update_message():
    """Occupants update includes structured and legacy fields."""
    msg = _builder(7).build_occupants_update_message("room_1", ["Alice"], ["Goblin"], ["Alice", "Goblin"])
    assert msg["event_type"] == "room_occupants"
    assert msg["sequence_number"] == 7
    assert msg["data"]["players"] == ["Alice"]
    assert msg["data"]["npcs"] == ["Goblin"]
    assert msg["data"]["occupants"] == ["Alice", "Goblin"]
    assert msg["data"]["count"] == 2


def test_build_room_update_message():
    """Room update wraps room data without occupants."""
    room_data = {"name": "Library", "description": "Dusty tomes."}
    msg = _builder().build_room_update_message("room_lib", room_data)
    assert msg["event_type"] == "room_update"
    assert msg["data"]["room"] == room_data
    assert msg["data"]["entities"] == []


def test_build_room_state_message():
    """Room state includes occupants from room_data."""
    room_data = {"name": "Hall", "occupants": ["Bob"], "occupant_count": 1}
    msg = _builder().build_room_state_message("room_hall", room_data)
    assert msg["event_type"] == "room_state"
    assert msg["data"]["occupants"] == ["Bob"]
    assert msg["data"]["occupant_count"] == 1
