"""
Tests for the Room model.

This module tests the Room class to ensure proper functionality of room
state tracking and event-driven operations for player, object, and NPC
movements.

As noted in the Pnakotic Manuscripts, proper testing of room awareness
is essential for maintaining the integrity of our eldritch architecture.
"""

from unittest.mock import Mock

import pytest

from server.events import EventBus
from server.models.room import Room


class TestRoomModel:
    """Test the Room model class."""

    def test_room_creation(self):
        """Test that Room can be created with proper data."""
        room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "description": "A test room for testing",
            "plane": "earth",
            "zone": "test_zone",
            "sub_zone": "test_subzone",
            "resolved_environment": "indoors",
            "exits": {"north": "test_room_002", "south": None},
        }

        room = Room(room_data)

        assert room.id == "test_room_001"
        assert room.name == "Test Room"
        assert room.description == "A test room for testing"
        assert room.plane == "earth"
        assert room.zone == "test_zone"
        assert room.sub_zone == "test_subzone"
        assert room.environment == "indoors"
        assert room.exits == {"north": "test_room_002", "south": None}

    def test_room_creation_with_defaults(self):
        """Test that Room can be created with minimal data."""
        room_data = {"id": "minimal_room"}

        room = Room(room_data)

        assert room.id == "minimal_room"
        assert room.name == ""
        assert room.description == ""
        assert room.plane == ""
        assert room.zone == ""
        assert room.sub_zone == ""
        assert room.environment == "outdoors"
        assert room.exits == {}

    def test_room_with_event_bus(self):
        """Test that Room can be created with EventBus."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)

        room = Room(room_data, event_bus)

        assert room._event_bus == event_bus

    def test_player_entered(self):
        """Test adding a player to the room."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.player_entered("player123")

        assert "player123" in room.get_players()
        assert room.has_player("player123")
        event_bus.publish.assert_called_once()

    def test_player_entered_duplicate(self):
        """Test that adding the same player twice is handled gracefully."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.player_entered("player123")
        room.player_entered("player123")  # Duplicate

        assert len(room.get_players()) == 1
        assert "player123" in room.get_players()

    def test_player_entered_empty_id(self):
        """Test that empty player ID raises ValueError."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        with pytest.raises(ValueError, match="Player ID cannot be empty"):
            room.player_entered("")

    def test_player_left(self):
        """Test removing a player from the room."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.player_entered("player123")
        room.player_left("player123")

        assert "player123" not in room.get_players()
        assert not room.has_player("player123")
        assert event_bus.publish.call_count == 2  # Enter + Leave

    def test_player_left_nonexistent(self):
        """Test that removing non-existent player is handled gracefully."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.player_left("nonexistent")

        assert len(room.get_players()) == 0
        # Should not publish event for non-existent player
        assert event_bus.publish.call_count == 0

    def test_player_left_empty_id(self):
        """Test that empty player ID raises ValueError."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        with pytest.raises(ValueError, match="Player ID cannot be empty"):
            room.player_left("")

    def test_object_added(self):
        """Test adding an object to the room."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.object_added("object123", "player456")

        assert "object123" in room.get_objects()
        assert room.has_object("object123")
        event_bus.publish.assert_called_once()

    def test_object_added_duplicate(self):
        """Test that adding the same object twice is handled gracefully."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.object_added("object123")
        room.object_added("object123")  # Duplicate

        assert len(room.get_objects()) == 1
        assert "object123" in room.get_objects()

    def test_object_added_empty_id(self):
        """Test that empty object ID raises ValueError."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        with pytest.raises(ValueError, match="Object ID cannot be empty"):
            room.object_added("")

    def test_object_removed(self):
        """Test removing an object from the room."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.object_added("object123")
        room.object_removed("object123", "player456")

        assert "object123" not in room.get_objects()
        assert not room.has_object("object123")
        assert event_bus.publish.call_count == 2  # Add + Remove

    def test_object_removed_nonexistent(self):
        """Test that removing non-existent object is handled gracefully."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.object_removed("nonexistent")

        assert len(room.get_objects()) == 0
        # Should not publish event for non-existent object
        assert event_bus.publish.call_count == 0

    def test_object_removed_empty_id(self):
        """Test that empty object ID raises ValueError."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        with pytest.raises(ValueError, match="Object ID cannot be empty"):
            room.object_removed("")

    def test_npc_entered(self):
        """Test adding an NPC to the room."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.npc_entered("npc123")

        assert "npc123" in room.get_npcs()
        assert room.has_npc("npc123")
        event_bus.publish.assert_called_once()

    def test_npc_entered_duplicate(self):
        """Test that adding the same NPC twice is handled gracefully."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.npc_entered("npc123")
        room.npc_entered("npc123")  # Duplicate

        assert len(room.get_npcs()) == 1
        assert "npc123" in room.get_npcs()

    def test_npc_entered_empty_id(self):
        """Test that empty NPC ID raises ValueError."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        with pytest.raises(ValueError, match="NPC ID cannot be empty"):
            room.npc_entered("")

    def test_npc_left(self):
        """Test removing an NPC from the room."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.npc_entered("npc123")
        room.npc_left("npc123")

        assert "npc123" not in room.get_npcs()
        assert not room.has_npc("npc123")
        assert event_bus.publish.call_count == 2  # Enter + Leave

    def test_npc_left_nonexistent(self):
        """Test that removing non-existent NPC is handled gracefully."""
        room_data = {"id": "test_room"}
        event_bus = Mock(spec=EventBus)
        room = Room(room_data, event_bus)

        room.npc_left("nonexistent")

        assert len(room.get_npcs()) == 0
        # Should not publish event for non-existent NPC
        assert event_bus.publish.call_count == 0

    def test_npc_left_empty_id(self):
        """Test that empty NPC ID raises ValueError."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        with pytest.raises(ValueError, match="NPC ID cannot be empty"):
            room.npc_left("")

    def test_get_occupant_count(self):
        """Test getting total occupant count."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        assert room.get_occupant_count() == 0

        room.player_entered("player1")
        assert room.get_occupant_count() == 1

        room.object_added("object1")
        assert room.get_occupant_count() == 2

        room.npc_entered("npc1")
        assert room.get_occupant_count() == 3

    def test_is_empty(self):
        """Test checking if room is empty."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        assert room.is_empty() is True

        room.player_entered("player1")
        assert room.is_empty() is False

        room.player_left("player1")
        assert room.is_empty() is True

    def test_to_dict(self):
        """Test converting room to dictionary."""
        room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "description": "A test room",
            "plane": "earth",
            "zone": "test_zone",
            "sub_zone": "test_subzone",
            "resolved_environment": "indoors",
            "exits": {"north": "room2"},
        }
        room = Room(room_data)

        room.player_entered("player1")
        room.object_added("object1")
        room.npc_entered("npc1")

        result = room.to_dict()

        assert result["id"] == "test_room_001"
        assert result["name"] == "Test Room"
        assert result["description"] == "A test room"
        assert result["plane"] == "earth"
        assert result["zone"] == "test_zone"
        assert result["sub_zone"] == "test_subzone"
        assert result["environment"] == "indoors"
        assert result["exits"] == {"north": "room2"}
        assert result["players"] == ["player1"]
        assert result["objects"] == ["object1"]
        assert result["npcs"] == ["npc1"]
        assert result["occupant_count"] == 3

    def test_str_representation(self):
        """Test string representation of room."""
        room_data = {"id": "test_room", "name": "Test Room"}
        room = Room(room_data)

        assert str(room) == "Room(test_room: Test Room)"

    def test_repr_representation(self):
        """Test detailed string representation of room."""
        room_data = {"id": "test_room", "name": "Test Room"}
        room = Room(room_data)

        room.player_entered("player1")
        room.object_added("object1")

        expected = "Room(id='test_room', name='Test Room', players=1, objects=1, npcs=0)"
        assert repr(room) == expected

    def test_event_publishing_without_event_bus(self):
        """Test that events are not published when no event bus is provided."""
        room_data = {"id": "test_room"}
        room = Room(room_data)  # No event bus

        # These should not raise exceptions
        room.player_entered("player1")
        room.object_added("object1")
        room.npc_entered("npc1")

        assert "player1" in room.get_players()
        assert "object1" in room.get_objects()
        assert "npc1" in room.get_npcs()

    def test_multiple_occupants(self):
        """Test room with multiple occupants of each type."""
        room_data = {"id": "test_room"}
        room = Room(room_data)

        # Add multiple players
        room.player_entered("player1")
        room.player_entered("player2")
        room.player_entered("player3")

        # Add multiple objects
        room.object_added("object1")
        room.object_added("object2")

        # Add multiple NPCs
        room.npc_entered("npc1")

        assert len(room.get_players()) == 3
        assert len(room.get_objects()) == 2
        assert len(room.get_npcs()) == 1
        assert room.get_occupant_count() == 6

        # Remove some occupants
        room.player_left("player2")
        room.object_removed("object1")
        room.npc_left("npc1")

        assert len(room.get_players()) == 2
        assert len(room.get_objects()) == 1
        assert len(room.get_npcs()) == 0
        assert room.get_occupant_count() == 3
