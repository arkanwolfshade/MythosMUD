"""
Command processing system for MythosMUD.

This package provides the command processing pipeline and individual
command handlers for the MythosMUD game system.
"""

from .admin_commands import (
    handle_add_admin_command,
    handle_goto_command,
    handle_mute_command,
    handle_mute_global_command,
    handle_mutes_command,
    handle_teleport_command,
    handle_unmute_command,
    handle_unmute_global_command,
)
from .admin_shutdown_command import handle_shutdown_command
from .admin_summon_command import handle_summon_command
from .alias_commands import (
    handle_alias_command,
    handle_aliases_command,
    handle_unalias_command,
)
from .command_service import CommandService
from .communication_commands import handle_me_command, handle_pose_command, handle_say_command
from .exploration_commands import handle_go_command, handle_look_command
from .inventory_commands import handle_inventory_command
from .npc_admin_commands import handle_npc_command
from .position_commands import handle_lie_command, handle_sit_command, handle_stand_command
from .rescue_commands import handle_ground_command
from .system_commands import handle_help_command
from .utility_commands import (
    handle_emote_command,
    handle_quit_command,
    handle_status_command,
    handle_who_command,
    handle_whoami_command,
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
    "handle_summon_command",
    # Admin teleport commands
    "handle_teleport_command",
    "handle_goto_command",
    # Admin server management commands
    "handle_shutdown_command",
    # Utility commands
    "handle_who_command",
    "handle_whoami_command",
    "handle_quit_command",
    "handle_status_command",
    "handle_inventory_command",
    # Position commands
    "handle_sit_command",
    "handle_stand_command",
    "handle_lie_command",
    # Rescue commands
    "handle_ground_command",
    # NPC Admin commands
    "handle_npc_command",
]
