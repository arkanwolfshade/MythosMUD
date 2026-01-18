"""Rescue commands for stabilising catatonic investigators."""

# pylint: disable=too-many-arguments,too-many-locals,too-many-return-statements  # Reason: Rescue commands require many parameters and intermediate variables for complex rescue logic and multiple return statements for early validation returns

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import Any

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..models.lucidity import PlayerLucidity
from ..services.lucidity_event_dispatcher import send_rescue_update_event
from ..services.lucidity_service import LucidityService
from ..services.rescue_service import RescueService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


def _get_ground_services(request: Any) -> tuple[Any, Any]:
    """Get persistence and registry from request. Returns (persistence, registry)."""
    app = getattr(request, "app", None)
    state = getattr(app, "state", None) if app else None
    persistence = getattr(state, "persistence", None) if state else None
    registry = getattr(state, "catatonia_registry", None) if state else None
    return persistence, registry


async def _validate_ground_context(
    persistence: Any, current_user: dict, player_name: str
) -> tuple[Any, dict[str, str] | None]:
    """Validate ground command context and get rescuer. Returns (rescuer, error_dict)."""
    if not persistence:
        logger.error("Ground command invoked without persistence", rescuer=player_name)
        return None, {"result": "The rescue falters; no anchor to reality can be found."}

    rescuer_username = get_username_from_user(current_user)
    rescuer = await persistence.get_player_by_name(rescuer_username)
    if not rescuer:
        logger.error("Ground command missing rescuer record", username=rescuer_username)
        return None, {"result": "Your identity drifts; regain your bearings before aiding another."}

    return rescuer, None


async def _validate_ground_target(
    persistence: Any, command_data: dict, rescuer: Any
) -> tuple[Any, dict[str, str] | None]:
    """Validate ground target and check same room. Returns (target, error_dict)."""
    target_name = command_data.get("target_player") or command_data.get("target")
    if not target_name:
        return None, {"result": "Ground whom? Specify an ally whose mind has shattered."}

    target = await persistence.get_player_by_name(target_name)
    if not target:
        return None, {"result": f"No echoes of '{target_name}' answer your call."}

    rescuer_room = getattr(rescuer, "current_room_id", None)
    target_room = getattr(target, "current_room_id", None)
    if not rescuer_room or rescuer_room != target_room:
        return None, {"result": f"{target_name} is not within reach to be grounded."}

    return target, None


def _normalize_player_ids(rescuer: Any, target: Any) -> tuple[uuid.UUID, uuid.UUID, str, str]:
    """Normalize player IDs to UUIDs. Returns (target_player_id, rescuer_player_id, target_id_str, rescuer_id_str)."""
    target_player_id_value = target.player_id
    target_player_id = (
        target_player_id_value
        if isinstance(target_player_id_value, uuid.UUID)
        else uuid.UUID(str(target_player_id_value))
    )
    rescuer_player_id_value = rescuer.player_id
    rescuer_player_id = (
        rescuer_player_id_value
        if isinstance(rescuer_player_id_value, uuid.UUID)
        else uuid.UUID(str(rescuer_player_id_value))
    )
    return target_player_id, rescuer_player_id, str(target_player_id), str(rescuer_player_id)


async def _send_grounding_channeling_events(
    target_player_id_str: str, rescuer_player_id_str: str, rescuer_username: str, target_name: str
) -> None:
    """Send channeling events for grounding ritual."""
    await send_rescue_update_event(
        target_player_id_str,
        status="channeling",
        rescuer_name=rescuer_username,
        target_name=target_name,
        message=f"{rescuer_username} kneels beside you and begins the grounding ritual.",
        progress=10.0,
    )
    await send_rescue_update_event(
        rescuer_player_id_str,
        status="channeling",
        rescuer_name=rescuer_username,
        target_name=target_name,
        message=f"You steady {target_name} and begin channeling focus.",
        progress=10.0,
    )


