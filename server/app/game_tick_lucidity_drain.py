"""lucidity_drain_over_time: a status effect that pulls LCD down once per game second until it reaches a floor.

Content applies it as a plain effect dict (e.g. via the ``apply_effect`` scripted action); every field but ``type`` is
optional and validated by ``LucidityDrainParams``. There is no fixed duration on purpose: the rate never falls, so the
drain always reaches the floor (delirium fires when LCD crosses -10), which instanced content relies on when delirium
is the only way out. Each step goes through ``LucidityService``, so tiers, events, catatonia and delirium behave as for
any other LCD loss.
"""

# pylint: disable=too-few-public-methods  # Reason: Pydantic models; validators are the behavior

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, cast

from pydantic import BaseModel, Field, ValidationError
from sqlalchemy.exc import SQLAlchemyError

from ..database import get_async_session
from ..services.lucidity_service import CatatoniaObserverProtocol, LucidityService
from ..structured_logging.enhanced_logging_config import get_logger
from .game_tick_protocols import _TickContainer

if TYPE_CHECKING:
    from ..models.player import Player

logger = get_logger("server.game_tick")

LUCIDITY_DRAIN_EFFECT = "lucidity_drain_over_time"
DRAIN_REASON_CODE = "lucidity_drain_over_time"


class DrainNarration(BaseModel):
    """A line sent to the player when the drain has run for ``at`` seconds."""

    at: int = Field(ge=0)
    text: str = Field(min_length=1)


class LucidityDrainParams(BaseModel):
    """Shape of a ``lucidity_drain_over_time`` effect dict."""

    rate: int = Field(default=1, ge=1)
    accelerate_every: int = Field(default=0, ge=0)
    accelerate_by: int = Field(default=0, ge=0)
    # Delirium fires when LCD crosses -10 (lucidity_trigger_handlers), so that is where a drain ends by default.
    floor: int = -10
    elapsed: int = Field(default=0, ge=0)
    narration: list[DrainNarration] = Field(default_factory=list)
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


def _no_liability(player_id: str, previous_lcd: int, new_lcd: int, reason_code: str) -> None:
    """Liability picker that never picks one (``grants_liabilities: false``)."""
    _ = player_id, previous_lcd, new_lcd, reason_code


async def _drain_step(
    container: _TickContainer, player_id: uuid.UUID, room_id: str | None, params: LucidityDrainParams
) -> tuple[int, bool] | None:
    """Apply one second's drain; returns (LCD now, whether LCD was changed), or None with no database session."""
    observer = cast(CatatoniaObserverProtocol | None, getattr(container, "catatonia_registry", None))
    async for session in get_async_session():
        service = LucidityService(
            session,
            None if params.grants_liabilities else _no_liability,
            catatonia_observer=observer,
        )
        current = (await service.get_player_lucidity(player_id)).current_lcd
        if current <= params.floor:
            return current, False
        delta = -min(params.rate_now(), current - params.floor)
        result = await service.apply_lucidity_adjustment(
            player_id, delta, reason_code=DRAIN_REASON_CODE, location_id=room_id
        )
        await session.commit()
        return result.new_lcd, True
    return None


async def process_lucidity_drain(
    container: _TickContainer, player: Player, effect: dict[str, object]
) -> tuple[dict[str, object] | None, bool]:
    """Run one second of a drain effect.

    Returns (updated effect or None once finished, whether the effect had an impact), like the other effect processors.
    A database failure keeps the effect so the next second retries; a malformed effect is dropped.
    """
    try:
        params = LucidityDrainParams.model_validate(effect)
    except ValidationError as e:
        logger.error("Malformed lucidity_drain_over_time effect dropped", error=str(e))
        return None, False
    player_id = uuid.UUID(str(player.player_id))
    try:
        outcome = await _drain_step(container, player_id, player.current_room_id, params)
    except (SQLAlchemyError, ValueError, RuntimeError, OSError) as e:
        logger.warning("Lucidity drain step failed; will retry next second", player_id=str(player_id), error=str(e))
        return effect, False
    if outcome is None:
        return effect, False
    new_lcd, applied = outcome
    if applied:
        for line in params.narration:
            if line.at == params.elapsed:
                await _narrate(player_id, line.text)
    if new_lcd <= params.floor:
        return None, applied
    return {**effect, "elapsed": params.elapsed + 1}, True
