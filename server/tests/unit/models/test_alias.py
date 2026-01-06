"""
Unit tests for the Alias model.

Tests the Alias model methods including validation, equality, hashing, and command expansion.
"""

from datetime import UTC, datetime

import pytest

from server.models.alias import Alias


def test_alias_repr():
    """Test __repr__ returns expected string format."""
    alias = Alias(name="test", command="look")
    alias.id = "test-id-123"

    repr_str = repr(alias)

    assert "Alias" in repr_str
    assert "test-id-123" in repr_str
    assert "test" in repr_str
    assert "look" in repr_str


def test_alias_equality_same_name_and_command():
    """Test __eq__ returns True for aliases with same name and command."""
    alias1 = Alias(name="test", command="look")
    alias2 = Alias(name="test", command="look")

    assert alias1 == alias2


def test_alias_equality_different_ids():
    """Test __eq__ returns True even if IDs are different."""
    alias1 = Alias(name="test", command="look")
    alias1.id = "id1"
    alias2 = Alias(name="test", command="look")
    alias2.id = "id2"

    assert alias1 == alias2


def test_alias_equality_different_name():
    """Test __eq__ returns False for aliases with different names."""
    alias1 = Alias(name="test1", command="look")
    alias2 = Alias(name="test2", command="look")

    assert alias1 != alias2


def test_alias_equality_different_command():
    """Test __eq__ returns False for aliases with different commands."""
    alias1 = Alias(name="test", command="look")
    alias2 = Alias(name="test", command="go north")

    assert alias1 != alias2


def test_alias_equality_with_non_alias():
    """Test __eq__ returns False when comparing with non-Alias object."""
    alias = Alias(name="test", command="look")

    assert alias != "not an alias"
    assert alias != {"name": "test", "command": "look"}
    assert alias != None  # noqa: E711


def test_alias_hash_same_name_and_command():
    """Test __hash__ returns same hash for aliases with same name and command."""
    alias1 = Alias(name="test", command="look")
    alias2 = Alias(name="test", command="look")

    assert hash(alias1) == hash(alias2)


def test_alias_hash_different_name():
    """Test __hash__ returns different hash for aliases with different names."""
    alias1 = Alias(name="test1", command="look")
    alias2 = Alias(name="test2", command="look")

    assert hash(alias1) != hash(alias2)


def test_alias_hash_different_command():
    """Test __hash__ returns different hash for aliases with different commands."""
    alias1 = Alias(name="test", command="look")
    alias2 = Alias(name="test", command="go north")

    assert hash(alias1) != hash(alias2)


def test_alias_hash_usable_in_set():
    """Test __hash__ allows aliases to be used in sets."""
    alias1 = Alias(name="test1", command="look")
    alias2 = Alias(name="test2", command="go")
    alias3 = Alias(name="test1", command="look")  # Same as alias1

    alias_set = {alias1, alias2, alias3}

    assert len(alias_set) == 2  # alias1 and alias3 are equal, so only 2 unique items


def test_alias_update_timestamp():
    """Test update_timestamp updates the updated_at field."""
    alias = Alias(name="test", command="look")
    original_updated_at = alias.updated_at

    # Wait a tiny bit to ensure timestamp changes
    import time

    time.sleep(0.01)

    alias.update_timestamp()

    assert alias.updated_at > original_updated_at
    assert alias.updated_at.tzinfo is None  # Should be naive UTC


def test_alias_is_reserved_command_true():
    """Test is_reserved_command returns True for reserved command names."""
    reserved_names = ["help", "quit", "look", "inventory", "alias", "who", "say", "emote"]

    for name in reserved_names:
        alias = Alias(name=name, command="some command")
        assert alias.is_reserved_command() is True


def test_alias_is_reserved_command_case_insensitive():
    """Test is_reserved_command is case insensitive."""
    alias_upper = Alias(name="HELP", command="some command")
    alias_lower = Alias(name="help", command="some command")
    alias_mixed = Alias(name="Help", command="some command")

    assert alias_upper.is_reserved_command() is True
    assert alias_lower.is_reserved_command() is True
    assert alias_mixed.is_reserved_command() is True


