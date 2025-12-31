"""
Unit tests for enhanced_error_logging utilities.

Tests error logging helper functions.
"""

from unittest.mock import patch

import pytest

from server.utils.enhanced_error_logging import (
    create_error_context,
    log_and_raise_enhanced,
)


def test_create_error_context():
    """Test create_error_context() creates error context."""
    context = create_error_context()
    assert context is not None
    assert hasattr(context, "to_dict")


def test_log_and_raise_enhanced():
    """Test log_and_raise_enhanced() logs and raises exception."""
    from server.exceptions import ValidationError

    with patch("server.utils.enhanced_error_logging.log_with_context") as mock_log:
        with pytest.raises(ValidationError):
            log_and_raise_enhanced(ValidationError, "Test error", context=create_error_context(), logger_name=__name__)
        mock_log.assert_called_once()


def test_log_and_raise_enhanced_with_metadata():
    """Test log_and_raise_enhanced() includes metadata in log."""
    from server.exceptions import ValidationError

    with patch("server.utils.enhanced_error_logging.log_with_context") as mock_log:
        context = create_error_context()
        context.metadata = {"key": "value"}
        with pytest.raises(ValidationError):
            log_and_raise_enhanced(ValidationError, "Test error", context=context, logger_name=__name__)
        mock_log.assert_called_once()
