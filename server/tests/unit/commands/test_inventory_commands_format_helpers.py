"""
Unit tests for inventory command formatting helper functions.

Tests the formatting helper functions in inventory_commands.py.
"""

from server.commands.inventory_commands import _format_metadata


def test_format_metadata_empty():
    """Test _format_metadata() returns empty string for None."""
    result = _format_metadata(None)
    assert result == ""


def test_format_metadata_simple():
    """Test _format_metadata() formats simple metadata."""
    metadata = {"key1": "value1", "key2": "value2"}
    result = _format_metadata(metadata)
    assert "key1=value1" in result
    assert "key2=value2" in result


def test_format_metadata_nested_dict():
    """Test _format_metadata() formats nested dict."""
    metadata = {"container": {"id": "container_001"}}
    result = _format_metadata(metadata)
    assert "container=" in result
