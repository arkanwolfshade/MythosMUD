"""
Unit tests for NATS Subject Manager.

Tests the NATSSubjectManager class.
"""

from unittest.mock import patch

import pytest

from server.services.nats_subject_manager.exceptions import (
    InvalidPatternError,
    MissingParameterError,
    PatternNotFoundError,
    SubjectValidationError,
)
from server.services.nats_subject_manager.manager import NATSSubjectManager


@pytest.fixture
def subject_manager():
    """Create NATSSubjectManager instance."""
    return NATSSubjectManager()


@pytest.fixture
def subject_manager_no_metrics():
    """Create NATSSubjectManager without metrics."""
    return NATSSubjectManager(enable_metrics=False)


@pytest.fixture
def subject_manager_no_cache():
    """Create NATSSubjectManager without cache."""
    return NATSSubjectManager(enable_cache=False)


def test_nats_subject_manager_init():
    """Test NATSSubjectManager initialization."""
    manager = NATSSubjectManager()
    assert manager.patterns is not None
    assert len(manager.patterns) > 0
    assert manager._cache_enabled is True
    assert manager._max_subject_length == 255
    assert manager._strict_validation is False
    assert manager.metrics is not None


def test_nats_subject_manager_init_no_metrics():
    """Test NATSSubjectManager initialization without metrics."""
    manager = NATSSubjectManager(enable_metrics=False)
    assert manager.metrics is None


def test_nats_subject_manager_init_no_cache():
    """Test NATSSubjectManager initialization without cache."""
    manager = NATSSubjectManager(enable_cache=False)
    assert manager._cache_enabled is False


def test_nats_subject_manager_init_strict_validation():
    """Test NATSSubjectManager initialization with strict validation."""
    manager = NATSSubjectManager(strict_validation=True)
    assert manager._strict_validation is True


def test_nats_subject_manager_init_custom_max_length():
    """Test NATSSubjectManager initialization with custom max length."""
    manager = NATSSubjectManager(max_subject_length=100)
    assert manager._max_subject_length == 100


def test_build_subject_success(subject_manager):
    """Test build_subject() successfully builds subject."""
    subject = subject_manager.build_subject("chat_say_room", room_id="arkham_1")
    assert subject == "chat.say.room.arkham_1"


def test_build_subject_no_params(subject_manager):
    """Test build_subject() with pattern requiring no parameters."""
    subject = subject_manager.build_subject("chat_global")
    assert subject == "chat.global"


def test_build_subject_multiple_params(subject_manager):
    """Test build_subject() with multiple parameters."""
    subject = subject_manager.build_subject("chat_whisper_player", target_id="player_123")
    assert subject == "chat.whisper.player.player_123"


def test_build_subject_pattern_not_found(subject_manager):
    """Test build_subject() raises PatternNotFoundError when pattern not found."""
    with pytest.raises(PatternNotFoundError, match="nonexistent_pattern"):
        subject_manager.build_subject("nonexistent_pattern", room_id="arkham_1")


def test_build_subject_missing_parameter(subject_manager):
    """Test build_subject() raises MissingParameterError when parameter missing."""
    with pytest.raises(MissingParameterError):
        subject_manager.build_subject("chat_say_room")  # Missing room_id


def test_build_subject_invalid_parameter_value(subject_manager):
    """Test build_subject() raises SubjectValidationError for invalid parameter."""
    with pytest.raises(SubjectValidationError):
        subject_manager.build_subject("chat_say_room", room_id="")  # Empty room_id


def test_build_subject_subject_too_long(subject_manager):
    """Test build_subject() raises SubjectValidationError when subject too long."""
    manager = NATSSubjectManager(max_subject_length=10)
    with pytest.raises(SubjectValidationError, match="exceeds maximum length"):
        manager.build_subject("chat_say_room", room_id="a" * 100)


def test_validate_subject_valid(subject_manager):
    """Test validate_subject() returns True for valid subject."""
    result = subject_manager.validate_subject("chat.say.room.arkham_1")
    assert result is True


def test_validate_subject_invalid(subject_manager):
    """Test validate_subject() returns False for invalid subject."""
    result = subject_manager.validate_subject("invalid.subject.format")
    assert result is False


def test_validate_subject_empty(subject_manager):
    """Test validate_subject() returns False for empty subject."""
    result = subject_manager.validate_subject("")
    assert result is False


def test_validate_subject_uses_cache(subject_manager):
    """Test validate_subject() uses cache for repeated validations."""
    subject = "chat.say.room.arkham_1"
    # First call
    result1 = subject_manager.validate_subject(subject)
    # Second call should use cache
    result2 = subject_manager.validate_subject(subject)
    assert result1 == result2
    assert subject in subject_manager._validation_cache


def test_validate_subject_no_cache(subject_manager_no_cache):
    """Test validate_subject() doesn't use cache when disabled."""
    subject = "chat.say.room.arkham_1"
    subject_manager_no_cache.validate_subject(subject)
    assert subject not in subject_manager_no_cache._validation_cache


def test_register_pattern_success(subject_manager):
    """Test register_pattern() successfully registers pattern."""
    subject_manager.register_pattern(
        name="test_pattern",
        pattern="test.{param1}.{param2}",
        required_params=["param1", "param2"],
        description="Test pattern",
    )
    assert "test_pattern" in subject_manager.patterns
    assert subject_manager.patterns["test_pattern"]["pattern"] == "test.{param1}.{param2}"


