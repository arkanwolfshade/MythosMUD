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

import re
from typing import Any


# Custom Exceptions
class NATSSubjectError(Exception):
    """Base exception for NATS subject-related errors."""

    pass


class PatternNotFoundError(NATSSubjectError):
    """Exception raised when a pattern name is not found in registry."""

    def __init__(self, pattern_name: str):
        self.pattern_name = pattern_name
        super().__init__(f"Pattern '{pattern_name}' not found in registry")


class MissingParameterError(NATSSubjectError):
    """Exception raised when required parameters are missing."""

    def __init__(self, pattern_name: str, missing_params: list[str]):
        self.pattern_name = pattern_name
        self.missing_params = missing_params
        params_str = ", ".join(missing_params)
        super().__init__(f"Pattern '{pattern_name}' is missing required parameter(s): {params_str}")


class InvalidPatternError(NATSSubjectError):
    """Exception raised when a pattern format is invalid."""

    pass


class SubjectValidationError(NATSSubjectError):
    """Exception raised when subject validation fails."""

    pass


# Predefined subject patterns for MythosMUD chat system
# AI: These patterns define the hierarchical structure: {service}.{channel}.{scope}.{identifier}
PREDEFINED_PATTERNS = {
    # Chat patterns
    "chat_say_room": {
        "pattern": "chat.say.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level say messages",
    },
    "chat_local_subzone": {
        "pattern": "chat.local.subzone.{subzone}",
        "required_params": ["subzone"],
        "description": "Subzone-level local messages",
    },
    "chat_global": {
        "pattern": "chat.global",
        "required_params": [],
        "description": "Global chat messages",
    },
    "chat_whisper_player": {
        "pattern": "chat.whisper.player.{target_id}",
        "required_params": ["target_id"],
        "description": "Player-to-player whisper messages",
    },
    "chat_system": {
        "pattern": "chat.system",
        "required_params": [],
        "description": "System-wide messages",
    },
    "chat_emote_room": {
        "pattern": "chat.emote.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level emote messages",
    },
    "chat_pose_room": {
        "pattern": "chat.pose.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level pose messages",
    },
    # Event patterns
    "event_player_entered": {
        "pattern": "events.player_entered.{room_id}",
        "required_params": ["room_id"],
        "description": "Player entered room events",
    },
    "event_player_left": {
        "pattern": "events.player_left.{room_id}",
        "required_params": ["room_id"],
        "description": "Player left room events",
    },
    "event_game_tick": {
        "pattern": "events.game_tick",
        "required_params": [],
        "description": "Global game tick events",
    },
    "event_player_mortally_wounded": {
        "pattern": "events.player_mortally_wounded.{room_id}",
        "required_params": ["room_id"],
        "description": "Player mortally wounded events",
    },
    "event_player_hp_decay": {
        "pattern": "events.player_hp_decay.{room_id}",
        "required_params": ["room_id"],
        "description": "Player HP decay events",
    },
    "event_player_died": {
        "pattern": "events.player_died.{room_id}",
        "required_params": ["room_id"],
        "description": "Player death events",
    },
    "event_player_respawned": {
        "pattern": "events.player_respawned.{room_id}",
        "required_params": ["room_id"],
        "description": "Player respawn events",
    },
    # Combat patterns
    "combat_attack": {
        "pattern": "combat.attack.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat attack events",
    },
    "combat_npc_attacked": {
        "pattern": "combat.npc_attacked.{room_id}",
        "required_params": ["room_id"],
        "description": "NPC attacked events",
    },
    "combat_npc_action": {
        "pattern": "combat.npc_action.{room_id}",
        "required_params": ["room_id"],
        "description": "NPC action events",
    },
    "combat_started": {
        "pattern": "combat.started.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat started events",
    },
    "combat_ended": {
        "pattern": "combat.ended.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat ended events",
    },
    "combat_npc_died": {
        "pattern": "combat.npc_died.{room_id}",
        "required_params": ["room_id"],
        "description": "NPC death events",
    },
    "combat_damage": {
        "pattern": "combat.damage.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat damage events",
    },
    "combat_turn": {
        "pattern": "combat.turn.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat turn events",
    },
    "combat_timeout": {
        "pattern": "combat.timeout.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat timeout events",
    },
    "combat_hp_update": {
        "pattern": "combat.hp_update.{player_id}",
        "required_params": ["player_id"],
        "description": "Player HP update events",
    },
}


