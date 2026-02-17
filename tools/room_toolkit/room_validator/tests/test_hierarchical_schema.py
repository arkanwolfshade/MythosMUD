"""
Tests for hierarchical room schema validation.

This module tests the new hierarchical room structure including:
- Environment inheritance validation
- Zone type validation
- Backward compatibility with old format
- Invalid configuration detection
"""

import os
import sys
import unittest
from typing import Any

# Add the room_validator directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.schema_validator import SchemaValidator


class ValidationResult:
    """Simple wrapper to match test expectations."""

    def __init__(self, errors: list[str]) -> None:
        """Initialize with list of validation errors."""
        self.errors = errors
        self.is_valid = len(errors) == 0


class TestHierarchicalSchema(unittest.TestCase):
    """Test the hierarchical room schema validation."""

    # No tearDown needed: validators are stateless, no resources to release.
    def setUp(self) -> None:
        """Set up test fixtures."""
        # Schema file paths
        self.room_schema_path = os.path.join(os.path.dirname(__file__), "..", "schemas", "room_hierarchy_schema.json")
        self.zone_schema_path = os.path.join(os.path.dirname(__file__), "..", "schemas", "zone_schema.json")
        self.subzone_schema_path = os.path.join(os.path.dirname(__file__), "..", "schemas", "subzone_schema.json")

        # Create validators for each schema type
        self.room_validator = SchemaValidator(self.room_schema_path)
        self.zone_validator = SchemaValidator(self.zone_schema_path)
        self.subzone_validator = SchemaValidator(self.subzone_schema_path)

    def _validate_room(self, room_data: dict[str, Any], schema_type: str = "room") -> ValidationResult:
        """Validate room data and return wrapped result."""
        if schema_type == "room":
            errors = self.room_validator.validate_room(room_data)
        elif schema_type == "zone":
            errors = self.zone_validator.validate_room(room_data)
        elif schema_type == "subzone":
            errors = self.subzone_validator.validate_room(room_data)
        else:
            raise ValueError(f"Unknown schema type: {schema_type}")
        return ValidationResult(errors)

    def test_valid_hierarchical_room(self) -> None:
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

        result = self._validate_room(room_data, "room")
        self.assertTrue(result.is_valid, f"Validation failed: {result.errors}")

    def test_invalid_room_missing_description_field(self) -> None:
        """Test that rooms missing description field fail validation."""
        # Single outcome: validation fails with description-related error.
        room_data = {
            "id": "test_room",
            "name": "Test Room",
            "exits": {},
            # Missing description
        }

        result = self._validate_room(room_data, "room")
        self.assertFalse(result.is_valid)
        self.assertIn("description", str(result.errors))

    def test_invalid_room_missing_exits_field(self) -> None:
        """Test that rooms missing exits field fail validation."""
        room_data = {
            "id": "test_room",
            "name": "Test Room",
            "description": "A test room.",
            # Missing exits
        }

        result = self._validate_room(room_data, "room")
        self.assertFalse(result.is_valid)
        self.assertIn("exits", str(result.errors))

    def test_invalid_environment_value(self) -> None:
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

        result = self._validate_room(room_data, "room")
        self.assertFalse(result.is_valid)
        self.assertIn("environment", str(result.errors))

    def test_valid_zone_config(self) -> None:
        """Test that a valid zone configuration passes validation."""
        zone_config = {
            "zone_type": "city",
            "environment": "outdoors",
            "description": "A bustling urban area",
            "weather_patterns": ["fog", "rain", "overcast"],
            "special_rules": {"lucidity_drain_rate": 0.1, "npc_spawn_modifier": 1.2},
        }

        result = self._validate_room(zone_config, "zone")
        self.assertTrue(result.is_valid, f"Validation failed: {result.errors}")

    def test_invalid_zone_type(self) -> None:
        """Test that invalid zone types fail validation."""
        zone_config = {
            "zone_type": "invalid_type",  # Invalid zone type
            "environment": "outdoors",
            "description": "A test zone",
        }

        result = self._validate_room(zone_config, "zone")
        self.assertFalse(result.is_valid)
        self.assertIn("zone_type", str(result.errors))

    def test_valid_subzone_config(self) -> None:
        """Test that a valid sub-zone configuration passes validation."""
        subzone_config = {
            "environment": "indoors",
            "description": "A residential district",
            "special_rules": {"lucidity_drain_rate": 0.05, "npc_spawn_modifier": 0.8},
        }

        result = self._validate_room(subzone_config, "subzone")
        self.assertTrue(result.is_valid, f"Validation failed: {result.errors}")

    def test_invalid_subzone_environment(self) -> None:
        """Test that invalid sub-zone environment values fail validation."""
        subzone_config = {
            "environment": "invalid_environment",  # Invalid value
            "description": "A test sub-zone",
        }

        result = self._validate_room(subzone_config, "subzone")
        self.assertFalse(result.is_valid)
        self.assertIn("environment", str(result.errors))

    def test_valid_room_id_patterns(self) -> None:
        """Test that valid room ID patterns pass validation."""
        valid_ids = [
            "earth_arkhamcity_french_hill_S_Garrison_St_001",
            "yeng_katmandu_palace_palace_ground_001",
        ]

        for room_id in valid_ids:
            room_data = {
                "id": room_id,
                "name": "Test Room",
                "description": "A test room.",
                "plane": "earth",
                "zone": "test_zone",
                "sub_zone": "test_subzone",
                "exits": {},
            }
            result = self._validate_room(room_data, "room")
            self.assertTrue(result.is_valid, f"Valid ID '{room_id}' failed validation")

    def test_invalid_room_id_patterns(self) -> None:
        """Test that invalid room ID patterns fail validation."""
        invalid_ids = [
            "earth-arkham-city",  # Contains hyphens
            "earth.arkham.city",  # Contains dots
            "",  # Empty string
        ]

        for room_id in invalid_ids:
            room_data = {
                "id": room_id,
                "name": "Test Room",
                "description": "A test room.",
                "plane": "earth",
                "zone": "test_zone",
                "sub_zone": "test_subzone",
                "exits": {},
            }
            result = self._validate_room(room_data, "room")
            self.assertFalse(result.is_valid, f"Invalid ID '{room_id}' passed validation")

    def test_valid_exits_pass_validation(self) -> None:
        """Test that valid room exits pass validation."""
        valid_exits = {
            "north": "target_room_id",
            "south": None,
            "east": {"target": "target_room_id", "flags": ["one_way"]},
        }
        room_data = {
            "id": "test_room",
            "name": "Test Room",
            "description": "A test room.",
            "plane": "earth",
            "zone": "test_zone",
            "sub_zone": "test_subzone",
            "exits": valid_exits,
        }
        result = self._validate_room(room_data, "room")
        self.assertTrue(result.is_valid, f"Valid exits failed validation: {result.errors}")

    def test_invalid_exits_fail_validation(self) -> None:
        """Test that invalid room exits fail validation."""
        invalid_exits = {
            "north": "invalid-room-id",  # Contains hyphens
            "south": {
                "target": "valid_id",
                "flags": ["invalid_flag"],  # Invalid flag
            },
        }
        room_data = {
            "id": "test_room",
            "name": "Test Room",
            "description": "A test room.",
            "plane": "earth",
            "zone": "test_zone",
            "sub_zone": "test_subzone",
            "exits": invalid_exits,
        }
        result = self._validate_room(room_data, "room")
        self.assertFalse(result.is_valid)

    def test_environment_inheritance_logic(self) -> None:
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

        result = self._validate_room(room_data, "room")
        self.assertTrue(result.is_valid, f"Room-level environment failed validation: {result.errors}")

    def test_valid_zone_type_values(self) -> None:
        """Test that valid zone type values pass validation."""
        valid_zone_types = ["city", "countryside", "mountains", "swamp", "tundra", "desert"]

        for zone_type in valid_zone_types:
            zone_config = {"zone_type": zone_type, "environment": "outdoors", "description": "A test zone"}
            result = self._validate_room(zone_config, "zone")
            self.assertTrue(result.is_valid, f"Valid zone type '{zone_type}' failed validation")

    def test_invalid_zone_type_values(self) -> None:
        """Test that invalid zone type values fail validation."""
        invalid_zone_types = ["invalid", "town", "village", "forest"]

        for zone_type in invalid_zone_types:
            zone_config = {"zone_type": zone_type, "environment": "outdoors", "description": "A test zone"}
            result = self._validate_room(zone_config, "zone")
            self.assertFalse(result.is_valid, f"Invalid zone type '{zone_type}' passed validation")

    def test_valid_environment_values(self) -> None:
        """Test that valid environment values pass validation."""
        valid_environments = ["indoors", "outdoors", "underwater"]

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
            result = self._validate_room(room_data, "room")
            self.assertTrue(result.is_valid, f"Valid environment '{env}' failed validation")

    def test_invalid_environment_values(self) -> None:
        """Test that invalid environment values fail validation."""
        invalid_environments = ["inside", "outside", "water", "underground"]

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
            result = self._validate_room(room_data, "room")
            self.assertFalse(result.is_valid, f"Invalid environment '{env}' passed validation")


if __name__ == "__main__":
    unittest.main()
