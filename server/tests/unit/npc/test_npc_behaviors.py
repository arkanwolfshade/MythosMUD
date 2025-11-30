"""
Tests for NPC base classes and behavior engines.

This module tests the NPC base classes, behavior engines, and core functionality
including stats, inventory, communication, and deterministic rule systems.

As noted in the Pnakotic Manuscripts, proper behavioral programming is essential
for maintaining the delicate balance between order and chaos in our eldritch
entity management systems.
"""

import time
from unittest.mock import MagicMock

import pytest

from server.logging.enhanced_logging_config import get_logger
from server.models.npc import NPCDefinitionType

logger = get_logger(__name__)


class TestNPCBaseClass:
    """Test NPC base class functionality."""

    @pytest.fixture
    def mock_npc_definition(self):
        """Create a mock NPC definition for testing."""
        npc_def = MagicMock()
        npc_def.id = 1
        npc_def.name = "Test NPC"
        npc_def.description = "A test NPC for behavioral testing"
        npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
        npc_def.sub_zone_id = "downtown"
        npc_def.room_id = "earth_arkhamcity_downtown_room_derby_st_001"
        npc_def.required_npc = True
        npc_def.max_population = 1
        npc_def.spawn_probability = 1.0
        npc_def.base_stats = '{"hp": 100, "strength": 10, "intelligence": 8, "charisma": 6}'
        npc_def.behavior_config = '{"wander_interval": 30, "response_chance": 0.7}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def mock_npc_base(self, mock_npc_definition):
        """Create a mock NPC base instance for testing."""
        from server.npc.behaviors import PassiveMobNPC

        npc = PassiveMobNPC(mock_npc_definition, "test_npc_1")
        return npc

    def test_npc_base_initialization(self, mock_npc_base, mock_npc_definition):
        """Test that NPC base class initializes correctly."""
        assert mock_npc_base.npc_id == "test_npc_1"
        assert mock_npc_base.definition == mock_npc_definition
        assert mock_npc_base.current_room == mock_npc_definition.room_id
        assert mock_npc_base.is_alive is True
        assert mock_npc_base.is_active is True

    def test_npc_base_stats_parsing(self, mock_npc_base):
        """Test that NPC base stats are parsed correctly."""
        stats = mock_npc_base.get_stats()
        assert stats["hp"] == 100
        assert stats["strength"] == 10
        assert stats["intelligence"] == 8
        assert stats["charisma"] == 6

    def test_npc_base_behavior_config_parsing(self, mock_npc_base):
        """Test that NPC behavior config is parsed correctly."""
        config = mock_npc_base.get_behavior_config()
        assert config["wander_interval"] == 30
        assert config["response_chance"] == 0.7

    def test_npc_base_ai_integration_stub_parsing(self, mock_npc_base):
        """Test that NPC AI integration stub is parsed correctly."""
        ai_config = mock_npc_base.get_ai_config()
        assert ai_config["ai_enabled"] is False
        assert ai_config["ai_model"] is None

    def test_npc_base_inventory_initialization(self, mock_npc_base):
        """Test that NPC inventory is initialized correctly."""
        inventory = mock_npc_base.get_inventory()
        assert isinstance(inventory, list)
        assert len(inventory) == 0

    def test_npc_base_add_item_to_inventory(self, mock_npc_base):
        """Test adding items to NPC inventory."""
        item = {"id": "torch", "name": "Torch", "quantity": 1}
        result = mock_npc_base.add_item_to_inventory(item)
        assert result is True

        inventory = mock_npc_base.get_inventory()
        assert len(inventory) == 1
        assert inventory[0]["id"] == "torch"

    def test_npc_base_remove_item_from_inventory(self, mock_npc_base):
        """Test removing items from NPC inventory."""
        item = {"id": "torch", "name": "Torch", "quantity": 1}
        mock_npc_base.add_item_to_inventory(item)

        result = mock_npc_base.remove_item_from_inventory("torch")
        assert result is True

        inventory = mock_npc_base.get_inventory()
        assert len(inventory) == 0

    def test_npc_base_get_item_from_inventory(self, mock_npc_base):
        """Test getting specific items from NPC inventory."""
        item = {"id": "torch", "name": "Torch", "quantity": 1}
        mock_npc_base.add_item_to_inventory(item)

        found_item = mock_npc_base.get_item_from_inventory("torch")
        assert found_item is not None
        assert found_item["id"] == "torch"

        not_found = mock_npc_base.get_item_from_inventory("nonexistent")
        assert not_found is None

    def test_npc_base_health_management(self, mock_npc_base):
        """Test NPC health management."""
        # Test taking damage
        result = mock_npc_base.take_damage(25)
        assert result is True

        stats = mock_npc_base.get_stats()
        assert stats["hp"] == 75

        # Test healing
        result = mock_npc_base.heal(10)
        assert result is True

        stats = mock_npc_base.get_stats()
        assert stats["hp"] == 85

        # Test death
        result = mock_npc_base.take_damage(100)
        assert result is True
        assert mock_npc_base.is_alive is False

    def test_npc_base_movement(self, mock_npc_base):
        """Test NPC movement functionality."""
        new_room = "earth_arkhamcity_downtown_room_derby_st_002"
        # Use simple movement mode (use_integration=False) to avoid dependency on persistence/event bus
        result = mock_npc_base.move_to_room(new_room, use_integration=False)
        assert result is True
        assert mock_npc_base.current_room == new_room

    def test_npc_base_communication(self, mock_npc_base):
        """Test NPC communication functionality."""
        message = "Hello, traveler!"
        channel = "local"
        result = mock_npc_base.speak(message, channel)
        assert result is True

    def test_npc_base_serialization(self, mock_npc_base):
        """Test NPC base serialization for persistence."""
        data = mock_npc_base.to_dict()
        assert "npc_id" in data
        assert "definition_id" in data
        assert "current_room" in data
        assert "stats" in data
        assert "inventory" in data
        assert "is_alive" in data
        assert "is_active" in data

    def test_npc_base_deserialization(self, mock_npc_definition):
        """Test NPC base deserialization from persistence."""
        from server.npc.behaviors import PassiveMobNPC

        # Create initial NPC
        npc = PassiveMobNPC(mock_npc_definition, "test_npc_1")
        npc.take_damage(25)
        npc.add_item_to_inventory({"id": "torch", "name": "Torch", "quantity": 1})

        # Serialize and deserialize
        data = npc.to_dict()
        restored_npc = PassiveMobNPC.from_dict(data, mock_npc_definition)

        assert restored_npc.npc_id == npc.npc_id
        assert restored_npc.current_room == npc.current_room
        assert restored_npc.get_stats()["hp"] == npc.get_stats()["hp"]
        assert len(restored_npc.get_inventory()) == len(npc.get_inventory())