def test_alias_is_reserved_command_false():
    """Test is_reserved_command returns False for non-reserved names."""
    alias = Alias(name="myalias", command="some command")

    assert alias.is_reserved_command() is False


def test_alias_validate_name_valid():
    """Test validate_name returns True for valid names."""
    alias = Alias(name="testalias", command="look")

    assert alias.validate_name() is True


def test_alias_validate_name_with_whitespace():
    """Test validate_name returns True for names with leading/trailing whitespace."""
    alias = Alias(name="  testalias  ", command="look")

    assert alias.validate_name() is True


def test_alias_validate_name_empty():
    """Test validate_name returns False for empty name."""
    alias = Alias(name="", command="look")

    assert alias.validate_name() is False


def test_alias_validate_name_whitespace_only():
    """Test validate_name returns False for whitespace-only name."""
    alias = Alias(name="   ", command="look")

    assert alias.validate_name() is False


def test_alias_get_expanded_command_no_args():
    """Test get_expanded_command returns command as-is when no args."""
    alias = Alias(name="test", command="look")

    result = alias.get_expanded_command()

    assert result == "look"


def test_alias_get_expanded_command_with_args():
    """Test get_expanded_command returns command as-is even with args (current implementation)."""
    alias = Alias(name="test", command="look")

    result = alias.get_expanded_command(_args=["north"])

    # Current implementation just returns command as-is
    assert result == "look"


def test_alias_model_dump():
    """Test model_dump returns dictionary with all fields."""
    alias = Alias(name="test", command="look")
    alias.id = "test-id-123"
    alias.version = "1.0"

    result = alias.model_dump()

    assert result["id"] == "test-id-123"
    assert result["name"] == "test"
    assert result["command"] == "look"
    assert result["version"] == "1.0"
    assert "created_at" in result
    assert "updated_at" in result
    assert result["created_at"].endswith("Z")
    assert result["updated_at"].endswith("Z")


def test_alias_model_dump_timestamps_isoformat():
    """Test model_dump returns timestamps in ISO format with Z suffix."""
    alias = Alias(name="test", command="look")

    result = alias.model_dump()

    # Should be valid ISO format strings ending with Z
    assert isinstance(result["created_at"], str)
    assert isinstance(result["updated_at"], str)
    assert result["created_at"].endswith("Z")
    assert result["updated_at"].endswith("Z")

    # Should be parseable as datetime
    created = datetime.fromisoformat(result["created_at"].replace("Z", "+00:00"))
    updated = datetime.fromisoformat(result["updated_at"].replace("Z", "+00:00"))
    assert isinstance(created, datetime)
    assert isinstance(updated, datetime)


def test_alias_default_id():
    """Test Alias generates UUID id by default."""
    alias1 = Alias(name="test1", command="look")
    alias2 = Alias(name="test2", command="go")

    # Should have different IDs
    assert alias1.id != alias2.id
    assert len(alias1.id) > 0
    assert len(alias2.id) > 0


def test_alias_default_version():
    """Test Alias has default version."""
    alias = Alias(name="test", command="look")

    assert alias.version == "1.0"


def test_alias_default_timestamps():
    """Test Alias has default timestamps."""
    before = datetime.now(UTC)
    alias = Alias(name="test", command="look")
    after = datetime.now(UTC)

    assert alias.created_at.tzinfo is None  # Should be naive
    assert alias.updated_at.tzinfo is None  # Should be naive

    # Convert to UTC for comparison
    created_utc = alias.created_at.replace(tzinfo=UTC)
    updated_utc = alias.updated_at.replace(tzinfo=UTC)

    assert before <= created_utc <= after
    assert before <= updated_utc <= after


def test_alias_rejects_extra_fields():
    """Test Alias rejects unknown fields (extra='forbid')."""
    from pydantic import ValidationError

    with pytest.raises(ValidationError) as exc_info:
        Alias(name="test", command="look", unknown_field="value")

    error_str = str(exc_info.value).lower()
    assert "extra" in error_str and ("not permitted" in error_str or "forbidden" in error_str)
