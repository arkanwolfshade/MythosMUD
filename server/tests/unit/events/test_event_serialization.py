"""Tests for event serialization used by the distributed EventBus."""

import uuid

import pytest

from server.events.event_serialization import deserialize_event, serialize_event
from server.events.event_types import PlayerDiedEvent, PlayerEnteredRoom
from server.services.player_combat_service import PlayerXPAwardEvent


def test_serialize_deserialize_player_entered_room():
    """Test PlayerEnteredRoom round-trip."""
    event = PlayerEnteredRoom(player_id="p1", room_id="r1", from_room_id="r0")
    data = serialize_event(event)
    assert data["_event_type"] == "PlayerEnteredRoom"
    assert data["player_id"] == "p1"
    assert data["room_id"] == "r1"

    restored = deserialize_event(data)
    assert isinstance(restored, PlayerEnteredRoom)
    assert restored.player_id == event.player_id
    assert restored.room_id == event.room_id
    assert restored.from_room_id == event.from_room_id


def test_serialize_deserialize_player_died_event():
    """Test PlayerDiedEvent with UUID round-trip."""
    pid = uuid.uuid4()
    event = PlayerDiedEvent(player_id=pid, player_name="Test", room_id="r1")
    data = serialize_event(event)
    assert "player_id" in data
    assert isinstance(data["player_id"], str)

    restored = deserialize_event(data)
    assert restored.player_id == pid
    assert restored.player_name == "Test"


def test_serialize_deserialize_player_xp_award_event():
    """Test PlayerXPAwardEvent round-trip (fixes NATS deserialization error)."""
    pid = uuid.uuid4()
    event = PlayerXPAwardEvent(player_id=pid, xp_amount=100, new_level=5)
    data = serialize_event(event)
    assert data["_event_type"] == "player_xp_awarded"
    assert "player_id" in data
    assert data["xp_amount"] == 100
    assert data["new_level"] == 5

    restored = deserialize_event(data)
    assert isinstance(restored, PlayerXPAwardEvent)
    assert restored.player_id == pid
    assert restored.xp_amount == 100
    assert restored.new_level == 5


def test_deserialize_unknown_event_type_raises():
    """Test deserialize with unknown event type raises ValueError."""
    with pytest.raises(ValueError, match="Unknown event type"):
        deserialize_event({"_event_type": "UnknownEventType", "foo": "bar"})


def test_deserialize_missing_event_type_raises():
    """Test deserialize without _event_type raises ValueError."""
    with pytest.raises(ValueError, match="Missing _event_type"):
        deserialize_event({"player_id": "p1", "room_id": "r1"})


def test_serialize_non_base_event_raises():
    """Test serialize with non-BaseEvent raises ValueError."""

    class NotAnEvent:
        pass

    with pytest.raises(ValueError, match="must inherit from BaseEvent"):
        serialize_event(NotAnEvent())
