"""
Unit tests for the CombatValidator class.

This module tests combat command validation, thematic error messages,
and security measures in isolation from other systems.
"""

import pytest

from server.validators.combat_validator import CombatValidator


class TestCombatValidatorUnit:
    """Unit tests for CombatValidator core functionality."""

    @pytest.fixture
    def combat_validator(self):
        """Create a combat validator instance for testing."""
        return CombatValidator()

    def test_combat_validator_initialization(self, combat_validator):
        """Test combat validator initialization."""
        assert hasattr(combat_validator, "attack_aliases")
        assert hasattr(combat_validator, "error_messages")
        assert isinstance(combat_validator.attack_aliases, set)
        assert isinstance(combat_validator.error_messages, dict)

    def test_attack_aliases_contains_expected_commands(self, combat_validator):
        """Test that attack aliases contain expected commands."""
        expected_aliases = {
            "attack",
            "punch",
            "kick",
            "strike",
            "hit",
            "smack",
            "thump",
            "pummel",
            "batter",
            "claw",
            "rend",
            "maul",
            "savage",
        }

        for alias in expected_aliases:
            assert alias in combat_validator.attack_aliases

    def test_error_messages_contains_expected_types(self, combat_validator):
        """Test that error messages contain expected types."""
        expected_types = {
            "invalid_command",
            "no_target",
            "target_not_found",
            "target_dead",
            "already_in_combat",
            "not_in_combat",
            "invalid_target",
            "insufficient_strength",
            "target_immune",
            "rate_limited",
            "invalid_weapon",
            "spell_interference",
        }

        for error_type in expected_types:
            assert error_type in combat_validator.error_messages
            assert isinstance(combat_validator.error_messages[error_type], list)
            assert len(combat_validator.error_messages[error_type]) > 0

    def test_validate_combat_command_valid_command(self, combat_validator):
        """Test validation of valid combat command."""
        command_data = {"command_type": "attack", "args": ["rat"]}
        player_context = {"player_id": "test_player_id", "player_name": "TestPlayer", "room_id": "test_room"}

        is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

        assert is_valid is True
        assert error_msg is None
        assert warning_msg is None

    def test_validate_combat_command_invalid_command_type(self, combat_validator):
        """Test validation of invalid command type."""
        command_data = {"command_type": "invalid_command", "args": ["rat"]}
        player_context = {"player_id": "test_player_id", "player_name": "TestPlayer", "room_id": "test_room"}

        is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

        assert is_valid is False
        assert error_msg is not None
        assert "ancient ones" in error_msg.lower() or "cosmic forces" in error_msg.lower()
        assert warning_msg is None

    def test_validate_combat_command_no_target(self, combat_validator):
        """Test validation of command with no target."""
        command_data = {"command_type": "attack", "args": []}
        player_context = {"player_id": "test_player_id", "player_name": "TestPlayer", "room_id": "test_room"}

        is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

        assert is_valid is False
        assert error_msg is not None
        assert "target" in error_msg.lower()
        assert warning_msg is None

    def test_validate_combat_command_suspicious_target(self, combat_validator):
        """Test validation of command with suspicious target."""
        command_data = {"command_type": "attack", "args": ["<script>alert('xss')</script>"]}
        player_context = {"player_id": "test_player_id", "player_name": "TestPlayer", "room_id": "test_room"}

        is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

        assert is_valid is False
        assert error_msg is not None
        assert warning_msg is not None
        assert "cosmic forces" in warning_msg.lower()

    def test_validate_combat_command_long_target_name(self, combat_validator):
        """Test validation of command with too long target name."""
        long_target = "a" * 100
        command_data = {"command_type": "attack", "args": [long_target]}
        player_context = {"player_id": "test_player_id", "player_name": "TestPlayer", "room_id": "test_room"}

        is_valid, error_msg, warning_msg = combat_validator.validate_combat_command(command_data, player_context)

        assert is_valid is False
        assert error_msg is not None
        assert warning_msg is not None
        assert "too long" in warning_msg.lower()

    def test_validate_target_exists_exact_match(self, combat_validator):
        """Test target existence validation with exact match."""
        target_name = "rat"
        available_targets = ["rat", "goblin", "orc"]

        target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

        assert target_exists is True
        assert error_msg is None

    def test_validate_target_exists_case_insensitive_match(self, combat_validator):
        """Test target existence validation with case insensitive match."""
        target_name = "RAT"
        available_targets = ["rat", "goblin", "orc"]

        target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

        assert target_exists is True
        assert error_msg is None

    def test_validate_target_exists_partial_match(self, combat_validator):
        """Test target existence validation with partial match."""
        target_name = "rat"
        available_targets = ["giant rat", "goblin", "orc"]

        target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

        assert target_exists is False
        assert error_msg is not None
        assert "giant rat" in error_msg  # Should suggest closest match

    def test_validate_target_exists_no_match(self, combat_validator):
        """Test target existence validation with no match."""
        target_name = "dragon"
        available_targets = ["rat", "goblin", "orc"]

        target_exists, error_msg = combat_validator.validate_target_exists(target_name, available_targets)

        assert target_exists is False
        assert error_msg is not None
        assert "dragon" in error_msg

    def test_validate_target_alive_alive_target(self, combat_validator):
        """Test target alive validation with alive target."""
        target_name = "rat"
        is_alive = True

        is_alive_result, error_msg = combat_validator.validate_target_alive(target_name, is_alive)

        assert is_alive_result is True
        assert error_msg is None

    def test_validate_target_alive_dead_target(self, combat_validator):
        """Test target alive validation with dead target."""
        target_name = "rat"
        is_alive = False

        is_alive_result, error_msg = combat_validator.validate_target_alive(target_name, is_alive)

        assert is_alive_result is False
        assert error_msg is not None
        assert "rat" in error_msg
        assert "dead" in error_msg.lower() or "lifeless" in error_msg.lower()

    def test_validate_combat_state_correct_state(self, combat_validator):
        """Test combat state validation with correct state."""
        is_in_combat = True
        required_state = True

        state_valid, error_msg = combat_validator.validate_combat_state(is_in_combat, required_state)

        assert state_valid is True
        assert error_msg is None

    def test_validate_combat_state_not_in_combat_when_required(self, combat_validator):
        """Test combat state validation when not in combat but required."""
        is_in_combat = False
        required_state = True

        state_valid, error_msg = combat_validator.validate_combat_state(is_in_combat, required_state)

        assert state_valid is False
        assert error_msg is not None
        assert "peace" in error_msg.lower() or "cosmic forces" in error_msg.lower()

    def test_validate_combat_state_in_combat_when_not_required(self, combat_validator):
        """Test combat state validation when in combat but not required."""
        is_in_combat = True
        required_state = False

        state_valid, error_msg = combat_validator.validate_combat_state(is_in_combat, required_state)

        assert state_valid is False
        assert error_msg is not None
        assert "battle" in error_msg.lower() or "conflict" in error_msg.lower()

    def test_validate_attack_strength_sufficient_strength(self, combat_validator):
        """Test attack strength validation with sufficient strength."""
        player_level = 10
        target_level = 8
        weapon_power = 1

        can_attack, error_msg, warning_msg = combat_validator.validate_attack_strength(
            player_level, target_level, weapon_power
        )

        assert can_attack is True
        assert error_msg is None
        assert warning_msg is None

    def test_validate_attack_strength_target_too_strong(self, combat_validator):
        """Test attack strength validation with target too strong."""
        player_level = 5
        target_level = 20  # Much higher level
        weapon_power = 1

        can_attack, error_msg, warning_msg = combat_validator.validate_attack_strength(
            player_level, target_level, weapon_power
        )

        assert can_attack is False
        assert error_msg is not None
        assert "strength" in error_msg.lower() or "mortal form" in error_msg.lower()
        assert warning_msg is None

    def test_validate_attack_strength_target_slightly_stronger(self, combat_validator):
        """Test attack strength validation with target slightly stronger."""
        player_level = 5
        target_level = 8  # Slightly higher level
        weapon_power = 1

        can_attack, error_msg, warning_msg = combat_validator.validate_attack_strength(
            player_level, target_level, weapon_power
        )

        assert can_attack is True
        assert error_msg is None
        assert warning_msg is not None
        assert "cosmic forces" in warning_msg.lower()

    def test_validate_attack_strength_weak_weapon(self, combat_validator):
        """Test attack strength validation with weak weapon."""
        player_level = 10
        target_level = 8
        weapon_power = 0  # Weak weapon

        can_attack, error_msg, warning_msg = combat_validator.validate_attack_strength(
            player_level, target_level, weapon_power
        )

        assert can_attack is False
        assert error_msg is not None
        assert "weapon" in error_msg.lower()
        assert warning_msg is None

    def test_is_valid_target_name_valid_names(self, combat_validator):
        """Test target name validation with valid names."""
        valid_names = ["rat", "giant rat", "orc-warrior", "dragon_lord", "king's guard"]

        for name in valid_names:
            assert combat_validator._is_valid_target_name(name) is True

    def test_is_valid_target_name_invalid_names(self, combat_validator):
        """Test target name validation with invalid names."""
        invalid_names = [
            "",  # Empty
            "   ",  # Whitespace only
            "a" * 100,  # Too long
            "rat<script>",  # Contains invalid characters
            "rat; rm -rf /",  # Contains command injection
        ]

        for name in invalid_names:
            assert combat_validator._is_valid_target_name(name) is False

    def test_contains_suspicious_patterns_detection(self, combat_validator):
        """Test suspicious pattern detection."""
        suspicious_patterns = [
            "<script>alert('xss')</script>",
            "rat; rm -rf /",
            "target | cat /etc/passwd",
            "npc && shutdown",
            "javascript:alert('xss')",
            "data:text/html",
        ]

        for pattern in suspicious_patterns:
            assert combat_validator._contains_suspicious_patterns(pattern) is True

    def test_contains_suspicious_patterns_clean_input(self, combat_validator):
        """Test suspicious pattern detection with clean input."""
        clean_inputs = [
            "rat",
            "giant rat",
            "orc warrior",
            "dragon lord",
            "king's guard",
        ]

        for input_text in clean_inputs:
            assert combat_validator._contains_suspicious_patterns(input_text) is False

    def test_get_random_error_message(self, combat_validator):
        """Test random error message generation."""
        error_type = "invalid_command"
        message = combat_validator._get_random_error_message(error_type)

        assert isinstance(message, str)
        assert len(message) > 0
        assert message in combat_validator.error_messages[error_type]

    def test_get_random_error_message_unknown_type(self, combat_validator):
        """Test random error message generation with unknown type."""
        error_type = "unknown_type"
        message = combat_validator._get_random_error_message(error_type)

        assert isinstance(message, str)
        assert message == "An error occurred."

    def test_get_combat_help_message(self, combat_validator):
        """Test combat help message generation."""
        help_message = combat_validator.get_combat_help_message()

        assert isinstance(help_message, str)
        assert len(help_message) > 0
        assert "ancient ones" in help_message.lower()
        assert "attack" in help_message.lower()
        assert "punch" in help_message.lower()

    def test_get_combat_status_message_in_combat(self, combat_validator):
        """Test combat status message for player in combat."""
        player_name = "TestPlayer"
        combat_state = {"in_combat": True, "target": "rat"}

        status_message = combat_validator.get_combat_status_message(player_name, combat_state)

        assert isinstance(status_message, str)
        assert "TestPlayer" in status_message
        assert "combat" in status_message.lower()
        assert "rat" in status_message

    def test_get_combat_status_message_not_in_combat(self, combat_validator):
        """Test combat status message for player not in combat."""
        player_name = "TestPlayer"
        combat_state = {"in_combat": False}

        status_message = combat_validator.get_combat_status_message(player_name, combat_state)

        assert isinstance(status_message, str)
        assert "TestPlayer" in status_message
        assert "ready" in status_message.lower() or "battle" in status_message.lower()

    def test_get_combat_result_message_success_with_damage(self, combat_validator):
        """Test combat result message for successful attack with damage."""
        action = "punch"
        target = "rat"
        success = True
        damage = 5

        result_message = combat_validator.get_combat_result_message(action, target, success, damage)

        assert isinstance(result_message, str)
        assert "punch" in result_message
        assert "rat" in result_message
        assert "5" in result_message
        assert "cosmic forces" in result_message.lower()

    def test_get_combat_result_message_success_no_damage(self, combat_validator):
        """Test combat result message for successful attack with no damage."""
        action = "punch"
        target = "rat"
        success = True
        damage = 0

        result_message = combat_validator.get_combat_result_message(action, target, success, damage)

        assert isinstance(result_message, str)
        assert "punch" in result_message
        assert "rat" in result_message
        assert "ancient ones" in result_message.lower()

    def test_get_combat_result_message_failure(self, combat_validator):
        """Test combat result message for failed attack."""
        action = "punch"
        target = "rat"
        success = False
        damage = 0

        result_message = combat_validator.get_combat_result_message(action, target, success, damage)

        assert isinstance(result_message, str)
        assert "punch" in result_message
        assert "rat" in result_message
        assert "fails" in result_message.lower()
        assert "cosmic forces" in result_message.lower()

    def test_get_combat_death_message(self, combat_validator):
        """Test combat death message generation."""
        target = "rat"
        killer = "TestPlayer"

        death_message = combat_validator.get_combat_death_message(target, killer)

        assert isinstance(death_message, str)
        assert "rat" in death_message
        assert "TestPlayer" in death_message
        assert "assault" in death_message.lower() or "blow" in death_message.lower()

    def test_get_combat_victory_message(self, combat_validator):
        """Test combat victory message generation."""
        player_name = "TestPlayer"
        target = "rat"
        xp_gained = 10

        victory_message = combat_validator.get_combat_victory_message(player_name, target, xp_gained)

        assert isinstance(victory_message, str)
        assert "TestPlayer" in victory_message
        assert "rat" in victory_message
        assert "10" in victory_message
        assert "experience" in victory_message.lower()
