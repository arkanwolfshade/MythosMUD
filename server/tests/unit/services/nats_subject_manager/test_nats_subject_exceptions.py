"""
Unit tests for NATS Subject Manager Exceptions.

Tests the exception classes.
"""

import pytest

from server.services.nats_subject_manager.exceptions import (
    InvalidPatternError,
    MissingParameterError,
    NATSSubjectError,
    PatternNotFoundError,
    SubjectValidationError,
)


def test_nats_subject_error():
    """Test NATSSubjectError base exception."""
    error = NATSSubjectError("Test error")
    assert str(error) == "Test error"
    assert isinstance(error, Exception)


def test_pattern_not_found_error():
    """Test PatternNotFoundError exception."""
    error = PatternNotFoundError("test_pattern")
    assert "test_pattern" in str(error)
    assert error.pattern_name == "test_pattern"
    assert isinstance(error, NATSSubjectError)


def test_missing_parameter_error_single():
    """Test MissingParameterError with single parameter."""
    error = MissingParameterError("test_pattern", ["room_id"])
    assert "test_pattern" in str(error)
    assert "room_id" in str(error)
    assert error.pattern_name == "test_pattern"
    assert error.missing_params == ["room_id"]
    assert isinstance(error, NATSSubjectError)


def test_missing_parameter_error_multiple():
    """Test MissingParameterError with multiple parameters."""
    error = MissingParameterError("test_pattern", ["room_id", "subzone"])
    assert "test_pattern" in str(error)
    assert "room_id" in str(error)
    assert "subzone" in str(error)
    assert error.missing_params == ["room_id", "subzone"]


def test_invalid_pattern_error():
    """Test InvalidPatternError exception."""
    error = InvalidPatternError("Invalid pattern format")
    assert str(error) == "Invalid pattern format"
    assert isinstance(error, NATSSubjectError)


def test_subject_validation_error():
    """Test SubjectValidationError exception."""
    error = SubjectValidationError("Validation failed")
    assert str(error) == "Validation failed"
    assert isinstance(error, NATSSubjectError)


def test_exception_hierarchy():
    """Test exception inheritance hierarchy."""
    pattern_error = PatternNotFoundError("test")
    missing_error = MissingParameterError("test", ["param"])
    invalid_error = InvalidPatternError("test")
    validation_error = SubjectValidationError("test")

    assert isinstance(pattern_error, NATSSubjectError)
    assert isinstance(missing_error, NATSSubjectError)
    assert isinstance(invalid_error, NATSSubjectError)
    assert isinstance(validation_error, NATSSubjectError)

    assert isinstance(pattern_error, Exception)
    assert isinstance(missing_error, Exception)
    assert isinstance(invalid_error, Exception)
    assert isinstance(validation_error, Exception)


def test_exceptions_can_be_raised():
    """Test exceptions can be raised and caught."""
    with pytest.raises(PatternNotFoundError):
        raise PatternNotFoundError("test_pattern")

    with pytest.raises(MissingParameterError):
        raise MissingParameterError("test_pattern", ["room_id"])

    with pytest.raises(InvalidPatternError):
        raise InvalidPatternError("Invalid format")

    with pytest.raises(SubjectValidationError):
        raise SubjectValidationError("Validation failed")


def test_exceptions_can_be_caught_by_base():
    """Test exceptions can be caught by base class."""
    with pytest.raises(NATSSubjectError):
        raise PatternNotFoundError("test_pattern")

    with pytest.raises(NATSSubjectError):
        raise MissingParameterError("test_pattern", ["room_id"])
