"""
Fake hallucination service for MythosMUD.

Implements fake NPC tells and room text overlays for Fractured tier hallucinations:
- Fake NPC tells: Hallucinatory whispers from non-existent NPCs
- Room text overlays: Hallucinatory text overlays on room descriptions

Spec: Fractured tier (part of hallucination event palette when not a phantom hostile)
"""

from __future__ import annotations

import random
import uuid
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Fake NPC names for hallucinatory tells
FAKE_NPC_NAMES: list[str] = [
    "The Whisperer",
    "Echo of the Depths",
    "Shadow Voice",
    "Forgotten One",
    "The Unseen",
    "Voice in the Void",
    "Phantom Speaker",
    "Whispering Shadow",
]

# Fake NPC tell messages (Mythos-themed, unsettling)
FAKE_NPC_TELL_MESSAGES: list[str] = [
    "They're watching you...",
    "The walls have eyes, you know.",
    "It's not too late to leave.",
    "Can you hear the chanting?",
    "The door behind you just closed.",
    "You're not alone in here.",
    "The shadows are moving.",
    "They're coming. They're coming for you.",
    "Don't look back. Don't ever look back.",
    "The whispers are getting louder.",
    "Something is wrong with this place.",
    "Your sanity is slipping away.",
]

# Room text overlay messages (Mythos-themed, unsettling)
ROOM_TEXT_OVERLAYS: list[str] = [
    "The walls seem to pulse with an unnatural rhythm.",
    "A faint, acrid smell hangs in the air.",
    "The shadows in the corner seem deeper than they should be.",
    "Something flickers at the edge of your vision.",
    "The temperature suddenly drops several degrees.",
    "You catch a whisper on the edge of hearing.",
    "The floorboards creak, though no one moves.",
    "Your reflection in the window seems to move on its own.",
    "The air grows heavy and oppressive.",
    "A chill runs down your spine.",
    "The light seems to bend unnaturally.",
    "Something feels fundamentally wrong here.",
]


class FakeHallucinationService:
    """
    Service for generating fake NPC tells and room text overlays.

    These hallucination types are part of the Fractured tier event palette,
    appearing when a hallucination triggers but is not a phantom hostile spawn.
    """

    def __init__(self) -> None:
        """Initialize the fake hallucination service."""
        logger.info("FakeHallucinationService initialized")

    def generate_fake_npc_tell(self, player_id: uuid.UUID, room_id: str) -> dict[str, Any]:
        """
        Generate a fake NPC tell hallucination.

        Args:
            player_id: Player UUID who will receive the fake tell
            room_id: Room where the hallucination occurs

        Returns:
            Dictionary with fake NPC tell data
        """
        fake_npc_name = random.choice(FAKE_NPC_NAMES)  # nosec B311: Game mechanics hallucination generation, not cryptographic
        fake_message = random.choice(FAKE_NPC_TELL_MESSAGES)  # nosec B311: Game mechanics hallucination generation, not cryptographic

        return {
            "npc_name": fake_npc_name,
            "message": fake_message,
            "room_id": room_id,
            "hallucination_id": f"fake_tell_{player_id}_{uuid.uuid4().hex[:8]}",
        }

    def generate_room_text_overlay(self, player_id: uuid.UUID, room_id: str) -> dict[str, Any]:
        """
        Generate a room text overlay hallucination.

        Args:
            player_id: Player UUID who will see the overlay
            room_id: Room where the overlay appears

        Returns:
            Dictionary with room text overlay data
        """
        overlay_text = random.choice(ROOM_TEXT_OVERLAYS)  # nosec B311: Game mechanics hallucination generation, not cryptographic

        return {
            "overlay_text": overlay_text,
            "room_id": room_id,
            "hallucination_id": f"room_overlay_{player_id}_{uuid.uuid4().hex[:8]}",
        }

    def select_hallucination_type(self) -> str:
        """
        Select which type of fake hallucination to trigger (50/50 chance).

        Returns:
            Either "fake_npc_tell" or "room_text_overlay"
        """
        return random.choice(["fake_npc_tell", "room_text_overlay"])  # nosec B311: Game mechanics hallucination type selection, not cryptographic


__all__ = ["FakeHallucinationService", "FAKE_NPC_NAMES", "FAKE_NPC_TELL_MESSAGES", "ROOM_TEXT_OVERLAYS"]
