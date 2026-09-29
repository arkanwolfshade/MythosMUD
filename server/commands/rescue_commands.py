"""Rescue commands for stabilising catatonic investigators."""

# pylint: disable=too-many-arguments,too-many-locals,too-many-return-statements  # Reason: Rescue commands require many parameters and intermediate variables for complex rescue logic and multiple return statements for early validation returns

from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, NamedTuple, Protocol, cast

from sqlalchemy.ext.asyncio import AsyncSession

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..models.lucidity import PlayerLucidity
from ..services.lucidity_event_dispatcher import send_rescue_update_event
from ..services.lucidity_helpers import CatatoniaObserverProtocol, LucidityUpdateResult
from ..services.lucidity_service import LucidityService
from ..services.rescue_service import RescueService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from .ground_channel import FinishOutcome, start_ground_channel
from .rest_command import check_player_in_combat

logger = get_logger(__name__)


class _GroundPlayer(Protocol):
    """The slice of a player `ground` reads."""

    player_id: uuid.UUID | str
    current_room_id: str | None


class _GroundPersistence(Protocol):
    """The slice of the persistence layer the completion re-check reads."""

    async def get_player_by_name(self, name: str) -> _GroundPlayer | None: ...  # pylint: disable=missing-function-docstring  # Reason: Protocol stub


class _GroundServices(NamedTuple):
    """Services `ground` needs, resolved once from `request.app.state` (an untyped boundary)."""

    persistence: _GroundPersistence | None
    registry: CatatoniaObserverProtocol | None
    connection_manager: object | None
    app: object | None


class _GroundContainer(Protocol):
    """DI container surface exposing the connection manager."""

    connection_manager: object


def _get_ground_services(request: object) -> _GroundServices:
    """Resolve persistence, catatonia registry, connection manager and app from the request."""
    # Annotated locals: app.state is an untyped boundary, so declare what each attribute is.
    app: object | None = getattr(request, "app", None)
    state: object | None = getattr(app, "state", None) if app else None
    persistence: _GroundPersistence | None = getattr(state, "persistence", None) if state else None
    registry: CatatoniaObserverProtocol | None = getattr(state, "catatonia_registry", None) if state else None
    container: _GroundContainer | None = getattr(state, "container", None) if state else None
    legacy_manager: object | None = getattr(state, "connection_manager", None) if state else None
    connection_manager = container.connection_manager if container else legacy_manager
    return _GroundServices(persistence, registry, connection_manager, app)


async def _validate_ground_context(
    persistence: _GroundPersistence | None, current_user: dict[str, object], player_name: str
) -> _GroundPlayer | dict[str, str]:
    """Validate ground command context. Returns the rescuer, or an error dict."""
    if not persistence:
        logger.error("Ground command invoked without persistence", rescuer=player_name)
        return {"result": "The rescue falters; no anchor to reality can be found."}

    rescuer_username = get_username_from_user(current_user)
    rescuer = await persistence.get_player_by_name(rescuer_username)
    if not rescuer:
        logger.error("Ground command missing rescuer record", username=rescuer_username)
        return {"result": "Your identity drifts; regain your bearings before aiding another."}

    return rescuer


async def _validate_ground_target(
    persistence: _GroundPersistence, command_data: dict[str, Any], rescuer: _GroundPlayer
) -> _GroundPlayer | dict[str, str]:
    """Validate ground target and check same room. Returns the target, or an error dict."""
    target_name: str | None = command_data.get("target_player") or command_data.get("target")
    if not target_name:
        return {"result": "Ground whom? Specify an ally whose mind has shattered."}

    target = await persistence.get_player_by_name(target_name)
    if not target:
        return {"result": f"No echoes of '{target_name}' answer your call."}

    if not rescuer.current_room_id or rescuer.current_room_id != target.current_room_id:
        return {"result": f"{target_name} is not within reach to be grounded."}

    return target


def _as_uuid(value: uuid.UUID | str) -> uuid.UUID:
    return value if isinstance(value, uuid.UUID) else uuid.UUID(str(value))


