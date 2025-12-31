"""
Unit tests for error_logging utilities.

Tests error logging helper functions.
"""

from server.utils.error_logging import create_error_context


def test_create_error_context():
    """Test create_error_context() creates error context."""
    context = create_error_context()
    assert context is not None
    assert hasattr(context, "to_dict")


def test_create_error_context_with_metadata():
    """Test create_error_context() can include metadata."""
    context = create_error_context()
    context.metadata = {"key": "value"}
    assert context.metadata == {"key": "value"}


def test_error_context_to_dict():
    """Test error context to_dict() method."""
    context = create_error_context()
    context.metadata = {"key": "value"}
    result = context.to_dict()
    assert isinstance(result, dict)
    assert "metadata" in result or "key" in result
