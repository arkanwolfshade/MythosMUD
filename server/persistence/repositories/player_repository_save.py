"""
Player save/upsert helpers for PlayerRepository.

Handles inventory validation, timestamp normalization, and upsert_player procedure execution.
"""

import json
from datetime import UTC, datetime
from typing import Any, cast

from sqlalchemy import text

from server.models.player import Player, PlayerInventory
from server.schemas.shared import InventorySchemaValidationError, validate_inventory_payload

UPSERT_PLAYER_SQL = text(
    "CALL upsert_player("
    ":player_id, :user_id, :name, :inventory, :status_effects,"
    ":current_room_id, :respawn_room_id, :experience_points, :level, :is_admin,"
    ":profession_id, :created_at, :last_active, :stats, :is_deleted, :deleted_at,"
    ":tutorial_instance_id, :inventory_json, :equipped_json)"
)


def _parse_inventory_raw(raw: Any) -> list[dict[str, Any]]:
    """Parse inventory from string or list. Raises InventorySchemaValidationError if invalid."""
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except (TypeError, json.JSONDecodeError) as exc:
            raise InventorySchemaValidationError(f"Invalid inventory JSON: {exc}") from exc
    if not isinstance(raw, list):
        raise InventorySchemaValidationError("Inventory payload must be an array of stacks")
    return cast(list[dict[str, Any]], raw)


def _parse_equipped_raw(raw: Any) -> dict[str, Any]:
    """Parse equipped from string or dict. Raises InventorySchemaValidationError if invalid."""
    raw = raw or {}
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except (TypeError, json.JSONDecodeError) as exc:
            raise InventorySchemaValidationError(f"Invalid equipped JSON: {exc}") from exc
    if not isinstance(raw, dict):
        raise InventorySchemaValidationError("Equipped payload must be an object")
    return cast(dict[str, Any], raw)


class PlayerSavePreparer:
    """
    Prepares Player objects for upsert_player procedure calls.

    Handles normalization, inventory validation, and params building.
    """

    def __init__(self, logger: Any) -> None:
        self._logger = logger

    def _normalize_is_admin(self, player: Player) -> None:
        """Ensure is_admin is an integer (PostgreSQL requires integer, not boolean)."""
        if isinstance(getattr(player, "is_admin", None), bool):
            player.is_admin = 1 if player.is_admin else 0

    def _ensure_inventory_record(self, player: Player, inventory_json: str, equipped_json: str) -> None:
        """Ensure player has inventory_record and update with current payload."""
        record = getattr(player, "inventory_record", None)
        if record is None:
            player.inventory_record = PlayerInventory(
                player_id=str(player.player_id),
                inventory_json=inventory_json,
                equipped_json=equipped_json,
            )
        else:
            record.inventory_json = inventory_json
            record.equipped_json = equipped_json

    def _normalize_timestamps(self, player: Player) -> tuple[datetime, datetime, datetime | None]:
        """Normalize last_active, created_at, deleted_at to UTC for procedure call."""
        last_active = getattr(player, "last_active", None)
        last_active = last_active.astimezone(UTC) if last_active and last_active.tzinfo else datetime.now(UTC)
        created_at = getattr(player, "created_at", None)
        created_at = created_at.astimezone(UTC) if created_at and created_at.tzinfo else datetime.now(UTC)
        deleted_at = getattr(player, "deleted_at", None)
        deleted_at = deleted_at.astimezone(UTC) if deleted_at and deleted_at.tzinfo else None
        return last_active, created_at, deleted_at

    def _upsert_string_defaults(self, player: Player) -> dict[str, Any]:
        """Extract string fields with defaults for upsert_player."""
        default_room = "earth_arkhamcity_sanitarium_room_foyer_001"
        return {
            "inventory": player.inventory or "[]",
            "status_effects": player.status_effects or "[]",
            "current_room_id": player.current_room_id or default_room,
            "respawn_room_id": player.respawn_room_id or default_room,
        }

    def _upsert_numeric_defaults(self, player: Player) -> dict[str, Any]:
        """Extract numeric/bool fields with defaults for upsert_player."""
        # Coerce is_deleted to bool so we never send None (players.is_deleted is NOT NULL)
        is_deleted = False if (getattr(player, "is_deleted", None) is None) else bool(player.is_deleted)
        return {
            "experience_points": player.experience_points or 0,
            "level": player.level or 1,
            "is_admin": player.is_admin or 0,
            "profession_id": player.profession_id if player.profession_id else None,
            "is_deleted": is_deleted,
        }

    def _prepare_inventory_payload(self, player: Player) -> tuple[str, str]:
        """Validate and serialize inventory payload. Returns (inventory_json, equipped_json)."""
        inventory = _parse_inventory_raw(player.get_inventory())
        equipped = _parse_equipped_raw(player.get_equipped_items())
        payload_dict: dict[str, Any] = {"inventory": inventory, "equipped": equipped, "version": 1}
        validate_inventory_payload(payload_dict)

        inventory_json = json.dumps(inventory)
        equipped_json = json.dumps(equipped)
        self._logger.debug(
            "Preparing inventory payload for save",
            player_id=str(player.player_id),
            player_name=player.name,
            inventory_length=len(inventory),
            inventory_items=[
                {
                    "item_name": item.get("item_name"),
                    "item_id": item.get("item_id"),
                    "slot_type": item.get("slot_type"),
                    "quantity": item.get("quantity"),
                }
                for item in inventory[:5]
            ],
        )

        player.inventory = cast(Any, inventory_json)  # keep ORM column in sync
        player.set_equipped_items(equipped)
        return inventory_json, equipped_json

    def prepare(self, player: Player) -> dict[str, Any]:
        """Prepare player for upsert: normalize, validate inventory, build params."""
        self._normalize_is_admin(player)
        inventory_json, equipped_json = self._prepare_inventory_payload(player)
        self._ensure_inventory_record(player, inventory_json, equipped_json)
        last_active, created_at, deleted_at = self._normalize_timestamps(player)

        strings = self._upsert_string_defaults(player)
        numerics = self._upsert_numeric_defaults(player)
        return {
            "player_id": str(player.player_id),
            "user_id": str(player.user_id),
            "name": player.name,
            **strings,
            **numerics,
            "created_at": created_at,
            "last_active": last_active,
            # Pass JSON-serialized stats so asyncpg sees a plain string, avoiding
            # ".encode" errors on dict/MutableDict while still letting PostgreSQL
            # cast the value into JSONB in upsert_player.
            "stats": json.dumps(player.get_stats()),
            "deleted_at": deleted_at,
            "tutorial_instance_id": getattr(player, "tutorial_instance_id", None),
            "inventory_json": inventory_json,
            "equipped_json": equipped_json,
        }

    async def execute(self, session: Any, params: dict[str, Any]) -> None:
        """Execute upsert_player procedure with given params."""
        await session.execute(UPSERT_PLAYER_SQL, params)
