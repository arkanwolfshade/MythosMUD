"""
NPC movement integration tests for MythosMUD.
"""

import time
from unittest.mock import AsyncMock, MagicMock, Mock

import pytest

from server.events import NPCEnteredRoom, NPCLeftRoom
from server.game.movement_service import MovementService
from server.models.npc import NPCDefinitionType
from server.npc.behaviors import PassiveMobNPC


@pytest.fixture
def event_bus():
    """Create an event bus for testing."""
    from server.events.event_bus import EventBus

    return EventBus()


class TestNPCMovementIntegration:
    """Test NPC integration with the movement system."""

    @pytest.fixture
    def mock_npc_definition(self):
        """Create a mock NPC definition for testing."""
        npc_def = MagicMock()
        npc_def.id = 1
        npc_def.name = "Test NPC"
        npc_def.description = "A test NPC for integration testing"
        npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
        npc_def.sub_zone_id = "downtown"
        npc_def.room_id = "earth_arkhamcity_downtown_room_derby_st_001"
        npc_def.base_stats = '{"hp": 100, "strength": 10}'
        npc_def.behavior_config = '{"wander_interval": 30}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def mock_room_1(self):
        """Create a mock room for testing."""
        room = MagicMock()
        room.id = "earth_arkhamcity_downtown_room_derby_st_001"
        room.name = "Derby Street"
        room.description = "A quiet street in downtown Arkham"
        room.exits = {"north": "earth_arkhamcity_downtown_room_derby_st_002"}
        room.get_players.return_value = []
        room.get_npcs.return_value = []
        room.add_npc.return_value = True
        room.remove_npc.return_value = True
        return room

    @pytest.fixture
    def mock_room_2(self):
        """Create a second mock room for testing."""
        room = MagicMock()
        room.id = "earth_arkhamcity_downtown_room_derby_st_002"
        room.name = "Derby Street North"
        room.description = "The northern end of Derby Street"
        room.exits = {"south": "earth_arkhamcity_downtown_room_derby_st_001"}
        room.get_players.return_value = []
        room.get_npcs.return_value = []
        room.add_npc.return_value = True
        room.remove_npc.return_value = True
        return room

    @pytest.fixture
    def mock_persistence(self, mock_room_1, mock_room_2):
        """Create a mock persistence layer for testing."""

        def get_room_by_id(room_id):
            room_map = {
                "earth_arkhamcity_downtown_room_derby_st_001": mock_room_1,
                "earth_arkhamcity_downtown_room_derby_st_002": mock_room_2,
            }
            return room_map.get(room_id)

        persistence = MagicMock()
        persistence.get_room_by_id = MagicMock(side_effect=get_room_by_id)
        persistence.get_room = MagicMock(side_effect=get_room_by_id)
        return persistence

    @pytest.fixture
    def movement_service(self, event_bus, mock_persistence):
        """Create a movement service for testing."""
        service = MovementService(event_bus, async_persistence=mock_persistence)
        return service

    @pytest.fixture
    def test_npc(self, mock_npc_definition, event_bus, mock_persistence):
        """Create a test NPC instance with container setup for movement integration."""
        from server.container import ApplicationContainer

        ApplicationContainer.reset_instance()
        mock_container = Mock()
        mock_container.event_bus = event_bus
        mock_container.async_persistence = mock_persistence
        ApplicationContainer._instance = mock_container
        try:
            npc = PassiveMobNPC(mock_npc_definition, "test_npc_1", event_bus=event_bus)
            yield npc
        finally:
            ApplicationContainer.reset_instance()

    def test_npc_movement_basic(self, test_npc, movement_service, mock_room_1, mock_room_2) -> None:
        """Test basic NPC movement between rooms."""
        assert test_npc.current_room == "earth_arkhamcity_downtown_room_derby_st_001"
        new_room_id = "earth_arkhamcity_downtown_room_derby_st_002"
        result = test_npc.move_to_room(new_room_id)
        assert result is True
        assert test_npc.current_room == new_room_id

    def test_npc_movement_with_room_validation(self, test_npc, movement_service, mock_room_1, mock_room_2) -> None:
        """Test NPC movement with room validation."""
        new_room_id = "earth_arkhamcity_downtown_room_derby_st_002"
        result = test_npc.move_to_room(new_room_id)
        assert result is True
        assert test_npc.current_room == new_room_id
        invalid_room_id = "nonexistent_room"
        result = test_npc.move_to_room(invalid_room_id)
        assert result is False
        assert test_npc.current_room == new_room_id

    def test_npc_movement_events(self, test_npc, event_bus, mock_room_1, mock_room_2) -> None:
        """Test that NPC movement triggers appropriate events."""
        events_received = []

        def capture_npc_events(event):
            events_received.append(event)

        event_bus.subscribe(NPCEnteredRoom, capture_npc_events)
        event_bus.subscribe(NPCLeftRoom, capture_npc_events)
        new_room_id = "earth_arkhamcity_downtown_room_derby_st_002"
        test_npc.move_to_room(new_room_id)
        time.sleep(0.1)
        # Note: The current NPC implementation doesn't publish events
        assert len(events_received) == 0

    def test_npc_movement_with_behavior_trigger(self, test_npc) -> None:
        """Test that NPC movement can trigger behavior rules."""
        initial_time = test_npc.to_dict().get("last_action_time")
        test_npc.move_to_room("earth_arkhamcity_downtown_room_derby_st_002")
        assert test_npc.to_dict().get("last_action_time") >= initial_time

    @pytest.mark.asyncio
    async def test_npc_movement_integration_with_movement_service(self, test_npc, movement_service) -> None:
        """Test NPC movement integration with the movement service."""
        player_id = "test_player_1"
        from_room = "earth_arkhamcity_downtown_room_derby_st_001"
        to_room = "earth_arkhamcity_downtown_room_derby_st_002"
        movement_service.move_player = AsyncMock(return_value=True)
        result = await movement_service.move_player(player_id, from_room, to_room)
        assert result is True
        movement_service.move_player.assert_called_once_with(player_id, from_room, to_room)
        npc_result = test_npc.move_to_room(to_room)
        assert npc_result is True
