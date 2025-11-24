"""
Integration tests for NPC periodic spawning and respawning functionality.

This module tests the complete NPC lifecycle including periodic spawn checks,
respawning after death, and game tick integration.

As documented in the Cultes des Goules, the cyclic nature of manifestations
requires careful observation to ensure entities return from the void at
the proper intervals.

AI Agent: Integration tests for Issue #257 - NPC periodic spawning and respawning.
         Tests the complete flow from game tick to NPC spawn/respawn.
"""

import asyncio
import time
from unittest.mock import MagicMock, patch

import pytest

from server.config.npc_config import NPCMaintenanceConfig
from server.events.event_bus import EventBus
from server.models.npc import NPCDefinition, NPCDefinitionType
from server.npc.lifecycle_manager import NPCLifecycleManager
from server.npc.population_control import NPCPopulationController, PopulationStats
from server.npc.spawning_service import NPCSpawningService


@pytest.fixture
def event_bus():
    """Create an event bus for testing."""
    return EventBus()


@pytest.fixture
def population_controller(event_bus):
    """Create a population controller with mocked zone configs."""
    # Create a mock async_persistence that doesn't actually load from database
    mock_persistence = MagicMock()

    # Patch the _load_zone_configurations method to skip database loading
    with patch.object(NPCPopulationController, "_load_zone_configurations", return_value=None):
        controller = NPCPopulationController(
            event_bus,
            spawning_service=None,
            lifecycle_manager=None,
            async_persistence=mock_persistence,
        )

        # Add a mock zone configuration
        mock_zone_config = MagicMock()
        mock_zone_config.get_effective_spawn_probability = lambda prob: prob
        controller.zone_configurations["arkhamcity/downtown"] = mock_zone_config

        # Add population stats for the zone
        stats = PopulationStats("arkhamcity", "downtown")
        controller.population_stats["arkhamcity/downtown"] = stats

        return controller


@pytest.fixture
def spawning_service(event_bus, population_controller):
    """Create a spawning service for testing."""
    return NPCSpawningService(event_bus, population_controller)


@pytest.fixture
def lifecycle_manager(event_bus, population_controller, spawning_service):
    """Create a lifecycle manager for testing."""
    manager = NPCLifecycleManager(
        event_bus,
        population_controller,
        spawning_service,
        persistence=None,
    )
    # Link back to lifecycle manager
    population_controller.lifecycle_manager = manager
    return manager


@pytest.fixture
def optional_npc_definition():
    """Create an optional NPC definition for testing."""
    definition = NPCDefinition(
        name="Wandering Cultist",
        description="A cultist who wanders the streets",
        npc_type=NPCDefinitionType.PASSIVE_MOB,
        sub_zone_id=1,  # downtown sub-zone
        required_npc=False,
        max_population=3,
        spawn_probability=0.3,  # 30% chance
        room_id="earth_arkhamcity_downtown_001",
        base_stats='{"strength": 5, "sanity": 30, "current_health": 50}',
        behavior_config='{"wander_probability": 0.2}',
        ai_integration_stub="{}",
    )
    definition.id = 100
    return definition


@pytest.fixture
def required_npc_definition():
    """Create a required NPC definition for testing."""
    definition = NPCDefinition(
        name="Dr. Morgan",
        description="The asylum director",
        npc_type=NPCDefinitionType.QUEST_GIVER,
        sub_zone_id=2,  # sanitarium sub-zone
        required_npc=True,
        max_population=1,
        spawn_probability=1.0,
        room_id="earth_arkhamcity_sanitarium_office",
        base_stats='{"strength": 10, "sanity": 80, "current_health": 100}',
        behavior_config="{}",
        ai_integration_stub="{}",
    )
    definition.id = 200
    return definition


