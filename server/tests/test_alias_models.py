"""Tests for the Alias model and related functionality.

As noted in the restricted archives of Miskatonic University, these tests
validate the command alias system that allows players to create shortcuts
for commonly used commands.
"""

import uuid
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from ..models import Alias


class TestAliasModel:
    """Test suite for the Alias model."""

    def test_create_valid_alias(self):
        """Test creating a valid alias with all required fields."""
        alias = Alias(name="look", command="look")

        assert alias.name == "look"
        assert alias.command == "look"
        assert isinstance(alias.id, str)
        assert isinstance(alias.created_at, datetime)
        assert isinstance(alias.updated_at, datetime)

    def test_create_alias_with_custom_timestamps(self):
        """Test creating an alias with custom timestamps."""
        custom_time = datetime(2024, 1, 1, 12, 0, 0)
        alias = Alias(name="test", command="look", created_at=custom_time, updated_at=custom_time)

        assert alias.created_at == custom_time
        assert alias.updated_at == custom_time

    def test_create_alias_with_custom_id(self):
        """Test creating an alias with a custom ID."""
        custom_id = str(uuid.uuid4())
        alias = Alias(id=custom_id, name="test", command="help")

        assert alias.id == custom_id
        assert alias.name == "test"
        assert alias.command == "help"

    def test_alias_timestamps(self):
        """Test that timestamps are properly set."""
        before_creation = datetime.now(UTC)
        alias = Alias(name="test", command="look")
        after_creation = datetime.now(UTC)

        # Convert alias timestamps to UTC for comparison
        alias_created_utc = alias.created_at.replace(tzinfo=UTC)
        alias_updated_utc = alias.updated_at.replace(tzinfo=UTC)

        assert before_creation <= alias_created_utc <= after_creation
        assert before_creation <= alias_updated_utc <= after_creation

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
        # Empty name should be allowed by Pydantic
        alias = Alias(name="", command="look")
        assert alias.name == ""

        # Empty command should be allowed
        alias = Alias(name="test", command="")
        assert alias.command == ""

    def test_alias_whitespace_handling(self):
        """Test that whitespace is handled properly."""
        alias = Alias(name="  test  ", command="  look  ")

        # Names and commands should preserve whitespace as entered
        assert alias.name == "  test  "
        assert alias.command == "  look  "

    def test_alias_equality(self):
        """Test alias equality comparison."""
        # Create aliases with same ID and timestamps for equality test
        custom_id = str(uuid.uuid4())
        custom_timestamp = datetime.now(UTC)
        alias1 = Alias(
            id=custom_id, name="test", command="look", created_at=custom_timestamp, updated_at=custom_timestamp
        )
        alias2 = Alias(
            id=custom_id, name="test", command="look", created_at=custom_timestamp, updated_at=custom_timestamp
        )
        alias3 = Alias(name="different", command="look")

        # Pydantic models compare by field values
        assert alias1 == alias2
        assert alias1 != alias3

    def test_alias_serialization(self):
        """Test that alias can be serialized to JSON."""
        alias = Alias(name="test", command="look")

        json_data = alias.model_dump()

        assert "id" in json_data
        assert "name" in json_data
        assert "command" in json_data
        assert "created_at" in json_data
        assert "updated_at" in json_data
        assert json_data["name"] == "test"
        assert json_data["command"] == "look"
        assert json_data["id"] == alias.id

    def test_alias_deserialization(self):
        """Test that alias can be deserialized from JSON."""
        custom_id = str(uuid.uuid4())
        json_data = {
            "id": custom_id,
            "name": "test",
            "command": "look",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
        }

        alias = Alias.model_validate(json_data)

        assert alias.id == custom_id
        assert alias.name == "test"
        assert alias.command == "look"

    def test_alias_repr(self):
        """Test the string representation of alias."""
        alias = Alias(name="test", command="look")
        repr_str = repr(alias)

        assert "Alias" in repr_str
        assert "test" in repr_str
        assert "look" in repr_str
        assert alias.id in repr_str

    def test_alias_model_dump_method(self):
        """Test the custom model_dump method."""
        alias = Alias(name="test", command="look")
        dump_data = alias.model_dump()

        assert dump_data["id"] == alias.id
        assert dump_data["name"] == "test"
        assert dump_data["command"] == "look"
        assert dump_data["created_at"].endswith("Z")
        assert dump_data["updated_at"].endswith("Z")

    def test_alias_with_special_characters(self):
        """Test alias with special characters in command."""
        special_command = "say 'Hello, world! How are you?'"
        alias = Alias(name="greet", command=special_command)

        assert alias.command == special_command

    def test_alias_maximum_length_validation(self):
        """Test that very long commands are handled."""
        long_command = "a" * 200  # 200 character command
        alias = Alias(name="long", command=long_command)

        assert alias.command == long_command

    def test_alias_case_insensitive_name(self):
        """Test that alias names preserve case as entered."""
        alias1 = Alias(name="Look", command="look")
        alias2 = Alias(name="look", command="look")

        # Names should be stored exactly as entered
        assert alias1.name == "Look"
        assert alias2.name == "look"
        assert alias1.name != alias2.name

    def test_alias_command_preservation(self):
        """Test that command text is preserved exactly."""
        complex_command = "go north; look; say 'Hello there!'"
        alias = Alias(name="complex", command=complex_command)

        assert alias.command == complex_command

    def test_alias_uuid_generation(self):
        """Test that UUIDs are properly generated."""
        alias1 = Alias(name="test1", command="look")
        alias2 = Alias(name="test2", command="help")

        # Each should have a unique ID
        assert alias1.id != alias2.id
        assert len(alias1.id) > 0
        assert len(alias2.id) > 0

        # IDs should be valid UUID strings
        try:
            uuid.UUID(alias1.id)
            uuid.UUID(alias2.id)
        except ValueError:
            pytest.fail("Generated IDs are not valid UUIDs")

    def test_alias_timestamp_format(self):
        """Test that timestamps are in the correct format."""
        alias = Alias(name="test", command="look")
        dump_data = alias.model_dump()

        # Check that timestamps end with 'Z' (UTC indicator)
        assert dump_data["created_at"].endswith("Z")
        assert dump_data["updated_at"].endswith("Z")

        # Check that timestamps are valid ISO format
        from datetime import datetime

        datetime.fromisoformat(dump_data["created_at"].replace("Z", "+00:00"))
        datetime.fromisoformat(dump_data["updated_at"].replace("Z", "+00:00"))


