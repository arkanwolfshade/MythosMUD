"""
Combat command handler singleton and public async command entry points.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from server.alias_storage import AliasStorage
from server.commands.combat_handler import CombatCommandHandler, CombatCommandHandlerExtras

if TYPE_CHECKING:
    from server.async_persistence import AsyncPersistenceLayer
    from server.events.event_bus import EventBus
    from server.realtime.connection_manager import ConnectionManager
    from server.services.combat_service import CombatService
    from server.services.player_combat_service import PlayerCombatService

_combat_command_handler: CombatCommandHandler | None = None  # pylint: disable=invalid-name  # Reason: Singleton


def get_combat_command_handler(app: object | None = None) -> CombatCommandHandler:
    """
    Get the global combat command handler instance, creating it if needed.
    Uses lazy initialization so combat_service from app.state is ready.
    """
    global _combat_command_handler  # pylint: disable=global-statement  # Reason: Singleton
    if _combat_command_handler is None:
        if app is None:
            raise RuntimeError("Cannot initialize combat command handler without app instance")
        app_obj: object = app
        state: object = cast(object, getattr(app_obj, "state", None))
        if state is None:
            raise RuntimeError("Cannot initialize combat command handler without app.state")
        container: object | None = cast(object | None, getattr(state, "container", None))
        if not container:
            raise RuntimeError("Cannot initialize combat command handler without container")
        container_obj: object = container
        _combat_command_handler = CombatCommandHandler(
            combat_service=cast("CombatService | None", getattr(container_obj, "combat_service", None)),
            event_bus=cast("EventBus | None", getattr(container_obj, "event_bus", None)),
            player_combat_service=cast(
                "PlayerCombatService | None", getattr(container_obj, "player_combat_service", None)
            ),
            connection_manager=cast("ConnectionManager | None", getattr(container_obj, "connection_manager", None)),
            async_persistence=cast("AsyncPersistenceLayer | None", getattr(container_obj, "async_persistence", None)),
            extras=CombatCommandHandlerExtras(
                item_prototype_registry=cast(object | None, getattr(container_obj, "item_prototype_registry", None)),
                party_service=cast(object | None, getattr(container_obj, "party_service", None)),
                movement_service=cast(object | None, getattr(container_obj, "movement_service", None)),
                player_position_service=cast(object | None, getattr(container_obj, "player_position_service", None)),
            ),
        )
    return _combat_command_handler


def _app_from_request(request: object | None) -> object | None:
    """Resolve Starlette/FastAPI app from request (or None if request is missing)."""
    if request is None:
        return None
    req: object = request
    return cast(object | None, getattr(req, "app", None))


async def handle_attack_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle attack command."""
    app = _app_from_request(request)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_punch_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle punch command (alias for attack)."""
    command_data = command_data.copy()
    command_data["command_type"] = "punch"
    app = _app_from_request(request)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_kick_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle kick command (alias for attack)."""
    command_data = command_data.copy()
    command_data["command_type"] = "kick"
    app = _app_from_request(request)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_flee_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle flee command: leave combat and move to random adjacent room."""
    app = _app_from_request(request)
    handler = get_combat_command_handler(app)
    return await handler.handle_flee_command(command_data, current_user, request, alias_storage, player_name)


async def handle_strike_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle strike command (alias for attack)."""
    command_data = command_data.copy()
    command_data["command_type"] = "strike"
    app = _app_from_request(request)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_taunt_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle taunt command: draw NPC aggro (ADR-016). Room-local only."""
    app = _app_from_request(request)
    handler = get_combat_command_handler(app)
    return await handler.handle_taunt_command(command_data, current_user, request, alias_storage, player_name)
