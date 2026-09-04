"""NPC instance management commands (spawn, despawn, move, stats)."""

import inspect
from typing import Any

from ...alias_storage import AliasStorage
from ...npc_database import get_npc_session
from ...services.npc_instance_service import get_npc_instance_service
from ...services.npc_service import npc_service
from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _normalize_spawn_room_id(val: str | None) -> str | None:
    """'npc' means current location; return None to resolve from player."""
    return None if val and val.lower() == "npc" else val


def _parse_npc_spawn_numeric(first_arg: str, args: list[str]) -> tuple[int, str | None] | None:
    """Parse numeric definition_id case. Returns (definition_id, room_id) or None if not numeric."""
    try:
        definition_id = int(first_arg)
        room_id = args[2] if len(args) >= 3 else None
        return (definition_id, _normalize_spawn_room_id(room_id))
    except ValueError:
        return None


def _parse_npc_spawn_name(first_arg: str, args: list[str]) -> tuple[str, int, str | None]:
    """Parse name-based spawn. Returns (npc_name, quantity, room_id)."""
    quantity = 1
    room_id: str | None = None
    if len(args) >= 3 and args[2].isdigit():
        quantity = int(args[2])
        room_id = args[3] if len(args) >= 4 else None
    else:
        room_id = args[2] if len(args) >= 3 else None
    return (first_arg, quantity, _normalize_spawn_room_id(room_id))


def _parse_npc_spawn_args(args: list[str]) -> tuple[int | None, str | None, int, str | None, str | None]:
    """
    Parse args for npc spawn. Returns (definition_id, npc_name, quantity, room_id, error).
    If error is set, caller should return it. definition_id or npc_name is set (not both).
    """
    usage = (
        "Usage: npc spawn <definition_id|name> [quantity] [room_id] "
        "(quantity only for name; room_id defaults to current room)"
    )
    if len(args) < 2:
        return (None, None, 0, None, usage)
    first_arg = args[1]
    numeric = _parse_npc_spawn_numeric(first_arg, args)
    if numeric is not None:
        definition_id, room_id = numeric
        return (definition_id, None, 1, room_id, None)
    npc_name, quantity, room_id = _parse_npc_spawn_name(first_arg, args)
    return (None, npc_name, quantity, room_id, None)


async def _resolve_definition_id_from_name(npc_name: str) -> int | None:
    """Resolve NPC definition ID by name. Returns None if not found."""
    definition = None
    async for session in get_npc_session():
        definition = await npc_service.get_npc_definition_by_name(session, npc_name)
        break
    return int(definition.id) if definition else None


async def _resolve_spawn_room_id(request: Any, player_name: str, room_id: str | None) -> tuple[str | None, str | None]:
    """Resolve room_id from player's current room when room_id is None. Returns (room_id, error)."""
    if room_id:
        return (room_id, None)
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    if not player_service:
        return (None, "Cannot determine spawn location. Specify room_id explicitly.")
    _maybe_coro = player_service.resolve_player_name(player_name)
    player_obj = await _maybe_coro if inspect.isawaitable(_maybe_coro) else _maybe_coro
    if not player_obj:
        return (None, "Player not found. Specify room_id explicitly.")
    resolved = getattr(player_obj, "current_room_id", None)
    if not resolved:
        return (None, "You have no current room. Specify room_id explicitly.")
    return (resolved, None)


async def _resolve_spawn_params(
    command_data: dict[str, Any],
    request: Any,
    player_name: str,
) -> tuple[int | None, str | None, int, str | None]:
    """
    Resolve definition_id, room_id, and quantity for spawn. Returns (definition_id, room_id, quantity, error).
    If error is set, caller should return it.
    """
    args = command_data.get("args", [])
    definition_id, npc_name, quantity, room_id, parse_error = _parse_npc_spawn_args(args)
    if parse_error:
        return (None, None, 0, parse_error)

    if npc_name is not None:
        definition_id = await _resolve_definition_id_from_name(npc_name)
        if definition_id is None:
            return (None, None, 0, f"No NPC definition named '{npc_name}'. Use 'npc list' to see definitions.")

    room_id, room_error = await _resolve_spawn_room_id(request, player_name, room_id)
    if room_error:
        return (None, None, 0, room_error)
    if definition_id is None or room_id is None:
        return (None, None, 0, "Internal error: spawn parameters not resolved. Please try again.")

    return (definition_id, room_id, quantity, None)


async def _execute_spawn_loop(
    definition_id: int,
    room_id: str,
    quantity: int,
    player_name: str,
) -> dict[str, str]:
    """Run the spawn loop and return result message or error."""
    try:
        instance_service = get_npc_instance_service()
        spawned = 0
        for _ in range(quantity):
            await instance_service.spawn_npc_instance(definition_id, room_id)
            spawned += 1

        logger.info(
            "NPC spawned",
            admin_name=player_name,
            definition_id=definition_id,
            room_id=room_id,
            quantity=spawned,
        )
        msg = (
            f"NPC spawned successfully in {room_id}"
            if spawned == 1
            else f"{spawned} NPCs spawned successfully in {room_id}"
        )
        return {"result": msg}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error spawning NPC", admin_name=player_name, error=str(e))
        return {"result": f"Error spawning NPC: {str(e)}"}


async def handle_npc_spawn_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC spawning command. Supports definition_id or name; room_id defaults to current room."""
    logger.debug("Processing NPC spawn command", player_name=player_name)

    definition_id, room_id, quantity, resolve_error = await _resolve_spawn_params(command_data, request, player_name)
    if resolve_error:
        return {"result": resolve_error}
    if definition_id is None or room_id is None:
        return {"result": "Internal error: spawn parameters not resolved. Please try again."}

    return await _execute_spawn_loop(definition_id, room_id, quantity, player_name)


async def handle_npc_despawn_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC despawning command."""
    logger.debug("Processing NPC despawn command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 2:
        return {"result": "Usage: npc despawn <npc_id>"}

    npc_id = args[1]

    try:
        instance_service = get_npc_instance_service()
        result = await instance_service.despawn_npc_instance(npc_id)

        if not result:
            return {"result": f"NPC {npc_id} not found or already despawned"}

        logger.info("NPC despawned", npc_id=npc_id, admin_name=player_name)
        return {"result": f"NPC {npc_id} despawned successfully"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error despawning NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error despawning NPC: {str(e)}"}


async def handle_npc_move_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC movement command."""
    logger.debug("Processing NPC move command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 3:
        return {"result": "Usage: npc move <npc_id> <room_id>"}

    npc_id = args[1]
    room_id = args[2]

    try:
        instance_service = get_npc_instance_service()
        result = await instance_service.move_npc_instance(npc_id, room_id)

        if not result:
            return {"result": f"NPC {npc_id} not found or could not be moved"}

        logger.info("NPC moved", npc_id=npc_id, admin_name=player_name, room_id=room_id)
        return {"result": f"NPC {npc_id} moved to {room_id}"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error moving NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error moving NPC: {str(e)}"}


async def handle_npc_stats_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC stats command."""
    logger.debug("Processing NPC stats command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 2:
        return {"result": "Usage: npc stats <npc_id>"}

    npc_id = args[1]

    try:
        instance_service = get_npc_instance_service()
        stats = await instance_service.get_npc_stats(npc_id)

        if not stats:
            return {"result": f"NPC {npc_id} not found"}

        result_lines = [f"NPC {npc_id} stats:"]
        for key, value in stats.items():
            result_lines.append(f"  {key}: {value}")

        logger.info("NPC stats retrieved", npc_id=npc_id, admin_name=player_name)
        return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error getting NPC stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC stats: {str(e)}"}
