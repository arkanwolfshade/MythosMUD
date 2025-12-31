"""
Teach command handler for learning spells from NPC teachers.

This module handles the /teach command for NPCs to teach spells to players.
"""

from typing import Any

from server.alias_storage import AliasStorage
from server.schemas.target_resolution import TargetType
from server.services.target_resolution_service import TargetResolutionService
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def handle_teach_command(
    command_data: dict,
    current_user: dict,
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

    # Get services from app state
    app = request.app if request else None
    if not app:
        return {"result": "System error: application not available."}

    persistence = getattr(app.state, "persistence", None)
    spell_learning_service = getattr(app.state, "spell_learning_service", None)
    player_service = getattr(app.state, "player_service", None)

    if not persistence or not player_service:
        return {"result": "System error: required services not available."}

    if not spell_learning_service:
        return {"result": "Spell learning system not initialized."}

    # Get player
    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        return {"result": "You are not recognized by the cosmic forces."}

    # Extract NPC name and spell name
    args = command_data.get("args", [])
    if len(args) < 2:
        return {"result": "Usage: /teach <npc_name> <spell_name>"}

    npc_name = args[0]
    spell_name = args[1]

    # Resolve NPC target
    target_resolution_service = TargetResolutionService(persistence, player_service)
    target_result = await target_resolution_service.resolve_target(player.player_id, npc_name)

    if not target_result.success:
        return {"result": target_result.error_message or "NPC not found."}

    target_match = target_result.get_single_match()
    if not target_match:
        return {"result": target_result.error_message or "No valid target found."}

    if target_match.target_type != TargetType.NPC:
        return {"result": f"{npc_name} is not an NPC."}

    # TODO: Check if NPC is a teacher and can teach this spell
    # This would require NPC definition metadata (e.g., "teaches_spells": ["spell1", "spell2"])
    # For now, allow any NPC to teach any spell (can be restricted later)

    # Learn the spell from NPC
    result = await spell_learning_service.learn_spell_from_npc(player.player_id, target_match.target_id, spell_name)

    if not result.get("success"):
        return {"result": result.get("message", "Failed to learn spell.")}

    message = result.get("message", f"Learned {spell_name}!")
    if result.get("corruption_applied", 0) > 0:
        message += f" The forbidden knowledge has tainted your mind (+{result['corruption_applied']} corruption)."

    # TODO: Send message to room about NPC teaching
    # "Professor Armitage teaches you the spell 'Minor Heal'."

    return {"result": message}
