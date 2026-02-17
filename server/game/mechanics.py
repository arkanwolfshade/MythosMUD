"""
Game mechanics service for MythosMUD server.

This module handles all game mechanics-related business logic including
lucidity, fear, corruption, healing, and damage mechanics.
"""

from pathlib import Path  # noqa: F401  # pylint: disable=unused-import  # Reserved for future use
from typing import Any

from ..exceptions import ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise

logger = get_logger(__name__)


class GameMechanicsService:
    """Service class for game mechanics operations."""

    def __init__(self, persistence: Any) -> None:
        """Initialize the game mechanics service with a persistence layer."""
        self.persistence = persistence
        logger.info("GameMechanicsService initialized")

    async def apply_lucidity_loss(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """Apply lucidity loss to a player."""
        import uuid

        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        player = await self.persistence.get_player_by_id(player_uuid)
        if not player:
            logger.warning("Lucidity loss failed - player not found", player_id=player_id)
            log_and_raise(
                ValidationError,
                "Player not found for lucidity loss",
                player_id=player_id,
                amount=amount,
                source=source,
                operation="apply_lucidity_loss",
                details={"player_id": player_id, "amount": amount, "source": source},
                user_friendly="Player not found",
            )

        await self.persistence.apply_lucidity_loss(player, amount, source)
        logger.info("Lucidity loss applied", player_id=player_id, amount=amount, source=source)
        return True, f"Applied {amount} lucidity loss to {player.name}"

    async def apply_fear(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """Apply fear to a player."""
        import uuid

        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        player = await self.persistence.get_player_by_id(player_uuid)
        if not player:
            logger.warning("Fear application failed - player not found", player_id=player_id)
            log_and_raise(
                ValidationError,
                "Player not found for fear application",
                player_id=player_id,
                amount=amount,
                source=source,
                operation="apply_fear",
                details={"player_id": player_id, "amount": amount, "source": source},
                user_friendly="Player not found",
            )

        await self.persistence.apply_fear(player, amount, source)
        logger.info("Fear applied", player_id=player_id, amount=amount, source=source)
        return True, f"Applied {amount} fear to {player.name}"

    async def apply_corruption(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """Apply corruption to a player."""
        import uuid

        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        player = await self.persistence.get_player_by_id(player_uuid)
        if not player:
            logger.warning("Corruption application failed - player not found", player_id=player_id)
            log_and_raise(
                ValidationError,
                "Player not found for corruption application",
                player_id=player_id,
                amount=amount,
                source=source,
                operation="apply_corruption",
                details={"player_id": player_id, "amount": amount, "source": source},
                user_friendly="Player not found",
            )

        await self.persistence.apply_corruption(player, amount, source)
        logger.info("Corruption applied", player_id=player_id, amount=amount, source=source)
        return True, f"Applied {amount} corruption to {player.name}"

    async def gain_occult_knowledge(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """Gain occult knowledge (with lucidity loss)."""
        import uuid

        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        player = await self.persistence.get_player_by_id(player_uuid)
        if not player:
            logger.warning("Occult knowledge gain failed - player not found", player_id=player_id)
            log_and_raise(
                ValidationError,
                "Player not found for occult knowledge gain",
                player_id=player_id,
                amount=amount,
                source=source,
                operation="gain_occult_knowledge",
                details={"player_id": player_id, "amount": amount, "source": source},
                user_friendly="Player not found",
            )

        # Update occult_knowledge stat and apply lucidity loss
        from server.persistence.repositories.experience_repository import ExperienceRepository

        experience_repo = ExperienceRepository(event_bus=None)
        await experience_repo.update_player_stat_field(
            player.player_id, "occult_knowledge", amount, f"{source}: occult knowledge gain"
        )
        await self.persistence.apply_lucidity_loss(player, amount // 2, f"{source}: occult knowledge lucidity cost")
        logger.info("Occult knowledge gained", player_id=player_id, amount=amount, source=source)
        return True, f"Gained {amount} occult knowledge for {player.name}"

    async def heal_player(self, player_id: str, amount: int) -> tuple[bool, str]:
        """Heal a player's health."""
        import uuid

        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        player = await self.persistence.get_player_by_id(player_uuid)
        if not player:
            logger.warning("Healing failed - player not found", player_id=player_id)
            log_and_raise(
                ValidationError,
                "Player not found for healing",
                player_id=player_id,
                amount=amount,
                operation="heal_player",
                details={"player_id": player_id, "amount": amount},
                user_friendly="Player not found",
            )

        await self.persistence.heal_player(player, amount)
        logger.info("Player healed", player_id=player_id, amount=amount)
        return True, f"Healed {player.name} for {amount} health"

    async def damage_player(self, player_id: str, amount: int, damage_type: str = "physical") -> tuple[bool, str]:
        """Damage a player's health."""
        import uuid

        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        player = await self.persistence.get_player_by_id(player_uuid)
        if not player:
            logger.warning("Damage failed - player not found", player_id=player_id)
            log_and_raise(
                ValidationError,
                "Player not found for damage",
                player_id=player_id,
                amount=amount,
                damage_type=damage_type,
                operation="damage_player",
                details={"player_id": player_id, "amount": amount, "damage_type": damage_type},
                user_friendly="Player not found",
            )

        await self.persistence.damage_player(player, amount, damage_type)
        logger.info("Player damaged", player_id=player_id, amount=amount, damage_type=damage_type)
        return True, f"Damaged {player.name} for {amount} {damage_type} damage"

    async def gain_experience(self, player_id: str, amount: int, source: str = "unknown") -> tuple[bool, str]:
        """
        Award experience points to a player.

        CRITICAL FIX: This method prevents XP awards from overwriting combat damage.
        Uses atomic XP update via persistence.gain_experience so in-flight health
        changes from combat are not overwritten.

        Args:
            player_id: ID of the player gaining XP
            amount: Amount of XP to award
            source: Source of the XP (e.g., "killed_nightgaunt")

        Returns:
            tuple: (success: bool, message: str)
        """
        import uuid as _uuid

        player_uuid = _uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        player = await self.persistence.get_player_by_id(player_uuid)
        if not player:
            logger.warning("XP gain failed - player not found", player_id=player_id)
            log_and_raise(
                ValidationError,
                "Player not found for XP gain",
                player_id=player_id,
                amount=amount,
                source=source,
                operation="gain_experience",
                details={"player_id": player_id, "amount": amount, "source": source},
                user_friendly="Player not found",
            )

        await self.persistence.gain_experience(player, amount, source)
        logger.info("XP awarded", player_id=player_id, amount=amount, source=source)
        return True, f"Awarded {amount} XP to {player.name}"
