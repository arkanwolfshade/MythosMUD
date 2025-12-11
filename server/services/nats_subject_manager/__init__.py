"""
NATS Subject Manager for MythosMUD.

This package provides centralized subject naming conventions for NATS messaging,
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

# Export exceptions for backward compatibility
from .exceptions import (
    InvalidPatternError,
    MissingParameterError,
    NATSSubjectError,
    PatternNotFoundError,
    SubjectValidationError,
)

# Export main manager class
from .manager import NATSSubjectManager

# Export metrics class
from .metrics import SubjectManagerMetrics

# Export patterns for backward compatibility
from .patterns import PREDEFINED_PATTERNS

# Global instance for convenience (can be overridden in tests)
nats_subject_manager = NATSSubjectManager()

__all__ = [
    # Exceptions
    "NATSSubjectError",
    "PatternNotFoundError",
    "MissingParameterError",
    "InvalidPatternError",
    "SubjectValidationError",
    # Classes
    "SubjectManagerMetrics",
    "NATSSubjectManager",
    # Constants
    "PREDEFINED_PATTERNS",
    # Global instance
    "nats_subject_manager",
]
