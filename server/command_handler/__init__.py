"""
Command Handler Package for MythosMUD.

This package provides modular components for command processing,
organized into logical submodules for maintainability.

As the Necronomicon states: "In unity there is strength, and in
consistency there is power."
"""

from .alias_expansion import (
    check_alias_safety,
    handle_expanded_command,
    validate_expanded_command,
)
from .catatonia_check import check_catatonia_block
from .command_input import (
    CATATONIA_ALLOWED_COMMANDS,
    MAX_COMMAND_LENGTH,
    MAX_EXPANDED_COMMAND_LENGTH,
    clean_command_input,
    normalize_command,
    should_treat_as_emote,
)
from .processing import process_command_with_validation

__all__ = [
    # Command input utilities
    "clean_command_input",
    "normalize_command",
    "should_treat_as_emote",
    "MAX_COMMAND_LENGTH",
    "MAX_EXPANDED_COMMAND_LENGTH",
    "CATATONIA_ALLOWED_COMMANDS",
    # Alias expansion
    "check_alias_safety",
    "handle_expanded_command",
    "validate_expanded_command",
    # Catatonia checking
    "check_catatonia_block",
    # Processing
    "process_command_with_validation",
]