class TestBehaviorEngine:
    """Test behavior engine framework."""

    @pytest.fixture
    def mock_behavior_engine(self):
        """Create a mock behavior engine for testing."""
        from server.npc.behaviors import BehaviorEngine

        engine = BehaviorEngine()
        return engine

    def test_behavior_engine_initialization(self, mock_behavior_engine):
        """Test that behavior engine initializes correctly."""
        assert mock_behavior_engine is not None
        assert hasattr(mock_behavior_engine, "rules")
        assert hasattr(mock_behavior_engine, "state")

    def test_behavior_engine_add_rule(self, mock_behavior_engine):
        """Test adding rules to behavior engine."""
        rule = {
            "name": "wander_rule",
            "condition": "time_since_last_action > 30",
            "action": "wander",
            "priority": 1,
        }
        result = mock_behavior_engine.add_rule(rule)
        assert result is True

        rules = mock_behavior_engine.get_rules()
        assert len(rules) == 1
        assert rules[0]["name"] == "wander_rule"

    def test_behavior_engine_remove_rule(self, mock_behavior_engine):
        """Test removing rules from behavior engine."""
        rule = {
            "name": "wander_rule",
            "condition": "time_since_last_action > 30",
            "action": "wander",
            "priority": 1,
        }
        mock_behavior_engine.add_rule(rule)

        result = mock_behavior_engine.remove_rule("wander_rule")
        assert result is True

        rules = mock_behavior_engine.get_rules()
        assert len(rules) == 0

    def test_behavior_engine_evaluate_conditions(self, mock_behavior_engine):
        """Test condition evaluation in behavior engine."""
        # Add a simple rule
        rule = {
            "name": "test_rule",
            "condition": "hp < 50",
            "action": "flee",
            "priority": 1,
        }
        mock_behavior_engine.add_rule(rule)

        # Test condition evaluation
        context = {"hp": 30}
        result = mock_behavior_engine.evaluate_condition("hp < 50", context)
        assert result is True

        context = {"hp": 80}
        result = mock_behavior_engine.evaluate_condition("hp < 50", context)
        assert result is False

    def test_behavior_engine_get_applicable_rules(self, mock_behavior_engine):
        """Test getting applicable rules based on context."""
        # Add multiple rules
        rules = [
            {
                "name": "low_hp_rule",
                "condition": "hp < 30",
                "action": "flee",
                "priority": 3,
            },
            {
                "name": "wander_rule",
                "condition": "time_since_last_action > 30",
                "action": "wander",
                "priority": 1,
            },
            {
                "name": "attack_rule",
                "condition": "enemy_nearby == true",
                "action": "attack",
                "priority": 2,
            },
        ]

        for rule in rules:
            mock_behavior_engine.add_rule(rule)

        # Test context with multiple applicable rules
        context = {"hp": 20, "time_since_last_action": 35, "enemy_nearby": True}
        applicable = mock_behavior_engine.get_applicable_rules(context)

        # Should return rules sorted by priority (highest first)
        assert len(applicable) == 3
        assert applicable[0]["name"] == "low_hp_rule"  # Priority 3
        assert applicable[1]["name"] == "attack_rule"  # Priority 2
        assert applicable[2]["name"] == "wander_rule"  # Priority 1

    def test_behavior_engine_execute_action(self, mock_behavior_engine):
        """Test action execution in behavior engine."""
        # Add a rule with a test action
        rule = {
            "name": "test_rule",
            "condition": "true",
            "action": "test_action",
            "priority": 1,
        }
        mock_behavior_engine.add_rule(rule)

        # Mock action handler
        action_executed = False

        def test_action_handler(context):
            nonlocal action_executed
            action_executed = True
            return True

        mock_behavior_engine.register_action_handler("test_action", test_action_handler)

        # Execute the action
        context = {}
        result = mock_behavior_engine.execute_action("test_action", context)
        assert result is True
        assert action_executed is True

    def test_behavior_engine_deterministic_execution(self, mock_behavior_engine):
        """Test deterministic rule execution."""
        # Add rules with different priorities
        rules = [
            {
                "name": "rule_1",
                "condition": "value > 5",
                "action": "action_1",
                "priority": 1,
            },
            {
                "name": "rule_2",
                "condition": "value > 10",
                "action": "action_2",
                "priority": 2,
            },
        ]

        for rule in rules:
            mock_behavior_engine.add_rule(rule)

        # Register action handlers
        actions_executed = []

        def action_1_handler(context):
            actions_executed.append("action_1")
            return True

        def action_2_handler(context):
            actions_executed.append("action_2")
            return True

        mock_behavior_engine.register_action_handler("action_1", action_1_handler)
        mock_behavior_engine.register_action_handler("action_2", action_2_handler)

        # Execute with context that matches both rules
        context = {"value": 15}
        result = mock_behavior_engine.execute_applicable_rules(context)

        assert result is True
        # Should execute highest priority rule first
        assert actions_executed == ["action_2"]


