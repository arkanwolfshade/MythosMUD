"""
Player state command factory methods.

This module contains factory methods for player state and information commands:
status, time, whoami, who, quit, logout.
"""

from ..exceptions import ValidationError as MythosValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..models.command import (
    LogoutCommand,
    QuitCommand,
    StatusCommand,
    TimeCommand,
    WhoamiCommand,
    WhoCommand,
)
from .enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


class PlayerStateCommandFactory:
    """Factory class for creating player state command objects."""

    @staticmethod
    def create_status_command(args: list[str]) -> StatusCommand:
        """Create StatusCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Status command takes no arguments", context=context, logger_name=__name__
            )
        return StatusCommand()

    @staticmethod
    def create_time_command(args: list[str]) -> TimeCommand:
        """Create TimeCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Time command takes no arguments", context=context, logger_name=__name__
            )
        return TimeCommand()

    @staticmethod
    def create_whoami_command(args: list[str]) -> WhoamiCommand:
        """Create WhoamiCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Whoami command takes no arguments", context=context, logger_name=__name__
            )
        return WhoamiCommand()

    @staticmethod
    def create_who_command(args: list[str]) -> WhoCommand:
        """Create WhoCommand from arguments."""
        filter_name = args[0] if args else None
        return WhoCommand(filter_name=filter_name)

    @staticmethod
    def create_quit_command(args: list[str]) -> QuitCommand:
        """Create QuitCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Quit command takes no arguments", context=context, logger_name=__name__
            )
        return QuitCommand()

    @staticmethod
    def create_logout_command(_args: list[str]) -> LogoutCommand:
        """Create LogoutCommand from arguments."""
        # Logout command ignores arguments (like quit command)
        # This allows for commands like "logout force now" to work
        return LogoutCommand()
