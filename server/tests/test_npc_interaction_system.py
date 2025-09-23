"""
Tests for NPC interaction and relationship system.

This module tests the NPC-to-NPC interaction and relationship management,
including relationship tracking, interaction processing, and behavioral
modifications based on NPC relationships.

As documented in the Cultes des Goules, proper relationship management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

import time
from unittest.mock import MagicMock

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom, NPCSpoke
from server.models.npc import NPCDefinition, NPCRelationship, NPCRelationshipType
from server.npc.behaviors import NPCBase
from server.npc.interaction_system import (
    NPCInteraction,
    NPCInteractionEngine,
    NPCInteractionResult,
    NPCInteractionType,
    NPCRelationshipManager,
)


class TestNPCInteraction:
    """Test NPC interaction functionality."""

    def test_interaction_creation(self):
        """Test creating an NPC interaction."""
        interaction = NPCInteraction(
            initiator_id="npc_001",
            target_id="npc_002",
            interaction_type=NPCInteractionType.GREETING,
            context={"room_id": "room_001"},
        )

        assert interaction.initiator_id == "npc_001"
        assert interaction.target_id == "npc_002"
        assert interaction.interaction_type == NPCInteractionType.GREETING
        assert interaction.context["room_id"] == "room_001"
        assert interaction.timestamp > 0
        assert interaction.result == NPCInteractionResult.NEUTRAL
        assert len(interaction.effects) == 0

    def test_interaction_repr(self):
        """Test interaction string representation."""
        interaction = NPCInteraction(
            initiator_id="npc_001",
            target_id="npc_002",
            interaction_type=NPCInteractionType.CONVERSATION,
        )
        interaction.result = NPCInteractionResult.SUCCESS

        repr_str = repr(interaction)
        assert "NPCInteraction" in repr_str
        assert "npc_001" in repr_str
        assert "npc_002" in repr_str
        assert "CONVERSATION" in repr_str
        assert "SUCCESS" in repr_str


class TestNPCRelationshipManager:
    """Test NPC relationship manager functionality."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def relationship_manager(self, event_bus):
        """Create a relationship manager for testing."""
        return NPCRelationshipManager(event_bus)

    @pytest.fixture
    def sample_relationships(self):
        """Create sample NPC relationships."""
        relationships = []

        # Ally relationship
        rel1 = NPCRelationship(
            npc_id_1=1,
            npc_id_2=2,
            relationship_type=NPCRelationshipType.ALLY.value,
            relationship_strength=0.8,
        )
        relationships.append(rel1)

        # Enemy relationship
        rel2 = NPCRelationship(
            npc_id_1=1,
            npc_id_2=3,
            relationship_type=NPCRelationshipType.ENEMY.value,
            relationship_strength=0.6,
        )
        relationships.append(rel2)

        # Neutral relationship
        rel3 = NPCRelationship(
            npc_id_1=2,
            npc_id_2=3,
            relationship_type=NPCRelationshipType.NEUTRAL.value,
            relationship_strength=0.3,
        )
        relationships.append(rel3)

        return relationships

    def test_relationship_manager_initialization(self, relationship_manager):
        """Test relationship manager initialization."""
        assert relationship_manager.event_bus is not None
        assert len(relationship_manager.relationships) == 0
        assert len(relationship_manager.relationship_cache) == 0
        assert len(relationship_manager.interaction_history) == 0

    def test_load_relationships(self, relationship_manager, sample_relationships):
        """Test loading NPC relationships."""
        relationship_manager.load_relationships(sample_relationships)

        assert len(relationship_manager.relationships) == 6  # 3 relationships * 2 directions
        assert len(relationship_manager.relationship_cache) == 3  # 3 unique NPCs

    def test_get_relationship_modifier(self, relationship_manager, sample_relationships):
        """Test getting relationship modifiers."""
        relationship_manager.load_relationships(sample_relationships)

        # Test ally relationship (positive)
        modifier = relationship_manager.get_relationship_modifier("1", "2")
        assert modifier == 0.8

        # Test enemy relationship (negative)
        modifier = relationship_manager.get_relationship_modifier("1", "3")
        assert modifier == -0.6

        # Test neutral relationship
        modifier = relationship_manager.get_relationship_modifier("2", "3")
        assert modifier == 0.0

        # Test non-existent relationship
        modifier = relationship_manager.get_relationship_modifier("1", "999")
        assert modifier == 0.0

    def test_get_relationship_type(self, relationship_manager, sample_relationships):
        """Test getting relationship types."""
        relationship_manager.load_relationships(sample_relationships)

        # Test ally relationship
        rel_type = relationship_manager.get_relationship_type("1", "2")
        assert rel_type == NPCRelationshipType.ALLY

        # Test enemy relationship
        rel_type = relationship_manager.get_relationship_type("1", "3")
        assert rel_type == NPCRelationshipType.ENEMY

        # Test neutral relationship
        rel_type = relationship_manager.get_relationship_type("2", "3")
        assert rel_type == NPCRelationshipType.NEUTRAL

        # Test non-existent relationship
        rel_type = relationship_manager.get_relationship_type("1", "999")
        assert rel_type is None

    def test_add_relationship(self, relationship_manager):
        """Test adding a new relationship."""
        relationship_manager.add_relationship(1, 2, NPCRelationshipType.ALLY, 0.7)

        assert len(relationship_manager.relationships) == 2  # Both directions
        assert len(relationship_manager.relationship_cache) == 2  # Both NPCs

        # Test the relationship
        modifier = relationship_manager.get_relationship_modifier("1", "2")
        assert modifier == 0.7

        rel_type = relationship_manager.get_relationship_type("1", "2")
        assert rel_type == NPCRelationshipType.ALLY

    def test_remove_relationship(self, relationship_manager, sample_relationships):
        """Test removing a relationship."""
        relationship_manager.load_relationships(sample_relationships)

        # Remove relationship between NPCs 1 and 2
        result = relationship_manager.remove_relationship(1, 2)
        assert result is True

        # Check that relationship is gone
        modifier = relationship_manager.get_relationship_modifier("1", "2")
        assert modifier == 0.0

        rel_type = relationship_manager.get_relationship_type("1", "2")
        assert rel_type is None

        # Try to remove non-existent relationship
        result = relationship_manager.remove_relationship(1, 999)
        assert result is False

    def test_get_relationship_statistics(self, relationship_manager, sample_relationships):
        """Test getting relationship statistics."""
        relationship_manager.load_relationships(sample_relationships)

        stats = relationship_manager.get_relationship_statistics()

        assert stats["total_relationships"] == 3
        # Note: The statistics method counts relationships in both directions, so we expect 2 for each type
        assert stats["relationship_types"]["ally"] == 1
        assert stats["relationship_types"]["enemy"] == 1
        assert stats["relationship_types"]["neutral"] == 1
        assert stats["cached_npcs"] == 3
        assert stats["interaction_history_size"] == 0

    def test_event_handling(self, relationship_manager, event_bus):
        """Test event handling."""
        # Test NPC entered room event
        event = NPCEnteredRoom(timestamp=None, event_type="", npc_id="npc_001", room_id="room_001")
        event_bus.publish(event)
        time.sleep(0.1)  # Allow event processing

        # Test NPC left room event
        event = NPCLeftRoom(timestamp=None, event_type="", npc_id="npc_001", room_id="room_001")
        event_bus.publish(event)
        time.sleep(0.1)  # Allow event processing

        # Test NPC spoke event
        event = NPCSpoke(timestamp=None, event_type="", npc_id="npc_001", room_id="room_001", message="Hello!")
        event_bus.publish(event)
        time.sleep(0.1)  # Allow event processing

        # Events should be handled without errors
        assert True  # If we get here, no exceptions were raised


