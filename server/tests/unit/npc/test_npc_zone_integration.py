"""
Tests for NPC zone integration.

This module tests the integration between NPCs and the zone/sub-zone system,
including room occupancy tracking and event publishing.

As documented in the Cultes des Goules, proper zone integration is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

import asyncio

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom
from server.models.room import Room


class TestNPCZoneIntegration:
    """Test NPC integration with zone and sub-zone systems."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def arkham_downtown_room(self, event_bus):
        """Create a room in Arkham downtown."""
        room_data = {
            "id": "earth_arkhamcity_downtown_001",
            "name": "Arkham Downtown Square",
            "description": "The bustling commercial heart of Arkham",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "downtown",
            "environment": "outdoors",
            "exits": {"north": "earth_arkhamcity_downtown_002", "south": "earth_arkhamcity_downtown_003"},
        }
        return Room(room_data, event_bus)

    @pytest.fixture
    def innsmouth_waterfront_room(self, event_bus):
        """Create a room in Innsmouth waterfront."""
        room_data = {
            "id": "earth_innsmouth_waterfront_001",
            "name": "Innsmouth Waterfront",
            "description": "The decaying waterfront district",
            "plane": "earth",
            "zone": "innsmouth",
            "sub_zone": "waterfront",
            "environment": "outdoors",
            "exits": {"east": "earth_innsmouth_waterfront_002", "west": "earth_innsmouth_waterfront_003"},
        }
        return Room(room_data, event_bus)

    def test_npc_zone_based_spawning(self, arkham_downtown_room, innsmouth_waterfront_room):
        """Test that NPCs spawn based on zone and sub-zone configurations."""
        # Test Arkham downtown (should have higher spawn modifier)
        assert arkham_downtown_room.zone == "arkhamcity"
        assert arkham_downtown_room.sub_zone == "downtown"
        assert arkham_downtown_room.environment == "outdoors"

        # Test Innsmouth waterfront (should have lower spawn modifier)
        assert innsmouth_waterfront_room.zone == "innsmouth"
        assert innsmouth_waterfront_room.sub_zone == "waterfront"
        assert innsmouth_waterfront_room.environment == "outdoors"

    def test_npc_room_occupancy_tracking(self, arkham_downtown_room, event_bus):
        """Test that rooms properly track NPC occupancy."""
        # Initially empty
        assert arkham_downtown_room.is_empty() is True
        assert arkham_downtown_room.get_occupant_count() == 0
        assert arkham_downtown_room.get_npcs() == []

        # Add NPCs
        npc_id_1 = "test_npc_001"
        npc_id_2 = "test_npc_002"

        arkham_downtown_room.npc_entered(npc_id_1)
        assert arkham_downtown_room.has_npc(npc_id_1) is True
        assert arkham_downtown_room.get_occupant_count() == 1
        assert arkham_downtown_room.get_npcs() == [npc_id_1]

        arkham_downtown_room.npc_entered(npc_id_2)
        assert arkham_downtown_room.has_npc(npc_id_2) is True
        assert arkham_downtown_room.get_occupant_count() == 2
        assert set(arkham_downtown_room.get_npcs()) == {npc_id_1, npc_id_2}

        # Remove NPCs
        arkham_downtown_room.npc_left(npc_id_1)
        assert arkham_downtown_room.has_npc(npc_id_1) is False
        assert arkham_downtown_room.has_npc(npc_id_2) is True
        assert arkham_downtown_room.get_occupant_count() == 1
        assert arkham_downtown_room.get_npcs() == [npc_id_2]

        arkham_downtown_room.npc_left(npc_id_2)
        assert arkham_downtown_room.has_npc(npc_id_2) is False
        assert arkham_downtown_room.is_empty() is True
        assert arkham_downtown_room.get_occupant_count() == 0
        assert arkham_downtown_room.get_npcs() == []

    @pytest.mark.asyncio
    async def test_npc_room_event_publishing(self, arkham_downtown_room, event_bus):
        """Test that room NPC events are properly published."""
        # Track events
        events = []

        def event_handler(event):
            events.append(event)

        event_bus.subscribe(NPCEnteredRoom, event_handler)
        event_bus.subscribe(NPCLeftRoom, event_handler)

        # Add NPC
        npc_id = "test_npc_001"
        arkham_downtown_room.npc_entered(npc_id)

        # Allow event processing with proper async handling
        await asyncio.sleep(0.1)

        # Check events
        assert len(events) == 1
        assert isinstance(events[0], NPCEnteredRoom)
        assert events[0].npc_id == npc_id
        assert events[0].room_id == arkham_downtown_room.id

        # Remove NPC
        arkham_downtown_room.npc_left(npc_id)

        # Allow event processing with proper async handling
        await asyncio.sleep(0.1)

        # Check events
        assert len(events) == 2
        assert isinstance(events[1], NPCLeftRoom)
        assert events[1].npc_id == npc_id
        assert events[1].room_id == arkham_downtown_room.id

    def test_npc_room_duplicate_handling(self, arkham_downtown_room):
        """Test that rooms handle duplicate NPC entries gracefully."""
        npc_id = "test_npc_001"

        # Add NPC first time
        arkham_downtown_room.npc_entered(npc_id)
        assert arkham_downtown_room.has_npc(npc_id) is True
        assert arkham_downtown_room.get_occupant_count() == 1

        # Try to add same NPC again (should be ignored)
        arkham_downtown_room.npc_entered(npc_id)
        assert arkham_downtown_room.has_npc(npc_id) is True
        assert arkham_downtown_room.get_occupant_count() == 1  # Should still be 1

    def test_npc_room_removal_of_nonexistent(self, arkham_downtown_room):
        """Test that rooms handle removal of non-existent NPCs gracefully."""
        npc_id = "nonexistent_npc"

        # Try to remove non-existent NPC (should be ignored)
        arkham_downtown_room.npc_left(npc_id)
        assert arkham_downtown_room.has_npc(npc_id) is False
        assert arkham_downtown_room.get_occupant_count() == 0

    def test_npc_room_mixed_occupancy(self, arkham_downtown_room, event_bus):
        """Test that rooms properly track mixed occupancy (players, objects, NPCs)."""
        # Add different types of occupants
        player_id = "test_player_001"
        object_id = "test_object_001"
        npc_id = "test_npc_001"

        arkham_downtown_room.player_entered(player_id)
        arkham_downtown_room.object_added(object_id)
        arkham_downtown_room.npc_entered(npc_id)

        # Check occupancy
        assert arkham_downtown_room.get_occupant_count() == 3
        assert arkham_downtown_room.get_players() == [player_id]
        assert arkham_downtown_room.get_objects() == [object_id]
        assert arkham_downtown_room.get_npcs() == [npc_id]
        assert arkham_downtown_room.is_empty() is False

        # Remove NPC
        arkham_downtown_room.npc_left(npc_id)
        assert arkham_downtown_room.get_occupant_count() == 2
        assert arkham_downtown_room.get_npcs() == []
        assert arkham_downtown_room.has_npc(npc_id) is False

    def test_npc_room_to_dict_serialization(self, arkham_downtown_room):
        """Test that rooms properly serialize to dictionary with NPC data."""
        # Add NPCs
        npc_id_1 = "test_npc_001"
        npc_id_2 = "test_npc_002"

        arkham_downtown_room.npc_entered(npc_id_1)
        arkham_downtown_room.npc_entered(npc_id_2)

        # Serialize to dict
        room_dict = arkham_downtown_room.to_dict()

        # Check NPC data
        assert "npcs" in room_dict
        assert set(room_dict["npcs"]) == {npc_id_1, npc_id_2}
        assert room_dict["occupant_count"] == 2

        # Check other room data
        assert room_dict["id"] == arkham_downtown_room.id
        assert room_dict["name"] == arkham_downtown_room.name
        assert room_dict["zone"] == arkham_downtown_room.zone
        assert room_dict["sub_zone"] == arkham_downtown_room.sub_zone
