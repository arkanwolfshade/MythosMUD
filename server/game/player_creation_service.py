"""
Player creation service.

This module handles player character creation operations.
"""

import datetime
import uuid
from typing import TYPE_CHECKING, Any, cast

from ..exceptions import ValidationError
from ..models import Stats
from ..models.player import Player
from ..schemas.player import PlayerRead
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.enhanced_error_logging import create_error_context, log_and_raise_enhanced

if TYPE_CHECKING:
    pass

logger = get_logger(__name__)


class PlayerCreationService:
    """Service for player creation operations."""

    def __init__(self, persistence: Any, schema_converter: Any) -> None:
        """Initialize with persistence layer and schema converter."""
        self.persistence = persistence
        self._schema_converter = schema_converter

    async def create_player(
        self,
        name: str,
        profession_id: int = 0,
        starting_room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001",
        user_id: uuid.UUID | None = None,
    ) -> PlayerRead:
        """
        Create a new player character.

        Args:
            name: The player's name
            profession_id: The profession ID for the character (default: 0 for Tramp)
            starting_room_id: The room ID where the player starts
            user_id: Optional user ID (will be generated if not provided)

        Returns:
            PlayerRead: The created player data

        Raises:
            ValueError: If player name already exists
        """
        logger.info(
            "Creating new player",
            name=name,
            profession_id=profession_id,
            starting_room_id=starting_room_id,
            user_id=user_id,
        )

        # Check if player already exists
        existing_player = await self.persistence.get_player_by_name(name)
        if existing_player:
            logger.warning("Player creation failed - name already exists")
            context = create_error_context()
            context.metadata["player_name"] = name
            context.metadata["operation"] = "create_player"
            log_and_raise_enhanced(
                ValidationError,
                "Player name already exists",
                context=context,
                details={"player_name": name, "existing_player_id": str(existing_player.player_id)},
                user_friendly="A player with this name already exists",
            )

        # Generate user_id if not provided
        if user_id is None:
            user_id = uuid.uuid4()
            logger.debug("Generated user_id for new player")

        # Use naive UTC datetime for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibility
        from datetime import UTC

        current_time = datetime.datetime.now(UTC).replace(tzinfo=None)
        # Generate UUID for player_id - Player model now uses UUID type
        player = Player(
            player_id=uuid.uuid4(),
            user_id=user_id,
            name=name,
            current_room_id=starting_room_id,
            profession_id=profession_id,
            experience_points=0,
            level=1,
            created_at=current_time,
            last_active=current_time,
        )

        # Save player to persistence
        await self.persistence.save_player(player)
        logger.info("Player created successfully", player_id=player.player_id)

        # Convert to schema format
        return cast(PlayerRead, await self._schema_converter.convert_player_to_schema(player))

    async def create_player_with_stats(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Player creation requires many parameters for stats and configuration
        self,
        name: str,
        stats: Stats,
        profession_id: int = 0,
        starting_room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001",
        user_id: uuid.UUID | None = None,
    ) -> PlayerRead:
        """
        Create a new player character with specific stats.

        Args:
            name: The player's name
            stats: The player's stats
            profession_id: The profession ID for the character (default: 0 for Tramp)
            starting_room_id: The room ID where the player starts
            user_id: Optional user ID (will be generated if not provided)

        Returns:
            PlayerRead: The created player data

        Raises:
            ValueError: If player name already exists
        """
        logger.info(
            "Creating new player with stats",
            name=name,
            profession_id=profession_id,
            starting_room_id=starting_room_id,
            user_id=user_id,
        )

        # MULTI-CHARACTER: Check character limit if user_id is provided
        if user_id is not None:
            active_characters = await self.persistence.get_active_players_by_user_id(str(user_id))
            if len(active_characters) >= 3:
                logger.warning("Character creation failed - character limit reached", user_id=user_id)
                context = create_error_context()
                context.metadata["user_id"] = str(user_id)
                context.metadata["operation"] = "create_player_with_stats"
                context.metadata["active_character_count"] = len(active_characters)
                log_and_raise_enhanced(
                    ValidationError,
                    "Character limit reached",
                    context=context,
                    details={"user_id": str(user_id), "active_character_count": len(active_characters)},
                    user_friendly="You have reached the maximum number of characters (3). Please delete a character to create a new one.",
                )

        # MULTI-CHARACTER: Check if character name already exists (case-insensitive, active characters only)
        # get_player_by_name now excludes deleted characters and uses case-insensitive comparison
        existing_player = await self.persistence.get_player_by_name(name)
        if existing_player:
            logger.warning("Character creation failed - name already exists", name=name)
            context = create_error_context()
            context.metadata["player_name"] = name
            context.metadata["operation"] = "create_player_with_stats"
            log_and_raise_enhanced(
                ValidationError,
                "Character name already exists",
                context=context,
                details={"player_name": name, "existing_player_id": str(existing_player.player_id)},
                user_friendly="A character with this name already exists (names are case-insensitive)",
            )

        # Generate user_id if not provided
        if user_id is None:
            user_id = uuid.uuid4()
            logger.debug("Generated user_id for new player")

        # Use naive UTC datetime for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibility
        from datetime import UTC

        current_time = datetime.datetime.now(UTC).replace(tzinfo=None)
        # Generate UUID for player_id - Player model now uses UUID type
        player = Player(
            player_id=uuid.uuid4(),
            user_id=user_id,
            name=name,
            current_room_id=starting_room_id,
            profession_id=profession_id,
            experience_points=0,
            level=1,
            created_at=current_time,
            last_active=current_time,
        )

        # Set the player's stats
        if hasattr(stats, "model_dump"):
            # Stats object
            player.set_stats(stats.model_dump())
        else:
            # Dictionary
            player.set_stats(stats)  # type: ignore[arg-type]  # Reason: Type narrowing from hasattr check doesn't satisfy mypy. After checking that stats doesn't have model_dump, we know it's a dict, but mypy can't infer this pattern.

        # Ensure JSONB fields are initialized (PostgreSQL NOT NULL constraints)
        if not getattr(player, "inventory", None):
            player.set_inventory([])
        if not getattr(player, "status_effects", None):
            player.set_status_effects([])

        # Save player to persistence
        await self.persistence.save_player(player)
        logger.info("Player created successfully with stats", player_id=player.player_id)

        # Convert to schema format
        return cast(PlayerRead, await self._schema_converter.convert_player_to_schema(player))
