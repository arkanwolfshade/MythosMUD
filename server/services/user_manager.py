"""
User management service for MythosMUD chat system.

This module provides comprehensive user management including muting,
permissions, and user state tracking for the chat system.
"""

import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from .chat_logger import chat_logger

logger = get_logger("communications.user_manager")


class UserManager:
    """
    Comprehensive user management for chat system.

    Handles player muting, channel muting, permissions, and user state
    tracking with integration to AI logging systems.
    """

    def __init__(self, data_dir: Path | None = None):
        """Initialize the user manager."""
        # Player mute storage: {player_id: {target_type: {target_id: mute_info}}}
        self._player_mutes: dict[str, dict[str, dict[str, Any]]] = {}  # player_id -> {target_type -> {target_id -> mute_info}}

        # Channel mute storage: {player_id: {channel: mute_info}}
        self._channel_mutes: dict[str, dict[str, Any]] = {}  # player_id -> {channel -> mute_info}

        # Global mute storage: {player_id: mute_info}
        self._global_mutes: dict[str, Any] = {}  # player_id -> mute_info

        # Admin players (immune to mutes)
        self._admin_players: set[str] = set()

        # Chat logger for AI processing
        self.chat_logger = chat_logger

        # Data directory for player-specific mute files
        self.data_dir = data_dir or Path("data/user_management")
        self.data_dir.mkdir(parents=True, exist_ok=True)

        logger.info("UserManager initialized with JSON file persistence")

    def add_admin(self, player_id: str, player_name: str = None):
        """
        Add a player as an admin.

        Args:
            player_id: Player ID
            player_name: Player name for logging
        """
        try:
            # Update database
            from ..persistence import get_persistence

            persistence = get_persistence()

            # Get player from database
            player = persistence.get_player(player_id)
            if player:
                player.set_admin_status(True)
                persistence.save_player(player)
                logger.info("Player added as admin in database", player_id=player_id, player_name=player_name)
            else:
                logger.error("Player not found in database")
                return False

            # Update in-memory cache
            self._admin_players.add(player_id)

            return True
        except OSError as e:
            logger.error("File system error adding admin status", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError) as e:
            logger.error("Data validation error adding admin status", error=str(e), error_type=type(e).__name__)
            return False
        except Exception as e:
            logger.error("Unexpected error adding admin status", error=str(e), error_type=type(e).__name__)
            return False

    def remove_admin(self, player_id: str, player_name: str = None):
        """
        Remove a player's admin status.

        Args:
            player_id: Player ID
            player_name: Player name for logging
        """
        try:
            # Update database
            from ..persistence import get_persistence

            persistence = get_persistence()

            # Get player from database
            player = persistence.get_player(player_id)
            if player:
                player.set_admin_status(False)
                persistence.save_player(player)
                logger.info(
                    "Player admin status removed from database",
                    player_id=player_id,
                    player_name=player_name,
                )
            else:
                logger.error("Player not found in database")
                return False

            # Update in-memory cache
            if player_id in self._admin_players:
                self._admin_players.remove(player_id)

            return True
        except OSError as e:
            logger.error("File system error removing admin status", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError) as e:
            logger.error("Data validation error removing admin status", error=str(e), error_type=type(e).__name__)
            return False
        except Exception as e:
            logger.error("Unexpected error removing admin status", error=str(e), error_type=type(e).__name__)
            return False

    def is_admin(self, player_id: str) -> bool:
        """
        Check if a player is an admin.

        Args:
            player_id: Player ID

        Returns:
            True if player is admin
        """
        # Check in-memory cache first
        if player_id in self._admin_players:
            return True

        # Check database if not in cache
        try:
            from ..persistence import get_persistence

            persistence = get_persistence()

            player = persistence.get_player(player_id)
            if player and player.is_admin_user():
                # Add to cache
                self._admin_players.add(player_id)
                return True
        except OSError as e:
            logger.error(
                "File system error checking admin status in database", error=str(e), error_type=type(e).__name__
            )
        except (ValueError, TypeError) as e:
            logger.error(
                "Data validation error checking admin status in database", error=str(e), error_type=type(e).__name__
            )
        except Exception as e:
            logger.error(
                "Unexpected error checking admin status in database", error=str(e), error_type=type(e).__name__
            )

        return False

    def mute_player(
        self,
        muter_id: str,
        muter_name: str,
        target_id: str,
        target_name: str,
        duration_minutes: int | None = None,
        reason: str = "",
    ) -> bool:
        """
        Mute a specific player for another player.

        Args:
            muter_id: ID of player applying the mute
            muter_name: Name of player applying the mute
            target_id: ID of player being muted
            target_name: Name of player being muted
            duration_minutes: Duration in minutes (None for permanent)
            reason: Reason for mute

        Returns:
            True if mute was applied successfully
        """
        try:
            # Check if target is admin (immune to mutes)
            if self.is_admin(target_id):
                logger.warning("Attempted to mute admin player")
                return False

            # Initialize player mutes if needed
            if muter_id not in self._player_mutes:
                self._player_mutes[muter_id] = {}

            # Calculate mute expiry
            expiry_time = None
            if duration_minutes:
                expiry_time = datetime.now(UTC) + timedelta(minutes=duration_minutes)

            # Store mute information
            mute_info = {
                "target_id": target_id,
                "target_name": target_name,
                "muted_by": muter_id,
                "muted_by_name": muter_name,
                "muted_at": datetime.now(UTC),
                "expires_at": expiry_time,
                "reason": reason,
                "is_permanent": duration_minutes is None,
            }

            self._player_mutes[muter_id][target_id] = mute_info

            # Log the mute for AI processing
            self.chat_logger.log_player_muted(
                muter_id=muter_id,
                target_id=target_id,
                target_name=target_name,
                mute_type="player",
                duration_minutes=duration_minutes,
                reason=reason,
            )

            logger.info(
                "Player muted another player",
                muter_id=muter_id,
                muter_name=muter_name,
                target_id=target_id,
                target_name=target_name,
                duration_minutes=duration_minutes,
                reason=reason,
            )

            # Save mute data for both players
            self.save_player_mutes(muter_id)
            self.save_player_mutes(target_id)

            return True

        except OSError as e:
            logger.error("File system error muting player", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError) as e:
            logger.error("Data validation error muting player", error=str(e), error_type=type(e).__name__)
            return False
        except Exception as e:
            logger.error("Unexpected error muting player", error=str(e), error_type=type(e).__name__)
            return False

    def unmute_player(self, unmuter_id: str, unmuter_name: str, target_id: str, target_name: str) -> bool:
        """
        Unmute a specific player.

        Args:
            unmuter_id: ID of player removing the mute
            unmuter_name: Name of player removing the mute
            target_id: ID of player being unmuted
            target_name: Name of player being unmuted

        Returns:
            True if unmute was successful
        """
        try:
            # Load unmuter's mute data to ensure it's available
            self.load_player_mutes(unmuter_id)

            # Debug logging
            logger.debug("Unmute debug - unmuter_id", unmuter_id=unmuter_id, unmuter_id_type=type(unmuter_id))
            logger.debug("Unmute debug - target_id", target_id=target_id, target_id_type=type(target_id))
            logger.debug("Unmute debug - player_mutes_keys", player_mutes_keys=list(self._player_mutes.keys()))
            logger.debug(
                "Unmute debug - unmuter_mutes keys",
                unmuter_mutes_keys=list(self._player_mutes.get(unmuter_id, {}).keys()),
            )
            logger.debug(
                "Unmute debug - target_id in unmuter_mutes",
                target_id_in_unmuter_mutes=target_id in self._player_mutes.get(unmuter_id, {}),
            )

            # Check if mute exists (convert target_id to string for comparison)
            target_id_str = str(target_id)
            if unmuter_id in self._player_mutes and target_id_str in self._player_mutes[unmuter_id]:
                # Remove the mute
                del self._player_mutes[unmuter_id][target_id_str]

                # Clean up empty player mute entries
                if not self._player_mutes[unmuter_id]:
                    del self._player_mutes[unmuter_id]

                # Log the unmute for AI processing
                self.chat_logger.log_player_unmuted(
                    unmuter_id=unmuter_id, target_id=target_id, target_name=target_name, mute_type="player"
                )

                logger.info(
                    "Player unmuted another player",
                    unmuter_id=unmuter_id,
                    unmuter_name=unmuter_name,
                    target_id=target_id,
                    target_name=target_name,
                )

                # Save mute data for both players
                self.save_player_mutes(unmuter_id)
                self.save_player_mutes(target_id)

                return True
            else:
                logger.warning("Attempted to unmute non-muted player", unmuter_id=unmuter_id, target_id=target_id)
                return False

        except Exception as e:
            logger.error("Error unmuting player", error=str(e), unmuter_id=unmuter_id, target_id=target_id)
            return False

    def mute_channel(
        self, player_id: str, player_name: str, channel: str, duration_minutes: int | None = None, reason: str = ""
    ) -> bool:
        """
        Mute a specific channel for a player.

        Args:
            player_id: Player ID
            player_name: Player name
            channel: Channel to mute
            duration_minutes: Duration in minutes (None for permanent)
            reason: Reason for mute

        Returns:
            True if mute was applied successfully
        """
        try:
            # Initialize channel mutes if needed
            if player_id not in self._channel_mutes:
                self._channel_mutes[player_id] = {}

            # Calculate mute expiry
            expiry_time = None
            if duration_minutes:
                expiry_time = datetime.now(UTC) + timedelta(minutes=duration_minutes)

            # Store mute information
            mute_info = {
                "channel": channel,
                "muted_at": datetime.now(UTC),
                "expires_at": expiry_time,
                "reason": reason,
                "is_permanent": duration_minutes is None,
            }

            self._channel_mutes[player_id][channel] = mute_info

            # Log the mute for AI processing
            self.chat_logger.log_player_muted(
                muter_id=player_id,
                target_id=player_id,
                target_name=player_name,
                mute_type=f"channel_{channel}",
                duration_minutes=duration_minutes,
                reason=reason,
            )

            logger.info(
                "Player muted channel",
                player_id=player_id,
                player_name=player_name,
                channel=channel,
                duration_minutes=duration_minutes,
                reason=reason,
            )

            # Save mute data for the player
            self.save_player_mutes(player_id)

            return True

        except OSError as e:
            logger.error("File system error muting channel", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError) as e:
            logger.error("Data validation error muting channel", error=str(e), error_type=type(e).__name__)
            return False
        except Exception as e:
            logger.error("Unexpected error muting channel", error=str(e), error_type=type(e).__name__)
            return False

    def unmute_channel(self, player_id: str, player_name: str, channel: str) -> bool:
        """
        Unmute a specific channel for a player.

        Args:
            player_id: Player ID
            player_name: Player name
            channel: Channel to unmute

        Returns:
            True if unmute was successful
        """
        try:
            # Check if channel mute exists
            if player_id in self._channel_mutes and channel in self._channel_mutes[player_id]:
                # Remove the mute
                del self._channel_mutes[player_id][channel]

                # Clean up empty channel mute entries
                if not self._channel_mutes[player_id]:
                    del self._channel_mutes[player_id]

                # Log the unmute for AI processing
                self.chat_logger.log_player_unmuted(
                    unmuter_id=player_id, target_id=player_id, target_name=player_name, mute_type=f"channel_{channel}"
                )

                logger.info("Player unmuted channel", player_id=player_id, player_name=player_name, channel=channel)

                # Save mute data for the player
                self.save_player_mutes(player_id)

                return True
            else:
                logger.warning("Attempted to unmute non-muted channel", player_id=player_id, channel=channel)
                return False

        except Exception as e:
            logger.error("Error unmuting channel", error=str(e), player_id=player_id, channel=channel)
            return False

    def mute_global(
        self,
        muter_id: str,
        muter_name: str,
        target_id: str,
        target_name: str,
        duration_minutes: int | None = None,
        reason: str = "",
    ) -> bool:
        """
        Apply a global mute to a player (cannot use any chat channels).

        Args:
            muter_id: ID of player applying the mute
            muter_name: Name of player applying the mute
            target_id: ID of player being muted
            target_name: Name of player being muted
            duration_minutes: Duration in minutes (None for permanent)
            reason: Reason for mute

        Returns:
            True if mute was applied successfully
        """
        try:
            # Check if target is admin (immune to mutes)
            if self.is_admin(target_id):
                logger.warning("Attempted to globally mute admin player", muter_id=muter_id, target_id=target_id)
                return False

            # Calculate mute expiry
            expiry_time = None
            if duration_minutes:
                expiry_time = datetime.now(UTC) + timedelta(minutes=duration_minutes)

            # Store global mute information
            mute_info = {
                "target_id": target_id,
                "target_name": target_name,
                "muted_by": muter_id,
                "muted_by_name": muter_name,
                "muted_at": datetime.now(UTC),
                "expires_at": expiry_time,
                "reason": reason,
                "is_permanent": duration_minutes is None,
            }

            self._global_mutes[target_id] = mute_info

            # Log the global mute for AI processing
            self.chat_logger.log_player_muted(
                muter_id=muter_id,
                target_id=target_id,
                target_name=target_name,
                mute_type="global",
                duration_minutes=duration_minutes,
                reason=reason,
            )

            logger.info(
                "Player globally muted",
                muter_id=muter_id,
                muter_name=muter_name,
                target_id=target_id,
                target_name=target_name,
                duration_minutes=duration_minutes,
                reason=reason,
            )

            # Save mute data for both players
            self.save_player_mutes(muter_id)
            self.save_player_mutes(target_id)

            return True

        except Exception as e:
            logger.error("Error applying global mute", error=str(e), muter_id=muter_id, target_id=target_id)
            return False

    def unmute_global(self, unmuter_id: str, unmuter_name: str, target_id: str, target_name: str) -> bool:
        """
        Remove a global mute from a player.

        Args:
            unmuter_id: ID of player removing the mute
            unmuter_name: Name of player removing the mute
            target_id: ID of player being unmuted
            target_name: Name of player being unmuted

        Returns:
            True if unmute was successful
        """
        try:
            # Load unmuter's mute data to ensure it's available
            self.load_player_mutes(unmuter_id)

            # Check if global mute exists
            if target_id in self._global_mutes:
                # Remove the global mute
                del self._global_mutes[target_id]

                # Log the global unmute for AI processing
                self.chat_logger.log_player_unmuted(
                    unmuter_id=unmuter_id, target_id=target_id, target_name=target_name, mute_type="global"
                )

                logger.info(
                    "Player globally unmuted",
                    unmuter_id=unmuter_id,
                    unmuter_name=unmuter_name,
                    target_id=target_id,
                    target_name=target_name,
                )

                # Save mute data for both players
                self.save_player_mutes(unmuter_id)
                self.save_player_mutes(target_id)

                return True
            else:
                logger.warning(
                    "Attempted to remove non-existent global mute", unmuter_id=unmuter_id, target_id=target_id
                )
                return False

        except Exception as e:
            logger.error(
                "Error removing global mute",
                error=str(e),
                unmuter_id=unmuter_id,
                target_id=target_id,
            )
            return False

    def is_player_muted(self, player_id: str, target_id: str) -> bool:
        """
        Check if a player has muted another player.

        Args:
            player_id: Player ID
            target_id: Target player ID

        Returns:
            True if target is muted by player
        """
        try:
            # Load player's mute data to ensure it's available
            self.load_player_mutes(player_id)

            # Check if mute exists and is not expired
            if player_id in self._player_mutes and target_id in self._player_mutes[player_id]:
                mute_info = self._player_mutes[player_id][target_id]

                # Check if mute is expired
                if mute_info["expires_at"] and mute_info["expires_at"] < datetime.now(UTC):
                    # Remove expired mute
                    del self._player_mutes[player_id][target_id]
                    if not self._player_mutes[player_id]:
                        del self._player_mutes[player_id]
                    return False

                return True

            return False

        except Exception as e:
            logger.error("Error checking player mute", error=str(e), player_id=player_id, target_id=target_id)
            return False

    def is_channel_muted(self, player_id: str, channel: str) -> bool:
        """
        Check if a player has muted a specific channel.

        Args:
            player_id: Player ID
            channel: Channel name

        Returns:
            True if channel is muted by player
        """
        try:
            # Check if channel mute exists and is not expired
            if player_id in self._channel_mutes and channel in self._channel_mutes[player_id]:
                mute_info = self._channel_mutes[player_id][channel]

                # Check if mute is expired
                if mute_info["expires_at"] and mute_info["expires_at"] < datetime.now(UTC):
                    # Remove expired mute
                    del self._channel_mutes[player_id][channel]
                    if not self._channel_mutes[player_id]:
                        del self._channel_mutes[player_id]
                    return False

                return True

            return False

        except Exception as e:
            logger.error("Error checking channel mute", error=str(e), player_id=player_id, channel=channel)
            return False

    def is_globally_muted(self, player_id: str) -> bool:
        """
        Check if a player is globally muted.

        Args:
            player_id: Player ID

        Returns:
            True if player is globally muted
        """
        try:
            # Check if global mute exists and is not expired
            if player_id in self._global_mutes:
                mute_info = self._global_mutes[player_id]

                # Check if mute is expired
                if mute_info["expires_at"] and mute_info["expires_at"] < datetime.now(UTC):
                    # Remove expired mute
                    del self._global_mutes[player_id]
                    return False

                return True

            return False

        except OSError as e:
            logger.error("File system error checking global mute", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError) as e:
            logger.error("Data validation error checking global mute", error=str(e), error_type=type(e).__name__)
            return False
        except Exception as e:
            logger.error("Unexpected error checking global mute", error=str(e), error_type=type(e).__name__)
            return False

    def can_send_message(self, sender_id: str, target_id: str = None, channel: str = None) -> bool:
        """
        Check if a player can send a message.

        Args:
            sender_id: Sender player ID
            target_id: Target player ID (for whispers)
            channel: Channel name (for channel messages)

        Returns:
            True if player can send message
        """
        try:
            # Admins can always send messages
            if self.is_admin(sender_id):
                return True

            # Check global mute first
            if self.is_globally_muted(sender_id):
                return False

            # Check channel mute if applicable
            if channel and self.is_channel_muted(sender_id, channel):
                return False

            # Note: We don't check if sender has muted target_id because that should not
            # prevent the sender from sending messages. The mute filtering happens on the
            # receiving end, not the sending end.

            return True

        except Exception as e:
            logger.error("Error checking message permissions", error=str(e), sender_id=sender_id)
            return False

    def get_player_mutes(self, player_id: str) -> dict[str, Any]:
        """
        Get all mutes applied by a player.

        Args:
            player_id: Player ID

        Returns:
            Dictionary with mute information
        """
        try:
            mutes: dict[str, dict[str, Any]] = {"player_mutes": {}, "channel_mutes": {}, "global_mutes": {}}

            # Get player mutes
            if player_id in self._player_mutes:
                for target_id, mute_info in self._player_mutes[player_id].items():
                    # Check if not expired
                    if not mute_info["expires_at"] or mute_info["expires_at"] > datetime.now(UTC):
                        mutes["player_mutes"][target_id] = mute_info

            # Get channel mutes
            if player_id in self._channel_mutes:
                for channel, mute_info in self._channel_mutes[player_id].items():
                    # Check if not expired
                    if not mute_info["expires_at"] or mute_info["expires_at"] > datetime.now(UTC):
                        mutes["channel_mutes"][channel] = mute_info

            # Get global mutes applied by this player
            for target_id, mute_info in self._global_mutes.items():
                if mute_info["muted_by"] == player_id:
                    # Check if not expired
                    if not mute_info["expires_at"] or mute_info["expires_at"] > datetime.now(UTC):
                        mutes["global_mutes"][target_id] = mute_info

            return mutes

        except OSError as e:
            logger.error("File system error getting player mutes", error=str(e), error_type=type(e).__name__)
            return {"player_mutes": {}, "channel_mutes": {}, "global_mutes": {}}
        except (ValueError, TypeError) as e:
            logger.error("Data validation error getting player mutes", error=str(e), error_type=type(e).__name__)
            return {"player_mutes": {}, "channel_mutes": {}, "global_mutes": {}}
        except Exception as e:
            logger.error("Unexpected error getting player mutes", error=str(e), error_type=type(e).__name__)
            return {"player_mutes": {}, "channel_mutes": {}, "global_mutes": {}}

    def is_player_muted_by_others(self, player_id: str) -> bool:
        """
        Check if a player is globally muted by any other player.

        Args:
            player_id: Player ID to check

        Returns:
            True if player is globally muted by others
        """
        # Only check if player is in any global mutes
        # Personal mutes should not prevent the muted player from sending messages
        if player_id in self._global_mutes:
            return True

        return False

    def get_who_muted_player(self, player_id: str) -> list[tuple[str, str]]:
        """
        Get information about who muted a player.

        Args:
            player_id: Player ID to check

        Returns:
            List of tuples (muter_name, mute_type)
        """
        muted_by = []

        # Check global mutes
        if player_id in self._global_mutes:
            mute_info = self._global_mutes[player_id]
            muter_name = mute_info.get("muted_by_name", "Unknown")
            muted_by.append((muter_name, "global"))

        # Check personal mutes
        for _muter_id, mutes in self._player_mutes.items():
            if player_id in mutes:
                mute_info = mutes[player_id]
                muter_name = mute_info.get("muted_by_name", "Unknown")
                muted_by.append((muter_name, "personal"))

        return muted_by

    def get_system_stats(self) -> dict[str, Any]:
        """
        Get system-wide user management statistics.

        Returns:
            Dictionary with system statistics
        """
        try:
            # Clean up expired mutes first
            self._cleanup_expired_mutes()

            stats = {
                "total_players_with_mutes": len(self._player_mutes),
                "total_channel_mutes": sum(len(mutes) for mutes in self._channel_mutes.values()),
                "total_global_mutes": len(self._global_mutes),
                "total_admin_players": len(self._admin_players),
                "admin_players": list(self._admin_players),
            }

            return stats

        except Exception as e:
            logger.error("Error getting system stats", error=str(e))
            return {}

    def _cleanup_expired_mutes(self):
        """Clean up expired mutes from all storage."""
        try:
            current_time = datetime.now(UTC)

            # Clean up player mutes
            for player_id in list(self._player_mutes.keys()):
                for target_id in list(self._player_mutes[player_id].keys()):
                    mute_info = self._player_mutes[player_id][target_id]
                    if mute_info["expires_at"] and mute_info["expires_at"] < current_time:
                        del self._player_mutes[player_id][target_id]

                # Remove empty player entries
                if not self._player_mutes[player_id]:
                    del self._player_mutes[player_id]

            # Clean up channel mutes
            for player_id in list(self._channel_mutes.keys()):
                for channel in list(self._channel_mutes[player_id].keys()):
                    mute_info = self._channel_mutes[player_id][channel]
                    if mute_info["expires_at"] and mute_info["expires_at"] < current_time:
                        del self._channel_mutes[player_id][channel]

                # Remove empty player entries
                if not self._channel_mutes[player_id]:
                    del self._channel_mutes[player_id]

            # Clean up global mutes
            for player_id in list(self._global_mutes.keys()):
                mute_info = self._global_mutes[player_id]
                if mute_info["expires_at"] and mute_info["expires_at"] < current_time:
                    del self._global_mutes[player_id]

        except Exception as e:
            logger.error("Error cleaning up expired mutes", error=str(e))

    def _get_player_mute_file(self, player_id: str) -> Path:
        """Get the mute data file path for a specific player."""
        return self.data_dir / f"mutes_{player_id}.json"

    def load_player_mutes(self, player_id: str) -> bool:
        """
        Load mute data for a specific player from JSON file.

        Args:
            player_id: Player ID to load mutes for

        Returns:
            True if data was loaded successfully, False otherwise
        """
        try:
            mute_file = self._get_player_mute_file(player_id)

            if not mute_file.exists():
                logger.debug("No mute file found for player")
                return False

            with open(mute_file, encoding="utf-8") as f:
                data = json.load(f)

            # Load player mutes
            if "player_mutes" in data:
                self._player_mutes[player_id] = {}
                for target_id, mute_info in data["player_mutes"].items():
                    # Convert timestamp strings back to datetime objects
                    if "muted_at" in mute_info:
                        mute_info["muted_at"] = datetime.fromisoformat(mute_info["muted_at"])
                    if "expires_at" in mute_info and mute_info["expires_at"]:
                        mute_info["expires_at"] = datetime.fromisoformat(mute_info["expires_at"])
                    self._player_mutes[player_id][target_id] = mute_info

            # Load channel mutes
            if "channel_mutes" in data:
                self._channel_mutes[player_id] = {}
                for channel, mute_info in data["channel_mutes"].items():
                    # Convert timestamp strings back to datetime objects
                    if "muted_at" in mute_info:
                        mute_info["muted_at"] = datetime.fromisoformat(mute_info["muted_at"])
                    if "expires_at" in mute_info and mute_info["expires_at"]:
                        mute_info["expires_at"] = datetime.fromisoformat(mute_info["expires_at"])
                    self._channel_mutes[player_id][channel] = mute_info

            # Load global mutes applied by this player
            if "global_mutes" in data:
                for target_id, mute_info in data["global_mutes"].items():
                    # Convert timestamp strings back to datetime objects
                    if "muted_at" in mute_info:
                        mute_info["muted_at"] = datetime.fromisoformat(mute_info["muted_at"])
                    if "expires_at" in mute_info and mute_info["expires_at"]:
                        mute_info["expires_at"] = datetime.fromisoformat(mute_info["expires_at"])
                    self._global_mutes[target_id] = mute_info

            # Load admin status
            if "is_admin" in data and data["is_admin"]:
                self._admin_players.add(player_id)

            logger.info("Player mute data loaded")
            return True

        except OSError as e:
            logger.error("File system error loading player mute data", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError, json.JSONDecodeError) as e:
            logger.error("Data validation error loading player mute data", error=str(e), error_type=type(e).__name__)
            return False
        except Exception as e:
            logger.error("Unexpected error loading player mute data", error=str(e), error_type=type(e).__name__)
            return False

    def save_player_mutes(self, player_id: str) -> bool:
        """
        Save mute data for a specific player to JSON file.

        Args:
            player_id: Player ID to save mutes for

        Returns:
            True if data was saved successfully, False otherwise
        """
        try:
            mute_file = self._get_player_mute_file(player_id)

            # Prepare data for serialization
            data = {
                "player_id": player_id,
                "last_updated": datetime.now(UTC).isoformat(),
                "player_mutes": {},
                "channel_mutes": {},
                "global_mutes": {},
                "is_admin": player_id in self._admin_players,
            }

            # Save player mutes
            if player_id in self._player_mutes:
                for target_id, mute_info in self._player_mutes[player_id].items():
                    # Convert datetime objects to ISO strings for JSON serialization
                    serialized_mute = mute_info.copy()
                    if "muted_at" in serialized_mute:
                        serialized_mute["muted_at"] = serialized_mute["muted_at"].isoformat()
                    if "expires_at" in serialized_mute and serialized_mute["expires_at"]:
                        serialized_mute["expires_at"] = serialized_mute["expires_at"].isoformat()
                    # Convert UUID to string for JSON serialization
                    if "target_id" in serialized_mute:
                        serialized_mute["target_id"] = str(serialized_mute["target_id"])
                    data["player_mutes"][str(target_id)] = serialized_mute

            # Save channel mutes
            if player_id in self._channel_mutes:
                for channel, mute_info in self._channel_mutes[player_id].items():
                    # Convert datetime objects to ISO strings for JSON serialization
                    serialized_mute = mute_info.copy()
                    if "muted_at" in serialized_mute:
                        serialized_mute["muted_at"] = serialized_mute["muted_at"].isoformat()
                    if "expires_at" in serialized_mute and serialized_mute["expires_at"]:
                        serialized_mute["expires_at"] = serialized_mute["expires_at"].isoformat()
                    data["channel_mutes"][channel] = serialized_mute

            # Save global mutes applied by this player
            for target_id, mute_info in self._global_mutes.items():
                if mute_info.get("muted_by") == player_id:
                    # Convert datetime objects to ISO strings for JSON serialization
                    serialized_mute = mute_info.copy()
                    if "muted_at" in serialized_mute:
                        serialized_mute["muted_at"] = serialized_mute["muted_at"].isoformat()
                    if "expires_at" in serialized_mute and serialized_mute["expires_at"]:
                        serialized_mute["expires_at"] = serialized_mute["expires_at"].isoformat()
                    # Convert UUID to string for JSON serialization
                    if "target_id" in serialized_mute:
                        serialized_mute["target_id"] = str(serialized_mute["target_id"])
                    data["global_mutes"][str(target_id)] = serialized_mute

            # Validate data is serializable before writing
            try:
                json.dumps(data, indent=2, ensure_ascii=False)
            except (TypeError, ValueError) as e:
                logger.error("Data is not JSON serializable", error=str(e), error_type=type(e).__name__)
                return False

            # Write to file atomically to prevent corruption

            # Create a temporary file
            temp_file = mute_file.with_suffix(".tmp")
            try:
                with open(temp_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                # Atomically replace the original file
                temp_file.replace(mute_file)
            except Exception as e:
                # Clean up temp file if it exists
                if temp_file.exists():
                    temp_file.unlink()
                raise e

            logger.debug("Player mute data saved")
            return True

        except Exception as e:
            logger.error(
                "Error saving player mute data",
                error=str(e),
                player_id=player_id,
                data_keys=list(data.keys()) if "data" in locals() else None,
            )
            return False

    def cleanup_player_mutes(self, player_id: str) -> bool:
        """
        Remove mute data for a player from memory and delete their file.
        Called when a player logs out or is deleted.

        Args:
            player_id: Player ID to cleanup

        Returns:
            True if cleanup was successful, False otherwise
        """
        try:
            # Remove from memory
            if player_id in self._player_mutes:
                del self._player_mutes[player_id]

            if player_id in self._channel_mutes:
                del self._channel_mutes[player_id]

            if player_id in self._global_mutes:
                del self._global_mutes[player_id]

            if player_id in self._admin_players:
                self._admin_players.remove(player_id)

            # Delete file
            mute_file = self._get_player_mute_file(player_id)
            if mute_file.exists():
                mute_file.unlink()

            logger.info("Player mute data cleaned up")
            return True

        except OSError as e:
            logger.error("File system error cleaning up player mute data", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError) as e:
            logger.error(
                "Data validation error cleaning up player mute data", error=str(e), error_type=type(e).__name__
            )
            return False
        except Exception as e:
            logger.error("Unexpected error cleaning up player mute data", error=str(e), error_type=type(e).__name__)
            return False


def _get_proper_data_dir() -> Path:
    """
    Get the proper environment-aware data directory for user management.

    Uses LOGGING_ENVIRONMENT from Pydantic config to determine the correct
    environment subdirectory (local, unit_test, e2e_test, production).

    AI: Environment separation prevents test data pollution.
    """
    from ..config import get_config

    config = get_config()
    environment = config.logging.environment

    # Find the project root (where pyproject.toml is located)
    current_file = Path(__file__).resolve()
    project_root = current_file.parent
    while project_root.parent != project_root:
        if (project_root / "pyproject.toml").exists():
            break
        project_root = project_root.parent

    # CRITICAL: Include environment in path for data isolation
    # data/{environment}/user_management NOT data/user_management
    data_path = project_root / "data" / environment / "user_management"
    return data_path


# Global user manager instance with environment-aware path resolution
user_manager = UserManager(data_dir=_get_proper_data_dir())
