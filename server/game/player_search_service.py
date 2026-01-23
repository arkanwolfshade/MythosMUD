"""
Player search and validation service.

This module handles player name resolution, search, and validation operations.
"""

from typing import cast

from ..schemas.player import PlayerRead
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PlayerSearchService:
    """Service for player search and validation operations."""

    def __init__(self, player_service):
        """Initialize with a reference to the player service for data access."""
        self.player_service = player_service

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
        player = await self.player_service.get_player_by_name(clean_name)
        if player:
            logger.debug("Exact match found", player_name=clean_name)
            return cast(PlayerRead, player)

        # Try case-insensitive exact match
        all_players = await self.player_service.list_players()
        for player_data in all_players:
            if player_data.name.lower() == clean_name.lower():
                logger.debug(
                    "Case-insensitive exact match found",
                    input_name=clean_name,
                    actual_name=player_data.name,
                )
                return cast(PlayerRead, player_data)

        # Try partial match (starts with)
        for player_data in all_players:
            if player_data.name.lower().startswith(clean_name.lower()):
                logger.debug(
                    "Partial match found (starts with)",
                    input_name=clean_name,
                    actual_name=player_data.name,
                )
                return cast(PlayerRead, player_data)

        # Try contains match (if no starts-with match found)
        for player_data in all_players:
            if clean_name.lower() in player_data.name.lower():
                logger.debug(
                    "Partial match found (contains)",
                    input_name=clean_name,
                    actual_name=player_data.name,
                )
                return cast(PlayerRead, player_data)

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
        return cast(list[PlayerRead], await self.player_service.list_players())

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
        all_players = await self.player_service.list_players()
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
