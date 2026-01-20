"""
Debrief command for MythosMUD.

After sanitarium failover (LCD -100), players must complete a debrief
that provides narrative recap and optionally allows immediate therapy session.
"""

# pylint: disable=too-many-locals  # Reason: Debrief command requires many intermediate variables for narrative generation

from __future__ import annotations

from typing import Any

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..services.active_lucidity_service import ActiveLucidityService, LucidityActionOnCooldownError
from ..services.lucidity_service import LucidityService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)

# Action code for tracking debrief availability
DEBRIEF_PENDING_ACTION_CODE = "debrief_pending"


def _get_persistence_from_app(app: Any) -> Any:
    """Retrieve persistence service from app container or state."""
    if app and hasattr(app.state, "container") and app.state.container:
        return app.state.container.async_persistence
    if app:
        return getattr(app.state, "persistence", None)
    return None


def _get_catatonia_registry_from_app(app: Any) -> Any:
    """Retrieve catatonia registry from app container or state."""
    if app and hasattr(app.state, "container") and app.state.container:
        return app.state.container.catatonia_registry
    if app:
        return getattr(app.state, "catatonia_registry", None)
    return None


async def _validate_debrief_context(
    persistence: Any, username: str, player_name: str
) -> tuple[Any, dict[str, str] | None]:
    """Validate persistence and player existence for debrief command."""
    if not persistence:
        logger.error("Debrief command invoked without persistence", player=player_name)
        return None, {"result": "The sanitarium records are inaccessible. The ley lines waver."}
    player = await persistence.get_player_by_name(username)
    if not player:
        logger.error("Debrief command failed to locate player", username=username)
        return None, {"result": "Your identity wavers in the void. Try again after stabilizing your presence."}
    return player, None


async def _check_debrief_availability(lucidity_service: LucidityService, player_id_uuid: Any) -> dict[str, str] | None:
    """Check if debrief cooldown exists and return error if not available."""
    debrief_cooldown = await lucidity_service.get_cooldown(player_id_uuid, DEBRIEF_PENDING_ACTION_CODE)
    if not debrief_cooldown:
        return {
            "result": (
                "No debrief session is available. This interaction is only available after sanitarium intervention."
            )
        }
    return None


async def _perform_therapy_if_requested(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Therapy session execution requires 6 parameters for decision flag, player data, database session, observer, and message accumulation; extracting into a class or dataclass would add unnecessary complexity
    wants_therapy: bool,
    player: Any,
    player_id_uuid: Any,
    session: Any,
    catatonia_observer: Any,
    result_message: str,
) -> str:
    """Perform therapy session if requested and append result to message."""
    if not wants_therapy:
        return result_message
    active_service = ActiveLucidityService(session, catatonia_observer=catatonia_observer)
    room_id = getattr(player, "current_room_id", None)
    try:
        therapy_result = await active_service.perform_recovery_action(
            player_id=str(player_id_uuid),
            action_code="therapy",
            location_id=str(room_id) if room_id else None,
        )
        therapy_delta = therapy_result.delta
        therapy_total = therapy_result.new_lcd
        sign = "+" if therapy_delta >= 0 else ""
        result_message += (
            f"\n\nYou opt for immediate therapy. The sanitarium staff guides you through "
            f"a structured session. Stability shifts {sign}{therapy_delta}, "
            f"settling at {therapy_total}/100."
        )
        logger.info("Debrief with immediate therapy completed", player_id=player_id_uuid)
    except LucidityActionOnCooldownError:
        result_message += (
            "\n\nTherapy is currently unavailable due to recent sessions. You may return later for additional support."
        )
    except Exception as therapy_exc:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Therapy errors unpredictable, must not fail debrief
        logger.warning(
            "Therapy failed during debrief",
            player_id=player_id_uuid,
            error=str(therapy_exc),
        )
        result_message += "\n\nTherapy session could not be initiated at this time."
    return result_message


async def _complete_debrief(
    lucidity_service: LucidityService,
    player_id_uuid: Any,
    session: Any,
    result_message: str,
    wants_therapy: bool,
) -> dict[str, str]:
    """Complete debrief by clearing cooldown and finalizing message."""
    await lucidity_service._repo.delete_cooldowns_by_action_code_pattern(  # pylint: disable=protected-access  # Reason: Accessing protected member _repo is necessary for lucidity service repository access, this is part of the service internal API
        player_id_uuid, DEBRIEF_PENDING_ACTION_CODE
    )
    await session.commit()
    result_message += (
        "\n\nThe debrief session concludes. You are free to leave the sanitarium "
        "when you are ready, though the staff recommends rest and reflection."
    )
    logger.info("Debrief completed", player_id=player_id_uuid, therapy_requested=wants_therapy)
    return {"result": result_message}


