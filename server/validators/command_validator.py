"""
Command input validation utilities for MythosMUD.

This module provides functions for validating, cleaning, and normalizing
command input to ensure security and consistency.

Includes both legacy sanitization functions and new security validation.

AI: Multiple layers of validation prevent command injection and other attacks.
"""

import re

from ..structured_logging.enhanced_logging_config import get_logger
from .security_validator import INJECTION_PATTERNS, comprehensive_sanitize_input

logger = get_logger(__name__)


# ============================================================================
# LEGACY VALIDATION FUNCTIONS (preserved for backward compatibility)
# ============================================================================


def normalize_command(command: str) -> str:
    """
    Normalize command input by removing optional slash prefix.

    Supports both traditional MUD commands (go north) and modern slash commands (/go north).
    This allows for flexible command input while maintaining backward compatibility.

    Args:
        command: The raw command string from user input

    Returns:
        Normalized command string with slash prefix removed if present
    """
    if not command:
        return command

    # Remove leading slash if present
    if command.startswith("/"):
        normalized = command[1:].strip()
        logger.debug("Slash prefix removed from command", original=command, normalized=normalized)
        return normalized

    return command.strip()


def is_suspicious_input(command: str) -> bool:
    """
    Check if command contains suspicious patterns that might indicate injection attempts.

    This function focuses on true injection attempts rather than legitimate user expression.
    It's designed to catch malicious patterns while avoiding false positives on
    creative user input.

    Args:
        command: The command string to validate

    Returns:
        bool: True if suspicious patterns are detected, False otherwise
    """
    for pat in INJECTION_PATTERNS:
        if re.search(pat, command, re.IGNORECASE):
            logger.warning("Suspicious command pattern detected", pattern=pat, command=command)
            return True
    return False


def clean_command_input(command: str) -> str:
    """
    Clean and normalize command input with comprehensive sanitization.

    This function applies multiple layers of sanitization:
    1. Unicode normalization and fixing (ftfy)
    2. ANSI code removal (strip-ansi)
    3. Control character removal
    4. Whitespace normalization

    Focuses on sanitization (cleaning) rather than validation (rejection)
    to preserve user expression freedom.

    Args:
        command: The raw command string

    Returns:
        str: Fully sanitized command string
    """
    if not command:
        return command

    # Apply comprehensive sanitization first
    sanitized = comprehensive_sanitize_input(command)

    # Then apply traditional cleaning (whitespace normalization)
    cleaned = re.sub(r"\s+", " ", sanitized).strip()

    if cleaned != command:
        logger.debug("Command input sanitized and cleaned", original=command, cleaned=cleaned)

    return cleaned


def validate_command_length(command: str, max_length: int = 1000) -> bool:
    """
    Validate that command length is within acceptable limits.

    Args:
        command: The command string to validate
        max_length: Maximum allowed command length

    Returns:
        bool: True if command length is acceptable, False otherwise
    """
    if len(command) > max_length:
        logger.warning("Command too long", command_length=len(command), max_length=max_length)
        return False
    return True


