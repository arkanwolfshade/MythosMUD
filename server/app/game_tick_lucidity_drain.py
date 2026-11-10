"""lucidity_drain_over_time: a status effect that pulls LCD down once per game second until it reaches a floor.

Content applies it as a plain effect dict (e.g. via the ``apply_effect`` scripted action); every field but ``type`` is
optional and validated by ``LucidityDrainParams``. There is no fixed duration on purpose: the rate never falls, so the
drain always reaches the floor (delirium fires when LCD crosses -10), which instanced content relies on when delirium
is the only way out. Each step goes through ``LucidityService``, so tiers, events, catatonia and delirium behave as for
any other LCD loss.

Content can also script the drain: ``narration`` lines and ``hallucinations`` beats fire once, at the second they name,
for the draining player only. A hallucination beat calls the same server-authoritative handlers the passive flux uses
(#714, ADR-024), with the tier resolved from the player's LCD at that moment, so what the player sees matches their
state. Beats exist because passive flux checks run every 60 s, which rarely lands inside a ~85 s drain.
"""

# pylint: disable=too-few-public-methods  # Reason: Pydantic models; validators are the behavior

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel, Field, ValidationError

from ..services.lucidity_helpers import resolve_tier
from ..services.lucidity_service import CatatoniaObserverProtocol, LucidityService
from ..structured_logging.enhanced_logging_config import get_logger
from .game_tick_protocols import EffectSecond

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from ..game.player_registry import PlayerAggregate, PlayerRegistry

logger = get_logger("server.game_tick")

LUCIDITY_DRAIN_EFFECT = "lucidity_drain_over_time"
DRAIN_REASON_CODE = "lucidity_drain_over_time"


class DrainNarration(BaseModel):
    """A line sent to the player when the drain has run for ``at`` seconds."""

    at: int = Field(ge=0)
    text: str = Field(min_length=1)


class DrainHallucination(BaseModel):
    """A hallucination of ``kind`` delivered to the player when the drain has run for ``at`` seconds."""

    at: int = Field(ge=0)
    # Deterministic handlers only: the random fake-NPC-tell/overlay pick would make an authored beat a coin flip.
    kind: Literal["room_text_overlay", "phantom_hostile"]


class LucidityDrainParams(BaseModel):
    """Shape of a ``lucidity_drain_over_time`` effect dict."""

    rate: int = Field(default=1, ge=1)
    accelerate_every: int = Field(default=0, ge=0)
    accelerate_by: int = Field(default=0, ge=0)
    # Delirium fires when LCD crosses -10 (lucidity_trigger_handlers), so that is where a drain ends by default.
    floor: int = -10
    elapsed: int = Field(default=0, ge=0)
    narration: list[DrainNarration] = Field(default_factory=list)
    hallucinations: list[DrainHallucination] = Field(default_factory=list)
    grants_liabilities: bool = True

    def rate_now(self) -> int:
        """LCD to drain this second: ``rate`` plus ``accelerate_by`` for every ``accelerate_every`` seconds elapsed."""
        if not self.accelerate_every:
            return self.rate
        return self.rate + (self.elapsed // self.accelerate_every) * self.accelerate_by


async def _narrate(player_id: uuid.UUID, text: str) -> None:
    # Imported here: chat_npc_system's import chain loops back through server.services at import time.
    from ..game.chat_npc_system import deliver_personal_quest

    # Authored narration beats are quest content, so they read on the quest channel.
    _ = await deliver_personal_quest(player_id, text)


async def _hallucinate(player_id: uuid.UUID, room_id: str, kind: str, lcd: int) -> None:
    """Deliver one authored hallucination, in the tier the player's LCD is in right now."""
    # Imported here for the same reason as _narrate: the handlers reach chat_npc_system lazily, and the package import
    # pulls in the passive flux service.
    from ..services.passive_lucidity_flux.hallucinations import (
        handle_phantom_hostile_hallucination,
        handle_room_text_overlay_hallucination,
    )

    handler = {
        "room_text_overlay": handle_room_text_overlay_hallucination,
        "phantom_hostile": handle_phantom_hostile_hallucination,
    }[kind]
    await handler(player_id, room_id, resolve_tier(lcd), lcd)


async def _fire_hallucinations(
    player_id: uuid.UUID, room_id: str | None, params: LucidityDrainParams, lcd: int
) -> None:
    """Fire the beats due at this second. A beat that fails is logged and skipped: the drain must still advance."""
    for beat in params.hallucinations:
        if beat.at != params.elapsed:
            continue
        if room_id is None:
            logger.warning("Drain hallucination skipped: player has no room", player_id=str(player_id), kind=beat.kind)
            continue
        try:
            await _hallucinate(player_id, room_id, beat.kind, lcd)
        except (ValueError, RuntimeError, OSError) as e:
            logger.warning(
                "Drain hallucination failed; skipped", player_id=str(player_id), kind=beat.kind, error=str(e)
            )


def _no_liability(player_id: str, previous_lcd: int, new_lcd: int, reason_code: str) -> None:
    """Liability picker that never picks one (``grants_liabilities: false``)."""
    _ = player_id, previous_lcd, new_lcd, reason_code


def drain_second(
    registry: PlayerRegistry,
    observer: CatatoniaObserverProtocol | None,
    player: PlayerAggregate,
    effect: dict[str, object],
) -> EffectSecond:
    """Run one second of a drain effect inside the player's unit of work (ADR-029 step 6d).

    The LCD loss is made in the caller's unit, so it commits with the effect's own state (``elapsed``): a failed
    commit rolls both back and the next second repeats the step, instead of draining twice for one ``elapsed``.
    The notifications, narration and hallucination beats are in ``after``, for once the unit has committed. A
    malformed effect is dropped.
    """
    try:
        params = LucidityDrainParams.model_validate(effect)
    except ValidationError as e:
        logger.error("Malformed lucidity_drain_over_time effect dropped", error=str(e))
        return EffectSecond(None, False)
    service = LucidityService(
        registry,
        None if params.grants_liabilities else _no_liability,
        catatonia_observer=observer,
    )

    def step(current_lcd: int) -> int:
        return -min(params.rate_now(), current_lcd - params.floor) if current_lcd > params.floor else 0

    room_id = player.row.current_room_id
    adjustment = service.apply_in(player, step, reason_code=DRAIN_REASON_CODE, location_id=room_id)
    lcd = player.lucidity.lcd
    after: list[Callable[[], Awaitable[None]]] = []
    if adjustment is not None:
        player_id = player.player_id

        lines = [line.text for line in params.narration if line.at == params.elapsed]

        async def announce() -> None:
            await service.announce(adjustment)

        async def narrate() -> None:
            for text in lines:
                await _narrate(player_id, text)

        async def hallucinate() -> None:
            await _fire_hallucinations(player_id, room_id, params, lcd)

        after.extend((announce, narrate, hallucinate))
    applied = adjustment is not None
    if lcd <= params.floor:
        return EffectSecond(None, applied, tuple(after))
    return EffectSecond({**effect, "elapsed": params.elapsed + 1}, True, tuple(after))
