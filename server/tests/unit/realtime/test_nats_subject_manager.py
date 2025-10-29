"""
Unit tests for NATS Subject Manager.

This module tests the NATSSubjectManager class which provides centralized
subject naming conventions for NATS messaging in MythosMUD.

AI: These tests follow TDD approach - written before implementation.
AI: Tests verify pattern building, validation, registration, and error handling.
"""

import pytest

from server.services.nats_subject_manager import (
    InvalidPatternError,
    MissingParameterError,
    NATSSubjectManager,
    PatternNotFoundError,
    SubjectValidationError,
)


class TestNATSSubjectManagerInit:
    """Test NATSSubjectManager initialization and pattern registry."""

    def test_manager_initializes_with_default_patterns(self):
        """Test that manager initializes with all predefined patterns."""
        manager = NATSSubjectManager()

        # Verify all 7 predefined patterns are registered
        assert "chat_say_room" in manager.patterns
        assert "chat_local_subzone" in manager.patterns
        assert "chat_global" in manager.patterns
        assert "chat_whisper_player" in manager.patterns
        assert "chat_system" in manager.patterns
        assert "chat_emote_room" in manager.patterns
        assert "chat_pose_room" in manager.patterns

    def test_manager_initializes_with_empty_cache(self):
        """Test that manager initializes with empty validation cache."""
        manager = NATSSubjectManager()

        # Cache should exist but be empty
        assert hasattr(manager, "_validation_cache")
        assert len(manager._validation_cache) == 0

    def test_manager_singleton_pattern(self):
        """Test that manager can be used as singleton if needed."""
        manager1 = NATSSubjectManager()
        manager2 = NATSSubjectManager()

        # Should be separate instances (not enforcing singleton at class level)
        # This allows for testing flexibility
        assert manager1 is not manager2


class TestBuildSubject:
    """Test subject building with pattern parameters."""

    def test_build_subject_with_room_pattern(self):
        """Test building subject for room-level say messages."""
        manager = NATSSubjectManager()

        subject = manager.build_subject("chat_say_room", room_id="arkham_1")

        assert subject == "chat.say.room.arkham_1"

    def test_build_subject_with_subzone_pattern(self):
        """Test building subject for subzone-level local messages."""
        manager = NATSSubjectManager()

        subject = manager.build_subject("chat_local_subzone", subzone="miskatonic_university")

        assert subject == "chat.local.subzone.miskatonic_university"

    def test_build_subject_with_global_pattern(self):
        """Test building subject for global messages (no parameters)."""
        manager = NATSSubjectManager()

        subject = manager.build_subject("chat_global")

        assert subject == "chat.global"

    def test_build_subject_with_whisper_pattern(self):
        """Test building subject for player whisper messages."""
        manager = NATSSubjectManager()

        subject = manager.build_subject("chat_whisper_player", target_id="player_123")

        assert subject == "chat.whisper.player.player_123"

    def test_build_subject_with_system_pattern(self):
        """Test building subject for system messages."""
        manager = NATSSubjectManager()

        subject = manager.build_subject("chat_system")

        assert subject == "chat.system"

    def test_build_subject_with_emote_pattern(self):
        """Test building subject for room-level emote messages."""
        manager = NATSSubjectManager()

        subject = manager.build_subject("chat_emote_room", room_id="innsmouth_1")

        assert subject == "chat.emote.room.innsmouth_1"

    def test_build_subject_with_pose_pattern(self):
        """Test building subject for room-level pose messages."""
        manager = NATSSubjectManager()

        subject = manager.build_subject("chat_pose_room", room_id="dunwich_1")

        assert subject == "chat.pose.room.dunwich_1"

    def test_build_subject_with_missing_required_parameter(self):
        """Test that missing required parameter raises MissingParameterError."""
        manager = NATSSubjectManager()

        with pytest.raises(MissingParameterError) as exc_info:
            manager.build_subject("chat_say_room")  # Missing room_id

        assert "room_id" in str(exc_info.value)
        assert "chat_say_room" in str(exc_info.value)

    def test_build_subject_with_unknown_pattern(self):
        """Test that unknown pattern name raises PatternNotFoundError."""
        manager = NATSSubjectManager()

        with pytest.raises(PatternNotFoundError) as exc_info:
            manager.build_subject("chat_unknown_pattern")

        assert "chat_unknown_pattern" in str(exc_info.value)

    def test_build_subject_with_extra_parameters(self):
        """Test that extra parameters are ignored gracefully."""
        manager = NATSSubjectManager()

        subject = manager.build_subject("chat_global", extra_param="ignored", another="also_ignored")

        # Should succeed and ignore extra parameters
        assert subject == "chat.global"

    def test_build_subject_with_special_characters_in_parameters(self):
        """Test parameter validation rejects special characters."""
        manager = NATSSubjectManager()

        with pytest.raises(SubjectValidationError) as exc_info:
            manager.build_subject("chat_say_room", room_id="room@invalid")

        assert "invalid characters" in str(exc_info.value).lower()

    def test_build_subject_with_empty_parameter_value(self):
        """Test that empty parameter values raise SubjectValidationError."""
        manager = NATSSubjectManager()

        with pytest.raises(SubjectValidationError) as exc_info:
            manager.build_subject("chat_say_room", room_id="")

        assert "empty" in str(exc_info.value).lower()


