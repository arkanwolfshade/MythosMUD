"""
Teach command handler for learning spells from NPC teachers.

This module handles the /teach command for NPCs to teach spells to players.
"""

# pylint: disable=too-many-locals,too-many-return-statements  # Reason: Teach commands require many intermediate variables for complex teaching logic and multiple return statements for early validation returns

from typing import Any

from server.alias_storage import AliasStorage
from server.schemas.shared import TargetType
from server.services.target_resolution_service import TargetResolutionService
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user

logger = get_logger(__name__)


def _get_teach_services(app: Any) -> tuple[Any, Any, Any] | dict[str, str]:
    if not app:
        return {"result": "System error: application not available."}

    persistence = getattr(app.state, "persistence", None)
    spell_learning_service = getattr(app.state, "spell_learning_service", None)
    player_service = getattr(app.state, "player_service", None)

    if not persistence or not player_service:
        return {"result": "System error: required services not available."}
    if not spell_learning_service:
        return {"result": "Spell learning system not initialized."}
    return persistence, spell_learning_service, player_service


async def _resolve_npc_teacher(
    persistence: Any, player_service: Any, player: Any, npc_name: str
) -> Any | dict[str, str]:
    target_resolution_service = TargetResolutionService(persistence, player_service)
    target_result = await target_resolution_service.resolve_target(player.player_id, npc_name)
    if not target_result.success:
        return {"result": target_result.error_message or "NPC not found."}

    target_match = target_result.get_single_match()
    if not target_match:
        return {"result": target_result.error_message or "No valid target found."}
    if target_match.target_type != TargetType.NPC:
        return {"result": f"{npc_name} is not an NPC."}
    return target_match


def _format_teach_result(result: dict[str, Any], spell_name: str) -> dict[str, str]:
    if not result.get("success"):
        return {"result": result.get("message", "Failed to learn spell.")}

    message = result.get("message", f"Learned {spell_name}!")
    if result.get("corruption_applied", 0) > 0:
        message += f" The forbidden knowledge has tainted your mind (+{result['corruption_applied']} corruption)."
    return {"result": message}


async def handle_teach_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /teach command for learning spells from NPCs.

    Usage: /teach <npc_name> <spell_name>
    Alternative: <npc_name> teach <spell_name>

    Args:
        command_data: Command data dictionary
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name

    Returns:
        dict: Command result
    """
    logger.debug("Handling teach command", player_name=player_name, command_data=command_data)

    app = request.app if request else None
    services = _get_teach_services(app)
    if isinstance(services, dict):
        return services
    persistence, spell_learning_service, player_service = services

    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        return {"result": "You are not recognized by the cosmic forces."}

    args = command_data.get("args", [])
    if len(args) < 2:
        return {"result": "Usage: /teach <npc_name> <spell_name>"}

    npc_name = args[0]
    spell_name = args[1]

    target_match = await _resolve_npc_teacher(persistence, player_service, player, npc_name)
    if isinstance(target_match, dict):
        return target_match

    result = await spell_learning_service.learn_spell_from_npc(player.player_id, target_match.target_id, spell_name)
    return _format_teach_result(result, spell_name)
