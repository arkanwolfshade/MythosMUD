"""
Game mechanics service for MythosMUD server.

This module handles all game mechanics-related business logic including
sanity, fear, corruption, healing, and damage mechanics.
"""

from pathlib import Path  # noqa: F401

from ..logging_config import get_logger

logger = get_logger(__name__)


class GameMechanicsService:
    """Service class for game mechanics operations."""

    def __init__(self, persistence):
        """Initialize the game mechanics service with a persistence layer."""
        self.persistence = persistence
        logger.info("GameMechanicsService initialized")

    def apply_sanity_loss(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """Apply sanity loss to a player."""
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Sanity loss failed - player not found", player_id=player_id)
            return False, "Player not found"

        self.persistence.apply_sanity_loss(player, amount, source)
        logger.info("Sanity loss applied", player_id=player_id, amount=amount, source=source)
        return True, f"Applied {amount} sanity loss to {player.name}"

    def apply_fear(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """Apply fear to a player."""
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Fear application failed - player not found", player_id=player_id)
            return False, "Player not found"

        self.persistence.apply_fear(player, amount, source)
        logger.info("Fear applied", player_id=player_id, amount=amount, source=source)
        return True, f"Applied {amount} fear to {player.name}"

    def apply_corruption(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """Apply corruption to a player."""
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Corruption application failed - player not found", player_id=player_id)
            return False, "Player not found"

        self.persistence.apply_corruption(player, amount, source)
        logger.info("Corruption applied", player_id=player_id, amount=amount, source=source)
        return True, f"Applied {amount} corruption to {player.name}"

    def gain_occult_knowledge(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """Gain occult knowledge (with sanity loss)."""
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Occult knowledge gain failed - player not found", player_id=player_id)
            return False, "Player not found"

        self.persistence.gain_occult_knowledge(player, amount, source)
        logger.info("Occult knowledge gained", player_id=player_id, amount=amount, source=source)
        return True, f"Gained {amount} occult knowledge for {player.name}"

    def heal_player(self, player_id: str, amount: int) -> tuple[bool, str]:
        """Heal a player's health."""
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Healing failed - player not found", player_id=player_id)
            return False, "Player not found"

        self.persistence.heal_player(player, amount)
        logger.info("Player healed", player_id=player_id, amount=amount)
        return True, f"Healed {player.name} for {amount} health"

    def damage_player(self, player_id: str, amount: int, damage_type: str = "physical") -> tuple[bool, str]:
        """Damage a player's health."""
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Damage failed - player not found", player_id=player_id)
            return False, "Player not found"

        self.persistence.damage_player(player, amount, damage_type)
        logger.info("Player damaged", player_id=player_id, amount=amount, damage_type=damage_type)
        return True, f"Damaged {player.name} for {amount} {damage_type} damage"
