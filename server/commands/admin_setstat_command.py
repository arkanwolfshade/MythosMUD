"""
Admin command to set player statistics.

This module provides the handler for the admin set command,
allowing administrators to set any player statistic including attributes,
DP, MP, lucidity, occult, and corruption.
"""

# pylint: disable=too-many-arguments,too-many-locals  # Reason: Admin command handler matches standard command signature

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import cast

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..exceptions import DatabaseError
from ..realtime.envelope import build_event
from ..realtime.posture_notify import emit_posture_change, normalize_posture
from ..services.corruption_service import CorruptionPersistenceProtocol, CorruptionService
from ..services.lucidity_helpers import CatatoniaObserverProtocol
from ..services.lucidity_service import LucidityService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .admin_setlucidity_command import get_current_lcd
from .admin_setstat_support import (
    AdminSetStatApplyContext,
    AdminSetStatLogContext,
    AdminSetStatNotifyContext,
    SetStatApp,
    SetStatConnectionManager,
    SetStatPlayerService,
    SetStatRequest,
    SetStatTargetPlayer,
    build_set_stat_error_response,
    calculate_stat_warnings,
    get_app_or_error,
    log_admin_set_stat,
    parse_set_stat_args,
    resolve_admin_services_and_permissions,
    stat_change_notification_text,
    target_player_uuid,
    validate_set_stat_inputs,
)

logger = get_logger(__name__)

__all__ = ["_handle_admin_set_stat_command", "AdminSetStatNotifyContext"]


def _get_catatonia_registry_from_app(app: object) -> CatatoniaObserverProtocol | None:
    """Get catatonia registry from container, fallback to app.state."""
    if not app:
        return None
    state = cast("object | None", getattr(app, "state", None))
    if state is None:
        return None
    container = cast("object | None", getattr(state, "container", None))
    if container is not None:
        return cast("CatatoniaObserverProtocol | None", getattr(container, "catatonia_registry", None))
    return cast("CatatoniaObserverProtocol | None", getattr(state, "catatonia_registry", None))


async def _maybe_attach_dp_posture_message(
    connection_manager: SetStatConnectionManager,
    target_player_obj: SetStatTargetPlayer,
    target_player_id: uuid.UUID,
    update_payload: dict[str, object],
    *,
    stat_key: str,
    previous_position: str | None,
    updated_stats: Mapping[str, object],
) -> None:
    if stat_key != "current_dp" or previous_position is None:
        return
    posture_message = await emit_posture_change(
        connection_manager,
        player_id=target_player_id,
        display_name=str(target_player_obj.name or "Unknown"),
        room_id=str(target_player_obj.current_room_id) if target_player_obj.current_room_id else None,
        previous_position=previous_position,
        new_position=normalize_posture(updated_stats.get("position")),
        include_self_message=True,
        send_personal_update=False,
    )
    if posture_message:
        update_payload["posture_message"] = posture_message


async def _notify_player_stat_change(ctx: AdminSetStatNotifyContext) -> None:
    """Notify target player of stat change and send player update event."""
    try:
        connection_manager = ctx.app.state.connection_manager
        if connection_manager is None:
            return

        target_player_id = target_player_uuid(ctx.target_player_obj)
        if target_player_id is None:
            return

        notification_event = build_event(
            "command_response",
            {
                "result": stat_change_notification_text(
                    ctx.stat_name_input,
                    ctx.old_value,
                    ctx.value,
                    ctx.warning_message,
                    ctx.range_warning,
                )
            },
            player_id=target_player_id,
            connection_manager=connection_manager,
        )
        _ = await connection_manager.send_personal_message(target_player_id, notification_event)

        if not ctx.include_player_update:
            return

        updated_stats = ctx.target_player_obj.get_stats()
        update_payload: dict[str, object] = {"player_id": str(target_player_id), "stats": updated_stats}
        await _maybe_attach_dp_posture_message(
            connection_manager,
            ctx.target_player_obj,
            target_player_id,
            update_payload,
            stat_key=ctx.stat_key,
            previous_position=ctx.previous_position,
            updated_stats=updated_stats,
        )
        player_update_event = build_event(
            "player_update",
            update_payload,
            player_id=target_player_id,
            connection_manager=connection_manager,
        )
        _ = await connection_manager.send_personal_message(target_player_id, player_update_event)
    except (AttributeError, TypeError, ValueError, OSError) as notify_exc:
        logger.warning("Failed to notify target player of stat change", error=str(notify_exc))


