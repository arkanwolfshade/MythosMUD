"""
Player state management service.

This module handles player state modifications including health, lucidity, fear, corruption, and occult knowledge.
"""

import uuid
from typing import Any

from ..exceptions import ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


class PlayerStateService:
    """Service for managing player state modifications."""

    def __init__(self, persistence: Any) -> None:
        """Initialize with a persistence layer."""
        self.persistence = persistence

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
        logger.info("Applying lucidity loss", player_id=player_id, amount=amount, source=source)

        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for lucidity loss", player_id=player_id)
            context = create_error_context()
            context.metadata["player_id"] = player_id
            context.metadata["operation"] = "apply_lucidity_loss"
            log_and_raise_enhanced(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found",
            )

        await self.persistence.apply_lucidity_loss(player, amount, source)
        logger.info("Lucidity loss applied successfully", player_id=player_id, amount=amount, source=source)
        return {"message": f"Applied {amount} lucidity loss to {player.name}"}

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
        logger.info("Applying fear", player_id=player_id, amount=amount, source=source)

        player = await self.persistence.get_player_by_id(player_id)
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

        await self.persistence.apply_fear(player, amount, source)
        logger.info("Fear applied successfully", player_id=player_id, amount=amount, source=source)
        return {"message": f"Applied {amount} fear to {player.name}"}

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
        logger.info("Applying corruption", player_id=player_id, amount=amount, source=source)

        player = await self.persistence.get_player_by_id(player_id)
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

        await self.persistence.apply_corruption(player, amount, source)
        logger.info("Corruption applied successfully", player_id=player_id, amount=amount, source=source)
        return {"message": f"Applied {amount} corruption to {player.name}"}

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
        logger.info("Gaining occult knowledge", player_id=player_id, amount=amount, source=source)

        player = await self.persistence.get_player_by_id(player_id)
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
        logger.info("Healing player", player_id=player_id, amount=amount)

        player = await self.persistence.get_player_by_id(player_id)
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
        logger.info("Damaging player", player_id=player_id, amount=amount, damage_type=damage_type)

        player = await self.persistence.get_player_by_id(player_id)
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
