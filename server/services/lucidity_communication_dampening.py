"""
Communication dampening utilities for lucidity system.

Implements communication filtering and alteration based on lucidity tier
as specified in docs/lucidity-system.md section 5.3.
"""

import random
import re
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Mythos glyphs for Fractured tier messages
MYTHOS_GLYPHS = ["\u2601", "\u2602", "\u2603", "\u2604", "\u2605", "\u2606", "\u2607", "\u2608"]

# Syllable patterns for scrambling (simple word-based approach)
SYLLABLE_PATTERN = re.compile(r"\b\w+\b")


def apply_communication_dampening(
    message: str, sender_tier: str, receiver_tier: str | None = None, message_type: str = "chat"
) -> dict[str, Any]:
    """
    Apply communication dampening based on lucidity tiers.

    Args:
        message: Original message content
        sender_tier: Tier of the message sender
        receiver_tier: Tier of the message receiver (optional, for incoming messages)
        message_type: Type of message (chat, whisper, shout, etc.)

    Returns:
        Dictionary with:
            - message: Modified message content
            - tags: List of tags to apply (e.g., 'strained')
            - blocked: Boolean indicating if message should be blocked
    """
    result: dict[str, Any] = {
        "message": message,
        "tags": [],
        "blocked": False,
    }

    # Whisper from Uneasy character: Add [strained] flag
    if message_type == "whisper" and sender_tier == "uneasy":
        result["tags"].append("strained")

    # Fractured tier outgoing chat: 20% chance to append Mythos glyphs
    if sender_tier == "fractured" and message_type in ("chat", "say", "local", "global"):
        if random.random() < 0.20:
            glyph = random.choice(MYTHOS_GLYPHS)
            result["message"] = message + f" {glyph}"

    # Deranged tier: Block shout commands
    if sender_tier == "deranged" and message_type == "shout":
        result["blocked"] = True
        result["message"] = ""  # Message blocked, replaced with hallucination on client
        result["tags"].append("hallucination")
        logger.debug("Shout blocked for Deranged character", tier=sender_tier)

    # Fractured tier incoming: 30% chance to lose punctuation
    if receiver_tier == "fractured" and message_type in ("chat", "say", "local", "global", "whisper"):
        if random.random() < 0.30:
            # Remove punctuation
            result["message"] = re.sub(r'[.,!?;:"]', "", message)
            result["tags"].append("muffled")

    # Deranged tier incoming: 10% chance to scramble syllables
    if receiver_tier == "deranged" and message_type in ("chat", "say", "local", "global", "whisper"):
        if random.random() < 0.10:
            # Simple word scrambling: swap adjacent words
            words = message.split()
            if len(words) > 1:
                # Swap random adjacent pairs
                for _ in range(min(len(words) // 4, 3)):  # Scramble up to 3 pairs
                    i = random.randint(0, len(words) - 2)
                    words[i], words[i + 1] = words[i + 1], words[i]
                result["message"] = " ".join(words)
                result["tags"].append("scrambled")

    return result


def should_block_shout(tier: str) -> bool:
    """Check if shout should be blocked based on tier."""
    return tier == "deranged"


__all__ = [
    "apply_communication_dampening",
    "should_block_shout",
    "MYTHOS_GLYPHS",
]
