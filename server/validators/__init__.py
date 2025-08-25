"""
Input validation utilities for MythosMUD.

This package provides validation functions for command input,
security checks, and data sanitization.
Focuses on sanitization (cleaning) rather than validation (rejection)
to preserve user expression freedom.
"""

from .command_validator import (
    clean_command_input,
    is_suspicious_input,
    normalize_command,
)
from .security_validator import (
    INJECTION_PATTERNS,
    SLASH_COMMANDS,
    comprehensive_sanitize_input,
    sanitize_unicode_input,
    strip_ansi_codes,
)

__all__ = [
    "clean_command_input",
    "is_suspicious_input",
    "normalize_command",
    "INJECTION_PATTERNS",
    "SLASH_COMMANDS",
    "comprehensive_sanitize_input",
    "sanitize_unicode_input",
    "strip_ansi_codes",
]