async def _apply_grounding_adjustment(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Rescue command requires many parameters for context and adjustment logic
    session: AsyncSession,
    target_player_id: uuid.UUID,
    lucidity_record: PlayerLucidity,
    rescuer_username: str,
    rescuer_room: str,
    registry: CatatoniaObserverProtocol | None,
) -> LucidityUpdateResult:
    """Apply lucidity adjustment for grounding. Returns result."""
    delta = 1 - lucidity_record.current_lcd
    if delta <= 0:
        delta = 1

    service = LucidityService(session, catatonia_observer=registry)
    result = await service.apply_lucidity_adjustment(
        target_player_id,
        delta,
        reason_code="ground_rescue",
        metadata={
            "rescuer": rescuer_username,
            "timestamp": datetime.now(UTC).isoformat(),
            "source": "ground_command",
        },
        location_id=str(rescuer_room),
    )
    await session.commit()
    return result


async def _send_grounding_failure_events(
    target_player_id: uuid.UUID, rescuer_player_id: uuid.UUID, rescuer_username: str, target_name: str
) -> None:
    """Send failure events for grounding ritual."""
    await send_rescue_update_event(
        target_player_id,
        status="failed",
        role="target",
        rescuer_name=rescuer_username,
        target_name=target_name,
        message="The void resists grounding; the ritual falters.",
    )
    await send_rescue_update_event(
        rescuer_player_id,
        status="failed",
        role="rescuer",
        rescuer_name=rescuer_username,
        target_name=target_name,
        message="Your focus shatters; the grounding ritual fails to take hold.",
    )


async def _send_grounding_success_events(
    target_player_id: uuid.UUID,
    rescuer_player_id: uuid.UUID,
    rescuer_username: str,
    target_name: str,
    new_lcd: int,
) -> None:
    """Send success events for grounding ritual."""
    await send_rescue_update_event(
        target_player_id,
        status="success",
        role="target",
        current_lcd=new_lcd,
        rescuer_name=rescuer_username,
        target_name=target_name,
        message=f"{rescuer_username} anchors your mind. Stability steadies at {new_lcd}/100.",
    )
    await send_rescue_update_event(
        rescuer_player_id,
        status="success",
        role="rescuer",
        rescuer_name=rescuer_username,
        target_name=target_name,
        message=f"{target_name} steadies at {new_lcd}/100 LCD.",
    )


