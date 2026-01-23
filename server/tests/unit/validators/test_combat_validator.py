"""
Unit tests for combat validator.

Tests the CombatValidator class for combat command validation with thematic error messages.
"""

from typing import Any

import pytest

from server.validators.combat_validator import CombatValidator

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def combat_validator():
    """Create a CombatValidator instance."""
    return CombatValidator()


def test_combat_validator_init(combat_validator):
    """Test CombatValidator initialization."""
    assert combat_validator.attack_aliases
    assert "attack" in combat_validator.attack_aliases
    assert "punch" in combat_validator.attack_aliases
    assert "kick" in combat_validator.attack_aliases
    assert combat_validator.error_messages
    assert "invalid_command" in combat_validator.error_messages


def test_validate_combat_command_valid(combat_validator):
    """Test validate_combat_command with valid command."""
    command_data = {"command_type": "attack", "args": ["target"]}
    player_context: dict[str, Any] = {}

    is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

    assert is_valid is True
    assert error_msg is None
    assert warning_msg is None


def test_validate_combat_command_invalid_command_type(combat_validator):
    """Test validate_combat_command with invalid command type."""
    command_data = {"command_type": "invalid_command", "args": ["target"]}
    player_context: dict[str, Any] = {}

    is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

    assert is_valid is False
    assert error_msg is not None
    assert "comprehension" in error_msg.lower() or "impossible" in error_msg.lower()
    assert warning_msg is None


def test_validate_combat_command_no_target(combat_validator):
    """Test validate_combat_command with no target."""
    command_data = {"command_type": "attack", "args": []}
    player_context: dict[str, Any] = {}

    is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

    assert is_valid is False
    assert error_msg is not None
    assert "target" in error_msg.lower()
    assert warning_msg is None


def test_validate_combat_command_invalid_target_name(combat_validator):
    """Test validate_combat_command with invalid target name format."""
    command_data = {"command_type": "attack", "args": ["target<script>"]}
    player_context: dict[str, Any] = {}

    is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

    assert is_valid is False
    assert error_msg is not None
    assert warning_msg is None


def test_validate_combat_command_suspicious_patterns(combat_validator):
    """Test validate_combat_command with suspicious patterns in target name."""
    # Note: Most suspicious patterns are caught by _is_valid_target_name format check
    # But we can test that the suspicious pattern check exists and works if format check somehow passes
    # The format check is very restrictive, so suspicious patterns are typically caught earlier
    command_data = {"command_type": "attack", "args": ["target<script>"]}
    player_context: dict[str, Any] = {}

    is_valid, error_msg, _warning_msg = combat_validator.validate_combat_command(command_data, player_context)

    # Suspicious patterns should be caught (either by format check or suspicious pattern check)
    assert is_valid is False
    assert error_msg is not None
    # Format check will catch most suspicious patterns, so warning might not be present


def test_validate_combat_command_target_too_long(combat_validator):
    """Test validate_combat_command with target name too long."""
    # Note: _is_valid_target_name checks length > 50 at line 294
    # The explicit check at line 161 would only trigger if _is_valid_target_name passes
    # but len(target_name) > 50, which is impossible since _is_valid_target_name already checks this
    # So line 161 is unreachable for length > 50, but we test that length > 50 is caught
    long_target = "a" * 51
    command_data = {"command_type": "attack", "args": [long_target]}
    player_context: dict[str, Any] = {}

    is_valid, error_msg, _warning_msg = combat_validator.validate_combat_command(command_data, player_context)

    assert is_valid is False
    assert error_msg is not None
    # Target will fail _is_valid_target_name check before reaching explicit length check
    # The explicit length check at line 161 is effectively unreachable


def test_validate_combat_command_rate_limited(combat_validator):
    """Test validate_combat_command when rate limited."""
    command_data = {"command_type": "attack", "args": ["target"]}
    player_context: dict[str, Any] = {"rate_limited": True}

    # Mock rate limiting to return True
    combat_validator._is_rate_limited = lambda ctx: ctx.get("rate_limited", False)

    is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

    assert is_valid is False
    assert error_msg is not None
    assert "pause" in error_msg.lower() or "wait" in error_msg.lower() or "moment" in error_msg.lower()
    assert warning_msg is None


def test_validate_combat_command_exception_handling(combat_validator):
    """Test validate_combat_command handles exceptions gracefully."""
    command_data = None  # Invalid data to cause exception
    player_context: dict[str, Any] = {}

    is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

    assert is_valid is False
    assert error_msg is not None
    assert "cosmic forces" in error_msg.lower() or "rejected" in error_msg.lower()
    assert warning_msg is None


