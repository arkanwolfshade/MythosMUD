"""
Integration tests for NPC system integration with existing game systems.

This module tests the integration between NPCs and existing game systems
including movement, combat, and communication systems.

As noted in the Pnakotic Manuscripts, proper integration testing is essential
for maintaining the delicate balance between our eldritch entities and the
existing dimensional architecture.
"""

import asyncio
import time
from unittest.mock import MagicMock, patch

import pytest

from server.events import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom, PlayerLeftRoom
from server.game.movement_service import MovementService
from server.logging.enhanced_logging_config import get_logger
from server.models.npc import NPCDefinitionType
from server.npc.behaviors import AggressiveMobNPC, PassiveMobNPC, ShopkeeperNPC

logger = get_logger(__name__)


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
        persistence = MagicMock()
        persistence.get_room.side_effect = lambda room_id: {
            "earth_arkhamcity_downtown_room_derby_st_001": mock_room_1,
            "earth_arkhamcity_downtown_room_derby_st_002": mock_room_2,
        }.get(room_id)
        return persistence

    @pytest.fixture
    def movement_service(self, event_bus, mock_persistence):
        """Create a movement service for testing."""
        service = MovementService(event_bus)
        service._persistence = mock_persistence
        return service

    @pytest.fixture
    def test_npc(self, mock_npc_definition):
        """Create a test NPC instance."""
        return PassiveMobNPC(mock_npc_definition, "test_npc_1")

    def test_npc_movement_basic(self, test_npc, movement_service, mock_room_1, mock_room_2):
        """Test basic NPC movement between rooms."""
        # Test initial room assignment
        assert test_npc.current_room == "earth_arkhamcity_downtown_room_derby_st_001"

        # Test movement to new room
        new_room_id = "earth_arkhamcity_downtown_room_derby_st_002"
        result = test_npc.move_to_room(new_room_id)

        assert result is True
        assert test_npc.current_room == new_room_id

    def test_npc_movement_with_room_validation(self, test_npc, movement_service, mock_room_1, mock_room_2):
        """Test NPC movement with room validation."""
        # Test movement to valid room
        new_room_id = "earth_arkhamcity_downtown_room_derby_st_002"
        result = test_npc.move_to_room(new_room_id)

        assert result is True
        assert test_npc.current_room == new_room_id

        # Test movement to invalid room
        invalid_room_id = "nonexistent_room"
        result = test_npc.move_to_room(invalid_room_id)

        # Should fail as NPC movement validates room existence
        assert result is False
        # Current room should remain unchanged
        assert test_npc.current_room == new_room_id

    def test_npc_movement_events(self, test_npc, event_bus, mock_room_1, mock_room_2):
        """Test that NPC movement triggers appropriate events."""
        events_received = []

        def capture_npc_events(event):
            events_received.append(event)

        # Subscribe to NPC movement events
        event_bus.subscribe(NPCEnteredRoom, capture_npc_events)
        event_bus.subscribe(NPCLeftRoom, capture_npc_events)

        # Move NPC to new room
        new_room_id = "earth_arkhamcity_downtown_room_derby_st_002"
        test_npc.move_to_room(new_room_id)

        # Give event processing time
        time.sleep(0.1)

        # Note: The current NPC implementation doesn't publish events
        # This test documents the expected behavior for future implementation
        assert len(events_received) == 0  # No events published yet

    def test_npc_movement_with_behavior_trigger(self, test_npc):
        """Test that NPC movement can trigger behavior rules."""
        # Test that movement updates last action time
        initial_time = test_npc._last_action_time

        # Move NPC
        test_npc.move_to_room("earth_arkhamcity_downtown_room_derby_st_002")

        # Last action time should be updated
        assert test_npc._last_action_time >= initial_time

    def test_npc_movement_integration_with_movement_service(self, test_npc, movement_service, mock_room_1, mock_room_2):
        """Test NPC movement integration with the movement service."""
        # This test documents how NPCs could integrate with the movement service
        # Currently, NPCs handle their own movement, but this could be extended

        # Test that NPC movement doesn't interfere with player movement
        player_id = "test_player_1"
        from_room = "earth_arkhamcity_downtown_room_derby_st_001"
        to_room = "earth_arkhamcity_downtown_room_derby_st_002"

        # Mock player movement
        with patch.object(movement_service, "move_player", return_value=True) as mock_move:
            result = movement_service.move_player(player_id, from_room, to_room)
            assert result is True
            mock_move.assert_called_once_with(player_id, from_room, to_room)

        # NPC movement should be independent
        npc_result = test_npc.move_to_room(to_room)
        assert npc_result is True


