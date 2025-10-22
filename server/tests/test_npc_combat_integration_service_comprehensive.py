"""
Comprehensive tests for NPC Combat Integration Service.

This module provides additional test coverage for the NPC combat integration
service to improve coverage from 69% to 80%+.
"""

from unittest.mock import AsyncMock, Mock, patch
from uuid import UUID, uuid4

import pytest

from server.services.npc_combat_integration_service import NPCCombatIntegrationService


class TestNPCCombatIntegrationServiceComprehensive:
    """Comprehensive test cases for NPC Combat Integration Service."""

    def setup_method(self):
        """Set up test environment."""
        self.event_bus = Mock()
        self.persistence = Mock()
        self.combat_service = AsyncMock()
        self.messaging_integration = Mock()
        self.event_publisher = Mock()

        # Mock combat result
        self.mock_combat_result = Mock()
        self.mock_combat_result.success = True
        self.mock_combat_result.combat_id = uuid4()
        self.mock_combat_result.combat_ended = False
        self.mock_combat_result.message = "Attack successful"
        self.combat_service.process_attack.return_value = self.mock_combat_result
        self.combat_service._player_combats = {}

        with (
            patch("server.services.npc_combat_integration_service.get_persistence") as mock_get_persistence,
            patch("server.services.npc_combat_integration_service.CombatService") as mock_combat_service,
            patch("server.services.npc_combat_integration_service.CombatMessagingIntegration") as mock_messaging,
            patch("server.services.npc_combat_integration_service.CombatEventPublisher") as mock_publisher,
            patch("server.app.lifespan.get_current_tick") as mock_tick,
        ):
            mock_get_persistence.return_value = self.persistence
            mock_combat_service.return_value = self.combat_service
            mock_messaging.return_value = self.messaging_integration
            mock_publisher.return_value = self.event_publisher
            mock_tick.return_value = 100

            self.service = NPCCombatIntegrationService(self.event_bus, self.combat_service)

    @pytest.mark.asyncio
    async def test_handle_player_attack_existing_combat(self):
        """Test player attack when combat already exists."""
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock existing combat
        self.combat_service._player_combats[UUID(player_id)] = "existing_combat_id"

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test NPC"
        npc_instance.get_stats.return_value = {"hp": 50, "max_hp": 100, "dexterity": 10}

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_player_name = Mock(return_value="TestPlayer")

        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id, npc_id=npc_id, room_id=room_id, damage=15
        )

        assert result == "Attack successful"
        self.combat_service.process_attack.assert_called_once()
        self.messaging_integration.broadcast_combat_attack.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_attack_new_combat(self):
        """Test player attack starting new combat."""
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test NPC"
        npc_instance.get_stats.return_value = {"hp": 50, "max_hp": 100, "dexterity": 10}

        # Mock player
        player = Mock()
        player.name = "TestPlayer"
        self.persistence.get_player.return_value = player

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_player_name = Mock(return_value="TestPlayer")

        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id, npc_id=npc_id, room_id=room_id, damage=15
        )

        assert result == "Attack successful"
        self.combat_service.start_combat.assert_called_once()
        self.combat_service.process_attack.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_attack_combat_ended(self):
        """Test player attack when combat ends."""
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock combat result with combat ended
        self.mock_combat_result.combat_ended = True

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test NPC"
        npc_instance.get_stats.return_value = {"hp": 0, "max_hp": 100, "dexterity": 10}

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_player_name = Mock(return_value="TestPlayer")
        self.service.handle_npc_death = Mock(return_value=True)

        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id, npc_id=npc_id, room_id=room_id, damage=15
        )

        assert result == "Attack successful"
        self.service.handle_npc_death.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_attack_combat_failed(self):
        """Test player attack when combat fails."""
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock failed combat result
        self.mock_combat_result.success = False
        self.mock_combat_result.message = "Combat failed"

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test NPC"
        npc_instance.get_stats.return_value = {"hp": 50, "max_hp": 100, "dexterity": 10}

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_player_name = Mock(return_value="TestPlayer")

        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id, npc_id=npc_id, room_id=room_id, damage=15
        )

        assert result == "Combat failed"
        self.messaging_integration.broadcast_combat_attack.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_player_attack_invalid_uuid(self):
        """Test player attack with invalid UUID strings."""
        player_id = "invalid_uuid"
        npc_id = "invalid_uuid"
        room_id = "test_room_001"

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test NPC"
        npc_instance.get_stats.return_value = {"hp": 50, "max_hp": 100, "dexterity": 10}

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_player_name = Mock(return_value="TestPlayer")

        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id, npc_id=npc_id, room_id=room_id, damage=15
        )

        assert result == "Attack successful"
        self.combat_service.start_combat.assert_called_once()

    def test_handle_npc_death_with_xp_reward(self):
        """Test NPC death with XP reward."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())
        combat_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        # Mock NPC definition with XP reward
        npc_definition = Mock()
        npc_definition.base_stats = {"xp_reward": 10}

        # Mock player
        player = Mock()
        player.stats.experience_points = 100

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)
        self.persistence.get_player.return_value = player

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id, combat_id=combat_id)

        assert result is True
        self.event_publisher.publish_npc_died.assert_called_once()
        self.messaging_integration.broadcast_combat_death.assert_called_once()

    def test_handle_npc_death_with_game_mechanics_service(self):
        """Test NPC death with game mechanics service."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        # Mock NPC definition with XP reward
        npc_definition = Mock()
        npc_definition.base_stats = {"xp_reward": 15}

        # Mock player
        player = Mock()

        # Mock game mechanics service
        game_mechanics = Mock()
        game_mechanics.gain_experience.return_value = (True, "XP awarded")

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)
        self.persistence.get_player.return_value = player
        self.persistence.get_game_mechanics_service = Mock(return_value=game_mechanics)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True
        game_mechanics.gain_experience.assert_called_once_with(killer_id, 15, f"killed_{npc_id}")

    def test_handle_npc_death_with_failed_xp_award(self):
        """Test NPC death with failed XP award."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        # Mock NPC definition with XP reward
        npc_definition = Mock()
        npc_definition.base_stats = {"xp_reward": 20}

        # Mock player
        player = Mock()

        # Mock game mechanics service that fails
        game_mechanics = Mock()
        game_mechanics.gain_experience.return_value = (False, "XP award failed")

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)
        self.persistence.get_player.return_value = player
        self.persistence.get_game_mechanics_service = Mock(return_value=game_mechanics)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True
        # Should still handle death even if XP award fails

    def test_handle_npc_death_with_fallback_xp_award(self):
        """Test NPC death with fallback XP award."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        # Mock NPC definition with XP reward
        npc_definition = Mock()
        npc_definition.base_stats = {"xp_reward": 25}

        # Mock player with stats object
        player = Mock()
        player.stats.experience_points = 50

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)
        self.persistence.get_player.return_value = player
        # No game mechanics service available
        self.persistence.get_game_mechanics_service = Mock(return_value=None)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True
        # Verify that save_player was called (indicating XP was awarded)
        self.persistence.save_player.assert_called_once_with(player)

    def test_handle_npc_death_without_killer(self):
        """Test NPC death without killer."""
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=None)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id)

        assert result is True
        self.event_publisher.publish_npc_died.assert_called_once()

    def test_handle_npc_death_with_invalid_combat_id(self):
        """Test NPC death with invalid combat ID."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())
        combat_id = "invalid_uuid"

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=None)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id, combat_id=combat_id)

        assert result is True
        self.event_publisher.publish_npc_died.assert_called_once()

    def test_handle_npc_death_clears_memory(self):
        """Test that NPC death clears combat memory."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Add memory first
        self.service._npc_combat_memory[npc_id] = killer_id

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=None)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True
        assert npc_id not in self.service._npc_combat_memory

    def test_get_npc_instance_success(self):
        """Test getting NPC instance successfully."""
        npc_id = str(uuid4())

        # Mock NPC instance service
        npc_instance_service = Mock()
        spawning_service = Mock()
        npc_instance = Mock()
        spawning_service.active_npc_instances = {npc_id: npc_instance}
        npc_instance_service.spawning_service = spawning_service

        with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
            mock_get_service.return_value = npc_instance_service

            result = self.service._get_npc_instance(npc_id)

            assert result == npc_instance

    def test_get_npc_instance_not_found(self):
        """Test getting NPC instance when not found."""
        npc_id = str(uuid4())

        # Mock NPC instance service
        npc_instance_service = Mock()
        spawning_service = Mock()
        spawning_service.active_npc_instances = {}
        npc_instance_service.spawning_service = spawning_service

        with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
            mock_get_service.return_value = npc_instance_service

            result = self.service._get_npc_instance(npc_id)

            assert result is None

    def test_get_npc_instance_exception(self):
        """Test getting NPC instance with exception."""
        npc_id = str(uuid4())

        with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
            mock_get_service.side_effect = Exception("Service error")

            result = self.service._get_npc_instance(npc_id)

            assert result is None

    def test_get_npc_definition_success(self):
        """Test getting NPC definition successfully."""
        npc_id = str(uuid4())

        # Mock lifecycle manager
        lifecycle_manager = Mock()
        lifecycle_record = Mock()
        lifecycle_record.definition = Mock()
        lifecycle_manager.lifecycle_records = {npc_id: lifecycle_record}

        self.persistence.get_npc_lifecycle_manager = Mock(return_value=lifecycle_manager)

        result = self.service._get_npc_definition(npc_id)

        assert result == lifecycle_record.definition

    def test_get_npc_definition_not_found(self):
        """Test getting NPC definition when not found."""
        npc_id = str(uuid4())

        # Mock lifecycle manager
        lifecycle_manager = Mock()
        lifecycle_manager.lifecycle_records = {}

        self.persistence.get_npc_lifecycle_manager = Mock(return_value=lifecycle_manager)

        result = self.service._get_npc_definition(npc_id)

        assert result is None

    def test_get_npc_definition_exception(self):
        """Test getting NPC definition with exception."""
        npc_id = str(uuid4())

        self.persistence.get_npc_lifecycle_manager = Mock(side_effect=Exception("Service error"))

        result = self.service._get_npc_definition(npc_id)

        assert result is None

    def test_get_player_name_success(self):
        """Test getting player name successfully."""
        player_id = str(uuid4())
        player_name = "TestPlayer"

        player = Mock()
        player.name = player_name
        self.persistence.get_player.return_value = player

        result = self.service._get_player_name(player_id)

        assert result == player_name

    def test_get_player_name_not_found(self):
        """Test getting player name when player not found."""
        player_id = str(uuid4())

        self.persistence.get_player.return_value = None

        result = self.service._get_player_name(player_id)

        assert result == "Unknown Player"

    def test_get_player_name_exception(self):
        """Test getting player name with exception."""
        player_id = str(uuid4())

        self.persistence.get_player.side_effect = Exception("Database error")

        result = self.service._get_player_name(player_id)

        assert result == "Unknown Player"

    def test_despawn_npc_lifecycle_manager(self):
        """Test despawning NPC with lifecycle manager."""
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock lifecycle manager
        lifecycle_manager = Mock()
        self.persistence.get_npc_lifecycle_manager = Mock(return_value=lifecycle_manager)

        self.service._despawn_npc(npc_id, room_id)

        lifecycle_manager.record_npc_death.assert_called_once_with(npc_id)
        lifecycle_manager.despawn_npc.assert_called_once_with(npc_id, "combat_death")

    def test_despawn_npc_spawning_service(self):
        """Test despawning NPC with spawning service fallback."""
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock spawning service
        spawning_service = Mock()
        spawning_service.active_npc_instances = {npc_id: Mock()}
        self.persistence.get_npc_lifecycle_manager = Mock(return_value=None)
        self.persistence.get_npc_spawning_service = Mock(return_value=spawning_service)

        self.service._despawn_npc(npc_id, room_id)

        assert npc_id not in spawning_service.active_npc_instances

    def test_despawn_npc_exception(self):
        """Test despawning NPC with exception."""
        npc_id = str(uuid4())
        room_id = "test_room_001"

        self.persistence.get_npc_lifecycle_manager = Mock(side_effect=Exception("Service error"))

        # Should not raise exception
        self.service._despawn_npc(npc_id, room_id)

    def test_is_valid_uuid_valid(self):
        """Test UUID validation with valid UUID."""
        valid_uuid = str(uuid4())

        result = self.service._is_valid_uuid(valid_uuid)

        assert result is True

    def test_is_valid_uuid_invalid(self):
        """Test UUID validation with invalid UUID."""
        invalid_uuid = "not_a_uuid"

        result = self.service._is_valid_uuid(invalid_uuid)

        assert result is False

    def test_is_valid_uuid_empty(self):
        """Test UUID validation with empty string."""
        empty_string = ""

        result = self.service._is_valid_uuid(empty_string)

        assert result is False


