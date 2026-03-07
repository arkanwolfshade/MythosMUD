"""
Combat command handler singleton and public async command entry points.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

from typing import Any

from server.alias_storage import AliasStorage
from server.commands.combat_handler import CombatCommandHandler

_combat_command_handler: CombatCommandHandler | None = None  # pylint: disable=invalid-name  # Reason: Singleton


def get_combat_command_handler(app: Any | None = None) -> CombatCommandHandler:
    """
    Get the global combat command handler instance, creating it if needed.
    Uses lazy initialization so combat_service from app.state is ready.
    """
    global _combat_command_handler  # pylint: disable=global-statement  # Reason: Singleton
    if _combat_command_handler is None:
        if app is None:
            raise RuntimeError("Cannot initialize combat command handler without app instance")
        container = getattr(app.state, "container", None)
        if not container:
            raise RuntimeError("Cannot initialize combat command handler without container")
        _combat_command_handler = CombatCommandHandler(
            combat_service=getattr(container, "combat_service", None),
            event_bus=getattr(container, "event_bus", None),
            player_combat_service=getattr(container, "player_combat_service", None),
            connection_manager=getattr(container, "connection_manager", None),
            async_persistence=getattr(container, "async_persistence", None),
            item_prototype_registry=getattr(container, "item_prototype_registry", None),
            party_service=getattr(container, "party_service", None),
            movement_service=getattr(container, "movement_service", None),
            player_position_service=getattr(container, "player_position_service", None),
        )
    return _combat_command_handler


async def handle_attack_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle attack command."""
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_punch_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle punch command (alias for attack)."""
    command_data = command_data.copy()
    command_data["command_type"] = "punch"
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_kick_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle kick command (alias for attack)."""
    command_data = command_data.copy()
    command_data["command_type"] = "kick"
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_flee_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle flee command: leave combat and move to random adjacent room."""
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_flee_command(command_data, current_user, request, alias_storage, player_name)


async def handle_strike_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle strike command (alias for attack)."""
    command_data = command_data.copy()
    command_data["command_type"] = "strike"
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_taunt_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle taunt command: draw NPC aggro (ADR-016). Room-local only."""
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_taunt_command(command_data, current_user, request, alias_storage, player_name)
