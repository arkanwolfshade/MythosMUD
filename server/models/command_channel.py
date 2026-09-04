"""
Channel management command models for MythosMUD.

This module provides command models for channel management commands.
"""

from typing import Literal

from pydantic import Field

from .command_base import BaseCommand, CommandType


class ChannelCommand(BaseCommand):
    """Command for managing channel preferences (switch channel or set default)."""

    command_type: Literal[CommandType.CHANNEL] = CommandType.CHANNEL
    channel: str = Field(..., min_length=1, max_length=50, description="Channel name or 'default'")
    action: str | None = Field(
        None, description="Action: 'default' to set as default channel, or channel name to switch to"
    )
