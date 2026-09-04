"""
Unit tests for database initialization.
"""

import pytest

from server.database import DatabaseManager


def test_database_manager_singleton():
    """Test that DatabaseManager is a singleton."""
    # Reset instance first
    DatabaseManager.reset_instance()

    instance1 = DatabaseManager.get_instance()
    instance2 = DatabaseManager.get_instance()

    assert instance1 is instance2


def test_database_manager_reset_instance():
    """Test resetting the singleton instance."""
    instance1 = DatabaseManager.get_instance()
    DatabaseManager.reset_instance()
    instance2 = DatabaseManager.get_instance()

    assert instance1 is not instance2


def test_database_manager_direct_init_raises():
    """Test that direct initialization raises RuntimeError when instance exists."""
    # First get an instance
    _instance = DatabaseManager.get_instance()

    # Now trying to create another should raise
    with pytest.raises(RuntimeError, match="Use DatabaseManager.get_instance"):
        DatabaseManager()


def test_database_manager_initial_state():
    """Test initial state of database manager."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    assert manager.engine is None
    assert manager.session_maker is None
    assert manager.database_url is None
    assert manager._initialized is False
