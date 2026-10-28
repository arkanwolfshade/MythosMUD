"""cmd_<name> quest activity: a command typed inside an instance counts toward quest goals.

Instanced content teaches by doing ("type look", "put the amulet in the coffin"); quests express that as a
``complete_activity`` goal whose target is ``cmd_<command>``. Only players inside an instance are recorded, and nothing
is looked up while no instance is live, so the rest of the world pays nothing for it.

ponytail: while some instance is live, every command costs one extra player read; cache the player's room if that shows
up in profiling.
"""

from __future__ import annotations

import uuid
from typing import Protocol, cast

from ..constants.instance_rooms import is_instance_room_id
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .communication_commands_support import app_from_request

logger = get_logger(__name__)

CMD_ACTIVITY_PREFIX = "cmd_"


class _PlayerLookup(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    async def get_player_by_name(self, name: str) -> object | None:
        """The player named ``name``, or None."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class _QuestActivity(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    async def record_complete_activity(self, player_id: uuid.UUID, activity_target: str) -> None:
        """Record a complete_activity event for the player."""


class _InstanceIds(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    def list_instance_ids(self) -> list[str]:
        """Ids of every live instance."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class _Services(Protocol):
    """The slice of the app container this hook reads."""

    async_persistence: _PlayerLookup | None
    quest_service: _QuestActivity | None
    instance_manager: _InstanceIds | None


def _services(request: object | None) -> _Services | None:
    state = cast(object | None, getattr(app_from_request(request), "state", None))
    return cast(_Services | None, getattr(state, "container", None))


async def record_command_activity(command: str, player_name: str, request: object | None) -> None:
    """Record ``cmd_<command>`` for the player if they are inside an instance. Never raises: it must not break a command."""
    try:
        services = _services(request)
        if services is None or services.async_persistence is None or services.quest_service is None:
            return
        if services.instance_manager is None or not services.instance_manager.list_instance_ids():
            return
        player = cast(Player | None, await services.async_persistence.get_player_by_name(player_name))
        if player is None or not is_instance_room_id(str(player.current_room_id)):
            return
        player_id = uuid.UUID(str(player.player_id))
        await services.quest_service.record_complete_activity(player_id, f"{CMD_ACTIVITY_PREFIX}{command}")
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: quest bookkeeping must never break the command that triggered it
        logger.warning("Command quest activity failed", command=command, player=player_name, error=str(e))
