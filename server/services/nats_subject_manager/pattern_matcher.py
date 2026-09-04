"""
Pattern matching utilities for NATS Subject Manager.

This module provides pattern matching logic for validating subjects against patterns.
"""

# pylint: disable=too-few-public-methods  # Reason: Pattern matcher class with focused responsibility, minimal public interface

import re
from typing import Any


class PatternMatcher:  # pylint: disable=too-few-public-methods  # Reason: Pattern matcher class with focused responsibility, minimal public interface
    """
    Matcher for validating subjects against registered patterns.
    """

    def __init__(self, strict_validation: bool = False) -> None:
        """
        Initialize pattern matcher.

        Args:
            strict_validation: Enable strict validation mode (no underscores)
        """
        self._strict_validation = strict_validation
        self._valid_component_pattern = re.compile(r"^[a-zA-Z0-9_-]+$")
        self._strict_component_pattern = re.compile(r"^[a-zA-Z0-9-]+$")  # No underscores

    def matches_any_pattern(self, subject: str, patterns: dict[str, dict[str, Any]]) -> bool:
        """
        Check if subject matches any registered pattern.

        Args:
            subject: Subject string to check
            patterns: Dictionary of registered patterns

        Returns:
            True if subject matches at least one pattern, False otherwise
        """
        components = subject.split(".")

        for pattern_info in patterns.values():
            pattern = pattern_info["pattern"]
            pattern_components = pattern.split(".")

            # Quick length check
            if len(components) != len(pattern_components):
                continue

            # Check if components match the pattern
            if self._components_match_pattern(components, pattern_components):
                return True

        return False

    def _components_match_pattern(self, components: list[str], pattern_components: list[str]) -> bool:
        """
        Check if subject components match a pattern.

        Args:
            components: Subject components to check
            pattern_components: Pattern components to match against

        Returns:
            True if components match the pattern, False otherwise
        """
        component_pattern = self._strict_component_pattern if self._strict_validation else self._valid_component_pattern

        for subject_comp, pattern_comp in zip(components, pattern_components, strict=False):
            # If pattern component is a placeholder, validate component format
            if pattern_comp.startswith("{") and pattern_comp.endswith("}"):
                if not component_pattern.match(subject_comp):
                    return False
            # Otherwise, must be exact match
            elif subject_comp != pattern_comp:
                return False

        return True