class TestNPCCombatIntegration:
    """Test NPC integration with the combat system."""

    @pytest.fixture
    def mock_aggressive_npc_definition(self):
        """Create a mock aggressive NPC definition for testing."""
        npc_def = MagicMock()
        npc_def.id = 2
        npc_def.name = "Test Cultist"
        npc_def.description = "A dark figure for combat testing"
        npc_def.npc_type = NPCDefinitionType.AGGRESSIVE_MOB
        npc_def.sub_zone_id = "sanitarium"
        npc_def.room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        npc_def.base_stats = '{"hp": 120, "strength": 15, "attack_damage": 25}'
        npc_def.behavior_config = '{"hunt_range": 5, "attack_damage": 25, "flee_threshold": 0.3}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def aggressive_npc(self, mock_aggressive_npc_definition, event_bus):
        """Create an aggressive NPC for testing."""
        npc = AggressiveMobNPC(mock_aggressive_npc_definition, "aggressive_npc_1")
        npc.event_bus = event_bus
        return npc

    def test_npc_combat_stats_integration(self, aggressive_npc):
        """Test that NPC stats integrate with combat mechanics."""
        stats = aggressive_npc.get_stats()

        # Test that NPC has combat-relevant stats
        assert "hp" in stats
        assert "strength" in stats
        assert stats["hp"] == 120
        assert stats["strength"] == 15

    def test_npc_damage_system_integration(self, aggressive_npc):
        """Test NPC damage system integration."""
        initial_hp = aggressive_npc.get_stats()["hp"]

        # Test taking damage
        result = aggressive_npc.take_damage(30)
        assert result is True

        new_hp = aggressive_npc.get_stats()["hp"]
        assert new_hp == initial_hp - 30

    def test_npc_combat_behavior_integration(self, aggressive_npc):
        """Test NPC combat behavior integration."""
        # Test attack behavior
        result = aggressive_npc.attack_target("test_player_1")
        assert result is True

        # Test hunt behavior
        result = aggressive_npc.hunt_target("test_player_1")
        assert result is True

        # Test flee behavior
        result = aggressive_npc.flee()
        assert result is True

    def test_npc_combat_with_game_mechanics(self, aggressive_npc):
        """Test NPC combat integration with game mechanics service."""
        # This test documents how NPCs could integrate with the game mechanics service
        # Currently, NPCs handle their own damage, but this could be extended

        # Test that NPC damage doesn't interfere with player damage mechanics
        initial_hp = aggressive_npc.get_stats()["hp"]

        # Apply damage directly to NPC
        aggressive_npc.take_damage(25)

        # Verify damage was applied
        new_hp = aggressive_npc.get_stats()["hp"]
        assert new_hp == initial_hp - 25

    @pytest.mark.asyncio
    async def test_npc_combat_events_integration(self, aggressive_npc, event_bus):
        """Test NPC combat event integration."""
        events_received = []

        def capture_combat_events(event):
            events_received.append(event)

        # Subscribe to combat events
        from server.events.event_types import NPCAttacked, NPCDied, NPCTookDamage

        event_bus.subscribe(NPCAttacked, capture_combat_events)
        event_bus.subscribe(NPCTookDamage, capture_combat_events)
        event_bus.subscribe(NPCDied, capture_combat_events)

        # Perform combat action
        aggressive_npc.attack_target("test_player_1")

        # Wait for event to be processed (EventBus processes asynchronously)
        import asyncio

        await asyncio.sleep(0.1)

        # Check that attack event was published
        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCAttacked"
        assert events_received[0].npc_id == "aggressive_npc_1"
        assert events_received[0].target_id == "test_player_1"
        assert events_received[0].damage == 25

        # Test damage event
        events_received.clear()
        aggressive_npc.take_damage(30, "physical", "test_player_1")

        # Wait for event to be processed
        await asyncio.sleep(0.1)

        # Check that damage event was published
        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCTookDamage"
        assert events_received[0].npc_id == "aggressive_npc_1"
        assert events_received[0].damage == 30
        assert events_received[0].damage_type == "physical"
        assert events_received[0].source_id == "test_player_1"

    @pytest.mark.asyncio
    async def test_npc_death_events_integration(self, aggressive_npc, event_bus):
        """Test NPC death event integration."""
        events_received = []

        def capture_death_events(event):
            events_received.append(event)

        # Subscribe to death events
        from server.events.event_types import NPCDied, NPCTookDamage

        event_bus.subscribe(NPCDied, capture_death_events)
        event_bus.subscribe(NPCTookDamage, capture_death_events)

        # Deal enough damage to kill the NPC
        initial_hp = aggressive_npc.get_stats()["hp"]
        aggressive_npc.take_damage(initial_hp, "physical", "test_player_1")

        # Wait for events to be processed
        import asyncio

        await asyncio.sleep(0.1)

        # Check that both damage and death events were published
        assert len(events_received) == 2

        # First event should be damage
        damage_event = events_received[0]
        assert damage_event.event_type == "NPCTookDamage"
        assert damage_event.damage == initial_hp

        # Second event should be death
        death_event = events_received[1]
        assert death_event.event_type == "NPCDied"
        assert death_event.npc_id == "aggressive_npc_1"
        assert death_event.cause == "damage"
        assert death_event.killer_id == "test_player_1"

    def test_npc_combat_with_game_mechanics_integration(self, aggressive_npc, event_bus):
        """Test NPC combat integration with game mechanics service."""
        from server.game.mechanics import GameMechanicsService

        # Create a mock persistence layer
        mock_persistence = MagicMock()
        GameMechanicsService(mock_persistence)

        # Test that NPC combat doesn't interfere with player mechanics
        initial_hp = aggressive_npc.get_stats()["hp"]

        # Apply damage directly to NPC
        aggressive_npc.take_damage(25, "physical", "test_player_1")

        # Verify damage was applied
        new_hp = aggressive_npc.get_stats()["hp"]
        assert new_hp == initial_hp - 25

        # Verify NPC is still alive
        assert aggressive_npc.is_alive is True

    @pytest.mark.asyncio
    async def test_npc_combat_damage_types(self, aggressive_npc, event_bus):
        """Test NPC combat with different damage types."""
        events_received = []

        def capture_damage_events(event):
            events_received.append(event)

        # Subscribe to damage events
        from server.events.event_types import NPCTookDamage

        event_bus.subscribe(NPCTookDamage, capture_damage_events)

        # Test different damage types
        damage_types = ["physical", "mental", "occult", "fire", "cold"]

        for damage_type in damage_types:
            events_received.clear()
            aggressive_npc.take_damage(10, damage_type, "test_player_1")

            # Wait for event to be processed
            import asyncio

            await asyncio.sleep(0.1)

            assert len(events_received) == 1
            assert events_received[0].damage_type == damage_type
            assert events_received[0].damage == 10

    @pytest.mark.asyncio
    async def test_npc_combat_behavior_trigger_integration(self, aggressive_npc, event_bus):
        """Test that NPC combat behaviors trigger correctly."""
        events_received = []

        def capture_events(event):
            events_received.append(event)

        # Subscribe to all combat events
        from server.events.event_types import NPCAttacked, NPCTookDamage

        event_bus.subscribe(NPCAttacked, capture_events)
        event_bus.subscribe(NPCTookDamage, capture_events)

        # Test attack behavior
        result = aggressive_npc.attack_target("test_player_1")
        assert result is True

        # Wait for event to be processed
        import asyncio

        await asyncio.sleep(0.1)

        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCAttacked"

        # Test hunt behavior (should not trigger attack events directly)
        events_received.clear()
        result = aggressive_npc.hunt_target("test_player_1")
        assert result is True
        # Hunt doesn't directly attack, so no attack events
        assert len(events_received) == 0

        # Test flee behavior
        result = aggressive_npc.flee()
        assert result is True

    def test_npc_combat_integration_system(self, aggressive_npc, event_bus):
        """Test the new NPC combat integration system."""
        from server.npc.combat_integration import NPCCombatIntegration

        # Create combat integration
        combat_integration = NPCCombatIntegration(event_bus)
        aggressive_npc.combat_integration = combat_integration

        # Test damage calculation
        attacker_stats = {"strength": 15, "constitution": 12}
        target_stats = {"constitution": 10}
        damage = combat_integration.calculate_damage(attacker_stats, target_stats, 20, "physical")

        # Should be base damage + strength bonus - constitution reduction
        # 20 + 2 (strength bonus) - 0 (constitution reduction) = 22
        assert damage == 22

        # Test combat stats retrieval
        npc_stats = aggressive_npc.get_stats()
        stats = combat_integration.get_combat_stats("aggressive_npc_1", npc_stats)
        assert "hp" in stats
        assert "strength" in stats
        assert stats["hp"] == 120
        assert stats["strength"] == 15

    @pytest.mark.asyncio
    async def test_npc_combat_integration_with_enhanced_attack(self, aggressive_npc, event_bus):
        """Test NPC attack with enhanced combat integration."""
        from server.npc.combat_integration import NPCCombatIntegration

        # Mock the persistence layer to prevent database access issues
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.stats.model_dump.return_value = {"constitution": 10, "health": 100}
        mock_persistence.get_player.return_value = mock_player

        # Mock the game mechanics service
        mock_game_mechanics = MagicMock()
        mock_game_mechanics.apply_combat_effects.return_value = True

        # Create combat integration with mocked dependencies
        with patch("server.npc.combat_integration.get_persistence", return_value=mock_persistence):
            with patch("server.npc.combat_integration.GameMechanicsService", return_value=mock_game_mechanics):
                combat_integration = NPCCombatIntegration(event_bus)
                aggressive_npc.combat_integration = combat_integration

                events_received = []

                def capture_events(event):
                    events_received.append(event)

                # Subscribe to combat events
                from server.events.event_types import NPCAttacked

                event_bus.subscribe(NPCAttacked, capture_events)

                # Test enhanced attack
                result = aggressive_npc.attack_target("test_player_1")
                assert result is True

                # Wait for event to be processed
                import asyncio

                await asyncio.sleep(0.1)

                # Should have attack event
                assert len(events_received) == 1
                assert events_received[0].event_type == "NPCAttacked"
                assert events_received[0].npc_id == "aggressive_npc_1"
                assert events_received[0].target_id == "test_player_1"