def _mutate_player_stat(ctx: AdminSetStatApplyContext, stats: dict[str, object]) -> str | None:
    """Apply DP or generic stat mutation; return previous posture when DP changes."""
    if ctx.stat_key == "current_dp":
        previous_position = normalize_posture(stats.get("position"))
        _ = ctx.target_player_obj.apply_dp_change(ctx.value)
        return previous_position
    stats[ctx.stat_key] = ctx.value
    ctx.target_player_obj.set_stats(stats)
    return None


async def _resolve_admin_id(ctx: AdminSetStatApplyContext) -> str:
    """Best-effort admin id for occult service metadata."""
    player_service_raw = ctx.app.state.player_service
    if player_service_raw is None:
        return ""
    player_service = cast(SetStatPlayerService, player_service_raw)
    admin = await player_service.resolve_player_name(ctx.player_name)
    return str(admin.id) if admin is not None else ""


async def _finish_occult_stat_change(
    ctx: AdminSetStatApplyContext,
    *,
    old_value: object,
    warning_message: str,
    range_warning: str,
) -> dict[str, str]:
    """Shared notify/log/result for occult service paths (no outer save_player / player_update)."""
    await _notify_player_stat_change(
        AdminSetStatNotifyContext(
            app=ctx.app,
            target_player_obj=ctx.target_player_obj,
            stat_name_input=ctx.stat_name_input,
            old_value=old_value,
            value=ctx.value,
            warning_message=warning_message,
            range_warning=range_warning,
            stat_key=ctx.stat_key,
            include_player_update=False,
        )
    )
    log_admin_set_stat(
        ctx.player_name,
        AdminSetStatLogContext(
            ctx.stat_name_input,
            ctx.target_player,
            ctx.value_input,
            ctx.target_player_obj,
            ctx.stat_key,
            old_value,
            ctx.value,
        ),
    )
    logger.info(
        "Admin set command successful",
        admin_name=ctx.player_name,
        target_player=ctx.target_player,
        stat_name=ctx.stat_key,
        old_value=old_value,
        new_value=ctx.value,
    )
    return {
        "result": (
            f"Set {ctx.target_player}'s {ctx.stat_name_input} from {old_value} to {ctx.value}."
            + warning_message
            + range_warning
        )
    }


async def _apply_corruption_via_service(ctx: AdminSetStatApplyContext) -> dict[str, str]:
    """Route corruption through CorruptionService with permanence-floor bypass (#816)."""
    stats = ctx.target_player_obj.get_stats()
    old_value = coerce_int(stats.get("corruption", 0), default=0)
    warning_message, range_warning = calculate_stat_warnings(ctx.stat_key, ctx.value, stats)
    player_id = target_player_uuid(ctx.target_player_obj)
    if player_id is None:
        return {"result": f"Player '{ctx.target_player}' has no valid id."}

    delta = ctx.value - old_value
    persistence = cast(CorruptionPersistenceProtocol, cast(object, ctx.persistence))
    _ = await CorruptionService(persistence).apply_corruption_adjustment(
        player_id,
        delta,
        reason_code="admin_set",
        bypass_permanence_floor=True,
        metadata={
            "admin_name": ctx.player_name,
            "admin_id": await _resolve_admin_id(ctx),
            "previous_corruption": old_value,
            "target_corruption": ctx.value,
            "command": "admin setstat",
        },
    )
    return await _finish_occult_stat_change(
        ctx, old_value=old_value, warning_message=warning_message, range_warning=range_warning
    )


async def _apply_lucidity_via_service(ctx: AdminSetStatApplyContext) -> dict[str, str]:
    """Route lucidity through LucidityService (same write path as admin setlucidity)."""
    stats = ctx.target_player_obj.get_stats()
    warning_message, range_warning = calculate_stat_warnings(ctx.stat_key, ctx.value, stats)
    player_id = target_player_uuid(ctx.target_player_obj)
    if player_id is None:
        return {"result": f"Player '{ctx.target_player}' has no valid id."}

    catatonia_observer = _get_catatonia_registry_from_app(ctx.app)
    async for session in get_async_session():
        lucidity_service = LucidityService(session, catatonia_observer=catatonia_observer)
        current_lcd = await get_current_lcd(session, player_id)
        delta = ctx.value - current_lcd
        try:
            _ = await lucidity_service.apply_lucidity_adjustment(
                player_id=player_id,
                delta=delta,
                reason_code="admin_set",
                metadata={
                    "admin_name": ctx.player_name,
                    "admin_id": await _resolve_admin_id(ctx),
                    "previous_lcd": current_lcd,
                    "target_lcd": ctx.value,
                    "command": "admin setstat",
                },
            )
            await session.commit()
        except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError) as adjust_exc:
            await session.rollback()
            logger.error(
                "Admin setstat lucidity adjustment failed",
                player_name=ctx.player_name,
                target_player=ctx.target_player,
                error=str(adjust_exc),
                error_type=type(adjust_exc).__name__,
            )
            return {"result": f"Error setting lucidity for {ctx.target_player}: {str(adjust_exc)}"}
        return await _finish_occult_stat_change(
            ctx, old_value=current_lcd, warning_message=warning_message, range_warning=range_warning
        )
    return {"result": "Database session could not be established. Please try again."}


