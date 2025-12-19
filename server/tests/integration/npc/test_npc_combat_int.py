"""
NPC combat integration tests for MythosMUD.
"""

import asyncio
from unittest.mock import MagicMock

import pytest

from server.models.npc import NPCDefinitionType
from server.npc.behaviors import AggressiveMobNPC


@pytest.fixture
def event_bus():
    """Create an event bus for testing."""
    from server.events.event_bus import EventBus

    return EventBus()


class TestNPCCombatIntegration:
    """Test NPC integration with the combat system."""

    @pytest.fixture
    def mock_aggressive_npc_definition(self):
        """Create a mock aggressive NPC definition for testing."""
        npc_def = MagicMock()
        npc_def.id = 2
        npc_def.name = "Test Cultist"
        npc_def.npc_type = NPCDefinitionType.AGGRESSIVE_MOB
        npc_def.room_id = "room1"
        npc_def.base_stats = '{"determination_points": 120, "max_dp": 120, "strength": 15, "attack_damage": 25}'
        npc_def.behavior_config = '{"hunt_range": 5, "attack_damage": 25, "flee_threshold": 0.3}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def aggressive_npc(self, mock_aggressive_npc_definition, event_bus):
        """Create an aggressive NPC for testing."""
        npc = AggressiveMobNPC(mock_aggressive_npc_definition, "aggressive_npc_1")
        npc.event_bus = event_bus
        return npc

    def test_npc_combat_stats_integration(self, aggressive_npc) -> None:
        """Test that NPC stats integrate with combat mechanics."""
        stats = aggressive_npc.get_stats()
        assert "strength" in stats
        assert stats["strength"] == 15
        dp = stats.get("determination_points", stats.get("dp", stats.get("hp", None)))
        assert dp is not None
        assert dp == 120

    def test_npc_damage_system_integration(self, aggressive_npc) -> None:
        """Test NPC damage system integration."""
        stats = aggressive_npc.get_stats()
        initial_dp = stats.get("determination_points", stats.get("dp", stats.get("hp", 120)))
        result = aggressive_npc.take_damage(30)
        assert result is True
        new_stats = aggressive_npc.get_stats()
        new_dp = new_stats.get("determination_points", new_stats.get("dp", new_stats.get("hp", 120)))
        assert new_dp == initial_dp - 30

    def test_npc_combat_behavior_integration(self, aggressive_npc) -> None:
        """Test NPC combat behavior integration."""
        assert aggressive_npc.attack_target("test_player_1") is True
        assert aggressive_npc.hunt_target("test_player_1") is True
        assert aggressive_npc.flee() is True

    @pytest.mark.asyncio
    async def test_npc_combat_events_integration(self, aggressive_npc, event_bus) -> None:
        """Test NPC combat event integration."""
        events_received = []

        def capture_combat_events(event):
            events_received.append(event)

        from server.events.event_types import NPCAttacked, NPCDied, NPCTookDamage

        event_bus.subscribe(NPCAttacked, capture_combat_events)
        event_bus.subscribe(NPCTookDamage, capture_combat_events)
        event_bus.subscribe(NPCDied, capture_combat_events)
        aggressive_npc.attack_target("test_player_1")
        await asyncio.sleep(0.1)
        assert len(events_received) >= 1
        attacked_event = next((e for e in events_received if e.event_type == "NPCAttacked"), None)
        assert attacked_event is not None
        assert attacked_event.npc_id == "aggressive_npc_1"
        assert attacked_event.target_id == "test_player_1"

    @pytest.mark.asyncio
    async def test_npc_death_events_integration(self, aggressive_npc, event_bus) -> None:
        """Test NPC death event integration."""
        events_received = []

        def capture_death_events(event):
            events_received.append(event)

        from server.events.event_types import NPCDied, NPCTookDamage

        event_bus.subscribe(NPCDied, capture_death_events)
        event_bus.subscribe(NPCTookDamage, capture_death_events)
        stats = aggressive_npc.get_stats()
        initial_dp = stats.get("determination_points", stats.get("dp", stats.get("hp", 120)))
        aggressive_npc.take_damage(initial_dp, "physical", "test_player_1")
        await asyncio.sleep(0.1)
        assert len(events_received) == 2
        assert any(e.event_type == "NPCDied" for e in events_received)