def validate_command_format(command: str) -> tuple[bool, str]:
    """
    Validate command format and return validation result with error message.

    Args:
        command: The command string to validate

    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if not command:
        return False, "Empty command"

    if is_suspicious_input(command):
        return False, "Command contains suspicious patterns"

    if not validate_command_length(command):
        return False, "Command too long"

    return True, ""


# ============================================================================
# NEW SECURITY VALIDATION CLASS (CRITICAL-3)
# ============================================================================


class CommandValidator:
    """
    Enhanced command security validation to prevent injection attacks.

    Implements multiple security checks:
    - Dangerous pattern detection (shell injection, etc.)
    - Length validation
    - Null byte detection
    - Security-sensitive command identification

    AI: Defense-in-depth approach - multiple independent checks for robustness.
    """

    # Patterns that indicate potential shell injection or system command execution
    # AI: These patterns target common injection techniques but aren't exhaustive
    DANGEROUS_PATTERNS = [
        r";\s*rm\s+-rf",  # Dangerous file deletion
        r"\$\(",  # Command substitution
        r"`",  # Backtick command execution
        r"\|\s*sh",  # Pipe to shell
        r">\s*/dev",  # Device file redirection
        r"<\s*/dev",  # Device file input
        r"2>&1",  # stderr redirection (suspicious in game context)
        r"&&\s*rm",  # Chained deletion
        r"\|\s*bash",  # Pipe to bash
        r"\|\s*zsh",  # Pipe to zsh
        r"exec\s+",  # Direct execution
        r"eval\s+",  # Eval command
        r"import\s+os",  # Python os import
        r"__import__",  # Python dynamic import
        r"subprocess",  # Python subprocess
    ]

    # Commands that require special audit logging
    # AI: These are admin/privileged commands that should be logged
    SECURITY_SENSITIVE_COMMANDS = {
        "admin",
        "teleport",
        "spawn",
        "delete",
        "grant",
        "revoke",
        "ban",
        "unban",
        "kick",
        "mute",
        "unmute",
        "promote",
        "demote",
        "shutdown",
        "restart",
        "reload",
        "config",
        "debug",
    }

    # Maximum lengths for different command contexts
    # AI: Limits prevent buffer overflow and DoS via excessive memory
    MAX_COMMAND_LENGTH = 1000  # Normal command
    MAX_EXPANDED_COMMAND_LENGTH = 10000  # After alias expansion
    MAX_ALIAS_DEFINITION_LENGTH = 5000  # Alias definition itself

    @classmethod
    def validate_command_content(cls, command: str) -> tuple[bool, str | None]:
        """
        Validate command for security threats.

        Performs comprehensive security checks on command content.

        Args:
            command: Command string to validate

        Returns:
            Tuple of (is_valid, error_message)
            - is_valid: True if command is safe, False otherwise
            - error_message: Description of security issue if invalid, None if valid

        AI: Call this before executing ANY user-provided command.
        """
        # Check for null bytes (common in injection attacks)
        if "\x00" in command:
            logger.warning("Command contains null bytes", command=command[:50])
            return False, "Command contains null bytes (potential injection attempt)"

        # Check for dangerous patterns
        for pattern in cls.DANGEROUS_PATTERNS:
            if re.search(pattern, command, re.IGNORECASE):
                logger.warning("Command contains dangerous pattern", pattern=pattern, command=command[:50])
                return False, "Command contains potentially dangerous pattern"

        # Check for excessive length
        if len(command) > cls.MAX_COMMAND_LENGTH:
            logger.warning("Command exceeds maximum length", length=len(command), max_length=cls.MAX_COMMAND_LENGTH)
            return False, f"Command exceeds maximum length ({cls.MAX_COMMAND_LENGTH} characters)"

        # Check for non-printable characters (except newline/tab/space)
        non_printable = [c for c in command if ord(c) < 32 and c not in "\n\t "]
        if non_printable:
            logger.warning("Command contains non-printable characters", command=command[:50])
            return False, "Command contains non-printable characters"

        # Command passed all checks
        return True, None

    @classmethod
    def validate_expanded_command(cls, command: str) -> tuple[bool, str | None]:
        """
        Validate command after alias expansion.

        Uses stricter length limits since aliases can expand significantly.

        Args:
            command: Expanded command string to validate

        Returns:
            Tuple of (is_valid, error_message)

        AI: Always validate AFTER alias expansion to catch expansion attacks.
        """
        # Check basic validation first
        is_valid, error = cls.validate_command_content(command)
        if not is_valid:
            return is_valid, error

        # Check expanded command length (more permissive than base)
        if len(command) > cls.MAX_EXPANDED_COMMAND_LENGTH:
            logger.warning(
                "Expanded command exceeds maximum length",
                length=len(command),
                max_length=cls.MAX_EXPANDED_COMMAND_LENGTH,
            )
            return False, f"Expanded command exceeds maximum length ({cls.MAX_EXPANDED_COMMAND_LENGTH} characters)"

        return True, None

    @classmethod
    def validate_alias_definition(cls, alias_command: str) -> tuple[bool, str | None]:
        """
        Validate alias definition command.

        Applies validation to alias commands before they're saved.
        Prevents storing malicious aliases.

        Args:
            alias_command: Alias command definition to validate

        Returns:
            Tuple of (is_valid, error_message)

        AI: Validate at alias creation time to prevent storing malicious content.
        """
        # Check basic validation
        is_valid, error = cls.validate_command_content(alias_command)
        if not is_valid:
            return is_valid, error

        # Check alias definition length
        if len(alias_command) > cls.MAX_ALIAS_DEFINITION_LENGTH:
            logger.warning(
                "Alias definition exceeds maximum length",
                length=len(alias_command),
                max_length=cls.MAX_ALIAS_DEFINITION_LENGTH,
            )
            return False, f"Alias definition exceeds maximum length ({cls.MAX_ALIAS_DEFINITION_LENGTH} characters)"

        return True, None

    @classmethod
    def is_security_sensitive(cls, command: str) -> bool:
        """
        Check if command requires audit logging.

        Identifies commands that should be logged for security auditing,
        such as admin commands, permission changes, etc.

        Args:
            command: Command string to check

        Returns:
            True if command should be audit logged, False otherwise

        AI: Use this to determine which commands need special audit logging.
        """
        cmd_parts = command.strip().split()
        if not cmd_parts:
            return False

        base_command = cmd_parts[0].lower()
        is_sensitive = base_command in cls.SECURITY_SENSITIVE_COMMANDS

        if is_sensitive:
            logger.debug("Security-sensitive command detected", command=base_command)

        return is_sensitive

    @classmethod
    def sanitize_for_logging(cls, command: str, max_length: int = 200) -> str:
        """
        Sanitize command for safe logging.

        Truncates and removes sensitive data before logging.
        Prevents log injection and credential leakage.

        Args:
            command: Command to sanitize
            max_length: Maximum length for log entry

        Returns:
            Sanitized command string safe for logging

        AI: Always use this before logging commands to prevent log injection.
        """
        # Remove potential passwords/tokens (naive approach)
        sanitized = re.sub(r"(password|token|secret|key)[\s=:]+\S+", r"\1=****", command, flags=re.IGNORECASE)

        # Truncate if too long
        if len(sanitized) > max_length:
            sanitized = sanitized[:max_length] + "...[truncated]"

        # Remove control characters
        sanitized = "".join(c if c.isprintable() or c in "\n\t " else "?" for c in sanitized)

        return sanitized

    @classmethod
    def extract_command_name(cls, command: str) -> str | None:
        """
        Extract the base command name from a command string.

        Handles various formats:
        - Simple: "look"
        - With args: "look north"
        - With pipes: "look | grep foo"
        - With semicolons: "look; inventory"

        Args:
            command: Command string

        Returns:
            Base command name or None if empty

        AI: Useful for command routing and statistics.
        """
        if not command or not command.strip():
            return None

        # Split on command separators and take first part
        first_part = re.split(r"[|;&]", command)[0].strip()

        # Extract first word
        words = first_part.split()
        if not words:
            return None

        return words[0].lower()

    @classmethod
    def is_valid_command_name(cls, name: str) -> bool:
        """
        Check if a string is a valid command/alias name.

        Valid names:
        - Start with letter
        - Contain only letters, numbers, underscore, dash
        - Length 1-50 characters

        Args:
            name: Command/alias name to validate

        Returns:
            True if valid name format, False otherwise

        AI: Use for alias name validation and command registration.
        """
        if not name or len(name) > 50:
            return False

        # Must start with letter
        if not name[0].isalpha():
            return False

        # Only alphanumeric, underscore, dash allowed
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", name):
            return False

        return True
