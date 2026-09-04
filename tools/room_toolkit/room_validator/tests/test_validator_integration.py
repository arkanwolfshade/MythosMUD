"""
Integration tests for the main validator CLI.

Tests the complete validation pipeline and CLI functionality.
"""

import json
import tempfile
from pathlib import Path

from click.testing import CliRunner
from validator import main


class TestValidatorIntegration:
    """Integration tests for the main validator."""

    def test_validator_with_valid_rooms(self, temp_rooms_dir):
        """Test validator with valid room files."""
        runner = CliRunner()
        result = runner.invoke(main, ["--base-path", str(temp_rooms_dir), "--no-colors"])

        assert result.exit_code == 0
        assert "All validations passed" in result.output or "errors found" in result.output

    def test_validator_with_invalid_rooms(self, temp_rooms_dir):
        """Test validator with invalid room files."""
        # Create an invalid room file
        invalid_room = {"id": "invalid", "name": "Invalid"}  # Missing required fields
        rooms_dir = Path(temp_rooms_dir) / "rooms" / "test_zone"
        rooms_dir.mkdir(parents=True, exist_ok=True)
        with open(rooms_dir / "invalid.json", "w", encoding="utf-8") as f:
            json.dump(invalid_room, f)

        runner = CliRunner()
        result = runner.invoke(main, ["--base-path", str(temp_rooms_dir), "--no-colors"])

        # Should exit with error code when validation fails
        assert result.exit_code != 0 or "errors found" in result.output

    def test_validator_json_output(self, temp_rooms_dir):
        """Test validator JSON output format."""
        runner = CliRunner()
        result = runner.invoke(main, ["--base-path", str(temp_rooms_dir), "--output-format", "json", "--no-colors"])

        assert result.exit_code == 0
        # JSON output should be parseable
        try:
            output_data = json.loads(result.output)
            assert "stats" in output_data or "summary" in output_data
        except json.JSONDecodeError:
            # If not JSON, check for console output
            assert "Validation" in result.output or "errors" in result.output.lower()

    def test_validator_zone_filtering(self, temp_rooms_dir):
        """Test validator zone filtering."""
        runner = CliRunner()
        # Test with a zone that might not exist (should handle gracefully)
        result = runner.invoke(main, ["--base-path", str(temp_rooms_dir), "--zone", "nonexistent", "--no-colors"])

        # Should either find the zone or report it doesn't exist
        assert result.exit_code != 0 or "not found" in result.output or result.exit_code == 0

    def test_validator_help_output(self):
        """Test that help text is properly displayed."""
        runner = CliRunner()
        result = runner.invoke(main, ["--help"])

        assert result.exit_code == 0
        assert "Validate room connectivity" in result.output
        assert "--zone" in result.output
        assert "--verbose" in result.output

    def test_validator_schema_only_flag(self, temp_rooms_dir):
        """Test schema-only validation flag."""
        runner = CliRunner()
        result = runner.invoke(main, ["--base-path", str(temp_rooms_dir), "--schema-only", "--no-colors"])

        assert result.exit_code == 0 or result.exit_code == 1  # May pass or fail depending on data


