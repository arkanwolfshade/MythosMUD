"""
Subscription pattern utilities for NATS Subject Manager.

This module provides utilities for generating subscription patterns with wildcards.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .exceptions import SubjectValidationError

if TYPE_CHECKING:
    from .validation import SubjectValidator


def get_subscription_pattern(pattern_info: dict[str, Any], validator: SubjectValidator | None = None) -> str:
    """
    Convert a pattern template into a subscription pattern with wildcards.

    Args:
        pattern_info: Pattern information dictionary with 'pattern' and 'required_params'
        validator: Optional SubjectValidator instance for wildcard validation

    Returns:
        Subscription pattern with wildcards

    Raises:
        SubjectValidationError: If generated pattern is overly broad

    AI: Validates that generated subscription patterns are not too broad to prevent
        unintended message subscriptions.
    """
    pattern = pattern_info["pattern"]

    # Replace all parameter placeholders with wildcards
    subscription_pattern = pattern
    for param in pattern_info["required_params"]:
        placeholder = f"{{{param}}}"
        subscription_pattern = subscription_pattern.replace(placeholder, "*")

    # Validate that the pattern is not overly broad
    if validator:
        if not validator.validate_subscription_pattern(subscription_pattern):
            raise SubjectValidationError(
                f"Subscription pattern is too broad: {subscription_pattern}. "
                "Patterns with more than 2 wildcards, starting with wildcards, "
                "or all wildcards are not allowed."
            )

    return subscription_pattern


def get_chat_subscription_patterns(
    patterns: dict[str, dict[str, Any]], validator: SubjectValidator | None = None
) -> list[str]:
    """
    Get all chat-related subscription patterns.

    Args:
        patterns: Dictionary of registered patterns
        validator: Optional SubjectValidator instance for wildcard validation

    Returns:
        List of subscription patterns for chat subjects
    """
    chat_patterns = []

    # Get subscription patterns for predefined chat patterns
    chat_pattern_names = [
        "chat_say_room",
        "chat_local_subzone",
        "chat_global",
        "chat_whisper_player",
        "chat_system",
        "chat_emote_room",
        "chat_pose_room",
    ]

    for pattern_name in chat_pattern_names:
        if pattern_name in patterns:
            chat_patterns.append(get_subscription_pattern(patterns[pattern_name], validator=validator))

    return chat_patterns


def get_event_subscription_patterns(
    patterns: dict[str, dict[str, Any]], validator: SubjectValidator | None = None
) -> list[str]:
    """
    Get all event-related subscription patterns.

    Args:
        patterns: Dictionary of registered patterns
        validator: Optional SubjectValidator instance for wildcard validation

    Returns:
        List of subscription patterns for event subjects
    """
    event_patterns = []

    # Get subscription patterns for predefined event patterns
    event_pattern_names = [
        "event_player_entered",
        "event_player_left",
        "event_game_tick",
        "event_player_mortally_wounded",
        "event_player_dp_decay",
        "event_player_died",
        "event_player_respawned",
        "combat_attack",
        "combat_npc_attacked",
        "combat_npc_action",
        "combat_started",
        "combat_ended",
        "combat_npc_died",
        "combat_damage",
        "combat_turn",
        "combat_timeout",
    ]

    for pattern_name in event_pattern_names:
        if pattern_name in patterns:
            event_patterns.append(get_subscription_pattern(patterns[pattern_name], validator=validator))

    return event_patterns
