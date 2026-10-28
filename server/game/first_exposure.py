"""The First Exposure ending (ADR-028): what a tutorial delirium respawn leaves the player with.

Ending the tutorial is two steps, because the respawn commits through its own database session:

* ``apply_first_exposure_end_state`` runs inside that session: the instance-bound items (the amulet) are cleared,
  lucidity is restored to 70, health is restored, and they wake in the Recovery Ward.
* ``FirstExposureFinisher.finish`` runs after the commit: it raises corruption to its floor and starts the epilogue
  quest (data, run by the scripted-action runner), clears any instance-scoped effects (the drain), then flushes the
  instance. Corruption is written after the commit
  because ``restore_to_full_health`` rewrites the same ``stats`` column, and it must be a floor ("at least 1"), never
  "+1", so replay, restart and skip are idempotent.

Anyone not in the tutorial is untouched: ``apply_first_exposure_end_state`` does nothing without a
``tutorial_instance_id``.

A character can skip the tutorial at creation once some character on the account has finished it (#1081, ADR-028
D22/D24). ``account_completed_first_exposure`` is that check, and ``skip_first_exposure`` gives the new character the
same end state a finished run leaves.
"""

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable, Iterable, Mapping, Sequence
from typing import Protocol, cast

from ..constants.spawn_defaults import RECOVERY_WARD_ROOM_ID
from ..models.lucidity import PlayerLucidity
from ..models.player import Player
from ..schemas.scripted_actions import CorruptionAtLeastAction, ScriptedAction, StartQuestAction
from ..services.corruption_service import CorruptionPersistenceProtocol
from ..services.lucidity_service import resolve_tier
from ..structured_logging.enhanced_logging_config import get_logger
from .effect_store import clear_instance_scoped_effects
from .instance_state import reset_instance_scoped_state
from .scripted_actions import QuestActionService, ScriptedActionContext, run_scripted_actions

logger = get_logger(__name__)

EPILOGUE_QUEST_ID = "first_exposure_sanitarium"
RESTORED_LCD = 70
# Finishing the Below act (the amulet returned to the Owner) is finishing the tutorial: what earns the skip.
COMPLETION_QUEST_ID = "first_exposure_below"

FINISH_ACTIONS: tuple[ScriptedAction, ...] = (
    CorruptionAtLeastAction(value=1, reason="first_exposure"),
    StartQuestAction(quest_id=EPILOGUE_QUEST_ID),
)


class FinishPersistence(CorruptionPersistenceProtocol, Protocol):
    """Player persistence the finisher needs: what the corruption write needs, which also loads the player."""