class TestValidateSubject:
    """Test subject validation against registered patterns."""

    def test_validate_subject_with_valid_room_subject(self):
        """Test validation of valid room-level subject."""
        manager = NATSSubjectManager()

        is_valid = manager.validate_subject("chat.say.room.arkham_1")

        assert is_valid is True

    def test_validate_subject_with_valid_subzone_subject(self):
        """Test validation of valid subzone-level subject."""
        manager = NATSSubjectManager()

        is_valid = manager.validate_subject("chat.local.subzone.miskatonic_university")

        assert is_valid is True

    def test_validate_subject_with_valid_global_subject(self):
        """Test validation of valid global subject."""
        manager = NATSSubjectManager()

        is_valid = manager.validate_subject("chat.global")

        assert is_valid is True

    def test_validate_subject_with_valid_whisper_subject(self):
        """Test validation of valid whisper subject."""
        manager = NATSSubjectManager()

        is_valid = manager.validate_subject("chat.whisper.player.player_123")

        assert is_valid is True

    def test_validate_subject_with_invalid_pattern(self):
        """Test validation rejects invalid subject patterns."""
        manager = NATSSubjectManager()

        is_valid = manager.validate_subject("invalid.pattern.format")

        assert is_valid is False

    def test_validate_subject_with_malformed_structure(self):
        """Test validation rejects malformed subject structure."""
        manager = NATSSubjectManager()

        is_valid = manager.validate_subject("chat..room.arkham")

        assert is_valid is False

    def test_validate_subject_with_empty_string(self):
        """Test validation rejects empty subject string."""
        manager = NATSSubjectManager()

        is_valid = manager.validate_subject("")

        assert is_valid is False

    def test_validate_subject_with_too_long_subject(self):
        """Test validation rejects subjects exceeding maximum length."""
        manager = NATSSubjectManager()

        # Create subject exceeding 255 characters
        long_subject = "chat.say.room." + "x" * 300

        is_valid = manager.validate_subject(long_subject)

        assert is_valid is False

    def test_validate_subject_caches_results(self):
        """Test that validation results are cached for performance."""
        manager = NATSSubjectManager()

        subject = "chat.say.room.arkham_1"

        # First validation
        result1 = manager.validate_subject(subject)
        cache_size_after_first = len(manager._validation_cache)

        # Second validation (should use cache)
        result2 = manager.validate_subject(subject)
        cache_size_after_second = len(manager._validation_cache)

        assert result1 is True
        assert result2 is True
        assert cache_size_after_first == cache_size_after_second == 1