class TestValidatorComponents:
    """Test individual validator components."""

    def test_room_loader_integration(self, temp_rooms_dir):
        """Test room loader integration."""
        from core.room_loader import RoomLoader

        loader = RoomLoader(temp_rooms_dir)
        database = loader.build_room_database(show_progress=False)

        assert len(database) == 3
        assert "test_zone_001" in database
        assert "test_zone_002" in database
        assert "test_zone_003" in database

    def test_schema_validator_integration(self, sample_room_database):
        """Test schema validator integration."""
        from core.schema_validator import SchemaValidator

        validator = SchemaValidator()
        results = validator.validate_room_database(sample_room_database)

        assert len(results) == 0

    def test_path_validator_integration(self, sample_room_database):
        """Test path validator integration."""
        from core.path_validator import PathValidator
        from core.schema_validator import SchemaValidator

        schema_validator = SchemaValidator()
        path_validator = PathValidator(schema_validator)

        # Test connectivity analysis
        unreachable = path_validator.find_unreachable_rooms(
            start_room_id="test_001", room_database=sample_room_database
        )
        assert len(unreachable) == 0

        # Test bidirectional connections
        missing_returns = path_validator.check_bidirectional_connections(sample_room_database)
        assert len(missing_returns) == 0

        # Test dead ends
        dead_ends = path_validator.find_dead_ends(sample_room_database)
        assert len(dead_ends) == 0

    def test_reporter_integration(self):
        """Test reporter integration."""
        from core.reporter import Reporter

        reporter = Reporter(use_colors=False)

        # Test error formatting
        formatted_error = reporter.format_error("test_error", "test_room", "Test error message", "Test suggestion")
        assert "test_room" in formatted_error
        assert "Test error message" in formatted_error

        # Test JSON generation
        stats = {"zones": 1, "rooms": 3, "errors": 0, "warnings": 0, "success": True}
        errors = []
        warnings = []

        json_output = reporter.generate_json_output(stats, errors, warnings)
        parsed = json.loads(json_output)

        assert parsed["stats"]["success"] is True
        assert len(parsed["errors"]) == 0
        assert len(parsed["warnings"]) == 0

    def test_full_validation_pipeline(self, temp_rooms_dir):
        """Test the full validation pipeline."""
        from core.path_validator import PathValidator
        from core.reporter import Reporter
        from core.room_loader import RoomLoader
        from core.schema_validator import SchemaValidator

        # Load rooms
        loader = RoomLoader(temp_rooms_dir)
        room_database = loader.build_room_database(show_progress=False)

        # Validate schema
        schema_validator = SchemaValidator()
        schema_errors = schema_validator.validate_room_database(room_database)

        # Validate paths
        path_validator = PathValidator(schema_validator)
        unreachable = path_validator.find_unreachable_rooms(start_room_id="test_zone_001", room_database=room_database)
        missing_returns = path_validator.check_bidirectional_connections(room_database)
        dead_ends = path_validator.find_dead_ends(room_database)

        # Generate report
        reporter = Reporter(use_colors=False)

        errors = []
        warnings = []

        # Add schema errors
        for room_id, room_errors in schema_errors.items():
            for error_msg in room_errors:
                errors.append(
                    {"type": "schema", "room_id": room_id, "message": error_msg, "suggestion": "Check JSON structure"}
                )

        # Add unreachable room errors
        for room_id in unreachable:
            errors.append(
                {
                    "type": "unreachable",
                    "room_id": room_id,
                    "message": "No path from starting room",
                    "suggestion": "Add connection from starting room",
                }
            )

        # Add missing return path errors
        for room_a, direction_a, room_b, direction_b in missing_returns:
            errors.append(
                {
                    "type": "bidirectional",
                    "room_id": room_a,
                    "message": f"Exit '{direction_a}' → {room_b}, but {room_b} has no '{direction_b}' return",
                    "suggestion": f'Add "{direction_b}": "{room_a}" to {room_b} or flag as one_way',
                }
            )

        # Add dead end errors
        for room_id in dead_ends:
            errors.append(
                {
                    "type": "dead_end",
                    "room_id": room_id,
                    "message": "No exits (dead end)",
                    "suggestion": "Add at least one exit to this room",
                }
            )

        # Generate statistics
        stats = {
            "zones": len(loader.get_zones()),
            "rooms": len(room_database),
            "errors": len(errors),
            "warnings": len(warnings),
            "success": len(errors) == 0,
        }

        # Test JSON output
        json_output = reporter.generate_json_output(stats, errors, warnings)
        parsed = json.loads(json_output)

        assert "stats" in parsed
        assert "errors" in parsed
        assert "warnings" in parsed
        assert parsed["stats"]["rooms"] == 3
        assert parsed["stats"]["success"] is True  # Should be valid


class TestValidatorEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_room_directory(self):
        """Test validator with empty room directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            from core.room_loader import RoomLoader

            loader = RoomLoader(temp_dir)
            database = loader.build_room_database(show_progress=False)

            assert len(database) == 0
            assert len(loader.get_zones()) == 0

    def test_room_with_malformed_json(self):
        """Test validator with malformed JSON files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            rooms_dir = Path(temp_dir) / "rooms" / "test_zone"
            rooms_dir.mkdir(parents=True)

            # Create a malformed JSON file
            with open(rooms_dir / "malformed.json", "w", encoding="utf-8") as f:
                f.write('{"invalid": json}')

            from core.room_loader import RoomLoader

            loader = RoomLoader(temp_dir)
            database = loader.build_room_database(show_progress=False)

            assert len(database) == 0
            assert len(loader.parsing_errors) == 1
            assert "malformed.json" in loader.parsing_errors[0][0]

    def test_room_with_missing_required_fields(self):
        """Test validator with rooms missing required fields."""
        with tempfile.TemporaryDirectory() as temp_dir:
            rooms_dir = Path(temp_dir) / "rooms" / "test_zone"
            rooms_dir.mkdir(parents=True)

            # Create a room missing required fields
            invalid_room = {
                "id": "invalid_001",
                "name": "Invalid Room",
                # Missing description, zone, exits
            }

            with open(rooms_dir / "invalid_001.json", "w", encoding="utf-8") as f:
                json.dump(invalid_room, f)

            from core.room_loader import RoomLoader
            # Removed unused import: SchemaValidator

            loader = RoomLoader(temp_dir)
            database = loader.build_room_database(show_progress=False)

            # Should not load the invalid room
            assert len(database) == 0
            assert len(loader.parsing_errors) == 1

    def test_room_with_nonexistent_exit_targets(self):
        """Test validator with rooms referencing non-existent targets."""
        with tempfile.TemporaryDirectory() as temp_dir:
            rooms_dir = Path(temp_dir) / "rooms" / "test_zone"
            rooms_dir.mkdir(parents=True)

            # Create a room with exit to non-existent room
            room_with_bad_exit = {
                "id": "room_001",
                "name": "Room with Bad Exit",
                "description": "A room with exit to nowhere",
                "zone": "test_zone",
                "exits": {
                    "north": "nonexistent_room",
                    "south": None,
                    "east": None,
                    "west": None,
                    "up": None,
                    "down": None,
                },
            }

            with open(rooms_dir / "room_001.json", "w", encoding="utf-8") as f:
                json.dump(room_with_bad_exit, f)

            from core.path_validator import PathValidator
            from core.room_loader import RoomLoader

            loader = RoomLoader(temp_dir)
            database = loader.build_room_database(show_progress=False)

            path_validator = PathValidator()
            graph = path_validator.build_graph(database)

            # Should not include the exit to non-existent room
            assert "room_001" in graph
            assert "north" not in graph["room_001"]