async def _apply_grounding_adjustment(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Rescue command requires many parameters for context and adjustment logic
    session: Any,
    target_player_id: uuid.UUID,
    lucidity_record: PlayerLucidity,
    rescuer_username: str,
    rescuer_room: str,
    registry: Any,
) -> Any:
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
        rescuer_name=rescuer_username,
        target_name=target_name,
        message="The void resists grounding; the ritual falters.",
    )
    await send_rescue_update_event(
        rescuer_player_id,
        status="failed",
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
        current_lcd=new_lcd,
        rescuer_name=rescuer_username,
        target_name=target_name,
        message=f"{rescuer_username} anchors your mind. Stability steadies at {new_lcd}/100.",
    )
    await send_rescue_update_event(
        rescuer_player_id,
        status="success",
        rescuer_name=rescuer_username,
        target_name=target_name,
        message=f"{target_name} steadies at {new_lcd}/100 LCD.",
    )


async def handle_rescue_command(
    command_data: dict,
    current_user: dict,
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


async def handle_ground_command(  # pylint: disable=too-many-arguments,too-many-locals  # Reason: Rescue command requires many parameters and intermediate variables for complex rescue logic
    command_data: dict,
    current_user: dict,
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Attempt to ground a catatonic ally back to 1 LCD."""

    persistence, registry = _get_ground_services(request)

    rescuer, error_result = await _validate_ground_context(persistence, current_user, player_name)
    if error_result:
        return error_result

    rescuer_username: str = get_username_from_user(current_user)
    rescuer_room = getattr(rescuer, "current_room_id", None)

    target, error_result = await _validate_ground_target(persistence, command_data, rescuer)
    if error_result:
        return error_result

    target_name = command_data.get("target_player") or command_data.get("target")
    if target_name is None:
        return {"result": "Target player is required for ground command."}

    target_player_id, rescuer_player_id, target_player_id_str, rescuer_player_id_str = _normalize_player_ids(
        rescuer, target
    )

    async for session in get_async_session():
        lucidity_record = await session.get(PlayerLucidity, target_player_id_str)
        if lucidity_record is None:
            logger.warning("Ground command missing lucidity record", target_id=target.player_id)
            return {"result": "The target's aura cannot be located among the ledgers of the mind."}

        if lucidity_record.current_tier != "catatonic":
            return {"result": f"{target_name} isn't catatonic and needs no grounding."}

        await _send_grounding_channeling_events(
            target_player_id_str, rescuer_player_id_str, rescuer_username, target_name
        )

        try:
            if rescuer_room is None:
                rescuer_room = ""
            result = await _apply_grounding_adjustment(
                session, target_player_id, lucidity_record, rescuer_username, rescuer_room, registry
            )
        except Exception as exc:  # noqa: B904  # pragma: no cover - defensive  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Database errors unpredictable, must rollback
            await session.rollback()
            logger.error(
                "Ground command failed",
                rescuer=rescuer_username,
                target=target_name,
                error=str(exc),
            )
            await _send_grounding_failure_events(target_player_id, rescuer_player_id, rescuer_username, target_name)
            return {"result": "Eldritch interference scatters your grounding ritual. Try again shortly."}

    if registry and hasattr(registry, "on_catatonia_cleared"):
        logger.debug("Catatonia registry notified via lucidity service observer", target=target_name)

    logger.info(
        "Ground command succeeded",
        rescuer=rescuer_username,
        target=target_name,
        new_lcd=result.new_lcd,
    )

    await _send_grounding_success_events(
        target_player_id, rescuer_player_id, rescuer_username, target_name, result.new_lcd
    )

    narrative = (
        f"You kneel beside {target_name} and anchor their mind.\n"
        f"Stability steadies at {result.new_lcd}/100, the fragility of reality humming in your ears."
    )
    return {"result": narrative}


__all__ = ["handle_rescue_command", "handle_ground_command"]