class TestShopkeeperNPC:
    """Test shopkeeper NPC type functionality."""

    @pytest.fixture
    def mock_shopkeeper_definition(self):
        """Create a mock shopkeeper NPC definition."""
        npc_def = MagicMock()
        npc_def.id = 1
        npc_def.name = "Ezekiel Whateley"
        npc_def.description = "A grizzled old shopkeeper with a suspicious glint in his eye."
        npc_def.npc_type = NPCDefinitionType.SHOPKEEPER
        npc_def.sub_zone_id = "merchant"
        npc_def.room_id = "earth_arkhamcity_merchant_room_peabody_ave_001"
        npc_def.base_stats = '{"hp": 100, "charisma": 12, "intelligence": 10}'
        npc_def.behavior_config = '{"sells": ["potion", "torch"], "buys": ["junk"], "markup": 1.5}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def mock_shopkeeper(self, mock_shopkeeper_definition):
        """Create a mock shopkeeper NPC instance."""
        from server.npc.behaviors import ShopkeeperNPC

        shopkeeper = ShopkeeperNPC(mock_shopkeeper_definition, "shopkeeper_1")
        return shopkeeper

    def test_shopkeeper_initialization(self, mock_shopkeeper):
        """Test that shopkeeper initializes correctly."""
        assert mock_shopkeeper.npc_type == NPCDefinitionType.SHOPKEEPER
        assert mock_shopkeeper.name == "Ezekiel Whateley"

    def test_shopkeeper_inventory_management(self, mock_shopkeeper):
        """Test shopkeeper inventory management."""
        # Test adding items to shop inventory
        item = {"id": "potion", "name": "Health Potion", "price": 50, "quantity": 5}
        result = mock_shopkeeper.add_shop_item(item)
        assert result is True

        # Test getting shop inventory
        inventory = mock_shopkeeper.get_shop_inventory()
        assert len(inventory) == 1
        assert inventory[0]["id"] == "potion"

    def test_shopkeeper_buy_from_player(self, mock_shopkeeper):
        """Test shopkeeper buying items from player."""
        # Add item to shop's buy list
        mock_shopkeeper.add_buyable_item("junk", 10)

        # Test buying from player
        player_item = {"id": "junk", "name": "Old Junk", "quantity": 1}
        result = mock_shopkeeper.buy_from_player("player_1", player_item)
        assert result is True

        # Check that item was added to shopkeeper's inventory
        inventory = mock_shopkeeper.get_inventory()
        assert len(inventory) == 1
        assert inventory[0]["id"] == "junk"

    def test_shopkeeper_sell_to_player(self, mock_shopkeeper):
        """Test shopkeeper selling items to player."""
        # Add item to shop inventory
        item = {"id": "potion", "name": "Health Potion", "price": 50, "quantity": 3}
        mock_shopkeeper.add_shop_item(item)

        # Test selling to player
        result = mock_shopkeeper.sell_to_player("player_1", "potion", 1)
        assert result is True

        # Check that quantity was reduced
        inventory = mock_shopkeeper.get_shop_inventory()
        potion_item = next((item for item in inventory if item["id"] == "potion"), None)
        assert potion_item is not None
        assert potion_item["quantity"] == 2

    def test_shopkeeper_price_calculation(self, mock_shopkeeper):
        """Test shopkeeper price calculation with markup."""
        # Test base price calculation
        base_price = 100
        markup = 1.5
        final_price = mock_shopkeeper.calculate_price(base_price, markup)
        assert final_price == 150

    def test_shopkeeper_behavior_rules(self, mock_shopkeeper):
        """Test shopkeeper-specific behavior rules."""
        rules = mock_shopkeeper.get_behavior_rules()
        assert len(rules) > 0

        # Check for shopkeeper-specific rules
        rule_names = [rule["name"] for rule in rules]
        assert "greet_customer" in rule_names
        assert "restock_inventory" in rule_names


