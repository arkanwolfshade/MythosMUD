"""
Unit tests for container persistence.
"""

import json

import pytest

from server.persistence.container_persistence import _parse_jsonb_column


def test_parse_jsonb_column_none():
    """Test parsing None JSONB column."""
    result = _parse_jsonb_column(None, {})
    assert result == {}


def test_parse_jsonb_column_string():
    """Test parsing string JSONB column."""
    data = {"key": "value"}
    result = _parse_jsonb_column(json.dumps(data), {})
    assert result == data


def test_parse_jsonb_column_dict():
    """Test parsing dict JSONB column."""
    data = {"key": "value"}
    result = _parse_jsonb_column(data, {})
    assert result == data


def test_parse_jsonb_column_empty_string():
    """Test parsing empty string JSONB column."""
    result = _parse_jsonb_column("", {})
    assert result == {}


def test_parse_jsonb_column_list():
    """Test parsing list JSONB column."""
    data = [1, 2, 3]
    result = _parse_jsonb_column(data, [])
    assert result == data


def test_parse_jsonb_column_invalid_json():
    """Test parsing invalid JSON string."""
    # Should raise JSONDecodeError, but function doesn't handle it
    # This tests the current behavior
    with pytest.raises(json.JSONDecodeError):
        _parse_jsonb_column("{invalid json}", {})

