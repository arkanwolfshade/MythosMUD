"""
Tests for hierarchical world loader functionality.

This module tests the enhanced world loader including:
- Hierarchical world loading
- Configuration file loading
- Room ID resolution (both formats)
- Environment inheritance
- Performance benchmarks
"""

import json
import os
import shutil
import sys
import tempfile
import unittest

import pytest

# Add the server directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Import the module to ensure coverage tracking
import server.world_loader
from server.world_loader import (
    generate_room_id,
    get_room_environment,
    load_hierarchical_world,
    load_subzone_config,
    load_zone_config,
    resolve_room_reference,
)


@pytest.fixture(autouse=True)
def reset_persistence_singleton():
    """Reset the persistence singleton before each test to ensure clean state."""
    # Clear the global persistence instance
    import server.persistence

    server.persistence._persistence_instance = None

    yield


class TestWorldLoaderHierarchy(unittest.TestCase):
    """Test cases for hierarchical world loader functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.rooms_path = os.path.join(self.temp_dir, "rooms")
        os.makedirs(self.rooms_path)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def create_test_structure(self):
        """Create a test hierarchical structure."""
        # Create plane/zone/subzone structure
        earth_path = os.path.join(self.rooms_path, "earth")
        arkham_path = os.path.join(earth_path, "arkham_city")
        french_hill_path = os.path.join(arkham_path, "french_hill")

        os.makedirs(french_hill_path)

        # Create zone config
        zone_config = {
            "zone_type": "city",
            "environment": "outdoors",
            "description": "A bustling urban area",
            "weather_patterns": ["fog", "rain", "overcast"],
            "special_rules": {"sanity_drain_rate": 0.1, "npc_spawn_modifier": 1.2},
        }

        with open(os.path.join(arkham_path, "zone_config.json"), "w") as f:
            json.dump(zone_config, f)

        # Create subzone config
        subzone_config = {
            "environment": "outdoors",
            "description": "A residential district",
            "special_rules": {"sanity_drain_rate": 0.05, "npc_spawn_modifier": 0.8},
        }

        with open(os.path.join(french_hill_path, "subzone_config.json"), "w") as f:
            json.dump(subzone_config, f)

        # Create room files
        room1_data = {
            "id": "earth_arkham_city_french_hill_S_Garrison_St_001",
            "name": "South Garrison Street",
            "description": "A quiet residential street.",
            "plane": "earth",
            "zone": "arkham_city",
            "sub_zone": "french_hill",
            "environment": "outdoors",
            "exits": {"north": "earth_arkham_city_french_hill_S_Garrison_St_002", "south": None},
        }

        room2_data = {
            "id": "earth_arkham_city_french_hill_S_Garrison_St_002",
            "name": "South Garrison Street (North)",
            "description": "The northern end of the street.",
            "plane": "earth",
            "zone": "arkham_city",
            "sub_zone": "french_hill",
            "exits": {"south": "earth_arkham_city_french_hill_S_Garrison_St_001"},
        }

        with open(os.path.join(french_hill_path, "S_Garrison_St_001.json"), "w") as f:
            json.dump(room1_data, f)

        with open(os.path.join(french_hill_path, "S_Garrison_St_002.json"), "w") as f:
            json.dump(room2_data, f)

    def test_load_zone_config(self):
        """Test loading zone configuration files."""
        # Create test zone config
        zone_path = os.path.join(self.temp_dir, "test_zone")
        os.makedirs(zone_path)

        zone_config = {"zone_type": "city", "environment": "outdoors", "description": "Test zone"}

        config_path = os.path.join(zone_path, "zone_config.json")
        with open(config_path, "w") as f:
            json.dump(zone_config, f)

        # Test loading
        loaded_config = load_zone_config(zone_path)
        self.assertIsNotNone(loaded_config)
        self.assertEqual(loaded_config["zone_type"], "city")
        self.assertEqual(loaded_config["environment"], "outdoors")

        # Test non-existent config
        empty_path = os.path.join(self.temp_dir, "empty_zone")
        os.makedirs(empty_path)
        loaded_config = load_zone_config(empty_path)
        self.assertIsNone(loaded_config)

    def test_load_subzone_config(self):
        """Test loading sub-zone configuration files."""
        # Create test subzone config
        subzone_path = os.path.join(self.temp_dir, "test_subzone")
        os.makedirs(subzone_path)

        subzone_config = {"environment": "indoors", "description": "Test subzone"}

        config_path = os.path.join(subzone_path, "subzone_config.json")
        with open(config_path, "w") as f:
            json.dump(subzone_config, f)

        # Test loading
        loaded_config = load_subzone_config(subzone_path)
        self.assertIsNotNone(loaded_config)
        self.assertEqual(loaded_config["environment"], "indoors")

        # Test non-existent config
        empty_path = os.path.join(self.temp_dir, "empty_subzone")
        os.makedirs(empty_path)
        loaded_config = load_subzone_config(empty_path)
        self.assertIsNone(loaded_config)

    def test_generate_room_id(self):
        """Test room ID generation from components."""
        room_id = generate_room_id("earth", "arkham_city", "french_hill", "S_Garrison_St_001")
        expected_id = "earth_arkham_city_french_hill_S_Garrison_St_001"
        self.assertEqual(room_id, expected_id)

        # Test with different components
        room_id = generate_room_id("yeng", "katmandu", "palace", "palace_Ground_001")
        expected_id = "yeng_katmandu_palace_palace_Ground_001"
        self.assertEqual(room_id, expected_id)

    def test_get_room_environment(self):
        """Test environment inheritance logic."""
        room_data = {"environment": "indoors"}
        subzone_config = {"environment": "outdoors"}
        zone_config = {"environment": "underwater"}

        # Test room-level override
        env = get_room_environment(room_data, subzone_config, zone_config)
        self.assertEqual(env, "indoors")

        # Test subzone inheritance
        room_data_no_env = {}
        env = get_room_environment(room_data_no_env, subzone_config, zone_config)
        self.assertEqual(env, "outdoors")

        # Test zone inheritance
        env = get_room_environment(room_data_no_env, None, zone_config)
        self.assertEqual(env, "underwater")

        # Test default fallback
        env = get_room_environment(room_data_no_env, None, None)
        self.assertEqual(env, "outdoors")

    def test_load_hierarchical_world(self):
        """Test loading the complete hierarchical world structure."""
        # Temporarily patch the ROOMS_BASE_PATH
        original_path = None
        try:
            import server.world_loader

            original_path = server.world_loader.ROOMS_BASE_PATH
            server.world_loader.ROOMS_BASE_PATH = self.rooms_path
            self.create_test_structure()

            # Load world data
            world_data = load_hierarchical_world()

            # Verify structure
            self.assertIn("rooms", world_data)
            self.assertIn("zone_configs", world_data)
            self.assertIn("subzone_configs", world_data)
            self.assertIn("room_mappings", world_data)

            # Verify rooms loaded
            self.assertEqual(len(world_data["rooms"]), 2)

            # Verify zone configs loaded
            self.assertEqual(len(world_data["zone_configs"]), 1)
            self.assertIn("earth/arkham_city", world_data["zone_configs"])

            # Verify subzone configs loaded
            self.assertEqual(len(world_data["subzone_configs"]), 1)
            self.assertIn("earth/arkham_city/french_hill", world_data["subzone_configs"])

            # Verify specific room loaded
            room_id = "earth_arkham_city_french_hill_S_Garrison_St_001"
            self.assertIn(room_id, world_data["rooms"])
            room = world_data["rooms"][room_id]
            self.assertEqual(room["name"], "South Garrison Street")

        finally:
            # Restore the original path
            if original_path is not None:
                server.world_loader.ROOMS_BASE_PATH = original_path

    def test_resolve_room_reference(self):
        """Test room reference resolution for both old and new formats."""
        # Temporarily patch the ROOMS_BASE_PATH
        original_path = None
        try:
            import server.world_loader

            original_path = server.world_loader.ROOMS_BASE_PATH
            server.world_loader.ROOMS_BASE_PATH = self.rooms_path
            self.create_test_structure()
            world_data = load_hierarchical_world()

            # Test new format ID
            new_id = "earth_arkham_city_french_hill_S_Garrison_St_001"
            resolved = resolve_room_reference(new_id, world_data)
            self.assertEqual(resolved, new_id)

            # Test non-existent ID
            resolved = resolve_room_reference("non_existent_room", world_data)
            self.assertIsNone(resolved)

            # Test without world_data (should load automatically)
            resolved = resolve_room_reference(new_id)
            self.assertEqual(resolved, new_id)

        finally:
            # Restore the original path
            if original_path is not None:
                server.world_loader.ROOMS_BASE_PATH = original_path

    def test_backward_compatibility(self):
        """Test backward compatibility with existing room loading."""
        # Temporarily patch the ROOMS_BASE_PATH
        original_path = None
        try:
            import server.world_loader

            original_path = server.world_loader.ROOMS_BASE_PATH
            server.world_loader.ROOMS_BASE_PATH = self.rooms_path
            self.create_test_structure()

            # Test that load_rooms() still works
            from server.world_loader import load_rooms

            rooms = load_rooms()

            # Should return the same rooms as hierarchical loader
            world_data = load_hierarchical_world()
            self.assertEqual(len(rooms), len(world_data["rooms"]))

            # Verify room IDs match
            for room_id in rooms:
                self.assertIn(room_id, world_data["rooms"])

        finally:
            # Restore the original path
            if original_path is not None:
                server.world_loader.ROOMS_BASE_PATH = original_path

    def test_empty_rooms_directory_isolated(self):
        """Test behavior with empty rooms directory - completely isolated."""
        # Create a completely isolated temporary directory
        isolated_temp_dir = tempfile.mkdtemp()
        isolated_rooms_path = os.path.join(isolated_temp_dir, "rooms")
        os.makedirs(isolated_rooms_path)

        try:
            # Temporarily patch the ROOMS_BASE_PATH
            original_path = None
            try:
                import server.world_loader

                original_path = server.world_loader.ROOMS_BASE_PATH
                print(f"[DEBUG] Original ROOMS_BASE_PATH: {original_path}")
                server.world_loader.ROOMS_BASE_PATH = isolated_rooms_path
                print(f"[DEBUG] Patched ROOMS_BASE_PATH: {server.world_loader.ROOMS_BASE_PATH}")

                world_data = load_hierarchical_world()
                print(f"[DEBUG] Loaded rooms: {list(world_data['rooms'].keys())}")

                # Should return empty structure
                self.assertEqual(len(world_data["rooms"]), 0)
                self.assertEqual(len(world_data["zone_configs"]), 0)
                self.assertEqual(len(world_data["subzone_configs"]), 0)
                self.assertEqual(len(world_data["room_mappings"]), 0)
            finally:
                # Restore the original path
                if original_path is not None:
                    server.world_loader.ROOMS_BASE_PATH = original_path
        finally:
            # Clean up
            shutil.rmtree(isolated_temp_dir)

    def test_malformed_config_files(self):
        """Test handling of malformed configuration files."""
        # Create malformed zone config
        zone_path = os.path.join(self.temp_dir, "malformed_zone")
        os.makedirs(zone_path)

        config_path = os.path.join(zone_path, "zone_config.json")
        with open(config_path, "w") as f:
            f.write('{"invalid": json}')  # Malformed JSON

        # Should handle gracefully
        loaded_config = load_zone_config(zone_path)
        self.assertIsNone(loaded_config)

    def test_environment_inheritance_priority(self):
        """Test that environment inheritance follows correct priority."""
        # Temporarily patch the ROOMS_BASE_PATH
        original_path = None
        try:
            import server.world_loader

            original_path = server.world_loader.ROOMS_BASE_PATH
            server.world_loader.ROOMS_BASE_PATH = self.rooms_path

            # Create test structure with different environment settings
            earth_path = os.path.join(self.rooms_path, "earth")
            zone_path = os.path.join(earth_path, "test_zone")
            subzone_path = os.path.join(zone_path, "test_subzone")

            os.makedirs(subzone_path)

            # Zone config with underwater environment
            zone_config = {"environment": "underwater"}
            with open(os.path.join(zone_path, "zone_config.json"), "w") as f:
                json.dump(zone_config, f)

            # Subzone config with outdoors environment
            subzone_config = {"environment": "outdoors"}
            with open(os.path.join(subzone_path, "subzone_config.json"), "w") as f:
                json.dump(subzone_config, f)

            # Room with indoor environment
            room_data = {
                "id": "test_room",
                "name": "Test Room",
                "description": "A test room.",
                "environment": "indoor",
                "exits": {},
            }

            with open(os.path.join(subzone_path, "test_room.json"), "w") as f:
                json.dump(room_data, f)

            # Load world data
            world_data = load_hierarchical_world()

            # Room should inherit indoor environment (highest priority)
            room = world_data["rooms"]["earth_test_zone_test_subzone_test_room"]
            self.assertEqual(room["resolved_environment"], "indoor")

        finally:
            # Restore the original path
            if original_path is not None:
                server.world_loader.ROOMS_BASE_PATH = original_path

    def test_module_coverage(self):
        """Test to ensure world_loader module is properly imported for coverage."""
        # This test ensures the module is executed and tracked by coverage
        assert hasattr(server.world_loader, "load_rooms")
        assert hasattr(server.world_loader, "load_hierarchical_world")
        assert hasattr(server.world_loader, "generate_room_id")
        assert hasattr(server.world_loader, "get_room_environment")
        assert hasattr(server.world_loader, "resolve_room_reference")
        assert hasattr(server.world_loader, "ROOMS_BASE_PATH")


if __name__ == "__main__":
    unittest.main()
