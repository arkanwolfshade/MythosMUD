"""
Moderation command factory methods.

This module contains factory methods for admin and moderation commands:
mute, unmute, mute_global, unmute_global, add_admin, admin, mutes.
"""

from ..exceptions import ValidationError as MythosValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..models.command import (
    AddAdminCommand,
    AdminCommand,
    MuteCommand,
    MuteGlobalCommand,
    MutesCommand,
    UnmuteCommand,
    UnmuteGlobalCommand,
)
from .enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


class ModerationCommandFactory:
    """Factory class for creating moderation and admin command objects."""

    @staticmethod
    def create_mute_command(args: list[str]) -> MuteCommand:
        """Create MuteCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Mute command requires a player name", context=context, logger_name=__name__
            )

        player_name = args[0]
        duration_minutes = None
        reason = None

        # Parse optional duration
        if len(args) > 1:
            try:
                duration_minutes = int(args[1])
                # Reason is everything after duration
                if len(args) > 2:
                    reason = " ".join(args[2:])
            except ValueError:
                # If second arg isn't a number, treat everything after player name as reason
                reason = " ".join(args[1:])

        return MuteCommand(player_name=player_name, duration_minutes=duration_minutes, reason=reason)

    @staticmethod
    def create_unmute_command(args: list[str]) -> UnmuteCommand:
        """Create UnmuteCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Unmute command requires a player name", context=context, logger_name=__name__
            )
        if len(args) > 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError, "Unmute command takes only one argument", context=context, logger_name=__name__
            )

        return UnmuteCommand(player_name=args[0])

    @staticmethod
    def create_mute_global_command(args: list[str]) -> MuteGlobalCommand:
        """Create MuteGlobalCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Mute_global command requires a player name",
                context=context,
                logger_name=__name__,
            )

        player_name = args[0]
        duration_minutes = None
        reason = None

        # Parse optional duration
        if len(args) > 1:
            try:
                duration_minutes = int(args[1])
                # Reason is everything after duration
                if len(args) > 2:
                    reason = " ".join(args[2:])
            except ValueError:
                # If second arg isn't a number, treat everything after player name as reason
                reason = " ".join(args[1:])

        return MuteGlobalCommand(player_name=player_name, duration_minutes=duration_minutes, reason=reason)

    @staticmethod
    def create_unmute_global_command(args: list[str]) -> UnmuteGlobalCommand:
        """Create UnmuteGlobalCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Unmute_global command requires a player name",
                context=context,
                logger_name=__name__,
            )
        if len(args) > 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError,
                "Unmute_global command takes only one argument",
                context=context,
                logger_name=__name__,
            )

        return UnmuteGlobalCommand(player_name=args[0])

    @staticmethod
    def create_add_admin_command(args: list[str]) -> AddAdminCommand:
        """Create AddAdminCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Add_admin command requires a player name", context=context, logger_name=__name__
            )
        if len(args) > 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError,
                "Add_admin command takes only one argument",
                context=context,
                logger_name=__name__,
            )

        return AddAdminCommand(player_name=args[0])

    @staticmethod
    def create_admin_command(args: list[str]) -> AdminCommand:
        """Create AdminCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Admin command requires a subcommand", context=context, logger_name=__name__
            )

        subcommand = args[0].lower()
        remaining_args = args[1:]

        if subcommand == "status" and remaining_args:
            context = create_error_context()
            context.metadata = {"args": args, "subcommand": subcommand}
            log_and_raise_enhanced(
                MythosValidationError,
                "Admin status command does not accept additional arguments",
                context=context,
                logger_name=__name__,
            )

        return AdminCommand(subcommand=subcommand, args=remaining_args)

    @staticmethod
    def create_mutes_command(args: list[str]) -> MutesCommand:
        """Create MutesCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Mutes command takes no arguments", context=context, logger_name=__name__
            )
        return MutesCommand()
