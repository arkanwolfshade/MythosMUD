"""
Command processing system for MythosMUD.

This package provides the command processing pipeline and individual
command handlers for the MythosMUD game system.
"""

from .alias_commands import (
    handle_alias_command,
    handle_aliases_command,
    handle_unalias_command,
)
from .command_service import CommandService
from .communication_commands import handle_me_command, handle_pose_command, handle_say_command
from .exploration_commands import handle_go_command, handle_look_command
from .system_commands import handle_help_command

__all__ = [
    "CommandService",
    "handle_alias_command",
    "handle_aliases_command",
    "handle_unalias_command",
    "handle_look_command",
    "handle_go_command",
    "handle_say_command",
    "handle_me_command",
    "handle_pose_command",
    "handle_help_command",
]
