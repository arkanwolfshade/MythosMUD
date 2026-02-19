"""
Skills command handler (plan 10.7 V4).

Returns the active character's skills as text for the /skills slash command.
"""

import uuid
from typing import Any

from ..alias_storage import AliasStorage
from ..game.skill_service import SkillService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


def _get_container_services(request: Any) -> tuple[Any, Any, SkillService] | None:
    """Get container, persistence, and skill_service from request, or None if unavailable."""
    app = request.app if request else None
    if not app or not getattr(app.state, "container", None):
        return None
    container = app.state.container
    persistence = getattr(container, "async_persistence", None)
    skill_service = getattr(container, "skill_service", None)
    if not persistence or not isinstance(skill_service, SkillService):
        return None
    return container, persistence, skill_service


def _resolve_player_id(player: Any) -> uuid.UUID | None:
    """Extract and validate player_id from player object, returning UUID or None."""
    player_id_raw = getattr(player, "player_id", None) or getattr(player, "id", None)
    if not player_id_raw:
        return None
    try:
        return uuid.UUID(player_id_raw) if isinstance(player_id_raw, str) else player_id_raw
    except (TypeError, ValueError):
        return None


def _resolve_user_id(current_user: Any, player: Any) -> str | None:
    """Resolve user_id from current_user (auth user) or fallback to player.user_id."""
    user_id = current_user.get("id") if isinstance(current_user, dict) else getattr(current_user, "id", None)
    if not user_id:
        user_id = getattr(player, "user_id", None)
    return user_id


def _format_skills_output(skills: list[dict[str, Any]]) -> str:
    """Format skills list as text output lines."""
    lines = ["Your skills:", "---"]
    for s in sorted(skills, key=lambda x: (x.get("skill_name") or x.get("skill_key") or "")):
        name = s.get("skill_name") or s.get("skill_key") or "Unknown"
        value = s.get("value", 0)
        lines.append(f"  {name}: {value}%")
    lines.append("---")
    return "\n".join(lines)


async def handle_skills_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the /skills command: return the active character's skills as text.

    Resolves the current character by player name (from command context), then
    fetches that character's skills with ownership check and formats as lines.
    """
    _args: list[Any] = command_data.get("args", [])

    logger.debug("Processing skills command", player=player_name)

    services = _get_container_services(request)
    if not services:
        return {"result": "Skills are not available."}
    _container, persistence, skill_service = services

    try:
        player = await persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "Character not found."}

        player_id = _resolve_player_id(player)
        if not player_id:
            return {"result": "Character id is invalid."}

        user_id = _resolve_user_id(current_user, player)
        if not user_id:
            return {"result": "Authentication error."}

        skills = await skill_service.get_player_skills(player_id, user_id)
        if skills is None:
            return {"result": "You do not have access to this character's skills."}

        if not skills:
            return {"result": "No skills recorded for this character."}

        return {"result": _format_skills_output(skills)}
    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Skills command failed", player=player_name, error=str(e))
        return {"result": "Failed to load skills."}
