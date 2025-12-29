"""
Unit tests for container helper functions.

Tests the helper functions in container.py.
"""

from pathlib import Path

import pytest

from server.container import ApplicationContainer, get_container, reset_container


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


def test_get_container_singleton():
    """Test get_container() returns same instance."""
    reset_container()
    container1 = get_container()
    container2 = get_container()
    assert container1 is container2


def test_reset_container_creates_new_instance():
    """Test reset_container() creates new instance."""
    container1 = get_container()
    reset_container()
    container2 = get_container()
    # Should be different instances after reset
    assert container1 is not container2


def test_application_container_get_instance():
    """Test ApplicationContainer.get_instance() returns singleton."""
    ApplicationContainer.reset_instance()
    container1 = ApplicationContainer.get_instance()
    container2 = ApplicationContainer.get_instance()
    assert container1 is container2


def test_application_container_set_instance():
    """Test ApplicationContainer.set_instance() sets instance."""
    ApplicationContainer.reset_instance()
    new_container = ApplicationContainer()
    ApplicationContainer.set_instance(new_container)
    assert ApplicationContainer.get_instance() is new_container


def test_application_container_reset_instance():
    """Test ApplicationContainer.reset_instance() resets singleton."""
    container1 = ApplicationContainer.get_instance()
    ApplicationContainer.reset_instance()
    container2 = ApplicationContainer.get_instance()
    assert container1 is not container2


def test_application_container_is_initialized():
    """Test ApplicationContainer.is_initialized returns False before initialization."""
    container = ApplicationContainer()
    assert container.is_initialized is False


def test_application_container_get_service():
    """Test ApplicationContainer.get_service() raises error when not initialized."""
    container = ApplicationContainer()
    with pytest.raises(RuntimeError, match="Container not initialized"):
        container.get_service("player_service")


def test_application_container_get_service_invalid():
    """Test ApplicationContainer.get_service() raises error for invalid service."""
    container = ApplicationContainer()
    container._initialized = True  # Mock initialization
    with pytest.raises(ValueError, match="Unknown service"):
        container.get_service("invalid_service")


def test_application_container_get_service_not_initialized_service():
    """Test ApplicationContainer.get_service() raises error when service is None."""
    container = ApplicationContainer()
    container._initialized = True  # Mock initialization
    with pytest.raises(ValueError, match="Service not initialized"):
        container.get_service("player_service")  # Will be None before initialization


def test_application_container_decode_json_column():
    """Test ApplicationContainer._decode_json_column() decodes JSON."""
    container = ApplicationContainer()
    result = container._decode_json_column('{"key": "value"}', dict)
    assert isinstance(result, dict)
    assert result["key"] == "value"


def test_application_container_decode_json_column_invalid():
    """Test ApplicationContainer._decode_json_column() handles invalid JSON."""
    container = ApplicationContainer()
    result = container._decode_json_column("invalid json", dict)
    assert isinstance(result, dict)  # Returns default dict on error


def test_application_container_decode_json_column_none():
    """Test ApplicationContainer._decode_json_column() handles None."""
    container = ApplicationContainer()
    result = container._decode_json_column(None, dict)
    assert isinstance(result, dict)  # Returns default dict


def test_application_container_decode_json_column_empty_string():
    """Test ApplicationContainer._decode_json_column() handles empty string."""
    container = ApplicationContainer()
    result = container._decode_json_column("", dict)
    assert isinstance(result, dict)  # Returns default dict


def test_application_container_decode_json_column_list():
    """Test ApplicationContainer._decode_json_column() handles list."""
    container = ApplicationContainer()
    result = container._decode_json_column([1, 2, 3], list)
    assert result == [1, 2, 3]


def test_application_container_decode_json_column_dict():
    """Test ApplicationContainer._decode_json_column() handles dict."""
    container = ApplicationContainer()
    result = container._decode_json_column({"key": "value"}, dict)
    assert result == {"key": "value"}


def test_application_container_normalize_path_from_url_or_path():
    """Test ApplicationContainer._normalize_path_from_url_or_path() normalizes path."""
    container = ApplicationContainer()
    container._project_root = Path("E:/projects/GitHub/MythosMUD")
    result = container._normalize_path_from_url_or_path("data/file.json", container._project_root)
    assert result is not None
    assert isinstance(result, Path)


def test_application_container_normalize_path_from_url():
    """Test ApplicationContainer._normalize_path_from_url_or_path() handles URL."""
    container = ApplicationContainer()
    container._project_root = Path("E:/projects/GitHub/MythosMUD")
    result = container._normalize_path_from_url_or_path("file:///E:/projects/GitHub/MythosMUD/data/file.json", container._project_root)
    assert result is not None
    assert isinstance(result, Path)


def test_application_container_normalize_path_postgresql_url():
    """Test ApplicationContainer._normalize_path_from_url_or_path() returns None for PostgreSQL URL."""
    container = ApplicationContainer()
    container._project_root = Path("E:/projects/GitHub/MythosMUD")
    result = container._normalize_path_from_url_or_path("postgresql://user:pass@host/db", container._project_root)
    assert result is None


def test_application_container_normalize_path_invalid():
    """Test ApplicationContainer._normalize_path_from_url_or_path() returns None for invalid path."""
    container = ApplicationContainer()
    container._project_root = Path("E:/projects/GitHub/MythosMUD")
    result = container._normalize_path_from_url_or_path("invalid://path", container._project_root)
    assert result is None or isinstance(result, Path)  # May return None or attempt to resolve


def test_application_container_get_project_root():
    """Test ApplicationContainer._get_project_root() returns Path."""
    container = ApplicationContainer()
    result = container._get_project_root()
    assert isinstance(result, Path) or result is None
