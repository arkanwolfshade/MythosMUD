"""
Tests for the reporter module.

Tests output formatting, color handling, and JSON generation.
"""

import json

# Removed unused import: pytest
from core.reporter import Reporter


# pylint: disable=too-many-public-methods
class TestReporter:
    """Test cases for the Reporter class."""

    def test_init_with_colors(self):
        """Test Reporter initialization with colors enabled."""
        reporter = Reporter(use_colors=True)
        assert reporter.use_colors is True

    def test_init_without_colors(self):
        """Test Reporter initialization with colors disabled."""
        reporter = Reporter(use_colors=False)
        assert reporter.use_colors is False

    def test_format_error_with_suggestion(self):
        """Test formatting error with suggestion."""
        reporter = Reporter(use_colors=False)
        formatted = reporter.format_error(
            "bidirectional", "test_001", "Missing return path", "Add south exit to test_002"
        )

        assert "test_001" in formatted
        assert "Bidirectional" in formatted
        assert "Missing return path" in formatted
        assert "Add south exit to test_002" in formatted

    def test_format_error_without_suggestion(self):
        """Test formatting error without suggestion."""
        reporter = Reporter(use_colors=False)
        formatted = reporter.format_error("unreachable", "test_001", "No path from starting room")

        assert "test_001" in formatted
        assert "Unreachable" in formatted
        assert "No path from starting room" in formatted

    def test_format_warning(self):
        """Test formatting warning."""
        reporter = Reporter(use_colors=False)
        formatted = reporter.format_warning("potential_dead_end", "test_001", "Only one exit")

        assert "test_001" in formatted
        assert "Potential_Dead_End" in formatted
        assert "Only one exit" in formatted

    def test_generate_json_output(self):
        """Test JSON output generation."""
        reporter = Reporter()

        stats = {"zones": 1, "rooms": 3, "errors": 1, "warnings": 2, "success": False}

        errors = [
            {
                "type": "bidirectional",
                "room_id": "test_001",
                "message": "Missing return path",
                "suggestion": "Add south exit",
            }
        ]

        warnings = [{"type": "potential_dead_end", "room_id": "test_002", "message": "Only one exit"}]

        json_output = reporter.generate_json_output(stats, errors, warnings)

        # Parse the JSON to verify structure
        parsed = json.loads(json_output)

        assert "summary" in parsed
        assert "errors" in parsed
        assert "warnings" in parsed

        assert parsed["summary"]["zones"] == 1
        assert parsed["summary"]["rooms"] == 3
        assert parsed["summary"]["errors"] == 1
        assert parsed["summary"]["warnings"] == 2
        assert parsed["summary"]["success"] is False

        assert len(parsed["errors"]) == 1
        assert parsed["errors"][0]["type"] == "bidirectional"
        assert parsed["errors"][0]["room_id"] == "test_001"

        assert len(parsed["warnings"]) == 1
        assert parsed["warnings"][0]["type"] == "potential_dead_end"
        assert parsed["warnings"][0]["room_id"] == "test_002"

    def test_colorize_output_with_colors(self):
        """Test colorizing output with colors enabled."""
        reporter = Reporter(use_colors=True)
        colored = reporter.colorize_output("test message", "red")

        # Should contain color codes
        assert "test message" in colored
        assert len(colored) > len("test message")

    def test_colorize_output_without_colors(self):
        """Test colorizing output with colors disabled."""
        reporter = Reporter(use_colors=False)
        colored = reporter.colorize_output("test message", "red")

        # Should return original text without color codes
        assert colored == "test message"

    def test_colorize_output_unknown_color(self):
        """Test colorizing output with unknown color."""
        reporter = Reporter(use_colors=True)
        colored = reporter.colorize_output("test message", "unknown")

        # Should return original text for unknown colors
        assert colored == "test message"

    def test_print_header_default(self, capsys):
        """Test printing default header."""
        reporter = Reporter(use_colors=False)
        reporter.print_header()

        captured = capsys.readouterr()
        assert "🔍 Room Validator v1.0" in captured.out

    def test_print_header_custom_title(self, capsys):
        """Test printing header with custom title."""
        reporter = Reporter(use_colors=False)
        reporter.print_header("Custom Title")

        captured = capsys.readouterr()
        assert "🔍 Custom Title" in captured.out

    def test_print_progress(self, capsys):
        """Test printing progress message."""
        reporter = Reporter(use_colors=False)
        reporter.print_progress("Processing rooms...")

        captured = capsys.readouterr()
        assert "🔄 Processing rooms..." in captured.out

    def test_print_success(self, capsys):
        """Test printing success message."""
        reporter = Reporter(use_colors=False)
        reporter.print_success("Validation passed")

        captured = capsys.readouterr()
        assert "✅ Validation passed" in captured.out

    def test_print_error(self, capsys):
        """Test printing error message."""
        reporter = Reporter(use_colors=False)
        reporter.print_error("Validation failed")

        captured = capsys.readouterr()
        assert "❌ Validation failed" in captured.out

    def test_print_warning(self, capsys):
        """Test printing warning message."""
        reporter = Reporter(use_colors=False)
        reporter.print_warning("Potential issue")

        captured = capsys.readouterr()
        assert "⚠️  Potential issue" in captured.out

    def test_print_summary_success(self, capsys):
        """Test printing summary for successful validation."""
        reporter = Reporter(use_colors=False)

        stats = {"zones": 1, "rooms": 3, "errors": 0, "warnings": 1, "success": True}

        reporter.print_summary(stats)

        captured = capsys.readouterr()
        assert "📊 SUMMARY:" in captured.out
        assert "Zones: 1" in captured.out
        assert "Rooms: 3 total" in captured.out
        assert "Errors: 0 🔴" in captured.out
        assert "Warnings: 1 🟡" in captured.out
        assert "✅ Validation passed" in captured.out

    def test_print_summary_failure(self, capsys):
        """Test printing summary for failed validation."""
        reporter = Reporter(use_colors=False)

        stats = {"zones": 1, "rooms": 3, "errors": 2, "warnings": 1, "success": False}

        reporter.print_summary(stats)

        captured = capsys.readouterr()
        assert "📊 SUMMARY:" in captured.out
        assert "Errors: 2 🔴" in captured.out
        assert "❌ Validation failed" in captured.out

    def test_print_zone_discovery(self, capsys):
        """Test printing zone discovery."""
        reporter = Reporter(use_colors=False)
        zones = ["arkham", "dungeon"]

        reporter.print_zone_discovery(zones)

        captured = capsys.readouterr()
        assert "📁 Scanning zones..." in captured.out
        assert "✅ arkham zone discovered" in captured.out
        assert "✅ dungeon zone discovered" in captured.out

    def test_print_parsing_errors(self, capsys):
        """Test printing parsing errors."""
        reporter = Reporter(use_colors=False)
        parsing_errors = [("file1.json", "Invalid JSON"), ("file2.json", "Missing required field")]

        reporter.print_parsing_errors(parsing_errors)

        captured = capsys.readouterr()
        assert "❌ PARSING ERRORS:" in captured.out
        assert "file1.json: Invalid JSON" in captured.out
        assert "file2.json: Missing required field" in captured.out

    def test_print_parsing_errors_empty(self, capsys):
        """Test printing parsing errors when none exist."""
        reporter = Reporter(use_colors=False)
        reporter.print_parsing_errors([])

        captured = capsys.readouterr()
        assert "❌ PARSING ERRORS:" not in captured.out

    def test_print_validation_errors(self, capsys):
        """Test printing validation errors."""
        reporter = Reporter(use_colors=False)
        errors = [
            {
                "type": "bidirectional",
                "room_id": "test_001",
                "message": "Missing return path",
                "suggestion": "Add south exit",
            }
        ]

        reporter.print_validation_errors(errors)

        captured = capsys.readouterr()
        assert "❌ ERRORS FOUND:" in captured.out
        assert "test_001" in captured.out
        assert "Bidirectional" in captured.out

    def test_print_validation_errors_empty(self, capsys):
        """Test printing validation errors when none exist."""
        reporter = Reporter(use_colors=False)
        reporter.print_validation_errors([])

        captured = capsys.readouterr()
        assert "❌ ERRORS FOUND:" not in captured.out

    def test_print_validation_warnings(self, capsys):
        """Test printing validation warnings."""
        reporter = Reporter(use_colors=False)
        warnings = [{"type": "potential_dead_end", "room_id": "test_001", "message": "Only one exit"}]

        reporter.print_validation_warnings(warnings)

        captured = capsys.readouterr()
        assert "⚠️  WARNINGS:" in captured.out
        assert "test_001" in captured.out
        assert "Potential_Dead_End" in captured.out

    def test_print_validation_warnings_empty(self, capsys):
        """Test printing validation warnings when none exist."""
        reporter = Reporter(use_colors=False)
        reporter.print_validation_warnings([])

        captured = capsys.readouterr()
        assert "⚠️  WARNINGS:" not in captured.out
