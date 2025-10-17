"""
Tests for combat system database schema and migration.

This module tests the database schema extensions for combat data,
including JSON field validation and data migration scripts.
"""

import json

import pytest
from sqlalchemy import text

from server.database import get_async_session, init_db
from server.models.npc import NPCDefinition


class TestCombatDatabaseSchema:
    """Test combat database schema extensions."""

    @pytest.mark.asyncio
    async def test_npc_definition_combat_fields_exist(self):
        """Test that NPC definition table has required combat fields."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            # Check that base_stats and behavior_config columns exist
            result = await session.execute(text("PRAGMA table_info(npc_definitions)"))
            columns = [row[1] for row in result.fetchall()]

            assert "base_stats" in columns
            assert "behavior_config" in columns

    @pytest.mark.asyncio
    async def test_base_stats_json_structure(self):
        """Test base_stats JSON field structure for combat data."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            # Create test NPC with combat stats
            npc = NPCDefinition(
                name="Test Rat",
                npc_type="passive_mob",
                sub_zone_id="test_zone",
                base_stats='{"hp": 10, "max_hp": 10, "xp_value": 5, "dexterity": 12}',
                behavior_config="{}",
            )

            session.add(npc)
            await session.commit()
            await session.refresh(npc)

            # Test JSON parsing
            stats = npc.get_base_stats()
            assert stats["hp"] == 10
            assert stats["max_hp"] == 10
            assert stats["xp_value"] == 5
            assert stats["dexterity"] == 12

    @pytest.mark.asyncio
    async def test_behavior_config_combat_messages(self):
        """Test behavior_config JSON field for combat messages."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            combat_messages = {
                "attack_attacker": "You swing your fist at {target_name} and hit for {damage} damage",
                "attack_defender": "{attacker_name} swings their fist at you and hits you for {damage} damage",
                "attack_other": "{attacker_name} swings their fist at {target_name} and hits for {damage} damage",
                "death_message": "The {npc_name} collapses, dead",
            }

            npc = NPCDefinition(
                name="Test Goblin",
                npc_type="aggressive_mob",
                sub_zone_id="test_zone",
                base_stats='{"hp": 15, "max_hp": 15, "xp_value": 10}',
                behavior_config=json.dumps({"combat_messages": combat_messages}),
            )

            session.add(npc)
            await session.commit()
            await session.refresh(npc)

            # Test JSON parsing
            config = npc.get_behavior_config()
            assert "combat_messages" in config
            assert config["combat_messages"]["attack_attacker"] == combat_messages["attack_attacker"]
            assert config["combat_messages"]["death_message"] == combat_messages["death_message"]

    @pytest.mark.asyncio
    async def test_combat_data_validation(self):
        """Test validation of combat data in JSON fields."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            # Test valid combat data
            valid_stats = {"hp": 10, "max_hp": 10, "xp_value": 5, "dexterity": 12, "strength": 10, "constitution": 8}

            npc = NPCDefinition(
                name="Valid Combat NPC",
                npc_type="passive_mob",
                sub_zone_id="test_zone",
                base_stats=json.dumps(valid_stats),
                behavior_config="{}",
            )

            session.add(npc)
            await session.commit()
            await session.refresh(npc)

            # Verify data integrity
            stats = npc.get_base_stats()
            assert stats["xp_value"] >= 0  # XP should be non-negative
            assert 1 <= stats["dexterity"] <= 20  # Dexterity should be 1-20
            assert 1 <= stats["strength"] <= 20  # Strength should be 1-20
            assert 1 <= stats["constitution"] <= 20  # Constitution should be 1-20

    @pytest.mark.asyncio
    async def test_invalid_combat_data_handling(self):
        """Test handling of invalid combat data."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            # Test invalid JSON
            npc = NPCDefinition(
                name="Invalid JSON NPC",
                npc_type="passive_mob",
                sub_zone_id="test_zone",
                base_stats='{"invalid": json}',  # Invalid JSON
                behavior_config="{}",
            )

            session.add(npc)
            await session.commit()
            await session.refresh(npc)

            # Should return empty dict for invalid JSON
            stats = npc.get_base_stats()
            assert stats == {}

    @pytest.mark.asyncio
    async def test_combat_message_template_validation(self):
        """Test validation of combat message templates."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            # Test message templates with required variables
            combat_messages = {
                "attack_attacker": "You swing your fist at {target_name} and hit for {damage} damage",
                "attack_defender": "{attacker_name} swings their fist at you and hits you for {damage} damage",
                "attack_other": "{attacker_name} swings their fist at {target_name} and hits for {damage} damage",
                "death_message": "The {npc_name} collapses, dead",
            }

            npc = NPCDefinition(
                name="Template Test NPC",
                npc_type="passive_mob",
                sub_zone_id="test_zone",
                base_stats='{"hp": 10, "max_hp": 10, "xp_value": 5}',
                behavior_config=json.dumps({"combat_messages": combat_messages}),
            )

            session.add(npc)
            await session.commit()
            await session.refresh(npc)

            # Verify message templates contain required variables
            config = npc.get_behavior_config()
            messages = config["combat_messages"]

            # Check for required variable placeholders
            assert "{target_name}" in messages["attack_attacker"]
            assert "{damage}" in messages["attack_attacker"]
            assert "{attacker_name}" in messages["attack_defender"]
            assert "{npc_name}" in messages["death_message"]


