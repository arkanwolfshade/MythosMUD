"""
Unit tests for Room class.

Tests the Room class methods for managing room occupants and state.
"""

import uuid
from unittest.mock import Mock

import pytest

from server.models.room import Room


def test_room_init():
    """Test Room initialization with room data."""
    room_data = {
        "id": "room_001",
        "name": "Test Room",
        "description": "A test room",
        "plane": "earth",
        "zone": "arkhamcity",
        "sub_zone": "northside",
        "resolved_environment": "outdoors",
        "exits": {"north": "room_002"},
        "containers": [],
    }

    room = Room(room_data)

    assert room.id == "room_001"
    assert room.name == "Test Room"
    assert room.description == "A test room"
    assert room.plane == "earth"
    assert room.zone == "arkhamcity"
    assert room.sub_zone == "northside"
    assert room.environment == "outdoors"
    assert room.exits == {"north": "room_002"}


def test_room_init_defaults():
    """Test Room initialization with minimal data."""
    room_data = {"id": "room_001"}

    room = Room(room_data)

    assert room.id == "room_001"
    assert room.name == ""
    assert room.description == ""
    assert room.plane == ""
    assert room.zone == ""
    assert room.sub_zone == ""
    assert room.environment == "outdoors"
    assert room.exits == {}


def test_room_player_entered():
    """Test Room.player_entered() adds player to room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    player_id = uuid.uuid4()

    room.player_entered(player_id)

    assert str(player_id) in room.get_players()


def test_room_player_entered_string_id():
    """Test Room.player_entered() accepts string player ID."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    player_id = str(uuid.uuid4())

    room.player_entered(player_id)

    assert player_id in room.get_players()


def test_room_player_entered_empty_id():
    """Test Room.player_entered() raises ValueError for empty ID."""
    room_data = {"id": "room_001"}
    room = Room(room_data)

    with pytest.raises(ValueError, match="Player ID cannot be empty"):
        room.player_entered("")


def test_room_add_player_silently():
    """Test Room.add_player_silently() adds player without event."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    player_id = uuid.uuid4()

    room.add_player_silently(player_id)

    assert str(player_id) in room.get_players()


def test_room_remove_player_silently():
    """Test Room.remove_player_silently() removes player without event."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    player_id = uuid.uuid4()
    room.add_player_silently(player_id)

    room.remove_player_silently(player_id)

    assert str(player_id) not in room.get_players()


def test_room_player_left():
    """Test Room.player_left() removes player and triggers event."""
    room_data = {"id": "room_001"}
    event_bus = Mock()
    room = Room(room_data, event_bus=event_bus)
    player_id = uuid.uuid4()
    room.add_player_silently(player_id)

    room.player_left(player_id)

    assert str(player_id) not in room.get_players()


def test_room_object_added():
    """Test Room.object_added() adds object to room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    object_id = "object_001"

    room.object_added(object_id)

    assert object_id in room.get_objects()


def test_room_object_removed():
    """Test Room.object_removed() removes object from room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    object_id = "object_001"
    room.object_added(object_id)

    room.object_removed(object_id)

    assert object_id not in room.get_objects()


def test_room_npc_entered():
    """Test Room.npc_entered() adds NPC to room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    npc_id = "npc_001"

    room.npc_entered(npc_id)

    assert npc_id in room.get_npcs()


def test_room_npc_left():
    """Test Room.npc_left() removes NPC from room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    npc_id = "npc_001"
    room.npc_entered(npc_id)

    room.npc_left(npc_id)

    assert npc_id not in room.get_npcs()


def test_room_get_players():
    """Test Room.get_players() returns list of player IDs."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    player_id1 = str(uuid.uuid4())
    player_id2 = str(uuid.uuid4())
    room.add_player_silently(player_id1)
    room.add_player_silently(player_id2)

    players = room.get_players()

    assert len(players) == 2
    assert player_id1 in players
    assert player_id2 in players


def test_room_get_objects():
    """Test Room.get_objects() returns list of object IDs."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    room.object_added("object_001")
    room.object_added("object_002")

    objects = room.get_objects()

    assert len(objects) == 2
    assert "object_001" in objects
    assert "object_002" in objects


def test_room_get_npcs():
    """Test Room.get_npcs() returns list of NPC IDs."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    room.npc_entered("npc_001")
    room.npc_entered("npc_002")

    npcs = room.get_npcs()

    assert len(npcs) == 2
    assert "npc_001" in npcs
    assert "npc_002" in npcs


def test_room_has_player():
    """Test Room.has_player() returns True if player in room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    player_id = uuid.uuid4()
    room.add_player_silently(player_id)

    assert room.has_player(player_id) is True


def test_room_has_player_false():
    """Test Room.has_player() returns False if player not in room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    player_id = uuid.uuid4()

    assert room.has_player(player_id) is False


def test_room_has_object():
    """Test Room.has_object() returns True if object in room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    room.object_added("object_001")

    assert room.has_object("object_001") is True


def test_room_has_npc():
    """Test Room.has_npc() returns True if NPC in room."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    room.npc_entered("npc_001")

    assert room.has_npc("npc_001") is True


def test_room_get_occupant_count():
    """Test Room.get_occupant_count() returns total occupants."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    room.add_player_silently(str(uuid.uuid4()))
    room.object_added("object_001")
    room.npc_entered("npc_001")

    count = room.get_occupant_count()

    assert count == 3


def test_room_is_empty():
    """Test Room.is_empty() returns True when no occupants."""
    room_data = {"id": "room_001"}
    room = Room(room_data)

    assert room.is_empty() is True


def test_room_is_empty_false():
    """Test Room.is_empty() returns False when occupants present."""
    room_data = {"id": "room_001"}
    room = Room(room_data)
    room.add_player_silently(str(uuid.uuid4()))

    assert room.is_empty() is False


def test_room_get_containers():
    """Test Room.get_containers() returns containers list."""
    room_data = {"id": "room_001", "containers": [{"id": "container_001"}]}
    room = Room(room_data)

    containers = room.get_containers()

    assert len(containers) == 1
    assert containers[0]["id"] == "container_001"


def test_room_to_dict():
    """Test Room.to_dict() returns room data dictionary."""
    room_data = {
        "id": "room_001",
        "name": "Test Room",
        "description": "A test room",
        "exits": {"north": "room_002"},
    }
    room = Room(room_data)
    room.add_player_silently(str(uuid.uuid4()))

    room_dict = room.to_dict()

    assert room_dict["id"] == "room_001"
    assert room_dict["name"] == "Test Room"
    assert "players" in room_dict
    assert len(room_dict["players"]) == 1


def test_room_str():
    """Test Room __str__ method."""
    room_data = {"id": "room_001", "name": "Test Room"}
    room = Room(room_data)

    room_str = str(room)

    assert "Test Room" in room_str


def test_room_repr():
    """Test Room __repr__ method."""
    room_data = {"id": "room_001", "name": "Test Room"}
    room = Room(room_data)

    repr_str = repr(room)

    assert "room_001" in repr_str
