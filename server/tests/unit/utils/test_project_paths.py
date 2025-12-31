"""
Unit tests for project_paths utilities.

Tests path resolution functions.
"""

from pathlib import Path
from unittest.mock import patch

from server.utils.project_paths import (
    get_calendar_paths_for_environment,
    get_environment_data_dir,
    get_project_root,
    normalize_environment,
)


def test_get_project_root():
    """Test get_project_root() returns project root path."""
    result = get_project_root()
    assert isinstance(result, Path)


def test_normalize_environment():
    """Test normalize_environment() normalizes environment names."""
    assert normalize_environment("production") == "local"
    assert normalize_environment("test") == "test"
    # When None is passed, it reads from LOGGING_ENVIRONMENT env var or defaults to "local"
    # In test environment, LOGGING_ENVIRONMENT is set to "unit_test", so we test that behavior
    with patch.dict("os.environ", {}, clear=False):
        # Remove LOGGING_ENVIRONMENT to test default
        import os

        original_env = os.environ.pop("LOGGING_ENVIRONMENT", None)
        try:
            assert normalize_environment(None) == "local"
        finally:
            if original_env:
                os.environ["LOGGING_ENVIRONMENT"] = original_env


def test_get_environment_data_dir():
    """Test get_environment_data_dir() returns data directory."""
    result = get_environment_data_dir("test")
    assert isinstance(result, Path)
    assert "data" in str(result)
    assert "test" in str(result)


def test_get_calendar_paths_for_environment():
    """Test get_calendar_paths_for_environment() returns calendar paths."""
    holidays_file, schedules_dir = get_calendar_paths_for_environment("test")
    assert isinstance(holidays_file, Path)
    assert isinstance(schedules_dir, Path)
    assert "calendar" in str(holidays_file)
    assert "schedules" in str(schedules_dir)
