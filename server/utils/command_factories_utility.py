"""
Utility command factory methods.

This module contains factory methods for utility commands:
alias, aliases, unalias, help, npc, summon, teleport, goto, shutdown, learn.
"""

from typing import Literal, cast

from ..exceptions import ValidationError as MythosValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..models.command import (
    AliasCommand,
    AliasesCommand,
    CastCommand,
    Direction,
    GotoCommand,
    HelpCommand,
    LearnCommand,
    NPCCommand,
    ShutdownCommand,
    SpellCommand,
    SpellsCommand,
    SummonCommand,
    TeleportCommand,
    UnaliasCommand,
)
from .enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


class UtilityCommandFactory:
    """Factory class for creating utility command objects."""

    @staticmethod
    def create_alias_command(args: list[str]) -> AliasCommand:
        """Create AliasCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Alias command requires an alias name", context=context, logger_name=__name__
            )

        alias_name = args[0]
        command = " ".join(args[1:]) if len(args) > 1 else None

        return AliasCommand(alias_name=alias_name, command=command)

    @staticmethod
    def create_aliases_command(args: list[str]) -> AliasesCommand:
        """Create AliasesCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Aliases command takes no arguments", context=context, logger_name=__name__
            )
        return AliasesCommand()

    @staticmethod
    def create_unalias_command(args: list[str]) -> UnaliasCommand:
        """Create UnaliasCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Unalias command requires an alias name", context=context, logger_name=__name__
            )
        if len(args) > 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError, "Unalias command takes only one argument", context=context, logger_name=__name__
            )

        return UnaliasCommand(alias_name=args[0])

    @staticmethod
    def create_help_command(args: list[str]) -> HelpCommand:
        """Create HelpCommand from arguments."""
        topic = args[0] if args else None
        return HelpCommand(topic=topic)

    @staticmethod
    def create_npc_command(args: list[str]) -> NPCCommand:
        """Create NPCCommand from arguments."""
        # NPC command can be called with or without subcommand
        # If no args, subcommand is None (will show help)
        # If args, first arg is subcommand, rest are args
        if not args:
            return NPCCommand(subcommand=None, args=[])

        subcommand = args[0].lower()
        remaining_args = args[1:]

        return NPCCommand(subcommand=subcommand, args=remaining_args)

    @staticmethod
    def create_summon_command(args: list[str]) -> SummonCommand:
        """Create SummonCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: summon <prototype_id> [quantity] [item|npc]",
                context=context,
                logger_name=__name__,
            )

        prototype_id = args[0]
        quantity: int | None = None
        target_type: Literal["item", "npc"] | None = None

        for token in args[1:]:
            lowered = token.lower()
            if lowered in {"item", "npc"} and target_type is None:
                target_type = cast(Literal["item", "npc"], lowered)
                continue
            if quantity is None:
                try:
                    parsed_quantity = int(token)
                except ValueError as error:
                    context = create_error_context()
                    context.metadata = {"args": args, "invalid_token": token}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Usage: summon <prototype_id> [quantity] [item|npc]",
                        context=context,
                        logger_name=__name__,
                        error=error,
                    )
                if parsed_quantity <= 0:
                    context = create_error_context()
                    context.metadata = {"args": args, "invalid_quantity": parsed_quantity}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Summon quantity must be a positive number.",
                        context=context,
                        logger_name=__name__,
                    )
                quantity = parsed_quantity
                continue

            # Extra positional argument that we don't recognise.
            context = create_error_context()
            context.metadata = {"args": args, "unexpected_token": token}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: summon <prototype_id> [quantity] [item|npc]",
                context=context,
                logger_name=__name__,
            )

        return SummonCommand(
            prototype_id=prototype_id,
            quantity=quantity if quantity is not None else 1,
            target_type=target_type if target_type is not None else "item",
        )

    @staticmethod
    def create_teleport_command(args: list[str]) -> TeleportCommand:
        """Create TeleportCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Teleport command requires a player name", context=context, logger_name=__name__
            )

        player_name = args[0]
        direction = None

        if len(args) > 1:
            if len(args) > 2:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Teleport command accepts at most one direction argument",
                    context=context,
                    logger_name=__name__,
                )
            raw_direction = args[1].lower()
            try:
                direction = Direction(raw_direction)
            except ValueError as error:
                context = create_error_context()
                context.metadata = {"args": args, "direction": raw_direction}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Teleport command direction must be a valid Mythos cardinal or intercardinal direction",
                    context=context,
                    logger_name=__name__,
                    error=error,
                )

        return TeleportCommand(player_name=player_name, direction=direction)

    @staticmethod
    def create_goto_command(args: list[str]) -> GotoCommand:
        """Create GotoCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Goto command requires a player name", context=context, logger_name=__name__
            )
        player_name = args[0]
        return GotoCommand(player_name=player_name)

    @staticmethod
    def create_shutdown_command(args: list[str]) -> ShutdownCommand:
        """
        Create ShutdownCommand from arguments.

        Args can be:
        - Empty: Default 10 second countdown
        - Number: Countdown duration in seconds
        - "cancel": Cancel active shutdown
        """
        return ShutdownCommand(args=args)

    @staticmethod
    def create_cast_command(args: list[str]) -> CastCommand:
        """Create CastCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Cast command requires a spell name", context=context, logger_name=__name__
            )
        # Join all arguments as spell name to support multi-word spell names (e.g., "basic heal")
        # Target parsing can be added later with a separator syntax if needed
        spell_name = " ".join(args)
        target = None
        return CastCommand(spell_name=spell_name, target=target)

    @staticmethod
    def create_spell_command(args: list[str]) -> SpellCommand:
        """Create SpellCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Spell command requires a spell name", context=context, logger_name=__name__
            )
        spell_name = " ".join(args)  # Allow multi-word spell names
        return SpellCommand(spell_name=spell_name)

    @staticmethod
    def create_spells_command(args: list[str]) -> SpellsCommand:
        """Create SpellsCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Spells command takes no arguments", context=context, logger_name=__name__
            )
        return SpellsCommand()

    @staticmethod
    def create_learn_command(args: list[str]) -> LearnCommand:
        """Create LearnCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Learn command requires a spell name", context=context, logger_name=__name__
            )
        spell_name = " ".join(args)  # Allow multi-word spell names
        return LearnCommand(spell_name=spell_name)
