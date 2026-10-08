"""
Help system for MythosMUD.

This package provides help content and command documentation
for the MythosMUD game system.
"""

from .help_content import get_help_content, get_manual, load_help_docs

__all__ = [
    "get_help_content",
    "get_manual",
    "load_help_docs",
]
