"""
Row-to-player mapping utilities for PlayerRepository.

Maps procedure result rows to Player domain objects.
"""

import json
from typing import Any

from server.models.player import Player, PlayerInventory


class InventoryPayload:
    """Type hint for inventory payload structure."""

    inventory: list[dict[str, Any]]
    equipped: dict[str, Any]
    version: int


def _coerce_row_stats(row: Any) -> dict[str, Any]:
    """Extract and coerce stats from row. Returns empty dict if not a dict."""
    return row.stats if isinstance(row.stats, dict) else {}


def _parse_equipped_safely(equipped_json: str) -> dict[str, Any]:
    """Parse equipped_json to dict. Returns empty dict on parse error or invalid type."""
    if not equipped_json:
        return {}
    try:
        parsed = json.loads(equipped_json)
        return parsed if isinstance(parsed, dict) else {}
    except (json.JSONDecodeError, TypeError):
        return {}


def _defaulted_strings(row: Any) -> tuple[str, str, str, str, str]:
    """Extract string fields with defaults: inventory_json, equipped_json, current_room_id, status_effects, inventory."""
    return (
        row.inventory_json or "[]",
        row.equipped_json or "{}",
        row.current_room_id or "earth_arkhamcity_sanitarium_room_foyer_001",
        row.status_effects or "[]",
        row.inventory or "[]",
    )


def _defaulted_numerics(row: Any) -> tuple[int, int, int, int, bool]:
    """Extract numeric/bool fields with defaults: experience_points, level, is_admin, profession_id, is_deleted."""
    return (
        row.experience_points or 0,
        row.level or 1,
        row.is_admin or 0,
        row.profession_id or 0,
        row.is_deleted or False,
    )


def row_to_player(row: Any) -> Player:
    """Map a procedure result row to a Player domain object."""
    player_id = row.player_id
    user_id = row.user_id
    stats = _coerce_row_stats(row)
    inv_json, equipped_json, current_room_id, status_effects, inventory = _defaulted_strings(row)
    exp, level, is_admin, profession_id, is_deleted = _defaulted_numerics(row)

    player = Player(
        player_id=str(player_id),
        user_id=str(user_id),
        name=row.name,
        inventory=inventory,
        status_effects=status_effects,
        current_room_id=current_room_id,
        respawn_room_id=row.respawn_room_id,
        experience_points=exp,
        level=level,
        is_admin=is_admin,
        profession_id=profession_id,
        created_at=row.created_at,
        last_active=row.last_active,
        stats=stats,
        is_deleted=is_deleted,
        deleted_at=row.deleted_at,
        tutorial_instance_id=row.tutorial_instance_id,
    )
    player.inventory_record = PlayerInventory(
        player_id=str(player_id),
        inventory_json=inv_json,
        equipped_json=equipped_json,
    )
    player.set_equipped_items(_parse_equipped_safely(equipped_json))
    return player
