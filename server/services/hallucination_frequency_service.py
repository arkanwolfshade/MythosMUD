"""
Hallucination frequency service for MythosMUD.

Implements tier-based hallucination frequency system:
- Uneasy: 10% chance per room entry
- Fractured: 25% chance per 30 seconds
- Deranged: 45% chance per 20 seconds
"""

# pylint: disable=too-many-return-statements  # Reason: Hallucination frequency service requires multiple return statements for different tier checks and frequency calculations

from __future__ import annotations

import random
import uuid
from datetime import UTC, datetime, timedelta
from typing import Any, cast

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.lucidity import LucidityActionCode
from ..services.lucidity_service import LucidityService, resolve_tier
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Frequency configuration per tier
HALLUCINATION_FREQUENCIES: dict[str, dict[str, Any]] = {
    "uneasy": {"chance": 0.10, "trigger": "room_entry", "cooldown_seconds": 0},
    "fractured": {"chance": 0.25, "trigger": "time_based", "cooldown_seconds": 30},
    "deranged": {"chance": 0.45, "trigger": "time_based", "cooldown_seconds": 20},
}


class HallucinationFrequencyService:
    """Service for managing hallucination frequency checks based on player tier."""

    def __init__(self) -> None:
        """Initialize the hallucination frequency service."""
        logger.info("HallucinationFrequencyService initialized")

    async def _time_based_hallucination_due(
        self, player_id: uuid.UUID, tier: str, config: dict[str, Any], session: AsyncSession
    ) -> bool:
        lucidity_service = LucidityService(session)
        cooldown = await lucidity_service.get_cooldown(player_id, LucidityActionCode.HALLUCINATION_TIMER)

        now = datetime.now(UTC)
        if cooldown and cooldown.cooldown_expires_at:
            expires_at = (
                cooldown.cooldown_expires_at.replace(tzinfo=UTC)
                if cooldown.cooldown_expires_at.tzinfo is None
                else cooldown.cooldown_expires_at
            )
            if now < expires_at:
                return False

        should_trigger: bool = random.random() < cast(float, config["chance"])  # nosec B311
        if should_trigger:
            cooldown_expires = now + timedelta(seconds=cast(int, config["cooldown_seconds"]))
            await lucidity_service.set_cooldown(
                player_id, LucidityActionCode.HALLUCINATION_TIMER, cooldown_expires.replace(tzinfo=None)
            )
            logger.debug(
                "Hallucination triggered",
                player_id=player_id,
                tier=tier,
                trigger_type="time_based",
                cooldown_seconds=cast(int, config["cooldown_seconds"]),
            )
        return should_trigger

    async def should_trigger_hallucination(
        self,
        player_id: uuid.UUID,
        tier: str,
        trigger_type: str = "time_based",
        session: AsyncSession | None = None,
    ) -> bool:
        """
        Check if a hallucination should trigger based on tier and frequency rules.

        Args:
            player_id: Player UUID
            tier: Current lucidity tier
            trigger_type: Type of trigger ("room_entry" or "time_based")

        Returns:
            True if hallucination should trigger, False otherwise
        """
        if tier not in HALLUCINATION_FREQUENCIES:
            return False

        config = HALLUCINATION_FREQUENCIES[tier]
        if config["trigger"] != trigger_type:
            return False  # Wrong trigger type for this tier

        # For room entry (Uneasy), no cooldown - just roll the chance
        if trigger_type == "room_entry":
            return random.random() < cast(float, config["chance"])  # nosec B311: Game mechanics probability check, not cryptographic

        if trigger_type == "time_based":
            if session is None:
                logger.warning(
                    "Session required for time-based hallucination checks",
                    player_id=player_id,
                    tier=tier,
                )
                return False
            try:
                return await self._time_based_hallucination_due(player_id, tier, config, session)
            except Exception as e:  # pylint: disable=broad-except  # Reason: Hallucination frequency check errors unpredictable, must catch all exceptions to handle various failure modes during frequency validation
                logger.warning(
                    "Error checking hallucination frequency",
                    player_id=player_id,
                    tier=tier,
                    error=str(e),
                    error_type=type(e).__name__,
                )
                return False

        return False

    async def check_room_entry_hallucination(
        self, player_id: uuid.UUID, current_lcd: int, session: AsyncSession | None = None
    ) -> bool:
        """
        Check if hallucination should trigger on room entry (Uneasy tier).

        Args:
            player_id: Player UUID
            current_lcd: Current lucidity value
            session: Optional database session (not used for room entry checks)

        Returns:
            True if hallucination should trigger, False otherwise
        """
        tier = resolve_tier(current_lcd)
        return await self.should_trigger_hallucination(player_id, tier, "room_entry", session)

    async def check_time_based_hallucination(
        self, player_id: uuid.UUID, current_lcd: int, session: AsyncSession
    ) -> bool:
        """
        Check if hallucination should trigger based on time (Fractured/Deranged tiers).

        Args:
            player_id: Player UUID
            current_lcd: Current lucidity value
            session: Database session (required for cooldown checks)

        Returns:
            True if hallucination should trigger, False otherwise
        """
        tier = resolve_tier(current_lcd)
        return await self.should_trigger_hallucination(player_id, tier, "time_based", session)


__all__ = ["HallucinationFrequencyService", "HALLUCINATION_FREQUENCIES"]
