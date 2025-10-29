"""
Player Preferences Service for Advanced Chat Channels.

This module provides functionality for managing player channel preferences
including default channel settings and channel muting preferences.
"""

import json
import sqlite3
import threading
from typing import Any

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PlayerPreferencesService:
    """
    Service for managing player channel preferences.

    This service handles:
    - Player default channel preferences
    - Channel muting preferences (stored in database, not JSON files)
    - Preference persistence across sessions
    """

    def __init__(self, db_path: str):
        """
        Initialize the PlayerPreferencesService.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self._lock = threading.Lock()

        # Valid channel names
        self._valid_channels = {"local", "global", "whisper", "system"}

        # Initialize the database table
        self._init_database()

        logger.info("PlayerPreferencesService initialized", db_path=db_path)

    def _init_database(self):
        """Initialize the player_channel_preferences table."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Create the table if it doesn't exist
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS player_channel_preferences (
                        player_id TEXT PRIMARY KEY NOT NULL,
                        default_channel TEXT NOT NULL DEFAULT 'local',
                        muted_channels TEXT NOT NULL DEFAULT '[]',
                        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
                    )
                """)

                # Create indexes
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_player_channel_preferences_player_id
                    ON player_channel_preferences(player_id)
                """)
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_player_channel_preferences_default_channel
                    ON player_channel_preferences(default_channel)
                """)

                # Create trigger for updated_at
                conn.execute("""
                    CREATE TRIGGER IF NOT EXISTS update_player_channel_preferences_updated_at
                    AFTER UPDATE ON player_channel_preferences
                    FOR EACH ROW
                    BEGIN
                        UPDATE player_channel_preferences
                        SET updated_at = CURRENT_TIMESTAMP
                        WHERE player_id = NEW.player_id;
                    END
                """)

                conn.commit()

        except Exception as e:
            logger.error("Failed to initialize player_channel_preferences table", error=str(e))
            raise

    def create_player_preferences(self, player_id: str) -> dict[str, Any]:
        """
        Create default preferences for a new player.

        Args:
            player_id: The player's unique identifier

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                # Check if preferences already exist
                cursor = conn.execute(
                    "SELECT player_id FROM player_channel_preferences WHERE player_id = ?", (player_id,)
                )
                if cursor.fetchone():
                    return {"success": False, "error": "Player preferences already exist"}

                # Insert default preferences
                conn.execute(
                    """
                    INSERT INTO player_channel_preferences
                    (player_id, default_channel, muted_channels, created_at, updated_at)
                    VALUES (?, 'local', '[]', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """,
                    (player_id,),
                )

                conn.commit()

                logger.info("Created player preferences", player_id=player_id)
                return {"success": True}

        except Exception as e:
            logger.error("Failed to create player preferences", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}

    def get_player_preferences(self, player_id: str) -> dict[str, Any]:
        """
        Get preferences for a player.

        Args:
            player_id: The player's unique identifier

        Returns:
            Dictionary with success status and preferences data or error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.execute(
                    """
                    SELECT player_id, default_channel, muted_channels, created_at, updated_at
                    FROM player_channel_preferences
                    WHERE player_id = ?
                """,
                    (player_id,),
                )

                row = cursor.fetchone()
                if not row:
                    return {"success": False, "error": "Player preferences not found"}

                # Convert row to dictionary
                preferences = {
                    "player_id": row["player_id"],
                    "default_channel": row["default_channel"],
                    "muted_channels": row["muted_channels"],
                    "created_at": row["created_at"],
                    "updated_at": row["updated_at"],
                }

                return {"success": True, "data": preferences}

        except Exception as e:
            logger.error("Failed to get player preferences", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}

    def update_default_channel(self, player_id: str, channel: str) -> dict[str, Any]:
        """
        Update a player's default channel.

        Args:
            player_id: The player's unique identifier
            channel: The new default channel name

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        if not self._is_valid_channel(channel):
            return {"success": False, "error": "Invalid channel name"}

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                # Check if player preferences exist
                cursor = conn.execute(
                    "SELECT player_id FROM player_channel_preferences WHERE player_id = ?", (player_id,)
                )
                if not cursor.fetchone():
                    return {"success": False, "error": "Player preferences not found"}

                # Update default channel
                conn.execute(
                    """
                    UPDATE player_channel_preferences
                    SET default_channel = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE player_id = ?
                """,
                    (channel, player_id),
                )

                conn.commit()

                logger.info("Updated default channel", player_id=player_id, channel=channel)
                return {"success": True}

        except Exception as e:
            logger.error("Failed to update default channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}

    def mute_channel(self, player_id: str, channel: str) -> dict[str, Any]:
        """
        Mute a channel for a player.

        Args:
            player_id: The player's unique identifier
            channel: The channel to mute

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        if not self._is_valid_channel(channel):
            return {"success": False, "error": "Invalid channel name"}

        # System channel cannot be muted
        if channel == "system":
            return {"success": False, "error": "System channel cannot be muted"}

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                # Get current muted channels
                cursor = conn.execute(
                    "SELECT muted_channels FROM player_channel_preferences WHERE player_id = ?", (player_id,)
                )
                row = cursor.fetchone()
                if not row:
                    return {"success": False, "error": "Player preferences not found"}

                # Parse current muted channels
                muted_channels = json.loads(row[0])

                # Add channel if not already muted
                if channel not in muted_channels:
                    muted_channels.append(channel)

                    # Update database
                    conn.execute(
                        """
                        UPDATE player_channel_preferences
                        SET muted_channels = ?, updated_at = CURRENT_TIMESTAMP
                        WHERE player_id = ?
                    """,
                        (json.dumps(muted_channels), player_id),
                    )

                    conn.commit()

                    logger.info("Muted channel for player", player_id=player_id, channel=channel)

                return {"success": True}

        except Exception as e:
            logger.error("Failed to mute channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}

    def unmute_channel(self, player_id: str, channel: str) -> dict[str, Any]:
        """
        Unmute a channel for a player.

        Args:
            player_id: The player's unique identifier
            channel: The channel to unmute

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        if not self._is_valid_channel(channel):
            return {"success": False, "error": "Invalid channel name"}

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                # Get current muted channels
                cursor = conn.execute(
                    "SELECT muted_channels FROM player_channel_preferences WHERE player_id = ?", (player_id,)
                )
                row = cursor.fetchone()
                if not row:
                    return {"success": False, "error": "Player preferences not found"}

                # Parse current muted channels
                muted_channels = json.loads(row[0])

                # Remove channel if muted
                if channel in muted_channels:
                    muted_channels.remove(channel)

                    # Update database
                    conn.execute(
                        """
                        UPDATE player_channel_preferences
                        SET muted_channels = ?, updated_at = CURRENT_TIMESTAMP
                        WHERE player_id = ?
                    """,
                        (json.dumps(muted_channels), player_id),
                    )

                    conn.commit()

                    logger.info("Unmuted channel for player", player_id=player_id, channel=channel)

                return {"success": True}

        except Exception as e:
            logger.error("Failed to unmute channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}

    def get_muted_channels(self, player_id: str) -> dict[str, Any]:
        """
        Get list of muted channels for a player.

        Args:
            player_id: The player's unique identifier

        Returns:
            Dictionary with success status and list of muted channels or error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    "SELECT muted_channels FROM player_channel_preferences WHERE player_id = ?", (player_id,)
                )
                row = cursor.fetchone()
                if not row:
                    return {"success": False, "error": "Player preferences not found"}

                muted_channels = json.loads(row[0])
                return {"success": True, "data": muted_channels}

        except Exception as e:
            logger.error("Failed to get muted channels", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}

    def is_channel_muted(self, player_id: str, channel: str) -> dict[str, Any]:
        """
        Check if a specific channel is muted for a player.

        Args:
            player_id: The player's unique identifier
            channel: The channel to check

        Returns:
            Dictionary with success status and boolean result or error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        if not self._is_valid_channel(channel):
            return {"success": False, "error": "Invalid channel name"}

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    "SELECT muted_channels FROM player_channel_preferences WHERE player_id = ?", (player_id,)
                )
                row = cursor.fetchone()
                if not row:
                    return {"success": False, "error": "Player preferences not found"}

                muted_channels = json.loads(row[0])
                is_muted = channel in muted_channels

                return {"success": True, "data": is_muted}

        except Exception as e:
            logger.error("Failed to check channel mute status", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}

    def delete_player_preferences(self, player_id: str) -> dict[str, Any]:
        """
        Delete preferences for a player.

        Args:
            player_id: The player's unique identifier

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("DELETE FROM player_channel_preferences WHERE player_id = ?", (player_id,))

                if cursor.rowcount == 0:
                    return {"success": False, "error": "Player preferences not found"}

                conn.commit()

                logger.info("Deleted player preferences", player_id=player_id)
                return {"success": True}

        except Exception as e:
            logger.error("Failed to delete player preferences", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}

    def _is_valid_player_id(self, player_id: str) -> bool:
        """
        Validate player ID.

        Args:
            player_id: The player ID to validate

        Returns:
            True if valid, False otherwise
        """
        if not player_id or not isinstance(player_id, str):
            return False

        if len(player_id) > 255:  # Reasonable limit
            return False

        return True

    def _is_valid_channel(self, channel: str) -> bool:
        """
        Validate channel name.

        Args:
            channel: The channel name to validate

        Returns:
            True if valid, False otherwise
        """
        if not channel or not isinstance(channel, str):
            return False

        return channel in self._valid_channels

    def _is_valid_json_array(self, json_str: str) -> bool:
        """
        Validate that a string is a valid JSON array.

        Args:
            json_str: The JSON string to validate

        Returns:
            True if valid JSON array, False otherwise
        """
        if not json_str or not isinstance(json_str, str):
            return False

        try:
            parsed = json.loads(json_str)
            return isinstance(parsed, list)
        except (json.JSONDecodeError, TypeError):
            return False
