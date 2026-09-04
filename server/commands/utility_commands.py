"""
Utility commands for MythosMUD.

This module contains handlers for utility commands like who, quit, and other system utilities.

NOTE: This module now re-exports handlers from specialized modules to maintain backward compatibility.
New code should import directly from the specialized modules:
- who_commands: handle_who_command and related helpers
- logout_commands: handle_quit_command, handle_logout_command
- status_commands: handle_status_command, handle_whoami_command
- time_commands: handle_time_command
- emote_commands: handle_emote_command
"""

# Re-export all command handlers for backward compatibility
from .emote_commands import handle_emote_command
from .logout_commands import handle_logout_command, handle_quit_command
from .status_commands import handle_status_command, handle_whoami_command
from .time_commands import handle_time_command
from .who_commands import (
    filter_players_by_name,
    format_player_entry,
    format_player_location,
    handle_who_command,
)

__all__ = [
    # Command handlers
    "handle_who_command",
    "handle_quit_command",
    "handle_logout_command",
    "handle_status_command",
    "handle_whoami_command",
    "handle_time_command",
    "handle_emote_command",
    # Helper functions (used by tests)
    "filter_players_by_name",
    "format_player_entry",
    "format_player_location",
]
