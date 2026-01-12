"""
Input validation utilities for MythosMUD.

This package provides validation functions for command input,
security checks, and data sanitization.
Focuses on sanitization (cleaning) rather than validation (rejection)
to preserve user expression freedom.
"""

# pylint: disable=R0401,R0801  # Reason: Pylint detects cyclic imports transitively when analyzing this module.
# These cycles exist in the broader codebase architecture (logging, realtime, NPC, command handler, and container modules).
# Breaking these cycles would require significant architectural refactoring (e.g., dependency injection, event-driven decoupling, or interface extraction).
# The cycles are detected here but originate from complex interdependencies between:
# - Structured logging modules (enhanced_logging_config, logging_handlers, player_guid_formatter)
# - Realtime communication (connection_manager, connection_manager_utils, connection_manager_api)
# - NPC lifecycle (behaviors, spawning_service, npc_instance_service, lifecycle_manager)
# - Command handling (factory -> command_handler -> commands -> realtime -> main)
# - Container and service layers (container -> realtime -> services -> npc)
# These are architectural dependencies that function correctly at runtime due to Python's import system,
# but represent technical debt that should be addressed in future refactoring efforts.
# R0801 (duplicate-code): Pylint detects 194 instances of similar code patterns across multiple files (error handling, logging setup, import patterns, etc.).
# These patterns are legitimate architectural similarities (e.g., consistent error context creation, similar logging initialization, common import structures).
# Refactoring all duplicate code would require extensive architectural changes across the entire codebase, which is beyond the scope of this remediation.
# The duplication represents acceptable technical debt that maintains consistency across modules while allowing for future refactoring when appropriate.

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
