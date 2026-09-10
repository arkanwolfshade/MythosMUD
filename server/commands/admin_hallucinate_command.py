"""
Admin command to force a specific hallucination for QA/testing purposes (#714).

Bypasses the frequency service's chance roll and cooldown entirely -- this is a
test affordance, not a player-facing mechanic. Delivered through the exact same
real-channel code paths (`passive_lucidity_flux/hallucinations.py`) a naturally
triggered hallucination uses, so it exercises the real delivery, not a stub.
"""

from __future__ import annotations

import uuid
from typing import cast

from fastapi import Request

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..services.lucidity_service import resolve_tier
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger
from .admin_setlucidity_command import (
    PlayerServiceLike,
    check_admin_permissions,
    get_current_lcd,
    get_player_service_from_app,
    resolve_target_player,
)

logger = get_logger(__name__)

_VALID_TYPES = ("fake_tell", "overlay", "phantom")


def extract_args(command_data: dict[str, object]) -> tuple[str | None, str | None]:
    """Extract target_player and hallucination_type from command_data."""
    target_player = cast(str | None, command_data.get("target_player") or command_data.get("target_name"))
    hallucination_type = cast(str | None, command_data.get("hallucination_type") or command_data.get("value"))
    args = cast(list[str], command_data.get("args", []))
    if not target_player and len(args) >= 1:
        target_player = args[0]
    if not hallucination_type and len(args) >= 2:
        hallucination_type = args[1]
    return target_player, hallucination_type


async def deliver_forced_hallucination(
    hallucination_type: str, player_id_uuid: uuid.UUID, room_id: str, tier: str, current_lcd: int
) -> None:
    """Deliver the requested hallucination type via the real handler functions."""
    from ..services.passive_lucidity_flux.hallucinations import (
        handle_phantom_hostile_hallucination,
        handle_room_text_overlay_hallucination,
    )

    if hallucination_type == "phantom":
        await handle_phantom_hostile_hallucination(player_id_uuid, room_id, tier, current_lcd)
    elif hallucination_type == "overlay":
        await handle_room_text_overlay_hallucination(player_id_uuid, room_id, tier, current_lcd)
    else:  # fake_tell
        from ..game.chat_npc_system import deliver_fake_npc_whisper
        from ..services.fake_hallucination_service import FakeHallucinationService
        from ..services.fake_sender_registry import fake_sender_registry
        from ..services.lucidity_event_dispatcher import send_hallucination_event

        fake_tell_data = FakeHallucinationService().generate_fake_npc_tell(player_id_uuid, room_id)
        _ = await deliver_fake_npc_whisper(player_id_uuid, fake_tell_data["npc_name"], fake_tell_data["message"])
        fake_sender_registry.record_fake_whisper(player_id_uuid, fake_tell_data["npc_name"])
        await send_hallucination_event(
            player_id_uuid,
            hallucination_type="fake_npc_tell",
            message=fake_tell_data["message"],
            metadata={
                "tier": tier,
                "lcd": current_lcd,
                "npc_name": fake_tell_data["npc_name"],
                "room_id": room_id,
                "hallucination_id": fake_tell_data["hallucination_id"],
                "forced": True,
            },
        )


class HallucinateCommandError(Exception):
    """Raised by a validation/resolution step to short-circuit straight to a result message.

    Collapses what would otherwise be a long chain of `if error: return error` checks in the
    top-level handler into a single try/except, keeping its cyclomatic complexity low.
    """

    def __init__(self, result: dict[str, str]) -> None:
        super().__init__(result.get("result", ""))
        self.result: dict[str, str] = result


def _validate_target_and_type(command_data: dict[str, object]) -> tuple[str, str]:
    """Extract and validate target_player/hallucination_type, raising on invalid input."""
    target_player, hallucination_type = extract_args(command_data)
    if not target_player or not hallucination_type:
        raise HallucinateCommandError(
            {"result": f"Usage: admin hallucinate <target_player> <{'|'.join(_VALID_TYPES)}>"}
        )
    if hallucination_type not in _VALID_TYPES:
        raise HallucinateCommandError(
            {"result": f"Unknown hallucination type '{hallucination_type}'. Valid types: {', '.join(_VALID_TYPES)}"}
        )
    return target_player, hallucination_type


