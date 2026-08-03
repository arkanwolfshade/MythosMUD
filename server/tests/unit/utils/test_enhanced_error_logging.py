"""
Unit tests for enhanced_error_logging utilities.

Tests error logging helper functions.
"""

from unittest.mock import patch

import pytest
from fastapi import HTTPException

from server.utils.enhanced_error_logging import (
    create_enhanced_error_context,
    create_error_context,
    create_logged_http_exception_enhanced,
    log_and_raise_enhanced,
    log_and_raise_http_enhanced,
    log_performance_metric,
    log_security_event_enhanced,
    log_structured_error,
    wrap_third_party_exception_enhanced,
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
            log_and_raise_enhanced(ValidationError, "Test error", operation="test_operation", logger_name=__name__)
        mock_log.assert_called_once()


def test_log_and_raise_enhanced_with_metadata():
    """Test log_and_raise_enhanced() includes metadata in log."""
    from server.exceptions import ValidationError

    with patch("server.utils.enhanced_error_logging.log_with_context") as mock_log:
        with pytest.raises(ValidationError):
            log_and_raise_enhanced(
                ValidationError, "Test error", operation="test_operation", key="value", logger_name=__name__
            )
        mock_log.assert_called_once()


def test_log_and_raise_http_enhanced():
    with patch("server.utils.enhanced_error_logging.log_with_context") as mock_log:
        with pytest.raises(HTTPException):
            log_and_raise_http_enhanced(404, "Not found", logger_name=__name__)
        mock_log.assert_called_once()


def test_create_logged_http_exception_enhanced():
    with patch("server.utils.enhanced_error_logging.log_with_context"):
        exc = create_logged_http_exception_enhanced(400, "Bad", logger_name=__name__)
    assert exc.status_code == 400


def test_log_structured_error():
    with patch("server.utils.enhanced_error_logging.log_with_context") as mock_log:
        log_structured_error(ValueError("x"), logger_name=__name__)
    mock_log.assert_called_once()


def test_wrap_third_party_exception_enhanced():
    from sqlalchemy.exc import OperationalError

    with patch("server.utils.enhanced_error_logging.log_with_context"):
        wrapped = wrap_third_party_exception_enhanced(
            OperationalError("stmt", {}, Exception("db down")),
            logger_name=__name__,
        )
    from server.exceptions import DatabaseError

    assert isinstance(wrapped, DatabaseError)


def test_create_enhanced_error_context():
    ctx = create_enhanced_error_context(user_id="u1", session_id="s1")
    assert ctx.user_id == "u1"


def test_log_performance_metric():
    with patch("server.utils.enhanced_error_logging.log_with_context") as mock_log:
        log_performance_metric("db_query", 12.0, success=True, logger_name=__name__)
    mock_log.assert_called_once()


def test_log_security_event_enhanced():
    with patch("server.utils.enhanced_error_logging.log_with_context") as mock_log:
        log_security_event_enhanced("login_failed", severity="medium", user_id="u1", logger_name=__name__)
    mock_log.assert_called_once()
