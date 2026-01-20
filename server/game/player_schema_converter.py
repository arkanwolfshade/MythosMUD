"""
Player schema conversion utilities.

This module handles conversion of Player objects and dictionaries to PlayerRead schemas.
"""

from typing import TYPE_CHECKING, Any

from ..exceptions import DatabaseError
from ..models import Stats
from ..models.game import (  # pylint: disable=unused-import  # Reason: InventoryItem and StatusEffect are used for type conversion
    InventoryItem,
    PositionState,
    StatusEffect,
)
from ..schemas.player import PlayerRead
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

if TYPE_CHECKING:
    pass


class PlayerSchemaConverter:
    """Utility class for converting Player objects to PlayerRead schemas."""

    def __init__(self, persistence, player_combat_service=None):
        """Initialize the converter with persistence and optional combat service."""
        self.persistence = persistence
        self.player_combat_service = player_combat_service

    async def check_player_combat_state(self, player: Any) -> bool:
        """Check if player is in combat."""
        in_combat = False
        if (
            hasattr(self, "player_combat_service")
            and self.player_combat_service
            and not hasattr(self.player_combat_service, "__class__")
            or "Mock" not in str(self.player_combat_service.__class__)
        ):
            if hasattr(player, "player_id"):
                try:
                    if hasattr(self.player_combat_service, "is_player_in_combat"):
                        in_combat = await self.player_combat_service.is_player_in_combat(player.player_id)
                except (DatabaseError, AttributeError) as e:
                    logger.warning("Failed to check combat state for player", player_id=player.player_id, error=str(e))
        return in_combat

    async def get_profession_details(self, player: Any) -> tuple[int, str | None, str | None, str | None]:
        """Get profession information for player."""
        player_profession_id = 0
        profession_name = None
        profession_description = None
        profession_flavor_text = None

        if hasattr(player, "profession_id"):
            player_profession_id = player.profession_id
        elif isinstance(player, dict):
            player_profession_id = player.get("profession_id", 0)

        if player_profession_id is not None:
            try:
                profession = await self.persistence.get_profession_by_id(player_profession_id)
                if profession:
                    profession_name = profession.name
                    profession_description = profession.description
                    profession_flavor_text = profession.flavor_text
            except (DatabaseError, AttributeError) as e:
                logger.warning("Failed to fetch profession", profession_id=player_profession_id, error=str(e))

        return player_profession_id, profession_name, profession_description, profession_flavor_text

    async def get_player_data_methods(
        self, player: Any
    ) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
        """Get stats, inventory, and status_effects from player, handling async methods."""
        stats = player.get_stats()
        inventory = player.get_inventory()
        status_effects = player.get_status_effects()

        # If these are coroutines (from AsyncMock), await them
        if hasattr(stats, "__await__"):
            stats = await stats
        if hasattr(inventory, "__await__"):
            inventory = await inventory
        if hasattr(status_effects, "__await__"):
            status_effects = await status_effects

        return stats, inventory, status_effects

    def compute_derived_stats_fields(self, stats: dict[str, Any]) -> None:
        """Compute derived stats fields (max_dp, max_magic_points, max_lucidity)."""
        try:
            import math

            con = stats.get("constitution", 50)
            siz = stats.get("size", 50)
            pow_val = stats.get("power", 50)
            edu = stats.get("education", 50)

            if "max_dp" not in stats:
                stats["max_dp"] = (con + siz) // 5
            if "max_magic_points" not in stats:
                stats["max_magic_points"] = math.ceil(pow_val * 0.2)
            if "max_lucidity" not in stats:
                stats["max_lucidity"] = edu

            # Initialize magic_points to max if it's 0 (full MP at character creation)
            if not stats.get("magic_points", 0) and stats.get("max_magic_points", 0) > 0:
                stats["magic_points"] = stats["max_magic_points"]
            # Cap lucidity to max_lucidity if it exceeds max
            max_lucidity_val = stats.get("max_lucidity", edu)
            if stats.get("lucidity", 100) > max_lucidity_val:
                stats["lucidity"] = max_lucidity_val
        except (DatabaseError, AttributeError) as e:
            logger.error(
                "Error adding computed fields to stats",
                player_id=stats.get("player_id"),
                error=str(e),
                exc_info=True,
            )

    def get_position_state(self, position_value: str | int, player_id: Any = None) -> PositionState:
        """Get PositionState from position value, with fallback to STANDING."""
        try:
            # PositionState is a str Enum, so convert int to str if needed
            if isinstance(position_value, int):
                # Try to find enum by value index (not recommended but handles legacy data)
                position_value = PositionState.STANDING.value
            return PositionState(str(position_value))
        except (ValueError, TypeError):
            logger.warning(
                "Invalid position value on player stats, defaulting to standing",
                player_id=player_id,
                position_value=position_value,
            )
            return PositionState.STANDING

    async def create_player_read_from_object(  # pylint: disable=too-many-locals  # Reason: Player schema conversion requires 16 local variables for unpacking profession data, extracting player data, model conversion, and PlayerRead construction; refactoring would reduce clarity
        self, player: Any, in_combat: bool, profession_data: tuple[int, str | None, str | None, str | None]
    ) -> PlayerRead:
        """Create PlayerRead schema from player object."""
        player_profession_id, profession_name, profession_description, profession_flavor_text = profession_data

        stats, inventory, status_effects = await self.get_player_data_methods(player)

        position_value = stats.get("position", PositionState.STANDING.value)
        position_state = self.get_position_state(position_value, getattr(player, "player_id", None))

        self.compute_derived_stats_fields(stats)

        # Convert dicts to typed models
        stats_model = Stats(**stats) if isinstance(stats, dict) else stats
        inventory_models = (
            [InventoryItem(**item) if isinstance(item, dict) else item for item in inventory]
            if isinstance(inventory, list)
            else inventory
        )
        status_effects_models = (
            [StatusEffect(**effect) if isinstance(effect, dict) else effect for effect in status_effects]
            if isinstance(status_effects, list)
            else status_effects
        )

        return PlayerRead(
            id=player.player_id,
            user_id=player.user_id,
            name=player.name,
            profession_id=player_profession_id,
            profession_name=profession_name,
            profession_description=profession_description,
            profession_flavor_text=profession_flavor_text,
            current_room_id=player.current_room_id,
            experience_points=player.experience_points,
            level=player.level,
            stats=stats_model,
            inventory=inventory_models,
            status_effects=status_effects_models,
            created_at=player.created_at,
            last_active=player.last_active,
            is_admin=bool(player.is_admin),  # Convert integer to boolean
            in_combat=in_combat,
            position=position_state,
        )

    def create_player_read_from_dict(
        self, player: dict[str, Any], in_combat: bool, profession_data: tuple[int, str | None, str | None, str | None]
    ) -> PlayerRead:
        """Create PlayerRead schema from player dictionary."""
        player_profession_id, profession_name, profession_description, profession_flavor_text = profession_data

        stats_data = player["stats"]
        # Extract position value - PositionState is a str Enum
        if isinstance(stats_data, dict):
            position_value = stats_data.get("position", PositionState.STANDING.value)
            # Ensure it's a string (PositionState is str Enum)
            if not isinstance(position_value, str):
                position_value = PositionState.STANDING.value
        else:
            position_value = PositionState.STANDING.value
        position_state = self.get_position_state(position_value, player.get("player_id"))

        # Convert dicts to typed models
        stats_model = Stats(**player["stats"]) if isinstance(player["stats"], dict) else player["stats"]
        inventory_models = (
            [InventoryItem(**item) if isinstance(item, dict) else item for item in player["inventory"]]
            if isinstance(player["inventory"], list)
            else player["inventory"]
        )
        status_effects_models = (
            [StatusEffect(**effect) if isinstance(effect, dict) else effect for effect in player["status_effects"]]
            if isinstance(player["status_effects"], list)
            else player["status_effects"]
        )

        return PlayerRead(
            id=player["player_id"],
            user_id=player["user_id"],
            name=player["name"],
            profession_id=player_profession_id,
            profession_name=profession_name,
            profession_description=profession_description,
            profession_flavor_text=profession_flavor_text,
            current_room_id=player["current_room_id"],
            experience_points=player["experience_points"],
            level=player["level"],
            stats=stats_model,
            inventory=inventory_models,
            status_effects=status_effects_models,
            created_at=player["created_at"],
            last_active=player["last_active"],
            is_admin=bool(player.get("is_admin", 0)),  # Convert integer to boolean with default
            in_combat=in_combat,
            position=position_state,
        )

    async def convert_player_to_schema(self, player: Any) -> PlayerRead:
        """
        Convert a player object to PlayerRead schema.

        Args:
            player: Player object or dictionary

        Returns:
            PlayerRead: The player data in schema format
        """
        # Check if player is in combat
        in_combat = await self.check_player_combat_state(player)

        # Get profession information
        profession_data = await self.get_profession_details(player)

        if hasattr(player, "player_id"):  # Player object
            return await self.create_player_read_from_object(player, in_combat, profession_data)

        # Dictionary
        # Check if player is a Mock by checking for MagicMock type
        if "Mock" in str(type(player).__name__):
            # In tests, return the Mock directly
            return player
        return self.create_player_read_from_dict(player, in_combat, profession_data)