async def _apply_stat_change_and_build_result(
    ctx: AdminSetStatApplyContext,
) -> dict[str, str]:
    """Apply stat change, persist, notify, log; return success result dict."""
    if ctx.stat_key == "corruption":
        return await _apply_corruption_via_service(ctx)
    if ctx.stat_key == "lucidity":
        return await _apply_lucidity_via_service(ctx)

    stats = ctx.target_player_obj.get_stats()
    old_value = stats.get(ctx.stat_key)
    warning_message, range_warning = calculate_stat_warnings(ctx.stat_key, ctx.value, stats)
    previous_position = _mutate_player_stat(ctx, stats)
    await ctx.persistence.save_player(ctx.target_player_obj)
    await _notify_player_stat_change(
        AdminSetStatNotifyContext(
            app=ctx.app,
            target_player_obj=ctx.target_player_obj,
            stat_name_input=ctx.stat_name_input,
            old_value=old_value,
            value=ctx.value,
            warning_message=warning_message,
            range_warning=range_warning,
            stat_key=ctx.stat_key,
            previous_position=previous_position,
        )
    )
    log_admin_set_stat(
        ctx.player_name,
        AdminSetStatLogContext(
            ctx.stat_name_input,
            ctx.target_player,
            ctx.value_input,
            ctx.target_player_obj,
            ctx.stat_key,
            old_value,
            ctx.value,
        ),
    )
    logger.info(
        "Admin set command successful",
        admin_name=ctx.player_name,
        target_player=ctx.target_player,
        stat_name=ctx.stat_key,
        old_value=old_value,
        new_value=ctx.value,
    )
    return {
        "result": (
            f"Set {ctx.target_player}'s {ctx.stat_name_input} from {old_value} to {ctx.value}."
            + warning_message
            + range_warning
        )
    }


async def _execute_admin_set_stat(
    app: SetStatApp,
    player_name: str,
    stat_name_input: str,
    target_player: str,
    value_input: str | int | None,
    stat_key: str,
    value: int,
) -> dict[str, str]:
    """Resolve services and apply the validated set-stat change."""
    service_result = await resolve_admin_services_and_permissions(app, player_name, target_player)
    if isinstance(service_result, dict):
        return service_result
    persistence, target_player_obj = service_result
    try:
        return await _apply_stat_change_and_build_result(
            AdminSetStatApplyContext(
                app=app,
                persistence=persistence,
                target_player_obj=target_player_obj,
                stat_name_input=stat_name_input,
                target_player=target_player,
                stat_key=stat_key,
                value=value,
                value_input=value_input,
                player_name=player_name,
            )
        )
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError) as e:
        return build_set_stat_error_response(player_name, stat_name_input, target_player, value_input, e)


async def _handle_admin_set_stat_command(  # pylint: disable=too-many-arguments,too-many-locals  # Reason: Admin command requires many parameters and intermediate variables for complex stat setting logic
    command_data: Mapping[str, object],
    current_user: Mapping[str, object],
    request: SetStatRequest | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle admin set <stat_name> <target_player> <value>."""
    _ = current_user
    _ = alias_storage
    logger.debug("Processing admin set command", player_name=player_name, command_data=command_data)

    app, app_error = get_app_or_error(request, player_name)
    if app_error is not None or app is None:
        return app_error or {"result": "Admin set functionality is not available."}

    stat_name_input, target_player, value_input = parse_set_stat_args(command_data)
    validation_result = validate_set_stat_inputs(stat_name_input, target_player, value_input, player_name)
    if isinstance(validation_result, dict):
        return validation_result

    stat_key, value = validation_result
    if not stat_name_input or not target_player:
        return {"result": "Target player and stat name are required."}

    return await _execute_admin_set_stat(app, player_name, stat_name_input, target_player, value_input, stat_key, value)
