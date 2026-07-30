"""Player posture coordination service for MythosMUD.

As noted in the Pnakotic Manuscripts, a practitioner's stance shapes the arcane
energies they can wield. This service synchronizes that stance across
in-memory sessions, persistence, and default alias bindings so scholars do not
fall out of alignment with the eldritch record.
"""

from __future__ import annotations

from typing import Protocol, TypedDict

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger

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

_DEFAULT_ALIAS_MAP = {"sit": "/sit", "stand": "/stand", "lie": "/lie"}


class PositionChangeResponse(TypedDict):
    """Result payload for a posture transition attempt."""

    position: str
    success: bool
    message: str
    previous_position: str | None
    player_id: str | None
    room_id: str | None
    player_display_name: str


class SupportsPlayerPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Persistence surface required for posture updates."""

    async def get_player_by_name(self, name: str) -> Player | None:
        """Look up a player by name."""

    async def save_player(self, player: Player) -> None:
        """Persist player posture and related state."""


class SupportsConnectionManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Live presence surface used to mirror posture into online player records."""

    online_players: dict[str, dict[str, object]]

    def get_online_player_by_display_name(self, display_name: str) -> dict[str, object] | None:
        """Return the online player record for a display name, if present."""


class PlayerPositionService:
    """Coordinate player posture transitions with persistence and live presence tracking."""

    def __init__(
        self,
        persistence: SupportsPlayerPersistence | None,
        connection_manager: SupportsConnectionManager | None,
        alias_storage: AliasStorage | None,
    ) -> None:
        self._persistence: SupportsPlayerPersistence | None = persistence
        self._connection_manager: SupportsConnectionManager | None = connection_manager
        self._alias_storage: AliasStorage | None = alias_storage

    def ensure_default_aliases(self, player_name: str) -> None:
        """Ensure the expected aliases exist for position commands."""
        if not self._alias_storage:
            return

        for alias_name, command in _DEFAULT_ALIAS_MAP.items():
            try:
                existing_alias = self._alias_storage.get_alias(player_name, alias_name)
                if existing_alias is None or existing_alias.command.lower() != command:
                    _ = self._alias_storage.create_alias(player_name, alias_name, command)
            except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Alias seeding errors unpredictable, must log but continue
                logger.warning(
                    "Failed to seed default position alias",
                    player_name=player_name,
                    alias_name=alias_name,
                    error=str(exc),
                )

    def _validate_position(self, target_position: str) -> str:
        """Validate and normalize position."""
        normalized_position = target_position.lower()
        if normalized_position not in VALID_POSITIONS:
            raise ValueError(f"Unsupported position: {target_position}")
        return normalized_position

    async def _get_player_for_position_change(self, player_name: str) -> tuple[Player | None, dict[str, str]] | None:
        """
        Get player for position change.

        Returns:
            Tuple of (player, response_dict) if persistence available, None if no persistence
            Response dict contains error_type: "not_found" or "error" when player is None
        """
        if not self._persistence:
            return None

        try:
            player = await self._persistence.get_player_by_name(player_name)
        except (DatabaseError, ValueError, AttributeError, TypeError) as exc:
            logger.error(
                "Failed to retrieve player for position update",
                player_name=player_name,
                error=str(exc),
            )
            return None, {"error_type": "error"}

        if not player:
            return None, {"error_type": "not_found"}

        return player, {}

    def _apply_player_info(self, response: PositionChangeResponse, player: Player, player_name: str) -> None:
        """Copy player identity fields into the position-change response."""
        response["player_display_name"] = player.name or player_name
        response["player_id"] = player.player_id
        response["room_id"] = player.current_room_id

    def _load_player_stats(self, player: Player, player_name: str) -> dict[str, object]:
        """Load player stats, returning {} when loading fails."""
        try:
            return player.get_stats()
        except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Player stats loading errors unpredictable, must use empty dict
            logger.error(
                "Failed to load player stats during position update",
                player_name=player_name,
                error=str(exc),
            )
            return {}

    def _get_current_position(self, player: Player, player_name: str) -> str:
        """Get current position from player stats."""
        stats = self._load_player_stats(player, player_name)
        position_value = stats.get("position", "standing")
        return position_value if isinstance(position_value, str) else "standing"

    async def _update_player_position(
        self, player: Player, stats: dict[str, object], normalized_position: str, player_name: str
    ) -> bool:
        """Update player position in persistence."""
        if self._persistence is None:
            return False
        stats["position"] = normalized_position
        player.set_stats(stats)

        try:
            await self._persistence.save_player(player)
            return True
        except (DatabaseError, ValueError, AttributeError, TypeError) as exc:
            logger.error(
                "Failed to persist player position",
                player_name=player_name,
                desired_position=normalized_position,
                error=str(exc),
            )
            return False

    def _initial_response(self, player_name: str, normalized_position: str) -> PositionChangeResponse:
        """Build the default unsuccessful position-change payload."""
        return {
            "position": normalized_position,
            "success": False,
            "message": "",
            "previous_position": None,
            "player_id": None,
            "room_id": None,
            "player_display_name": player_name,
        }

    async def change_position(self, player_name: str, target_position: str) -> PositionChangeResponse:
        """Mutate persistence and in-memory tracking to reflect the requested position."""
        normalized_position = self._validate_position(target_position)
        response = self._initial_response(player_name, normalized_position)
        self.ensure_default_aliases(player_name)

        if not self._persistence:
            response["message"] = "Position changes are currently unavailable."
            return response

        player_result = await self._get_player_for_position_change(player_name)
        if player_result is None:
            response["message"] = "Unable to change position right now."
            return response

        player, error_info = player_result
        if player is None:
            if error_info.get("error_type", "error") == "not_found":
                response["message"] = "Player not found."
            else:
                response["message"] = "Unable to change position right now."
            return response

        self._apply_player_info(response, player, player_name)
        current_position = self._get_current_position(player, player_name)
        response["previous_position"] = current_position

        if current_position == normalized_position:
            response["message"] = _POSITION_MESSAGES[normalized_position]["already"]
            self._update_connection_manager(player, player_name, normalized_position)
            return response

        stats = self._load_player_stats(player, player_name)
        success = await self._update_player_position(player, stats, normalized_position, player_name)
        if not success:
            response["message"] = "Unable to change position right now."
            return response

        self._update_connection_manager(player, player_name, normalized_position)
        response["success"] = True
        response["message"] = _POSITION_MESSAGES[normalized_position]["success"]
        return response

    def _update_connection_manager(self, player: Player, player_name: str, position: str) -> None:
        """Mirror posture changes into the live connection manager."""
        connection_manager = self._connection_manager
        if connection_manager is None:
            return

        try:
            key = str(player.player_id)
            online_players = connection_manager.online_players
            existing = online_players.get(key)
            if existing is None:
                created: dict[str, object] = {}
                created["player_id"] = key
                created["player_name"] = player.name or player_name
                created["connection_types"] = set[str]()
                created["total_connections"] = 0
                online_players[key] = created
                existing = created
            existing["position"] = position

            getter_info = connection_manager.get_online_player_by_display_name(player_name)
            if getter_info is not None:
                getter_info["position"] = position
        except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Position tracking errors unpredictable, must log but continue
            logger.warning(
                "Failed to update in-memory position tracking",
                player_name=player_name,
                position=position,
                error=str(exc),
            )