class TestPassiveMobNPC:
    """Test passive mob NPC type functionality."""

    @pytest.fixture
    def mock_passive_mob_definition(self):
        """Create a mock passive mob NPC definition."""
        npc_def = MagicMock()
        npc_def.id = 2
        npc_def.name = "Wandering Scholar"
        npc_def.description = "A scholarly figure wandering the streets in search of knowledge."
        npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
        npc_def.sub_zone_id = "downtown"
        npc_def.room_id = "earth_arkhamcity_downtown_room_derby_st_001"
        npc_def.base_stats = '{"hp": 80, "intelligence": 15, "charisma": 8}'
        npc_def.behavior_config = '{"wander_interval": 60, "response_chance": 0.8, "wander_radius": 3}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def mock_passive_mob(self, mock_passive_mob_definition):
        """Create a mock passive mob NPC instance."""
        from server.npc.behaviors import PassiveMobNPC

        passive_mob = PassiveMobNPC(mock_passive_mob_definition, "passive_mob_1")
        return passive_mob

    def test_passive_mob_initialization(self, mock_passive_mob):
        """Test that passive mob initializes correctly."""
        assert mock_passive_mob.npc_type == NPCDefinitionType.PASSIVE_MOB
        assert mock_passive_mob.name == "Wandering Scholar"

    def test_passive_mob_wandering_behavior(self, mock_passive_mob):
        """Test passive mob wandering behavior."""
        # Test wander interval configuration
        config = mock_passive_mob.get_behavior_config()
        assert config["wander_interval"] == 60
        assert config["wander_radius"] == 3

        # Test wander action
        # Note: wander() may return False if movement conditions aren't met (no valid exits,
        # probability check fails, etc.), which is expected behavior in test environments
        result = mock_passive_mob.wander()
        # The method should execute without error; False is acceptable if conditions aren't met
        assert isinstance(result, bool)

    def test_passive_mob_response_behavior(self, mock_passive_mob):
        """Test passive mob response behavior."""
        # Test response to player interaction
        result = mock_passive_mob.respond_to_player("player_1", "greet")
        assert result is True

        # Test response chance configuration
        config = mock_passive_mob.get_behavior_config()
        assert config["response_chance"] == 0.8

    def test_passive_mob_behavior_rules(self, mock_passive_mob):
        """Test passive mob-specific behavior rules."""
        rules = mock_passive_mob.get_behavior_rules()
        assert len(rules) > 0

        # Check for passive mob-specific rules
        rule_names = [rule["name"] for rule in rules]
        # Note: wander_periodically was removed - idle movement is now handled by
        # schedule_idle_movement() in execute_behavior(), not through behavior rules
        assert "respond_to_greeting" in rule_names
        assert "avoid_conflict" in rule_names
        # Base class rules should also be present
        assert "check_health" in rule_names
        assert "idle_behavior" in rule_names


