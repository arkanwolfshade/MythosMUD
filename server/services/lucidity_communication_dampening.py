"""
Communication dampening utilities for lucidity system.

Implements communication filtering and alteration based on lucidity tier
as specified in docs/lucidity-system.md section 5.3.
"""

import random
import re
from typing import TypedDict

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Mythos glyphs for Fractured tier messages
MYTHOS_GLYPHS = ["\u2601", "\u2602", "\u2603", "\u2604", "\u2605", "\u2606", "\u2607", "\u2608"]

# Syllable patterns for scrambling (simple word-based approach)
SYLLABLE_PATTERN = re.compile(r"\b\w+\b")

_CHAT_TYPES = frozenset({"chat", "say", "local", "global"})
_INCOMING_TYPES = frozenset({"chat", "say", "local", "global", "whisper"})


class DampeningResult(TypedDict):
    """Filtered chat payload after lucidity-tier effects."""

    message: str
    tags: list[str]
    blocked: bool


def _apply_sender_effects(result: DampeningResult, sender_tier: str, message_type: str) -> None:
    if message_type == "whisper" and sender_tier == "uneasy":
        result["tags"].append("strained")

    if sender_tier == "fractured" and message_type in _CHAT_TYPES:
        if random.random() < 0.20:  # nosec B311: Game mechanics probability check, not cryptographic
            glyph = random.choice(MYTHOS_GLYPHS)  # nosec B311: Game mechanics glyph selection, not cryptographic
            result["message"] = result["message"] + f" {glyph}"

    if sender_tier == "deranged" and message_type == "shout":
        result["blocked"] = True
        result["message"] = ""
        result["tags"].append("hallucination")
        logger.debug("Shout blocked for Deranged character", tier=sender_tier)


def _maybe_muffle_fractured_message(result: DampeningResult, receiver_tier: str | None, message_type: str) -> None:
    if receiver_tier != "fractured" or message_type not in _INCOMING_TYPES:
        return
    if random.random() >= 0.30:  # nosec B311: Game mechanics probability check, not cryptographic
        return
    result["message"] = re.sub(r'[.,!?;:"]', "", result["message"])
    result["tags"].append("muffled")


def _maybe_scramble_deranged_message(result: DampeningResult, receiver_tier: str | None, message_type: str) -> None:
    if receiver_tier != "deranged" or message_type not in _INCOMING_TYPES:
        return
    if random.random() >= 0.10:  # nosec B311: Game mechanics probability check, not cryptographic
        return
    words = result["message"].split()
    if len(words) <= 1:
        return
    for _ in range(min(len(words) // 4, 3)):
        index = random.randint(0, len(words) - 2)  # nosec B311: Game mechanics word scrambling
        words[index], words[index + 1] = words[index + 1], words[index]
    result["message"] = " ".join(words)
    result["tags"].append("scrambled")


def _apply_receiver_effects(result: DampeningResult, receiver_tier: str | None, message_type: str) -> None:
    _maybe_muffle_fractured_message(result, receiver_tier, message_type)
    _maybe_scramble_deranged_message(result, receiver_tier, message_type)


def apply_communication_dampening(
    message: str, sender_tier: str, receiver_tier: str | None = None, message_type: str = "chat"
) -> DampeningResult:
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
    result: DampeningResult = {
        "message": message,
        "tags": [],
        "blocked": False,
    }

    _apply_sender_effects(result, sender_tier, message_type)
    _apply_receiver_effects(result, receiver_tier, message_type)
    return result


def should_block_shout(tier: str) -> bool:
    """Check if shout should be blocked based on tier."""
    return tier == "deranged"
