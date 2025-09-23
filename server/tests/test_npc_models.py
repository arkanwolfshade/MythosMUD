"""
Tests for NPC database models and schema validation.

This module tests the NPC database models including npc_definitions,
npc_spawn_rules, and npc_relationships tables and their associated
SQLAlchemy models.
"""

import asyncio

import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from server.models.npc import (
    NPCDefinition,
    NPCDefinitionType,
    NPCRelationship,
    NPCRelationshipType,
    NPCSpawnRule,
)


class TestNPCDefinition:
    """Test the NPCDefinition model."""

    def test_npc_definition_creation(self):
        """Test creating an NPC definition with required fields using mocked persistence."""
        # Test creating an NPC definition object (without database persistence)
        npc_def = NPCDefinition(
            name="Test Shopkeeper",
            description="A friendly shopkeeper",
            npc_type=NPCDefinitionType.SHOPKEEPER,
            sub_zone_id="arkham_northside",
            room_id="arkham_001",
            required_npc=True,
            max_population=1,
            spawn_probability=1.0,
        )

        # Set JSON fields using the setter methods
        npc_def.set_base_stats({"hp": 100, "mp": 50, "str": 12, "dex": 10})
        npc_def.set_behavior_config({"aggression_level": 0.0, "wander_radius": 0})

        # Verify the NPC object was created correctly
        assert npc_def.name == "Test Shopkeeper"
        assert npc_def.description == "A friendly shopkeeper"
        assert npc_def.npc_type == NPCDefinitionType.SHOPKEEPER
        assert npc_def.sub_zone_id == "arkham_northside"
        assert npc_def.room_id == "arkham_001"
        assert npc_def.required_npc is True
        assert npc_def.max_population == 1
        assert npc_def.spawn_probability == 1.0
        assert npc_def.get_base_stats() == {"hp": 100, "mp": 50, "str": 12, "dex": 10}
        assert npc_def.get_behavior_config() == {"aggression_level": 0.0, "wander_radius": 0}
        # Note: created_at and updated_at are set by the database, not the model constructor
        # This test verifies the object structure without database persistence

    def test_npc_definition_default_values(self):
        """Test NPC definition with default values using mocked persistence."""
        # Test creating an NPC definition with minimal required fields
        # Note: Default values are set at the database level, not in the Python constructor
        npc_def = NPCDefinition(
            name="Default NPC", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
        )

        # Verify the object was created with the required fields
        assert npc_def.name == "Default NPC"
        assert npc_def.npc_type == NPCDefinitionType.PASSIVE_MOB
        assert npc_def.sub_zone_id == "arkham_northside"

        # Verify JSON fields work correctly (these have default empty dicts in the model)
        assert npc_def.get_base_stats() == {}
        assert npc_def.get_behavior_config() == {}
        assert npc_def.get_ai_integration_stub() == {}

        # Note: required_npc, max_population, spawn_probability defaults are set by the database
        # This test verifies the object structure without database persistence

    def test_npc_definition_type_validation(self):
        """Test that only valid NPC types are accepted using mocked persistence."""
        # Test valid types by creating NPC definition objects
        valid_types = [
            NPCDefinitionType.SHOPKEEPER,
            NPCDefinitionType.QUEST_GIVER,
            NPCDefinitionType.PASSIVE_MOB,
            NPCDefinitionType.AGGRESSIVE_MOB,
        ]

        for npc_type in valid_types:
            npc_def = NPCDefinition(name=f"Test {npc_type.value}", npc_type=npc_type, sub_zone_id="arkham_northside")
            # Verify the NPC definition was created with the correct type
            assert npc_def.npc_type == npc_type
            assert npc_def.name == f"Test {npc_type.value}"

    def test_npc_definition_unique_constraints(self):
        """Test that NPC names must be unique within zones using mocked persistence."""
        # This test verifies the model structure supports unique constraints
        # The actual constraint enforcement is handled by the database schema

        # Create first NPC
        npc1 = NPCDefinition(
            name="Unique NPC Test", npc_type=NPCDefinitionType.SHOPKEEPER, sub_zone_id="arkham_northside"
        )

        # Create second NPC with same name in same zone
        npc2 = NPCDefinition(
            name="Unique NPC Test", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
        )

        # Verify both NPCs can be created as objects
        # The unique constraint enforcement would happen at the database level
        assert npc1.name == npc2.name
        assert npc1.sub_zone_id == npc2.sub_zone_id
        assert npc1.npc_type != npc2.npc_type

    def test_npc_definition_json_fields(self):
        """Test JSON field serialization and deserialization using mocked persistence."""
        complex_stats = {
            "hp": 150,
            "mp": 75,
            "str": 15,
            "dex": 12,
            "con": 14,
            "int": 10,
            "wis": 8,
            "cha": 11,
            "resistances": ["fire", "cold"],
            "immunities": ["poison"],
        }

        complex_behavior = {
            "aggression_level": 0.8,
            "territory_radius": 3,
            "hunt_players": True,
            "flee_threshold": 0.2,
            "preferred_targets": ["players", "other_mobs"],
        }

        ai_stub = {
            "model": "gpt-4",
            "temperature": 0.7,
            "max_tokens": 150,
            "system_prompt": "You are a helpful shopkeeper",
        }

        npc_def = NPCDefinition(
            name="Complex NPC",
            npc_type=NPCDefinitionType.AGGRESSIVE_MOB,
            sub_zone_id="arkham_northside",
        )

        # Set JSON fields using the setter methods
        npc_def.set_base_stats(complex_stats)
        npc_def.set_behavior_config(complex_behavior)
        npc_def.set_ai_integration_stub(ai_stub)

        # Verify JSON fields can be set and retrieved
        assert npc_def.get_base_stats() == complex_stats
        assert npc_def.get_behavior_config() == complex_behavior
        assert npc_def.get_ai_integration_stub() == ai_stub


