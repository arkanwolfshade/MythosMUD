"""
Custom exceptions for NATS Subject Manager.

This module defines all exception classes used by the NATS Subject Manager
for error handling and validation.
"""


class NATSSubjectError(Exception):
    """Base exception for NATS subject-related errors."""


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


class SubjectValidationError(NATSSubjectError):
    """Exception raised when subject validation fails."""
