"""Item-use effects: maps an item's ``effect_components`` tags to async handlers (#870).

``/use`` resolves a consumable's prototype, finds the first of its ``effect_components`` that has a
handler here, and awaits it. A handler reports ``ok=False`` when the effect did not happen (for
example a cooldown); the caller then keeps the item. Handler parameters live in the prototype's
``metadata`` under a key named for the effect, validated by the models in ``metadata_models``.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from datetime import timedelta
from typing import cast
from uuid import UUID

from pydantic import ValidationError as PydanticValidationError

from server.database import get_async_session
from server.game.items.metadata_models import LucidityRecoveryMetadata
from server.game.items.models import ItemPrototypeModel
from server.services.active_lucidity_service import ActiveLucidityService, LucidityActionOnCooldownError
from server.services.lucidity_service import CatatoniaObserverProtocol
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

LUCIDITY_RECOVERY_TAG = "component.lucidity_recovery"

_COOLDOWN_REFUSAL = "You don't think you can stomach another tonic at this time."
_INERT_MESSAGE = "You swallow it, but nothing happens."


@dataclass(frozen=True)
class ItemUseContext:
    """What an effect handler needs to act on a player."""

    app: object | None
    player_id: UUID
    room_id: str
    prototype: ItemPrototypeModel


@dataclass(frozen=True)
class ItemEffectResult:
    """Outcome of one effect. ``ok=False`` means nothing happened and the item must be kept."""

    ok: bool
    message: str


ItemEffectHandler = Callable[[ItemUseContext], Awaitable[ItemEffectResult]]


def _catatonia_observer(app: object | None) -> CatatoniaObserverProtocol | None:
    """Catatonia registry from the app container, falling back to app.state (as the recovery commands do)."""
    state: object = getattr(app, "state", None)
    container: object = getattr(state, "container", None)
    source = container if container else state
    return cast(CatatoniaObserverProtocol | None, getattr(source, "catatonia_registry", None))


async def _lucidity_recovery(ctx: ItemUseContext) -> ItemEffectResult:
    """Restore LCD under the item's named cooldown (see ``LucidityRecoveryMetadata``)."""
    try:
        params = LucidityRecoveryMetadata.model_validate(cast(object, ctx.prototype.metadata.get("lucidity_recovery")))
    except PydanticValidationError as exc:
        logger.error(
            "Consumable has invalid lucidity_recovery metadata",
            prototype_id=ctx.prototype.prototype_id,
            error=str(exc),
        )
        return ItemEffectResult(ok=False, message=_INERT_MESSAGE)

    async for session in get_async_session():
        service = ActiveLucidityService(session, catatonia_observer=_catatonia_observer(ctx.app))
        try:
            result = await service.apply_timed_recovery(
                ctx.player_id,
                cooldown_key=params.cooldown_key,
                lcd_delta=params.lcd_delta,
                cooldown=timedelta(minutes=params.cooldown_minutes),
                location_id=ctx.room_id,
            )
            await session.commit()
        except LucidityActionOnCooldownError:
            await session.rollback()
            return ItemEffectResult(ok=False, message=_COOLDOWN_REFUSAL)
        sign = "+" if result.delta >= 0 else ""
        return ItemEffectResult(
            ok=True,
            message=(
                f"You swallow the {ctx.prototype.name.lower()}. A bitter warmth settles your thoughts. "
                f"({sign}{result.delta} LCD, now {result.new_lcd}/100)"
            ),
        )
    return ItemEffectResult(ok=False, message=_INERT_MESSAGE)


ITEM_EFFECTS: dict[str, ItemEffectHandler] = {LUCIDITY_RECOVERY_TAG: _lucidity_recovery}


def find_effect(prototype: ItemPrototypeModel) -> ItemEffectHandler | None:
    """Handler for the first of the prototype's ``effect_components`` that has one."""
    for tag in prototype.effect_components:
        if handler := ITEM_EFFECTS.get(tag):
            return handler
    return None
