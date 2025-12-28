"""
Unit tests for corpse lifecycle service.

Tests the CorpseLifecycleService class.
"""

from unittest.mock import MagicMock

import pytest

from server.services.corpse_lifecycle_service import (
    CorpseLifecycleService,
    CorpseNotFoundError,
    CorpseServiceError,
    _get_enum_value,
)


def test_get_enum_value_enum():
    """Test _get_enum_value() with enum instance."""
    from enum import Enum

    class TestEnum(Enum):
        VALUE1 = "value1"

    result = _get_enum_value(TestEnum.VALUE1)
    assert result == "value1"


def test_get_enum_value_string():
    """Test _get_enum_value() with string."""
    result = _get_enum_value("test_string")
    assert result == "test_string"


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def corpse_service(mock_persistence):
    """Create a CorpseLifecycleService instance."""
    return CorpseLifecycleService(persistence=mock_persistence)


def test_corpse_lifecycle_service_init(corpse_service, mock_persistence):
    """Test CorpseLifecycleService initialization."""
    assert corpse_service.persistence == mock_persistence


def test_corpse_lifecycle_service_init_no_persistence():
    """Test CorpseLifecycleService initialization fails without persistence."""
    with pytest.raises(ValueError, match="persistence.*required"):
        CorpseLifecycleService(persistence=None)


def test_corpse_service_error():
    """Test CorpseServiceError exception."""
    error = CorpseServiceError("Test error")
    assert str(error) == "Test error"


def test_corpse_not_found_error():
    """Test CorpseNotFoundError exception."""
    error = CorpseNotFoundError("Corpse not found")
    assert isinstance(error, CorpseServiceError)
    assert str(error) == "Corpse not found"
