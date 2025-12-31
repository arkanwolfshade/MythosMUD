"""
Combat command factory methods.

This module contains factory methods for combat-related commands:
attack, punch, kick, strike.
"""

from ..models.command import (
    AttackCommand,
    KickCommand,
    PunchCommand,
    StrikeCommand,
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
