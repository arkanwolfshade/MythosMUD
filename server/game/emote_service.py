"""
Emote Service for handling predefined emote actions and their messages.

This service manages a collection of predefined emotes that players can use
with simple commands like 'twibble' or 'dance', automatically expanding them
to appropriate messages for both the player and room occupants.
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class EmoteService:
    """Service for managing predefined emote actions and their messages."""

    def __init__(self, emote_file_path: str | None = None):
        """
        Initialize the EmoteService.

        Args:
            emote_file_path: Path to the emote definitions JSON file.
                            Defaults to 'data/emotes.json' relative to project root.
        """
        if emote_file_path is None:
            # Default to data/emotes.json relative to project root
            project_root = Path(__file__).parent.parent.parent
            emote_file_path = project_root / "data" / "emotes.json"

        self.emote_file_path = Path(emote_file_path)
        self.emotes: dict[str, dict] = {}
        self.alias_to_emote: dict[str, str] = {}

        self._load_emotes()

    def _load_emotes(self) -> None:
        """Load emote definitions from the JSON file."""
        try:
            if not self.emote_file_path.exists():
                logger.warning(f"Emote file not found: {self.emote_file_path}")
                return

            with open(self.emote_file_path, encoding="utf-8") as f:
                data = json.load(f)

            self.emotes = data.get("emotes", {})

            # Build alias mapping
            self.alias_to_emote = {}
            for emote_name, emote_data in self.emotes.items():
                # The emote name itself is also an alias
                self.alias_to_emote[emote_name] = emote_name

                # Add explicit aliases
                aliases = emote_data.get("aliases", [])
                for alias in aliases:
                    if alias in self.alias_to_emote:
                        logger.warning(f"Duplicate emote alias: {alias} (already maps to {self.alias_to_emote[alias]})")
                    else:
                        self.alias_to_emote[alias] = emote_name

            logger.info(f"Loaded {len(self.emotes)} emotes with {len(self.alias_to_emote)} total aliases")

        except Exception as e:
            logger.error(f"Failed to load emotes from {self.emote_file_path}: {e}")
            self.emotes = {}
            self.alias_to_emote = {}

    def is_emote_alias(self, command: str) -> bool:
        """
        Check if a command is an emote alias.

        Args:
            command: The command to check

        Returns:
            True if the command is an emote alias, False otherwise
        """
        return command.lower() in self.alias_to_emote

    def get_emote_definition(self, command: str) -> dict | None:
        """
        Get the emote definition for a command.

        Args:
            command: The command (emote name or alias)

        Returns:
            Emote definition dict or None if not found
        """
        emote_name = self.alias_to_emote.get(command.lower())
        if emote_name:
            return self.emotes.get(emote_name)
        return None

    def format_emote_messages(self, command: str, player_name: str) -> tuple[str, str]:
        """
        Format emote messages for the player and room occupants.

        Args:
            command: The emote command (e.g., 'twibble')
            player_name: Name of the player performing the emote

        Returns:
            Tuple of (self_message, other_message)

        Raises:
            ValueError: If the command is not a valid emote
        """
        emote_def = self.get_emote_definition(command)
        if not emote_def:
            raise ValueError(f"Unknown emote: {command}")

        self_message = emote_def["self_message"]
        other_message = emote_def["other_message"].format(player_name=player_name)

        return self_message, other_message

    def list_available_emotes(self) -> dict[str, list]:
        """
        Get a list of all available emotes and their aliases.

        Returns:
            Dict mapping emote names to their aliases
        """
        result = {}
        for emote_name, emote_data in self.emotes.items():
            aliases = [emote_name] + emote_data.get("aliases", [])
            result[emote_name] = aliases
        return result

    def reload_emotes(self) -> None:
        """Reload emote definitions from the file."""
        logger.info("Reloading emote definitions")
        self._load_emotes()
