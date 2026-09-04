"""
Unit tests for NATS Pattern Matcher.

Tests the PatternMatcher class.
"""

import pytest

from server.services.nats_subject_manager.pattern_matcher import PatternMatcher


@pytest.fixture
def pattern_matcher():
    """Create PatternMatcher instance."""
    return PatternMatcher()


@pytest.fixture
def strict_pattern_matcher():
    """Create PatternMatcher with strict validation."""
    return PatternMatcher(strict_validation=True)


def test_pattern_matcher_init():
    """Test PatternMatcher initialization."""
    matcher = PatternMatcher()
    assert matcher._strict_validation is False


def test_pattern_matcher_init_strict():
    """Test PatternMatcher initialization with strict validation."""
    matcher = PatternMatcher(strict_validation=True)
    assert matcher._strict_validation is True


def test_matches_any_pattern_exact_match(pattern_matcher):
    """Test matches_any_pattern() returns True for exact match."""
    patterns = {
        "chat_say_room": {
            "pattern": "chat.say.room.{room_id}",
            "required_params": ["room_id"],
        }
    }
    assert pattern_matcher.matches_any_pattern("chat.say.room.arkham_1", patterns) is True


def test_matches_any_pattern_no_match(pattern_matcher):
    """Test matches_any_pattern() returns False when no match."""
    patterns = {
        "chat_say_room": {
            "pattern": "chat.say.room.{room_id}",
            "required_params": ["room_id"],
        }
    }
    assert pattern_matcher.matches_any_pattern("invalid.subject.format", patterns) is False


def test_matches_any_pattern_different_length(pattern_matcher):
    """Test matches_any_pattern() returns False for different component count."""
    patterns = {
        "chat_say_room": {
            "pattern": "chat.say.room.{room_id}",
            "required_params": ["room_id"],
        }
    }
    assert pattern_matcher.matches_any_pattern("chat.say", patterns) is False


def test_matches_any_pattern_multiple_patterns(pattern_matcher):
    """Test matches_any_pattern() matches any of multiple patterns."""
    patterns = {
        "chat_say_room": {
            "pattern": "chat.say.room.{room_id}",
            "required_params": ["room_id"],
        },
        "chat_global": {
            "pattern": "chat.global",
            "required_params": [],
        },
    }
    assert pattern_matcher.matches_any_pattern("chat.global", patterns) is True
    assert pattern_matcher.matches_any_pattern("chat.say.room.arkham_1", patterns) is True


def test_matches_any_pattern_strict_validation(strict_pattern_matcher):
    """Test matches_any_pattern() respects strict validation."""
    patterns = {
        "chat_say_room": {
            "pattern": "chat.say.room.{room_id}",
            "required_params": ["room_id"],
        }
    }
    # Underscores not allowed in strict mode
    assert strict_pattern_matcher.matches_any_pattern("chat.say.room.arkham_1", patterns) is False
    # Hyphens allowed
    assert strict_pattern_matcher.matches_any_pattern("chat.say.room.arkham-1", patterns) is True


def test_components_match_pattern_exact(pattern_matcher):
    """Test _components_match_pattern() matches exact components."""
    components = ["chat", "say", "room", "arkham_1"]
    pattern_components = ["chat", "say", "room", "{room_id}"]
    assert pattern_matcher._components_match_pattern(components, pattern_components) is True


def test_components_match_pattern_placeholder(pattern_matcher):
    """Test _components_match_pattern() matches placeholder components."""
    components = ["chat", "say", "room", "arkham_1"]
    pattern_components = ["chat", "say", "room", "{room_id}"]
    assert pattern_matcher._components_match_pattern(components, pattern_components) is True


def test_components_match_pattern_mismatch(pattern_matcher):
    """Test _components_match_pattern() returns False for mismatch."""
    components = ["chat", "say", "room", "arkham_1"]
    pattern_components = ["chat", "whisper", "room", "{room_id}"]  # "say" != "whisper"
    assert pattern_matcher._components_match_pattern(components, pattern_components) is False


def test_components_match_pattern_invalid_placeholder_value(pattern_matcher):
    """Test _components_match_pattern() validates placeholder values."""
    components = ["chat", "say", "room", "arkham@1"]  # Invalid characters
    pattern_components = ["chat", "say", "room", "{room_id}"]
    assert pattern_matcher._components_match_pattern(components, pattern_components) is False


def test_components_match_pattern_strict_no_underscores(strict_pattern_matcher):
    """Test _components_match_pattern() disallows underscores in strict mode."""
    components = ["chat", "say", "room", "arkham_1"]  # Underscore
    pattern_components = ["chat", "say", "room", "{room_id}"]
    assert strict_pattern_matcher._components_match_pattern(components, pattern_components) is False


def test_components_match_pattern_strict_allows_hyphens(strict_pattern_matcher):
    """Test _components_match_pattern() allows hyphens in strict mode."""
    components = ["chat", "say", "room", "arkham-1"]  # Hyphen
    pattern_components = ["chat", "say", "room", "{room_id}"]
    assert strict_pattern_matcher._components_match_pattern(components, pattern_components) is True


def test_components_match_pattern_numbers(pattern_matcher):
    """Test _components_match_pattern() allows numbers in placeholder."""
    components = ["chat", "say", "room", "123"]
    pattern_components = ["chat", "say", "room", "{room_id}"]
    assert pattern_matcher._components_match_pattern(components, pattern_components) is True


def test_components_match_pattern_multiple_placeholders(pattern_matcher):
    """Test _components_match_pattern() handles multiple placeholders."""
    components = ["chat", "whisper", "player", "player_123"]
    pattern_components = ["chat", "whisper", "player", "{target_id}"]
    assert pattern_matcher._components_match_pattern(components, pattern_components) is True
