"""
Exploration commands for MythosMUD.

This module contains handlers for exploration-related commands like look and go.
This is a thin wrapper that imports and re-exports command handlers from separate modules.
"""

# Import go command handler
from .go_command import handle_go_command

# Import look command handler
from .look_command import handle_look_command

# Re-export public functions for backward compatibility
__all__ = ["handle_look_command", "handle_go_command"]