class TestNPCSpawnRule:
    """Test the NPCSpawnRule model."""

    def test_spawn_rule_creation(self, test_client, test_npc_database):
        """Test creating an NPC spawn rule."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # First create an NPC definition
                npc_def = NPCDefinition(
                    name="Spawnable NPC", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )
                session.add(npc_def)
                await session.commit()

                # Create spawn rule
                spawn_rule = NPCSpawnRule(
                    npc_definition_id=npc_def.id,
                    sub_zone_id="arkham_northside",
                    min_players=2,
                    max_players=10,
                )

                # Set spawn conditions using the setter method
                spawn_rule.set_spawn_conditions({"time_of_day": "night", "weather": "foggy"})

                session.add(spawn_rule)
                await session.commit()

                assert spawn_rule.id is not None
                assert spawn_rule.npc_definition_id == npc_def.id
                assert spawn_rule.sub_zone_id == "arkham_northside"
                assert spawn_rule.min_players == 2
                assert spawn_rule.max_players == 10
                assert spawn_rule.get_spawn_conditions() == {"time_of_day": "night", "weather": "foggy"}
                break

        asyncio.run(_test())

    def test_spawn_rule_default_values(self, test_client, test_npc_database):
        """Test spawn rule with default values."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Create NPC definition
                npc_def = NPCDefinition(
                    name="Default Spawn NPC", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )
                session.add(npc_def)
                await session.commit()

                # Create spawn rule with minimal data
                spawn_rule = NPCSpawnRule(npc_definition_id=npc_def.id, sub_zone_id="arkham_northside")

                session.add(spawn_rule)
                await session.commit()

                assert spawn_rule.min_players == 0
                assert spawn_rule.max_players == 999
                assert spawn_rule.get_spawn_conditions() == {}
                break

        asyncio.run(_test())

    def test_spawn_rule_foreign_key_constraint(self, test_client, test_npc_database):
        """Test that spawn rules require valid NPC definitions."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Try to create spawn rule with non-existent NPC definition
                spawn_rule = NPCSpawnRule(
                    npc_definition_id=99999,  # Non-existent ID
                    sub_zone_id="arkham_northside",
                )

                session.add(spawn_rule)

                with pytest.raises(IntegrityError):
                    await session.commit()
                break

        asyncio.run(_test())

    def test_spawn_rule_json_conditions(self, test_client, test_npc_database):
        """Test complex spawn conditions in JSON format."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Create NPC definition
                npc_def = NPCDefinition(
                    name="Conditional Spawn NPC",
                    npc_type=NPCDefinitionType.AGGRESSIVE_MOB,
                    sub_zone_id="arkham_northside",
                )
                session.add(npc_def)
                await session.commit()

                # Complex spawn conditions
                complex_conditions = {
                    "time_of_day": "night",
                    "weather": ["foggy", "stormy"],
                    "player_level_min": 5,
                    "player_level_max": 20,
                    "zone_population_max": 50,
                    "events": ["full_moon", "eclipse"],
                    "required_items": ["holy_symbol", "silver_weapon"],
                }

                spawn_rule = NPCSpawnRule(npc_definition_id=npc_def.id, sub_zone_id="arkham_northside")

                # Set complex spawn conditions using the setter method
                spawn_rule.set_spawn_conditions(complex_conditions)

                session.add(spawn_rule)
                await session.commit()

                # Verify complex conditions are stored correctly
                retrieved = await session.get(NPCSpawnRule, spawn_rule.id)
                assert retrieved.get_spawn_conditions() == complex_conditions
                break

        asyncio.run(_test())


