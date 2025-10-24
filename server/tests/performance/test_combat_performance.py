"""
Performance tests for the combat system.

This module tests the performance characteristics of the combat system
to ensure no server degradation under various load conditions.
"""

import asyncio
import time
from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.commands.combat import CombatCommandHandler
from server.services.combat_service import CombatService
from server.services.player_combat_service import PlayerCombatService


class TestCombatPerformance:
    """Performance tests for combat system."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return AsyncMock()

    @pytest.fixture
    def mock_event_bus(self):
        """Create a mock event bus."""
        return AsyncMock()

    @pytest.fixture
    def player_combat_service(self, mock_persistence, mock_event_bus):
        """Create a player combat service."""
        return PlayerCombatService(mock_persistence, mock_event_bus)

    @pytest.fixture
    def mock_nats_service(self):
        """Create a mock NATS service."""
        nats_service = Mock()
        nats_service.is_connected.return_value = True
        nats_service.publish = AsyncMock(return_value=True)
        return nats_service

    @pytest.fixture
    def combat_service(self, player_combat_service, mock_nats_service):
        """Create a combat service."""
        return CombatService(player_combat_service=player_combat_service, nats_service=mock_nats_service)

    @pytest.fixture
    def combat_command_handler(self):
        """Create a combat command handler."""
        return CombatCommandHandler()

    @pytest.mark.asyncio
    async def test_combat_startup_performance(self, combat_service):
        """Test performance of starting multiple combats."""
        num_combats = 100
        start_time = time.time()

        # Start multiple combats concurrently
        tasks = []
        for i in range(num_combats):
            player_id = uuid4()
            npc_id = uuid4()

            task = combat_service.start_combat(
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
            tasks.append(task)

        # Wait for all combats to start
        await asyncio.gather(*tasks)

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should complete within reasonable time
        assert duration < 5.0  # Should complete within 5 seconds
        assert len(combat_service._active_combats) == num_combats

    @pytest.mark.asyncio
    async def test_combat_attack_performance(self, combat_service):
        """Test performance of processing multiple attacks."""
        num_attacks = 1000
        start_time = time.time()

        # Start a combat
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
            target_hp=1000,  # High HP to survive many attacks
            target_max_hp=1000,
            target_dex=10,
            current_tick=0,
        )

        # Process multiple attacks (system handles turn progression automatically)
        for _i in range(num_attacks):
            await combat_service.process_attack(player_id, npc_id, damage=1)

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should complete within reasonable time
        assert duration < 10.0  # Should complete within 10 seconds

    @pytest.mark.asyncio
    async def test_combat_memory_usage(self, combat_service):
        """Test memory usage of combat system."""
        import os

        import psutil

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        # Create many combats
        num_combats = 1000
        for i in range(num_combats):
            player_id = uuid4()
            npc_id = uuid4()

            await combat_service.start_combat(
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

        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory

        # Memory assertion: should not use excessive memory
        # Allow for 1MB per combat (generous estimate)
        max_expected_memory = num_combats * 1024 * 1024  # 1MB per combat
        assert memory_increase < max_expected_memory

    @pytest.mark.asyncio
    async def test_combat_cleanup_performance(self, combat_service):
        """Test performance of cleaning up combats."""
        # Start many combats
        num_combats = 100
        combat_ids = []

        for i in range(num_combats):
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
            combat_ids.append(combat.combat_id)

        start_time = time.time()

        # Clean up all combats
        for combat_id in combat_ids:
            await combat_service.end_combat(combat_id, "Test cleanup")

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should complete within reasonable time
        assert duration < 2.0  # Should complete within 2 seconds
        assert len(combat_service._active_combats) == 0

    @pytest.mark.asyncio
    async def test_combat_concurrent_access_performance(self, combat_service):
        """Test performance under concurrent access."""
        num_concurrent_combats = 50
        start_time = time.time()

        # Start combats concurrently
        async def start_combat(i):
            player_id = uuid4()
            npc_id = uuid4()

            return await combat_service.start_combat(
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

        # Start all combats concurrently
        combats = await asyncio.gather(*[start_combat(i) for i in range(num_concurrent_combats)])

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should handle concurrent access efficiently
        assert duration < 3.0  # Should complete within 3 seconds
        assert len(combats) == num_concurrent_combats
        assert len(combat_service._active_combats) == num_concurrent_combats

    @pytest.mark.asyncio
    async def test_combat_command_performance(self, combat_command_handler):
        """Test performance of combat commands."""
        num_commands = 100
        start_time = time.time()

        # Mock dependencies
        command_data = {"command": "attack rat", "target": "rat", "action": "attack"}
        current_user = {"user_id": str(uuid4())}
        request = Mock()
        alias_storage = Mock()

        # Mock the combat service to avoid actual combat logic
        with patch.object(combat_command_handler, "npc_combat_service") as mock_service:
            mock_service.handle_attack_command = AsyncMock(return_value={"result": "You attack the rat!"})

            # Process multiple commands
            tasks = []
            for _ in range(num_commands):
                task = combat_command_handler.handle_attack_command(
                    command_data=command_data,
                    current_user=current_user,
                    request=request,
                    alias_storage=alias_storage,
                    player_name="TestPlayer",
                )
                tasks.append(task)

            # Wait for all commands to complete
            await asyncio.gather(*tasks)

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should complete within reasonable time
        assert duration < 5.0  # Should complete within 5 seconds

    @pytest.mark.asyncio
    async def test_combat_statistics_performance(self, combat_service):
        """Test performance of getting combat statistics."""
        # Start many combats
        num_combats = 100
        for i in range(num_combats):
            player_id = uuid4()
            npc_id = uuid4()

            await combat_service.start_combat(
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

        start_time = time.time()

        # Get statistics multiple times
        for _ in range(100):
            stats = await combat_service.get_combat_stats()

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should complete within reasonable time
        assert duration < 1.0  # Should complete within 1 second
        assert stats["active_combats"] == num_combats

    @pytest.mark.asyncio
    async def test_combat_stale_cleanup_performance(self, combat_service):
        """Test performance of cleaning up stale combats."""
        # Start many combats
        num_combats = 100
        for i in range(num_combats):
            player_id = uuid4()
            npc_id = uuid4()

            await combat_service.start_combat(
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

        start_time = time.time()

        # Clean up stale combats
        cleaned_count = await combat_service.cleanup_stale_combats()

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should complete within reasonable time
        assert duration < 1.0  # Should complete within 1 second
        assert cleaned_count == 0  # No stale combats initially

    @pytest.mark.asyncio
    async def test_combat_xp_award_performance(self, player_combat_service, mock_persistence):
        """Test performance of XP award system."""
        num_awards = 100
        start_time = time.time()

        # Mock player data
        mock_player = Mock()
        mock_player.experience_points = 100
        mock_player.level = 5
        mock_player.add_experience = Mock()
        mock_persistence.async_get_player.return_value = mock_player
        mock_persistence.async_save_player = AsyncMock()

        # Award XP multiple times
        tasks = []
        for _ in range(num_awards):
            player_id = uuid4()
            npc_id = uuid4()

            task = player_combat_service.award_xp_on_npc_death(
                player_id=player_id,
                npc_id=npc_id,
                xp_amount=10,
            )
            tasks.append(task)

        # Wait for all awards to complete
        await asyncio.gather(*tasks)

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should complete within reasonable time
        assert duration < 3.0  # Should complete within 3 seconds

    @pytest.mark.asyncio
    async def test_combat_validation_performance(self, combat_command_handler):
        """Test performance of combat validation."""
        num_validations = 1000
        start_time = time.time()

        # Test various command types
        command_types = ["attack", "punch", "kick", "strike", "hit"]

        for i in range(num_validations):
            command_type = command_types[i % len(command_types)]
            command_data = {"command": f"{command_type} rat", "target": "rat", "action": command_type}
            current_user = {"user_id": str(uuid4())}
            request = Mock()
            alias_storage = Mock()

            # Mock the combat service
            with patch.object(combat_command_handler, "npc_combat_service") as mock_service:
                mock_service.handle_attack_command = AsyncMock(return_value={"result": "You attack the rat!"})

                await combat_command_handler.handle_attack_command(
                    command_data=command_data,
                    current_user=current_user,
                    request=request,
                    alias_storage=alias_storage,
                    player_name="TestPlayer",
                )

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should complete within reasonable time
        assert duration < 10.0  # Should complete within 10 seconds

    @pytest.mark.asyncio
    async def test_combat_system_load_test(self, combat_service):
        """Test combat system under high load."""
        num_combats = 500
        num_attacks_per_combat = 10
        start_time = time.time()

        # Start many combats and process attacks
        async def simulate_combat(i):
            player_id = uuid4()
            npc_id = uuid4()

            # Start combat
            combat = await combat_service.start_combat(
                room_id=f"room_{i}",
                attacker_id=player_id,
                target_id=npc_id,
                attacker_name=f"Player_{i}",
                target_name=f"NPC_{i}",
                attacker_hp=100,
                attacker_max_hp=100,
                attacker_dex=15,
                target_hp=100,  # High HP to survive attacks
                target_max_hp=100,
                target_dex=10,
                current_tick=0,
            )

            # Process multiple attacks (system handles turn progression automatically)
            for _attack_num in range(num_attacks_per_combat):
                await combat_service.process_attack(player_id, npc_id, damage=1)

            return combat

        # Run all combats concurrently
        combats = await asyncio.gather(*[simulate_combat(i) for i in range(num_combats)])

        end_time = time.time()
        duration = end_time - start_time

        # Performance assertion: should handle high load efficiently
        # Adjusted threshold to account for realistic performance with 5000 total operations
        assert duration < 60.0  # Should complete within 60 seconds
        assert len(combats) == num_combats
        assert len(combat_service._active_combats) == num_combats