async def handle_rescue_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Delegate rescue handling to the RescueService for testable, real logic.
    """
    app = getattr(request, "app", None)
    state = getattr(app, "state", None) if app else None
    persistence = getattr(state, "persistence", None) if state else None
    registry = getattr(state, "catatonia_registry", None) if state else None

    target_name = command_data.get("target") or command_data.get("target_player")
    if not target_name:
        return {"result": "Specify a target to rescue."}

    service = RescueService(
        persistence=persistence,
        session_factory=get_async_session,
        catatonia_registry=registry,
    )

    return await service.rescue(target_name, current_user, player_name)


_GROUND_STARTED = (
    "You kneel beside {target} and begin the grounding ritual. "
    "Any movement, combat, or spellcasting will break your focus."
)


@dataclass(frozen=True)
class _GroundContext:
    """Everything the up-front check and the completion step need, captured when `ground` starts."""

    persistence: _GroundPersistence
    registry: CatatoniaObserverProtocol | None
    target_name: str
    target_player_id: uuid.UUID
    rescuer_player_id: uuid.UUID
    rescuer_username: str
    rescuer_room: str | None


async def _check_ground_target_ready(ctx: _GroundContext) -> dict[str, str] | None:
    """Up-front feedback for the rescuer: is the target catatonic? Returns an error dict if not."""
    async for session in get_async_session():
        lucidity_record = await session.get(PlayerLucidity, str(ctx.target_player_id))
        if lucidity_record is None:
            logger.warning("Ground command missing lucidity record", target_id=ctx.target_player_id)
            return {"result": "The target's aura cannot be located among the ledgers of the mind."}
        if lucidity_record.current_tier != "catatonic":
            return {"result": f"{ctx.target_name} isn't catatonic and needs no grounding."}
        return None
    return {"result": "Eldritch interference scatters your grounding ritual. Try again shortly."}


async def _participants_still_together(ctx: _GroundContext) -> bool:
    """Re-check at completion that both participants still exist and share a room."""
    rescuer = await ctx.persistence.get_player_by_name(ctx.rescuer_username)
    target = await ctx.persistence.get_player_by_name(ctx.target_name)
    if rescuer is None or target is None:
        return False
    return rescuer.current_room_id == target.current_room_id


async def _finish_ground(ctx: _GroundContext) -> FinishOutcome:
    """Channel elapsed: apply the grounding if the target still needs it, else report interrupted."""
    if not await _participants_still_together(ctx):
        return "interrupted"

    async for session in get_async_session():
        lucidity_record = await session.get(PlayerLucidity, str(ctx.target_player_id))
        if lucidity_record is None or lucidity_record.current_tier != "catatonic":
            return "interrupted"

        try:
            result = await _apply_grounding_adjustment(
                session,
                ctx.target_player_id,
                lucidity_record,
                ctx.rescuer_username,
                ctx.rescuer_room or "",
                ctx.registry,
            )
        except Exception as exc:  # noqa: B904  # pragma: no cover - defensive  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Database errors unpredictable, must rollback
            await session.rollback()
            logger.error("Ground command failed", rescuer=ctx.rescuer_username, target=ctx.target_name, error=str(exc))
            await _send_grounding_failure_events(
                ctx.target_player_id, ctx.rescuer_player_id, ctx.rescuer_username, ctx.target_name
            )
            return "done"

        logger.info(
            "Ground command succeeded", rescuer=ctx.rescuer_username, target=ctx.target_name, new_lcd=result.new_lcd
        )
        await _send_grounding_success_events(
            ctx.target_player_id, ctx.rescuer_player_id, ctx.rescuer_username, ctx.target_name, result.new_lcd
        )
        return "done"

    await _send_grounding_failure_events(
        ctx.target_player_id, ctx.rescuer_player_id, ctx.rescuer_username, ctx.target_name
    )
    return "done"


async def handle_ground_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Begin a timed ritual to ground a catatonic ally back to 1 LCD (#713).

    The adjustment lands after `GameConfig.ground_channel_seconds`, unless movement, spellcasting,
    combat or a disconnect interrupts either participant first (see `ground_channel`).
    """

    # Reason: DYNAMIC_DISPATCH - request is Any per this command handler's own signature (registry contract).
    # Appropriate because: the callee takes object and immediately types every attribute it reads.
    services = _get_ground_services(request)  # pyright: ignore[reportAny]

    rescuer = await _validate_ground_context(services.persistence, current_user, player_name)
    if isinstance(rescuer, dict):
        return rescuer
    persistence = cast(_GroundPersistence, services.persistence)  # _validate_ground_context rejected None

    rescuer_username: str = get_username_from_user(current_user)

    target = await _validate_ground_target(persistence, command_data, rescuer)
    if isinstance(target, dict):
        return target

    target_name: str | None = command_data.get("target_player") or command_data.get("target")
    if target_name is None:
        return {"result": "Target player is required for ground command."}

    target_player_id = _as_uuid(target.player_id)
    rescuer_player_id = _as_uuid(rescuer.player_id)

    ctx = _GroundContext(
        persistence=persistence,
        registry=services.registry,
        target_name=target_name,
        target_player_id=target_player_id,
        rescuer_player_id=rescuer_player_id,
        rescuer_username=rescuer_username,
        rescuer_room=rescuer.current_room_id,
    )
    error_result = await _check_ground_target_ready(ctx)
    if error_result:
        return error_result

    if await check_player_in_combat(rescuer_player_id, services.app):
        return {"result": "You cannot perform a grounding ritual during combat. End combat first."}

    error_message = await start_ground_channel(
        services.connection_manager,
        rescuer_id=rescuer_player_id,
        target_id=target_player_id,
        rescuer_name=rescuer_username,
        target_name=target_name,
        finish=lambda: _finish_ground(ctx),
        notify=send_rescue_update_event,
    )
    if error_message:
        return {"result": error_message}

    return {"result": _GROUND_STARTED.format(target=target_name)}


__all__ = ["handle_rescue_command", "handle_ground_command"]
