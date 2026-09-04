"""NPC test-occupants command for debugging occupant queries."""

import inspect
from typing import Any

from ...alias_storage import AliasStorage
from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def _get_room_id_for_test_occupants(
    command_data: dict[str, Any], player_obj: Any
) -> tuple[str | None, dict[str, str] | None]:
    """Get room_id from args or current room. Returns (room_id, error_result)."""
    args = command_data.get("args", [])
    room_id = args[1] if len(args) > 1 else None

    if not room_id:
        room_id = getattr(player_obj, "current_room_id", None)
        if not room_id:
            return None, {"result": "No room ID provided and player has no current room."}

    return room_id, None


def _get_event_handler_for_test_occupants(app: Any) -> tuple[Any | None, dict[str, str] | None]:
    """Get event handler from app.state. Returns (event_handler, error_result)."""
    event_handler = getattr(app.state, "event_handler", None)
    if not event_handler:
        event_handler = getattr(app.state.container, "real_time_event_handler", None)

    if not event_handler:
        return None, {"result": "Event handler not available. Cannot test occupants directly."}

    return event_handler, None


def _separate_occupants(occupants_info: list[dict[str, Any]] | None) -> tuple[list[str], list[str]]:
    """Separate occupants into players and NPCs."""
    players: list[str] = []
    npcs: list[str] = []

    for occ in occupants_info or []:
        if isinstance(occ, dict):
            if "player_name" in occ:
                players.append(occ.get("player_name", "Unknown"))
            elif "npc_name" in occ:
                npcs.append(occ.get("npc_name", "Unknown"))

    return players, npcs


def _format_occupants_result(room_id: str, players: list[str], npcs: list[str]) -> str:
    """Format occupants result as a string."""
    result_lines = [f"Occupants in room: {room_id}", ""]
    result_lines.append(f"Players ({len(players)}):")
    if players:
        for player in players:
            result_lines.append(f"  - {player}")
    else:
        result_lines.append("  (none)")

    result_lines.append(f"\nNPCs ({len(npcs)}):")
    if npcs:
        for npc in npcs:
            result_lines.append(f"  - {npc}")
    else:
        result_lines.append("  (none)")

    result_lines.append("\nOccupant update broadcast triggered. Check logs for detailed NPC query information.")
    return "\n".join(result_lines)


async def _resolve_app_and_player_for_test_occupants(
    request: Any, player_name: str
) -> tuple[Any | None, Any | None, dict[str, str] | None]:
    """Resolve application and player object for NPC test occupants command."""
    app = request.app if request else None
    if not app:
        return None, None, {"result": "Server application not available."}

    player_service = getattr(app.state, "player_service", None)
    if not player_service:
        return None, None, {"result": "Player service not available."}

    maybe_coro = player_service.resolve_player_name(player_name)
    player_obj = await maybe_coro if inspect.isawaitable(maybe_coro) else maybe_coro
    if not player_obj:
        return None, None, {"result": "Player not found."}

    return app, player_obj, None


async def _resolve_room_and_handler_for_test_occupants(
    command_data: dict[str, Any], app: Any, player_obj: Any
) -> tuple[Any | None, str | None, dict[str, str] | None]:
    """Resolve room_id and event handler for NPC test occupants command."""
    room_id, error_result = await _get_room_id_for_test_occupants(command_data, player_obj)
    if error_result:
        return None, None, error_result

    event_handler, error_result = _get_event_handler_for_test_occupants(app)
    if error_result or event_handler is None:
        return None, None, error_result or {"result": "Event handler not available."}

    if room_id is None:
        return None, None, {"result": "Room ID is required for testing occupants."}

    return event_handler, room_id, None


async def _resolve_test_occupants_context(
    command_data: dict[str, Any], request: Any, player_name: str
) -> tuple[tuple[Any, str] | None, dict[str, str] | None]:
    """
    Resolve application, player, room_id, and event handler for NPC test occupants command.

    Returns (event_handler, room_id), None on success, or (None, error_result) on failure.
    """
    app, player_obj, error_result = await _resolve_app_and_player_for_test_occupants(request, player_name)
    if error_result:
        return None, error_result

    event_handler, room_id, error_result = await _resolve_room_and_handler_for_test_occupants(
        command_data, app, player_obj
    )
    if error_result:
        return None, error_result

    if event_handler is None or room_id is None:
        raise RuntimeError("event_handler and room_id must be set when error_result is None")
    return (event_handler, room_id), None


async def handle_npc_test_occupants_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle NPC test occupants command - manually trigger occupant query for debugging.

    Usage: npc test-occupants [room_id]
    If room_id is not provided, uses the current room.
    """
    logger.info("Processing NPC test occupants command", admin_name=player_name)

    try:
        context, error_result = await _resolve_test_occupants_context(command_data, request, player_name)
        if error_result:
            return error_result
        if context is None:
            raise RuntimeError("context must be set when error_result is None")
        event_handler, room_id = context

        logger.info("Manually triggering occupant query for testing", admin_name=player_name, room_id=room_id)

        occupants_info = event_handler._get_room_occupants(room_id)  # noqa: SLF001  # pylint: disable=protected-access
        players, npcs = _separate_occupants(occupants_info)

        await event_handler.send_room_occupants_update(room_id)

        result_text = _format_occupants_result(room_id, players, npcs)

        logger.info(
            "NPC test occupants command completed",
            admin_name=player_name,
            room_id=room_id,
            player_count=len(players),
            npc_count=len(npcs),
        )

        return {"result": result_text}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error testing NPC occupants", admin_name=player_name, error=str(e), exc_info=True)
        return {"result": f"Error testing NPC occupants: {str(e)}"}
