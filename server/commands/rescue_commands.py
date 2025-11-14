"""Rescue commands for stabilising catatonic investigators."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..logging.enhanced_logging_config import get_logger
from ..models.sanity import PlayerSanity
from ..services.sanity_service import SanityService
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def handle_ground_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Attempt to ground a catatonic ally back to 1 SAN."""

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

    async for session in get_async_session():
        sanity_record = await session.get(PlayerSanity, str(target.player_id))
        if sanity_record is None:
            logger.warning("Ground command missing sanity record", target_id=target.player_id)
            return {"result": "The target's aura cannot be located among the ledgers of the mind."}

        if sanity_record.current_tier != "catatonic":
            return {"result": f"{target_name} isn't catatonic and needs no grounding."}

        delta = 1 - sanity_record.current_san
        if delta <= 0:
            delta = 1  # Ensure at least a single point of recovery

        service = SanityService(session, catatonia_observer=registry)
        try:
            result = await service.apply_sanity_adjustment(
                str(target.player_id),
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
            return {"result": "Eldritch interference scatters your grounding ritual. Try again shortly."}

    if registry and hasattr(registry, "on_catatonia_cleared"):
        logger.debug("Catatonia registry notified via sanity service observer", target=target_name)

    logger.info(
        "Ground command succeeded",
        rescuer=rescuer_username,
        target=target_name,
        new_san=result.new_san,
    )

    narrative = (
        f"You kneel beside {target_name} and anchor their mind.\n"
        f"Stability steadies at {result.new_san}/100, the fragility of reality humming in your ears."
    )
    return {"result": narrative}


__all__ = ["handle_ground_command"]
