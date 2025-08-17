"""
Security validation constants and patterns for MythosMUD.

This module defines security patterns and constants used for
validating command input and preventing injection attacks.
"""

# Patterns to reject for command injection (expand as needed)
INJECTION_PATTERNS = [
    r"[;|&]",  # shell metacharacters
    r"\b(or|and)\b.*=",  # SQL injection
    r"__import__|eval|exec|system|os\.",  # Python injection
    r"%[a-zA-Z]",  # format string
]

# Commands that traditionally use slash prefix in modern interfaces
SLASH_COMMANDS = {"help", "who", "quit", "look", "go", "say", "me", "pose", "alias", "aliases", "unalias"}
