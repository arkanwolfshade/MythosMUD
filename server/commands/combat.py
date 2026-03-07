"""
Combat command handlers for the MUD.

This module re-exports combat command handler, loader, and helpers so that
existing imports (e.g. from server.commands.combat import handle_attack_command)
continue to work. Implementation is split across combat_helpers, combat_handler,
combat_loader, combat_attack, combat_flee, and combat_taunt to keep file nloc under 500.
"""

from server.commands.combat_handler import CombatCommandHandler
from server.commands.combat_helpers import (
    FleePreconditionError,
    _format_combat_status,
    _get_combat_target,
)
from server.commands.combat_loader import (
    get_combat_command_handler,
    handle_attack_command,
    handle_flee_command,
    handle_kick_command,
    handle_punch_command,
    handle_strike_command,
    handle_taunt_command,
)

__all__ = [
    "CombatCommandHandler",
    "FleePreconditionError",
    "get_combat_command_handler",
    "handle_attack_command",
    "handle_flee_command",
    "handle_kick_command",
    "handle_punch_command",
    "handle_strike_command",
    "handle_taunt_command",
    "_format_combat_status",
    "_get_combat_target",
]
