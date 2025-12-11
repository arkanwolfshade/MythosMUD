"""
Subscription pattern utilities for NATS Subject Manager.

This module provides utilities for generating subscription patterns with wildcards.
"""

from typing import Any


def get_subscription_pattern(pattern_info: dict[str, Any]) -> str:
    """
    Convert a pattern template into a subscription pattern with wildcards.

    Args:
        pattern_info: Pattern information dictionary with 'pattern' and 'required_params'

    Returns:
        Subscription pattern with wildcards
    """
    pattern = pattern_info["pattern"]

    # Replace all parameter placeholders with wildcards
    subscription_pattern = pattern
    for param in pattern_info["required_params"]:
        placeholder = f"{{{param}}}"
        subscription_pattern = subscription_pattern.replace(placeholder, "*")

    return subscription_pattern


def get_chat_subscription_patterns(patterns: dict[str, dict[str, Any]]) -> list[str]:
    """
    Get all chat-related subscription patterns.

    Args:
        patterns: Dictionary of registered patterns

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
            chat_patterns.append(get_subscription_pattern(patterns[pattern_name]))

    return chat_patterns


def get_event_subscription_patterns(patterns: dict[str, dict[str, Any]]) -> list[str]:
    """
    Get all event-related subscription patterns.

    Args:
        patterns: Dictionary of registered patterns

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
            event_patterns.append(get_subscription_pattern(patterns[pattern_name]))

    return event_patterns