class InstanceFlush(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """The slice of InstanceFlushService the finisher drives."""

    async def flush(self, instance_id: str) -> int:
        """Destroy one instance, banking what it held (instance-bound items are dropped)."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


FinishFirstExposure = Callable[[uuid.UUID, str], Awaitable[None]]


class QuestLogReader(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """The slice of QuestService the skip check reads."""

    async def get_quest_log(
        self, player_id: uuid.UUID, include_completed: bool = True
    ) -> Sequence[Mapping[str, object]]:
        """Quest log entries (quest_id, state, ...) for one character."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


async def account_completed_first_exposure(characters: Iterable[Player], quests: QuestLogReader) -> bool:
    """True if any of the account's characters (deleted ones included) has finished First Exposure."""
    for character in characters:
        log = await quests.get_quest_log(uuid.UUID(str(character.player_id)), include_completed=True)
        if any(entry.get("quest_id") == COMPLETION_QUEST_ID and entry.get("state") == "completed" for entry in log):
            return True
    return False


async def skip_first_exposure(
    player_id: uuid.UUID, persistence: FinishPersistence, quest_service: QuestActionService | None
) -> None:
    """Give a character created with the tutorial skipped the state a finished run leaves (ADR-028 D22/D24).

    The character is created in the Recovery Ward at full health. This adds the rest: lucidity 70 and Dr. Morgan's
    debrief pending (one session), then the same finish actions the ending runs (the corruption floor and the
    epilogue quest).
    """
    # Imported here: the database module pulls in the app's engine setup, which this module must not need to import.
    from ..database import get_async_session
    from ..services.debrief_service import mark_debrief_pending
    from ..services.lucidity_repository import LucidityRepository
    from ..services.lucidity_service import LucidityService

    async for session in get_async_session():
        lucidity = await LucidityRepository(session).get_or_create_player_lucidity(player_id)
        lucidity.current_lcd = RESTORED_LCD
        lucidity.current_tier = resolve_tier(RESTORED_LCD)
        await mark_debrief_pending(LucidityService(session), player_id)
        await session.commit()
    player = cast(Player | None, await persistence.get_player_by_id(player_id))
    if player is None:
        logger.warning("Tutorial skip: the new character could not be loaded", player_id=str(player_id))
        return
    await run_scripted_actions(FINISH_ACTIONS, ScriptedActionContext(player, persistence, quest_service))


def tutorial_instance_of(player: Player) -> str | None:
    """The tutorial instance the player is in (or the pending marker), or None when they are not in the tutorial."""
    raw = cast(object, player.tutorial_instance_id)
    return raw if isinstance(raw, str) and raw else None


def apply_first_exposure_end_state(player: Player, lucidity: PlayerLucidity) -> bool:
    """Leave a tutorial player whole and in the Recovery Ward; True if they were in the tutorial, else a no-op."""
    if tutorial_instance_of(player) is None:
        return False
    _ = reset_instance_scoped_state(player)
    lucidity.current_lcd = RESTORED_LCD
    lucidity.current_tier = resolve_tier(RESTORED_LCD)
    _ = player.restore_to_full_health()
    player.current_room_id = RECOVERY_WARD_ROOM_ID
    player.tutorial_instance_id = None
    return True


class FirstExposureFinisher:  # pylint: disable=too-few-public-methods  # Reason: one collaborator-driven operation
    """Everything the ending does after the respawn has committed."""

    _persistence: FinishPersistence
    _quest_service: QuestActionService | None
    _flush: InstanceFlush

    def __init__(
        self, persistence: FinishPersistence, quest_service: QuestActionService | None, flush: InstanceFlush
    ) -> None:
        self._persistence = persistence
        self._quest_service = quest_service
        self._flush = flush

    async def finish(self, player_id: uuid.UUID, instance_id: str) -> None:
        """Run the finish actions for the player, then flush their instance. Each step is isolated from the other."""
        try:
            player = cast(Player | None, await self._persistence.get_player_by_id(player_id))
            if player is not None:
                ctx = ScriptedActionContext(player, self._persistence, self._quest_service)
                await run_scripted_actions(FINISH_ACTIONS, ctx)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: the respawn already committed; a failed finish must not undo or hide it
            logger.error("First Exposure finish actions failed", player_id=str(player_id), error=str(e))
        try:
            # The drain ends itself at its floor; anything instance-scoped left over must not follow them out.
            _ = await clear_instance_scoped_effects(player_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: as above; the respawn already committed
            logger.error("First Exposure instance-scoped effect clear failed", player_id=str(player_id), error=str(e))
        try:
            _ = await self._flush.flush(instance_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: as above; a stuck instance is cleaned up at shutdown
            logger.error("First Exposure instance flush failed", instance_id=instance_id, error=str(e))


def make_first_exposure_finish(container: object) -> FinishFirstExposure:
    """A finish callable that resolves its services from the app container when called, not when built.

    The respawn service is constructed before the quest and flush services exist, so it is handed this lazily.
    """

    async def finish(player_id: uuid.UUID, instance_id: str) -> None:
        persistence = cast(FinishPersistence | None, getattr(container, "async_persistence", None))
        flush = cast(InstanceFlush | None, getattr(container, "instance_flush_service", None))
        if persistence is None or flush is None:
            logger.warning("First Exposure finish skipped: persistence or instance flush unavailable")
            return
        quests = cast(QuestActionService | None, getattr(container, "quest_service", None))
        await FirstExposureFinisher(persistence, quests, flush).finish(player_id, instance_id)

    return finish