async def handle_debrief_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the debrief command after sanitarium failover.

    Provides narrative recap and optional immediate therapy session.
    Debrief is mandatory and becomes available after respawning from sanitarium failover.
    """
    app = getattr(request, "app", None)
    persistence = _get_persistence_from_app(app)
    username = get_username_from_user(current_user)
    player, context_error = await _validate_debrief_context(persistence, username, player_name)
    if context_error:
        return context_error
    catatonia_observer = _get_catatonia_registry_from_app(app)
    async for session in get_async_session():
        try:
            lucidity_service = LucidityService(session)
            player_id_uuid = player.player_id
            availability_error = await _check_debrief_availability(lucidity_service, player_id_uuid)
            if availability_error:
                return availability_error
            command_args = command_data.get("args", "")
            wants_therapy = command_args.lower().strip() in ("therapy", "yes", "y", "t")
            recap = _generate_narrative_recap(player_id_uuid, session, lucidity_service)
            result_message = await _perform_therapy_if_requested(
                wants_therapy, player, player_id_uuid, session, catatonia_observer, recap
            )
            return await _complete_debrief(lucidity_service, player_id_uuid, session, result_message, wants_therapy)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Debrief errors unpredictable, must handle gracefully
            logger.error(
                "Debrief command failed",
                player_id=player.player_id,
                error=str(e),
                exc_info=True,
            )
            await session.rollback()
            return {"result": "The debrief session encountered complications. Please try again."}
    return {"result": "The sanitarium records could not be accessed. Please try again."}


def _generate_narrative_recap(player_id: Any, session: Any, _lucidity_service: LucidityService) -> str:
    """
    Generate narrative recap of recent events leading to sanitarium intervention.

    Args:
        player_id: Player UUID
        session: Database session
        lucidity_service: Lucidity service instance

    Returns:
        Narrative recap string
    """
    try:
        from sqlalchemy import desc, select

        from ..models.lucidity import LucidityAdjustmentLog

        # Get recent lucidity adjustments (last 10 entries)
        stmt = (
            select(LucidityAdjustmentLog)
            .where(LucidityAdjustmentLog.player_id == player_id)
            .order_by(desc(LucidityAdjustmentLog.created_at))
            .limit(10)
        )
        result = session.execute(stmt)
        adjustments = list(result.scalars().all())

        if not adjustments:
            return (
                "The sanitarium staff notes your arrival but records are incomplete. "
                "They recommend rest and observation. Your mind has been through a trial, "
                "though the specifics remain clouded."
            )

        # Build narrative from adjustments
        recap_parts = [
            "The sanitarium staff provides you with a brief recap of recent events:",
            "",
        ]

        # Group by reason code and summarize
        recent_events: dict[str, list[int]] = {}
        for adj in adjustments[:5]:  # Last 5 adjustments
            reason = adj.reason_code.replace("_", " ").title()
            if reason not in recent_events:
                recent_events[reason] = []
            recent_events[reason].append(adj.delta)

        for reason, deltas in recent_events.items():
            total_delta = sum(deltas)
            count = len(deltas)
            sign = "+" if total_delta >= 0 else ""
            recap_parts.append(
                f"- {reason}: {count} occurrence{'s' if count > 1 else ''}, net change {sign}{total_delta} LCD"
            )

        recap_parts.append("")
        recap_parts.append(
            "The staff explains that you experienced a significant lucidity crisis, "
            "requiring immediate intervention. Your mind has been stabilized, but "
            "the effects of your ordeal remain. Recovery will take time and care."
        )

        return "\n".join(recap_parts)

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Recap generation errors unpredictable, must return fallback
        logger.warning("Failed to generate narrative recap", player_id=player_id, error=str(e))
        return (
            "The sanitarium staff provides a general overview: you experienced a severe "
            "lucidity crisis requiring immediate intervention. Your mind has been stabilized, "
            "but recovery will require time and care."
        )


__all__ = ["handle_debrief_command", "DEBRIEF_PENDING_ACTION_CODE"]
