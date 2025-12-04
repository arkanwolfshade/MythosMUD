"""
Tests for NPC Spawning Service.

This module tests the NPC spawning logic that integrates with the population
control system to spawn NPCs based on rules and game state conditions.

AI Agent: Tests for NPCSpawningService covering spawn request handling,
         NPC instantiation, and spawn rule evaluation with mocked dependencies.
"""

# pylint: disable=redefined-outer-name,protected-access
# Justification: pytest fixtures redefine names, protected access needed for testing internals

from unittest.mock import Mock

import pytest

from server.npc.spawning_service import (
    NPCSpawnRequest,
    SimpleNPCDefinition,
)


@pytest.fixture
def simple_npc_definition():
    """Provide simple NPC definition for testing."""
    return SimpleNPCDefinition(
        id=1,
        name="Test NPC",
        npc_type="passive_mob",
        room_id="earth_arkhamcity_northside_alley_01",
        base_stats='{"health": 100, "attack": 10}',
        behavior_config='{"wander": true}',
        ai_integration_stub='{"enabled": false}',
    )


class TestSimpleNPCDefinition:
    """Test SimpleNPCDefinition dataclass."""

    def test_initialization(self, simple_npc_definition):
        """Test SimpleNPCDefinition initializes correctly."""
        assert simple_npc_definition.id == 1
        assert simple_npc_definition.name == "Test NPC"
        assert simple_npc_definition.npc_type == "passive_mob"
        assert simple_npc_definition.room_id == "earth_arkhamcity_northside_alley_01"

    def test_base_stats_is_string(self, simple_npc_definition):
        """Test base_stats is stored as string."""
        assert isinstance(simple_npc_definition.base_stats, str)
        assert "health" in simple_npc_definition.base_stats

    def test_behavior_config_is_string(self, simple_npc_definition):
        """Test behavior_config is stored as string."""
        assert isinstance(simple_npc_definition.behavior_config, str)
        assert "wander" in simple_npc_definition.behavior_config

    def test_ai_integration_stub_is_string(self, simple_npc_definition):
        """Test ai_integration_stub is stored as string."""
        assert isinstance(simple_npc_definition.ai_integration_stub, str)
        assert "enabled" in simple_npc_definition.ai_integration_stub


class TestNPCSpawnRequest:
    """Test NPCSpawnRequest class."""

    def test_spawn_request_initialization_without_rule(self):
        """Test spawn request initializes without spawn rule."""
        mock_definition = Mock()
        mock_definition.id = 1
        mock_definition.name = "Guard"

        request = NPCSpawnRequest(definition=mock_definition, room_id="room1", spawn_rule=None)

        assert request.definition == mock_definition
        assert request.room_id == "room1"
        assert request.spawn_rule is None

    def test_spawn_request_initialization_with_rule(self):
        """Test spawn request initializes with spawn rule."""
        mock_definition = Mock()
        mock_definition.id = 1

        mock_spawn_rule = Mock()
        mock_spawn_rule.id = 100

        request = NPCSpawnRequest(definition=mock_definition, room_id="room2", spawn_rule=mock_spawn_rule)

        assert request.definition == mock_definition
        assert request.room_id == "room2"
        assert request.spawn_rule == mock_spawn_rule

    def test_spawn_request_stores_definition(self):
        """Test spawn request properly stores NPC definition reference."""
        mock_definition = Mock()
        mock_definition.name = "Shopkeeper"
        mock_definition.npc_type = "shopkeeper"

        request = NPCSpawnRequest(definition=mock_definition, room_id="shop_room")

        assert request.definition.name == "Shopkeeper"
        assert request.definition.npc_type == "shopkeeper"
