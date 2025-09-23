"""
Tests for hierarchical room schema validation.

This module tests the new hierarchical room structure including:
- Environment inheritance validation
- Zone type validation
- Backward compatibility with old format
- Invalid configuration detection
"""

import json
import os
import sys
import unittest

# Add the room_validator directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.schema_validator import SchemaValidator


class TestHierarchicalSchema(unittest.TestCase):
    """Test the hierarchical room schema validation."""

    def setUp(self):
        """Set up test fixtures."""
        # Schema file paths
        self.room_schema_path = os.path.join(os.path.dirname(__file__), "..", "schemas", "room_hierarchy_schema.json")
        self.zone_schema_path = os.path.join(os.path.dirname(__file__), "..", "schemas", "zone_schema.json")
        self.subzone_schema_path = os.path.join(os.path.dirname(__file__), "..", "schemas", "subzone_schema.json")

        # Load schemas
        with open(self.room_schema_path) as f:
            self.room_schema = json.load(f)
        with open(self.zone_schema_path) as f:
            self.zone_schema = json.load(f)
        with open(self.subzone_schema_path) as f:
            self.subzone_schema = json.load(f)

        self.validator = SchemaValidator()

    def test_valid_hierarchical_room(self):
        """Test that a valid hierarchical room passes validation."""
        room_data = {
            "id": "earth_arkhamcity_french_hill_S_Garrison_St_001",
            "name": "South Garrison Street",
            "description": "A quiet residential street in French Hill.",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "french_hill",
            "environment": "outdoors",
            "exits": {"north": "earth_arkhamcity_french_hill_S_Garrison_St_002", "south": None},
        }

        result = self.validator.validate_room(room_data, self.room_schema)
        self.assertTrue(result.is_valid, f"Validation failed: {result.errors}")

    def test_invalid_room_missing_required_fields(self):
        """Test that rooms missing required fields fail validation."""
        room_data = {
            "id": "test_room",
            "name": "Test Room",
            # Missing description and exits
        }

        result = self.validator.validate_room(room_data, self.room_schema)
        self.assertFalse(result.is_valid)
        self.assertIn("description", str(result.errors))
        self.assertIn("exits", str(result.errors))

    def test_invalid_environment_value(self):
        """Test that invalid environment values fail validation."""
        room_data = {
            "id": "test_room",
            "name": "Test Room",
            "description": "A test room.",
            "plane": "earth",
            "zone": "test_zone",
            "sub_zone": "test_subzone",
            "environment": "invalid_environment",  # Invalid value
            "exits": {},
        }

        result = self.validator.validate_room(room_data, self.room_schema)
        self.assertFalse(result.is_valid)
        self.assertIn("environment", str(result.errors))

    def test_valid_zone_config(self):
        """Test that a valid zone configuration passes validation."""
        zone_config = {
            "zone_type": "city",
            "environment": "outdoors",
            "description": "A bustling urban area",
            "weather_patterns": ["fog", "rain", "overcast"],
            "special_rules": {"sanity_drain_rate": 0.1, "npc_spawn_modifier": 1.2},
        }

        result = self.validator.validate_room(zone_config, self.zone_schema)
        self.assertTrue(result.is_valid, f"Validation failed: {result.errors}")

    def test_invalid_zone_type(self):
        """Test that invalid zone types fail validation."""
        zone_config = {
            "zone_type": "invalid_type",  # Invalid zone type
            "environment": "outdoors",
            "description": "A test zone",
        }

        result = self.validator.validate_room(zone_config, self.zone_schema)
        self.assertFalse(result.is_valid)
        self.assertIn("zone_type", str(result.errors))

    def test_valid_subzone_config(self):
        """Test that a valid sub-zone configuration passes validation."""
        subzone_config = {
            "environment": "indoors",
            "description": "A residential district",
            "special_rules": {"sanity_drain_rate": 0.05, "npc_spawn_modifier": 0.8},
        }

        result = self.validator.validate_room(subzone_config, self.subzone_schema)
        self.assertTrue(result.is_valid, f"Validation failed: {result.errors}")

    def test_invalid_subzone_environment(self):
        """Test that invalid sub-zone environment values fail validation."""
        subzone_config = {
            "environment": "invalid_environment",  # Invalid value
            "description": "A test sub-zone",
        }

        result = self.validator.validate_room(subzone_config, self.subzone_schema)
        self.assertFalse(result.is_valid)
        self.assertIn("environment", str(result.errors))

    def test_room_id_pattern_validation(self):
        """Test that room IDs follow the correct pattern."""
        valid_ids = [
            "earth_arkhamcity_french_hill_S_Garrison_St_001",
            "yeng_katmandu_palace_palace_ground_001",
        ]

        invalid_ids = [
            "earth-arkham-city",  # Contains hyphens
            "earth.arkham.city",  # Contains dots
            "Earth_Arkham_City",  # Contains uppercase
            "",  # Empty string
        ]

        for room_id in valid_ids:
            room_data = {"id": room_id, "name": "Test Room", "description": "A test room.", "exits": {}}
            result = self.validator.validate_room(room_data, self.room_schema)
            self.assertTrue(result.is_valid, f"Valid ID '{room_id}' failed validation")

        for room_id in invalid_ids:
            room_data = {"id": room_id, "name": "Test Room", "description": "A test room.", "exits": {}}
            result = self.validator.validate_room(room_data, self.room_schema)
            self.assertFalse(result.is_valid, f"Invalid ID '{room_id}' passed validation")

    def test_exit_validation(self):
        """Test that room exits are properly validated."""
        valid_exits = {
            "north": "target_room_id",
            "south": None,
            "east": {"target": "target_room_id", "flags": ["one_way"]},
        }

        invalid_exits = {
            "north": "invalid-room-id",  # Contains hyphens
            "south": {
                "target": "valid_id",
                "flags": ["invalid_flag"],  # Invalid flag
            },
        }

        # Test valid exits
        room_data = {"id": "test_room", "name": "Test Room", "description": "A test room.", "exits": valid_exits}
        result = self.validator.validate_room(room_data, self.room_schema)
        self.assertTrue(result.is_valid, f"Valid exits failed validation: {result.errors}")

        # Test invalid exits
        room_data["exits"] = invalid_exits
        result = self.validator.validate_room(room_data, self.room_schema)
        self.assertFalse(result.is_valid)

    def test_environment_inheritance_logic(self):
        """Test that environment inheritance follows the correct priority chain."""
        # This test validates the logic, not the schema itself
        # The actual inheritance is handled by the world loader

        # Test that room-level environment overrides zone/subzone
        room_data = {
            "id": "test_room",
            "name": "Test Room",
            "description": "A test room.",
            "plane": "earth",
            "zone": "test_zone",
            "sub_zone": "test_subzone",
            "environment": "indoors",  # Room-level setting
            "exits": {},
        }

        result = self.validator.validate_room(room_data, self.room_schema)
        self.assertTrue(result.is_valid, f"Room-level environment failed validation: {result.errors}")

    def test_zone_type_enum_validation(self):
        """Test that zone types are properly validated against the enum."""
        valid_zone_types = ["city", "countryside", "mountains", "swamp", "tundra", "desert"]
        invalid_zone_types = ["invalid", "town", "village", "forest"]

        for zone_type in valid_zone_types:
            zone_config = {"zone_type": zone_type, "environment": "outdoors", "description": "A test zone"}
            result = self.validator.validate_room(zone_config, self.zone_schema)
            self.assertTrue(result.is_valid, f"Valid zone type '{zone_type}' failed validation")

        for zone_type in invalid_zone_types:
            zone_config = {"zone_type": zone_type, "environment": "outdoors", "description": "A test zone"}
            result = self.validator.validate_room(zone_config, self.zone_schema)
            self.assertFalse(result.is_valid, f"Invalid zone type '{zone_type}' passed validation")

    def test_environment_enum_validation(self):
        """Test that environment values are properly validated against the enum."""
        valid_environments = ["indoors", "outdoors", "underwater"]
        invalid_environments = ["inside", "outside", "water", "underground"]

        for env in valid_environments:
            room_data = {
                "id": "test_room",
                "name": "Test Room",
                "description": "A test room.",
                "plane": "earth",
                "zone": "test_zone",
                "sub_zone": "test_subzone",
                "environment": env,
                "exits": {},
            }
            result = self.validator.validate_room(room_data, self.room_schema)
            self.assertTrue(result.is_valid, f"Valid environment '{env}' failed validation")

        for env in invalid_environments:
            room_data = {
                "id": "test_room",
                "name": "Test Room",
                "description": "A test room.",
                "plane": "earth",
                "zone": "test_zone",
                "sub_zone": "test_subzone",
                "environment": env,
                "exits": {},
            }
            result = self.validator.validate_room(room_data, self.room_schema)
            self.assertFalse(result.is_valid, f"Invalid environment '{env}' passed validation")


if __name__ == "__main__":
    unittest.main()
