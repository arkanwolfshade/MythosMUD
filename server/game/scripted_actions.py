"""The single runner for scripted actions (dialogue node actions, container on_put).

The vocabulary lives in ``schemas.scripted_actions``. Actions run in order; one that fails is logged and skipped so a
broken quest store cannot strand a player mid-scene.
"""

from __future__ import annotations

import uuid
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from ..models.player import Player
from ..schemas.scripted_actions import (
    ApplyEffectAction,
    CorruptionAtLeastAction,
    NarrateAction,
    QuestActivityAction,
    ScriptedAction,
    StartQuestAction,
)
from ..services.corruption_service import CorruptionPersistenceProtocol, CorruptionService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .chat_npc_system import deliver_personal_system

logger = get_logger(__name__)


class QuestActionService(Protocol):
    """The slice of QuestService the runner drives."""

    async def start_quest(self, player_id: uuid.UUID, quest_id: str) -> dict[str, object]:
        """Start a quest for the player."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    async def record_complete_activity(self, player_id: uuid.UUID, activity_target: str) -> None:
        """Record a complete_activity event."""


@dataclass(frozen=True)
class ScriptedActionContext:
    """Who the script acts on and the services it may touch."""

    player: Player
    persistence: CorruptionPersistenceProtocol
    quest_service: QuestActionService | None = None


async def _apply_effect(action: ApplyEffectAction, ctx: ScriptedActionContext) -> None:
    effects = ctx.player.get_status_effects()
    effects.append(dict(action.effect))
    ctx.player.set_status_effects(effects)
    await ctx.persistence.save_player(ctx.player)


async def _corruption_at_least(action: CorruptionAtLeastAction, ctx: ScriptedActionContext) -> None:
    current = coerce_int(ctx.player.get_stats().get("corruption", 0), default=0)
    if current >= action.value:
        return
    result = await CorruptionService(ctx.persistence).apply_corruption_adjustment(
        uuid.UUID(str(ctx.player.player_id)), action.value - current, reason_code=action.reason
    )
    # The service edits and saves its own copy of the player; mirror the new value onto ours so a later save
    # (apply_effect) does not write the old corruption back.
    stats = ctx.player.get_stats()
    stats["corruption"] = result.new_value
    ctx.player.set_stats(stats)


async def _run_one(action: ScriptedAction, ctx: ScriptedActionContext) -> None:
    player_id = uuid.UUID(str(ctx.player.player_id))
    match action:
        case NarrateAction():
            _ = await deliver_personal_system(player_id, action.text)
        case ApplyEffectAction():
            await _apply_effect(action, ctx)
        case CorruptionAtLeastAction():
            await _corruption_at_least(action, ctx)
        case StartQuestAction():
            if ctx.quest_service is not None:
                _ = await ctx.quest_service.start_quest(player_id, action.quest_id)
        case QuestActivityAction():
            if ctx.quest_service is not None:
                await ctx.quest_service.record_complete_activity(player_id, action.target)


async def run_scripted_actions(actions: Sequence[ScriptedAction], ctx: ScriptedActionContext) -> None:
    """Run ``actions`` in order against ``ctx.player``; a failing action is logged and skipped."""
    for action in actions:
        try:
            await _run_one(action, ctx)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: one bad action must not strand the scene
            logger.error("Scripted action failed", action_type=action.type, error=str(e))
