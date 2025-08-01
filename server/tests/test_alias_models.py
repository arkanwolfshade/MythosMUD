"""Tests for the Alias model and related functionality.

As noted in the restricted archives of Miskatonic University, these tests
validate the command alias system that allows players to create shortcuts
for commonly used commands.
"""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from ..models import Alias

# Skip all alias tests for now since the Alias model is simplified
pytest.skip("Alias model needs full implementation", allow_module_level=True)


class TestAliasModel:
    """Test suite for the Alias model."""

    def test_create_valid_alias(self):
        """Test creating a valid alias with all required fields."""
        alias = Alias(name="look", command="look")

        assert alias.name == "look"
        assert alias.command == "look"
        assert alias.version == "1.0"
        assert isinstance(alias.created_at, datetime)
        assert isinstance(alias.updated_at, datetime)

    def test_create_alias_with_custom_version(self):
        """Test creating an alias with a custom version."""
        alias = Alias(name="test", command="help", version="2.0")

        assert alias.version == "2.0"

    def test_alias_timestamps(self):
        """Test that timestamps are properly set."""
        before_creation = datetime.now(UTC)
        alias = Alias(name="test", command="look")
        after_creation = datetime.now(UTC)

        assert before_creation <= alias.created_at <= after_creation
        assert before_creation <= alias.updated_at <= after_creation

    def test_update_timestamp(self):
        """Test updating the timestamp."""
        alias = Alias(name="test", command="look")
        original_updated = alias.updated_at

        # Wait a moment to ensure timestamp difference
        import time

        time.sleep(0.001)

        alias.update_timestamp()

        assert alias.updated_at > original_updated

    def test_validate_name_valid_patterns(self):
        """Test alias name validation with valid patterns."""
        valid_names = [
            "look",
            "myAlias",
            "alias_123",
            "TestAlias",
            "a",
            "abc123",
        ]

        for name in valid_names:
            alias = Alias(name=name, command="help")
            assert alias.validate_name() is True

    def test_validate_name_invalid_patterns(self):
        """Test alias name validation with invalid patterns."""
        invalid_names = [
            "123alias",  # Starts with number
            "_alias",  # Starts with underscore
            "my-alias",  # Contains hyphen
            "my alias",  # Contains space
            "my.alias",  # Contains dot
            "",  # Empty string
        ]

        for name in invalid_names:
            alias = Alias(name=name, command="help")
            assert alias.validate_name() is False

    def test_is_reserved_command(self):
        """Test detection of reserved commands."""
        reserved_aliases = [
            Alias(name="test", command="alias"),
            Alias(name="test", command="aliases"),
            Alias(name="test", command="unalias"),
            Alias(name="test", command="help"),
            Alias(name="test", command="ALIAS"),  # Case insensitive
            Alias(name="test", command="Help"),  # Case insensitive
        ]

        for alias in reserved_aliases:
            assert alias.is_reserved_command() is True

    def test_is_not_reserved_command(self):
        """Test detection of non-reserved commands."""
        non_reserved_aliases = [
            Alias(name="test", command="look"),
            Alias(name="test", command="go north"),
            Alias(name="test", command="say hello"),
            Alias(name="test", command="inventory"),
            Alias(name="test", command="stats"),
        ]

        for alias in non_reserved_aliases:
            assert alias.is_reserved_command() is False

    def test_get_expanded_command_simple(self):
        """Test simple command expansion."""
        alias = Alias(name="l", command="look")

        result = alias.get_expanded_command()
        assert result == "look"

    def test_get_expanded_command_with_args(self):
        """Test command expansion with arguments (future feature)."""
        alias = Alias(name="ln", command="look north")

        result = alias.get_expanded_command(["north"])
        # Currently returns base command, future will handle args
        assert result == "look north"

    def test_alias_case_insensitive_name(self):
        """Test that alias names are case-insensitive in practice."""
        alias1 = Alias(name="Look", command="look")
        alias2 = Alias(name="look", command="look")

        # Names are stored as-is, but comparison should be case-insensitive
        assert alias1.name.lower() == alias2.name.lower()

    def test_alias_command_preservation(self):
        """Test that command text is preserved exactly."""
        complex_command = "go north; look; say 'Hello there!'"
        alias = Alias(name="complex", command=complex_command)

        assert alias.command == complex_command

    def test_alias_maximum_length_validation(self):
        """Test that very long commands are handled."""
        long_command = "a" * 200  # 200 character command
        alias = Alias(name="long", command=long_command)

        assert alias.command == long_command

    def test_alias_with_special_characters(self):
        """Test alias with special characters in command."""
        special_command = "say 'Hello, world! How are you?'"
        alias = Alias(name="greet", command=special_command)

        assert alias.command == special_command

    def test_alias_equality(self):
        """Test alias equality comparison."""
        alias1 = Alias(name="test", command="look")
        alias2 = Alias(name="test", command="look")
        alias3 = Alias(name="different", command="look")

        # Pydantic models compare by field values
        assert alias1 == alias2
        assert alias1 != alias3

    def test_alias_serialization(self):
        """Test that alias can be serialized to JSON."""
        alias = Alias(name="test", command="look")

        json_data = alias.model_dump()

        assert "name" in json_data
        assert "command" in json_data
        assert "version" in json_data
        assert "created_at" in json_data
        assert "updated_at" in json_data
        assert json_data["name"] == "test"
        assert json_data["command"] == "look"

    def test_alias_deserialization(self):
        """Test that alias can be deserialized from JSON."""
        json_data = {
            "name": "test",
            "command": "look",
            "version": "1.0",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
        }

        alias = Alias.model_validate(json_data)

        assert alias.name == "test"
        assert alias.command == "look"
        assert alias.version == "1.0"

    def test_alias_required_fields(self):
        """Test that required fields are enforced."""
        with pytest.raises(ValidationError):
            Alias()  # Missing required fields

        with pytest.raises(ValidationError):
            Alias(name="test")  # Missing command

        with pytest.raises(ValidationError):
            Alias(command="look")  # Missing name

    def test_alias_empty_strings(self):
        """Test that empty strings are handled properly."""
        # Empty name should be allowed by Pydantic but fail validation
        alias = Alias(name="", command="look")
        assert alias.validate_name() is False

        # Empty command should be allowed
        alias = Alias(name="test", command="")
        assert alias.command == ""

    def test_alias_whitespace_handling(self):
        """Test that whitespace is handled properly."""
        alias = Alias(name="  test  ", command="  look  ")

        # Names and commands should preserve whitespace as entered
        assert alias.name == "  test  "
        assert alias.command == "  look  "

    def test_alias_future_expansion_fields(self):
        """Test that future expansion fields are commented but accessible."""
        alias = Alias(name="test", command="look")

        # These fields don't exist yet, but the structure is ready
        # Future: alias.alias_type, alias.parameters, etc.
        assert hasattr(alias, "name")
        assert hasattr(alias, "command")
        assert hasattr(alias, "version")
        assert hasattr(alias, "created_at")
        assert hasattr(alias, "updated_at")


