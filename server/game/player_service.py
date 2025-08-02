"""
Player service for MythosMUD server.

This module handles all player-related business logic including
creation, retrieval, validation, and state management.
"""

import datetime
import uuid

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..schemas.player import PlayerRead


class PlayerService:
    """Service class for player-related business operations."""

    def __init__(self, persistence):
        """Initialize the player service with a persistence layer."""
        self.persistence = persistence

    def create_player(
        self, name: str, starting_room_id: str = "arkham_001", user_id: uuid.UUID | None = None
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
        # Check if player already exists
        existing_player = self.persistence.get_player_by_name(name)
        if existing_player:
            raise ValueError("Player name already exists")

        # Generate user_id if not provided
        if user_id is None:
            user_id = uuid.uuid4()

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
        player = self.persistence.get_player(player_id)
        if not player:
            return None

        return self._convert_player_to_schema(player)

    def get_player_by_name(self, player_name: str) -> PlayerRead | None:
        """
        Get a player by their name.

        Args:
            player_name: The player's name

        Returns:
            PlayerRead: The player data, or None if not found
        """
        player = self.persistence.get_player_by_name(player_name)
        if not player:
            return None

        return self._convert_player_to_schema(player)

    def list_players(self) -> list[PlayerRead]:
        """
        Get a list of all players.

        Returns:
            List[PlayerRead]: List of all players
        """
        players = self.persistence.list_players()
        result = []
        for player in players:
            result.append(self._convert_player_to_schema(player))
        return result

    def delete_player(self, player_id: str) -> tuple[bool, str]:
        """
        Delete a player character.

        Args:
            player_id: The player's ID

        Returns:
            tuple[bool, str]: (success, message)
        """
        player = self.persistence.get_player(player_id)
        if not player:
            return False, "Player not found"

        # Delete the player from the database
        success = self.persistence.delete_player(player_id)
        if not success:
            return False, "Failed to delete player"

        # Delete player aliases if they exist
        alias_storage = AliasStorage()
        alias_storage.delete_player_aliases(player.name)

        return True, f"Player {player.name} has been deleted"

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
