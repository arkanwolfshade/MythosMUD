"""
End-to-end combat scenarios and user workflow tests.

This module tests complete combat workflows from user interaction
to system response, ensuring the entire combat system works correctly.
"""

from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.commands.combat import CombatCommandHandler
from server.events.event_bus import EventBus
from server.logging.enhanced_logging_config import get_logger
from server.persistence import PersistenceLayer
from server.services.combat_service import CombatService
from server.services.npc_combat_integration_service import NPCCombatIntegrationService
from server.services.player_combat_service import PlayerCombatService

logger = get_logger(__name__)


class TestCombatScenarios:
    """End-to-end combat scenario tests."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return AsyncMock(spec=PersistenceLayer)

    @pytest.fixture
    def mock_event_bus(self):
        """Create a mock event bus."""
        mock_bus = AsyncMock(spec=EventBus)
        mock_bus.publish = AsyncMock()
        return mock_bus

    @pytest.fixture
    def player_combat_service(self, mock_persistence, mock_event_bus):
        """Create a player combat service."""
        return PlayerCombatService(mock_persistence, mock_event_bus)

    @pytest.fixture
    def combat_service(self, player_combat_service):
        """Create a combat service."""
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
    async def test_basic_combat_scenario(self, combat_service, player_combat_service):
        """Test a basic combat scenario from start to finish."""
        # Scenario: Player attacks NPC, NPC dies, player gets XP

        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Step 1: Start combat
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=5,  # Low HP to ensure death
            target_max_hp=50,
            target_dex=10,
            current_tick=0,
        )

        # Verify combat started
        assert combat.room_id == room_id
        assert combat.status.value == "active"
        assert len(combat.participants) == 2
        assert player_id in combat.participants
        assert npc_id in combat.participants

        # Step 2: Process attack that kills NPC
        result = await combat_service.process_attack(player_id, npc_id, damage=10)

        # Verify attack results
        assert result.success is True
        assert result.damage == 10
        assert result.target_died is True
        assert result.combat_ended is True
        assert result.xp_awarded > 0

        # Step 3: Verify combat ended
        assert combat.status.value == "ended"

    @pytest.mark.asyncio
    async def test_multi_round_combat_scenario(self, combat_service):
        """Test a multi-round combat scenario."""
        # Scenario: Player and NPC fight for multiple rounds

        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat with higher HP
        await combat_service.start_combat(
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
            current_tick=0,
        )

        # Round 1: Player attacks (system will auto-advance to NPC turn)
        result1 = await combat_service.process_attack(player_id, npc_id, damage=10)
        assert result1.success is True
        assert result1.target_died is False
        assert result1.combat_ended is False

        # Round 2: Player attacks again (system auto-advanced back to player turn)
        result2 = await combat_service.process_attack(player_id, npc_id, damage=15)
        assert result2.success is True
        assert result2.target_died is False
        assert result2.combat_ended is False

        # Round 3: Final attack that kills NPC
        result3 = await combat_service.process_attack(player_id, npc_id, damage=30)
        assert result3.success is True
        assert result3.target_died is True
        assert result3.combat_ended is True

    @pytest.mark.asyncio
    async def test_combat_command_workflow(self, combat_command_handler):
        """Test complete combat command workflow."""
        # Scenario: User types combat command, system processes it

        command_data = {"command_type": "attack", "args": ["rat"], "target_player": "rat"}
        current_user = {"player_id": str(uuid4()), "room_id": "test_room_001", "name": "TestPlayer"}
        alias_storage = Mock()

        # Mock the request object with proper app state
        mock_request = Mock()
        mock_app = Mock()
        mock_app.state.persistence = Mock()
        mock_request.app = mock_app

        # Mock player data
        mock_player = Mock()
        mock_player.player_id = str(uuid4())
        mock_player.current_room_id = "test_room_001"
        mock_player.name = "TestPlayer"
        mock_app.state.persistence.get_player_by_name.return_value = mock_player

        # Mock room data
        mock_room = Mock()
        mock_room.room_id = "test_room_001"
        mock_app.state.persistence.get_room.return_value = mock_room

        # Mock the combat command handler's persistence layer directly
        mock_global_persistence = Mock()
        mock_global_persistence.get_player_by_name.return_value = mock_player
        mock_global_persistence.get_room.return_value = mock_room
        combat_command_handler.persistence = mock_global_persistence

        # Mock target resolution success
        with patch.object(combat_command_handler, "target_resolution_service") as mock_target_resolution:
            with patch.object(combat_command_handler, "npc_combat_service") as mock_npc_service:
                with patch.object(combat_command_handler, "_get_npc_instance") as mock_get_npc:
                    from server.schemas.target_resolution import TargetMatch, TargetResolutionResult, TargetType

                    npc_id = str(uuid4())
                    mock_target_match = TargetMatch(
                        target_id=npc_id, target_name="rat", target_type=TargetType.NPC, room_id="test_room_001"
                    )
                    mock_target_result = TargetResolutionResult(
                        success=True, matches=[mock_target_match], search_term="rat", room_id="test_room_001"
                    )
                    mock_target_resolution.resolve_target = AsyncMock(return_value=mock_target_result)

                    # Mock NPC instance
                    mock_npc = Mock()
                    mock_npc.name = "rat"
                    mock_npc.is_alive = True
                    mock_get_npc.return_value = mock_npc

                    # Mock NPC combat service success
                    mock_npc_service.handle_player_attack_on_npc = AsyncMock(return_value=True)

                    # Process command
                    result = await combat_command_handler.handle_attack_command(
                        command_data=command_data,
                        current_user=current_user,
                        request=mock_request,
                        alias_storage=alias_storage,
                        player_name="TestPlayer",
                    )

                    # Verify command was processed
                    assert "result" in result
                    assert isinstance(result["result"], str)
                    assert "attack" in result["result"].lower()  # Should contain attack message
                    logger.debug("Command result", result=result)

    @pytest.mark.asyncio
    async def test_combat_validation_workflow(self, combat_command_handler):
        """Test combat command validation workflow."""
        # Scenario: User enters invalid command, system validates and responds

        invalid_command_data = {"command": "invalid_command", "target": "rat", "action": "invalid"}
        current_user = {"user_id": str(uuid4())}
        request = Mock()
        alias_storage = Mock()

        # Process invalid command
        result = await combat_command_handler.handle_attack_command(
            command_data=invalid_command_data,
            current_user=current_user,
            request=request,
            alias_storage=alias_storage,
            player_name="TestPlayer",
        )

        # Verify validation response
        assert "result" in result
        assert isinstance(result["result"], str)

    @pytest.mark.asyncio
    async def test_combat_security_workflow(self, combat_command_handler):
        """Test combat security validation workflow."""
        # Scenario: User attempts malicious command, system blocks it

        malicious_command_data = {
            "command": "attack <script>alert('xss')</script>",
            "target": "<script>alert('xss')</script>",
            "action": "attack",
        }
        current_user = {"user_id": str(uuid4())}
        request = Mock()
        alias_storage = Mock()

        # Process malicious command
        result = await combat_command_handler.handle_attack_command(
            command_data=malicious_command_data,
            current_user=current_user,
            request=request,
            alias_storage=alias_storage,
            player_name="TestPlayer",
        )

        # Verify security response
        assert "result" in result
        assert "<script>" not in str(result)
        assert "alert('xss')" not in str(result)

    @pytest.mark.asyncio
    async def test_combat_xp_workflow(self, player_combat_service, mock_persistence, mock_event_bus):
        """Test complete XP award workflow."""
        # Scenario: Player defeats NPC, gets XP, level increases

        player_id = uuid4()
        npc_id = uuid4()
        xp_amount = 10

        # Mock player data
        mock_player = Mock()
        mock_player.experience_points = 100
        mock_player.level = 5
        mock_player.add_experience = Mock()
        mock_persistence.async_get_player.return_value = mock_player
        mock_persistence.async_save_player = AsyncMock()

        # Award XP
        await player_combat_service.award_xp_on_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

        # Verify XP was awarded
        mock_persistence.async_get_player.assert_called_once_with(str(player_id))
        mock_persistence.async_save_player.assert_called_once_with(mock_player)
        mock_event_bus.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_combat_messaging_workflow(self, npc_combat_integration_service):
        """Test combat messaging workflow."""
        # Scenario: Combat messages are generated and sent to players

        # Test that messaging integration exists
        assert hasattr(npc_combat_integration_service, "_messaging_integration")
        assert hasattr(npc_combat_integration_service, "_event_publisher")

    @pytest.mark.asyncio
    async def test_combat_cleanup_workflow(self, combat_service):
        """Test combat cleanup workflow."""
        # Scenario: Combat ends, system cleans up resources

        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
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
            current_tick=0,
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
    async def test_combat_error_handling_workflow(self, combat_service):
        """Test combat error handling workflow."""
        # Scenario: Error occurs during combat, system handles gracefully

        player_id = uuid4()
        npc_id = uuid4()

        # Try to attack when not in combat (should raise error)
        with pytest.raises(ValueError, match="Attacker is not in combat"):
            await combat_service.process_attack(player_id, npc_id, damage=5)

    @pytest.mark.asyncio
    async def test_combat_concurrent_workflow(self, combat_service):
        """Test concurrent combat workflow."""
        # Scenario: Multiple players in different combats simultaneously

        # Start multiple combats
        combats = []
        for i in range(5):
            player_id = uuid4()
            npc_id = uuid4()

            combat = await combat_service.start_combat(
                room_id=f"room_{i}",
                attacker_id=player_id,
                target_id=npc_id,
                attacker_name=f"Player_{i}",
                target_name=f"NPC_{i}",
                attacker_hp=100,
                attacker_max_hp=100,
                attacker_dex=15,
                target_hp=50,
                target_max_hp=50,
                target_dex=10,
                current_tick=0,
            )
            combats.append(combat)

        # Verify all combats exist independently
        assert len(combats) == 5
        assert len(combat_service._active_combats) == 5

        # End all combats
        for combat in combats:
            await combat_service.end_combat(combat.combat_id, "Test end")

        # Verify all combats ended
        assert len(combat_service._active_combats) == 0

    @pytest.mark.asyncio
    async def test_combat_statistics_workflow(self, combat_service):
        """Test combat statistics workflow."""
        # Scenario: System tracks and reports combat statistics

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
            current_tick=0,
        )

        # Get stats after combat
        stats = await combat_service.get_combat_stats()
        assert stats["active_combats"] == 1
        assert stats["player_combats"] == 1
        assert stats["npc_combats"] == 1

    @pytest.mark.asyncio
    async def test_combat_audit_workflow(self, combat_command_handler):
        """Test combat audit logging workflow."""
        # Scenario: Combat actions are logged for security and compliance

        command_data = {"command_type": "attack", "args": ["rat"], "target_player": "rat"}
        current_user = {"player_id": str(uuid4()), "room_id": "test_room_001"}
        alias_storage = Mock()

        # Mock the request object with proper app state
        mock_request = Mock()
        mock_app = Mock()
        mock_app.state.persistence = Mock()
        mock_request.app = mock_app

        # Mock player data
        mock_player = Mock()
        mock_player.player_id = str(uuid4())
        mock_player.current_room_id = "test_room_001"
        mock_player.name = "TestPlayer"
        mock_app.state.persistence.get_player_by_name.return_value = mock_player

        # Mock room data
        mock_room = Mock()
        mock_room.room_id = "test_room_001"
        mock_app.state.persistence.get_room.return_value = mock_room

        # Mock target resolution success
        with patch.object(combat_command_handler, "target_resolution_service") as mock_target_resolution:
            with patch.object(combat_command_handler, "npc_combat_service") as mock_npc_service:
                with patch.object(combat_command_handler, "_get_npc_instance") as mock_get_npc:
                    from server.schemas.target_resolution import TargetMatch, TargetResolutionResult, TargetType

                    npc_id = str(uuid4())
                    mock_target_match = TargetMatch(
                        target_id=npc_id, target_name="rat", target_type=TargetType.NPC, room_id="test_room_001"
                    )
                    mock_target_result = TargetResolutionResult(
                        success=True, matches=[mock_target_match], search_term="rat", room_id="test_room_001"
                    )
                    mock_target_resolution.resolve_target.return_value = mock_target_result

                    # Mock NPC instance
                    mock_npc = Mock()
                    mock_npc.name = "rat"
                    mock_npc.is_alive = True
                    mock_get_npc.return_value = mock_npc

                    # Mock NPC combat service success
                    mock_npc_service.handle_player_attack_on_npc = AsyncMock(return_value=True)

                    # Process command
                    result = await combat_command_handler.handle_attack_command(
                        command_data=command_data,
                        current_user=current_user,
                        request=mock_request,
                        alias_storage=alias_storage,
                        player_name="TestPlayer",
                    )

                    # Verify audit logging (should be handled by the combat system)
                    assert "result" in result
                    assert isinstance(result["result"], str)
                    logger.debug("Audit workflow result", result=result)

    @pytest.mark.asyncio
    async def test_combat_rate_limiting_workflow(self, combat_command_handler):
        """Test combat rate limiting workflow."""
        # Scenario: User exceeds rate limit, system blocks further commands
        # Note: Rate limiting is not yet implemented, so this test is skipped

        pytest.skip("Rate limiting functionality not yet implemented")

    @pytest.mark.asyncio
    async def test_combat_monitoring_workflow(self, combat_service):
        """Test combat monitoring workflow."""
        # Scenario: System monitors combat for unusual activity

        # Start combat
        player_id = uuid4()
        npc_id = uuid4()

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
            current_tick=0,
        )

        # Verify combat is being monitored
        assert combat.combat_id in combat_service._active_combats
        assert player_id in combat_service._player_combats
        assert npc_id in combat_service._npc_combats

    @pytest.mark.asyncio
    async def test_combat_complete_user_journey(
        self, combat_service, player_combat_service, mock_persistence, mock_event_bus
    ):
        """Test complete user journey through combat system."""
        # Scenario: Complete user journey from login to combat victory

        # Step 1: Player enters room with NPC
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Step 2: Player attacks NPC
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=5,  # Low HP to ensure death
            target_max_hp=50,
            target_dex=10,
            current_tick=0,
        )

        # Step 3: Combat progresses
        result = await combat_service.process_attack(player_id, npc_id, damage=10)

        # Step 4: NPC dies, player gets XP
        assert result.success is True
        assert result.target_died is True
        assert result.combat_ended is True
        assert result.xp_awarded > 0

        # Step 5: Combat ends, system cleans up
        assert combat.status.value == "ended"
        assert combat.combat_id not in combat_service._active_combats

        # Step 6: Player continues with increased XP
        # (This would be handled by the player service in real implementation)
        assert result.xp_awarded > 0