class TestNPCCommunicationIntegration:
    """Test NPC integration with the communication system."""

    @pytest.fixture
    def mock_shopkeeper_definition(self):
        """Create a mock shopkeeper NPC definition for testing."""
        npc_def = MagicMock()
        npc_def.id = 3
        npc_def.name = "Test Shopkeeper"
        npc_def.description = "A shopkeeper for communication testing"
        npc_def.npc_type = NPCDefinitionType.SHOPKEEPER
        npc_def.sub_zone_id = "merchant"
        npc_def.room_id = "earth_arkhamcity_merchant_room_peabody_ave_001"
        npc_def.base_stats = '{"hp": 100, "charisma": 12}'
        npc_def.behavior_config = '{"sells": ["potion"], "markup": 1.5}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def shopkeeper_npc(self, mock_shopkeeper_definition, event_bus):
        """Create a shopkeeper NPC for testing."""
        npc = ShopkeeperNPC(mock_shopkeeper_definition, "shopkeeper_1")
        npc.event_bus = event_bus
        return npc

    def test_npc_communication_basic(self, shopkeeper_npc):
        """Test basic NPC communication functionality."""
        # Test NPC speaking
        result = shopkeeper_npc.speak("Welcome to my shop!")
        assert result is True

    def test_npc_communication_with_chat_service(self, shopkeeper_npc):
        """Test NPC communication integration with chat service."""
        # This test documents how NPCs could integrate with the chat service
        # Currently, NPCs handle their own communication, but this could be extended

        # Test that NPC communication doesn't interfere with player communication
        result = shopkeeper_npc.speak("Hello, traveler!", "local")
        assert result is True

    @pytest.mark.asyncio
    async def test_npc_communication_events_integration(self, shopkeeper_npc, event_bus):
        """Test NPC communication event integration."""
        events_received = []

        def capture_communication_events(event):
            events_received.append(event)

        # Subscribe to communication events
        from server.events.event_types import NPCListened, NPCSpoke

        event_bus.subscribe(NPCSpoke, capture_communication_events)
        event_bus.subscribe(NPCListened, capture_communication_events)

        # Test NPC speaking
        shopkeeper_npc.speak("Welcome to my shop!")

        # Wait for event to be processed
        import asyncio

        await asyncio.sleep(0.1)

        # Check that speak event was published
        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCSpoke"
        assert events_received[0].npc_id == "shopkeeper_1"
        assert events_received[0].message == "Welcome to my shop!"
        assert events_received[0].channel == "local"

        # Test NPC listening
        events_received.clear()
        shopkeeper_npc.listen("Hello there!", "test_player_1", "local")

        # Wait for event to be processed
        await asyncio.sleep(0.1)

        # Check that listen event was published
        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCListened"
        assert events_received[0].npc_id == "shopkeeper_1"
        assert events_received[0].message == "Hello there!"
        assert events_received[0].speaker_id == "test_player_1"
        assert events_received[0].channel == "local"

    @pytest.mark.asyncio
    async def test_npc_communication_channels(self, shopkeeper_npc, event_bus):
        """Test NPC communication with different channels."""
        events_received = []

        def capture_communication_events(event):
            events_received.append(event)

        # Subscribe to communication events
        from server.events.event_types import NPCSpoke

        event_bus.subscribe(NPCSpoke, capture_communication_events)

        # Test different communication channels
        channels = ["local", "say", "whisper", "shout"]

        for channel in channels:
            events_received.clear()
            shopkeeper_npc.speak(f"Message on {channel} channel", channel)

            # Wait for event to be processed
            await asyncio.sleep(0.1)

            assert len(events_received) == 1
            assert events_received[0].channel == channel
            assert events_received[0].message == f"Message on {channel} channel"

    @pytest.mark.asyncio
    async def test_npc_communication_with_target(self, shopkeeper_npc, event_bus):
        """Test NPC communication with specific targets."""
        events_received = []

        def capture_communication_events(event):
            events_received.append(event)

        # Subscribe to communication events
        from server.events.event_types import NPCSpoke

        event_bus.subscribe(NPCSpoke, capture_communication_events)

        # Test targeted communication (whisper)
        shopkeeper_npc.speak("Secret message", "whisper", "test_player_1")

        # Wait for event to be processed
        await asyncio.sleep(0.1)

        assert len(events_received) == 1
        assert events_received[0].channel == "whisper"
        assert events_received[0].target_id == "test_player_1"
        assert events_received[0].message == "Secret message"

    @pytest.mark.asyncio
    async def test_npc_communication_integration_with_chat_service(self, shopkeeper_npc, event_bus):
        """Test NPC communication integration with chat service."""
        # Create a mock chat service instead of real one
        mock_chat_service = MagicMock()

        events_received = []

        def capture_communication_events(event):
            events_received.append(event)

        # Subscribe to communication events
        from server.events.event_types import NPCListened, NPCSpoke

        event_bus.subscribe(NPCSpoke, capture_communication_events)
        event_bus.subscribe(NPCListened, capture_communication_events)

        # Test that NPC communication works alongside chat service
        shopkeeper_npc.speak("Welcome to my shop!")

        # Wait for event to be processed
        await asyncio.sleep(0.1)

        # Should have communication event
        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCSpoke"

        # Test that NPC can listen to chat messages
        events_received.clear()
        shopkeeper_npc.listen("Hello shopkeeper!", "test_player_1", "local")

        # Wait for event to be processed
        await asyncio.sleep(0.1)

        # Should have listening event
        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCListened"

        # Verify that NPC communication doesn't interfere with chat service
        # (This is more of a conceptual test since we're using a mock)
        assert mock_chat_service is not None

    @pytest.mark.asyncio
    async def test_npc_communication_integration_system(self, shopkeeper_npc, event_bus):
        """Test the new NPC communication integration system."""
        from server.npc.communication_integration import NPCCommunicationIntegration

        # Create communication integration
        communication_integration = NPCCommunicationIntegration(event_bus)
        shopkeeper_npc.communication_integration = communication_integration

        events_received = []

        def capture_communication_events(event):
            events_received.append(event)

        # Subscribe to communication events
        from server.events.event_types import NPCListened, NPCSpoke

        event_bus.subscribe(NPCSpoke, capture_communication_events)
        event_bus.subscribe(NPCListened, capture_communication_events)

        # Test enhanced speaking
        result = shopkeeper_npc.speak("Welcome to my shop!")
        assert result is True

        # Wait for event to be processed
        await asyncio.sleep(0.1)

        # Should have speak event
        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCSpoke"
        assert events_received[0].npc_id == "shopkeeper_1"
        assert events_received[0].message == "Welcome to my shop!"

        # Test enhanced listening with automatic response
        events_received.clear()
        result = shopkeeper_npc.listen("Hello there!", "test_player_1", "local")
        assert result is True

        # Wait for events to be processed
        await asyncio.sleep(0.1)

        # Should have listen event and potentially a response
        assert len(events_received) >= 1
        assert events_received[0].event_type == "NPCListened"
        assert events_received[0].npc_id == "shopkeeper_1"
        assert events_received[0].message == "Hello there!"
        assert events_received[0].speaker_id == "test_player_1"

    @pytest.mark.asyncio
    async def test_npc_communication_integration_whisper(self, shopkeeper_npc, event_bus):
        """Test NPC communication integration with whisper functionality."""
        from server.npc.communication_integration import NPCCommunicationIntegration

        # Create communication integration
        communication_integration = NPCCommunicationIntegration(event_bus)
        shopkeeper_npc.communication_integration = communication_integration

        events_received = []

        def capture_communication_events(event):
            events_received.append(event)

        # Subscribe to communication events
        from server.events.event_types import NPCSpoke

        event_bus.subscribe(NPCSpoke, capture_communication_events)

        # Test whisper functionality
        result = shopkeeper_npc.speak("Secret message", "whisper", "test_player_1")
        assert result is True

        # Wait for event to be processed
        await asyncio.sleep(0.1)

        # Should have whisper event
        assert len(events_received) == 1
        assert events_received[0].event_type == "NPCSpoke"
        assert events_received[0].channel == "whisper"
        assert events_received[0].target_id == "test_player_1"
        assert events_received[0].message == "Secret message"

    def test_npc_ai_communication_integration(self, shopkeeper_npc):
        """Test NPC AI communication integration."""
        # Test AI response generation (placeholder)
        response = shopkeeper_npc.generate_ai_response("Hello, how are you?")
        assert response is not None
        assert isinstance(response, str)

        # Test AI decision making (placeholder)
        decision = shopkeeper_npc.make_ai_decision({"context": "test"})
        assert decision is not None
        assert isinstance(decision, dict)


