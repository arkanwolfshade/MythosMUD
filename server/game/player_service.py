"""
Player service for MythosMUD server.

This module handles all player-related business logic including
creation, retrieval, validation, and state management.
"""

import datetime
import uuid

from ..alias_storage import AliasStorage
from ..logging_config import get_logger
from ..models import Stats
from ..models.player import Player
from ..schemas.player import PlayerRead

logger = get_logger(__name__)


class PlayerService:
    """Service class for player-related business operations."""

    def __init__(self, persistence):
        """Initialize the player service with a persistence layer."""
        self.persistence = persistence
        logger.info("PlayerService initialized")

    def create_player(
        self,
        name: str,
        starting_room_id: str = "earth_arkham_city_northside_intersection_derby_high",
        user_id: uuid.UUID | None = None,
    ) -> PlayerRead:
        """
        Create a new player character.

        Args:
            name: The player's name
            starting_room_id: The room ID where the player starts
            user_id: Optional user ID (will be generated if not provided)

        Returns:
            PlayerRead: The created player data

        Raises:
            ValueError: If player name already exists
        """
        logger.info("Creating new player", name=name, starting_room_id=starting_room_id, user_id=user_id)

        # Check if player already exists
        existing_player = self.persistence.get_player_by_name(name)
        if existing_player:
            logger.warning("Player creation failed - name already exists", name=name)
            raise ValueError("Player name already exists")

        # Generate user_id if not provided
        if user_id is None:
            user_id = uuid.uuid4()
            logger.debug("Generated user_id for new player", name=name, user_id=user_id)

        current_time = datetime.datetime.now()
        player = Player(
            player_id=uuid.uuid4(),
            user_id=user_id,
            name=name,
            current_room_id=starting_room_id,
            experience_points=0,
            level=1,
            created_at=current_time,
            last_active=current_time,
        )

        # Save player to persistence
        self.persistence.save_player(player)
        logger.info("Player created successfully", name=name, player_id=player.player_id, user_id=user_id)

        # Convert to schema format
        return self._convert_player_to_schema(player)

    def create_player_with_stats(
        self,
        name: str,
        stats: Stats,
        starting_room_id: str = "earth_arkham_city_northside_intersection_derby_high",
        user_id: uuid.UUID | None = None,
    ) -> PlayerRead:
        """
        Create a new player character with specific stats.

        Args:
            name: The player's name
            stats: The player's stats
            starting_room_id: The room ID where the player starts
            user_id: Optional user ID (will be generated if not provided)

        Returns:
            PlayerRead: The created player data

        Raises:
            ValueError: If player name already exists
        """
        logger.info("Creating new player with stats", name=name, starting_room_id=starting_room_id, user_id=user_id)

        # Check if player already exists
        existing_player = self.persistence.get_player_by_name(name)
        if existing_player:
            logger.warning("Player creation failed - name already exists", name=name)
            raise ValueError("Player name already exists")

        # Generate user_id if not provided
        if user_id is None:
            user_id = uuid.uuid4()
            logger.debug("Generated user_id for new player", name=name, user_id=user_id)

        current_time = datetime.datetime.now()
        player = Player(
            player_id=uuid.uuid4(),
            user_id=user_id,
            name=name,
            current_room_id=starting_room_id,
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

        # Save player to persistence
        self.persistence.save_player(player)
        logger.info("Player created successfully with stats", name=name, player_id=player.player_id, user_id=user_id)

        # Convert to schema format
        return self._convert_player_to_schema(player)

    def get_player_by_id(self, player_id: str) -> PlayerRead | None:
        """
        Get a player by their ID.

        Args:
            player_id: The player's ID

        Returns:
            PlayerRead: The player data, or None if not found
        """
        logger.debug("Getting player by ID", player_id=player_id)

        player = self.persistence.get_player(player_id)
        if not player:
            logger.debug("Player not found by ID", player_id=player_id)
            return None

        # Safely get player name for logging
        player_name = player.name if hasattr(player, "name") else player.get("name", "unknown")
        logger.debug("Player found by ID", player_id=player_id, name=player_name)
        return self._convert_player_to_schema(player)

    def get_player_by_name(self, player_name: str) -> PlayerRead | None:
        """
        Get a player by their name.

        Args:
            player_name: The player's name

        Returns:
            PlayerRead: The player data, or None if not found
        """
        logger.debug("Getting player by name", player_name=player_name)

        player = self.persistence.get_player_by_name(player_name)
        if not player:
            logger.debug("Player not found by name", player_name=player_name)
            return None

        # Safely get player ID for logging
        player_id = player.player_id if hasattr(player, "player_id") else player.get("player_id", "unknown")
        logger.debug("Player found by name", player_name=player_name, player_id=player_id)
        return self._convert_player_to_schema(player)

    def list_players(self) -> list[PlayerRead]:
        """
        Get a list of all players.

        Returns:
            List[PlayerRead]: List of all players
        """
        logger.debug("Listing all players")
        players = self.persistence.list_players()
        result = []
        for player in players:
            result.append(self._convert_player_to_schema(player))
        logger.debug("Finished listing all players")
        return result

    def delete_player(self, player_id: str) -> tuple[bool, str]:
        """
        Delete a player character.

        Args:
            player_id: The player's ID

        Returns:
            tuple[bool, str]: (success, message)
        """
        logger.debug("Attempting to delete player", player_id=player_id)
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Player not found for deletion", player_id=player_id)
            return False, "Player not found"

        # Delete the player from the database
        success = self.persistence.delete_player(player_id)
        if not success:
            logger.error("Failed to delete player from persistence", player_id=player_id)
            return False, "Failed to delete player"

        # Safely get player name for logging
        player_name = player.name if hasattr(player, "name") else player.get("name", "unknown")
        logger.info("Player deleted successfully", player_id=player_id, name=player_name)

        # Delete player aliases if they exist
        alias_storage = AliasStorage()
        alias_storage.delete_player_aliases(player_name)
        logger.debug("Player aliases deleted", player_id=player_id, name=player_name)

        return True, f"Player {player_name} has been deleted"

    def _convert_player_to_schema(self, player) -> PlayerRead:
        """
        Convert a player object to PlayerRead schema.

        Args:
            player: Player object or dictionary

        Returns:
            PlayerRead: The player data in schema format
        """
        if hasattr(player, "player_id"):  # Player object
            return PlayerRead(
                id=player.player_id,
                user_id=player.user_id,
                name=player.name,
                current_room_id=player.current_room_id,
                experience_points=player.experience_points,
                level=player.level,
                stats=player.get_stats(),
                inventory=player.get_inventory(),
                status_effects=player.get_status_effects(),
                created_at=player.created_at,
                last_active=player.last_active,
            )
        else:  # Dictionary
            return PlayerRead(
                id=player["player_id"],
                user_id=player["user_id"],
                name=player["name"],
                current_room_id=player["current_room_id"],
                experience_points=player["experience_points"],
                level=player["level"],
                stats=player["stats"],
                inventory=player["inventory"],
                status_effects=player["status_effects"],
                created_at=player["created_at"],
                last_active=player["last_active"],
            )
