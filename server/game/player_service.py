"""
Player service for MythosMUD server.

This module handles all player-related business logic including
creation, retrieval, validation, and state management.
"""

# pylint: disable=wrong-import-position,too-many-lines  # Reason: Imports after TYPE_CHECKING block are intentional to avoid circular dependencies. Player service requires 650 lines to implement comprehensive player operations (CRUD, state management, combat integration, search, creation, validation); splitting would reduce cohesion and increase coupling between player-related concerns

import uuid
from typing import TYPE_CHECKING, Any

from ..alias_storage import AliasStorage

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    # Removed: from ..persistence import PersistenceLayer - now using async_persistence parameter
    from ..services.player_respawn_service import PlayerRespawnService
from ..config import get_config
from ..exceptions import DatabaseError, ValidationError
from ..models import Stats
from ..schemas.player import PlayerRead
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.enhanced_error_logging import create_error_context, log_and_raise_enhanced
from .player_creation_service import PlayerCreationService
from .player_respawn_wrapper import PlayerRespawnWrapper
from .player_schema_converter import PlayerSchemaConverter
from .player_search_service import PlayerSearchService
from .player_state_service import PlayerStateService

logger = get_logger(__name__)


class PlayerService:  # pylint: disable=too-many-instance-attributes,too-many-public-methods  # Reason: PlayerService requires 8 instance attributes for persistence, combat services, and sub-service composition (schema_converter, creation_service, search_service, state_service, respawn_wrapper); it exposes 24 public methods for comprehensive player operations (CRUD, state management, combat integration, search) which is necessary for the service's role as the primary player API
    """Service class for player-related business operations."""

    def __init__(
        self,
        persistence: Any,
        combat_service: Any = None,
        player_combat_service: Any = None,
        item_prototype_registry: Any = None,
    ) -> None:
        """Initialize the player service with a persistence layer and optional combat service and prototype registry."""
        self.persistence = persistence
        self.combat_service = combat_service
        self.player_combat_service = player_combat_service
        # Initialize sub-services (order matters - schema_converter needed by creation_service)
        self._schema_converter = PlayerSchemaConverter(
            persistence, player_combat_service, item_prototype_registry=item_prototype_registry
        )
        self._creation_service = PlayerCreationService(persistence, self._schema_converter)
        self._search_service = PlayerSearchService(self)
        self._state_service = PlayerStateService(persistence)
        self._respawn_wrapper = PlayerRespawnWrapper(persistence)
        logger.info("PlayerService initialized")

    def set_item_prototype_registry(self, registry: Any) -> None:
        """Set the item prototype registry on the schema converter (e.g. after item services load)."""
        self._schema_converter.item_prototype_registry = registry

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
        return await self._creation_service.create_player(name, profession_id, starting_room_id, user_id)

    def get_default_starting_room(self, requested_room_id: str | None = None) -> str:
        """
        Get the default starting room for new characters.

        Returns the requested room ID if provided, otherwise returns the configured
        default starting room. Falls back to a hardcoded default if configuration is unavailable.

        Args:
            requested_room_id: Optional room ID from request, takes precedence over config

        Returns:
            str: Starting room ID to use
        """
        if requested_room_id:
            return requested_room_id

        try:
            default_start_room = get_config().game.default_player_room
            return default_start_room
        except (ImportError, AttributeError, ValueError) as e:
            logger.error("Error getting default start room config", error=str(e), error_type=type(e).__name__)
            # Fallback to hardcoded default
            return "earth_arkhamcity_northside_intersection_derby_high"

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
        return await self._creation_service.create_player_with_stats(
            name, stats, profession_id, starting_room_id, user_id
        )

    async def get_player_by_id(self, player_id: uuid.UUID) -> PlayerRead | None:
        """
        Get a player by their ID.

        Args:
            player_id: The player's ID (UUID)

        Returns:
            PlayerRead: The player data, or None if not found
        """
        # Structlog handles UUID objects automatically, no need to convert to string
        logger.debug("Getting player by ID", player_id=player_id)

        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            logger.debug("Player not found by ID")
            return None

        logger.debug("Player found by ID")
        return await self._schema_converter.convert_player_to_schema(player)

    async def get_player_by_name(self, player_name: str) -> PlayerRead | None:
        """
        Get a player by their name.

        Args:
            player_name: The player's name

        Returns:
            PlayerRead: The player data, or None if not found
        """
        logger.debug("Getting player by name")

        player = await self.persistence.get_player_by_name(player_name)
        if not player:
            logger.debug("Player not found by name")
            return None

        logger.debug("Player found by name")
        return await self._schema_converter.convert_player_to_schema(player)

    async def list_players(self) -> list[PlayerRead]:
        """
        Get a list of all players.

        Returns:
            List[PlayerRead]: List of all players
        """
        logger.debug("Listing all players")
        players = await self.persistence.list_players()
        result = []
        for player in players:
            result.append(await self._schema_converter.convert_player_to_schema(player))
        logger.debug("Finished listing all players")
        return result

    async def resolve_player_name(self, player_name: str) -> PlayerRead | None:
        """
        Resolve a player name with fuzzy matching and case-insensitive search.

        This method is designed for chat system use, where players might type
        partial names or use different capitalization.

        Args:
            player_name: The player name to resolve (can be partial or case-insensitive)

        Returns:
            PlayerRead: The player data, or None if not found
        """
        return await self._search_service.resolve_player_name(player_name)

    async def get_online_players(self) -> list[PlayerRead]:
        """
        Get a list of currently online players.

        Note: This is a placeholder implementation. In a full implementation,
        this would check against the connection manager to see which players
        are actually connected.

        Returns:
            List[PlayerRead]: List of online players
        """
        return await self._search_service.get_online_players()

    async def search_players_by_name(self, search_term: str, limit: int = 10) -> list[PlayerRead]:
        """
        Search for players by name with fuzzy matching.

        This method returns multiple matches for autocomplete and
        player discovery features.

        Args:
            search_term: The search term to match against player names
            limit: Maximum number of results to return

        Returns:
            List[PlayerRead]: List of matching players
        """
        return await self._search_service.search_players_by_name(search_term, limit)

    async def validate_player_name(self, player_name: str) -> tuple[bool, str]:
        """
        Validate a player name for chat system use.

        This checks if the name is valid and provides helpful error messages.

        Args:
            player_name: The player name to validate

        Returns:
            tuple[bool, str]: (is_valid, error_message)
        """
        return await self._search_service.validate_player_name(player_name)

    async def delete_player(self, player_id: uuid.UUID) -> tuple[bool, str]:
        """
        Delete a player character.

        Args:
            player_id: The player's ID (UUID)

        Returns:
            tuple[bool, str]: (success, message)
        """
        logger.debug("Attempting to delete player")
        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for deletion")
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "delete_player"
            log_and_raise_enhanced(
                ValidationError,
                "Player not found for deletion",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found",
            )

        # Delete the player from the database
        success = await self.persistence.delete_player(player_id)
        if not success:
            logger.error("Failed to delete player from persistence", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "delete_player"
            log_and_raise_enhanced(
                DatabaseError,
                "Failed to delete player from persistence",
                context=context,
                details={"player_id": player_id},
                user_friendly="Failed to delete player",
            )

        # Safely get player name for logging
        player_name = player.name if hasattr(player, "name") else player.get("name", "unknown")
        logger.info("Player deleted successfully", player_id=player_id)

        # Delete player aliases if they exist
        config = get_config()
        aliases_dir = config.game.aliases_dir
        alias_storage = AliasStorage(storage_dir=aliases_dir) if aliases_dir else AliasStorage()
        alias_storage.delete_player_aliases(player_name)
        logger.debug("Player aliases deleted")

        return True, f"Player {player_name} has been deleted"

    async def get_user_characters(self, user_id: uuid.UUID) -> list[PlayerRead]:
        """
        Get all active characters for a user.

        MULTI-CHARACTER: Returns list of active (non-deleted) characters for a user.

        Args:
            user_id: The user's ID (UUID)

        Returns:
            list[PlayerRead]: List of active character data
        """
        logger.debug("Getting user characters", user_id=user_id)
        players = await self.persistence.get_active_players_by_user_id(str(user_id))
        return [await self._schema_converter.convert_player_to_schema(player) for player in players]

    async def validate_character_access(
        self, character_id: uuid.UUID, user_id: uuid.UUID
    ) -> tuple[bool, PlayerRead | None, str]:
        """
        Validate that a character exists, belongs to the user, and is not deleted.

        Args:
            character_id: Character UUID to validate
            user_id: User UUID that should own the character

        Returns:
            Tuple of (is_valid, character, error_message)
            - is_valid: True if character is valid and accessible
            - character: PlayerRead object if valid, None otherwise
            - error_message: Error message if validation failed, empty string if valid
        """
        logger.debug("Validating character access", character_id=character_id, user_id=user_id)

        # Get character from player service
        character = await self.get_player_by_id(character_id)
        if not character:
            return False, None, "Character not found"

        # Get the actual Player object to check is_deleted and user_id
        player = await self.persistence.get_player_by_id(character_id)
        if not player:
            return False, None, "Character not found"

        # Validate character belongs to user
        if str(player.user_id) != str(user_id):
            return False, None, "Character does not belong to user"

        # Validate character is not deleted
        if player.is_deleted:
            return False, None, "Character has been deleted"

        logger.debug("Character access validated successfully", character_id=character_id, user_id=user_id)
        return True, character, ""

    async def soft_delete_character(self, player_id: uuid.UUID, user_id: uuid.UUID) -> tuple[bool, str]:
        """
        Soft delete a character (sets is_deleted=True, deleted_at=timestamp).

        MULTI-CHARACTER: Soft deletion allows character names to be reused while preserving data.
        Validates that the character belongs to the user before deletion.

        Args:
            player_id: The character's ID (UUID)
            user_id: The user's ID (UUID) - used for validation

        Returns:
            tuple[bool, str]: (success, message)

        Raises:
            ValidationError: If character not found or doesn't belong to user
        """
        logger.debug("Attempting to soft delete character", player_id=player_id, user_id=user_id)
        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            logger.warning("Character not found for soft deletion", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "soft_delete_character"
            log_and_raise_enhanced(
                ValidationError,
                "Character not found for deletion",
                context=context,
                details={"player_id": player_id},
                user_friendly="Character not found",
            )

        # Validate that character belongs to user
        if str(player.user_id) != str(user_id):
            logger.warning("Character does not belong to user", player_id=player_id, user_id=user_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["user_id"] = str(user_id)
            context.metadata["operation"] = "soft_delete_character"
            log_and_raise_enhanced(
                ValidationError,
                "Character does not belong to user",
                context=context,
                details={"player_id": player_id, "user_id": str(user_id)},
                user_friendly="You can only delete your own characters",
            )

        # Check if already deleted
        if player.is_deleted:
            logger.warning("Character already deleted", player_id=player_id)
            return False, "Character is already deleted"

        # Soft delete the character
        success = await self.persistence.soft_delete_player(player_id)
        if not success:
            logger.error("Failed to soft delete character", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "soft_delete_character"
            log_and_raise_enhanced(
                DatabaseError,
                "Failed to soft delete character",
                context=context,
                details={"player_id": player_id},
                user_friendly="Failed to delete character",
            )

        player_name = player.name if hasattr(player, "name") else "unknown"
        logger.info("Character soft-deleted successfully", player_id=player_id, character_name=player_name)

        return True, f"Character {player_name} has been deleted"

    async def update_player_location(self, player_name: str, new_room_id: str) -> bool:
        """
        Update a player's current room location and save to database.

        Args:
            player_name: Name of the player to update
            new_room_id: New room ID to move player to

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Get the raw SQLAlchemy player object for modification
            player = await self.persistence.get_player_by_name(player_name)
            if not player:
                logger.warning("Cannot update location - player not found", player_name=player_name)
                context = create_error_context()
                context.metadata["player_name"] = player_name
                context.metadata["new_room_id"] = new_room_id
                context.metadata["operation"] = "update_player_location"
                log_and_raise_enhanced(
                    ValidationError,
                    f"Player not found: {player_name}",
                    context=context,
                    details={"player_name": player_name, "new_room_id": new_room_id},
                    user_friendly="Player not found",
                )

            # Update location
            old_room = player.current_room_id
            player.current_room_id = new_room_id

            # Save to database
            await self.persistence.save_player(player)

            logger.info("Player location updated", player_name=player_name, from_room=old_room, to_room=new_room_id)
            return True

        except (DatabaseError, AttributeError) as e:
            logger.error("Failed to update player location", player_name=player_name, room_id=new_room_id, error=str(e))
            context = create_error_context()
            context.metadata["player_name"] = player_name
            context.metadata["new_room_id"] = new_room_id
            context.metadata["operation"] = "update_player_location"
            log_and_raise_enhanced(
                DatabaseError,
                f"Failed to update player location: {str(e)}",
                context=context,
                details={"player_name": player_name, "new_room_id": new_room_id, "error": str(e)},
                user_friendly="Failed to update player location",
            )

    async def apply_lucidity_loss(self, player_id: uuid.UUID, amount: int, source: str = "unknown") -> dict[str, Any]:
        """
        Apply lucidity loss to a player.

        Args:
            player_id: The player's ID (UUID)
            amount: Amount of lucidity to lose
            source: Source of the lucidity loss

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        return await self._state_service.apply_lucidity_loss(player_id, amount, source)

    async def apply_fear(self, player_id: uuid.UUID, amount: int, source: str = "unknown") -> dict[str, Any]:
        """
        Apply fear to a player.

        Args:
            player_id: The player's ID (UUID)
            amount: Amount of fear to apply
            source: Source of the fear

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        return await self._state_service.apply_fear(player_id, amount, source)

    async def apply_corruption(self, player_id: uuid.UUID, amount: int, source: str = "unknown") -> dict[str, Any]:
        """
        Apply corruption to a player.

        Args:
            player_id: The player's ID (UUID)
            amount: Amount of corruption to apply
            source: Source of the corruption

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        return await self._state_service.apply_corruption(player_id, amount, source)

    async def gain_occult_knowledge(self, player_id: uuid.UUID, amount: int, source: str = "unknown") -> dict[str, Any]:
        """
        Gain occult knowledge (with lucidity loss).

        Args:
            player_id: The player's ID (UUID)
            amount: Amount of occult knowledge to gain
            source: Source of the knowledge

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        return await self._state_service.gain_occult_knowledge(player_id, amount, source)

    async def heal_player(self, player_id: uuid.UUID, amount: int) -> dict[str, Any]:
        """
        Heal a player's health.

        Args:
            player_id: The player's ID (UUID)
            amount: Amount of health to restore

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        return await self._state_service.heal_player(player_id, amount)

    async def damage_player(self, player_id: uuid.UUID, amount: int, damage_type: str = "physical") -> dict[str, Any]:
        """
        Damage a player's health.

        Args:
            player_id: The player's ID (UUID)
            amount: Amount of damage to apply
            damage_type: Type of damage

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        return await self._state_service.damage_player(player_id, amount, damage_type)

    async def respawn_player_by_user_id(  # pylint: disable=too-many-locals  # Reason: Respawn requires many intermediate variables for complex respawn logic
        self,
        user_id: str,
        session: "AsyncSession",
        respawn_service: "PlayerRespawnService",
        persistence: Any,  # AsyncPersistenceLayer
    ) -> dict[str, Any]:
        """
        Respawn a dead player by user ID.

        This method handles the complete respawn flow:
        1. Gets player by user_id
        2. Verifies player is dead
        3. Calls respawn service to respawn player
        4. Gets respawn room data
        5. Returns structured response

        Args:
            user_id: The user ID to respawn
            session: Database session for player data access
            respawn_service: PlayerRespawnService instance
            persistence: AsyncPersistenceLayer for room data access

        Returns:
            dict: Respawn response with player and room data

        Raises:
            ValidationError: If player not found or not dead
        """
        return await self._respawn_wrapper.respawn_player_by_user_id(user_id, session, respawn_service, persistence)

    async def respawn_player_from_delirium_by_user_id(  # pylint: disable=too-many-locals  # Reason: Delirium respawn requires many intermediate variables for complex respawn logic
        self,
        user_id: str,
        session: "AsyncSession",
        respawn_service: "PlayerRespawnService",
        persistence: Any,  # AsyncPersistenceLayer
    ) -> dict[str, Any]:
        """
        Respawn a delirious player by user ID.

        This method handles the complete delirium respawn flow:
        1. Gets player by user_id
        2. Verifies player is delirious (lucidity <= -10)
        3. Calls respawn service to respawn player from delirium
        4. Gets respawn room data
        5. Returns structured response

        Args:
            user_id: The user ID to respawn
            session: Database session for player data access
            respawn_service: PlayerRespawnService instance
            persistence: AsyncPersistenceLayer for room data access

        Returns:
            dict: Respawn response with player and room data

        Raises:
            ValidationError: If player not found or not delirious
        """
        return await self._respawn_wrapper.respawn_player_from_delirium_by_user_id(
            user_id, session, respawn_service, persistence
        )

    async def convert_player_to_schema(self, player: Any) -> PlayerRead:
        """
        Convert a player object to PlayerRead schema.

        This is a public method that wraps the internal conversion logic.

        Args:
            player: Player object or dictionary

        Returns:
            PlayerRead: The player data in schema format
        """
        return await self._schema_converter.convert_player_to_schema(player)