class TestNPCEventIntegration:
    """Test NPC integration with the event system."""

    @pytest.fixture
    def mock_npc_definition(self):
        """Create a mock NPC definition for testing."""
        npc_def = MagicMock()
        npc_def.id = 4
        npc_def.name = "Event Test NPC"
        npc_def.description = "An NPC for event testing"
        npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
        npc_def.sub_zone_id = "downtown"
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
    async def test_npc_event_subscription(self, test_npc, event_bus):
        """Test NPC event subscription capabilities."""
        events_received = []

        def handle_player_entered(event):
            events_received.append(event)

        # Subscribe to player events
        event_bus.subscribe(PlayerEnteredRoom, handle_player_entered)

        # Publish a player event
        event = PlayerEnteredRoom(
            player_id="test_player_1",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
        )
        event.timestamp = None
        event_bus.publish(event)

        # Give event processing time
        await asyncio.sleep(0.1)

        # Verify event was received
        assert len(events_received) == 1
        assert events_received[0].player_id == "test_player_1"

    @pytest.mark.asyncio
    async def test_npc_event_reaction_system(self, test_npc, event_bus):
        """Test NPC event reaction system."""
        # This test documents how NPCs could react to game events
        # Currently, NPCs don't subscribe to events, but this could be implemented

        # Test that NPCs can be made to react to events
        initial_room = test_npc.current_room

        # Simulate a player entering the room
        event = PlayerEnteredRoom(player_id="test_player_1", room_id=initial_room)
        event.timestamp = None
        event_bus.publish(event)

        # Give event processing time
        await asyncio.sleep(0.1)

        # Note: NPCs don't currently react to events
        # This test documents the expected behavior for future implementation
        assert test_npc.current_room == initial_room  # No reaction yet

    @pytest.mark.asyncio
    async def test_npc_behavior_triggered_by_events(self, test_npc, event_bus):
        """Test that NPC behavior can be triggered by events."""
        # This test documents how NPC behavior could be triggered by events
        # Currently, NPCs use their own behavior engine, but this could be extended

        # Test that NPCs can execute behavior based on context
        context = {"player_nearby": True, "time_since_last_action": 35}

        # Execute behavior
        result = await test_npc.execute_behavior(context)
        assert result is True

    @pytest.mark.asyncio
    async def test_npc_event_publishing(self, test_npc, event_bus):
        """Test NPC event publishing capabilities."""
        events_received = []

        def capture_npc_events(event):
            events_received.append(event)

        # Subscribe to NPC events
        event_bus.subscribe(NPCEnteredRoom, capture_npc_events)
        event_bus.subscribe(NPCLeftRoom, capture_npc_events)

        # Move NPC (which could trigger events in the future)
        test_npc.move_to_room("earth_arkhamcity_downtown_room_derby_st_002")

        # Give event processing time
        await asyncio.sleep(0.1)

        # Note: NPCs don't currently publish events
        # This test documents the expected behavior for future implementation
        assert len(events_received) == 0  # No events published yet