class TestCombatDataMigration:
    """Test combat data migration scripts."""

    @pytest.mark.asyncio
    async def test_migration_adds_default_combat_data(self):
        """Test that migration adds default combat data to existing NPCs."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            # Create NPC without combat data
            npc = NPCDefinition(
                name="Pre-Migration NPC",
                npc_type="passive_mob",
                sub_zone_id="test_zone",
                base_stats='{"hp": 10}',
                behavior_config="{}",
            )

            session.add(npc)
            await session.commit()
            await session.refresh(npc)

            # Simulate migration by adding default combat data
            stats = npc.get_base_stats()
            stats.update(
                {
                    "xp_value": 1,  # Default XP
                    "dexterity": 10,  # Default dexterity
                    "strength": 10,  # Default strength
                    "constitution": 8,  # Default constitution
                }
            )
            npc.set_base_stats(stats)

            # Add default combat messages
            config = npc.get_behavior_config()
            config["combat_messages"] = {
                "attack_attacker": "You swing your fist at {target_name} and hit for {damage} damage",
                "attack_defender": "{attacker_name} swings their fist at you and hits you for {damage} damage",
                "attack_other": "{attacker_name} swings their fist at {target_name} and hits for {damage} damage",
                "death_message": "The {npc_name} collapses, dead",
            }
            npc.set_behavior_config(config)

            await session.commit()
            await session.refresh(npc)

            # Verify migration results
            final_stats = npc.get_base_stats()
            assert "xp_value" in final_stats
            assert "dexterity" in final_stats
            assert final_stats["xp_value"] == 1
            assert final_stats["dexterity"] == 10

            final_config = npc.get_behavior_config()
            assert "combat_messages" in final_config
            assert "attack_attacker" in final_config["combat_messages"]

    @pytest.mark.asyncio
    async def test_migration_preserves_existing_data(self):
        """Test that migration preserves existing NPC data."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            # Create NPC with existing data
            existing_stats = {"hp": 20, "max_hp": 20, "custom_field": "custom_value"}
            existing_config = {"custom_behavior": "custom_setting"}

            npc = NPCDefinition(
                name="Existing Data NPC",
                npc_type="aggressive_mob",
                sub_zone_id="test_zone",
                base_stats=json.dumps(existing_stats),
                behavior_config=json.dumps(existing_config),
            )

            session.add(npc)
            await session.commit()
            await session.refresh(npc)

            # Simulate migration - add combat data without overwriting
            stats = npc.get_base_stats()
            if "xp_value" not in stats:
                stats["xp_value"] = 5  # Add XP if not present
            if "dexterity" not in stats:
                stats["dexterity"] = 12  # Add dexterity if not present
            npc.set_base_stats(stats)

            config = npc.get_behavior_config()
            if "combat_messages" not in config:
                config["combat_messages"] = {
                    "attack_attacker": "You swing your fist at {target_name} and hit for {damage} damage",
                    "death_message": "The {npc_name} collapses, dead",
                }
            npc.set_behavior_config(config)

            await session.commit()
            await session.refresh(npc)

            # Verify existing data is preserved
            final_stats = npc.get_base_stats()
            assert final_stats["hp"] == 20  # Original data preserved
            assert final_stats["custom_field"] == "custom_value"  # Custom data preserved
            assert final_stats["xp_value"] == 5  # New combat data added

            final_config = npc.get_behavior_config()
            assert final_config["custom_behavior"] == "custom_setting"  # Original data preserved
            assert "combat_messages" in final_config  # New combat data added

    @pytest.mark.asyncio
    async def test_migration_handles_missing_fields_gracefully(self):
        """Test that migration handles missing JSON fields gracefully."""
        # Initialize database first
        await init_db()

        async for session in get_async_session():
            # Create NPC with minimal data
            npc = NPCDefinition(
                name="Minimal NPC",
                npc_type="passive_mob",
                sub_zone_id="test_zone",
                base_stats="{}",
                behavior_config="{}",
            )

            session.add(npc)
            await session.commit()
            await session.refresh(npc)

            # Test that getters return empty dict for missing data
            stats = npc.get_base_stats()
            config = npc.get_behavior_config()

            assert isinstance(stats, dict)
            assert isinstance(config, dict)

            # Add default combat data
            stats.update({"hp": 10, "max_hp": 10, "xp_value": 1, "dexterity": 10})
            npc.set_base_stats(stats)

            config["combat_messages"] = {
                "attack_attacker": "You swing your fist at {target_name} and hit for {damage} damage",
                "death_message": "The {npc_name} collapses, dead",
            }
            npc.set_behavior_config(config)

            await session.commit()
            await session.refresh(npc)

            # Verify data was added successfully
            final_stats = npc.get_base_stats()
            final_config = npc.get_behavior_config()

            assert final_stats["xp_value"] == 1
            assert "combat_messages" in final_config
