"""
Communication command factory methods.

This module contains factory methods for communication-related commands:
say, local, system, emote, me, pose, whisper, reply.
"""

from ..exceptions import ValidationError as MythosValidationError
from ..models.command import (
    ChannelCommand,
    EmoteCommand,
    LocalCommand,
    MeCommand,
    PoseCommand,
    ReplyCommand,
    SayCommand,
    SystemCommand,
    WhisperCommand,
)
from ..structured_logging.enhanced_logging_config import get_logger
from .enhanced_error_logging import log_and_raise_enhanced

logger = get_logger(__name__)


class CommunicationCommandFactory:
    """Factory class for creating communication command objects."""

    @staticmethod
    def create_say_command(args: list[str]) -> SayCommand:
        """Create SayCommand from arguments."""
        if not args:
            log_and_raise_enhanced(
                MythosValidationError, "Say command requires a message", args=args, logger_name=__name__
            )
        message = " ".join(args)
        return SayCommand(message=message)

    @staticmethod
    def create_local_command(
        args: list[str],
        raw_command: str | None = None,
        original_command: str | None = None,
    ) -> LocalCommand:
        """Create LocalCommand from arguments."""
        if not args:
            logger.debug(
                "Local command invoked with empty args (trace empty local from client/e2e)",
                args=args,
                raw_command=raw_command,
                original_command=original_command,
            )
            log_and_raise_enhanced(
                MythosValidationError,
                "You must provide a message to send locally",
                args=args,
                logger_name=__name__,
            )
        message = " ".join(args)
        if len(message) > 500:
            log_and_raise_enhanced(
                MythosValidationError,
                "Local message too long",
                args=args,
                message_length=len(message),
                logger_name=__name__,
            )
        return LocalCommand(message=message)

    @staticmethod
    def create_system_command(args: list[str]) -> SystemCommand:
        """Create SystemCommand from arguments."""
        if not args:
            log_and_raise_enhanced(
                MythosValidationError, "System command requires a message", args=args, logger_name=__name__
            )
        message = " ".join(args)
        return SystemCommand(message=message)

    @staticmethod
    def create_emote_command(args: list[str]) -> EmoteCommand:
        """Create EmoteCommand from arguments."""
        if not args:
            log_and_raise_enhanced(
                MythosValidationError, "Emote command requires an action", args=args, logger_name=__name__
            )
        action = " ".join(args)
        return EmoteCommand(action=action)

    @staticmethod
    def create_me_command(args: list[str]) -> MeCommand:
        """Create MeCommand from arguments."""
        if not args:
            log_and_raise_enhanced(
                MythosValidationError, "Me command requires an action", args=args, logger_name=__name__
            )
        action = " ".join(args)
        return MeCommand(action=action)

    @staticmethod
    def create_pose_command(args: list[str]) -> PoseCommand:
        """Create PoseCommand from arguments."""
        pose = " ".join(args) if args else None
        return PoseCommand(pose=pose)

    @staticmethod
    def create_whisper_command(args: list[str]) -> WhisperCommand:
        """Create a WhisperCommand from parsed arguments."""
        # Check if target is provided
        if len(args) < 1:
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: whisper <player> <message>",
                args=args,
                arg_count=len(args),
                logger_name=__name__,
            )

        target = args[0]
        message = " ".join(args[1:]) if len(args) > 1 else ""

        # Check if message is provided (not empty or whitespace-only)
        if not message.strip():
            log_and_raise_enhanced(
                MythosValidationError,
                "You must provide a message to whisper. Usage: whisper <player> <message>",
                args=args,
                target=target,
                logger_name=__name__,
            )

        if len(message) > 500:
            log_and_raise_enhanced(
                MythosValidationError,
                "Whisper message too long",
                args=args,
                message_length=len(message),
                logger_name=__name__,
            )

        return WhisperCommand(target=target, message=message)

    @staticmethod
    def create_reply_command(args: list[str]) -> ReplyCommand:
        """Create a ReplyCommand from parsed arguments."""
        if not args:
            log_and_raise_enhanced(MythosValidationError, "Usage: reply <message>", args=args, logger_name=__name__)

        message = " ".join(args)

        if not message.strip():
            log_and_raise_enhanced(MythosValidationError, "Usage: reply <message>", args=args, logger_name=__name__)

        return ReplyCommand(message=message)

    @staticmethod
    def create_channel_command(args: list[str]) -> ChannelCommand:
        """Create a ChannelCommand from parsed arguments."""
        if not args:
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: channel <channel_name> or channel default <channel_name>",
                args=args,
                logger_name=__name__,
            )

        channel = args[0].lower().strip()
        action = None

        # Handle "default" action: channel default <channel_name>
        if channel == "default":
            if len(args) < 2:
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Usage: channel default <channel_name>",
                    args=args,
                    logger_name=__name__,
                )
            action = args[1].lower().strip()

        return ChannelCommand(channel=channel, action=action)