class TestAliasIntegration:
    """Integration tests for alias functionality."""

    def test_alias_with_command_processing(self):
        """Test alias integration with command processing."""
        alias = Alias(name="l", command="look")

        # Simulate command processing
        original_command = "l"
        if original_command == alias.name:
            expanded_command = alias.command
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

    def test_alias_serialization_performance(self):
        """Test alias serialization performance."""
        import time

        # Test serialization performance with many aliases
        aliases = [Alias(name=f"test{i}", command=f"command{i}") for i in range(100)]

        start_time = time.time()
        for alias in aliases:
            _ = alias.model_dump()

        end_time = time.time()
        serialization_time = end_time - start_time

        # Should be very fast (less than 1 second for 100 serializations)
        assert serialization_time < 1.0

    def test_alias_field_access(self):
        """Test that all alias fields are accessible."""
        alias = Alias(name="test", command="look")

        # Test all fields are accessible
        assert hasattr(alias, "id")
        assert hasattr(alias, "name")
        assert hasattr(alias, "command")
        assert hasattr(alias, "created_at")
        assert hasattr(alias, "updated_at")

        # Test field values
        assert isinstance(alias.id, str)
        assert isinstance(alias.name, str)
        assert isinstance(alias.command, str)
        assert isinstance(alias.created_at, datetime)
        assert isinstance(alias.updated_at, datetime)
