"""
Party command model for MythosMUD.

Single command 'party' with subcommands: invite, leave, kick, list; no subcommand = status.
"""

from typing import Literal

from pydantic import Field

from .command_base import BaseCommand, CommandType


class PartyCommand(BaseCommand):
    """
    Party management: party [invite|leave|kick|list] [target].

    No subcommand = show party status. invite and kick require a target name.
    """

    command_type: Literal[CommandType.PARTY] = CommandType.PARTY
    subcommand: Literal["", "invite", "leave", "kick", "list"] = Field(
        default="",
        description="Subcommand: invite, leave, kick, list, or empty for status/chat",
    )
    target: str | None = Field(default=None, description="Target player name for invite/kick")
    message: str | None = Field(default=None, description="Party chat message when no subcommand (e.g. party Hello)")