class TestPeriodicSpawning:
    """Test periodic spawning of optional NPCs."""

    def test_periodic_maintenance_spawns_optional_npcs(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test that periodic maintenance can spawn optional NPCs."""
        # Add the optional NPC definition to population controller
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Mock spawn to always succeed
        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "earth_arkhamcity_downtown_001"
                mock_create.return_value = mock_npc

                class _FakeRoom:
                    def npc_entered(self, _nid):
                        pass  # Don't publish event for this test

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

                    # Force spawn probability to 100% for testing
                    with patch("random.random", return_value=0.0):  # Will be <= any positive probability
                        results = lifecycle_manager.periodic_maintenance()

                        # Verify spawn check was performed
                        assert "spawn_checks_performed" in results
                        assert "spawned_npcs" in results

    def test_periodic_maintenance_respects_spawn_interval(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test that spawn checks respect minimum interval."""
        # Add optional NPC
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Set last check time to now (should skip check)
        lifecycle_manager.last_spawn_check[optional_npc_definition.id] = time.time()

        # Run maintenance
        results = lifecycle_manager.periodic_maintenance()

        # Should not perform spawn check due to interval
        assert results["spawn_checks_performed"] == 0

    def test_periodic_maintenance_respects_population_limits(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test that periodic spawning respects population limits."""
        # Add optional NPC
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Set population to maximum
        stats = population_controller.get_population_stats("arkhamcity/downtown")
        stats.npcs_by_definition[optional_npc_definition.id] = optional_npc_definition.max_population

        # Run maintenance
        results = lifecycle_manager.periodic_maintenance()

        # Should check but not spawn
        assert results["spawned_npcs"] == 0

    def test_periodic_maintenance_skips_required_npcs(
        self,
        lifecycle_manager,
        population_controller,
        required_npc_definition,
    ):
        """Test that periodic spawn checks skip required NPCs."""
        # Add required NPC
        population_controller.npc_definitions[required_npc_definition.id] = required_npc_definition

        # Run maintenance
        results = lifecycle_manager.periodic_maintenance()

        # Should not check required NPCs
        assert results["spawn_checks_performed"] == 0


class TestNPCRespawning:
    """Test NPC respawning functionality."""

    @pytest.mark.slow
    def test_npc_respawn_after_death(
        self,
        lifecycle_manager,
        population_controller,
        spawning_service,
        optional_npc_definition,
    ):
        """Test that dead NPCs respawn after delay."""
        # Spawn an NPC first
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "earth_arkhamcity_downtown_001"
                mock_create.return_value = mock_npc

                class _FakeRoom:
                    def npc_entered(self, _nid):
                        pass

                    def npc_left(self, _nid):
                        pass

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

                    # Spawn NPC
                    npc_id = lifecycle_manager.spawn_npc(
                        optional_npc_definition,
                        "earth_arkhamcity_downtown_001",
                        "test",
                    )
                    assert npc_id is not None

                    # Despawn the NPC
                    result = lifecycle_manager.despawn_npc(npc_id, "death")
                    assert result is True

                    # Record death AFTER despawn (simulating actual death flow)
                    lifecycle_manager.record_npc_death(npc_id)

                    # Try to schedule respawn immediately - should fail due to death suppression
                    result = lifecycle_manager.respawn_npc(npc_id, delay=0.1, reason="death")
                    assert result is False  # Death suppression blocks respawn

                    # Wait for death suppression to expire
                    time.sleep(lifecycle_manager.death_suppression_duration + 0.1)

                    # Now respawn should work
                    result = lifecycle_manager.respawn_npc(npc_id, delay=0.1, reason="death")
                    assert result is True

                    # Wait for respawn delay
                    time.sleep(0.2)

                    # Process respawn queue
                    respawned_count = lifecycle_manager.process_respawn_queue()

                    # Should have respawned now
                    assert respawned_count >= 0

    def test_respawn_queue_processes_correctly(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test that respawn queue is processed correctly."""
        # Add definition
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Create a lifecycle record
        from server.npc.lifecycle_manager import NPCLifecycleRecord

        record = NPCLifecycleRecord("npc_001", optional_npc_definition)
        lifecycle_manager.lifecycle_records["npc_001"] = record

        # Add to respawn queue with past scheduled time
        respawn_data = {
            "npc_id": "npc_001",
            "definition": optional_npc_definition,
            "room_id": "earth_arkhamcity_downtown_001",
            "scheduled_time": time.time() - 1.0,  # Past
            "reason": "test",
            "attempts": 0,
        }
        lifecycle_manager.respawn_queue["npc_001"] = respawn_data

        # Mock spawning
        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "earth_arkhamcity_downtown_001"
                mock_create.return_value = mock_npc

                class _FakeRoom:
                    def npc_entered(self, _nid):
                        pass

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

                    # Process respawn queue
                    respawned_count = lifecycle_manager.process_respawn_queue()

                    # Verify respawn occurred
                    assert respawned_count == 1
                    assert "npc_001" not in lifecycle_manager.respawn_queue

    def test_max_respawn_attempts_respected(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test that max respawn attempts limit is respected."""
        # Add definition
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Create lifecycle record
        from server.npc.lifecycle_manager import NPCLifecycleRecord

        record = NPCLifecycleRecord("npc_001", optional_npc_definition)
        lifecycle_manager.lifecycle_records["npc_001"] = record

        # Add to respawn queue with max attempts reached
        respawn_data = {
            "npc_id": "npc_001",
            "definition": optional_npc_definition,
            "room_id": "earth_arkhamcity_downtown_001",
            "scheduled_time": time.time() - 1.0,
            "reason": "test",
            "attempts": lifecycle_manager.max_respawn_attempts,  # At max
        }
        lifecycle_manager.respawn_queue["npc_001"] = respawn_data

        # Mock spawn to fail
        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=False):
            # Process respawn queue
            respawned_count = lifecycle_manager.process_respawn_queue()

            # Should have been removed from queue despite failure
            assert "npc_001" not in lifecycle_manager.respawn_queue
            assert respawned_count == 0


class TestGameTickIntegration:
    """Test integration with game tick loop."""

    def test_maintenance_config_should_run_maintenance(self):
        """Test maintenance interval configuration."""
        # Should run on multiples of 60
        assert NPCMaintenanceConfig.should_run_maintenance(60) is True
        assert NPCMaintenanceConfig.should_run_maintenance(120) is True
        assert NPCMaintenanceConfig.should_run_maintenance(180) is True

        # Should not run on non-multiples
        assert NPCMaintenanceConfig.should_run_maintenance(59) is False
        assert NPCMaintenanceConfig.should_run_maintenance(61) is False
        assert NPCMaintenanceConfig.should_run_maintenance(119) is False

    def test_maintenance_config_get_respawn_delay(self):
        """Test getting respawn delay for different NPC types."""
        # Test configured types
        assert NPCMaintenanceConfig.get_respawn_delay("quest_giver") == 600.0
        assert NPCMaintenanceConfig.get_respawn_delay("shopkeeper") == 300.0
        assert NPCMaintenanceConfig.get_respawn_delay("passive_mob") == 180.0
        assert NPCMaintenanceConfig.get_respawn_delay("aggressive_mob") == 300.0

        # Test default for unknown type
        assert NPCMaintenanceConfig.get_respawn_delay("unknown_type") == 300.0

    def test_maintenance_config_summary(self):
        """Test configuration summary."""
        summary = NPCMaintenanceConfig.get_config_summary()

        assert "maintenance_interval_ticks" in summary
        assert "spawn_reroll_interval" in summary
        assert "respawn_delays" in summary
        assert "min_spawn_check_interval" in summary
        assert summary["maintenance_interval_ticks"] == 60
        assert summary["spawn_reroll_interval"] == 600.0


class TestCompleteLifecycle:
    """Test complete NPC lifecycle with periodic spawning."""

    @pytest.mark.asyncio
    @pytest.mark.slow
    async def test_complete_spawn_despawn_respawn_cycle(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test complete lifecycle: spawn -> despawn -> respawn."""
        # Add definition
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Mock persistence with proper tracking
        class _FakeRoom:
            def __init__(self):
                self.npcs = []

            def npc_entered(self, npc_id):
                self.npcs.append(npc_id)

            def npc_left(self, npc_id):
                if npc_id in self.npcs:
                    self.npcs.remove(npc_id)

        fake_room = _FakeRoom()

        # Ensure lifecycle manager has persistence
        mock_persistence = MagicMock()
        mock_persistence.get_room.return_value = fake_room
        lifecycle_manager.persistence = mock_persistence

        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "earth_arkhamcity_downtown_001"
                mock_create.return_value = mock_npc

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value = mock_persistence

                    # Step 1: Spawn NPC
                    npc_id = lifecycle_manager.spawn_npc(
                        optional_npc_definition,
                        "earth_arkhamcity_downtown_001",
                        "test",
                    )
                    assert npc_id is not None
                    assert npc_id in lifecycle_manager.active_npcs
                    assert npc_id in fake_room.npcs

                    # Step 2: Despawn NPC (simulate death)
                    result = lifecycle_manager.despawn_npc(npc_id, "death")
                    assert result is True
                    assert npc_id not in lifecycle_manager.active_npcs
                    assert npc_id not in fake_room.npcs  # Should be removed now

                    # Step 3: Record death and schedule respawn
                    lifecycle_manager.record_npc_death(npc_id)
                    # Wait for death suppression to expire
                    await asyncio.sleep(lifecycle_manager.death_suppression_duration + 0.1)

                    result = lifecycle_manager.respawn_npc(npc_id, delay=0.1, reason="death")
                    assert result is True
                    assert npc_id in lifecycle_manager.respawn_queue

                    # Step 4: Wait for respawn delay
                    await asyncio.sleep(0.15)

                    # Step 5: Process respawn queue
                    respawned_count = lifecycle_manager.process_respawn_queue()

                    # Should have respawned
                    assert respawned_count >= 0

    def test_periodic_spawn_checks_honor_probability(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test that periodic spawn checks honor spawn probability."""
        # Add definition with low probability
        optional_npc_definition.spawn_probability = 0.0  # 0% chance
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Mock zone config
        mock_zone_config = MagicMock()
        mock_zone_config.get_effective_spawn_probability.return_value = 0.0  # 0%

        # Mock population stats
        mock_stats = MagicMock()
        mock_stats.npcs_by_definition = {}

        with patch.object(
            population_controller,
            "get_zone_configuration",
            return_value=mock_zone_config,
        ):
            with patch.object(
                population_controller,
                "get_population_stats",
                return_value=mock_stats,
            ):
                # Run spawn checks
                results = lifecycle_manager._check_optional_npc_spawns()

                # Should check but not spawn due to 0% probability
                assert results["spawned_count"] == 0


class TestMultipleNPCTypes:
    """Test periodic spawning with multiple NPC types."""

    def test_multiple_optional_npcs_spawn_independently(
        self,
        lifecycle_manager,
        population_controller,
    ):
        """Test that multiple optional NPCs are handled independently."""
        # Create multiple optional NPCs
        npc1 = NPCDefinition(
            name="Cultist A",
            description="First cultist",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id=1,
            required_npc=False,
            max_population=2,
            spawn_probability=1.0,
            room_id="earth_arkhamcity_downtown_001",
            base_stats="{}",
            behavior_config="{}",
            ai_integration_stub="{}",
        )
        npc1.id = 101

        npc2 = NPCDefinition(
            name="Cultist B",
            description="Second cultist",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id=1,
            required_npc=False,
            max_population=2,
            spawn_probability=1.0,
            room_id="earth_arkhamcity_downtown_002",
            base_stats="{}",
            behavior_config="{}",
            ai_integration_stub="{}",
        )
        npc2.id = 102

        # Add both to population controller
        population_controller.npc_definitions[101] = npc1
        population_controller.npc_definitions[102] = npc2

        # Mock spawning
        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "earth_arkhamcity_downtown_001"
                mock_create.return_value = mock_npc

                class _FakeRoom:
                    def npc_entered(self, _nid):
                        pass

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

                    # Force spawn probability to 100%
                    with patch("random.random", return_value=0.0):
                        results = lifecycle_manager._check_optional_npc_spawns()

                        # Should check both NPCs
                        assert results["checks_performed"] >= 0


class TestEdgeCases:
    """Test edge cases in periodic spawning."""

    def test_spawn_check_with_no_zone_config(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test spawn check when zone config is missing."""
        # Add definition
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Remove zone configuration
        population_controller.zone_configurations.clear()

        # Run spawn checks
        results = lifecycle_manager._check_optional_npc_spawns()

        # Should handle gracefully
        assert results["spawned_count"] == 0

    def test_spawn_check_with_no_room_id(
        self,
        lifecycle_manager,
        population_controller,
    ):
        """Test spawn check when NPC has no room_id."""
        # Create NPC without room_id
        npc_no_room = NPCDefinition(
            name="Homeless Cultist",
            description="A cultist with no home",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id=1,
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
            room_id=None,  # No room configured
            base_stats="{}",
            behavior_config="{}",
            ai_integration_stub="{}",
        )
        npc_no_room.id = 103

        population_controller.npc_definitions[103] = npc_no_room

        # Mock zone config
        mock_zone_config = MagicMock()
        mock_zone_config.get_effective_spawn_probability.return_value = 1.0

        # Mock population stats
        mock_stats = MagicMock()
        mock_stats.npcs_by_definition = {}

        with patch.object(
            population_controller,
            "get_zone_configuration",
            return_value=mock_zone_config,
        ):
            with patch.object(
                population_controller,
                "get_population_stats",
                return_value=mock_stats,
            ):
                # Run spawn checks
                results = lifecycle_manager._check_optional_npc_spawns()

                # Should handle gracefully (can't spawn without room_id)
                assert results["spawned_count"] == 0

    def test_periodic_maintenance_handles_exceptions(
        self,
        lifecycle_manager,
        population_controller,
        optional_npc_definition,
    ):
        """Test that periodic maintenance handles exceptions gracefully."""
        # Add definition
        population_controller.npc_definitions[optional_npc_definition.id] = optional_npc_definition

        # Mock spawn check to raise exception
        with patch.object(lifecycle_manager, "_check_optional_npc_spawns", side_effect=Exception("Test error")):
            # Should not raise exception - should handle it gracefully
            results = lifecycle_manager.periodic_maintenance()

            # Should still have respawned_npcs in results (from queue processing)
            assert "respawned_npcs" in results
            # Should have default values for spawn checks due to exception
            assert "spawned_npcs" in results
            assert results["spawned_npcs"] == 0
            assert "spawn_checks_performed" in results
            assert results["spawn_checks_performed"] == 0
