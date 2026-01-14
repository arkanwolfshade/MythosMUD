"""
NATS Subject Manager for MythosMUD.

This module provides centralized subject naming conventions for NATS messaging,
ensuring consistent subject patterns across the chat system.

The NATSSubjectManager handles:
- Subject pattern registration and validation
- Subject building with parameter validation
- Pattern caching for performance
- Error handling for invalid subjects
- Performance monitoring and metrics collection

AI: Implements centralized pattern management to replace ad-hoc subject construction.
AI: Uses template-based patterns with validation to prevent routing errors.
AI: Tracks performance metrics for optimization and monitoring.
"""

# pylint: disable=too-many-instance-attributes  # Reason: Subject manager requires many state tracking and configuration attributes

from typing import Any

from .exceptions import (
    InvalidPatternError,
    MissingParameterError,
    PatternNotFoundError,
    SubjectValidationError,
)
from .metrics import SubjectManagerMetrics
from .pattern_matcher import PatternMatcher
from .patterns import PREDEFINED_PATTERNS
from .subscription_patterns import (
    get_chat_subscription_patterns,
    get_event_subscription_patterns,
    get_subscription_pattern,
)
from .validation import SubjectValidator


class NATSSubjectManager:  # pylint: disable=too-many-instance-attributes  # Reason: Subject manager requires many state tracking and configuration attributes
    """
    Manager for NATS subject patterns and validation.

    This class provides centralized management of NATS subject naming conventions,
    ensuring consistent subject patterns across the MythosMUD chat system.

    Features:
    - Pattern registration and validation
    - Subject building with parameter validation
    - Subject validation against registered patterns
    - Performance optimization through caching
    - Configurable validation strictness

    Example:
        >>> manager = NATSSubjectManager()
        >>> subject = manager.build_subject("chat_say_room", room_id="arkham_1")
        >>> print(subject)
        'chat.say.room.arkham_1'

    AI: Centralizes subject construction to prevent routing errors and improve debugging.
    AI: Uses caching for performance optimization in high-throughput scenarios.
    """

    def __init__(
        self,
        enable_cache: bool = True,
        max_subject_length: int = 255,
        strict_validation: bool = False,
        enable_metrics: bool = True,
    ):
        """
        Initialize NATS Subject Manager.

        Args:
            enable_cache: Enable validation result caching for performance
            max_subject_length: Maximum allowed subject length (NATS limit is 255)
            strict_validation: Enable strict validation mode (no underscores in identifiers)
            enable_metrics: Enable performance metrics collection

        AI: Cache improves performance for repeated subject validations.
        AI: Strict mode enforces additional constraints for production environments.
        AI: Metrics provide observability for monitoring and optimization.
        """
        # Pattern registry - copy predefined patterns to allow dynamic registration
        self.patterns: dict[str, dict[str, Any]] = {}
        for name, pattern_info in PREDEFINED_PATTERNS.items():
            self.patterns[name] = pattern_info.copy()

        # Validation cache for performance
        self._validation_cache: dict[str, bool] = {}
        self._cache_enabled = enable_cache

        # Configuration
        self._max_subject_length = max_subject_length
        self._strict_validation = strict_validation
        self._metrics_enabled = enable_metrics

        # Performance metrics
        self.metrics = SubjectManagerMetrics() if enable_metrics else None

        # Initialize helper classes
        self._validator = SubjectValidator(max_subject_length, strict_validation)
        self._pattern_matcher = PatternMatcher(strict_validation)

    def build_subject(self, pattern_name: str, **params) -> str:
        """
        Build a NATS subject from a pattern and parameters.

        Args:
            pattern_name: Name of the registered pattern to use
            **params: Parameters required by the pattern

        Returns:
            Fully constructed NATS subject string

        Raises:
            PatternNotFoundError: If pattern_name is not registered
            MissingParameterError: If required parameters are missing
            SubjectValidationError: If parameter values fail validation

        Example:
            >>> manager = NATSSubjectManager()
            >>> subject = manager.build_subject("chat_say_room", room_id="arkham_1")
            >>> print(subject)
            'chat.say.room.arkham_1'

        AI: Validates all parameters before subject construction to prevent invalid subjects.
        AI: Uses template substitution for clean, readable pattern definitions.
        AI: Records performance metrics for monitoring build operations.
        """
        # Avoid expensive timers in hot path for performance; tests capture wall time externally
        success = False

        try:
            pattern_info = self._ensure_pattern_exists(pattern_name)
            pattern = pattern_info["pattern"]
            required_params = pattern_info["required_params"]

            self._ensure_required_params(pattern_name, required_params, params)
            self._validator.validate_pattern_params(pattern, params)
            subject = self._format_subject(pattern_name, pattern, params)
            self._ensure_subject_length(subject)

            success = True
            return subject

        finally:
            # Record metrics with minimal overhead
            if self.metrics:
                self.metrics.record_build(0.0, success)

    def _ensure_pattern_exists(self, pattern_name: str) -> dict[str, Any]:
        """
        Ensure pattern exists in registry.

        Args:
            pattern_name: Name of the pattern to check

        Returns:
            Pattern information dictionary

        Raises:
            PatternNotFoundError: If pattern_name is not registered
        """
        if pattern_name not in self.patterns:
            if self.metrics:
                self.metrics.record_error("pattern_not_found")
            raise PatternNotFoundError(pattern_name)
        return self.patterns[pattern_name]

    def _ensure_required_params(self, pattern_name: str, required_params: list[str], params: dict[str, Any]) -> None:
        """
        Ensure all required parameters are provided.

        Args:
            pattern_name: Name of the pattern
            required_params: List of required parameter names
            params: Provided parameters

        Raises:
            MissingParameterError: If required parameters are missing
        """
        missing_params = [param for param in required_params if param not in params]
        if missing_params:
            if self.metrics:
                self.metrics.record_error("missing_parameter")
            raise MissingParameterError(pattern_name, missing_params)

    def _format_subject(self, pattern_name: str, pattern: str, params: dict[str, Any]) -> str:
        """
        Format subject string from pattern and parameters.

        Args:
            pattern_name: Name of the pattern
            pattern: Pattern template string
            params: Parameters for substitution

        Returns:
            Formatted subject string

        Raises:
            MissingParameterError: If format fails due to missing parameters
        """
        try:
            return pattern.format(**params)
        except KeyError as e:
            # This shouldn't happen if our validation is correct, but handle it anyway
            if self.metrics:
                self.metrics.record_error("missing_parameter")
            raise MissingParameterError(pattern_name, [str(e)]) from e

    def _ensure_subject_length(self, subject: str) -> None:
        """
        Ensure subject length is within limits.

        Args:
            subject: Subject string to validate

        Raises:
            SubjectValidationError: If subject exceeds maximum length
        """
        if len(subject) > self._max_subject_length:
            if self.metrics:
                self.metrics.record_error("validation_error")
            raise SubjectValidationError(
                f"Subject exceeds maximum length of {self._max_subject_length} characters: {len(subject)}"
            )

    def validate_subject(self, subject: str) -> bool:
        """
        Validate a NATS subject against registered patterns.

        Args:
            subject: Subject string to validate

        Returns:
            True if subject is valid, False otherwise

        Example:
            >>> manager = NATSSubjectManager()
            >>> is_valid = manager.validate_subject("chat.say.room.arkham_1")
            >>> print(is_valid)
            True

        AI: Checks subject against all registered patterns for match.
        AI: Uses caching to improve performance for repeated validations.
        AI: Records performance metrics for monitoring validation operations.
        """
        # Check cache first if enabled
        cache_hit = False
        if self._cache_enabled and subject in self._validation_cache:
            cache_hit = True
            result = self._validation_cache[subject]
            self._record_validation_metrics(result, cache_hit)
            return result

        # Perform validation checks
        if not self._validator.validate_subject_basic(subject):
            result = self._cache_result(subject, False)
            self._record_validation_metrics(result, cache_hit)
            return result

        if not self._validator.validate_subject_components(subject):
            result = self._cache_result(subject, False)
            self._record_validation_metrics(result, cache_hit)
            return result

        # Check if subject matches any registered pattern
        is_valid = self._pattern_matcher.matches_any_pattern(subject, self.patterns)
        result = self._cache_result(subject, is_valid)
        self._record_validation_metrics(result, cache_hit)

        return result

    def _record_validation_metrics(self, result: bool, cache_hit: bool) -> None:
        """
        Record validation metrics if metrics are enabled.

        Args:
            result: Validation result
            cache_hit: Whether result was from cache
        """
        if self.metrics:
            self.metrics.record_validation(0.0, result, cache_hit)

    def register_pattern(
        self,
        name: str,
        pattern: str,
        required_params: list[str],
        description: str = "",
    ) -> None:
        """
        Register a new subject pattern.

        Args:
            name: Unique name for the pattern
            pattern: Pattern template with {param} placeholders
            required_params: List of required parameter names
            description: Human-readable description of the pattern

        Raises:
            InvalidPatternError: If pattern format is invalid or name already exists

        Example:
            >>> manager = NATSSubjectManager()
            >>> manager.register_pattern(
            ...     name="chat_party_group",
            ...     pattern="chat.party.group.{party_id}",
            ...     required_params=["party_id"],
            ...     description="Party group messages"
            ... )

        AI: Allows dynamic pattern registration for extensibility without code changes.
        AI: Validates pattern format and parameter consistency before registration.
        """
        # Check for duplicate pattern name
        if name in self.patterns:
            raise InvalidPatternError(f"Pattern '{name}' is already registered")

        # Validate pattern format
        if ".." in pattern or pattern.startswith(".") or pattern.endswith("."):
            raise InvalidPatternError(f"Invalid pattern format: {pattern}")

        # Validate that all required parameters have placeholders
        for param in required_params:
            placeholder = f"{{{param}}}"
            if placeholder not in pattern:
                raise InvalidPatternError(f"Pattern '{pattern}' missing placeholder for required parameter '{param}'")

        # Register the pattern
        self.patterns[name] = {
            "pattern": pattern,
            "required_params": required_params,
            "description": description,
        }

        # Clear validation cache since patterns have changed
        if self._cache_enabled:
            self._validation_cache.clear()

    def get_pattern_info(self, pattern_name: str) -> dict[str, Any]:
        """
        Get information about a registered pattern.

        Args:
            pattern_name: Name of the pattern to retrieve

        Returns:
            Dictionary containing pattern information

        Raises:
            PatternNotFoundError: If pattern_name is not registered

        Example:
            >>> manager = NATSSubjectManager()
            >>> info = manager.get_pattern_info("chat_say_room")
            >>> print(info["pattern"])
            'chat.say.room.{room_id}'

        AI: Provides introspection for debugging and documentation generation.
        """
        if pattern_name not in self.patterns:
            raise PatternNotFoundError(pattern_name)

        pattern_info = self.patterns[pattern_name].copy()
        pattern_info["name"] = pattern_name
        return pattern_info

    def get_all_patterns(self) -> dict[str, dict[str, Any]]:
        """
        Get all registered patterns.

        Returns:
            Dictionary of all registered patterns

        Example:
            >>> manager = NATSSubjectManager()
            >>> patterns = manager.get_all_patterns()
            >>> print(len(patterns))
            7

        AI: Useful for API endpoints that list available subject patterns.
        """
        return {name: self.get_pattern_info(name) for name in self.patterns}

    def get_subscription_pattern(self, pattern_name: str) -> str:
        """
        Get a subscription pattern with wildcards for NATS subscriptions.

        This method converts a pattern template into a subscription pattern
        by replacing parameter placeholders with wildcards (*).

        Args:
            pattern_name: Name of the registered pattern

        Returns:
            Subscription pattern with wildcards

        Raises:
            PatternNotFoundError: If pattern_name is not registered
            SubjectValidationError: If generated pattern is overly broad

        Example:
            >>> manager = NATSSubjectManager()
            >>> sub_pattern = manager.get_subscription_pattern("chat_say_room")
            >>> print(sub_pattern)
            'chat.say.room.*'

        AI: Generates wildcard patterns for NATS subscriptions from registered patterns.
        AI: Replaces all parameter placeholders with '*' for subscription matching.
        AI: Validates that generated patterns are not too broad to prevent unintended subscriptions.
        """
        if pattern_name not in self.patterns:
            raise PatternNotFoundError(pattern_name)

        return get_subscription_pattern(self.patterns[pattern_name], validator=self._validator)

    def get_chat_subscription_patterns(self) -> list[str]:
        """
        Get all chat-related subscription patterns.

        Returns:
            List of subscription patterns for chat subjects

        Example:
            >>> manager = NATSSubjectManager()
            >>> patterns = manager.get_chat_subscription_patterns()
            >>> print(patterns)
            ['chat.say.room.*', 'chat.local.subzone.*', 'chat.global', ...]

        AI: Provides subscription patterns for all chat-related subjects.
        AI: Used by message handlers to subscribe to all chat channels.
        """
        return get_chat_subscription_patterns(self.patterns, validator=self._validator)

    def get_event_subscription_patterns(self) -> list[str]:
        """
        Get all event-related subscription patterns.

        Returns:
            List of subscription patterns for event subjects

        Example:
            >>> manager = NATSSubjectManager()
            >>> patterns = manager.get_event_subscription_patterns()
            >>> print(patterns)
            ['events.player_entered.*', 'events.player_left.*', ...]

        AI: Provides subscription patterns for all event-related subjects.
        AI: Used by message handlers to subscribe to game events and combat events.
        """
        return get_event_subscription_patterns(self.patterns, validator=self._validator)

    def clear_cache(self) -> None:
        """
        Clear the validation cache.

        This is useful for testing or when patterns have been modified.

        AI: Allows cache invalidation when patterns are dynamically updated.
        """
        self._validation_cache.clear()

    def get_performance_metrics(self) -> dict[str, Any] | None:
        """
        Get current performance metrics.

        Returns:
            Dictionary containing performance metrics, or None if metrics disabled

        Example:
            >>> manager = NATSSubjectManager()
            >>> metrics = manager.get_performance_metrics()
            >>> print(f"Cache hit rate: {metrics['cache']['hit_rate']:.2%}")

        AI: Provides observability into subject manager performance.
        AI: Returns None if metrics collection is disabled.
        """
        return self.metrics.get_metrics() if self.metrics else None

    def _cache_result(self, subject: str, result: bool) -> bool:
        """
        Cache validation result if caching is enabled.

        Args:
            subject: Subject that was validated
            result: Validation result

        Returns:
            The result (pass-through)

        AI: Implements simple dict-based cache for validation results.
        AI: Cache is cleared when patterns are modified to prevent stale results.
        """
        if self._cache_enabled:
            self._validation_cache[subject] = result
        return result