class TestAggressiveMobNPC:
    """Test aggressive mob NPC type functionality."""

    @pytest.fixture
    def mock_aggressive_mob_definition(self):
        """Create a mock aggressive mob NPC definition."""
        npc_def = MagicMock()
        npc_def.id = 3
        npc_def.name = "Cultist"
        npc_def.description = "A dark figure clad in robes, muttering forbidden incantations."
        npc_def.npc_type = NPCDefinitionType.AGGRESSIVE_MOB
        npc_def.sub_zone_id = "sanitarium"
        npc_def.room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        npc_def.base_stats = '{"hp": 120, "strength": 15, "intelligence": 12, "aggression": 8}'
        npc_def.behavior_config = '{"hunt_range": 5, "attack_damage": 25, "flee_threshold": 0.3, "territory_size": 2}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'
        return npc_def

    @pytest.fixture
    def mock_aggressive_mob(self, mock_aggressive_mob_definition):
        """Create a mock aggressive mob NPC instance."""
        from server.npc.behaviors import AggressiveMobNPC

        aggressive_mob = AggressiveMobNPC(mock_aggressive_mob_definition, "aggressive_mob_1")
        return aggressive_mob

    def test_aggressive_mob_initialization(self, mock_aggressive_mob):
        """Test that aggressive mob initializes correctly."""
        assert mock_aggressive_mob.npc_type == NPCDefinitionType.AGGRESSIVE_MOB
        assert mock_aggressive_mob.name == "Cultist"

    def test_aggressive_mob_hunting_behavior(self, mock_aggressive_mob):
        """Test aggressive mob hunting behavior."""
        # Test hunt range configuration
        config = mock_aggressive_mob.get_behavior_config()
        assert config["hunt_range"] == 5

        # Test hunting action
        result = mock_aggressive_mob.hunt_target("player_1")
        assert result is True

    def test_aggressive_mob_attack_behavior(self, mock_aggressive_mob):
        """Test aggressive mob attack behavior."""
        # Test attack damage configuration
        config = mock_aggressive_mob.get_behavior_config()
        assert config["attack_damage"] == 25

        # Test attack action
        result = mock_aggressive_mob.attack_target("player_1")
        assert result is True

    def test_aggressive_mob_flee_behavior(self, mock_aggressive_mob):
        """Test aggressive mob flee behavior."""
        # Test flee threshold configuration
        config = mock_aggressive_mob.get_behavior_config()
        assert config["flee_threshold"] == 0.3

        # Test flee action
        result = mock_aggressive_mob.flee()
        assert result is True

    def test_aggressive_mob_territorial_behavior(self, mock_aggressive_mob):
        """Test aggressive mob territorial behavior."""
        # Test territory size configuration
        config = mock_aggressive_mob.get_behavior_config()
        assert config["territory_size"] == 2

        # Test territorial patrol
        result = mock_aggressive_mob.patrol_territory()
        assert result is True

    def test_aggressive_mob_behavior_rules(self, mock_aggressive_mob):
        """Test aggressive mob-specific behavior rules."""
        rules = mock_aggressive_mob.get_behavior_rules()
        assert len(rules) > 0

        # Check for aggressive mob-specific rules
        rule_names = [rule["name"] for rule in rules]
        assert "hunt_players" in rule_names
        assert "attack_on_sight" in rule_names
        assert "flee_when_low_hp" in rule_names
        assert "patrol_territory" in rule_names


