"""
Unit tests for connection helpers.

Tests the connection helper functions.
"""

import uuid

from server.realtime.connection_helpers import convert_uuids_to_strings


def test_convert_uuids_to_strings_uuid():
    """Test convert_uuids_to_strings() with UUID object."""
    player_id = uuid.uuid4()
    result = convert_uuids_to_strings(player_id)
    assert isinstance(result, str)
    assert result == str(player_id)


def test_convert_uuids_to_strings_dict():
    """Test convert_uuids_to_strings() with dict containing UUID."""
    player_id = uuid.uuid4()
    data = {"player_id": player_id, "name": "TestPlayer"}
    result = convert_uuids_to_strings(data)
    assert isinstance(result["player_id"], str)
    assert result["name"] == "TestPlayer"


def test_convert_uuids_to_strings_list():
    """Test convert_uuids_to_strings() with list containing UUID."""
    player_id1 = uuid.uuid4()
    player_id2 = uuid.uuid4()
    data = [player_id1, player_id2, "string_value"]
    result = convert_uuids_to_strings(data)
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)
    assert result[2] == "string_value"


def test_convert_uuids_to_strings_nested():
    """Test convert_uuids_to_strings() with nested structures."""
    player_id = uuid.uuid4()
    data = {"players": [{"id": player_id, "name": "TestPlayer"}]}
    result = convert_uuids_to_strings(data)
    assert isinstance(result["players"][0]["id"], str)
    assert result["players"][0]["name"] == "TestPlayer"


def test_convert_uuids_to_strings_string():
    """Test convert_uuids_to_strings() with string (no conversion)."""
    result = convert_uuids_to_strings("test_string")
    assert result == "test_string"


def test_convert_uuids_to_strings_int():
    """Test convert_uuids_to_strings() with int (no conversion)."""
    result = convert_uuids_to_strings(42)
    assert result == 42
