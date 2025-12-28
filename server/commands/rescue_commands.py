"""Rescue commands for stabilising catatonic investigators."""

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


async def handle_rescue_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
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


async def handle_ground_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Attempt to ground a catatonic ally back to 1 LCD."""

    app = getattr(request, "app", None)
    state = getattr(app, "state", None) if app else None
    persistence = getattr(state, "persistence", None) if state else None
    registry = getattr(state, "catatonia_registry", None) if state else None

    if not persistence:
        logger.error("Ground command invoked without persistence", rescuer=player_name)
        return {"result": "The rescue falters; no anchor to reality can be found."}

    rescuer_username = get_username_from_user(current_user)
    rescuer = persistence.get_player_by_name(rescuer_username)
    if not rescuer:
        logger.error("Ground command missing rescuer record", username=rescuer_username)
        return {"result": "Your identity drifts; regain your bearings before aiding another."}

    target_name = command_data.get("target_player") or command_data.get("target")
    if not target_name:
        return {"result": "Ground whom? Specify an ally whose mind has shattered."}

    target = persistence.get_player_by_name(target_name)
    if not target:
        return {"result": f"No echoes of '{target_name}' answer your call."}

    rescuer_room = getattr(rescuer, "current_room_id", None)
    target_room = getattr(target, "current_room_id", None)
    if not rescuer_room or rescuer_room != target_room:
        return {"result": f"{target_name} is not within reach to be grounded."}

    # Convert player.player_id to UUID if needed (handles SQLAlchemy Column[str])
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
    target_player_id_str = str(target_player_id)
    rescuer_player_id_str = str(rescuer_player_id)

    async for session in get_async_session():
        lucidity_record = await session.get(PlayerLucidity, target_player_id_str)
        if lucidity_record is None:
            logger.warning("Ground command missing lucidity record", target_id=target.player_id)
            return {"result": "The target's aura cannot be located among the ledgers of the mind."}

        if lucidity_record.current_tier != "catatonic":
            return {"result": f"{target_name} isn't catatonic and needs no grounding."}

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

        delta = 1 - lucidity_record.current_lcd
        if delta <= 0:
            delta = 1  # Ensure at least a single point of recovery

        service = LucidityService(session, catatonia_observer=registry)
        try:
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
        except Exception as exc:  # pragma: no cover - defensive
            await session.rollback()
            logger.error(
                "Ground command failed",
                rescuer=rescuer_username,
                target=target_name,
                error=str(exc),
            )
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
            return {"result": "Eldritch interference scatters your grounding ritual. Try again shortly."}

    if registry and hasattr(registry, "on_catatonia_cleared"):
        logger.debug("Catatonia registry notified via lucidity service observer", target=target_name)

    logger.info(
        "Ground command succeeded",
        rescuer=rescuer_username,
        target=target_name,
        new_lcd=result.new_lcd,
    )

    await send_rescue_update_event(
        target_player_id,
        status="success",
        current_lcd=result.new_lcd,
        rescuer_name=rescuer_username,
        target_name=target_name,
        message=f"{rescuer_username} anchors your mind. Stability steadies at {result.new_lcd}/100.",
    )
    await send_rescue_update_event(
        rescuer_player_id,
        status="success",
        rescuer_name=rescuer_username,
        target_name=target_name,
        message=f"{target_name} steadies at {result.new_lcd}/100 LCD.",
    )

    narrative = (
        f"You kneel beside {target_name} and anchor their mind.\n"
        f"Stability steadies at {result.new_lcd}/100, the fragility of reality humming in your ears."
    )
    return {"result": narrative}


__all__ = ["handle_rescue_command", "handle_ground_command"]
