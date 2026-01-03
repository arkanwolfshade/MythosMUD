"""
Phantom hostile service for MythosMUD.

Implements phantom hostile spawns for lucidity hallucinations:
- 1 HP phantoms that dissipate on hit
- Player-specific entities (only visible to the hallucinating player)
- Combat integration with special handling
- [Phantom] tag in combat logs after dismissal

Spec: Fractured tier (15% chance of non-damaging combat), Deranged tier (attackable but vanish on hit)
"""

from __future__ import annotations

import random
import uuid
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Phantom hostile names for variety
PHANTOM_HOSTILE_NAMES: list[str] = [
    "Shambling Horror",
    "Writhing Shadow",
    "Echo of Madness",
    "Phantom Menace",
    "Terror Manifest",
    "Whispering Phantom",
    "Dread Apparition",
    "Nightmare Form",
]


class PhantomHostileService:
    """
    Service for managing phantom hostile spawns for hallucinations.

    NOTE: This is a foundational service. Full implementation requires:
    1. Player-specific NPC/entity system (hallucinations only visible to one player)
    2. Combat integration with special phantom handling
    3. Client-side rendering of phantom entities
    4. Combat log tagging with [Phantom] after dismissal

    This service provides the core logic for phantom hostile generation and tracking.
    """

    def __init__(self) -> None:
        """Initialize the phantom hostile service."""
        logger.info("PhantomHostileService initialized")
        # Track active phantom hostiles per player (player_id -> list of phantom_ids)
        self._active_phantoms: dict[str, list[str]] = {}

    def should_spawn_phantom_hostile(self, tier: str) -> bool:
        """
        Check if a phantom hostile should spawn based on tier.

        Args:
            tier: Current lucidity tier ("fractured" or "deranged")

        Returns:
            True if phantom hostile should spawn, False otherwise
        """
        if tier == "fractured":
            # Fractured: 15% chance of non-damaging combat
            return random.random() < 0.15
        if tier == "deranged":
            # Deranged: Always spawn if hallucination triggers (handled by frequency system)
            # This method just confirms it's a valid tier for phantoms
            return True
        return False

    def generate_phantom_name(self) -> str:
        """
        Generate a random phantom hostile name.

        Returns:
            Random phantom hostile name
        """
        return random.choice(PHANTOM_HOSTILE_NAMES)

    def create_phantom_hostile_data(self, player_id: uuid.UUID, room_id: str, tier: str) -> dict[str, Any]:
        """
        Create phantom hostile data structure.

        Args:
            player_id: Player UUID who will see the phantom
            room_id: Room where phantom should appear
            tier: Lucidity tier (affects behavior)

        Returns:
            Dictionary with phantom hostile data
        """
        phantom_id = f"phantom_{player_id}_{uuid.uuid4().hex[:8]}"
        phantom_name = self.generate_phantom_name()

        # Track this phantom for the player
        player_id_str = str(player_id)
        if player_id_str not in self._active_phantoms:
            self._active_phantoms[player_id_str] = []
        self._active_phantoms[player_id_str].append(phantom_id)

        return {
            "phantom_id": phantom_id,
            "player_id": str(player_id),
            "room_id": room_id,
            "name": phantom_name,
            "tier": tier,
            "max_dp": 1,  # Phantoms have 1 HP
            "current_dp": 1,
            "is_non_damaging": tier == "fractured",  # Fractured tier: non-damaging combat
        }

    def remove_phantom(self, player_id: uuid.UUID, phantom_id: str) -> bool:
        """
        Remove a phantom hostile from tracking.

        Args:
            player_id: Player UUID
            phantom_id: Phantom ID to remove

        Returns:
            True if phantom was found and removed, False otherwise
        """
        player_id_str = str(player_id)
        if player_id_str in self._active_phantoms:
            if phantom_id in self._active_phantoms[player_id_str]:
                self._active_phantoms[player_id_str].remove(phantom_id)
                logger.debug("Phantom hostile removed", player_id=player_id, phantom_id=phantom_id)
                return True
        return False

    def get_active_phantoms(self, player_id: uuid.UUID) -> list[str]:
        """
        Get list of active phantom IDs for a player.

        Args:
            player_id: Player UUID

        Returns:
            List of active phantom IDs
        """
        player_id_str = str(player_id)
        return self._active_phantoms.get(player_id_str, [])

    def clear_all_phantoms(self, player_id: uuid.UUID) -> None:
        """
        Clear all phantom hostiles for a player.

        Args:
            player_id: Player UUID
        """
        player_id_str = str(player_id)
        if player_id_str in self._active_phantoms:
            count = len(self._active_phantoms[player_id_str])
            del self._active_phantoms[player_id_str]
            logger.debug("All phantoms cleared for player", player_id=player_id, count=count)


__all__ = ["PhantomHostileService", "PHANTOM_HOSTILE_NAMES"]