def test_validate_target_exists_exact_match(combat_validator):
    """Test validate_target_exists with exact match."""
    target_name = "Enemy"
    available_targets = ["Enemy", "Friend", "Neutral"]

    target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

    assert target_exists is True
    assert error_msg is None


def test_validate_target_exists_case_insensitive(combat_validator):
    """Test validate_target_exists with case-insensitive match."""
    target_name = "enemy"
    available_targets = ["Enemy", "Friend"]

    target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

    assert target_exists is True
    assert error_msg is None


def test_validate_target_exists_partial_match(combat_validator):
    """Test validate_target_exists with partial match."""
    target_name = "en"
    available_targets = ["Enemy", "Friend"]

    target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

    assert target_exists is False
    assert error_msg is not None
    assert "did you mean" in error_msg.lower() or "enemy" in error_msg.lower()


def test_validate_target_exists_no_match(combat_validator):
    """Test validate_target_exists with no match."""
    target_name = "Nonexistent"
    available_targets = ["Enemy", "Friend"]

    target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

    assert target_exists is False
    assert error_msg is not None
    assert "nonexistent" in error_msg.lower() or "not here" in error_msg.lower()


def test_validate_target_exists_no_target_name(combat_validator):
    """Test validate_target_exists with empty target name."""
    target_name = ""
    available_targets = ["Enemy", "Friend"]

    target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

    assert target_exists is False
    assert error_msg is not None
    assert "target" in error_msg.lower() or "direction" in error_msg.lower()


def test_validate_target_alive_alive(combat_validator):
    """Test validate_target_alive when target is alive."""
    target_name = "Enemy"
    is_alive = True

    is_alive_valid, error_msg = combat_validator.validate_target_alive(target_name, is_alive)

    assert is_alive_valid is True
    assert error_msg is None


def test_validate_target_alive_dead(combat_validator):
    """Test validate_target_alive when target is dead."""
    target_name = "Enemy"
    is_alive = False

    is_alive_valid, error_msg = combat_validator.validate_target_alive(target_name, is_alive)

    assert is_alive_valid is False
    assert error_msg is not None
    assert "enemy" in error_msg.lower() or "life force" in error_msg.lower() or "dead" in error_msg.lower()


def test_validate_combat_state_in_combat_required(combat_validator):
    """Test validate_combat_state when in combat and combat required."""
    is_in_combat = True
    required_state = True

    state_valid, error_msg = combat_validator.validate_combat_state(is_in_combat, required_state)

    assert state_valid is True
    assert error_msg is None


def test_validate_combat_state_not_in_combat_required(combat_validator):
    """Test validate_combat_state when not in combat but combat required."""
    is_in_combat = False
    required_state = True

    state_valid, error_msg = combat_validator.validate_combat_state(is_in_combat, required_state)

    assert state_valid is False
    assert error_msg is not None
    assert "not" in error_msg.lower() or "peace" in error_msg.lower()


def test_validate_combat_state_in_combat_not_required(combat_validator):
    """Test validate_combat_state when in combat but combat not required."""
    is_in_combat = True
    required_state = False

    state_valid, error_msg = combat_validator.validate_combat_state(is_in_combat, required_state)

    assert state_valid is False
    assert error_msg is not None
    assert "already" in error_msg.lower() or "engaged" in error_msg.lower()


def test_validate_combat_state_not_in_combat_not_required(combat_validator):
    """Test validate_combat_state when not in combat and combat not required."""
    is_in_combat = False
    required_state = False

    state_valid, error_msg = combat_validator.validate_combat_state(is_in_combat, required_state)

    assert state_valid is True
    assert error_msg is None


def test_validate_attack_strength_success(combat_validator):
    """Test validate_attack_strength with successful validation."""
    player_level = 10
    target_level = 10
    weapon_power = 1

    can_attack, error_msg, warning_msg = combat_validator.validate_attack_strength(
        player_level, target_level, weapon_power
    )

    assert can_attack is True
    assert error_msg is None
    assert warning_msg is None


def test_validate_attack_strength_target_too_strong(combat_validator):
    """Test validate_attack_strength when target is too strong."""
    player_level = 10
    target_level = 25  # More than 10 levels higher
    weapon_power = 1

    can_attack, error_msg, warning_msg = combat_validator.validate_attack_strength(
        player_level, target_level, weapon_power
    )

    assert can_attack is False
    assert error_msg is not None
    assert "strength" in error_msg.lower() or "feeble" in error_msg.lower()
    assert warning_msg is None


