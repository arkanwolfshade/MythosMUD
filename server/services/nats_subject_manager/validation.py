"""
Subject validation utilities for NATS Subject Manager.

This module provides validation functions for NATS subjects and parameters.
"""

import re
from typing import Any

from .exceptions import SubjectValidationError


class SubjectValidator:
    """
    Validator for NATS subjects and parameters.

    Provides validation logic that can be reused across the subject manager.
    """

    def __init__(self, max_subject_length: int = 255, strict_validation: bool = False):
        """
        Initialize validator.

        Args:
            max_subject_length: Maximum allowed subject length
            strict_validation: Enable strict validation mode (no underscores)
        """
        self._max_subject_length = max_subject_length
        self._strict_validation = strict_validation
        self._valid_component_pattern = re.compile(r"^[a-zA-Z0-9_-]+$")
        self._strict_component_pattern = re.compile(r"^[a-zA-Z0-9-]+$")  # No underscores

    def validate_subject_basic(self, subject: str) -> bool:
        """
        Perform basic validation checks on subject.

        Args:
            subject: Subject string to validate

        Returns:
            True if basic validation passes, False otherwise
        """
        if not subject:
            return False

        if len(subject) > self._max_subject_length:
            return False

        # Check for malformed structure (empty components)
        if ".." in subject or subject.startswith(".") or subject.endswith("."):
            return False

        return True

    def validate_subject_components(self, subject: str) -> bool:
        """
        Validate each component of the subject.

        Args:
            subject: Subject string to validate

        Returns:
            True if all components are valid, False otherwise
        """
        components = subject.split(".")
        component_pattern = self._strict_component_pattern if self._strict_validation else self._valid_component_pattern

        for component in components:
            if not component or not component_pattern.match(component):
                return False

        return True

    def validate_parameter_value(self, param_name: str, param_value: Any) -> None:
        """
        Validate a parameter value.

        Args:
            param_name: Name of the parameter
            param_value: Value to validate

        Raises:
            SubjectValidationError: If parameter value is invalid
        """
        # Convert to string for validation
        str_value = str(param_value)

        # Check for empty values
        if not str_value:
            raise SubjectValidationError(f"Parameter '{param_name}' cannot be empty")

        # Check for invalid characters
        component_pattern = self._strict_component_pattern if self._strict_validation else self._valid_component_pattern

        if not component_pattern.match(str_value):
            if self._strict_validation:
                raise SubjectValidationError(
                    f"Parameter '{param_name}' contains invalid characters: '{str_value}' "
                    "(strict mode: only letters, numbers, and hyphens allowed)"
                )
            raise SubjectValidationError(
                f"Parameter '{param_name}' contains invalid characters: '{str_value}' "
                "(allowed: letters, numbers, underscores, hyphens)"
            )

    def validate_pattern_params(self, pattern: str, params: dict[str, Any]) -> None:
        """
        Validate all parameters used in the pattern.

        Args:
            pattern: Pattern template string
            params: Parameters to validate

        Raises:
            SubjectValidationError: If parameter values fail validation
        """
        for param_name, param_value in params.items():
            # Only validate parameters that are actually used in the pattern
            if f"{{{param_name}}}" in pattern:
                self.validate_parameter_value(param_name, param_value)

    def validate_subscription_pattern(self, pattern: str) -> bool:
        """
        Validate that a subscription pattern is not overly broad.

        Prevents patterns like:
        - `*.*.*.*` (too many wildcards)
        - `chat.*.*` (too broad)
        - `*` (single wildcard for entire subject)

        Args:
            pattern: Subscription pattern to validate (may contain wildcards)

        Returns:
            True if pattern is appropriately scoped, False if too broad

        AI: Prevents overly broad subscriptions that could receive unintended messages.
        """
        if not pattern:
            return False

        components = pattern.split(".")
        wildcard_count = sum(1 for comp in components if comp == "*" or comp == ">")

        # Reject patterns with too many wildcards (more than 2)
        if wildcard_count > 2:
            return False

        # Reject single-component wildcard patterns (e.g., "*", ">")
        if len(components) == 1 and wildcard_count == 1:
            return False

        # Reject patterns where all components are wildcards (e.g., "*.*", "*.*.*")
        if wildcard_count == len(components) and len(components) > 1:
            return False

        # Reject patterns starting with wildcard (e.g., "*.chat.say")
        if components[0] in ("*", ">"):
            return False

        return True