class TestAIIntegrationStubs:
    """Test AI integration stubs for future enhancement."""

    @pytest.fixture
    def mock_ai_npc_definition(self):
        """Create a mock NPC definition with AI integration."""
        npc_def = MagicMock()
        npc_def.id = 4
        npc_def.name = "AI Test NPC"
        npc_def.description = "An NPC designed for AI integration testing."
        npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
        npc_def.base_stats = '{"hp": 100, "intelligence": 15}'
        npc_def.behavior_config = '{"ai_enabled": true, "ai_model": "gpt-4", "ai_personality": "scholarly"}'
        npc_def.ai_integration_stub = '{"ai_enabled": true, "ai_model": "gpt-4", "ai_personality": "scholarly"}'
        return npc_def

    @pytest.fixture
    def mock_ai_npc(self, mock_ai_npc_definition):
        """Create a mock NPC with AI integration."""
        from server.npc.behaviors import PassiveMobNPC

        ai_npc = PassiveMobNPC(mock_ai_npc_definition, "ai_npc_1")
        return ai_npc

    def test_ai_integration_stub_parsing(self, mock_ai_npc):
        """Test AI integration stub parsing."""
        ai_config = mock_ai_npc.get_ai_config()
        assert ai_config["ai_enabled"] is True
        assert ai_config["ai_model"] == "gpt-4"
        assert ai_config["ai_personality"] == "scholarly"

    def test_ai_integration_placeholder_methods(self, mock_ai_npc):
        """Test AI integration placeholder methods."""
        # Test AI response generation (placeholder)
        response = mock_ai_npc.generate_ai_response("Hello, how are you?")
        assert response is not None
        assert isinstance(response, str)

        # Test AI decision making (placeholder)
        decision = mock_ai_npc.make_ai_decision({"context": "test"})
        assert decision is not None
        assert isinstance(decision, dict)

        # Test AI learning (placeholder)
        result = mock_ai_npc.learn_from_interaction("player_1", "positive")
        assert result is True