class TestRegisterPattern:
    """Test dynamic pattern registration."""

    def test_register_new_pattern(self):
        """Test registering a new subject pattern."""
        manager = NATSSubjectManager()

        manager.register_pattern(
            name="chat_party_group",
            pattern="chat.party.group.{party_id}",
            required_params=["party_id"],
            description="Party group messages",
        )

        assert "chat_party_group" in manager.patterns
        subject = manager.build_subject("chat_party_group", party_id="party_123")
        assert subject == "chat.party.group.party_123"

    def test_register_pattern_with_duplicate_name(self):
        """Test that registering duplicate pattern name raises InvalidPatternError."""
        manager = NATSSubjectManager()

        with pytest.raises(InvalidPatternError) as exc_info:
            manager.register_pattern(
                name="chat_global",  # Already exists
                pattern="chat.global.duplicate",
                required_params=[],
            )

        assert "already registered" in str(exc_info.value).lower()

    def test_register_pattern_with_invalid_format(self):
        """Test that invalid pattern format raises InvalidPatternError."""
        manager = NATSSubjectManager()

        with pytest.raises(InvalidPatternError) as exc_info:
            manager.register_pattern(
                name="chat_invalid",
                pattern="invalid..pattern",  # Double dots are invalid
                required_params=[],
            )

        assert "invalid pattern format" in str(exc_info.value).lower()

    def test_register_pattern_with_missing_placeholder(self):
        """Test pattern with required params must have placeholders."""
        manager = NATSSubjectManager()

        with pytest.raises(InvalidPatternError) as exc_info:
            manager.register_pattern(
                name="chat_test",
                pattern="chat.test.static",  # No placeholder
                required_params=["missing_param"],  # But requires param
            )

        assert "placeholder" in str(exc_info.value).lower()


class TestGetPatternInfo:
    """Test pattern information retrieval."""

    def test_get_pattern_info_for_existing_pattern(self):
        """Test retrieving information for existing pattern."""
        manager = NATSSubjectManager()

        info = manager.get_pattern_info("chat_say_room")

        assert info["name"] == "chat_say_room"
        assert info["pattern"] == "chat.say.room.{room_id}"
        assert info["required_params"] == ["room_id"]
        assert info["description"] == "Room-level say messages"

    def test_get_pattern_info_for_nonexistent_pattern(self):
        """Test that nonexistent pattern raises PatternNotFoundError."""
        manager = NATSSubjectManager()

        with pytest.raises(PatternNotFoundError) as exc_info:
            manager.get_pattern_info("chat_nonexistent")

        assert "chat_nonexistent" in str(exc_info.value)

    def test_get_all_patterns(self):
        """Test retrieving all registered patterns."""
        manager = NATSSubjectManager()

        all_patterns = manager.get_all_patterns()

        assert len(all_patterns) >= 7  # At least the predefined patterns
        assert "chat_say_room" in all_patterns
        assert "chat_global" in all_patterns


class TestErrorHandling:
    """Test comprehensive error handling."""

    def test_custom_exception_hierarchy(self):
        """Test that custom exceptions have proper inheritance."""
        # All custom exceptions should inherit from a base exception
        assert issubclass(PatternNotFoundError, Exception)
        assert issubclass(MissingParameterError, Exception)
        assert issubclass(InvalidPatternError, Exception)
        assert issubclass(SubjectValidationError, Exception)

    def test_error_messages_are_descriptive(self):
        """Test that error messages provide useful debugging information."""
        manager = NATSSubjectManager()

        try:
            manager.build_subject("chat_say_room")  # Missing room_id
        except MissingParameterError as e:
            error_msg = str(e)
            assert "room_id" in error_msg
            assert "chat_say_room" in error_msg
            assert "required" in error_msg.lower()


class TestPerformanceOptimization:
    """Test performance optimization features."""

    def test_pattern_caching_enabled_by_default(self):
        """Test that pattern caching is enabled by default."""
        manager = NATSSubjectManager()

        assert hasattr(manager, "_validation_cache")
        assert manager._cache_enabled is True

    def test_cache_can_be_disabled(self):
        """Test that caching can be disabled for testing."""
        manager = NATSSubjectManager(enable_cache=False)

        assert manager._cache_enabled is False

    def test_cache_can_be_cleared(self):
        """Test that validation cache can be cleared."""
        manager = NATSSubjectManager()

        # Add some cached entries
        manager.validate_subject("chat.global")
        manager.validate_subject("chat.say.room.arkham_1")

        assert len(manager._validation_cache) > 0

        # Clear cache
        manager.clear_cache()

        assert len(manager._validation_cache) == 0

    def test_build_subject_performance(self):
        """Test that subject building is performant."""
        import time

        manager = NATSSubjectManager()

        start_time = time.time()
        for i in range(1000):
            manager.build_subject("chat_say_room", room_id=f"room_{i}")
        elapsed_time = time.time() - start_time

        # Should complete 1000 operations in under 100ms
        assert elapsed_time < 0.1