def test_validate_attack_strength_target_significantly_stronger(combat_validator):
    """Test validate_attack_strength when target is significantly stronger."""
    player_level = 10
    target_level = 17  # More than 5 levels higher but not more than 10
    weapon_power = 1

    can_attack, error_msg, warning_msg = combat_validator.validate_attack_strength(
        player_level, target_level, weapon_power
    )

    assert can_attack is True  # Can attack but with warning
    assert error_msg is None
    assert warning_msg is not None
    assert "warn" in warning_msg.lower() or "beyond" in warning_msg.lower()


def test_validate_attack_strength_weak_weapon(combat_validator):
    """Test validate_attack_strength with weak weapon."""
    player_level = 10
    target_level = 10
    weapon_power = 0  # Invalid weapon power

    can_attack, error_msg, warning_msg = combat_validator.validate_attack_strength(
        player_level, target_level, weapon_power
    )

    assert can_attack is False
    assert error_msg is not None
    assert "weapon" in error_msg.lower()
    assert warning_msg is None


def test_is_valid_target_name_valid(combat_validator):
    """Test _is_valid_target_name with valid target name."""
    assert combat_validator._is_valid_target_name("Enemy") is True
    assert combat_validator._is_valid_target_name("Enemy NPC") is True
    assert combat_validator._is_valid_target_name("Enemy-NPC") is True
    assert combat_validator._is_valid_target_name("Enemy's Guard") is True


def test_is_valid_target_name_invalid(combat_validator):
    """Test _is_valid_target_name with invalid target name."""
    assert combat_validator._is_valid_target_name("") is False
    assert combat_validator._is_valid_target_name(None) is False
    assert combat_validator._is_valid_target_name("Target<script>") is False
    assert combat_validator._is_valid_target_name("a" * 51) is False  # Too long
    assert combat_validator._is_valid_target_name("   ") is False  # Empty after strip


def test_contains_suspicious_patterns_detected(combat_validator):
    """Test _contains_suspicious_patterns detects suspicious patterns."""
    assert combat_validator._contains_suspicious_patterns("target<script>") is True
    assert combat_validator._contains_suspicious_patterns('target"alert') is True
    assert combat_validator._contains_suspicious_patterns("target;rm -rf") is True
    assert combat_validator._contains_suspicious_patterns("target|ls") is True
    assert combat_validator._contains_suspicious_patterns("target&echo") is True
    assert combat_validator._contains_suspicious_patterns("target../etc") is True
    assert combat_validator._contains_suspicious_patterns("targetjavascript:alert") is True
    assert combat_validator._contains_suspicious_patterns("targetdata:text/html") is True


def test_contains_suspicious_patterns_clean(combat_validator):
    """Test _contains_suspicious_patterns with clean target name."""
    assert combat_validator._contains_suspicious_patterns("Enemy") is False
    assert combat_validator._contains_suspicious_patterns("Enemy NPC") is False
    assert combat_validator._contains_suspicious_patterns("Enemy's Guard") is False


def test_is_rate_limited(combat_validator):
    """Test _is_rate_limited (currently always returns False)."""
    player_context: dict[str, Any] = {}
    assert combat_validator._is_rate_limited(player_context) is False


def test_get_random_error_message(combat_validator):
    """Test _get_random_error_message returns error message."""
    error_msg = combat_validator._get_random_error_message("invalid_command")
    assert error_msg is not None
    assert isinstance(error_msg, str)
    assert len(error_msg) > 0


def test_get_random_error_message_unknown_type(combat_validator):
    """Test _get_random_error_message with unknown error type."""
    error_msg = combat_validator._get_random_error_message("unknown_error_type")
    assert error_msg == "An error occurred."


def test_get_combat_help_message(combat_validator):
    """Test get_combat_help_message returns help message."""
    help_msg = combat_validator.get_combat_help_message()
    assert isinstance(help_msg, str)
    assert "attack" in help_msg.lower()
    assert "punch" in help_msg.lower()
    assert "kick" in help_msg.lower()


def test_get_combat_status_message_in_combat(combat_validator):
    """Test get_combat_status_message when in combat."""
    player_name = "Player"
    combat_state = {"in_combat": True, "target": "Enemy"}

    status_msg = combat_validator.get_combat_status_message(player_name, combat_state)

    assert isinstance(status_msg, str)
    assert player_name in status_msg
    assert "combat" in status_msg.lower()
    assert "enemy" in status_msg.lower()