def test_register_pattern_duplicate_name(subject_manager):
    """Test register_pattern() raises InvalidPatternError for duplicate name."""
    with pytest.raises(InvalidPatternError, match="already registered"):
        subject_manager.register_pattern(
            name="chat_say_room",  # Already exists
            pattern="test.pattern",
            required_params=[],
        )


def test_register_pattern_invalid_format(subject_manager):
    """Test register_pattern() raises InvalidPatternError for invalid format."""
    with pytest.raises(InvalidPatternError, match="Invalid pattern format"):
        subject_manager.register_pattern(
            name="test_pattern",
            pattern="test..pattern",  # Double dots
            required_params=[],
        )


def test_register_pattern_missing_placeholder(subject_manager):
    """Test register_pattern() raises InvalidPatternError when placeholder missing."""
    with pytest.raises(InvalidPatternError, match="missing placeholder"):
        subject_manager.register_pattern(
            name="test_pattern",
            pattern="test.pattern",  # Missing {param1}
            required_params=["param1"],
        )


def test_register_pattern_clears_cache(subject_manager):
    """Test register_pattern() clears validation cache."""
    subject = "chat.say.room.arkham_1"
    subject_manager.validate_subject(subject)  # Populate cache
    assert subject in subject_manager._validation_cache

    subject_manager.register_pattern(
        name="test_pattern",
        pattern="test.pattern",
        required_params=[],
    )
    assert len(subject_manager._validation_cache) == 0


def test_get_pattern_info_success(subject_manager):
    """Test get_pattern_info() returns pattern information."""
    info = subject_manager.get_pattern_info("chat_say_room")
    assert "pattern" in info
    assert "required_params" in info
    assert "description" in info
    assert info["pattern"] == "chat.say.room.{room_id}"


def test_get_pattern_info_not_found(subject_manager):
    """Test get_pattern_info() raises PatternNotFoundError when pattern not found."""
    with pytest.raises(PatternNotFoundError):
        subject_manager.get_pattern_info("nonexistent_pattern")


def test_get_all_patterns(subject_manager):
    """Test get_all_patterns() returns all registered patterns."""
    patterns = subject_manager.get_all_patterns()
    assert isinstance(patterns, dict)
    assert len(patterns) > 0
    assert "chat_say_room" in patterns


def test_get_subscription_pattern_success(subject_manager):
    """Test get_subscription_pattern() returns subscription pattern."""
    pattern = subject_manager.get_subscription_pattern("chat_say_room")
    assert pattern == "chat.say.room.*"


def test_get_subscription_pattern_not_found(subject_manager):
    """Test get_subscription_pattern() raises PatternNotFoundError when pattern not found."""
    with pytest.raises(PatternNotFoundError):
        subject_manager.get_subscription_pattern("nonexistent_pattern")


def test_get_chat_subscription_patterns(subject_manager):
    """Test get_chat_subscription_patterns() returns chat patterns."""
    patterns = subject_manager.get_chat_subscription_patterns()
    assert isinstance(patterns, list)
    assert len(patterns) > 0
    assert "chat.say.room.*" in patterns or "chat.global" in patterns


def test_get_event_subscription_patterns(subject_manager):
    """Test get_event_subscription_patterns() returns event patterns."""
    patterns = subject_manager.get_event_subscription_patterns()
    assert isinstance(patterns, list)
    assert len(patterns) > 0


def test_clear_cache(subject_manager):
    """Test clear_cache() clears validation cache."""
    subject = "chat.say.room.arkham_1"
    subject_manager.validate_subject(subject)
    assert subject in subject_manager._validation_cache

    subject_manager.clear_cache()
    assert len(subject_manager._validation_cache) == 0


def test_get_performance_metrics_with_metrics(subject_manager):
    """Test get_performance_metrics() returns metrics when enabled."""
    metrics = subject_manager.get_performance_metrics()
    assert metrics is not None
    assert isinstance(metrics, dict)


def test_get_performance_metrics_without_metrics(subject_manager_no_metrics):
    """Test get_performance_metrics() returns None when disabled."""
    metrics = subject_manager_no_metrics.get_performance_metrics()
    assert metrics is None


def test_build_subject_records_metrics(subject_manager):
    """Test build_subject() records metrics when enabled."""
    with patch.object(subject_manager.metrics, "record_build") as mock_record:
        subject_manager.build_subject("chat_global")
        mock_record.assert_called_once()


def test_build_subject_records_error_metrics(subject_manager):
    """Test build_subject() records error metrics on failure."""
    with patch.object(subject_manager.metrics, "record_error") as mock_record:
        try:
            subject_manager.build_subject("nonexistent_pattern")
        except PatternNotFoundError:
            pass
        mock_record.assert_called_once_with("pattern_not_found")


def test_validate_subject_records_metrics(subject_manager):
    """Test validate_subject() records metrics when enabled."""
    with patch.object(subject_manager.metrics, "record_validation") as mock_record:
        subject_manager.validate_subject("chat.say.room.arkham_1")
        mock_record.assert_called_once()


def test_validate_subject_records_cache_hit(subject_manager):
    """Test validate_subject() records cache hit in metrics."""
    subject = "chat.say.room.arkham_1"
    subject_manager.validate_subject(subject)  # First call - cache miss

    with patch.object(subject_manager.metrics, "record_validation") as mock_record:
        subject_manager.validate_subject(subject)  # Second call - cache hit
        # Check that cache_hit=True was passed
        call_args = mock_record.call_args[0]
        assert call_args[2] is True  # cache_hit parameter