class TestPatternConfiguration:
    """Test pattern configuration and management."""

    def test_max_subject_length_configuration(self):
        """Test that maximum subject length can be configured."""
        manager = NATSSubjectManager(max_subject_length=100)

        # Subject within limit should succeed
        subject = manager.build_subject("chat_say_room", room_id="short")
        assert subject == "chat.say.room.short"

        # Subject exceeding limit should fail validation
        long_room_id = "x" * 150
        with pytest.raises(SubjectValidationError):
            manager.build_subject("chat_say_room", room_id=long_room_id)

    def test_strict_validation_mode(self):
        """Test strict validation mode enforces additional rules."""
        manager = NATSSubjectManager(strict_validation=True)

        # Strict mode should reject underscores in identifiers
        with pytest.raises(SubjectValidationError):
            manager.build_subject("chat_say_room", room_id="room_with_underscore")

    def test_lenient_validation_mode(self):
        """Test lenient validation mode allows more flexibility."""
        manager = NATSSubjectManager(strict_validation=False)

        # Lenient mode should allow underscores
        subject = manager.build_subject("chat_say_room", room_id="room_with_underscore")
        assert subject == "chat.say.room.room_with_underscore"


class TestSubscriptionPatterns:
    """Test subscription pattern generation for message handlers."""

    def test_get_subscription_pattern_with_room_pattern(self):
        """Test generating subscription pattern for room-level messages."""
        manager = NATSSubjectManager()

        pattern = manager.get_subscription_pattern("chat_say_room")

        assert pattern == "chat.say.room.*"

    def test_get_subscription_pattern_with_subzone_pattern(self):
        """Test generating subscription pattern for subzone-level messages."""
        manager = NATSSubjectManager()

        pattern = manager.get_subscription_pattern("chat_local_subzone")

        assert pattern == "chat.local.subzone.*"

    def test_get_subscription_pattern_with_no_params(self):
        """Test generating subscription pattern for patterns with no parameters."""
        manager = NATSSubjectManager()

        pattern = manager.get_subscription_pattern("chat_global")

        # Pattern without parameters should remain unchanged
        assert pattern == "chat.global"

    def test_get_subscription_pattern_with_nonexistent_pattern(self):
        """Test that nonexistent pattern raises PatternNotFoundError."""
        manager = NATSSubjectManager()

        with pytest.raises(PatternNotFoundError) as exc_info:
            manager.get_subscription_pattern("chat_nonexistent")

        assert "chat_nonexistent" in str(exc_info.value)

    def test_get_chat_subscription_patterns(self):
        """Test getting all chat subscription patterns."""
        manager = NATSSubjectManager()

        patterns = manager.get_chat_subscription_patterns()

        # Should include all predefined chat patterns
        assert "chat.say.room.*" in patterns
        assert "chat.local.subzone.*" in patterns
        assert "chat.global" in patterns
        assert "chat.whisper.player.*" in patterns
        assert "chat.system" in patterns
        assert "chat.emote.room.*" in patterns
        assert "chat.pose.room.*" in patterns

        # Should have 7 chat patterns
        assert len(patterns) == 7

    def test_get_event_subscription_patterns(self):
        """Test getting all event subscription patterns."""
        manager = NATSSubjectManager()

        patterns = manager.get_event_subscription_patterns()

        # Should include all predefined event patterns
        assert "events.player_entered.*" in patterns
        assert "events.player_left.*" in patterns
        assert "events.game_tick" in patterns
        assert "events.player_mortally_wounded.*" in patterns
        assert "events.player_hp_decay.*" in patterns
        assert "events.player_died.*" in patterns
        assert "events.player_respawned.*" in patterns

        # Should include all combat patterns
        assert "combat.attack.*" in patterns
        assert "combat.npc_attacked.*" in patterns
        assert "combat.npc_action.*" in patterns
        assert "combat.started.*" in patterns
        assert "combat.ended.*" in patterns
        assert "combat.npc_died.*" in patterns
        assert "combat.damage.*" in patterns
        assert "combat.turn.*" in patterns
        assert "combat.timeout.*" in patterns

        # Should have 16 event/combat patterns (7 event + 9 combat)
        assert len(patterns) == 16

    def test_subscription_patterns_are_valid(self):
        """Test that generated subscription patterns are valid NATS subjects."""
        manager = NATSSubjectManager()

        chat_patterns = manager.get_chat_subscription_patterns()
        event_patterns = manager.get_event_subscription_patterns()

        # All patterns should be non-empty strings
        for pattern in chat_patterns + event_patterns:
            assert isinstance(pattern, str)
            assert len(pattern) > 0
            # Should not contain double dots or invalid characters
            assert ".." not in pattern
            assert not pattern.startswith(".")
            assert not pattern.endswith(".")

    def test_subscription_patterns_use_wildcards(self):
        """Test that subscription patterns use wildcards for parameters."""
        manager = NATSSubjectManager()

        # Patterns with parameters should use wildcards
        assert "*" in manager.get_subscription_pattern("chat_say_room")
        assert "*" in manager.get_subscription_pattern("chat_local_subzone")

        # Patterns without parameters should not have wildcards
        assert "*" not in manager.get_subscription_pattern("chat_global")
        assert "*" not in manager.get_subscription_pattern("chat_system")


