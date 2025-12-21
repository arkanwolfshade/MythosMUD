"""
Tests for NPC Combat Integration Service.

This module tests the integration between NPCs and the combat system,
including combat memory, damage handling, and event publishing.
"""

from typing import Any
from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.services.npc_combat_integration_service import NPCCombatIntegrationService


class TestNPCCombatIntegrationService:
    """Test cases for NPC Combat Integration Service."""

    # Type annotations for instance attributes (satisfies linter without requiring __init__)
    # Attributes are initialized in setup_method() per pytest best practices
    event_bus: Mock
    persistence: Mock
    combat_service: AsyncMock
    messaging_integration: Mock
    event_publisher: Mock
    mock_npc_instance_service: Mock
    npc_service_patcher: Any
    mock_get_service: Mock
    service: NPCCombatIntegrationService

    def setup_method(self) -> None:
        """Set up test environment."""
        self.event_bus = Mock()
        self.persistence = Mock()
        self.persistence.get_player_by_id = AsyncMock(return_value=None)
        self.combat_service = AsyncMock()
        # Mock the combat result object
        mock_combat_result = Mock()
        mock_combat_result.success = True
        mock_combat_result.combat_id = "test_combat_123"
        mock_combat_result.combat_ended = False
        mock_combat_result.message = True  # Set message to True for successful attack
        self.combat_service.process_attack.return_value = mock_combat_result
        # Mock the player combats dictionary
        self.combat_service._player_combats = {}
        self.messaging_integration = Mock()
        self.messaging_integration.broadcast_combat_attack = AsyncMock(return_value=True)
        self.event_publisher = Mock()

        # Mock NPC instance service to avoid initialization errors
        self.mock_npc_instance_service = Mock()
        self.mock_npc_instance_service.lifecycle_manager = Mock()
        self.mock_npc_instance_service.lifecycle_manager.active_npcs = {}

        # Patch get_npc_instance_service before creating the service
        self.npc_service_patcher = patch("server.services.npc_instance_service.get_npc_instance_service")
        self.mock_get_service = self.npc_service_patcher.start()
        self.mock_get_service.return_value = self.mock_npc_instance_service

        with (
            patch("server.services.npc_combat_integration_service.CombatService") as mock_combat_service,
            patch("server.services.npc_combat_integration_service.CombatMessagingIntegration") as mock_messaging,
            patch("server.services.npc_combat_integration_service.CombatEventPublisher") as mock_publisher,
        ):
            mock_combat_service.return_value = self.combat_service
            mock_messaging.return_value = self.messaging_integration
            mock_publisher.return_value = self.event_publisher

            self.service = NPCCombatIntegrationService(
                event_bus=self.event_bus,
                combat_service=self.combat_service,
                async_persistence=self.persistence,
            )

    def teardown_method(self) -> None:
        """Clean up test environment."""
        if hasattr(self, "npc_service_patcher"):
            self.npc_service_patcher.stop()

    @pytest.mark.asyncio
    async def test_handle_player_attack_on_npc_success(self) -> None:
        """Test successful player attack on NPC."""
        # Setup
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"
        action_type = "punch"
        damage = 1

        # Mock player with proper room ID
        mock_player = Mock()
        mock_player.current_room_id = room_id
        mock_player.get_stats.return_value = {"current_health": 100, "max_health": 100, "dexterity": 10}
        self.persistence.get_player.return_value = mock_player
        self.persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        # Mock NPC instance with proper room ID
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test Rat"
        npc_instance.take_damage = Mock(return_value=True)
        npc_instance._stats = {"hp": 5, "max_hp": 10}
        npc_instance.get_stats.return_value = {"hp": 5, "max_hp": 10, "dexterity": 10}
        npc_instance.current_room = room_id  # Set the room ID to match player
        npc_instance.room_id = room_id  # Also set room_id for compatibility

        # Set up NPC instance in mock service's active_npcs
        self.mock_npc_instance_service.lifecycle_manager.active_npcs[npc_id] = npc_instance

        # Type ignore: Dynamic attribute assignment for testing purposes
        self.service._get_player_name = AsyncMock(return_value="TestPlayer")  # type: ignore[attr-defined]
        self.service._get_player_room_id = AsyncMock(return_value=room_id)  # type: ignore[attr-defined]

        # Execute
        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id,
            npc_id=npc_id,
            room_id=room_id,
            action_type=action_type,
            damage=damage,
        )

        # Verify
        assert result is True
        assert self.service.get_npc_combat_memory(npc_id) == player_id

        # Verify combat service was called
        self.combat_service.process_attack.assert_called_once()
        self.messaging_integration.broadcast_combat_attack.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_attack_on_dead_npc(self) -> None:
        """Test player attack on dead NPC."""
        # Setup
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock dead NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = False

        # Set up NPC instance in mock service's active_npcs
        self.mock_npc_instance_service.lifecycle_manager.active_npcs[npc_id] = npc_instance

        # Execute
        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id,
            npc_id=npc_id,
            room_id=room_id,
        )

        # Verify
        assert result is False
        self.event_publisher.publish_player_attacked.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_player_attack_on_nonexistent_npc(self) -> None:
        """Test player attack on non-existent NPC."""
        # Setup
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Don't add NPC to active_npcs to simulate NPC not found

        # Execute
        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id,
            npc_id=npc_id,
            room_id=room_id,
        )

        # Verify
        assert result is False
        self.event_publisher.publish_player_attacked.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_npc_death_success(self) -> None:
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
        npc_definition.get_base_stats.return_value = {"xp_value": 5}  # Changed from xp_reward to xp_value

        # Mock player for XP award
        player = Mock()
        player.username = "TestPlayer"

        # Mock game mechanics service
        game_mechanics = Mock()
        game_mechanics.gain_experience.return_value = (True, "XP awarded")
        self.persistence.get_game_mechanics_service = AsyncMock(return_value=game_mechanics)

        # Set up NPC instance in mock service's active_npcs
        self.mock_npc_instance_service.lifecycle_manager.active_npcs[npc_id] = npc_instance

        # Mock NPC definition lookup through data provider
        async def mock_get_npc_definition(_npc_id):
            return npc_definition

        # Type ignore: Method assignment for testing purposes (mocking internal methods)
        self.service._data_provider.get_npc_definition = mock_get_npc_definition  # type: ignore[method-assign]

        # Mock rewards handler to return XP reward
        self.service._rewards.calculate_xp_reward = AsyncMock(return_value=5)  # type: ignore[method-assign]
        self.service._rewards.award_xp_to_killer = AsyncMock(return_value=True)  # type: ignore[method-assign]

        # Mock lifecycle handler
        self.service._lifecycle.despawn_npc_safely = AsyncMock(return_value=True)  # type: ignore[method-assign]

        # Execute
        result = await self.service.handle_npc_death(
            npc_id=npc_id,
            room_id=room_id,
            killer_id=killer_id,
            combat_id=combat_id,
        )

        # Verify
        assert result is True
        # Note: publish_npc_died and broadcast_combat_death are handled by CombatService, not in handle_npc_death

    def test_get_npc_combat_memory(self) -> None:
        """Test getting NPC combat memory."""
        # Setup
        npc_id = str(uuid4())
        attacker_id = str(uuid4())
        self.service._combat_memory.record_attack(npc_id, attacker_id)

        # Execute
        result = self.service.get_npc_combat_memory(npc_id)

        # Verify
        assert result == attacker_id

    def test_get_npc_combat_memory_not_found(self) -> None:
        """Test getting NPC combat memory when not found."""
        # Setup
        npc_id = str(uuid4())

        # Execute
        result = self.service.get_npc_combat_memory(npc_id)

        # Verify
        assert result is None

    def test_clear_npc_combat_memory(self) -> None:
        """Test clearing NPC combat memory."""
        # Setup
        npc_id = str(uuid4())
        attacker_id = str(uuid4())
        self.service._combat_memory.record_attack(npc_id, attacker_id)

        # Execute
        result = self.service.clear_npc_combat_memory(npc_id)

        # Verify
        assert result is True
        assert self.service.get_npc_combat_memory(npc_id) is None

    def test_clear_npc_combat_memory_not_found(self) -> None:
        """Test clearing NPC combat memory when not found."""
        # Setup
        npc_id = str(uuid4())

        # Execute
        result = self.service.clear_npc_combat_memory(npc_id)

        # Verify
        assert result is False

    def test_handle_npc_death_clears_memory(self) -> None:
        """Test that NPC death clears combat memory."""
        # Setup
        npc_id = str(uuid4())
        killer_id = str(uuid4())

        # Add memory first
        self.service._combat_memory.record_attack(npc_id, killer_id)

        # Verify memory exists
        assert self.service.get_npc_combat_memory(npc_id) == killer_id

        # Clear memory directly (simulating what happens in NPC death)
        self.service._combat_memory.clear_memory(npc_id)

        # Verify memory is cleared
        assert self.service.get_npc_combat_memory(npc_id) is None

    @pytest.mark.asyncio
    async def test_handle_player_attack_error_handling(self) -> None:
        """Test error handling in player attack."""
        # Setup
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock NPC instance that raises exception when get_stats is called
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test NPC"
        npc_instance.get_stats = Mock(side_effect=Exception("Test error"))

        # Set up NPC instance in mock service's active_npcs
        self.mock_npc_instance_service.lifecycle_manager.active_npcs[npc_id] = npc_instance

        # Execute
        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id,
            npc_id=npc_id,
            room_id=room_id,
        )

        # Verify
        assert result is False

    @pytest.mark.asyncio
    async def test_handle_npc_death_error_handling(self) -> None:
        """Test error handling in NPC death."""
        # Setup
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Don't add NPC to active_npcs to simulate NPC not found error
        # This will cause get_npc_instance to return None

        # Execute
        result = await self.service.handle_npc_death(
            npc_id=npc_id,
            room_id=room_id,
        )

        # Verify
        assert result is False