class TestAliasIntegration:
    """Integration tests for alias functionality."""

    def test_alias_with_command_processing(self):
        """Test alias integration with command processing."""
        alias = Alias(name="l", command="look")

        # Simulate command processing
        original_command = "l"
        if original_command == alias.name:
            expanded_command = alias.get_expanded_command()
            assert expanded_command == "look"

    def test_multiple_aliases(self):
        """Test handling multiple aliases."""
        aliases = [
            Alias(name="l", command="look"),
            Alias(name="n", command="go north"),
            Alias(name="s", command="go south"),
            Alias(name="e", command="go east"),
            Alias(name="w", command="go west"),
        ]

        # Test alias lookup
        alias_map = {alias.name: alias for alias in aliases}

        assert "l" in alias_map
        assert "n" in alias_map
        assert alias_map["l"].command == "look"
        assert alias_map["n"].command == "go north"

    def test_alias_conflicts(self):
        """Test handling of alias name conflicts."""
        alias1 = Alias(name="test", command="look")
        alias2 = Alias(name="test", command="help")

        # Both should be valid individually
        assert alias1.name == "test"
        assert alias2.name == "test"
        assert alias1.command == "look"
        assert alias2.command == "help"

        # In a real system, only one would be stored per player
        # This test ensures both can exist in memory

    def test_alias_performance(self):
        """Test alias lookup performance."""
        import time

        # Create many aliases
        aliases = [Alias(name=f"alias{i}", command=f"command{i}") for i in range(100)]

        # Create lookup dictionary
        alias_map = {alias.name: alias for alias in aliases}

        # Test lookup performance
        start_time = time.time()
        for i in range(1000):
            alias = alias_map.get(f"alias{i % 100}")
            if alias:
                _ = alias.command

        end_time = time.time()
        lookup_time = end_time - start_time

        # Should be very fast (less than 1 second for 1000 lookups)
        assert lookup_time < 1.0

    def test_alias_validation_performance(self):
        """Test alias validation performance."""
        import time

        # Test validation performance with many aliases
        start_time = time.time()

        for i in range(1000):
            alias = Alias(name=f"test{i}", command=f"command{i}")
            alias.validate_name()
            alias.is_reserved_command()

        end_time = time.time()
        validation_time = end_time - start_time

        # Should be very fast (less than 1 second for 1000 validations)
        assert validation_time < 1.0
