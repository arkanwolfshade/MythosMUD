"""Player posture coordination service for MythosMUD.

As noted in the Pnakotic Manuscripts, a practitioner's stance shapes the arcane
energies they can wield. This service synchronizes that stance across
in-memory sessions, persistence, and default alias bindings so scholars do not
fall out of alignment with the eldritch record.
"""

from __future__ import annotations

from typing import Any, cast

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

VALID_POSITIONS = {"standing", "sitting", "lying"}

_POSITION_MESSAGES: dict[str, dict[str, str]] = {
    "sitting": {
        "success": "You settle into a seated position.",
        "already": "You are already seated.",
    },
    "standing": {
        "success": "You rise to your feet.",
        "already": "You are already standing.",
    },
    "lying": {
        "success": "You stretch out and lie down.",
        "already": "You are already lying down.",
    },
}

_DEFAULT_ALIAS_MAP = {"sit": "sit", "stand": "stand", "lie": "lie"}


class PlayerPositionService:
    """Coordinate player posture transitions with persistence and live presence tracking."""

    def __init__(
        self,
        persistence: Any | None,
        connection_manager: Any | None,
        alias_storage: AliasStorage | None,
    ) -> None:
        self._persistence = persistence
        self._connection_manager = connection_manager
        self._alias_storage = alias_storage

    def ensure_default_aliases(self, player_name: str) -> None:
        """Ensure the expected aliases exist for position commands."""
        if not self._alias_storage:
            return

        for alias_name, command in _DEFAULT_ALIAS_MAP.items():
            try:
                existing_alias = self._alias_storage.get_alias(player_name, alias_name)
                if existing_alias is None or existing_alias.command.lower() != command:
                    self._alias_storage.create_alias(player_name, alias_name, command)
            except Exception as exc:  # pragma: no cover - defensive logging path
                logger.warning(
                    "Failed to seed default position alias",
                    player_name=player_name,
                    alias_name=alias_name,
                    error=str(exc),
                )

    def change_position(self, player_name: str, target_position: str) -> dict[str, Any]:
        """Mutate persistence and in-memory tracking to reflect the requested position."""
        normalized_position = target_position.lower()
        if normalized_position not in VALID_POSITIONS:
            raise ValueError(f"Unsupported position: {target_position}")

        # Both scholars and agents rely on the same payload shape for downstream routing.
        response: dict[str, Any] = {
            "position": normalized_position,
            "success": False,
            "message": "",
            "previous_position": None,
            "player_id": None,
            "room_id": None,
            "player_display_name": player_name,
        }

        self.ensure_default_aliases(player_name)

        if not self._persistence:
            response["message"] = "Position changes are currently unavailable."
            return response

        try:
            player = self._persistence.get_player_by_name(player_name)
        except Exception as exc:
            logger.error(
                "Failed to retrieve player for position update",
                player_name=player_name,
                error=str(exc),
            )
            response["message"] = "Unable to change position right now."
            return response

        if not player:
            response["message"] = "Player information not found."
            return response

        player_id_value = getattr(player, "player_id", None)
        room_id_value = getattr(player, "current_room_id", None)
        player_display_name = getattr(player, "name", player_name)

        if player_id_value is not None:
            response["player_id"] = str(player_id_value)
        if room_id_value is not None:
            response["room_id"] = str(room_id_value)
        response["player_display_name"] = player_display_name

        stats: dict[str, Any]
        try:
            stats = player.get_stats() if hasattr(player, "get_stats") else {}
        except Exception as exc:  # pragma: no cover - defensive logging path
            logger.error(
                "Failed to load player stats during position update",
                player_name=player_name,
                error=str(exc),
            )
            stats = {}

        if not isinstance(stats, dict):
            stats = {}

        current_position = stats.get("position", "standing")
        response["previous_position"] = current_position

        if current_position == normalized_position:
            response["message"] = _POSITION_MESSAGES[normalized_position]["already"]
            self._update_connection_manager(player, player_name, normalized_position)
            return response

        stats["position"] = normalized_position
        if hasattr(player, "set_stats"):
            player.set_stats(stats)

        try:
            self._persistence.save_player(player)
        except Exception as exc:
            logger.error(
                "Failed to persist player position",
                player_name=player_name,
                desired_position=normalized_position,
                error=str(exc),
            )
            response["message"] = "Unable to change position right now."
            return response

        self._update_connection_manager(player, player_name, normalized_position)
        response["success"] = True
        response["message"] = _POSITION_MESSAGES[normalized_position]["success"]
        return response

    def _update_connection_manager(self, player: Any, player_name: str, position: str) -> None:
        """Mirror posture changes into the live connection manager."""
        connection_manager = self._connection_manager
        if not connection_manager or not hasattr(connection_manager, "online_players"):
            return

        try:
            player_id = getattr(player, "player_id", None)
            if player_id is not None:
                key = str(player_id)
                online_players = getattr(connection_manager, "online_players", None)
                if isinstance(online_players, dict):
                    player_info = cast(dict[str, Any] | None, online_players.get(key))
                    if player_info is None:
                        player_info = {
                            "player_id": key,
                            "player_name": getattr(player, "name", player_name),
                            "connection_types": set(),
                            "total_connections": 0,
                        }
                        online_players[key] = player_info
                    player_info["position"] = position

            getter = getattr(connection_manager, "get_online_player_by_display_name", None)
            if callable(getter):
                player_info = getter(player_name)
                if isinstance(player_info, dict):
                    player_info["position"] = position
        except Exception as exc:  # pragma: no cover - defensive logging path
            logger.warning(
                "Failed to update in-memory position tracking",
                player_name=player_name,
                position=position,
                error=str(exc),
            )
