"""
Command models for MythosMUD using Pydantic for validation.

This module provides type-safe command models with comprehensive validation
to prevent command injection and ensure data integrity.

This module re-exports all command models from specialized submodules to maintain
backward compatibility while keeping the codebase organized.
"""

# Import base classes and enums
# Import admin commands
from .command_admin import GotoCommand, NPCCommand, ShutdownCommand, SummonCommand, TeleportCommand

# Import alias commands
from .command_alias import AliasCommand, AliasesCommand, UnaliasCommand
from .command_base import BaseCommand, CommandType, Direction

# Import channel commands
from .command_channel import ChannelCommand

# Import combat commands
from .command_combat import AttackCommand, KickCommand, PunchCommand, StrikeCommand

# Import communication commands
from .command_communication import (
    EmoteCommand,
    LocalCommand,
    MeCommand,
    PoseCommand,
    ReplyCommand,
    SayCommand,
    SystemCommand,
    WhisperCommand,
)

# Import exploration commands
from .command_exploration import GoCommand, LookCommand

# Import inventory commands
from .command_inventory import (
    DropCommand,
    EquipCommand,
    GetCommand,
    InventoryCommand,
    PickupCommand,
    PutCommand,
    UnequipCommand,
)

# Import magic commands
from .command_magic import CastCommand, LearnCommand, SpellCommand, SpellsCommand

# Import moderation commands
from .command_moderation import (
    AddAdminCommand,
    AdminCommand,
    MuteCommand,
    MuteGlobalCommand,
    MutesCommand,
    UnmuteCommand,
    UnmuteGlobalCommand,
)

# Import player state commands
from .command_player_state import (
    GroundCommand,
    LieCommand,
    LogoutCommand,
    QuitCommand,
    RestCommand,
    SitCommand,
    StandCommand,
)

# Import utility commands
from .command_utility import HelpCommand, StatusCommand, TimeCommand, WhoamiCommand, WhoCommand

# Re-export all imports for backward compatibility
__all__ = [
    # Base classes and enums
    "BaseCommand",
    "CommandType",
    "Direction",
    # Channel commands
    "ChannelCommand",
    # Communication commands
    "SayCommand",
    "LocalCommand",
    "SystemCommand",
    "EmoteCommand",
    "MeCommand",
    "PoseCommand",
    "WhisperCommand",
    "ReplyCommand",
    # Exploration commands
    "LookCommand",
    "GoCommand",
    # Alias commands
    "AliasCommand",
    "AliasesCommand",
    "UnaliasCommand",
    # Moderation commands
    "MuteCommand",
    "UnmuteCommand",
    "MuteGlobalCommand",
    "UnmuteGlobalCommand",
    "AddAdminCommand",
    "MutesCommand",
    "AdminCommand",
    # Admin commands
    "NPCCommand",
    "SummonCommand",
    "TeleportCommand",
    "GotoCommand",
    # Utility commands
    "WhoCommand",
    "StatusCommand",
    "TimeCommand",
    "WhoamiCommand",
    "HelpCommand",
    # Inventory commands
    "InventoryCommand",
    "PickupCommand",
    "DropCommand",
    "PutCommand",
    "GetCommand",
    "EquipCommand",
    "UnequipCommand",
    # Player state commands
    "QuitCommand",
    "LogoutCommand",
    "SitCommand",
    "StandCommand",
    "LieCommand",
    "RestCommand",
    "GroundCommand",
    # System commands
    "ShutdownCommand",
    # Combat commands
    "AttackCommand",
    "PunchCommand",
    "KickCommand",
    "StrikeCommand",
    # Magic commands
    "CastCommand",
    "SpellCommand",
    "SpellsCommand",
    "LearnCommand",
    # Union type
    "Command",
]

# Union type for all commands
Command = (
    LookCommand
    | GoCommand
    | SayCommand
    | LocalCommand
    | SystemCommand
    | EmoteCommand
    | MeCommand
    | PoseCommand
    | AliasCommand
    | AliasesCommand
    | UnaliasCommand
    | HelpCommand
    | MuteCommand
    | UnmuteCommand
    | MuteGlobalCommand
    | UnmuteGlobalCommand
    | AddAdminCommand
    | MutesCommand
    | TeleportCommand
    | GotoCommand
    | WhoCommand
    | StatusCommand
    | InventoryCommand
    | PickupCommand
    | DropCommand
    | PutCommand
    | GetCommand
    | EquipCommand
    | UnequipCommand
    | QuitCommand
    | LogoutCommand
    | SitCommand
    | StandCommand
    | LieCommand
    | RestCommand
    | GroundCommand
    | ShutdownCommand
    | ChannelCommand
    | WhisperCommand
    | ReplyCommand
    | AttackCommand
    | PunchCommand
    | KickCommand
    | StrikeCommand
    | CastCommand
    | SpellCommand
    | SpellsCommand
    | LearnCommand
    | AdminCommand
    | NPCCommand
    | SummonCommand
    | TimeCommand
    | WhoamiCommand
)