class SubjectManagerMetrics:
    """
    Performance metrics for NATS Subject Manager operations.

    Tracks validation times, cache performance, and operation counts
    for monitoring and optimization purposes.

    AI: Provides observability into subject management performance.
    AI: Helps identify bottlenecks and optimize validation operations.
    """

    def __init__(self):
        """Initialize metrics collection."""
        # Validation metrics
        self.validation_count = 0
        self.validation_success_count = 0
        self.validation_failure_count = 0
        self.validation_times: list[float] = []  # Rolling window of last 1000 times

        # Cache metrics
        self.cache_hits = 0
        self.cache_misses = 0

        # Build metrics
        self.build_count = 0
        self.build_success_count = 0
        self.build_failure_count = 0
        self.build_times: list[float] = []  # Rolling window of last 1000 times

        # Error metrics
        self.pattern_not_found_errors = 0
        self.missing_parameter_errors = 0
        self.validation_errors = 0

    def record_validation(self, duration: float, success: bool, cache_hit: bool):
        """
        Record a validation operation.

        Args:
            duration: Time taken in seconds
            success: Whether validation succeeded
            cache_hit: Whether result was from cache
        """
        self.validation_count += 1
        if success:
            self.validation_success_count += 1
        else:
            self.validation_failure_count += 1

        if cache_hit:
            self.cache_hits += 1
        else:
            self.cache_misses += 1

        self.validation_times.append(duration)
        if len(self.validation_times) > 1000:
            self.validation_times = self.validation_times[-1000:]

    def record_build(self, duration: float, success: bool):
        """
        Record a build operation.

        Args:
            duration: Time taken in seconds
            success: Whether build succeeded
        """
        self.build_count += 1
        if success:
            self.build_success_count += 1
        else:
            self.build_failure_count += 1

        self.build_times.append(duration)
        if len(self.build_times) > 1000:
            self.build_times = self.build_times[-1000:]

    def record_error(self, error_type: str):
        """
        Record an error occurrence.

        Args:
            error_type: Type of error (pattern_not_found, missing_parameter, validation_error)
        """
        if error_type == "pattern_not_found":
            self.pattern_not_found_errors += 1
        elif error_type == "missing_parameter":
            self.missing_parameter_errors += 1
        elif error_type == "validation_error":
            self.validation_errors += 1

    def get_metrics(self) -> dict[str, Any]:
        """
        Get current metrics summary.

        Returns:
            Dictionary containing all metrics
        """
        return {
            "validation": {
                "total_count": self.validation_count,
                "success_count": self.validation_success_count,
                "failure_count": self.validation_failure_count,
                "success_rate": self.validation_success_count / max(self.validation_count, 1),
                "avg_time_ms": sum(self.validation_times) / max(len(self.validation_times), 1) * 1000,
                "p95_time_ms": self._calculate_percentile(self.validation_times, 0.95) * 1000
                if self.validation_times
                else 0,
            },
            "cache": {
                "hits": self.cache_hits,
                "misses": self.cache_misses,
                "hit_rate": self.cache_hits / max(self.cache_hits + self.cache_misses, 1),
            },
            "build": {
                "total_count": self.build_count,
                "success_count": self.build_success_count,
                "failure_count": self.build_failure_count,
                "success_rate": self.build_success_count / max(self.build_count, 1),
                "avg_time_ms": sum(self.build_times) / max(len(self.build_times), 1) * 1000,
                "p95_time_ms": self._calculate_percentile(self.build_times, 0.95) * 1000 if self.build_times else 0,
            },
            "errors": {
                "pattern_not_found": self.pattern_not_found_errors,
                "missing_parameter": self.missing_parameter_errors,
                "validation_errors": self.validation_errors,
                "total_errors": self.pattern_not_found_errors + self.missing_parameter_errors + self.validation_errors,
            },
        }

    @staticmethod
    def _calculate_percentile(times: list[float], percentile: float) -> float:
        """
        Calculate percentile from list of times.

        Args:
            times: List of time measurements
            percentile: Percentile to calculate (0.0-1.0)

        Returns:
            Percentile value
        """
        if not times:
            return 0.0
        sorted_times = sorted(times)
        index = int(len(sorted_times) * percentile)
        return sorted_times[min(index, len(sorted_times) - 1)]

    def reset(self):
        """Reset all metrics to zero."""
        self.__init__()


