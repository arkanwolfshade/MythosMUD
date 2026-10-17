"""
Debrief command for MythosMUD.

After a delirium or sanitarium respawn a player has a pending debrief: a narrative recap and, optionally, an
immediate therapy session. The logic lives in ``services.debrief_service``; Dr. Morgan runs it through dialogue (the
``debrief`` scripted action, ADR-028), which is how players reach it.

PARKED (#813, #872): this handler is deliberately NOT registered in ``_COMMAND_HANDLERS``
(server/commands/command_service.py). Registered as a bare no-arg command it would let a player self-administer their
debrief with no NPC present. ``args`` arrives from the real pipeline as a **list** (``_prepare_command_data``), which
``_wants_therapy`` handles; a string is accepted too.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import cast

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..services.debrief_service import perform_debrief
from ..services.lucidity_service import CatatoniaObserverProtocol
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from .communication_commands_support import AsyncPersistenceForPose, app_from_request, get_pose_persistence

logger = get_logger(__name__)

_THERAPY_ARGS = frozenset({"therapy", "yes", "y", "t"})


def _get_catatonia_registry_from_app(app: object | None) -> CatatoniaObserverProtocol | None:
    """Catatonia registry from the app container, falling back to app.state."""
    state = cast(object | None, getattr(app, "state", None))
    container = cast(object | None, getattr(state, "container", None))
    source = container if container else state
    return cast(CatatoniaObserverProtocol | None, getattr(source, "catatonia_registry", None))


def _wants_therapy(command_data: Mapping[str, object]) -> bool:
    """True when the first argument asks for the immediate therapy session (list or string ``args``)."""
    args: object = command_data.get("args") or []
    items = cast(list[object], args) if isinstance(args, list) else [args]
    first = items[0] if items else ""
    return isinstance(first, str | int) and str(first).strip().lower() in _THERAPY_ARGS


async def _validate_debrief_context(
    persistence: AsyncPersistenceForPose | None, username: str, player_name: str
) -> tuple[Player | None, dict[str, str] | None]:
    """Validate persistence and player existence for the debrief command."""
    if not persistence:
        logger.error("Debrief command invoked without persistence", player=player_name)
        return None, {"result": "The sanitarium records are inaccessible. The ley lines waver."}
    player = cast(Player | None, await persistence.get_player_by_name(username))
    if not player:
        logger.error("Debrief command failed to locate player", username=username)
        return None, {"result": "Your identity wavers in the void. Try again after stabilizing your presence."}
    return player, None


async def handle_debrief_command(
    command_data: Mapping[str, object],
    current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the debrief command: recap plus optional therapy for a player with a pending debrief."""
    app = app_from_request(request)
    username = get_username_from_user(current_user)
    player, context_error = await _validate_debrief_context(get_pose_persistence(app), username, player_name)
    if context_error or player is None:
        return context_error or {"result": "Your identity wavers in the void."}
    outcome = await perform_debrief(
        player, wants_therapy=_wants_therapy(command_data), catatonia_observer=_get_catatonia_registry_from_app(app)
    )
    return {"result": outcome.message}


__all__ = ["handle_debrief_command"]
