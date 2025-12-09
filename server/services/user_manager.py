"""
User management service for MythosMUD chat system.

This module provides comprehensive user management including muting,
permissions, and user state tracking for the chat system.
"""

import asyncio
import json
import uuid
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

    def __init__(self, data_dir: Path | None = None, mute_cache_ttl: int = 300):
        """
        Initialize the user manager.

        Args:
            data_dir: Directory for player-specific mute files
            mute_cache_ttl: Cache TTL in seconds (default: 5 minutes)
        """
        # Player mute storage: {player_id: {target_id: mute_info}}
        # Using UUID objects as keys for type safety and consistency
        self._player_mutes: dict[uuid.UUID, dict[uuid.UUID, dict[str, Any]]] = {}

        # Channel mute storage: {player_id: {channel: mute_info}}
        # Using UUID objects as keys for type safety and consistency
        self._channel_mutes: dict[uuid.UUID, dict[str, Any]] = {}

        # Global mute storage: {player_id: mute_info}
        # Using UUID objects as keys for type safety and consistency
        self._global_mutes: dict[uuid.UUID, dict[str, Any]] = {}

        # Admin players (immune to mutes)
        # Using UUID objects for type safety and consistency
        self._admin_players: set[uuid.UUID] = set()

        # Chat logger for AI processing
        self.chat_logger = chat_logger

        # Data directory for player-specific mute files
        self.data_dir = data_dir or Path("data/user_management")
        self.data_dir.mkdir(parents=True, exist_ok=True)

        # Mute data cache with TTL: {player_id: (load_time, data_loaded)}
        # Using UUID objects as keys for type safety and consistency
        self._mute_cache: dict[uuid.UUID, tuple[datetime, bool]] = {}
        self._mute_cache_ttl = timedelta(seconds=mute_cache_ttl)

        logger.info("UserManager initialized with JSON file persistence", cache_ttl_seconds=mute_cache_ttl)

    def _normalize_to_uuid(self, player_id: uuid.UUID | str) -> uuid.UUID:
        """
        Normalize player_id to UUID object.

        Args:
            player_id: Player ID as UUID or string

        Returns:
            UUID object

        Raises:
            ValueError: If player_id cannot be converted to UUID
        """
        if isinstance(player_id, uuid.UUID):
            return player_id
        try:
            return uuid.UUID(player_id)
        except (ValueError, AttributeError, TypeError) as e:
            raise ValueError(f"Invalid player_id format: {player_id}") from e

    async def add_admin(self, player_id: uuid.UUID | str, player_name: str | None = None):
        """
        Add a player as an admin.

        Args:
            player_id: Player ID
            player_name: Player name for logging
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Update database
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            if container and container.async_persistence:
                persistence = container.async_persistence
                player = await persistence.get_player_by_id(player_id_uuid)
                if player:
                    player.set_admin_status(True)
                    await persistence.save_player(player)
                logger.info(
                    "Player added as admin in database",
                    # Structlog handles UUID objects automatically, no need to convert to string
                    player_id=player_id_uuid,
                    player_name=player_name,
                )
            else:
                logger.error("Player not found in database")
                return False

            # Update in-memory cache (using UUID object as key)
            self._admin_players.add(player_id_uuid)

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

    async def remove_admin(self, player_id: uuid.UUID | str, player_name: str | None = None):
        """
        Remove a player's admin status.

        Args:
            player_id: Player ID
            player_name: Player name for logging
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Update database
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            if container and container.async_persistence:
                persistence = container.async_persistence
                player = await persistence.get_player_by_id(player_id_uuid)
                if player:
                    player.set_admin_status(False)
                    await persistence.save_player(player)
                logger.info(
                    "Player admin status removed from database",
                    player_id=player_id_uuid,
                    player_name=player_name,
                )
            else:
                logger.error("Player not found in database")
                return False

            # Update in-memory cache (using UUID object as key)
            if player_id_uuid in self._admin_players:
                self._admin_players.remove(player_id_uuid)

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

    def is_admin_sync(self, player_id: uuid.UUID | str) -> bool:
        """
        Synchronous version of is_admin that only checks the cache.

        Use this in synchronous contexts. For async contexts, use is_admin().

        Args:
            player_id: Player ID

        Returns:
            True if player is admin (and in cache), False otherwise
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Check in-memory cache only
            return player_id_uuid in self._admin_players
        except (ValueError, TypeError, AttributeError) as e:
            logger.warning("Error in is_admin_sync", player_id=player_id, error=str(e))
            return False

    async def is_admin(self, player_id: uuid.UUID | str) -> bool:
        """
        Check if a player is an admin.

        Args:
            player_id: Player ID

        Returns:
            True if player is admin
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Check in-memory cache first
            if player_id_uuid in self._admin_players:
                return True

            # Check database if not in cache
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            if container and container.async_persistence:
                persistence = container.async_persistence
                player = await persistence.get_player_by_id(player_id_uuid)
            else:
                player = None
            if player and player.is_admin_user():
                # Add to cache (using UUID object as key)
                self._admin_players.add(player_id_uuid)
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
        muter_id: uuid.UUID | str,
        muter_name: str,
        target_id: uuid.UUID | str,
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
            # Normalize to UUID for dictionary operations
            muter_id_uuid = self._normalize_to_uuid(muter_id)
            target_id_uuid = self._normalize_to_uuid(target_id)

            # Check if target is admin (immune to mutes)
            if self.is_admin_sync(target_id_uuid):
                logger.warning("Attempted to mute admin player")
                return False

            # Initialize player mutes if needed
            if muter_id_uuid not in self._player_mutes:
                self._player_mutes[muter_id_uuid] = {}

            # Calculate mute expiry
            expiry_time = None
            if duration_minutes:
                expiry_time = datetime.now(UTC) + timedelta(minutes=duration_minutes)

            # Store mute information (use UUID objects - convert to string only for JSON serialization)
            mute_info = {
                "target_id": target_id_uuid,  # Store as UUID object
                "target_name": target_name,
                "muted_by": muter_id_uuid,  # Store as UUID object
                "muted_by_name": muter_name,
                "muted_at": datetime.now(UTC),
                "expires_at": expiry_time,
                "reason": reason,
                "is_permanent": duration_minutes is None,
            }

            self._player_mutes[muter_id_uuid][target_id_uuid] = mute_info

            # Log the mute for AI processing (chat_logger may expect strings)
            self.chat_logger.log_player_muted(
                muter_id=str(muter_id_uuid),  # chat_logger may expect strings
                target_id=str(target_id_uuid),  # chat_logger may expect strings
                target_name=target_name,
                mute_type="player",
                duration_minutes=duration_minutes,
                reason=reason,
            )

            logger.info(
                "Player muted another player",
                # Structlog handles UUID objects automatically, no need to convert to string
                muter_id=muter_id_uuid,
                muter_name=muter_name,
                target_id=target_id_uuid,
                target_name=target_name,
                duration_minutes=duration_minutes,
                reason=reason,
            )

            # Save mute data for both players
            self.save_player_mutes(muter_id_uuid)
            self.save_player_mutes(target_id_uuid)

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

    def unmute_player(
        self, unmuter_id: uuid.UUID | str, unmuter_name: str, target_id: uuid.UUID | str, target_name: str
    ) -> bool:
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
            # Normalize to UUID for dictionary operations
            unmuter_id_uuid = self._normalize_to_uuid(unmuter_id)
            target_id_uuid = self._normalize_to_uuid(target_id)

            # Load unmuter's mute data to ensure it's available
            self.load_player_mutes(unmuter_id_uuid)

            # Check if mute exists
            if unmuter_id_uuid in self._player_mutes and target_id_uuid in self._player_mutes[unmuter_id_uuid]:
                # Remove the mute
                del self._player_mutes[unmuter_id_uuid][target_id_uuid]

                # Clean up empty player mute entries
                if not self._player_mutes[unmuter_id_uuid]:
                    del self._player_mutes[unmuter_id_uuid]

                # Log the unmute for AI processing (chat_logger may expect strings)
                self.chat_logger.log_player_unmuted(
                    unmuter_id=str(unmuter_id_uuid),
                    target_id=str(target_id_uuid),
                    target_name=target_name,
                    mute_type="player",
                )

                logger.info(
                    "Player unmuted another player",
                    # Structlog handles UUID objects automatically, no need to convert to string
                    unmuter_id=unmuter_id_uuid,
                    unmuter_name=unmuter_name,
                    target_id=target_id_uuid,
                    target_name=target_name,
                )

                # Save mute data for both players
                self.save_player_mutes(unmuter_id_uuid)
                self.save_player_mutes(target_id_uuid)

                return True
            else:
                logger.warning(
                    "Attempted to unmute non-muted player", unmuter_id=unmuter_id_uuid, target_id=target_id_uuid
                )
                return False

        except Exception as e:
            logger.error("Error unmuting player", error=str(e), unmuter_id=unmuter_id, target_id=target_id)
            return False

    def mute_channel(
        self,
        player_id: uuid.UUID | str,
        player_name: str,
        channel: str,
        duration_minutes: int | None = None,
        reason: str = "",
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
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Initialize channel mutes if needed
            if player_id_uuid not in self._channel_mutes:
                self._channel_mutes[player_id_uuid] = {}

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

            self._channel_mutes[player_id_uuid][channel] = mute_info

            # Log the mute for AI processing
            self.chat_logger.log_player_muted(
                muter_id=str(player_id_uuid),
                target_id=str(player_id_uuid),
                target_name=player_name,
                mute_type=f"channel_{channel}",
                duration_minutes=duration_minutes,
                reason=reason,
            )

            logger.info(
                "Player muted channel",
                player_id=player_id_uuid,
                player_name=player_name,
                channel=channel,
                duration_minutes=duration_minutes,
                reason=reason,
            )

            # Save mute data for the player
            self.save_player_mutes(player_id_uuid)

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

    def unmute_channel(self, player_id: uuid.UUID | str, player_name: str, channel: str) -> bool:
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
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Check if channel mute exists
            if player_id_uuid in self._channel_mutes and channel in self._channel_mutes[player_id_uuid]:
                # Remove the mute
                del self._channel_mutes[player_id_uuid][channel]

                # Clean up empty channel mute entries
                if not self._channel_mutes[player_id_uuid]:
                    del self._channel_mutes[player_id_uuid]

                # Log the unmute for AI processing (chat_logger may expect strings)
                self.chat_logger.log_player_unmuted(
                    unmuter_id=str(player_id_uuid),
                    target_id=str(player_id_uuid),
                    target_name=player_name,
                    mute_type=f"channel_{channel}",
                )

                logger.info(
                    "Player unmuted channel",
                    # Structlog handles UUID objects automatically, no need to convert to string
                    player_id=player_id_uuid,
                    player_name=player_name,
                    channel=channel,
                )

                # Save mute data for the player
                self.save_player_mutes(player_id_uuid)

                return True
            else:
                logger.warning("Attempted to unmute non-muted channel", player_id=player_id_uuid, channel=channel)
                return False

        except Exception as e:
            logger.error("Error unmuting channel", error=str(e), player_id=player_id, channel=channel)
            return False

    def mute_global(
        self,
        muter_id: uuid.UUID | str,
        muter_name: str,
        target_id: uuid.UUID | str,
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
            # Normalize to UUID for dictionary operations
            muter_id_uuid = self._normalize_to_uuid(muter_id)
            target_id_uuid = self._normalize_to_uuid(target_id)

            # Check if target is admin (immune to mutes)
            if self.is_admin(target_id_uuid):
                logger.warning(
                    "Attempted to globally mute admin player", muter_id=muter_id_uuid, target_id=target_id_uuid
                )
                return False

            # Calculate mute expiry
            expiry_time = None
            if duration_minutes:
                expiry_time = datetime.now(UTC) + timedelta(minutes=duration_minutes)

            # Store global mute information (use UUID objects - convert to string only for JSON serialization)
            mute_info = {
                "target_id": target_id_uuid,  # Store as UUID object
                "target_name": target_name,
                "muted_by": muter_id_uuid,  # Store as UUID object
                "muted_by_name": muter_name,
                "muted_at": datetime.now(UTC),
                "expires_at": expiry_time,
                "reason": reason,
                "is_permanent": duration_minutes is None,
            }

            self._global_mutes[target_id_uuid] = mute_info

            # Log the global mute for AI processing (chat_logger may expect strings)
            self.chat_logger.log_player_muted(
                muter_id=str(muter_id_uuid),
                target_id=str(target_id_uuid),
                target_name=target_name,
                mute_type="global",
                duration_minutes=duration_minutes,
                reason=reason,
            )

            logger.info(
                "Player globally muted",
                # Structlog handles UUID objects automatically, no need to convert to string
                muter_id=muter_id_uuid,
                muter_name=muter_name,
                target_id=target_id_uuid,
                target_name=target_name,
                duration_minutes=duration_minutes,
                reason=reason,
            )

            # Save mute data for both players
            self.save_player_mutes(muter_id_uuid)
            self.save_player_mutes(target_id_uuid)

            return True

        except Exception as e:
            logger.error("Error applying global mute", error=str(e), muter_id=muter_id, target_id=target_id)
            return False

    def unmute_global(
        self, unmuter_id: uuid.UUID | str, unmuter_name: str, target_id: uuid.UUID | str, target_name: str
    ) -> bool:
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
            # Normalize to UUID for dictionary operations
            unmuter_id_uuid = self._normalize_to_uuid(unmuter_id)
            target_id_uuid = self._normalize_to_uuid(target_id)

            # Load unmuter's mute data to ensure it's available
            self.load_player_mutes(unmuter_id_uuid)

            # Check if global mute exists
            if target_id_uuid in self._global_mutes:
                # Remove the global mute
                del self._global_mutes[target_id_uuid]

                # Log the global unmute for AI processing (chat_logger may expect strings)
                self.chat_logger.log_player_unmuted(
                    unmuter_id=str(unmuter_id_uuid),
                    target_id=str(target_id_uuid),
                    target_name=target_name,
                    mute_type="global",
                )

                logger.info(
                    "Player globally unmuted",
                    # Structlog handles UUID objects automatically, no need to convert to string
                    unmuter_id=unmuter_id_uuid,
                    unmuter_name=unmuter_name,
                    target_id=target_id_uuid,
                    target_name=target_name,
                )

                # Save mute data for both players
                self.save_player_mutes(unmuter_id_uuid)
                self.save_player_mutes(target_id_uuid)

                return True
            else:
                logger.warning(
                    "Attempted to remove non-existent global mute", unmuter_id=unmuter_id_uuid, target_id=target_id_uuid
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

    def is_player_muted(self, player_id: uuid.UUID | str, target_id: uuid.UUID | str) -> bool:
        """
        Check if a player has muted another player.

        Args:
            player_id: Player ID
            target_id: Target player ID

        Returns:
            True if target is muted by player
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)
            target_id_uuid = self._normalize_to_uuid(target_id)

            logger.info(
                "=== USER MANAGER: is_player_muted called ===",
                player_id=str(player_id_uuid),
                target_id=str(target_id_uuid),
                player_id_type=type(player_id).__name__,
                target_id_type=type(target_id).__name__,
            )

            # Load player's mute data to ensure it's available
            load_result = self.load_player_mutes(player_id_uuid)
            logger.info(
                "=== USER MANAGER: Mute data load result ===",
                player_id=str(player_id_uuid),
                load_result=load_result,
                has_mute_data=player_id_uuid in self._player_mutes,
            )

            # Check if mute exists and is not expired
            if player_id_uuid in self._player_mutes:
                muted_players = list(self._player_mutes[player_id_uuid].keys())
                logger.info(
                    "=== USER MANAGER: Player's muted players list ===",
                    player_id=str(player_id_uuid),
                    muted_players=[str(p) for p in muted_players],
                    target_id=str(target_id_uuid),
                    target_in_list=target_id_uuid in self._player_mutes[player_id_uuid],
                )

                if target_id_uuid in self._player_mutes[player_id_uuid]:
                    mute_info = self._player_mutes[player_id_uuid][target_id_uuid]

                    # Check if mute is expired
                    if mute_info["expires_at"] and mute_info["expires_at"] < datetime.now(UTC):
                        logger.info(
                            "=== USER MANAGER: Mute is EXPIRED ===",
                            player_id=str(player_id_uuid),
                            target_id=str(target_id_uuid),
                            expires_at=mute_info["expires_at"],
                        )
                        # Remove expired mute
                        del self._player_mutes[player_id_uuid][target_id_uuid]
                        if not self._player_mutes[player_id_uuid]:
                            del self._player_mutes[player_id_uuid]
                        return False

                    logger.info(
                        "=== USER MANAGER: Mute EXISTS and is VALID ===",
                        player_id=str(player_id_uuid),
                        target_id=str(target_id_uuid),
                        mute_info=mute_info,
                    )
                    return True
                else:
                    logger.info(
                        "=== USER MANAGER: Target NOT in muted players list ===",
                        player_id=str(player_id_uuid),
                        target_id=str(target_id_uuid),
                        muted_players=[str(p) for p in muted_players],
                    )
            else:
                logger.info(
                    "=== USER MANAGER: Player has NO mute data loaded ===",
                    player_id=str(player_id_uuid),
                    target_id=str(target_id_uuid),
                )

            logger.info(
                "=== USER MANAGER: Returning False (not muted) ===",
                player_id=str(player_id_uuid),
                target_id=str(target_id_uuid),
            )
            return False

        except Exception as e:
            logger.error(
                "Error checking player mute",
                error=str(e),
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                target_id=target_id,
            )
            return False

    async def is_player_muted_async(self, player_id: uuid.UUID | str, target_id: uuid.UUID | str) -> bool:
        """
        Async version of is_player_muted using async mute loading.

        Args:
            player_id: Player ID
            target_id: Target player ID

        Returns:
            True if target is muted by player

        AI: Uses async mute loading to prevent blocking the event loop.
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)
            target_id_uuid = self._normalize_to_uuid(target_id)

            # Load player's mute data asynchronously to ensure it's available
            await self.load_player_mutes_async(player_id_uuid)

            # Check if mute exists and is not expired
            if player_id_uuid in self._player_mutes and target_id_uuid in self._player_mutes[player_id_uuid]:
                mute_info = self._player_mutes[player_id_uuid][target_id_uuid]

                # Check if mute is expired
                if mute_info["expires_at"] and mute_info["expires_at"] < datetime.now(UTC):
                    # Remove expired mute
                    del self._player_mutes[player_id_uuid][target_id_uuid]
                    if not self._player_mutes[player_id_uuid]:
                        del self._player_mutes[player_id_uuid]
                    return False

                return True

            return False

        except Exception as e:
            logger.error(
                "Error checking player mute (async)",
                error=str(e),
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                target_id=target_id,
            )
            return False

    def is_channel_muted(self, player_id: uuid.UUID | str, channel: str) -> bool:
        """
        Check if a player has muted a specific channel.

        Args:
            player_id: Player ID
            channel: Channel name

        Returns:
            True if channel is muted by player
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Check if channel mute exists and is not expired
            if player_id_uuid in self._channel_mutes and channel in self._channel_mutes[player_id_uuid]:
                mute_info = self._channel_mutes[player_id_uuid][channel]

                # Check if mute is expired
                if mute_info["expires_at"] and mute_info["expires_at"] < datetime.now(UTC):
                    # Remove expired mute
                    del self._channel_mutes[player_id_uuid][channel]
                    if not self._channel_mutes[player_id_uuid]:
                        del self._channel_mutes[player_id_uuid]
                    return False

                return True

            return False

        except Exception as e:
            logger.error(
                "Error checking channel mute",
                error=str(e),
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                channel=channel,
            )
            return False

    def is_globally_muted(self, player_id: uuid.UUID | str) -> bool:
        """
        Check if a player is globally muted.

        Args:
            player_id: Player ID

        Returns:
            True if player is globally muted
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Check if global mute exists and is not expired
            if player_id_uuid in self._global_mutes:
                mute_info = self._global_mutes[player_id_uuid]

                # Check if mute is expired
                if mute_info["expires_at"] and mute_info["expires_at"] < datetime.now(UTC):
                    # Remove expired mute
                    del self._global_mutes[player_id_uuid]
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

    def can_send_message(
        self, sender_id: uuid.UUID | str, target_id: uuid.UUID | str | None = None, channel: str | None = None
    ) -> bool:
        """
        Check if a player can send a message.

        Args:
            sender_id: Sender player ID
            target_id: Target player ID (for whispers)
            channel: Channel name (for channel messages)

        Returns:
            True if player can send message
        """
        # No need to convert to string here - methods accept UUID | str

        try:
            # Admins can always send messages
            if self.is_admin_sync(sender_id):
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

        except (OSError, ValueError, TypeError, AttributeError) as e:
            logger.error(
                "Error checking message permissions",
                error=str(e),
                # Structlog handles UUID objects automatically, no need to convert to string
                sender_id=sender_id,
            )
            return False

    def get_player_mutes(self, player_id: uuid.UUID | str) -> dict[str, Any]:
        """
        Get all mutes applied by a player.

        Args:
            player_id: Player ID

        Returns:
            Dictionary with mute information
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Type annotation: player_mutes and global_mutes use UUID keys, channel_mutes uses string keys
            mutes: dict[str, Any] = {"player_mutes": {}, "channel_mutes": {}, "global_mutes": {}}

            # Get player mutes (keep UUID objects)
            if player_id_uuid in self._player_mutes:
                for target_id_uuid, mute_info in self._player_mutes[player_id_uuid].items():
                    # Check if not expired
                    if not mute_info["expires_at"] or mute_info["expires_at"] > datetime.now(UTC):
                        mutes["player_mutes"][target_id_uuid] = mute_info

            # Get channel mutes
            if player_id_uuid in self._channel_mutes:
                for channel, mute_info in self._channel_mutes[player_id_uuid].items():
                    # Check if not expired
                    if not mute_info["expires_at"] or mute_info["expires_at"] > datetime.now(UTC):
                        mutes["channel_mutes"][channel] = mute_info

            # Get global mutes applied by this player (keep UUID objects)
            for target_id_uuid, mute_info in self._global_mutes.items():
                if mute_info["muted_by"] == player_id_uuid:  # Compare UUID objects
                    # Check if not expired
                    if not mute_info["expires_at"] or mute_info["expires_at"] > datetime.now(UTC):
                        mutes["global_mutes"][target_id_uuid] = mute_info

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

    def is_player_muted_by_others(self, player_id: uuid.UUID | str) -> bool:
        """
        Check if a player is globally muted by any other player.

        Args:
            player_id: Player ID to check

        Returns:
            True if player is globally muted by others
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Only check if player is in any global mutes
            # Personal mutes should not prevent the muted player from sending messages
            if player_id_uuid in self._global_mutes:
                return True

            return False
        except (ValueError, TypeError):
            return False

    def get_who_muted_player(self, player_id: uuid.UUID | str) -> list[tuple[str, str]]:
        """
        Get information about who muted a player.

        Args:
            player_id: Player ID to check

        Returns:
            List of tuples (muter_name, mute_type)
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            muted_by = []

            # Check global mutes
            if player_id_uuid in self._global_mutes:
                mute_info = self._global_mutes[player_id_uuid]
                muter_name = mute_info.get("muted_by_name", "Unknown")
                muted_by.append((muter_name, "global"))

            # Check personal mutes
            for _muter_id_uuid, mutes in self._player_mutes.items():
                if player_id_uuid in mutes:
                    mute_info = mutes[player_id_uuid]
                    muter_name = mute_info.get("muted_by_name", "Unknown")
                    muted_by.append((muter_name, "personal"))

            return muted_by
        except (ValueError, TypeError):
            return []

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
                "admin_players": [str(pid) for pid in self._admin_players],  # Convert UUIDs to strings for JSON
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

    def _get_player_mute_file(self, player_id: uuid.UUID | str) -> Path:
        """Get the mute data file path for a specific player."""
        # Convert to string for filename
        player_id_str = str(player_id)
        return self.data_dir / f"mutes_{player_id_str}.json"

    def load_player_mutes(self, player_id: uuid.UUID | str) -> bool:
        """
        Load mute data for a specific player from JSON file.

        Args:
            player_id: Player ID to load mutes for

        Returns:
            True if data was loaded successfully, False otherwise
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            mute_file = self._get_player_mute_file(player_id_uuid)

            if not mute_file.exists():
                logger.debug("No mute file found for player")
                return False

            with open(mute_file, encoding="utf-8") as f:
                data = json.load(f)

            # Load player mutes (convert string keys from JSON to UUID keys and UUID strings to UUID objects)
            if "player_mutes" in data:
                self._player_mutes[player_id_uuid] = {}
                for target_id_str, mute_info in data["player_mutes"].items():
                    # Convert timestamp strings back to datetime objects
                    if "muted_at" in mute_info:
                        mute_info["muted_at"] = datetime.fromisoformat(mute_info["muted_at"])
                    if "expires_at" in mute_info and mute_info["expires_at"]:
                        mute_info["expires_at"] = datetime.fromisoformat(mute_info["expires_at"])
                    # Convert string UUIDs in mute_info back to UUID objects
                    if "target_id" in mute_info and isinstance(mute_info["target_id"], str):
                        mute_info["target_id"] = uuid.UUID(mute_info["target_id"])
                    if "muted_by" in mute_info and isinstance(mute_info["muted_by"], str):
                        mute_info["muted_by"] = uuid.UUID(mute_info["muted_by"])
                    # Convert string key to UUID
                    try:
                        target_id_uuid = uuid.UUID(target_id_str)
                        self._player_mutes[player_id_uuid][target_id_uuid] = mute_info
                    except (ValueError, TypeError):
                        logger.warning("Invalid UUID format in player_mutes", target_id=target_id_str)
                        continue

            # Load channel mutes
            if "channel_mutes" in data:
                self._channel_mutes[player_id_uuid] = {}
                for channel, mute_info in data["channel_mutes"].items():
                    # Convert timestamp strings back to datetime objects
                    if "muted_at" in mute_info:
                        mute_info["muted_at"] = datetime.fromisoformat(mute_info["muted_at"])
                    if "expires_at" in mute_info and mute_info["expires_at"]:
                        mute_info["expires_at"] = datetime.fromisoformat(mute_info["expires_at"])
                    self._channel_mutes[player_id_uuid][channel] = mute_info

            # Load global mutes applied by this player (convert string keys from JSON to UUID keys and UUID strings to UUID objects)
            if "global_mutes" in data:
                for target_id_str, mute_info in data["global_mutes"].items():
                    # Convert timestamp strings back to datetime objects
                    if "muted_at" in mute_info:
                        mute_info["muted_at"] = datetime.fromisoformat(mute_info["muted_at"])
                    if "expires_at" in mute_info and mute_info["expires_at"]:
                        mute_info["expires_at"] = datetime.fromisoformat(mute_info["expires_at"])
                    # Convert string UUIDs in mute_info back to UUID objects
                    if "target_id" in mute_info and isinstance(mute_info["target_id"], str):
                        mute_info["target_id"] = uuid.UUID(mute_info["target_id"])
                    if "muted_by" in mute_info and isinstance(mute_info["muted_by"], str):
                        mute_info["muted_by"] = uuid.UUID(mute_info["muted_by"])
                    # Convert string key to UUID
                    try:
                        target_id_uuid = uuid.UUID(target_id_str)
                        self._global_mutes[target_id_uuid] = mute_info
                    except (ValueError, TypeError):
                        logger.warning("Invalid UUID format in global_mutes", target_id=target_id_str)
                        continue

            # Load admin status (using UUID object as key)
            if "is_admin" in data and data["is_admin"]:
                self._admin_players.add(player_id_uuid)

            # Update cache (using UUID object as key)
            self._mute_cache[player_id_uuid] = (datetime.now(UTC), True)
            logger.info("Player mute data loaded")
            return True

        except OSError as e:
            logger.error("File system error loading player mute data", error=str(e), error_type=type(e).__name__)
            try:
                player_id_uuid = self._normalize_to_uuid(player_id)
                self._mute_cache[player_id_uuid] = (datetime.now(UTC), False)
            except (ValueError, TypeError):
                pass
            return False
        except (ValueError, TypeError, json.JSONDecodeError) as e:
            logger.error("Data validation error loading player mute data", error=str(e), error_type=type(e).__name__)
            try:
                player_id_uuid = self._normalize_to_uuid(player_id)
                self._mute_cache[player_id_uuid] = (datetime.now(UTC), False)
            except (ValueError, TypeError):
                pass
            return False
        except Exception as e:
            logger.error("Unexpected error loading player mute data", error=str(e), error_type=type(e).__name__)
            try:
                player_id_uuid = self._normalize_to_uuid(player_id)
                self._mute_cache[player_id_uuid] = (datetime.now(UTC), False)
            except (ValueError, TypeError):
                pass
            return False

    def _is_cache_valid(self, player_id: uuid.UUID) -> bool:
        """
        Check if cached mute data is still valid.

        Args:
            player_id: Player ID to check (UUID object)

        Returns:
            True if cache is valid, False otherwise
        """
        if player_id not in self._mute_cache:
            return False

        load_time, _ = self._mute_cache[player_id]
        age = datetime.now(UTC) - load_time
        return age < self._mute_cache_ttl

    async def load_player_mutes_async(self, player_id: uuid.UUID | str) -> bool:
        """
        Async version of load_player_mutes using asyncio.to_thread for file I/O.

        Args:
            player_id: Player ID to load mutes for

        Returns:
            True if data was loaded successfully, False otherwise

        AI: Uses asyncio.to_thread to run synchronous file I/O in thread pool,
            preventing blocking of the event loop.
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Check cache first
            if self._is_cache_valid(player_id_uuid):
                logger.debug("Using cached mute data", player_id=player_id_uuid)
                return True

            # Load from file using thread pool
            result = await asyncio.to_thread(self.load_player_mutes, player_id_uuid)
            return result
        except Exception as e:
            logger.error("Error in async mute loading", player_id=player_id, error=str(e))
            return False

    async def load_player_mutes_batch(self, player_ids: list[uuid.UUID | str]) -> dict[str, bool]:
        """
        Batch load mute data for multiple players concurrently.

        Args:
            player_ids: List of player IDs to load mutes for

        Returns:
            Dictionary mapping player_id to load success status

        AI: Loads mute data for all players concurrently using asyncio.gather,
            significantly improving performance when loading multiple players.
        """
        # Filter out players with valid cache (normalize to UUID first)
        players_to_load = []
        for pid in player_ids:
            try:
                pid_uuid = self._normalize_to_uuid(pid)
                if not self._is_cache_valid(pid_uuid):
                    players_to_load.append(pid)
            except (ValueError, TypeError):
                # Invalid UUID, include in load list to handle error
                players_to_load.append(pid)

        if not players_to_load:
            logger.debug("All players have valid cached mute data", total_players=len(player_ids))
            # Convert all UUIDs to strings for dict.fromkeys
            player_ids_str = [str(pid) for pid in player_ids]
            return dict.fromkeys(player_ids_str, True)

        logger.debug(
            "Batch loading mute data",
            total_players=len(player_ids),
            cached=len(player_ids) - len(players_to_load),
            to_load=len(players_to_load),
        )

        # Load all players concurrently
        results = await asyncio.gather(
            *[self.load_player_mutes_async(pid) for pid in players_to_load],
            return_exceptions=True,
        )

        # Build result dictionary (convert UUIDs to strings for dictionary keys)
        result_dict: dict[str, bool] = {}
        for i, player_id in enumerate(players_to_load):
            player_id_str = str(player_id)  # Convert to string for dictionary key
            if isinstance(results[i], Exception):
                logger.error(
                    "Error loading mute data in batch",
                    # Structlog handles UUID objects automatically, no need to convert to string
                    player_id=player_id,
                    error=str(results[i]),
                )
                result_dict[player_id_str] = False
            else:
                result_dict[player_id_str] = bool(results[i])

        # Add cached players (convert UUIDs to strings for dictionary keys)
        for player_id in player_ids:
            player_id_str = str(player_id)  # Convert to string for dictionary key
            if player_id_str not in result_dict:
                result_dict[player_id_str] = True

        return result_dict

    def save_player_mutes(self, player_id: uuid.UUID | str) -> bool:
        """
        Save mute data for a specific player to JSON file.

        Args:
            player_id: Player ID to save mutes for

        Returns:
            True if data was saved successfully, False otherwise
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)
            player_id_str = str(player_id_uuid)  # For JSON serialization

            mute_file = self._get_player_mute_file(player_id_uuid)

            # Prepare data for serialization
            data: dict[str, Any] = {
                "player_id": player_id_str,  # Use string for JSON serialization
                "last_updated": datetime.now(UTC).isoformat(),
                "player_mutes": {},
                "channel_mutes": {},
                "global_mutes": {},
                "is_admin": player_id_uuid in self._admin_players,  # Use UUID for dictionary lookup
            }

            # Save player mutes (convert UUID keys to strings for JSON)
            if player_id_uuid in self._player_mutes:
                for target_id_uuid, mute_info in self._player_mutes[player_id_uuid].items():
                    # Convert datetime objects to ISO strings for JSON serialization
                    serialized_mute = mute_info.copy()
                    if "muted_at" in serialized_mute:
                        serialized_mute["muted_at"] = serialized_mute["muted_at"].isoformat()
                    if "expires_at" in serialized_mute and serialized_mute["expires_at"]:
                        serialized_mute["expires_at"] = serialized_mute["expires_at"].isoformat()
                    # Convert UUID objects to strings for JSON serialization
                    if "target_id" in serialized_mute and isinstance(serialized_mute["target_id"], uuid.UUID):
                        serialized_mute["target_id"] = str(serialized_mute["target_id"])
                    if "muted_by" in serialized_mute and isinstance(serialized_mute["muted_by"], uuid.UUID):
                        serialized_mute["muted_by"] = str(serialized_mute["muted_by"])
                    data["player_mutes"][str(target_id_uuid)] = serialized_mute

            # Save channel mutes
            if player_id_uuid in self._channel_mutes:
                for channel, mute_info in self._channel_mutes[player_id_uuid].items():
                    # Convert datetime objects to ISO strings for JSON serialization
                    serialized_mute = mute_info.copy()
                    if "muted_at" in serialized_mute:
                        serialized_mute["muted_at"] = serialized_mute["muted_at"].isoformat()
                    if "expires_at" in serialized_mute and serialized_mute["expires_at"]:
                        serialized_mute["expires_at"] = serialized_mute["expires_at"].isoformat()
                    data["channel_mutes"][channel] = serialized_mute

            # Save global mutes applied by this player (convert UUID keys to strings for JSON)
            for target_id_uuid, mute_info in self._global_mutes.items():
                if mute_info.get("muted_by") == player_id_uuid:  # Compare UUID objects
                    # Convert datetime objects to ISO strings for JSON serialization
                    serialized_mute = mute_info.copy()
                    if "muted_at" in serialized_mute:
                        serialized_mute["muted_at"] = serialized_mute["muted_at"].isoformat()
                    if "expires_at" in serialized_mute and serialized_mute["expires_at"]:
                        serialized_mute["expires_at"] = serialized_mute["expires_at"].isoformat()
                    # Convert UUID objects to strings for JSON serialization
                    if "target_id" in serialized_mute and isinstance(serialized_mute["target_id"], uuid.UUID):
                        serialized_mute["target_id"] = str(serialized_mute["target_id"])
                    if "muted_by" in serialized_mute and isinstance(serialized_mute["muted_by"], uuid.UUID):
                        serialized_mute["muted_by"] = str(serialized_mute["muted_by"])
                    data["global_mutes"][str(target_id_uuid)] = serialized_mute

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

    def cleanup_player_mutes(self, player_id: uuid.UUID | str, *, delete_file: bool = False) -> bool:
        """
        Remove mute data for a player from memory and optionally delete their file.
        Called when a player logs out or is deleted.

        Args:
            player_id: Player ID to cleanup
            delete_file: Whether to delete the persisted mute file. Defaults to False.

        Returns:
            True if cleanup was successful, False otherwise
        """
        try:
            # Normalize to UUID for dictionary operations
            player_id_uuid = self._normalize_to_uuid(player_id)

            # Remove from memory (using UUID objects as keys)
            if player_id_uuid in self._player_mutes:
                del self._player_mutes[player_id_uuid]

            if player_id_uuid in self._channel_mutes:
                del self._channel_mutes[player_id_uuid]

            if player_id_uuid in self._global_mutes:
                del self._global_mutes[player_id_uuid]

            if player_id_uuid in self._admin_players:
                self._admin_players.remove(player_id_uuid)

            if delete_file:
                # Delete file only when explicitly requested (e.g., account deletion)
                mute_file = self._get_player_mute_file(player_id_uuid)
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
