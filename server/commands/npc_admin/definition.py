"""NPC definition management commands (create, edit, delete, list)."""

from collections.abc import Callable
from typing import Any

from ...alias_storage import AliasStorage
from ...models.npc import NPCDefinitionType
from ...services.npc_service import NPCDefinitionUpdateParams, npc_service
from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _parse_npc_edit_args(args: list[Any]) -> tuple[int, str, Any] | dict[str, str]:
    """
    Parse and validate NPC edit command args.

    Returns:
        (npc_id, field, value) on success, or an error result dict on validation failure.
    """
    if len(args) < 4:
        return {"result": "Usage: npc edit <id> <field> <value>"}
    try:
        npc_id = int(args[1])
    except ValueError:
        return {"result": f"Invalid NPC ID: {args[1]}"}
    field = args[2]
    value = args[3]
    valid_fields = ["name", "npc_type", "sub_zone_id", "room_id"]
    if field not in valid_fields:
        return {"result": f"Invalid field: {field}. Valid fields: {', '.join(valid_fields)}"}
    if field == "npc_type":
        try:
            value = NPCDefinitionType(value)
        except ValueError:
            valid_types = [t.value for t in NPCDefinitionType]
            return {"result": f"Invalid NPC type: {value}. Valid types: {', '.join(valid_types)}"}
    return (npc_id, field, value)


_NPC_EDIT_FIELD_BUILDERS: dict[str, Callable[[Any], NPCDefinitionUpdateParams]] = {
    "name": lambda value: {"name": value},
    "description": lambda value: {"description": value},
    "npc_type": lambda value: {"npc_type": value},
    "sub_zone_id": lambda value: {"sub_zone_id": value},
    "room_id": lambda value: {"room_id": value},
    "required_npc": lambda value: {"required_npc": value},
    "max_population": lambda value: {"max_population": value},
    "spawn_probability": lambda value: {"spawn_probability": value},
    "base_stats": lambda value: {"base_stats": value},
    "behavior_config": lambda value: {"behavior_config": value},
    "ai_integration_stub": lambda value: {"ai_integration_stub": value},
}


def _build_npc_edit_params(field: str, value: Any) -> tuple[NPCDefinitionUpdateParams | None, dict[str, str] | None]:
    """Map a single NPC field/value into NPCDefinitionUpdateParams, or return an error dict."""
    builder = _NPC_EDIT_FIELD_BUILDERS.get(field)
    if builder is None:
        return None, {"result": f"Unsupported NPC field: {field}"}
    return builder(value), None


async def _execute_npc_edit(request: Any, npc_id: int, field: str, value: Any, player_name: str) -> dict[str, str]:
    """Run NPC definition update in DB session. Returns result or error dict."""
    try:
        app = request.app if request else None
        if not app or not hasattr(app.state, "db_session_maker"):
            return {"result": "Database not available."}

        async with app.state.db_session_maker() as session:
            params, error = _build_npc_edit_params(field, value)
            if error:
                return error
            if params is None:
                raise RuntimeError("params must be set when error is None")

            definition = await npc_service.update_npc_definition(
                session=session,
                definition_id=npc_id,
                params=params,
            )
            if not definition:
                return {"result": f"NPC definition {npc_id} not found"}

            logger.info("NPC definition updated", npc_id=npc_id, admin_name=player_name, field=field, value=value)
            return {"result": f"NPC definition {npc_id} updated successfully"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error editing NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error editing NPC: {str(e)}"}


async def handle_npc_create_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC creation command."""
    logger.debug("Processing NPC create command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 5:
        return {"result": "Usage: npc create <name> <type> <sub_zone_id> <room_id>"}

    name = args[1]
    npc_type_str = args[2]
    sub_zone_id = args[3]
    room_id = args[4]

    try:
        npc_type = NPCDefinitionType(npc_type_str)
    except ValueError:
        valid_types = [t.value for t in NPCDefinitionType]
        return {"result": f"Invalid NPC type: {npc_type_str}. Valid types: {', '.join(valid_types)}"}

    try:
        app = request.app if request else None
        if not app or not hasattr(app.state, "db_session_maker"):
            return {"result": "Database not available."}

        async with app.state.db_session_maker() as session:
            definition = await npc_service.create_npc_definition(
                session,
                {
                    "name": name,
                    "description": None,
                    "npc_type": npc_type,
                    "sub_zone_id": sub_zone_id,
                    "room_id": room_id,
                    "base_stats": {},
                    "behavior_config": {},
                    "ai_integration_stub": {},
                },
            )

            logger.info("NPC created successfully", npc_name=name, admin_name=player_name, npc_id=definition.id)
            return {"result": f"NPC '{name}' created successfully with ID {definition.id}"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error creating NPC", admin_name=player_name, error=str(e))
        return {"result": f"Error creating NPC: {str(e)}"}


async def handle_npc_edit_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC editing command."""
    logger.debug("Processing NPC edit command", player_name=player_name)

    parsed = _parse_npc_edit_args(command_data.get("args", []))
    if isinstance(parsed, dict):
        return parsed
    npc_id, field, value = parsed
    return await _execute_npc_edit(request, npc_id, field, value, player_name)


async def handle_npc_delete_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC deletion command."""
    logger.debug("Processing NPC delete command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 2:
        return {"result": "Usage: npc delete <id>"}

    try:
        npc_id = int(args[1])
    except ValueError:
        return {"result": f"Invalid NPC ID: {args[1]}"}

    try:
        app = request.app if request else None
        if not app or not hasattr(app.state, "db_session_maker"):
            return {"result": "Database not available."}

        async with app.state.db_session_maker() as session:
            deleted = await npc_service.delete_npc_definition(session, npc_id)

            if not deleted:
                return {"result": f"NPC definition {npc_id} not found"}

            logger.info("NPC definition deleted", npc_id=npc_id, admin_name=player_name)
            return {"result": f"NPC definition {npc_id} deleted successfully"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error deleting NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error deleting NPC: {str(e)}"}


async def handle_npc_list_command(
    _command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC listing command."""
    logger.debug("Processing NPC list command", player_name=player_name)

    try:
        app = request.app if request else None
        if not app or not hasattr(app.state, "db_session_maker"):
            return {"result": "Database not available."}

        async with app.state.db_session_maker() as session:
            definitions = await npc_service.get_npc_definitions(session)

            if not definitions:
                return {"result": "No NPC definitions found"}

            result_lines = ["NPC Definitions:"]
            for definition in definitions:
                result_lines.append(f"  ID {definition.id}: {definition.name} ({definition.npc_type})")
                result_lines.append(f"    Zone: {definition.sub_zone_id}, Room: {definition.room_id}")

            logger.info("NPC definitions listed", admin_name=player_name, count=len(definitions))
            return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error listing NPCs", admin_name=player_name, error=str(e))
        return {"result": f"Error listing NPCs: {str(e)}"}