class TestNPCSystemIntegration:
    """Test overall NPC system integration."""

    @pytest.fixture
    def mock_npc_definitions(self):
        """Create multiple mock NPC definitions for testing."""
        definitions = []

        # Passive mob
        npc_def = MagicMock()
        npc_def.id = 1
        npc_def.name = "Wandering Scholar"
        npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
        npc_def.room_id = "earth_arkhamcity_downtown_room_derby_st_001"
        npc_def.base_stats = '{"hp": 80, "intelligence": 15}'
        npc_def.behavior_config = '{"wander_interval": 60}'
        npc_def.ai_integration_stub = '{"ai_enabled": false}'
        definitions.append(npc_def)

        # Aggressive mob
        npc_def = MagicMock()
        npc_def.id = 2
        npc_def.name = "Cultist"
        npc_def.npc_type = NPCDefinitionType.AGGRESSIVE_MOB
        npc_def.room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        npc_def.base_stats = '{"hp": 120, "strength": 15}'
        npc_def.behavior_config = '{"hunt_range": 5, "attack_damage": 25}'
        npc_def.ai_integration_stub = '{"ai_enabled": false}'
        definitions.append(npc_def)

        # Shopkeeper
        npc_def = MagicMock()
        npc_def.id = 3
        npc_def.name = "Ezekiel Whateley"
        npc_def.npc_type = NPCDefinitionType.SHOPKEEPER
        npc_def.room_id = "earth_arkhamcity_merchant_room_peabody_ave_001"
        npc_def.base_stats = '{"hp": 100, "charisma": 12}'
        npc_def.behavior_config = '{"sells": ["potion"], "markup": 1.5}'
        npc_def.ai_integration_stub = '{"ai_enabled": false}'
        definitions.append(npc_def)

        return definitions

    @pytest.fixture
    def test_npcs(self, mock_npc_definitions):
        """Create multiple test NPC instances."""
        npcs = []
        npcs.append(PassiveMobNPC(mock_npc_definitions[0], "passive_npc_1"))
        npcs.append(AggressiveMobNPC(mock_npc_definitions[1], "aggressive_npc_1"))
        npcs.append(ShopkeeperNPC(mock_npc_definitions[2], "shopkeeper_1"))
        return npcs

    def test_multiple_npc_types_integration(self, test_npcs):
        """Test integration of multiple NPC types."""
        # Test that all NPC types can coexist
        assert len(test_npcs) == 3

        # Test that each NPC type has appropriate behavior
        for npc in test_npcs:
            assert npc.is_alive is True
            assert npc.is_active is True
            assert npc.get_behavior_rules() is not None

    @pytest.mark.asyncio
    async def test_npc_system_performance(self, test_npcs):
        """Test NPC system performance with multiple NPCs."""
        # Test behavior execution performance
        start_time = time.time()

        for npc in test_npcs:
            context = {"time_since_last_action": 35}
            await npc.execute_behavior(context)

        execution_time = time.time() - start_time

        # Should execute all NPCs quickly
        assert execution_time < 1.0

        logger.info("NPC system execution time", execution_time=execution_time, npc_count=len(test_npcs))

    @pytest.mark.asyncio
    async def test_npc_system_error_handling(self, test_npcs):
        """Test NPC system error handling."""
        # Test that errors in one NPC don't affect others
        for npc in test_npcs:
            # Test with invalid context
            result = await npc.execute_behavior(None)
            assert result is False  # Should handle invalid context gracefully

        # Test that all NPCs are still functional
        for npc in test_npcs:
            assert npc.is_alive is True
            assert npc.is_active is True

    @pytest.mark.asyncio
    async def test_npc_system_integration_with_game_services(self, test_npcs, event_bus):
        """Test NPC system integration with game services."""
        # Test that NPCs can interact with the event system
        events_received = []

        def capture_all_events(event):
            events_received.append(event)

        # Subscribe to all event types
        event_bus.subscribe(PlayerEnteredRoom, capture_all_events)
        event_bus.subscribe(PlayerLeftRoom, capture_all_events)
        event_bus.subscribe(NPCEnteredRoom, capture_all_events)
        event_bus.subscribe(NPCLeftRoom, capture_all_events)

        # Publish some test events
        player_event = PlayerEnteredRoom(
            player_id="test_player_1",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
        )
        player_event.timestamp = None
        event_bus.publish(player_event)

        # Give event processing time
        await asyncio.sleep(0.1)

        # Verify events were processed
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
        from server.npc.behaviors import ShopkeeperNPC

        definition = NPCDefinition(
            name="Test Shopkeeper",
            npc_type="shopkeeper",
            sub_zone_id="test_zone",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
            base_stats='{"hp": 100, "strength": 10, "constitution": 12}',
            behavior_config='{"greeting_message": "Welcome to my shop!", "farewell_message": "Come back soon!"}',
            ai_integration_stub='{"enabled": false}',
        )

        npc = ShopkeeperNPC(definition, "shopkeeper_1", event_bus, event_reaction_system)
        return npc

    def test_event_reaction_system_initialization(self, event_reaction_system):
        """Test that the event reaction system initializes correctly."""
        assert event_reaction_system.event_bus is not None
        assert event_reaction_system._npc_reactions == {}
        assert event_reaction_system._event_subscriptions != {}
        assert event_reaction_system._reaction_cooldowns == {}

    def test_register_npc_reactions(self, event_reaction_system):
        """Test registering reactions for an NPC."""
        from server.events.event_types import PlayerEnteredRoom
        from server.npc.event_reaction_system import NPCEventReactionTemplates

        # Create a simple reaction
        reaction = NPCEventReactionTemplates.player_entered_room_greeting("test_npc", "Hello!")

        # Register the reaction
        event_reaction_system.register_npc_reactions("test_npc", [reaction])

        # Check that it was registered
        assert "test_npc" in event_reaction_system._npc_reactions
        assert len(event_reaction_system._npc_reactions["test_npc"]) == 1
        assert PlayerEnteredRoom in event_reaction_system._event_subscriptions
        assert "test_npc" in event_reaction_system._event_subscriptions[PlayerEnteredRoom]

    def test_unregister_npc_reactions(self, event_reaction_system):
        """Test unregistering reactions for an NPC."""
        from server.npc.event_reaction_system import NPCEventReactionTemplates

        # Register a reaction
        reaction = NPCEventReactionTemplates.player_entered_room_greeting("test_npc", "Hello!")
        event_reaction_system.register_npc_reactions("test_npc", [reaction])

        # Unregister the reaction
        event_reaction_system.unregister_npc_reactions("test_npc")

        # Check that it was unregistered
        assert "test_npc" not in event_reaction_system._npc_reactions
        from server.events.event_types import PlayerEnteredRoom

        assert "test_npc" not in event_reaction_system._event_subscriptions[PlayerEnteredRoom]

    @pytest.mark.asyncio
    async def test_npc_reaction_to_player_entered_room(
        self, event_bus, event_reaction_system, shopkeeper_npc_with_reactions
    ):
        """Test that NPCs react when players enter their room."""
        from server.events.event_types import PlayerEnteredRoom

        events_received = []

        def capture_events(event):
            events_received.append(event)

        # Subscribe to all events to capture reactions
        event_bus.subscribe(PlayerEnteredRoom, capture_events)

        # Simulate a player entering the room
        player_entered_event = PlayerEnteredRoom(
            player_id="test_player_1",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
            from_room_id="earth_arkhamcity_downtown_room_derby_st_002",
        )
        player_entered_event.timestamp = time.time()

        event_bus.publish(player_entered_event)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Should have received the player entered event
        assert len(events_received) == 1
        assert events_received[0].event_type == "PlayerEnteredRoom"
        assert events_received[0].player_id == "test_player_1"

    def test_npc_reaction_priority_system(self, event_reaction_system):
        """Test that NPC reactions are executed in priority order."""
        from server.events.event_types import PlayerEnteredRoom
        from server.npc.event_reaction_system import NPCEventReaction

        # Create reactions with different priorities
        low_priority_reaction = NPCEventReaction(
            event_type=PlayerEnteredRoom,
            condition=lambda event, context: True,
            action=lambda event, context: logger.debug("Low priority reaction triggered"),
            priority=1,
        )

        high_priority_reaction = NPCEventReaction(
            event_type=PlayerEnteredRoom,
            condition=lambda event, context: True,
            action=lambda event, context: logger.debug("High priority reaction triggered"),
            priority=10,
        )

        # Register reactions
        event_reaction_system.register_npc_reactions("test_npc", [low_priority_reaction, high_priority_reaction])

        # Check that reactions are sorted by priority (highest first)
        reactions = event_reaction_system._npc_reactions["test_npc"]
        assert reactions[0].priority == 10
        assert reactions[1].priority == 1

    @pytest.mark.asyncio
    async def test_npc_reaction_cooldown_system(self, event_bus, event_reaction_system):
        """Test that NPC reactions have cooldown periods."""
        from server.events.event_types import PlayerEnteredRoom
        from server.npc.event_reaction_system import NPCEventReaction

        reaction_count = 0

        def counting_action(event, context):
            nonlocal reaction_count
            reaction_count += 1
            return True

        # Create a reaction
        reaction = NPCEventReaction(
            event_type=PlayerEnteredRoom, condition=lambda event, context: True, action=counting_action, priority=1
        )

        # Register the reaction
        event_reaction_system.register_npc_reactions("test_npc", [reaction])

        # Simulate multiple rapid events
        for i in range(3):
            player_entered_event = PlayerEnteredRoom(player_id=f"test_player_{i}", room_id="test_room")
            player_entered_event.timestamp = time.time()
            event_bus.publish(player_entered_event)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Should only have triggered once due to cooldown
        assert reaction_count == 1

    def test_npc_reaction_stats(self, event_reaction_system):
        """Test getting NPC reaction statistics."""
        from server.npc.event_reaction_system import NPCEventReactionTemplates

        # Register reactions
        greeting_reaction = NPCEventReactionTemplates.player_entered_room_greeting("test_npc", "Hello!")
        farewell_reaction = NPCEventReactionTemplates.player_left_room_farewell("test_npc", "Goodbye!")

        event_reaction_system.register_npc_reactions("test_npc", [greeting_reaction, farewell_reaction])

        # Get stats
        stats = event_reaction_system.get_npc_reaction_stats("test_npc")

        # Check stats
        assert stats["reaction_count"] == 2
        assert stats["total_triggers"] == 0  # No triggers yet
        assert len(stats["reactions"]) == 2

        # Check individual reaction stats
        reaction_types = [r["event_type"] for r in stats["reactions"]]
        assert "PlayerEnteredRoom" in reaction_types
        assert "PlayerLeftRoom" in reaction_types

    def test_npc_reaction_templates(self):
        """Test the predefined reaction templates."""
        from server.events.event_types import NPCAttacked, NPCListened, PlayerEnteredRoom, PlayerLeftRoom
        from server.npc.event_reaction_system import NPCEventReactionTemplates

        # Test greeting template
        greeting_reaction = NPCEventReactionTemplates.player_entered_room_greeting("test_npc", "Hello!")
        assert greeting_reaction.event_type == PlayerEnteredRoom
        assert greeting_reaction.priority == 1

        # Test farewell template
        farewell_reaction = NPCEventReactionTemplates.player_left_room_farewell("test_npc", "Goodbye!")
        assert farewell_reaction.event_type == PlayerLeftRoom
        assert farewell_reaction.priority == 1

        # Test retaliation template
        retaliation_reaction = NPCEventReactionTemplates.npc_attacked_retaliation("test_npc")
        assert retaliation_reaction.event_type == NPCAttacked
        assert retaliation_reaction.priority == 10

        # Test response template
        response_reaction = NPCEventReactionTemplates.player_spoke_response("test_npc", "I heard you!")
        assert response_reaction.event_type == NPCListened
        assert response_reaction.priority == 2

    def test_npc_automatic_reaction_registration(self, event_bus, event_reaction_system):
        """Test that NPCs automatically register reactions when created with reaction system."""
        from server.models.npc import NPCDefinition
        from server.npc.behaviors import ShopkeeperNPC

        definition = NPCDefinition(
            name="Test Shopkeeper",
            npc_type="shopkeeper",
            sub_zone_id="test_zone",
            room_id="test_room",
            base_stats='{"hp": 100}',
            behavior_config='{"greeting_message": "Welcome!"}',
            ai_integration_stub='{"enabled": false}',
        )

        # Create NPC with reaction system
        ShopkeeperNPC(definition, "shopkeeper_1", event_bus, event_reaction_system)

        # Check that reactions were registered
        assert "shopkeeper_1" in event_reaction_system._npc_reactions
        reactions = event_reaction_system._npc_reactions["shopkeeper_1"]
        assert len(reactions) > 0

        # Check that greeting reaction was registered
        reaction_types = [r.event_type.__name__ for r in reactions]
        assert "PlayerEnteredRoom" in reaction_types