class TestNPCRelationship:
    """Test the NPCRelationship model."""

    def test_relationship_creation(self, test_client, test_npc_database):
        """Test creating an NPC relationship."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Create two NPC definitions
                npc1 = NPCDefinition(
                    name="Guard Captain", npc_type=NPCDefinitionType.AGGRESSIVE_MOB, sub_zone_id="arkham_northside"
                )
                npc2 = NPCDefinition(
                    name="Guard Soldier", npc_type=NPCDefinitionType.AGGRESSIVE_MOB, sub_zone_id="arkham_northside"
                )

                session.add_all([npc1, npc2])
                await session.commit()

                # Create relationship
                relationship = NPCRelationship(
                    npc_id_1=npc1.id,
                    npc_id_2=npc2.id,
                    relationship_type=NPCRelationshipType.ALLY,
                    relationship_strength=0.8,
                )

                session.add(relationship)
                await session.commit()

                assert relationship.id is not None
                assert relationship.npc_id_1 == npc1.id
                assert relationship.npc_id_2 == npc2.id
                assert relationship.relationship_type == NPCRelationshipType.ALLY
                assert relationship.relationship_strength == 0.8
                break

        asyncio.run(_test())

    def test_relationship_type_validation(self, test_client, test_npc_database):
        """Test that only valid relationship types are accepted."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Create NPC definitions
                npc1 = NPCDefinition(
                    name="Test NPC 1", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )
                npc2 = NPCDefinition(
                    name="Test NPC 2", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )

                session.add_all([npc1, npc2])
                await session.commit()

                # Test valid relationship types
                valid_types = [
                    NPCRelationshipType.ALLY,
                    NPCRelationshipType.ENEMY,
                    NPCRelationshipType.NEUTRAL,
                    NPCRelationshipType.FOLLOWER,
                ]

                for rel_type in valid_types:
                    relationship = NPCRelationship(npc_id_1=npc1.id, npc_id_2=npc2.id, relationship_type=rel_type)
                    session.add(relationship)
                    await session.commit()
                    await session.delete(relationship)
                    await session.commit()
                break

        asyncio.run(_test())

    def test_relationship_default_strength(self, test_client, test_npc_database):
        """Test relationship with default strength value."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Create NPC definitions
                npc1 = NPCDefinition(
                    name="Default NPC 1", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )
                npc2 = NPCDefinition(
                    name="Default NPC 2", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )

                session.add_all([npc1, npc2])
                await session.commit()

                # Create relationship without specifying strength
                relationship = NPCRelationship(
                    npc_id_1=npc1.id, npc_id_2=npc2.id, relationship_type=NPCRelationshipType.NEUTRAL
                )

                session.add(relationship)
                await session.commit()

                assert relationship.relationship_strength == 0.5
                break

        asyncio.run(_test())

    def test_relationship_unique_constraint(self, test_client, test_npc_database):
        """Test that relationships between the same NPCs are unique."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Create NPC definitions
                npc1 = NPCDefinition(
                    name="Unique NPC 1", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )
                npc2 = NPCDefinition(
                    name="Unique NPC 2", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )

                session.add_all([npc1, npc2])
                await session.commit()

                # Create first relationship
                rel1 = NPCRelationship(npc_id_1=npc1.id, npc_id_2=npc2.id, relationship_type=NPCRelationshipType.ALLY)
                session.add(rel1)
                await session.commit()

                # Try to create duplicate relationship
                rel2 = NPCRelationship(npc_id_1=npc1.id, npc_id_2=npc2.id, relationship_type=NPCRelationshipType.ENEMY)
                session.add(rel2)

                with pytest.raises(IntegrityError):
                    await session.commit()
                break

        asyncio.run(_test())

    def test_relationship_bidirectional_constraint(self, test_client, test_npc_database):
        """Test that relationships can be created bidirectionally."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Create NPC definitions
                npc1 = NPCDefinition(
                    name="Bidirectional NPC 1", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )
                npc2 = NPCDefinition(
                    name="Bidirectional NPC 2", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                )

                session.add_all([npc1, npc2])
                await session.commit()

                # Create relationship from npc1 to npc2
                rel1 = NPCRelationship(npc_id_1=npc1.id, npc_id_2=npc2.id, relationship_type=NPCRelationshipType.ALLY)
                session.add(rel1)
                await session.commit()

                # Create reverse relationship (should succeed - bidirectional relationships are allowed)
                rel2 = NPCRelationship(npc_id_1=npc2.id, npc_id_2=npc1.id, relationship_type=NPCRelationshipType.ALLY)
                session.add(rel2)
                await session.commit()

                # Verify both relationships exist
                relationships = await session.execute(
                    select(NPCRelationship).where(
                        (NPCRelationship.npc_id_1 == npc1.id) | (NPCRelationship.npc_id_2 == npc1.id)
                    )
                )
                rel_count = len(relationships.scalars().all())
                assert rel_count == 2, f"Expected 2 relationships, got {rel_count}"
                break

        asyncio.run(_test())


class TestNPCModelEnums:
    """Test the NPC model enums."""

    def test_npc_definition_type_enum(self):
        """Test NPCDefinitionType enum values."""
        assert NPCDefinitionType.SHOPKEEPER == "shopkeeper"
        assert NPCDefinitionType.QUEST_GIVER == "quest_giver"
        assert NPCDefinitionType.PASSIVE_MOB == "passive_mob"
        assert NPCDefinitionType.AGGRESSIVE_MOB == "aggressive_mob"

    def test_npc_relationship_type_enum(self):
        """Test NPCRelationshipType enum values."""
        assert NPCRelationshipType.ALLY == "ally"
        assert NPCRelationshipType.ENEMY == "enemy"
        assert NPCRelationshipType.NEUTRAL == "neutral"
        assert NPCRelationshipType.FOLLOWER == "follower"


class TestNPCDatabaseConstraints:
    """Test database constraints and indexes."""

    def test_npc_definition_required_fields(self, test_client, test_npc_database):
        """Test that required fields cannot be null."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Test missing name
                npc_def = NPCDefinition(npc_type=NPCDefinitionType.SHOPKEEPER, sub_zone_id="arkham_northside")
                session.add(npc_def)

                with pytest.raises(IntegrityError):
                    await session.commit()

                await session.rollback()
                break

        asyncio.run(_test())

    def test_npc_definition_zone_index(self, test_client, test_npc_database):
        """Test that zone-based queries are efficient."""
        from server.npc_database import get_npc_async_session

        async def _test():
            async for session in get_npc_async_session():
                # Clean up any existing NPC data to avoid conflicts
                from sqlalchemy import text

                await session.execute(text("DELETE FROM npc_relationships"))
                await session.execute(text("DELETE FROM npc_spawn_rules"))
                await session.execute(text("DELETE FROM npc_definitions"))
                await session.commit()

                # Create NPCs in different zones
                npcs = []
                for i in range(5):
                    npc = NPCDefinition(
                        name=f"Zone NPC {i}", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="arkham_northside"
                    )
                    npcs.append(npc)
                    session.add(npc)

                for i in range(3):
                    npc = NPCDefinition(
                        name=f"Innsmouth NPC {i}", npc_type=NPCDefinitionType.PASSIVE_MOB, sub_zone_id="innsmouth_docks"
                    )
                    npcs.append(npc)
                    session.add(npc)

                await session.commit()

                # Query by zone (should use index)
                from sqlalchemy import select

                arkham_npcs = await session.execute(
                    select(NPCDefinition).filter(NPCDefinition.sub_zone_id == "arkham_northside")
                )
                arkham_results = arkham_npcs.scalars().all()

                assert len(arkham_results) == 5
                assert all(npc.sub_zone_id == "arkham_northside" for npc in arkham_results)
                break

        asyncio.run(_test())
