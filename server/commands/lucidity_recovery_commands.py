"""Recovery rituals that steady a mind frayed by eldritch exposure."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..services.active_lucidity_service import (
    ActiveLucidityService,
    LucidityActionOnCooldownError,
    UnknownLucidityActionError,
)
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def _perform_recovery_action(
    action_code: str,
    _command_data: dict,
    current_user: dict,
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Common execution path for LCD recovery commands."""

    app = getattr(request, "app", None)
    persistence = getattr(app.state, "persistence", None) if app else None
    if not persistence:
        logger.error("Recovery command invoked without persistence", action=action_code, player=player_name)
        return {"result": "The ritual falters; the ley lines are inaccessible."}

    username = get_username_from_user(current_user)
    player = persistence.get_player_by_name(username)
    if not player:
        logger.error("Recovery command failed to locate player", action=action_code, username=username)
        return {"result": "Your identity wavers in the void. Try again after stabilizing your presence."}

    room_id = getattr(player, "current_room_id", None)
    if not room_id:
        return {"result": "Without a locus in space, the ritual dissipates into meaningless static."}

    catatonia_observer = getattr(app.state, "catatonia_registry", None) if app else None

    async for session in get_async_session():
        service = ActiveLucidityService(session, catatonia_observer=catatonia_observer)
        try:
            result = await service.perform_recovery_action(
                player_id=str(player.player_id),
                action_code=action_code,
                location_id=str(room_id),
            )
            await session.commit()
        except LucidityActionOnCooldownError:
            await session.rollback()
            cooldown = await service.get_action_cooldown(player.player_id, action_code)
            if cooldown and cooldown.cooldown_expires_at:
                expiry = cooldown.cooldown_expires_at
                if expiry.tzinfo is None:
                    expiry = expiry.replace(tzinfo=UTC)
                remaining_seconds = max(0.0, (expiry - datetime.now(UTC)).total_seconds())
                remaining_minutes = int(remaining_seconds // 60)
                return {
                    "result": (
                        "The sigils are still cooling from your previous rite. "
                        f"Return in {remaining_minutes or 1} minutes to try again."
                    )
                }
            return {"result": "The ritual pathways are still resonating; patience is required."}
        except UnknownLucidityActionError:
            await session.rollback()
            return {"result": "That rite is uncharted in the Pnakotic addenda. Choose a known discipline."}
        except OSError as exc:  # pragma: no cover - defensive logging
            await session.rollback()
            logger.error(
                "Recovery ritual failed",
                action=action_code,
                player_id=str(player.player_id),
                room_id=str(room_id),
                error=str(exc),
            )
            return {"result": "Anomalous interference disrupts the ritual. Try again when the stars align."}
        else:
            delta = result.delta
            new_total = result.new_lcd
            sign = "+" if delta >= 0 else ""
            narrative = (
                f"You complete the {action_code.replace('_', ' ')} rite. "
                f"Stability shifts {sign}{delta}, settling at {new_total}/100."
            )

            # Restore MP for meditation and rest actions
            mp_message = ""
            if action_code in ("meditate", "pray"):
                mp_regeneration_service = getattr(app.state, "mp_regeneration_service", None) if app else None
                if mp_regeneration_service:
                    if action_code == "meditate":
                        mp_result = await mp_regeneration_service.restore_mp_from_meditation(
                            player.player_id, duration_seconds=180
                        )
                    else:  # pray
                        mp_result = await mp_regeneration_service.restore_mp_from_rest(
                            player.player_id, duration_seconds=60
                        )

                    if mp_result.get("mp_restored", 0) > 0:
                        mp_message = f" You also recover {mp_result['mp_restored']} magic points."

            lore_note = "Archivist's Aside: record this moment; resilience is born in repeated discipline."
            return {"result": f"{narrative}{mp_message}\n{lore_note}"}

    return {"result": "The rite fizzles before contact is made with the numinous."}


async def handle_pray_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Invoke the prayer rite to petition the Elder Light."""

    return await _perform_recovery_action("pray", command_data, current_user, request, alias_storage, player_name)


async def handle_meditate_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Invoke the meditation rite to anchor the mind."""

    return await _perform_recovery_action("meditate", command_data, current_user, request, alias_storage, player_name)


async def handle_group_solace_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Share solace among nearby allies to salve frayed nerves."""

    return await _perform_recovery_action(
        "group_solace", command_data, current_user, request, alias_storage, player_name
    )


async def handle_therapy_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Undertake sanctioned therapy under Arkham Sanitarium protocols."""

    return await _perform_recovery_action("therapy", command_data, current_user, request, alias_storage, player_name)


async def handle_folk_tonic_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Swallow a dubious folk tonic brewed by cautiously reliable apothecaries."""

    return await _perform_recovery_action("folk_tonic", command_data, current_user, request, alias_storage, player_name)


__all__ = [
    "handle_pray_command",
    "handle_meditate_command",
    "handle_group_solace_command",
    "handle_therapy_command",
    "handle_folk_tonic_command",
]
