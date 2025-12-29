"""
Unit tests for NATS Subscription Patterns.

Tests the subscription pattern utility functions.
"""


from server.services.nats_subject_manager.subscription_patterns import (
    get_chat_subscription_patterns,
    get_event_subscription_patterns,
    get_subscription_pattern,
)


def test_get_subscription_pattern_single_param():
    """Test get_subscription_pattern() replaces single parameter."""
    pattern_info = {
        "pattern": "chat.say.room.{room_id}",
        "required_params": ["room_id"],
    }
    result = get_subscription_pattern(pattern_info)
    assert result == "chat.say.room.*"


def test_get_subscription_pattern_multiple_params():
    """Test get_subscription_pattern() replaces multiple parameters."""
    pattern_info = {
        "pattern": "chat.whisper.player.{target_id}.room.{room_id}",
        "required_params": ["target_id", "room_id"],
    }
    result = get_subscription_pattern(pattern_info)
    assert result == "chat.whisper.player.*.room.*"


def test_get_subscription_pattern_no_params():
    """Test get_subscription_pattern() returns pattern unchanged when no params."""
    pattern_info = {
        "pattern": "chat.global",
        "required_params": [],
    }
    result = get_subscription_pattern(pattern_info)
    assert result == "chat.global"


def test_get_chat_subscription_patterns():
    """Test get_chat_subscription_patterns() returns chat patterns."""
    patterns = {
        "chat_say_room": {
            "pattern": "chat.say.room.{room_id}",
            "required_params": ["room_id"],
        },
        "chat_global": {
            "pattern": "chat.global",
            "required_params": [],
        },
        "chat_whisper_player": {
            "pattern": "chat.whisper.player.{target_id}",
            "required_params": ["target_id"],
        },
    }
    result = get_chat_subscription_patterns(patterns)
    assert isinstance(result, list)
    assert "chat.say.room.*" in result
    assert "chat.global" in result
    assert "chat.whisper.player.*" in result


def test_get_chat_subscription_patterns_missing_pattern():
    """Test get_chat_subscription_patterns() handles missing patterns."""
    patterns = {
        "chat_global": {
            "pattern": "chat.global",
            "required_params": [],
        },
        # Missing chat_say_room
    }
    result = get_chat_subscription_patterns(patterns)
    assert "chat.global" in result
    # chat_say_room not included since it's missing


def test_get_event_subscription_patterns():
    """Test get_event_subscription_patterns() returns event patterns."""
    patterns = {
        "event_player_entered": {
            "pattern": "events.player_entered.{room_id}",
            "required_params": ["room_id"],
        },
        "event_game_tick": {
            "pattern": "events.game_tick",
            "required_params": [],
        },
        "combat_attack": {
            "pattern": "combat.attack.{room_id}",
            "required_params": ["room_id"],
        },
    }
    result = get_event_subscription_patterns(patterns)
    assert isinstance(result, list)
    assert "events.player_entered.*" in result
    assert "events.game_tick" in result
    assert "combat.attack.*" in result


def test_get_event_subscription_patterns_missing_pattern():
    """Test get_event_subscription_patterns() handles missing patterns."""
    patterns = {
        "event_game_tick": {
            "pattern": "events.game_tick",
            "required_params": [],
        },
        # Missing other event patterns
    }
    result = get_event_subscription_patterns(patterns)
    assert "events.game_tick" in result


def test_get_chat_subscription_patterns_empty():
    """Test get_chat_subscription_patterns() returns empty list when no chat patterns."""
    patterns = {
        "event_player_entered": {
            "pattern": "events.player_entered.{room_id}",
            "required_params": ["room_id"],
        },
    }
    result = get_chat_subscription_patterns(patterns)
    assert result == []


def test_get_event_subscription_patterns_empty():
    """Test get_event_subscription_patterns() returns empty list when no event patterns."""
    patterns = {
        "chat_global": {
            "pattern": "chat.global",
            "required_params": [],
        },
    }
    result = get_event_subscription_patterns(patterns)
    assert result == []
