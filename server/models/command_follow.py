"""
Follow command models for MythosMUD.

This module provides command models for follow, unfollow, and following.
"""

from typing import Literal

from pydantic import Field

from .command_base import BaseCommand, CommandType


class FollowCommand(BaseCommand):
    """Command to follow a player or NPC in the same room."""

    command_type: Literal[CommandType.FOLLOW] = CommandType.FOLLOW
    target: str = Field(..., min_length=1, description="Name or ID of player or NPC to follow")


class UnfollowCommand(BaseCommand):
    """Command to stop following the current target."""

    command_type: Literal[CommandType.UNFOLLOW] = CommandType.UNFOLLOW


class FollowingCommand(BaseCommand):
    """Command to show who you are following and who is following you."""

    command_type: Literal[CommandType.FOLLOWING] = CommandType.FOLLOWING
