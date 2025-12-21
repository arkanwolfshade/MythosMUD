"""
NPC communication and event integration tests for MythosMUD.
"""

import asyncio
from datetime import UTC, datetime
from unittest.mock import MagicMock

import pytest

from server.events import PlayerEnteredRoom
from server.logging.enhanced_logging_config import get_logger
from server.models.npc import NPCDefinitionType
from server.npc.behaviors import PassiveMobNPC, ShopkeeperNPC

logger = get_logger(__name__)


@pytest.fixture
def event_bus():
    """Create an event bus for testing."""
    from server.events.event_bus import EventBus

    return EventBus()


class TestNPCEventIntegration:
    """Test NPC integration with the event system."""

    @pytest.fixture
    def mock_npc_definition(self):
        """Create a mock NPC definition for testing."""
        npc_def = MagicMock()
        npc_def.id = 4
        npc_def.name = "Event Test NPC"
        npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
        npc_def.room_id = "earth_arkhamcity_downtown_room_derby_st_001"
        npc_def.base_stats = '{"hp": 100}'
        npc_def.behavior_config = '{"wander_interval": 30}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def test_npc(self, mock_npc_definition):
        """Create a test NPC instance."""
        return PassiveMobNPC(mock_npc_definition, "event_test_npc_1")

    @pytest.mark.asyncio
    async def test_npc_event_subscription(self, event_bus) -> None:
        """Test NPC event subscription capabilities."""
        events_received = []

        def handle_player_entered(event):
            events_received.append(event)

        event_bus.subscribe(PlayerEnteredRoom, handle_player_entered)
        event = PlayerEnteredRoom(player_id="test_player_1", room_id="earth_arkhamcity_downtown_room_derby_st_001")
        # Ensure timestamp is set to a valid datetime
        event.timestamp = datetime.now(UTC)
        event_bus.publish(event)
        await asyncio.sleep(0.1)
        assert len(events_received) == 1
        assert events_received[0].player_id == "test_player_1"


class TestNPCEventReactionSystem:
    """Test the NPC event reaction system."""

    @pytest.fixture
    def event_reaction_system(self, event_bus):
        """Create an event reaction system for testing."""
        from server.npc.event_reaction_system import NPCEventReactionSystem

        return NPCEventReactionSystem(event_bus)

    @pytest.fixture
    def shopkeeper_npc_with_reactions(self, event_bus, event_reaction_system):
        """Create a shopkeeper NPC with event reactions."""
        from server.models.npc import NPCDefinition

        definition = NPCDefinition(
            name="Test Shopkeeper",
            npc_type="shopkeeper",
            sub_zone_id="test_zone",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
            base_stats='{"hp": 100, "strength": 10, "constitution": 12}',
            behavior_config='{"greeting_message": "Welcome to my shop!", "farewell_message": "Come back soon!"}',
            ai_integration_stub='{"enabled": false}',
        )
        return ShopkeeperNPC(definition, "shopkeeper_1", event_bus, event_reaction_system)

    def test_event_reaction_system_initialization(self, event_reaction_system) -> None:
        """Test that the event reaction system initializes correctly."""
        assert event_reaction_system.event_bus is not None
        assert event_reaction_system._npc_reactions == {}

    def test_register_npc_reactions(self, event_reaction_system) -> None:
        """Test registering reactions for an NPC."""
        from server.npc.event_reaction_system import NPCEventReactionTemplates

        reaction = NPCEventReactionTemplates.player_entered_room_greeting("test_npc", "Hello!")
        event_reaction_system.register_npc_reactions("test_npc", [reaction])
        assert "test_npc" in event_reaction_system._npc_reactions
        assert len(event_reaction_system._npc_reactions["test_npc"]) == 1

    @pytest.mark.asyncio
    async def test_npc_reaction_to_player_entered_room(self, event_bus, shopkeeper_npc_with_reactions) -> None:  # pylint: disable=unused-argument
        """Test that NPCs react when players enter their room."""
        events_received = []

        def capture_events(event):
            events_received.append(event)

        event_bus.subscribe(PlayerEnteredRoom, capture_events)
        player_entered_event = PlayerEnteredRoom(
            player_id="test_player_1",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
            from_room_id="earth_arkhamcity_downtown_room_derby_st_002",
        )
        player_entered_event.timestamp = datetime.now(UTC)
        event_bus.publish(player_entered_event)
        await asyncio.sleep(0.1)
        assert len(events_received) == 1
        assert events_received[0].player_id == "test_player_1"