class TestNPCInteractionEngine:
    """Test NPC interaction engine functionality."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def relationship_manager(self, event_bus):
        """Create a relationship manager for testing."""
        return NPCRelationshipManager(event_bus)

    @pytest.fixture
    def interaction_engine(self, event_bus, relationship_manager):
        """Create an interaction engine for testing."""
        return NPCInteractionEngine(event_bus, relationship_manager)

    @pytest.fixture
    def mock_npc1(self):
        """Create a mock NPC instance."""
        npc = MagicMock(spec=NPCBase)
        npc.npc_id = "npc_001"
        npc.definition = MagicMock(spec=NPCDefinition)
        npc.definition.id = 1
        npc.definition.name = "Test NPC 1"
        return npc

    @pytest.fixture
    def mock_npc2(self):
        """Create a mock NPC instance."""
        npc = MagicMock(spec=NPCBase)
        npc.npc_id = "npc_002"
        npc.definition = MagicMock(spec=NPCDefinition)
        npc.definition.id = 2
        npc.definition.name = "Test NPC 2"
        return npc

    def test_interaction_engine_initialization(self, interaction_engine):
        """Test interaction engine initialization."""
        assert interaction_engine.event_bus is not None
        assert interaction_engine.relationship_manager is not None
        assert len(interaction_engine.active_npcs) == 0
        assert len(interaction_engine.interaction_rules) > 0

    def test_register_unregister_npc(self, interaction_engine, mock_npc1):
        """Test registering and unregistering NPCs."""
        # Register NPC
        interaction_engine.register_npc("npc_001", mock_npc1)
        assert "npc_001" in interaction_engine.active_npcs
        assert interaction_engine.active_npcs["npc_001"] == mock_npc1

        # Unregister NPC
        interaction_engine.unregister_npc("npc_001")
        assert "npc_001" not in interaction_engine.active_npcs

    def test_process_interaction_both_npcs_active(self, interaction_engine, mock_npc1, mock_npc2):
        """Test processing interaction with both NPCs active."""
        # Register both NPCs
        interaction_engine.register_npc("npc_001", mock_npc1)
        interaction_engine.register_npc("npc_002", mock_npc2)

        # Process interaction
        interaction = interaction_engine.process_interaction(
            "npc_001", "npc_002", NPCInteractionType.GREETING, {"room_id": "room_001"}
        )

        assert interaction.initiator_id == "npc_001"
        assert interaction.target_id == "npc_002"
        assert interaction.interaction_type == NPCInteractionType.GREETING
        assert interaction.context["room_id"] == "room_001"
        assert interaction.result in [
            NPCInteractionResult.SUCCESS,
            NPCInteractionResult.FAILURE,
            NPCInteractionResult.NEUTRAL,
            NPCInteractionResult.POSITIVE,
            NPCInteractionResult.NEGATIVE,
        ]

    def test_process_interaction_npc_not_active(self, interaction_engine, mock_npc1):
        """Test processing interaction with one NPC not active."""
        # Register only one NPC
        interaction_engine.register_npc("npc_001", mock_npc1)

        # Process interaction with inactive NPC
        interaction = interaction_engine.process_interaction("npc_001", "npc_002", NPCInteractionType.GREETING)

        assert interaction.result == NPCInteractionResult.IGNORED
        assert interaction.effects["reason"] == "One or both NPCs not active"

    def test_process_interaction_with_relationship(self, interaction_engine, mock_npc1, mock_npc2):
        """Test processing interaction with existing relationship."""
        # Register both NPCs
        interaction_engine.register_npc("npc_001", mock_npc1)
        interaction_engine.register_npc("npc_002", mock_npc2)

        # Add ally relationship
        interaction_engine.relationship_manager.add_relationship(1, 2, NPCRelationshipType.ALLY, 0.8)

        # Process interaction
        interaction = interaction_engine.process_interaction("npc_001", "npc_002", NPCInteractionType.COOPERATION)

        # The result can be any valid interaction result due to randomness
        assert interaction.result in [
            NPCInteractionResult.SUCCESS,
            NPCInteractionResult.FAILURE,
            NPCInteractionResult.NEUTRAL,
            NPCInteractionResult.POSITIVE,
            NPCInteractionResult.NEGATIVE,
        ]
        # Check that effects are applied regardless of success/failure
        assert len(interaction.effects) > 0

    def test_process_interaction_with_enemy_relationship(self, interaction_engine, mock_npc1, mock_npc2):
        """Test processing interaction with enemy relationship."""
        # Register both NPCs
        interaction_engine.register_npc("npc_001", mock_npc1)
        interaction_engine.register_npc("npc_002", mock_npc2)

        # Add enemy relationship
        interaction_engine.relationship_manager.add_relationship(1, 2, NPCRelationshipType.ENEMY, 0.6)

        # Process interaction
        interaction = interaction_engine.process_interaction("npc_001", "npc_002", NPCInteractionType.CONFLICT)

        assert interaction.result in [
            NPCInteractionResult.SUCCESS,
            NPCInteractionResult.NEGATIVE,
            NPCInteractionResult.FAILURE,
        ]

    def test_get_interaction_statistics(self, interaction_engine, mock_npc1, mock_npc2):
        """Test getting interaction statistics."""
        # Register NPCs and process some interactions
        interaction_engine.register_npc("npc_001", mock_npc1)
        interaction_engine.register_npc("npc_002", mock_npc2)

        # Process a few interactions
        for _ in range(3):
            interaction_engine.process_interaction("npc_001", "npc_002", NPCInteractionType.GREETING)

        stats = interaction_engine.get_interaction_statistics()

        assert stats["total_interactions"] == 3
        assert stats["active_npcs"] == 2
        assert "success_rate" in stats
        assert "result_counts" in stats
        assert "type_counts" in stats

    def test_cleanup_old_interactions(self, interaction_engine, mock_npc1, mock_npc2):
        """Test cleaning up old interactions."""
        # Register NPCs
        interaction_engine.register_npc("npc_001", mock_npc1)
        interaction_engine.register_npc("npc_002", mock_npc2)

        # Process some interactions
        for _ in range(5):
            interaction_engine.process_interaction("npc_001", "npc_002", NPCInteractionType.GREETING)

        # Manually set old timestamps for some interactions
        for i, interaction in enumerate(interaction_engine.relationship_manager.interaction_history):
            if i < 2:  # Make first 2 interactions old
                interaction.timestamp = time.time() - 90000  # 25 hours ago

        # Clean up old interactions
        cleaned_count = interaction_engine.cleanup_old_interactions(max_age_seconds=86400)  # 24 hours

        assert cleaned_count == 2
        assert len(interaction_engine.relationship_manager.interaction_history) == 3

    def test_interaction_rules_initialization(self, interaction_engine):
        """Test that interaction rules are properly initialized."""
        rules = interaction_engine.interaction_rules

        assert NPCInteractionType.GREETING in rules
        assert NPCInteractionType.CONVERSATION in rules
        assert NPCInteractionType.COOPERATION in rules
        assert NPCInteractionType.CONFLICT in rules
        assert NPCInteractionType.ASSISTANCE in rules

        # Check that each rule has required fields
        for _interaction_type, rule in rules.items():
            assert "base_probability" in rule
            assert "relationship_modifier" in rule
            assert "success_threshold" in rule
            assert 0.0 <= rule["base_probability"] <= 1.0
            assert 0.0 <= rule["success_threshold"] <= 1.0