class TestPerformanceMetrics:
    """Test performance metrics collection for subject manager operations."""

    def test_metrics_enabled_by_default(self):
        """Test that metrics collection is enabled by default."""
        manager = NATSSubjectManager()

        assert manager.metrics is not None
        assert manager._metrics_enabled is True

    def test_metrics_can_be_disabled(self):
        """Test that metrics collection can be disabled."""
        manager = NATSSubjectManager(enable_metrics=False)

        assert manager.metrics is None
        assert manager._metrics_enabled is False

    def test_build_metrics_recorded(self):
        """Test that build operations record metrics."""
        manager = NATSSubjectManager()

        # Perform some build operations
        manager.build_subject("chat_say_room", room_id="room_1")
        manager.build_subject("chat_global")
        manager.build_subject("chat_local_subzone", subzone="test_zone")

        # Get metrics
        metrics = manager.get_performance_metrics()

        assert metrics is not None
        assert metrics["build"]["total_count"] == 3
        assert metrics["build"]["success_count"] == 3
        assert metrics["build"]["failure_count"] == 0
        assert metrics["build"]["success_rate"] == 1.0
        assert metrics["build"]["avg_time_ms"] >= 0

    def test_build_error_metrics_recorded(self):
        """Test that build errors are recorded in metrics."""
        manager = NATSSubjectManager()

        # Attempt build with missing parameters
        try:
            manager.build_subject("chat_say_room")  # Missing room_id
        except Exception:
            pass

        # Attempt build with nonexistent pattern
        try:
            manager.build_subject("nonexistent_pattern")
        except Exception:
            pass

        # Get metrics
        metrics = manager.get_performance_metrics()

        assert metrics is not None
        assert metrics["build"]["total_count"] == 2
        assert metrics["build"]["failure_count"] == 2
        assert metrics["errors"]["missing_parameter"] == 1
        assert metrics["errors"]["pattern_not_found"] == 1

    def test_validation_metrics_recorded(self):
        """Test that validation operations record metrics."""
        manager = NATSSubjectManager()

        # Perform some validation operations
        manager.validate_subject("chat.say.room.room_1")
        manager.validate_subject("chat.global")
        manager.validate_subject("invalid..subject")

        # Get metrics
        metrics = manager.get_performance_metrics()

        assert metrics is not None
        assert metrics["validation"]["total_count"] == 3
        assert metrics["validation"]["success_count"] == 2
        assert metrics["validation"]["failure_count"] == 1
        assert metrics["validation"]["avg_time_ms"] >= 0

    def test_cache_metrics_recorded(self):
        """Test that cache hits and misses are recorded."""
        manager = NATSSubjectManager()

        subject = "chat.say.room.room_1"

        # First validation - cache miss
        manager.validate_subject(subject)

        # Second validation - cache hit
        manager.validate_subject(subject)

        # Third validation - same subject, cache hit
        manager.validate_subject(subject)

        # Get metrics
        metrics = manager.get_performance_metrics()

        assert metrics is not None
        assert metrics["cache"]["hits"] == 2
        assert metrics["cache"]["misses"] == 1
        assert metrics["cache"]["hit_rate"] == 2 / 3

    def test_metrics_percentile_calculation(self):
        """Test that p95 percentile is calculated correctly."""
        manager = NATSSubjectManager()

        # Perform multiple operations to get timing data
        for i in range(10):
            manager.build_subject("chat_say_room", room_id=f"room_{i}")

        metrics = manager.get_performance_metrics()

        assert metrics is not None
        assert metrics["build"]["p95_time_ms"] >= 0
        # P95 should be greater than or equal to average
        assert metrics["build"]["p95_time_ms"] >= metrics["build"]["avg_time_ms"]

    def test_metrics_return_none_when_disabled(self):
        """Test that get_performance_metrics returns None when disabled."""
        manager = NATSSubjectManager(enable_metrics=False)

        metrics = manager.get_performance_metrics()

        assert metrics is None

    def test_metrics_rolling_window(self):
        """Test that metrics maintain a rolling window of times."""
        manager = NATSSubjectManager()

        # Metrics should only keep last 1000 times
        for i in range(1500):
            manager.build_subject("chat_say_room", room_id=f"room_{i}")

        # Check that we don't have more than 1000 times stored
        assert len(manager.metrics.build_times) <= 1000

    def test_metrics_success_rate_calculation(self):
        """Test that success rates are calculated correctly."""
        manager = NATSSubjectManager()

        # Perform 7 successful and 3 failed operations
        for i in range(7):
            manager.build_subject("chat_say_room", room_id=f"room_{i}")

        for _ in range(3):
            try:
                manager.build_subject("chat_say_room")  # Missing parameter
            except Exception:
                pass

        metrics = manager.get_performance_metrics()

        assert metrics is not None
        assert metrics["build"]["total_count"] == 10
        assert metrics["build"]["success_count"] == 7
        assert metrics["build"]["failure_count"] == 3
        assert metrics["build"]["success_rate"] == 0.7

    def test_metrics_comprehensive_summary(self):
        """Test that metrics provide comprehensive summary."""
        manager = NATSSubjectManager()

        # Mix of operations
        manager.build_subject("chat_say_room", room_id="room_1")
        manager.validate_subject("chat.say.room.room_1")
        manager.validate_subject("chat.say.room.room_1")  # Cache hit

        try:
            manager.build_subject("nonexistent")
        except Exception:
            pass

        metrics = manager.get_performance_metrics()

        # Verify all metric categories are present
        assert "validation" in metrics
        assert "cache" in metrics
        assert "build" in metrics
        assert "errors" in metrics

        # Verify all fields are present
        assert "total_count" in metrics["validation"]
        assert "success_count" in metrics["validation"]
        assert "failure_count" in metrics["validation"]
        assert "success_rate" in metrics["validation"]
        assert "avg_time_ms" in metrics["validation"]
        assert "p95_time_ms" in metrics["validation"]

        assert "hits" in metrics["cache"]
        assert "misses" in metrics["cache"]
        assert "hit_rate" in metrics["cache"]

        assert "total_count" in metrics["build"]
        assert "success_count" in metrics["build"]
        assert "failure_count" in metrics["build"]
        assert "success_rate" in metrics["build"]
        assert "avg_time_ms" in metrics["build"]
        assert "p95_time_ms" in metrics["build"]

        assert "pattern_not_found" in metrics["errors"]
        assert "missing_parameter" in metrics["errors"]
        assert "validation_errors" in metrics["errors"]
        assert "total_errors" in metrics["errors"]
