"""
Unit tests for project path utilities.

Tests the project path resolution helpers used across runtime code and tooling.
"""

import os
from pathlib import Path
from unittest.mock import patch

import pytest

from server.utils.project_paths import (
    get_calendar_paths_for_environment,
    get_environment_data_dir,
    get_project_root,
    normalize_environment,
)


def test_get_project_root_returns_path():
    """Test get_project_root returns a Path object."""
    result = get_project_root()
    
    assert isinstance(result, Path)
    assert result.exists()


def test_get_project_root_contains_pyproject_toml():
    """Test get_project_root returns directory containing pyproject.toml."""
    result = get_project_root()
    
    assert (result / "pyproject.toml").exists()


def test_normalize_environment_none():
    """Test normalize_environment handles None."""
    with patch.dict(os.environ, {}, clear=True):
        result = normalize_environment(None)
        
        assert result == "local"


def test_normalize_environment_empty_string():
    """Test normalize_environment handles empty string."""
    with patch.dict(os.environ, {}, clear=True):
        result = normalize_environment("")
        
        assert result == "local"


def test_normalize_environment_from_env_var():
    """Test normalize_environment reads from LOGGING_ENVIRONMENT."""
    with patch.dict(os.environ, {"LOGGING_ENVIRONMENT": "unit_test"}, clear=False):
        result = normalize_environment(None)
        
        assert result == "unit_test"


def test_normalize_environment_production_alias():
    """Test normalize_environment maps 'production' to 'local'."""
    result = normalize_environment("production")
    
    assert result == "local"


def test_normalize_environment_strips_whitespace():
    """Test normalize_environment strips whitespace."""
    result = normalize_environment("  unit_test  ")
    
    assert result == "unit_test"


def test_normalize_environment_lowercase():
    """Test normalize_environment converts to lowercase."""
    result = normalize_environment("UNIT_TEST")
    
    assert result == "unit_test"


def test_get_environment_data_dir_default():
    """Test get_environment_data_dir uses default environment."""
    with patch.dict(os.environ, {}, clear=True):
        result = get_environment_data_dir(None)
        
        assert isinstance(result, Path)
        assert result.name == "local"
        assert "data" in str(result)


def test_get_environment_data_dir_specific():
    """Test get_environment_data_dir uses specified environment."""
    result = get_environment_data_dir("unit_test")
    
    assert isinstance(result, Path)
    assert result.name == "unit_test"
    assert "data" in str(result)


def test_get_environment_data_dir_production_alias():
    """Test get_environment_data_dir handles production alias."""
    result = get_environment_data_dir("production")
    
    assert isinstance(result, Path)
    assert result.name == "local"  # production maps to local
    assert "data" in str(result)


def test_get_calendar_paths_for_environment_default():
    """Test get_calendar_paths_for_environment returns paths for default environment."""
    with patch.dict(os.environ, {}, clear=True):
        holidays_file, schedules_dir = get_calendar_paths_for_environment(None)
        
        assert isinstance(holidays_file, Path)
        assert isinstance(schedules_dir, Path)
        assert holidays_file.name == "holidays.json"
        assert schedules_dir.name == "schedules"
        assert "calendar" in str(holidays_file)
        assert "calendar" in str(schedules_dir)


def test_get_calendar_paths_for_environment_specific():
    """Test get_calendar_paths_for_environment returns paths for specific environment."""
    holidays_file, schedules_dir = get_calendar_paths_for_environment("unit_test")
        
    assert isinstance(holidays_file, Path)
    assert isinstance(schedules_dir, Path)
    assert holidays_file.name == "holidays.json"
    assert schedules_dir.name == "schedules"
    assert "unit_test" in str(holidays_file)
    assert "unit_test" in str(schedules_dir)


def test_get_calendar_paths_for_environment_production_alias():
    """Test get_calendar_paths_for_environment handles production alias."""
    holidays_file, schedules_dir = get_calendar_paths_for_environment("production")
        
    assert isinstance(holidays_file, Path)
    assert isinstance(schedules_dir, Path)
    assert "local" in str(holidays_file)  # production maps to local
    assert "local" in str(schedules_dir)