def test_get_combat_status_message_not_in_combat(combat_validator):
    """Test get_combat_status_message when not in combat."""
    player_name = "Player"
    combat_state = {"in_combat": False}

    status_msg = combat_validator.get_combat_status_message(player_name, combat_state)

    assert isinstance(status_msg, str)
    assert player_name in status_msg
    assert "ready" in status_msg.lower() or "battle" in status_msg.lower()


def test_get_combat_result_message_success_with_damage(combat_validator):
    """Test get_combat_result_message with successful attack and damage."""
    action = "attack"
    target = "Enemy"
    success = True
    damage = 10

    result_msg = combat_validator.get_combat_result_message(action, target, success, damage)

    assert isinstance(result_msg, str)
    assert action in result_msg
    assert target in result_msg
    assert "10" in result_msg or "damage" in result_msg.lower()


def test_get_combat_result_message_success_no_damage(combat_validator):
    """Test get_combat_result_message with successful attack but no damage."""
    action = "attack"
    target = "Enemy"
    success = True
    damage = 0

    result_msg = combat_validator.get_combat_result_message(action, target, success, damage)

    assert isinstance(result_msg, str)
    assert action in result_msg
    assert target in result_msg


def test_get_combat_result_message_failure(combat_validator):
    """Test get_combat_result_message with failed attack."""
    action = "attack"
    target = "Enemy"
    success = False

    result_msg = combat_validator.get_combat_result_message(action, target, success)

    assert isinstance(result_msg, str)
    assert action in result_msg
    assert target in result_msg
    assert "fail" in result_msg.lower() or "mock" in result_msg.lower()


def test_get_combat_death_message(combat_validator):
    """Test get_combat_death_message returns death message."""
    target = "Enemy"
    killer = "Player"

    death_msg = combat_validator.get_combat_death_message(target, killer)

    assert isinstance(death_msg, str)
    assert target in death_msg
    assert killer in death_msg
    assert "life force" in death_msg.lower() or "void" in death_msg.lower() or "claim" in death_msg.lower()


def test_get_combat_victory_message(combat_validator):
    """Test get_combat_victory_message returns victory message."""
    player_name = "Player"
    target = "Enemy"
    xp_gained = 100

    victory_msg = combat_validator.get_combat_victory_message(player_name, target, xp_gained)

    assert isinstance(victory_msg, str)
    assert player_name in victory_msg
    assert target in victory_msg
    assert "100" in victory_msg or "experience" in victory_msg.lower()


def test_validate_combat_command_all_attack_aliases(combat_validator):
    """Test validate_combat_command accepts all attack aliases."""
    for alias in combat_validator.attack_aliases:
        command_data = {"command_type": alias, "args": ["target"]}
        player_context: dict[str, Any] = {}

        is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

        assert is_valid is True, f"Failed for alias: {alias}"
        assert error_msg is None
        assert warning_msg is None


def test_validate_combat_state_edge_case_return_true(combat_validator):
    """Test validate_combat_state fallback return (edge case coverage)."""
    # This tests the unreachable fallback return True, None at line 249
    # The function logic ensures all paths return before this, but we test for coverage
    is_in_combat = False
    required_state = False

    state_valid, error_msg = combat_validator.validate_combat_state(is_in_combat, required_state)

    assert state_valid is True
    assert error_msg is None


def test_validate_combat_command_suspicious_patterns_with_mock(combat_validator):
    """Test validate_combat_command suspicious patterns path (line 158)."""
    # Mock _is_valid_target_name to return True to reach suspicious pattern check
    # This tests the warning path that would trigger if format check somehow passed
    from unittest.mock import patch

    command_data = {"command_type": "attack", "args": ["target<script>"]}
    player_context: dict[str, Any] = {}

    with patch.object(combat_validator, "_is_valid_target_name", return_value=True):
        is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

        assert is_valid is False
        assert error_msg is not None
        assert warning_msg is not None
        assert "cosmic forces" in warning_msg.lower() or "amiss" in warning_msg.lower()


def test_validate_combat_command_target_too_long_with_mock(combat_validator):
    """Test validate_combat_command target too long warning path (line 163)."""
    # Mock _is_valid_target_name to return True to reach explicit length check
    # This tests the warning path that would trigger if format check somehow passed
    from unittest.mock import patch

    long_target = "a" * 51
    command_data = {"command_type": "attack", "args": [long_target]}
    player_context: dict[str, Any] = {}

    with patch.object(combat_validator, "_is_valid_target_name", return_value=True):
        with patch.object(combat_validator, "_contains_suspicious_patterns", return_value=False):
            is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

            assert is_valid is False
            assert error_msg is not None
            assert warning_msg is not None
            assert "too long" in warning_msg.lower() or "comprehension" in warning_msg.lower()
