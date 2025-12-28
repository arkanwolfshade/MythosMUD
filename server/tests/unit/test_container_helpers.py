"""
Unit tests for container helper functions.

Tests the helper functions in container.py.
"""

from server.container import get_container, reset_container


def test_get_container():
    """Test get_container() returns container instance."""
    # This will return None if container not initialized, or the instance if it is
    result = get_container()
    # Just verify it doesn't raise
    assert result is None or hasattr(result, "player_service")


def test_reset_container():
    """Test reset_container() resets container instance."""
    reset_container()
    result = get_container()
    # After reset, get_container may return None or a new uninitialized instance
    assert result is None or (hasattr(result, "_initialized") and not result._initialized)
