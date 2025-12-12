"""
Shared fixtures for NPC population controller tests.
"""

import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import pytest

from server.events.event_bus import EventBus
from server.models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from server.npc.population_control import NPCPopulationController, ZoneConfiguration


@pytest.fixture
def event_bus():
    """Create an event bus for testing."""
    return EventBus()


@pytest.fixture
def temp_rooms_dir():
    """Create a temporary directory with test room configurations."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create proper directory structure: plane/zone/subzone
        earth_dir = temp_path / "earth"
        earth_dir.mkdir()

        arkham_dir = earth_dir / "arkhamcity"
        arkham_dir.mkdir()

        downtown_dir = arkham_dir / "downtown"
        downtown_dir.mkdir()

        # Create zone config
        zone_config = {
            "zone_type": "city",
            "environment": "outdoors",
            "description": "A bustling urban area",
            "weather_patterns": ["fog", "rain", "overcast"],
            "special_rules": {
                "npc_spawn_modifier": 1.2,
                "lucidity_drain_rate": 0.1,
                "combat_modifier": 1.0,
                "exploration_bonus": 0.5,
            },
        }

        with open(arkham_dir / "zone_config.json", "w", encoding="utf-8") as f:
            json.dump(zone_config, f)

        # Create sub-zone config
        subzone_config = {
            "environment": "outdoors",
            "description": "The bustling commercial heart",
            "special_rules": {
                "npc_spawn_modifier": 1.5,
                "lucidity_drain_rate": 0.08,
                "combat_modifier": 1.1,
                "exploration_bonus": 0.7,
            },
        }

        with open(downtown_dir / "subzone_config.json", "w", encoding="utf-8") as f:
            json.dump(subzone_config, f)

        yield temp_path


@pytest.fixture
def population_controller(request):
    """Create a population controller with test data."""
    # Get the event_bus fixture to avoid name shadowing
    bus = request.getfixturevalue("event_bus")

    # Create a mock spawning service
    mock_spawning_service = Mock()

    # Create a counter to generate unique NPC IDs
    npc_id_counter = [0]

    def create_mock_npc_instance(*args, **kwargs):
        npc_id_counter[0] += 1
        mock_npc_instance = Mock()
        mock_npc_instance.success = True
        mock_npc_instance.npc_id = f"test_npc_{npc_id_counter[0]:03d}"
        return mock_npc_instance

    mock_spawning_service._spawn_npc_from_request = Mock(side_effect=create_mock_npc_instance)

    # Create a mock lifecycle manager that tracks spawned NPCs
    mock_lifecycle_manager = Mock()
    mock_lifecycle_manager.active_npcs = {}

    def mock_spawn_npc(def_, room_id, _reason):
        """Mock spawn_npc that actually adds to active_npcs."""
        npc_id = f"test_npc_{npc_id_counter[0]:03d}"
        npc_id_counter[0] += 1
        # Add the NPC to active_npcs
        mock_npc_instance = Mock()
        mock_npc_instance.name = def_.name
        mock_npc_instance.current_room_id = room_id
        mock_npc_instance.current_room = room_id
        mock_npc_instance.room_id = room_id
        mock_npc_instance.npc_type = def_.npc_type.value if hasattr(def_.npc_type, "value") else str(def_.npc_type)
        mock_npc_instance.is_required = def_.is_required() if hasattr(def_, "is_required") else False
        mock_npc_instance.definition_id = def_.id if hasattr(def_, "id") else None
        mock_lifecycle_manager.active_npcs[npc_id] = mock_npc_instance
        return npc_id

    mock_lifecycle_manager.spawn_npc = Mock(side_effect=mock_spawn_npc)

    # Create a mock async_persistence that doesn't actually load from database
    mock_persistence = MagicMock()

    # Patch the _load_zone_configurations method to skip database loading
    with patch.object(NPCPopulationController, "_load_zone_configurations", return_value=None):
        controller = NPCPopulationController(
            bus,
            spawning_service=mock_spawning_service,
            lifecycle_manager=mock_lifecycle_manager,
            async_persistence=mock_persistence,
        )

        # Manually add zone configurations that tests expect (from temp_rooms_dir fixture)
        # Zone config for "arkhamcity"
        zone_config_data = {
            "zone_type": "city",
            "environment": "outdoors",
            "description": "A bustling urban area",
            "weather_patterns": ["fog", "rain", "overcast"],
            "special_rules": {
                "npc_spawn_modifier": 1.2,
                "lucidity_drain_rate": 0.1,
                "combat_modifier": 1.0,
                "exploration_bonus": 0.5,
            },
        }
        controller.zone_configurations["arkhamcity"] = ZoneConfiguration(zone_config_data)

        # Sub-zone config for "arkhamcity/downtown"
        subzone_config_data = {
            "environment": "outdoors",
            "description": "The bustling commercial heart",
            "special_rules": {
                "npc_spawn_modifier": 1.5,
                "lucidity_drain_rate": 0.08,
                "combat_modifier": 1.1,
                "exploration_bonus": 0.7,
            },
        }
        controller.zone_configurations["arkhamcity/downtown"] = ZoneConfiguration(subzone_config_data)

        return controller


@pytest.fixture
def shopkeeper_definition():
    """Create a shopkeeper NPC definition."""
    definition = NPCDefinition(
        name="Test Shopkeeper",
        description="A test shopkeeper",
        npc_type=NPCDefinitionType.SHOPKEEPER,
        sub_zone_id="downtown",
        required_npc=True,
        max_population=1,
        spawn_probability=1.0,
        base_stats='{"strength": 50, "lucidity": 80, "dp": 100, "max_dp": 100}',
        behavior_config='{"greeting_message": "Welcome!"}',
        ai_integration_stub='{"ai_enabled": false}',
    )
    definition.id = 1  # Set explicit ID for testing
    return definition


@pytest.fixture
def passive_mob_definition():
    """Create a passive mob NPC definition."""
    definition = NPCDefinition(
        name="Test Passive Mob",
        description="A test passive mob",
        npc_type=NPCDefinitionType.PASSIVE_MOB,
        sub_zone_id="downtown",
        required_npc=False,
        max_population=3,
        spawn_probability=0.7,
        base_stats='{"strength": 8, "lucidity": 60, "current_dp": 80}',
        behavior_config='{"wandering_behavior": true}',
        ai_integration_stub='{"ai_enabled": false}',
    )
    definition.id = 2  # Set explicit ID for testing
    return definition


@pytest.fixture
def spawn_rule_shopkeeper(request):
    """Create a spawn rule for the shopkeeper."""
    shopkeeper_def = request.getfixturevalue("shopkeeper_definition")
    return NPCSpawnRule(
        npc_definition_id=shopkeeper_def.id,
        sub_zone_id="arkhamcity/downtown",
        min_population=0,
        max_population=999,
        spawn_conditions="{}",
    )


@pytest.fixture
def spawn_rule_passive_mob(request):
    """Create a spawn rule for the passive mob."""
    passive_mob_def = request.getfixturevalue("passive_mob_definition")
    return NPCSpawnRule(
        npc_definition_id=passive_mob_def.id,
        sub_zone_id="arkhamcity/downtown",
        min_population=1,
        max_population=5,
        spawn_conditions='{"time_of_day": "day", "weather": "clear"}',
    )
