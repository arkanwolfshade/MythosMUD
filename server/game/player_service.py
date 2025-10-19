"""
Player service for MythosMUD server.

This module handles all player-related business logic including
creation, retrieval, validation, and state management.
"""

import datetime
import uuid

from ..alias_storage import AliasStorage
from ..config import get_config
from ..exceptions import DatabaseError, ValidationError
from ..logging.enhanced_logging_config import get_logger
from ..models import Stats
from ..models.player import Player
from ..schemas.player import PlayerRead
from ..utils.enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


class PlayerService:
    """Service class for player-related business operations."""

    def __init__(self, persistence):
        """Initialize the player service with a persistence layer."""
        self.persistence = persistence
        logger.info("PlayerService initialized")

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
        existing_player = await self.persistence.async_get_player_by_name(name)
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

        current_time = datetime.datetime.now()
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
        await self.persistence.async_save_player(player)
        logger.info("Player created successfully", player_id=player.player_id)

        # Convert to schema format
        return await self._convert_player_to_schema(player)

    async def create_player_with_stats(
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

        # Check if player already exists
        existing_player = await self.persistence.async_get_player_by_name(name)
        if existing_player:
            logger.warning("Player creation failed - name already exists")
            context = create_error_context()
            context.metadata["player_name"] = name
            context.metadata["operation"] = "create_player_with_stats"
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

        current_time = datetime.datetime.now()
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
            player.set_stats(stats)

        # Ensure JSON TEXT fields are initialized (SQLite NOT NULL constraints)
        if not getattr(player, "inventory", None):
            player.set_inventory([])
        if not getattr(player, "status_effects", None):
            player.set_status_effects([])

        # Save player to persistence
        await self.persistence.async_save_player(player)
        logger.info("Player created successfully with stats", player_id=player.player_id)

        # Convert to schema format
        return await self._convert_player_to_schema(player)

    async def get_player_by_id(self, player_id: str) -> PlayerRead | None:
        """
        Get a player by their ID.

        Args:
            player_id: The player's ID

        Returns:
            PlayerRead: The player data, or None if not found
        """
        logger.debug("Getting player by ID")

        player = await self.persistence.async_get_player(player_id)
        if not player:
            logger.debug("Player not found by ID")
            return None

        logger.debug("Player found by ID")
        return await self._convert_player_to_schema(player)

    async def get_player_by_name(self, player_name: str) -> PlayerRead | None:
        """
        Get a player by their name.

        Args:
            player_name: The player's name

        Returns:
            PlayerRead: The player data, or None if not found
        """
        logger.debug("Getting player by name")

        player = await self.persistence.async_get_player_by_name(player_name)
        if not player:
            logger.debug("Player not found by name")
            return None

        logger.debug("Player found by name")
        return await self._convert_player_to_schema(player)

    async def list_players(self) -> list[PlayerRead]:
        """
        Get a list of all players.

        Returns:
            List[PlayerRead]: List of all players
        """
        logger.debug("Listing all players")
        players = await self.persistence.async_list_players()
        result = []
        for player in players:
            result.append(await self._convert_player_to_schema(player))
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
        logger.debug("Resolving player name")

        if not player_name or not player_name.strip():
            logger.debug("Empty player name provided")
            return None

        # Clean the input
        clean_name = player_name.strip()

        # First try exact match (case-sensitive)
        player = await self.get_player_by_name(clean_name)
        if player:
            logger.debug("Exact match found", player_name=clean_name)
            return player

        # Try case-insensitive exact match
        all_players = await self.list_players()
        for player_data in all_players:
            if player_data.name.lower() == clean_name.lower():
                logger.debug(
                    "Case-insensitive exact match found",
                    input_name=clean_name,
                    actual_name=player_data.name,
                )
                return player_data

        # Try partial match (starts with)
        for player_data in all_players:
            if player_data.name.lower().startswith(clean_name.lower()):
                logger.debug(
                    "Partial match found (starts with)",
                    input_name=clean_name,
                    actual_name=player_data.name,
                )
                return player_data

        # Try contains match (if no starts-with match found)
        for player_data in all_players:
            if clean_name.lower() in player_data.name.lower():
                logger.debug(
                    "Partial match found (contains)",
                    input_name=clean_name,
                    actual_name=player_data.name,
                )
                return player_data

        logger.debug("No player name match found", player_name=clean_name)
        return None

    async def get_online_players(self) -> list[PlayerRead]:
        """
        Get a list of currently online players.

        Note: This is a placeholder implementation. In a full implementation,
        this would check against the connection manager to see which players
        are actually connected.

        Returns:
            List[PlayerRead]: List of online players
        """
        logger.debug("Getting online players")
        # For now, return all players. In a real implementation,
        # this would filter by connection status
        return await self.list_players()

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
        logger.debug("Searching players by name")

        if not search_term or not search_term.strip():
            logger.debug("Empty search term provided")
            return []

        clean_term = search_term.strip().lower()
        all_players = await self.list_players()
        matches = []

        # Score-based matching
        scored_matches = []
        for player in all_players:
            player_name_lower = player.name.lower()
            score = 0

            # Exact match gets highest score
            if player_name_lower == clean_term:
                score = 100
            # Starts with gets high score
            elif player_name_lower.startswith(clean_term):
                score = 50
            # Contains gets medium score
            elif clean_term in player_name_lower:
                score = 25
            else:
                continue

            scored_matches.append((score, player))

        # Sort by score (highest first) and then by name
        scored_matches.sort(key=lambda x: (-x[0], x[1].name.lower()))

        # Return top matches up to limit
        matches = [player for score, player in scored_matches[:limit]]

        logger.debug(
            "Player search completed",
            search_term=search_term,
            matches_found=len(matches),
        )
        return matches

    async def validate_player_name(self, player_name: str) -> tuple[bool, str]:
        """
        Validate a player name for chat system use.

        This checks if the name is valid and provides helpful error messages.

        Args:
            player_name: The player name to validate

        Returns:
            tuple[bool, str]: (is_valid, error_message)
        """
        logger.debug("Validating player name")

        if not player_name or not player_name.strip():
            return False, "Player name cannot be empty"

        clean_name = player_name.strip()

        # Check length
        if len(clean_name) < 2:
            return False, "Player name must be at least 2 characters long"

        if len(clean_name) > 20:
            return False, "Player name must be 20 characters or less"

        # Check for invalid characters
        invalid_chars = ["<", ">", "&", '"', "'", "\\", "/", "|", ":", ";", "*", "?"]
        for char in invalid_chars:
            if char in clean_name:
                return False, f"Player name cannot contain '{char}'"

        # Check if player exists
        player = await self.resolve_player_name(clean_name)
        if not player:
            return False, f"Player '{clean_name}' not found"

        return True, "Valid player name"

    async def delete_player(self, player_id: str) -> tuple[bool, str]:
        """
        Delete a player character.

        Args:
            player_id: The player's ID

        Returns:
            tuple[bool, str]: (success, message)
        """
        logger.debug("Attempting to delete player")
        player = await self.persistence.async_get_player(player_id)
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
        success = await self.persistence.async_delete_player(player_id)
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
            player = await self.persistence.async_get_player_by_name(player_name)
            if not player:
                logger.warning(f"Cannot update location - player not found: {player_name}")
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
            await self.persistence.async_save_player(player)

            logger.info(f"Player location updated: {player_name} moved from {old_room} to {new_room_id}")
            return True

        except Exception as e:
            logger.error(f"Failed to update player location: {player_name} -> {new_room_id}: {str(e)}")
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

    async def apply_sanity_loss(self, player_id: str, amount: int, source: str = "unknown") -> dict:
        """
        Apply sanity loss to a player.

        Args:
            player_id: The player's ID
            amount: Amount of sanity to lose
            source: Source of the sanity loss

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        logger.info("Applying sanity loss", player_id=player_id, amount=amount, source=source)

        player = await self.persistence.async_get_player(player_id)
        if not player:
            logger.warning("Player not found for sanity loss", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "apply_sanity_loss"
            log_and_raise_enhanced(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found",
            )

        await self.persistence.async_apply_sanity_loss(player, amount, source)
        logger.info("Sanity loss applied successfully", player_id=player_id, amount=amount, source=source)
        return {"message": f"Applied {amount} sanity loss to {player.name}"}

    async def apply_fear(self, player_id: str, amount: int, source: str = "unknown") -> dict:
        """
        Apply fear to a player.

        Args:
            player_id: The player's ID
            amount: Amount of fear to apply
            source: Source of the fear

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        logger.info("Applying fear", player_id=player_id, amount=amount, source=source)

        player = await self.persistence.async_get_player(player_id)
        if not player:
            logger.warning("Player not found for fear application", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "apply_fear"
            log_and_raise_enhanced(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found",
            )

        await self.persistence.async_apply_fear(player, amount, source)
        logger.info("Fear applied successfully", player_id=player_id, amount=amount, source=source)
        return {"message": f"Applied {amount} fear to {player.name}"}

    async def apply_corruption(self, player_id: str, amount: int, source: str = "unknown") -> dict:
        """
        Apply corruption to a player.

        Args:
            player_id: The player's ID
            amount: Amount of corruption to apply
            source: Source of the corruption

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        logger.info("Applying corruption", player_id=player_id, amount=amount, source=source)

        player = await self.persistence.async_get_player(player_id)
        if not player:
            logger.warning("Player not found for corruption application", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "apply_corruption"
            log_and_raise_enhanced(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found",
            )

        await self.persistence.async_apply_corruption(player, amount, source)
        logger.info("Corruption applied successfully", player_id=player_id, amount=amount, source=source)
        return {"message": f"Applied {amount} corruption to {player.name}"}

    async def gain_occult_knowledge(self, player_id: str, amount: int, source: str = "unknown") -> dict:
        """
        Gain occult knowledge (with sanity loss).

        Args:
            player_id: The player's ID
            amount: Amount of occult knowledge to gain
            source: Source of the knowledge

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        logger.info("Gaining occult knowledge", player_id=player_id, amount=amount, source=source)

        player = await self.persistence.async_get_player(player_id)
        if not player:
            logger.warning("Player not found for occult knowledge gain", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "gain_occult_knowledge"
            log_and_raise_enhanced(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found",
            )

        await self.persistence.async_gain_occult_knowledge(player, amount, source)
        logger.info("Occult knowledge gained successfully", player_id=player_id, amount=amount, source=source)
        return {"message": f"Gained {amount} occult knowledge for {player.name}"}

    async def heal_player(self, player_id: str, amount: int) -> dict:
        """
        Heal a player's health.

        Args:
            player_id: The player's ID
            amount: Amount of health to restore

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        logger.info("Healing player", player_id=player_id, amount=amount)

        player = await self.persistence.async_get_player(player_id)
        if not player:
            logger.warning("Player not found for healing", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "heal_player"
            log_and_raise_enhanced(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found",
            )

        await self.persistence.async_heal_player(player, amount)
        logger.info("Player healed successfully", player_id=player_id, amount=amount)
        return {"message": f"Healed {player.name} for {amount} health"}

    async def damage_player(self, player_id: str, amount: int, damage_type: str = "physical") -> dict:
        """
        Damage a player's health.

        Args:
            player_id: The player's ID
            amount: Amount of damage to apply
            damage_type: Type of damage

        Returns:
            dict: Success message

        Raises:
            ValidationError: If player not found
        """
        logger.info("Damaging player", player_id=player_id, amount=amount, damage_type=damage_type)

        player = await self.persistence.async_get_player(player_id)
        if not player:
            logger.warning("Player not found for damage", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "damage_player"
            log_and_raise_enhanced(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found",
            )

        await self.persistence.async_damage_player(player, amount, damage_type)
        logger.info("Player damaged successfully", player_id=player_id, amount=amount, damage_type=damage_type)
        return {"message": f"Damaged {player.name} for {amount} {damage_type} damage"}

    async def _convert_player_to_schema(self, player) -> PlayerRead:
        """
        Convert a player object to PlayerRead schema.

        Args:
            player: Player object or dictionary

        Returns:
            PlayerRead: The player data in schema format
        """
        # Get profession information
        player_profession_id = 0
        profession_name = None
        profession_description = None
        profession_flavor_text = None

        if hasattr(player, "profession_id"):
            player_profession_id = player.profession_id
        elif isinstance(player, dict):
            player_profession_id = player.get("profession_id", 0)

        # Fetch profession details from persistence
        if player_profession_id is not None:
            try:
                profession = await self.persistence.async_get_profession_by_id(player_profession_id)
                if profession:
                    profession_name = profession.name
                    profession_description = profession.description
                    profession_flavor_text = profession.flavor_text
            except Exception as e:
                logger.warning(f"Failed to fetch profession {player_profession_id}: {e}")

        if hasattr(player, "player_id"):  # Player object
            # Handle both sync and async method calls
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
                stats=stats,
                inventory=inventory,
                status_effects=status_effects,
                created_at=player.created_at,
                last_active=player.last_active,
                is_admin=bool(player.is_admin),  # Convert integer to boolean
            )
        else:  # Dictionary
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
                stats=player["stats"],
                inventory=player["inventory"],
                status_effects=player["status_effects"],
                created_at=player["created_at"],
                last_active=player["last_active"],
                is_admin=bool(player.get("is_admin", 0)),  # Convert integer to boolean with default
            )