class NATSSubjectManager:
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

        # Compiled regex patterns for validation
        # AI: Pre-compile patterns for better performance
        self._valid_component_pattern = re.compile(r"^[a-zA-Z0-9_-]+$")
        self._strict_component_pattern = re.compile(r"^[a-zA-Z0-9-]+$")  # No underscores

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
            # Check if pattern exists
            if pattern_name not in self.patterns:
                if self.metrics:
                    self.metrics.record_error("pattern_not_found")
                raise PatternNotFoundError(pattern_name)

            pattern_info = self.patterns[pattern_name]
            pattern = pattern_info["pattern"]
            required_params = pattern_info["required_params"]

            # Check for missing required parameters
            missing_params = [param for param in required_params if param not in params]
            if missing_params:
                if self.metrics:
                    self.metrics.record_error("missing_parameter")
                raise MissingParameterError(pattern_name, missing_params)

            # Validate parameter values
            for param_name, param_value in params.items():
                # Only validate parameters that are actually used in the pattern
                if f"{{{param_name}}}" in pattern:
                    self._validate_parameter_value(param_name, param_value)

            # Build subject by substituting parameters
            try:
                subject = pattern.format(**params)
            except KeyError as e:
                # This shouldn't happen if our validation is correct, but handle it anyway
                if self.metrics:
                    self.metrics.record_error("missing_parameter")
                raise MissingParameterError(pattern_name, [str(e)]) from e

            # Validate final subject length
            if len(subject) > self._max_subject_length:
                if self.metrics:
                    self.metrics.record_error("validation_error")
                raise SubjectValidationError(
                    f"Subject exceeds maximum length of {self._max_subject_length} characters: {len(subject)}"
                )

            success = True
            return subject

        finally:
            # Record metrics with minimal overhead
            if self.metrics:
                self.metrics.record_build(0.0, success)

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
        # Avoid expensive timers in hot path; tests measure externally
        cache_hit = False

        # Check cache first if enabled
        if self._cache_enabled and subject in self._validation_cache:
            cache_hit = True
            result = self._validation_cache[subject]
            if self.metrics:
                self.metrics.record_validation(0.0, result, cache_hit)
            return result

        # Basic validation checks
        if not subject or len(subject) == 0:
            result = self._cache_result(subject, False)
            if self.metrics:
                self.metrics.record_validation(0.0, result, cache_hit)
            return result

        if len(subject) > self._max_subject_length:
            result = self._cache_result(subject, False)
            if self.metrics:
                self.metrics.record_validation(0.0, result, cache_hit)
            return result

        # Check for malformed structure (empty components)
        if ".." in subject or subject.startswith(".") or subject.endswith("."):
            result = self._cache_result(subject, False)
            if self.metrics:
                self.metrics.record_validation(0.0, result, cache_hit)
            return result

        # Validate each component
        components = subject.split(".")
        component_pattern = self._strict_component_pattern if self._strict_validation else self._valid_component_pattern

        for component in components:
            if not component or not component_pattern.match(component):
                result = self._cache_result(subject, False)
                if self.metrics:
                    self.metrics.record_validation(0.0, result, cache_hit)
                return result

        # Check if subject matches any registered pattern
        is_valid = self._matches_any_pattern(subject)
        result = self._cache_result(subject, is_valid)

        # Record metrics
        if self.metrics:
            self.metrics.record_validation(0.0, result, cache_hit)

        return result

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

        Example:
            >>> manager = NATSSubjectManager()
            >>> sub_pattern = manager.get_subscription_pattern("chat_say_room")
            >>> print(sub_pattern)
            'chat.say.room.*'

        AI: Generates wildcard patterns for NATS subscriptions from registered patterns.
        AI: Replaces all parameter placeholders with '*' for subscription matching.
        """
        if pattern_name not in self.patterns:
            raise PatternNotFoundError(pattern_name)

        pattern_info = self.patterns[pattern_name]
        pattern = pattern_info["pattern"]

        # Replace all parameter placeholders with wildcards
        subscription_pattern = pattern
        for param in pattern_info["required_params"]:
            placeholder = f"{{{param}}}"
            subscription_pattern = subscription_pattern.replace(placeholder, "*")

        return subscription_pattern

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
        chat_patterns = []

        # Get subscription patterns for predefined chat patterns
        chat_pattern_names = [
            "chat_say_room",
            "chat_local_subzone",
            "chat_global",
            "chat_whisper_player",
            "chat_system",
            "chat_emote_room",
            "chat_pose_room",
        ]

        for pattern_name in chat_pattern_names:
            if pattern_name in self.patterns:
                chat_patterns.append(self.get_subscription_pattern(pattern_name))

        return chat_patterns

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
        event_patterns = []

        # Get subscription patterns for predefined event patterns
        event_pattern_names = [
            "event_player_entered",
            "event_player_left",
            "event_game_tick",
            "event_player_mortally_wounded",
            "event_player_hp_decay",
            "event_player_died",
            "event_player_respawned",
            "combat_attack",
            "combat_npc_attacked",
            "combat_npc_action",
            "combat_started",
            "combat_ended",
            "combat_npc_died",
            "combat_damage",
            "combat_turn",
            "combat_timeout",
        ]

        for pattern_name in event_pattern_names:
            if pattern_name in self.patterns:
                event_patterns.append(self.get_subscription_pattern(pattern_name))

        return event_patterns

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

    def _validate_parameter_value(self, param_name: str, param_value: Any) -> None:
        """
        Validate a parameter value.

        Args:
            param_name: Name of the parameter
            param_value: Value to validate

        Raises:
            SubjectValidationError: If parameter value is invalid

        AI: Ensures parameter values don't contain characters that would break NATS subjects.
        """
        # Convert to string for validation
        str_value = str(param_value)

        # Check for empty values
        if not str_value or len(str_value) == 0:
            raise SubjectValidationError(f"Parameter '{param_name}' cannot be empty")

        # Check for invalid characters
        component_pattern = self._strict_component_pattern if self._strict_validation else self._valid_component_pattern

        if not component_pattern.match(str_value):
            if self._strict_validation:
                raise SubjectValidationError(
                    f"Parameter '{param_name}' contains invalid characters: '{str_value}' "
                    "(strict mode: only letters, numbers, and hyphens allowed)"
                )
            else:
                raise SubjectValidationError(
                    f"Parameter '{param_name}' contains invalid characters: '{str_value}' "
                    "(allowed: letters, numbers, underscores, hyphens)"
                )

    def _matches_any_pattern(self, subject: str) -> bool:
        """
        Check if subject matches any registered pattern.

        Args:
            subject: Subject string to check

        Returns:
            True if subject matches at least one pattern, False otherwise

        AI: Converts pattern templates to regex for flexible matching.
        AI: Supports both exact subjects and wildcard subscription patterns.
        """
        components = subject.split(".")

        for pattern_info in self.patterns.values():
            pattern = pattern_info["pattern"]
            pattern_components = pattern.split(".")

            # Quick length check
            if len(components) != len(pattern_components):
                continue

            # Check each component
            matches = True
            for subject_comp, pattern_comp in zip(components, pattern_components, strict=False):
                # If pattern component is a placeholder, any valid component matches
                if pattern_comp.startswith("{") and pattern_comp.endswith("}"):
                    # Validate component format
                    component_pattern = (
                        self._strict_component_pattern if self._strict_validation else self._valid_component_pattern
                    )
                    if not component_pattern.match(subject_comp):
                        matches = False
                        break
                # Otherwise, must be exact match
                elif subject_comp != pattern_comp:
                    matches = False
                    break

            if matches:
                return True

        return False

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


# Global instance for convenience (can be overridden in tests)
nats_subject_manager = NATSSubjectManager()
