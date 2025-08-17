"""
Help system for MythosMUD.

This package provides help content and command documentation
for the MythosMUD game system.
"""

from .help_content import COMMANDS, get_help_content

__all__ = [
    "COMMANDS",
    "get_help_content",
]
