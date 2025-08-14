"""
User management service for MythosMUD chat system.

This module provides comprehensive user management including muting,
permissions, and user state tracking for the chat system.
"""

from datetime import UTC, datetime, timedelta
from typing import Any

from ..logging_config import get_logger
from .chat_logger import chat_logger

logger = get_logger("communications.user_manager")


class UserManager:
    """
    Comprehensive user management for chat system.

    Handles player muting, channel muting, permissions, and user state
    tracking with integration to AI logging systems.
    """

    def __init__(self):
        """Initialize the user manager."""
        # Player mute storage: {player_id: {target_type: {target_id: mute_info}}}
        self._player_mutes = {}  # player_id -> {target_type -> {target_id -> mute_info}}

        # Channel mute storage: {player_id: {channel: mute_info}}
        self._channel_mutes = {}  # player_id -> {channel -> mute_info}

        # Global mute storage: {player_id: mute_info}
        self._global_mutes = {}  # player_id -> mute_info

        # Admin players (immune to mutes)
        self._admin_players = set()

        # Chat logger for AI processing
        self.chat_logger = chat_logger

        logger.info("UserManager initialized")

    def add_admin(self, player_id: str, player_name: str = None):
        """
        Add a player as an admin.

        Args:
            player_id: Player ID
            player_name: Player name for logging
        """
        self._admin_players.add(player_id)
        logger.info("Player added as admin", player_id=player_id, player_name=player_name)

    def remove_admin(self, player_id: str, player_name: str = None):
        """
        Remove a player's admin status.

        Args:
            player_id: Player ID
            player_name: Player name for logging
        """
        if player_id in self._admin_players:
            self._admin_players.remove(player_id)
            logger.info("Player admin status removed", player_id=player_id, player_name=player_name)

    def is_admin(self, player_id: str) -> bool:
        """
        Check if a player is an admin.

        Args:
            player_id: Player ID

        Returns:
            True if player is admin
        """
        return player_id in self._admin_players

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
                logger.warning("Attempted to mute admin player", muter_id=muter_id, target_id=target_id)
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

            return True

        except Exception as e:
            logger.error("Error muting player", error=str(e), muter_id=muter_id, target_id=target_id)
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
            # Check if mute exists
            if unmuter_id in self._player_mutes and target_id in self._player_mutes[unmuter_id]:
                # Remove the mute
                del self._player_mutes[unmuter_id][target_id]

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

            return True

        except Exception as e:
            logger.error("Error muting channel", error=str(e), player_id=player_id, channel=channel)
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

                return True
            else:
                logger.warning(
                    "Attempted to remove non-existent global mute", unmuter_id=unmuter_id, target_id=target_id
                )
                return False

        except Exception as e:
            logger.error("Error removing global mute", error=str(e), unmuter_id=unmuter_id, target_id=target_id)
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

        except Exception as e:
            logger.error("Error checking global mute", error=str(e), player_id=player_id)
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

            # Check player mute if applicable
            if target_id and self.is_player_muted(sender_id, target_id):
                return False

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
            mutes = {"player_mutes": {}, "channel_mutes": {}, "global_mutes": {}}

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

        except Exception as e:
            logger.error("Error getting player mutes", error=str(e), player_id=player_id)
            return {"player_mutes": {}, "channel_mutes": {}, "global_mutes": {}}

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


# Global user manager instance
user_manager = UserManager()
