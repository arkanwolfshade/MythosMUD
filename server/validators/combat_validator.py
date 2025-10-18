"""
Combat command validation with thematic error messages.

This module provides enhanced validation for combat commands with
Cthulhu Mythos-themed error messages that maintain the atmosphere
while providing clear feedback to players.
"""

import re
from typing import Any

from server.logging_config import get_logger

logger = get_logger(__name__)


class CombatValidator:
    """
    Enhanced combat command validator with thematic error messages.

    Provides comprehensive validation for combat commands while maintaining
    the Cthulhu Mythos atmosphere through carefully crafted error messages.
    """

    def __init__(self):
        """Initialize the combat validator."""
        self.attack_aliases = {
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

        # Thematic error messages for different validation failures
        self.error_messages = {
            "invalid_command": [
                "The ancient ones whisper that such an action is beyond mortal comprehension.",
                "Your mind recoils at the thought of such an impossible action.",
                "The cosmic forces reject your feeble attempt at violence.",
                "Such actions are forbidden by the laws that govern reality itself.",
            ],
            "no_target": [
                "You must focus your wrath upon a specific target, lest your fury be wasted.",
                "The void stares back at you, demanding a name to direct your hatred.",
                "Your anger needs direction - who shall bear the brunt of your assault?",
                "The cosmic forces require a target for your destructive intent.",
            ],
            "target_not_found": [
                "Your eyes strain against the darkness, but {target} is not here.",
                "The shadows mock your search for {target} - they are not present.",
                "Your senses fail to detect {target} in this accursed place.",
                "The very air seems to laugh at your futile search for {target}.",
            ],
            "target_dead": [
                "{target} lies still, their life force already extinguished by forces beyond your understanding.",
                "The corpse of {target} offers no resistance to your assault.",
                "Your target has already been claimed by the great beyond.",
                "The lifeless form of {target} cannot be harmed further.",
            ],
            "already_in_combat": [
                "You are already engaged in a battle that would make the gods themselves tremble.",
                "Your focus is consumed by the ongoing struggle against cosmic forces.",
                "The battle rages on, and you cannot divide your attention.",
                "Your current conflict demands all your concentration.",
            ],
            "not_in_combat": [
                "The peace of this place is not to be disturbed by mortal violence.",
                "The cosmic forces have not aligned for combat in this sacred space.",
                "Your violent intent is repelled by the protective energies of this location.",
                "The ancient ones have decreed this place free from mortal conflict.",
            ],
            "invalid_target": [
                "Your target is beyond the reach of mortal violence.",
                "The cosmic forces protect {target} from your assault.",
                "Your attack glances harmlessly off {target}'s otherworldly defenses.",
                "The very fabric of reality bends to protect {target} from your wrath.",
            ],
            "insufficient_strength": [
                "Your mortal form lacks the strength to harm such a being.",
                "The cosmic forces laugh at your feeble attempt to cause harm.",
                "Your attack is but a whisper against the roar of cosmic power.",
                "The ancient ones mock your puny efforts at violence.",
            ],
            "target_immune": [
                "{target} is protected by forces beyond mortal comprehension.",
                "Your attack passes through {target} as if they were made of shadow.",
                "The cosmic energies surrounding {target} absorb your assault harmlessly.",
                "Your violence is meaningless against {target}'s otherworldly nature.",
            ],
            "rate_limited": [
                "The cosmic forces demand you pause before unleashing more violence.",
                "Your mortal form needs a moment to recover from the exertion.",
                "The ancient ones decree that you must wait before striking again.",
                "The very air itself resists your rapid succession of attacks.",
            ],
            "invalid_weapon": [
                "Your weapon is not suited for combat against such beings.",
                "The cosmic forces reject your choice of weapon for this battle.",
                "Your implement of violence is inadequate for the task at hand.",
                "The ancient ones frown upon your choice of weapon.",
            ],
            "spell_interference": [
                "The arcane energies swirling about interfere with your combat abilities.",
                "Mystical forces disrupt your attempts at physical violence.",
                "The cosmic energies in this place make combat unpredictable.",
                "The ancient magics here interfere with your violent intent.",
            ],
        }

    def validate_combat_command(
        self, command_data: dict[str, Any], player_context: dict[str, Any]
    ) -> tuple[bool, str | None, str | None]:
        """
        Validate a combat command with thematic error messages.

        Args:
            command_data: The command data to validate
            player_context: Player context information

        Returns:
            Tuple of (is_valid, error_message, warning_message)
        """
        try:
            # Extract command information
            command = command_data.get("command_type", "").lower()
            args = command_data.get("args", [])
            target_name = args[0] if args else None

            # Validate command type
            if command not in self.attack_aliases:
                error_msg = self._get_random_error_message("invalid_command")
                return False, error_msg, None

            # Validate target
            if not target_name:
                error_msg = self._get_random_error_message("no_target")
                return False, error_msg, None

            # Validate target name format
            if not self._is_valid_target_name(target_name):
                error_msg = self._get_random_error_message("invalid_target").format(target=target_name)
                return False, error_msg, None

            # Check for suspicious patterns
            if self._contains_suspicious_patterns(target_name):
                error_msg = self._get_random_error_message("invalid_target").format(target=target_name)
                return False, error_msg, "The cosmic forces detect something amiss with your target."

            # Validate command length
            if len(target_name) > 50:
                error_msg = self._get_random_error_message("invalid_target").format(target=target_name)
                return False, error_msg, "Your target's name is too long for mortal comprehension."

            # Check for rate limiting
            if self._is_rate_limited(player_context):
                error_msg = self._get_random_error_message("rate_limited")
                return False, error_msg, None

            # All validations passed
            return True, None, None

        except Exception as e:
            logger.error(f"Error in combat command validation: {e}")
            return False, "The cosmic forces have rejected your command.", None

    def validate_target_exists(self, target_name: str, available_targets: list[str]) -> tuple[bool, str | None]:
        """
        Validate that a target exists with thematic error messages.

        Args:
            target_name: Name of the target to find
            available_targets: List of available targets

        Returns:
            Tuple of (target_exists, error_message)
        """
        if not target_name:
            error_msg = self._get_random_error_message("no_target")
            return False, error_msg

        # Check for exact match
        for target in available_targets:
            if target.lower() == target_name.lower():
                return True, None

        # Check for partial match
        partial_matches = [target for target in available_targets if target_name.lower() in target.lower()]

        if partial_matches:
            # Suggest the closest match
            closest_match = min(partial_matches, key=len)
            error_msg = f"You don't see {target_name} here. Did you mean {closest_match}?"
            return False, error_msg

        # No matches found
        error_msg = self._get_random_error_message("target_not_found").format(target=target_name)
        return False, error_msg

    def validate_target_alive(self, target_name: str, is_alive: bool) -> tuple[bool, str | None]:
        """
        Validate that a target is alive with thematic error messages.

        Args:
            target_name: Name of the target
            is_alive: Whether the target is alive

        Returns:
            Tuple of (is_alive, error_message)
        """
        if is_alive:
            return True, None

        error_msg = self._get_random_error_message("target_dead").format(target=target_name)
        return False, error_msg

    def validate_combat_state(self, is_in_combat: bool, required_state: bool) -> tuple[bool, str | None]:
        """
        Validate combat state with thematic error messages.

        Args:
            is_in_combat: Whether player is currently in combat
            required_state: Whether combat is required for this action

        Returns:
            Tuple of (state_valid, error_message)
        """
        if is_in_combat == required_state:
            return True, None

        if required_state and not is_in_combat:
            error_msg = self._get_random_error_message("not_in_combat")
            return False, error_msg

        if not required_state and is_in_combat:
            error_msg = self._get_random_error_message("already_in_combat")
            return False, error_msg

        return True, None

    def validate_attack_strength(
        self, player_level: int, target_level: int, weapon_power: int = 1
    ) -> tuple[bool, str | None, str | None]:
        """
        Validate attack strength with thematic error messages.

        Args:
            player_level: Player's level
            target_level: Target's level
            weapon_power: Weapon power modifier

        Returns:
            Tuple of (can_attack, error_message, warning_message)
        """
        level_difference = target_level - player_level

        # Check if target is too strong
        if level_difference > 10:
            error_msg = self._get_random_error_message("insufficient_strength")
            return False, error_msg, None

        # Check if target is significantly stronger
        if level_difference > 5:
            warning_msg = "The cosmic forces warn you that this target is beyond your current power."
            return True, None, warning_msg

        # Check if weapon is too weak
        if weapon_power < 1:
            error_msg = self._get_random_error_message("invalid_weapon")
            return False, error_msg, None

        return True, None, None

    def _is_valid_target_name(self, target_name: str) -> bool:
        """Check if target name is valid."""
        if not target_name or not isinstance(target_name, str):
            return False

        # Check for basic format
        if not re.match(r"^[a-zA-Z0-9\s\-_\']+$", target_name):
            return False

        # Check length
        if len(target_name.strip()) < 1 or len(target_name) > 50:
            return False

        return True

    def _contains_suspicious_patterns(self, target_name: str) -> bool:
        """Check for suspicious patterns in target name."""
        suspicious_patterns = [
            r'[<>"\']',  # HTML/script injection
            r"[;|&]",  # Command injection
            r"\.\./",  # Path traversal
            r"javascript:",  # XSS
            r"data:",  # Data URLs
        ]

        for pattern in suspicious_patterns:
            if re.search(pattern, target_name, re.IGNORECASE):
                return True

        return False

    def _is_rate_limited(self, player_context: dict[str, Any]) -> bool:
        """Check if player is rate limited."""
        # This would integrate with actual rate limiting system
        # For now, return False (no rate limiting)
        return False

    def _get_random_error_message(self, error_type: str) -> str:
        """Get a random error message for the given error type."""
        import random

        messages = self.error_messages.get(error_type, ["An error occurred."])
        return random.choice(messages)

    def get_combat_help_message(self) -> str:
        """Get a thematic help message for combat commands."""
        return """
The ancient ones have granted you the power of violence. You may use these commands:

• attack <target> - Strike your target with all your might
• punch <target> - Deliver a quick, sharp blow
• kick <target> - Lash out with your feet
• strike <target> - A precise, focused attack
• hit <target> - A simple, direct assault
• smack <target> - A sharp, stinging blow
• thump <target> - A heavy, thudding attack

The cosmic forces will guide your hand in battle, but choose your targets wisely.
        """.strip()

    def get_combat_status_message(self, player_name: str, combat_state: dict[str, Any]) -> str:
        """Get a thematic combat status message."""
        if combat_state.get("in_combat", False):
            return f"{player_name} is locked in mortal combat with {combat_state.get('target', 'unknown')}."
        else:
            return f"{player_name} stands ready for battle, their eyes scanning for threats."

    def get_combat_result_message(self, action: str, target: str, success: bool, damage: int = 0) -> str:
        """Get a thematic combat result message."""
        if success:
            if damage > 0:
                return f"You {action} {target} for {damage} damage! The cosmic forces favor your assault."
            else:
                return f"You {action} {target}! The ancient ones watch your battle with interest."
        else:
            return f"Your {action} against {target} fails! The cosmic forces mock your feeble attempt."

    def get_combat_death_message(self, target: str, killer: str) -> str:
        """Get a thematic death message."""
        death_messages = [
            f"{target} falls to {killer}'s assault, their life force extinguished by cosmic violence.",
            f"The ancient ones claim {target} as {killer} delivers the final blow.",
            f"{target} is consumed by the void as {killer}'s attack finds its mark.",
            f"The cosmic forces claim {target} as {killer} proves their dominance.",
        ]

        import random

        return random.choice(death_messages)

    def get_combat_victory_message(self, player_name: str, target: str, xp_gained: int) -> str:
        """Get a thematic victory message."""
        victory_messages = [
            f"{player_name} has vanquished {target}! The cosmic forces grant you {xp_gained} experience.",
            f"Victory! {player_name} has defeated {target} and gained {xp_gained} experience.",
            f"The ancient ones smile upon {player_name} as they defeat {target} and gain {xp_gained} experience.",
            f"{player_name} emerges victorious over {target}, earning {xp_gained} experience from the cosmic forces.",
        ]

        import random

        return random.choice(victory_messages)