async def resolve_hallucinate_target(app: object, player_name: str, target_player: str) -> tuple[uuid.UUID, str]:
    """Resolve admin permissions, the target's id, and the target's current room; raises on failure."""
    player_service: PlayerServiceLike | None = get_player_service_from_app(app)
    if not player_service:
        raise HallucinateCommandError({"result": "Player service not available."})

    current_player_obj, permission_error = await check_admin_permissions(app, player_name, player_service)
    if permission_error:
        raise HallucinateCommandError(permission_error)
    if current_player_obj is None:
        raise HallucinateCommandError({"result": "Current player not found."})

    target_player_id, resolve_error = await resolve_target_player(player_service, target_player)
    if resolve_error:
        raise HallucinateCommandError(resolve_error)
    if target_player_id is None:
        raise HallucinateCommandError({"result": f"Player '{target_player}' not found."})

    target_player_obj = await player_service.resolve_player_name(target_player)
    if target_player_obj is None or not target_player_obj.current_room_id:
        raise HallucinateCommandError({"result": f"'{target_player}' is not currently in a room."})

    return target_player_id, target_player_obj.current_room_id


async def get_current_lcd_or_error(target_player_id: uuid.UUID) -> int:
    """Resolve the target's current LCD via a fresh DB session; raises if none is available."""
    async for session in get_async_session():
        return await get_current_lcd(session, target_player_id)
    raise HallucinateCommandError({"result": "Database session could not be established. Please try again."})


def _log_hallucinate_command(player_name: str, target_player: str, hallucination_type: str, tier: str) -> None:
    """Record the forced hallucination in the admin actions log (best-effort)."""
    try:
        admin_logger = get_admin_actions_logger()
        admin_logger.log_admin_command(
            admin_name=player_name,
            command=f"admin hallucinate {target_player} {hallucination_type}",
            success=True,
            additional_data={"target_player": target_player, "hallucination_type": hallucination_type, "tier": tier},
        )
    except (OSError, AttributeError, TypeError) as log_exc:
        logger.warning("Failed to log admin hallucinate command", player_name=player_name, error=str(log_exc))


async def _handle_admin_hallucinate_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: Request | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the admin hallucinate command to force a hallucination on self or a target."""
    _ = current_user  # Intentionally unused - part of standard command handler interface
    _ = alias_storage  # Intentionally unused - part of standard command handler interface

    # Request.app is declared `Any` by Starlette itself; `object` is the narrowest honest type
    # we can assign it without lying about what's actually known here.
    app = cast(object, request.app) if request else None
    if not app:
        logger.warning("Admin hallucinate command failed - no application context", player_name=player_name)
        return {"result": "Admin hallucinate functionality is not available."}

    try:
        target_player, hallucination_type = _validate_target_and_type(command_data)
        target_player_id, room_id = await resolve_hallucinate_target(app, player_name, target_player)
        current_lcd = await get_current_lcd_or_error(target_player_id)
    except HallucinateCommandError as validation_exc:
        return validation_exc.result

    tier = resolve_tier(current_lcd)

    try:
        await deliver_forced_hallucination(hallucination_type, target_player_id, room_id, tier, current_lcd)
    except (AttributeError, TypeError, ValueError, RuntimeError) as exc:
        logger.error(
            "Admin hallucinate command failed while delivering hallucination",
            player_name=player_name,
            target_player=target_player,
            hallucination_type=hallucination_type,
            error=str(exc),
        )
        return {"result": f"Error forcing hallucination for {target_player}: {str(exc)}"}

    _log_hallucinate_command(player_name, target_player, hallucination_type, tier)
    return {"result": f"Forced '{hallucination_type}' hallucination on {target_player}."}


__all__ = ["_handle_admin_hallucinate_command"]
