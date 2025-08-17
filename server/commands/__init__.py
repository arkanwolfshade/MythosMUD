"""
Command processing system for MythosMUD.

This package provides the command processing pipeline and individual
command handlers for the MythosMUD game system.
"""

from .admin_commands import (
    handle_add_admin_command,
    handle_mute_command,
    handle_mute_global_command,
    handle_mutes_command,
    handle_unmute_command,
    handle_unmute_global_command,
)
from .alias_commands import (
    handle_alias_command,
    handle_aliases_command,
    handle_unalias_command,
)
from .command_service import CommandService
from .communication_commands import handle_me_command, handle_pose_command, handle_say_command
from .exploration_commands import handle_go_command, handle_look_command
from .system_commands import handle_help_command
from .utility_commands import (
    handle_emote_command,
    handle_inventory_command,
    handle_quit_command,
    handle_status_command,
    handle_who_command,
)

__all__ = [
    "CommandService",
    # System commands
    "handle_help_command",
    # Alias commands
    "handle_alias_command",
    "handle_aliases_command",
    "handle_unalias_command",
    # Exploration commands
    "handle_look_command",
    "handle_go_command",
    # Communication commands
    "handle_say_command",
    "handle_me_command",
    "handle_pose_command",
    "handle_emote_command",
    # Administrative commands
    "handle_mute_command",
    "handle_unmute_command",
    "handle_mute_global_command",
    "handle_unmute_global_command",
    "handle_add_admin_command",
    "handle_mutes_command",
    # Utility commands
    "handle_who_command",
    "handle_quit_command",
    "handle_status_command",
    "handle_inventory_command",
]