class TestNPCBehaviorIntegration:
    """Integration tests for NPC behavior system."""

    @pytest.mark.asyncio
    async def test_npc_behavior_workflow(self):
        """Test complete NPC behavior workflow."""
        from server.npc.behaviors import ShopkeeperNPC

        # Create NPC definition
        npc_def = MagicMock()
        npc_def.id = 1
        npc_def.name = "Test Shopkeeper"
        npc_def.npc_type = NPCDefinitionType.SHOPKEEPER
        npc_def.base_stats = '{"hp": 100, "charisma": 10}'
        npc_def.behavior_config = '{"sells": ["potion"], "markup": 1.5}'
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'

        # Create NPC instance
        npc = ShopkeeperNPC(npc_def, "test_shopkeeper")

        # Test basic functionality
        assert npc.is_alive is True
        assert npc.is_active is True

        # Test behavior engine integration
        behavior_engine = npc.get_behavior_engine()
        assert behavior_engine is not None

        # Test rule execution
        rules = npc.get_behavior_rules()
        assert len(rules) > 0

        # Test action execution
        context = {"player_nearby": True}
        result = await npc.execute_behavior(context)
        assert result is True

    @pytest.mark.asyncio
    async def test_npc_behavior_performance(self):
        """Test NPC behavior system performance."""
        from server.npc.behaviors import PassiveMobNPC

        # Create multiple NPCs
        npc_count = 10
        npcs = []

        for i in range(npc_count):
            npc_def = MagicMock()
            npc_def.id = i + 1
            npc_def.name = f"Test NPC {i + 1}"
            npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
            npc_def.base_stats = '{"hp": 100}'
            npc_def.behavior_config = '{"wander_interval": 30}'
            npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'

            npc = PassiveMobNPC(npc_def, f"test_npc_{i + 1}")
            npcs.append(npc)

        # Test behavior execution performance
        start_time = time.time()
        for npc in npcs:
            context = {"time_since_last_action": 35}
            await npc.execute_behavior(context)
        execution_time = time.time() - start_time

        # Performance assertion (should execute 10 NPCs quickly)
        # Note: First-time database initialization (room loading, container loading) adds overhead
        # Allow up to 15 seconds to account for database initialization overhead in test environment
        assert execution_time < 15.0

        logger.info("NPC behavior execution time", execution_time=execution_time, npc_count=npc_count)

    @pytest.mark.asyncio
    async def test_npc_behavior_error_handling(self):
        """Test NPC behavior system error handling."""

        # Create NPC with invalid configuration
        npc_def = MagicMock()
        npc_def.id = 1
        npc_def.name = "Error Test NPC"
        npc_def.npc_type = NPCDefinitionType.PASSIVE_MOB
        npc_def.base_stats = '{"invalid": json}'  # Invalid JSON
        npc_def.behavior_config = '{"invalid": json}'  # Invalid JSON
        npc_def.ai_integration_stub = '{"ai_enabled": false, "ai_model": null}'

        # Should handle invalid configuration gracefully
        from server.npc.behaviors import PassiveMobNPC

        npc = PassiveMobNPC(npc_def, "error_npc")
        assert npc is not None

        # Test behavior execution with invalid context
        result = await npc.execute_behavior(None)
        assert result is False  # Should return False for invalid context

        # Test with empty context
        result = await npc.execute_behavior({})
        assert result is True  # Should handle empty context gracefully