class TestNPCCombatIntegrationServiceEdgeCases:
    """Test edge cases for NPC Combat Integration Service."""

    def setup_method(self):
        """Set up test environment."""
        self.event_bus = Mock()
        self.persistence = Mock()
        self.combat_service = AsyncMock()
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

            self.service = NPCCombatIntegrationService(self.event_bus, self.combat_service)

    @pytest.mark.asyncio
    async def test_handle_player_attack_with_exception_during_combat(self):
        """Test player attack with exception during combat processing."""
        player_id = str(uuid4())
        npc_id = str(uuid4())
        room_id = "test_room_001"

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.is_alive = True
        npc_instance.name = "Test NPC"
        npc_instance.get_stats.return_value = {"hp": 50, "max_hp": 100, "dexterity": 10}

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_player_name = Mock(return_value="TestPlayer")

        # Mock exception during combat processing
        self.combat_service.process_attack.side_effect = Exception("Combat error")

        result = await self.service.handle_player_attack_on_npc(
            player_id=player_id, npc_id=npc_id, room_id=room_id, damage=15
        )

        assert result is False

    def test_handle_npc_death_with_xp_award_exception(self):
        """Test NPC death with exception during XP award."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        # Mock NPC definition with XP reward
        npc_definition = Mock()
        npc_definition.base_stats = {"xp_reward": 30}

        # Mock player
        player = Mock()

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)
        self.persistence.get_player.return_value = player
        self.persistence.get_game_mechanics_service = Mock(side_effect=Exception("Service error"))

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True  # Should still handle death even if XP award fails

    def test_handle_npc_death_with_non_dict_base_stats(self):
        """Test NPC death with non-dict base stats."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        # Mock NPC definition with non-dict base stats
        npc_definition = Mock()
        npc_definition.base_stats = "not_a_dict"

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True

    def test_handle_npc_death_with_no_xp_reward_key(self):
        """Test NPC death with base stats missing xp_reward key."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        # Mock NPC definition without xp_reward
        npc_definition = Mock()
        npc_definition.base_stats = {"hp": 100}

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True

    def test_handle_npc_death_with_zero_xp_reward(self):
        """Test NPC death with zero XP reward."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        # Mock NPC definition with zero XP reward
        npc_definition = Mock()
        npc_definition.base_stats = {"xp_reward": 0}

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=npc_definition)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True
        # Should not attempt XP award with zero reward

    def test_handle_npc_death_with_string_npc_id(self):
        """Test NPC death with string NPC ID (not UUID)."""
        npc_id = "npc_123"
        room_id = "test_room_001"
        killer_id = str(uuid4())

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=None)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id)

        assert result is True
        self.event_publisher.publish_npc_died.assert_called_once()

    def test_handle_npc_death_with_string_combat_id(self):
        """Test NPC death with string combat ID (not UUID)."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        killer_id = str(uuid4())
        combat_id = "combat_123"

        # Mock NPC instance
        npc_instance = Mock()
        npc_instance.name = "Test NPC"

        self.service._get_npc_instance = Mock(return_value=npc_instance)
        self.service._get_npc_definition = Mock(return_value=None)

        result = self.service.handle_npc_death(npc_id=npc_id, room_id=room_id, killer_id=killer_id, combat_id=combat_id)

        assert result is True
        self.event_publisher.publish_npc_died.assert_called_once()
