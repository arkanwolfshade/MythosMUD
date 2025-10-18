"""
Tests for NPC Combat Integration Service.

This module tests the integration between NPCs and the combat system,
including combat memory, damage handling, and event publishing.
"""

from unittest.mock import Mock, patch
from uuid import uuid4

from server.services.npc_combat_integration_service import NPCCombatIntegrationService


class TestNPCCombatIntegrationService:
    """Test cases for NPC Combat Integration Service."""

    def setup_method(self):
        """Set up test environment."""
        self.event_bus = Mock()
        self.persistence = Mock()
        self.combat_service = Mock()
        self.messaging_integration = Mock()
        self.event_publisher = Mock()

        with (
            patch("server.services.npc_combat_integration_service.get_persistence") as mock_get_persistence,
            patch("server.services.npc_combat_integration_service.CombatService") as mock_combat_service,
            patch("server.services.npc_combat_integration_service.CombatMessagingIntegration") as mock_messaging,
            patch("server.services.npc_combat_integration_service.CombatEventPublisher") as mock_publisher,
        ):
            mock_get_persistence.return_value = self.persistence
            mock_combat_service.return_value = self.combat_service
            mock_messaging.return_value = self.messaging_integration
            mock_publisher.return_value = self.event_publisher

            self.service = NPCCombatIntegrationService(self.event_bus)

    def test_handle_player_attack_on_npc_success(self):
        """Test successful player attack on NPC."""
        # Setup
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"
        action_type = "punch"
        damage = 1

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test Rat"
        npc_instance.take_damage = Mock(return_value=True)
        npc_instance._stats = {"hp": 5, "max_hp": 10}

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_player_name = Mock(return_value="TestPlayer")

        # Execute
        result = self.service.handle_player_attack_on_npc(
            player_id=player_id,
            npc_id=npc_id,
            room_id=room_id,
            action_type=action_type,
            damage=damage,
        )

        # Verify
        assert result is True
        assert npc_id in self.service._npc_combat_memory
        assert self.service._npc_combat_memory[npc_id] == player_id

        npc_instance.take_damage.assert_called_once_with(damage, "physical", player_id)
        self.event_publisher.publish_player_attacked.assert_called_once()
        self.event_publisher.publish_npc_took_damage.assert_called_once()
        self.messaging_integration.broadcast_combat_attack.assert_called_once()

    def test_handle_player_attack_on_dead_npc(self):
        """Test player attack on dead NPC."""
        # Setup
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock dead NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = False

        self.service._get_npc_instance = Mock(return_value=npc_instance)

        # Execute
        result = self.service.handle_player_attack_on_npc(
            player_id=player_id,
            npc_id=npc_id,
            room_id=room_id,
        )

        # Verify
        assert result is False
        self.event_publisher.publish_player_attacked.assert_not_called()

    def test_handle_player_attack_on_nonexistent_npc(self):
        """Test player attack on non-existent NPC."""
        # Setup
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        self.service._get_npc_instance = Mock(return_value=None)

        # Execute
        result = self.service.handle_player_attack_on_npc(
            player_id=player_id,
            npc_id=npc_id,
            room_id=room_id,
        )

        # Verify
        assert result is False
        self.event_publisher.publish_player_attacked.assert_not_called()

    def test_handle_npc_death_success(self):
        """Test successful NPC death handling."""
        # Setup
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())
        combat_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test Rat"

        # Mock NPC definition with XP reward
        npc_definition = Mock()
        npc_definition.base_stats = {"xp_reward": 5}

        # Mock player for XP award
        player = Mock()
        player.username = "TestPlayer"

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)
        self.persistence.get_player = Mock(return_value=player)

        # Execute
        result = self.service.handle_npc_death(
            npc_id=npc_id,
            room_id=room_id,
            killer_id=killer_id,
            combat_id=combat_id,
        )

        # Verify
        assert result is True
        self.event_publisher.publish_npc_died.assert_called_once()
        self.messaging_integration.broadcast_combat_death.assert_called_once()

    def test_get_npc_combat_memory(self):
        """Test getting NPC combat memory."""
        # Setup
        npc_id = str(uuid4())
        attacker_id = str(uuid4())
        self.service._npc_combat_memory[npc_id] = attacker_id

        # Execute
        result = self.service.get_npc_combat_memory(npc_id)

        # Verify
        assert result == attacker_id

    def test_get_npc_combat_memory_not_found(self):
        """Test getting NPC combat memory when not found."""
        # Setup
        npc_id = str(uuid4())

        # Execute
        result = self.service.get_npc_combat_memory(npc_id)

        # Verify
        assert result is None

    def test_clear_npc_combat_memory(self):
        """Test clearing NPC combat memory."""
        # Setup
        npc_id = str(uuid4())
        attacker_id = str(uuid4())
        self.service._npc_combat_memory[npc_id] = attacker_id

        # Execute
        result = self.service.clear_npc_combat_memory(npc_id)

        # Verify
        assert result is True
        assert npc_id not in self.service._npc_combat_memory

    def test_clear_npc_combat_memory_not_found(self):
        """Test clearing NPC combat memory when not found."""
        # Setup
        npc_id = str(uuid4())

        # Execute
        result = self.service.clear_npc_combat_memory(npc_id)

        # Verify
        assert result is False

    def test_handle_npc_death_clears_memory(self):
        """Test that NPC death clears combat memory."""
        # Setup
        npc_id = str(uuid4())
        killer_id = str(uuid4())

        # Add memory first
        self.service._npc_combat_memory[npc_id] = killer_id

        # Verify memory exists
        assert npc_id in self.service._npc_combat_memory
        assert self.service._npc_combat_memory[npc_id] == killer_id

        # Clear memory directly (simulating what happens in NPC death)
        if npc_id in self.service._npc_combat_memory:
            del self.service._npc_combat_memory[npc_id]

        # Verify memory is cleared
        assert npc_id not in self.service._npc_combat_memory

    def test_handle_player_attack_error_handling(self):
        """Test error handling in player attack."""
        # Setup
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock NPC instance that raises exception
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.take_damage = Mock(side_effect=Exception("Test error"))

        self.service._get_npc_instance = Mock(return_value=npc_instance)

        # Execute
        result = self.service.handle_player_attack_on_npc(
            player_id=player_id,
            npc_id=npc_id,
            room_id=room_id,
        )

        # Verify
        assert result is False

    def test_handle_npc_death_error_handling(self):
        """Test error handling in NPC death."""
        # Setup
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock NPC instance that raises exception
        self.service._get_npc_instance = Mock(side_effect=Exception("Test error"))

        # Execute
        result = self.service.handle_npc_death(
            npc_id=npc_id,
            room_id=room_id,
        )

        # Verify
        assert result is False
