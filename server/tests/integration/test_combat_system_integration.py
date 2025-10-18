"""
Integration tests for combat system with existing systems.

This module tests the integration of the combat system with the command system,
messaging system, persistence layer, and event system.
"""

from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.commands.combat import CombatCommandHandler
from server.events.event_bus import EventBus
from server.persistence import PersistenceLayer
from server.services.combat_service import CombatService
from server.services.npc_combat_integration_service import NPCCombatIntegrationService
from server.services.player_combat_service import PlayerCombatService


class TestCombatSystemIntegration:
    """Integration tests for combat system with existing systems."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return AsyncMock(spec=PersistenceLayer)

    @pytest.fixture
    def mock_event_bus(self):
        """Create a mock event bus."""
        mock_bus = AsyncMock(spec=EventBus)
        mock_bus.publish_event = AsyncMock()
        return mock_bus

    @pytest.fixture
    def player_combat_service(self, mock_persistence, mock_event_bus):
        """Create a player combat service with mocked dependencies."""
        return PlayerCombatService(mock_persistence, mock_event_bus)

    @pytest.fixture
    def combat_service(self, player_combat_service):
        """Create a combat service with player combat service."""
        return CombatService(player_combat_service=player_combat_service)

    @pytest.fixture
    def npc_combat_integration_service(self, mock_event_bus):
        """Create an NPC combat integration service."""
        return NPCCombatIntegrationService(event_bus=mock_event_bus)

    @pytest.fixture
    def combat_command_handler(self):
        """Create a combat command handler."""
        return CombatCommandHandler()

    @pytest.mark.asyncio
    async def test_combat_command_integration_with_validation(self, combat_command_handler):
        """Test that combat commands integrate with validation system."""
        command_data = {"command": "attack rat", "target": "rat", "action": "attack"}
        current_user = {"user_id": str(uuid4())}
        request = Mock()
        alias_storage = Mock()

        # Mock the combat service to avoid actual combat logic
        with patch.object(combat_command_handler, "npc_combat_service") as mock_service:
            mock_service.handle_player_attack_on_npc = Mock(return_value=True)

            result = await combat_command_handler.handle_attack_command(
                command_data=command_data,
                current_user=current_user,
                request=request,
                alias_storage=alias_storage,
                player_name="TestPlayer",
            )

            assert "result" in result
            assert isinstance(result["result"], str)

    @pytest.mark.asyncio
    async def test_combat_service_integration_with_player_service(self, combat_service, player_combat_service):
        """Test that combat service integrates with player combat service."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=5,  # Low HP to trigger death
            target_max_hp=50,
            target_dex=10,
        )

        # Process attack that kills target
        result = await combat_service.process_attack(player_id, npc_id, damage=10)

        # Verify combat ended and XP was awarded
        assert result.success is True
        assert result.target_died is True
        assert result.combat_ended is True
        assert result.xp_awarded > 0

    @pytest.mark.asyncio
    async def test_combat_messaging_integration(self, npc_combat_integration_service):
        """Test that combat integrates with messaging system."""
        # Test that the integration service has messaging components
        assert hasattr(npc_combat_integration_service, "_messaging_integration")
        assert hasattr(npc_combat_integration_service, "_event_publisher")

    @pytest.mark.asyncio
    async def test_combat_persistence_integration(self, player_combat_service, mock_persistence):
        """Test that combat integrates with persistence layer."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_amount = 10

        # Mock player data
        mock_player = Mock()
        mock_player.experience_points = 100
        mock_player.level = 5
        mock_player.add_experience = Mock()
        mock_persistence.async_get_player.return_value = mock_player

        # Award XP
        await player_combat_service.award_xp_on_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

        # Verify persistence was called
        mock_persistence.async_get_player.assert_called_once_with(str(player_id))
        mock_persistence.async_save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_combat_event_integration(self, player_combat_service, mock_event_bus):
        """Test that combat integrates with event system."""
        player_id = uuid4()
        npc_id = uuid4()
        xp_amount = 10

        # Mock persistence
        mock_persistence = AsyncMock()
        mock_player = Mock()
        mock_player.experience_points = 100
        mock_player.level = 5
        mock_player.add_experience = Mock()
        mock_persistence.async_get_player.return_value = mock_player
        mock_persistence.async_save_player = AsyncMock()

        # Set up player combat service with mocked persistence
        player_combat_service._persistence = mock_persistence

        # Award XP
        await player_combat_service.award_xp_on_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

        # Verify event was published
        mock_event_bus.publish_event.assert_called_once()

    @pytest.mark.asyncio
    async def test_combat_security_integration(self, combat_command_handler):
        """Test that combat integrates with security validation."""
        # Test malicious command
        malicious_command_data = {
            "command": "attack <script>alert('xss')</script>",
            "target": "<script>alert('xss')</script>",
            "action": "attack",
        }
        current_user = {"user_id": str(uuid4())}
        request = Mock()
        alias_storage = Mock()

        result = await combat_command_handler.handle_attack_command(
            command_data=malicious_command_data,
            current_user=current_user,
            request=request,
            alias_storage=alias_storage,
            player_name="TestPlayer",
        )

        # Should not contain XSS content in result
        assert "<script>" not in str(result)
        assert "alert('xss')" not in str(result)

    @pytest.mark.asyncio
    async def test_combat_rate_limiting_integration(self, combat_command_handler):
        """Test that combat integrates with rate limiting."""
        # Note: Rate limiting is not yet implemented, so this test is skipped

        pytest.skip("Rate limiting functionality not yet implemented")

    @pytest.mark.asyncio
    async def test_combat_audit_logging_integration(self, combat_command_handler):
        """Test that combat integrates with audit logging."""
        command_data = {"command": "attack rat", "target": "rat", "action": "attack"}
        current_user = {"user_id": str(uuid4())}
        request = Mock()
        alias_storage = Mock()

        # Mock audit logging
        with patch("server.logging.combat_audit.combat_audit_logger") as mock_audit_logger:
            # Mock the combat service
            with patch.object(combat_command_handler, "npc_combat_service") as mock_service:
                mock_service.handle_player_attack_on_npc = Mock(return_value=True)

                await combat_command_handler.handle_attack_command(
                    command_data=command_data,
                    current_user=current_user,
                    request=request,
                    alias_storage=alias_storage,
                    player_name="TestPlayer",
                )

                # Verify audit logging was called
                mock_audit_logger.log_combat_start.assert_called_once()
                mock_audit_logger.log_combat_attack.assert_called_once()

    @pytest.mark.asyncio
    async def test_combat_npc_integration(self, npc_combat_integration_service):
        """Test that combat integrates with NPC system."""
        # Test that the integration service has NPC components
        assert hasattr(npc_combat_integration_service, "_persistence")
        assert hasattr(npc_combat_integration_service, "_combat_service")

    @pytest.mark.asyncio
    async def test_combat_room_integration(self, combat_service):
        """Test that combat integrates with room system."""
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat in specific room
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Verify combat is associated with correct room
        assert combat.room_id == room_id

    @pytest.mark.asyncio
    async def test_combat_cleanup_integration(self, combat_service, player_combat_service):
        """Test that combat cleanup integrates with all systems."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        combat_id = combat.combat_id

        # End combat
        await combat_service.end_combat(combat_id, "Test end")

        # Verify cleanup
        assert combat.status.value == "ended"
        assert combat_id not in combat_service._active_combats
        assert player_id not in combat_service._player_combats
        assert npc_id not in combat_service._npc_combats

    @pytest.mark.asyncio
    async def test_combat_error_handling_integration(self, combat_command_handler):
        """Test that combat integrates with error handling."""
        # Test with invalid command data
        invalid_command_data = {"command": "invalid_command", "target": "rat", "action": "invalid"}
        current_user = {"user_id": str(uuid4())}
        request = Mock()
        alias_storage = Mock()

        result = await combat_command_handler.handle_attack_command(
            command_data=invalid_command_data,
            current_user=current_user,
            request=request,
            alias_storage=alias_storage,
            player_name="TestPlayer",
        )

        # Should return error message
        assert "result" in result
        assert isinstance(result["result"], str)

    @pytest.mark.asyncio
    async def test_combat_concurrent_access_integration(self, combat_service):
        """Test that combat handles concurrent access properly."""
        player1_id = uuid4()
        player2_id = uuid4()
        npc1_id = uuid4()
        npc2_id = uuid4()

        # Start two separate combats with different NPCs
        combat1 = await combat_service.start_combat(
            room_id="room1",
            attacker_id=player1_id,
            target_id=npc1_id,
            attacker_name="Player1",
            target_name="NPC1",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        combat2 = await combat_service.start_combat(
            room_id="room2",
            attacker_id=player2_id,
            target_id=npc2_id,
            attacker_name="Player2",
            target_name="NPC2",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Verify both combats exist independently
        assert combat1.combat_id != combat2.combat_id
        assert len(combat_service._active_combats) == 2
        assert player1_id in combat_service._player_combats
        assert player2_id in combat_service._player_combats

    @pytest.mark.asyncio
    async def test_combat_statistics_integration(self, combat_service):
        """Test that combat integrates with statistics collection."""
        # Get initial stats
        initial_stats = await combat_service.get_combat_stats()
        assert initial_stats["active_combats"] == 0

        # Start combat
        player_id = uuid4()
        npc_id = uuid4()

        await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
        )

        # Get stats after combat
        stats = await combat_service.get_combat_stats()
        assert stats["active_combats"] == 1
        assert stats["player_combats"] == 1
        assert stats["npc_combats"] == 1
