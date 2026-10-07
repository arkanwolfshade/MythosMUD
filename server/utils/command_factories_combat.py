"""
Combat command factory methods.

This module contains factory methods for combat-related commands:
attack, punch, kick, strike, flee.
"""

from ..models.command import (
    AssistCommand,
    AttackCommand,
    FleeCommand,
    KickCommand,
    ProtectCommand,
    PunchCommand,
    StrikeCommand,
    TauntCommand,
)
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CombatCommandFactory:
    """Factory class for creating combat command objects."""

    @staticmethod
    def create_attack_command(args: list[str]) -> AttackCommand:
        """Create AttackCommand from arguments."""
        # Allow attack commands without targets - let the combat handler validate
        target = " ".join(args) if args else None
        return AttackCommand(target=target)

    @staticmethod
    def create_punch_command(args: list[str]) -> PunchCommand:
        """Create PunchCommand from arguments."""
        # Allow punch commands without targets - let the combat handler validate
        target = " ".join(args) if args else None
        return PunchCommand(target=target)

    @staticmethod
    def create_kick_command(args: list[str]) -> KickCommand:
        """Create KickCommand from arguments."""
        # Allow kick commands without targets - let the combat handler validate
        target = " ".join(args) if args else None
        return KickCommand(target=target)

    @staticmethod
    def create_strike_command(args: list[str]) -> StrikeCommand:
        """Create StrikeCommand from arguments."""
        # Allow strike commands without targets - let the combat handler validate
        target = " ".join(args) if args else None
        return StrikeCommand(target=target)

    @staticmethod
    def create_flee_command(_args: list[str]) -> FleeCommand:
        """Create FleeCommand (no arguments)."""
        return FleeCommand()

    @staticmethod
    def create_taunt_command(args: list[str]) -> TauntCommand:
        """Create TauntCommand from arguments (target NPC name)."""
        target = " ".join(args) if args else None
        return TauntCommand(target=target)

    @staticmethod
    def create_assist_command(args: list[str]) -> AssistCommand:
        """Create AssistCommand from arguments (player name, or none for the party leader)."""
        target = " ".join(args) if args else None
        return AssistCommand(target=target)

    @staticmethod
    def create_protect_command(args: list[str]) -> ProtectCommand:
        """Create ProtectCommand from arguments (the player to cover)."""
        target = " ".join(args) if args else None
        return ProtectCommand(target=target)
