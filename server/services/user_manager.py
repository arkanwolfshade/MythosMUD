"""
User management service for MythosMUD chat system.

This module provides comprehensive user management including muting,
permissions, and user state tracking for the chat system.
"""

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments,too-many-lines,too-many-public-methods  # Reason: User manager requires many state tracking attributes and complex user management logic. User manager requires extensive user management operations for comprehensive chat system user management. User manager legitimately requires many public methods for comprehensive user management.

import uuid
from datetime import UTC, datetime, timedelta
from typing import Literal, cast

from structlog.stdlib import BoundLogger

from ..async_persistence import AsyncPersistenceLayer
from ..persistence.repositories.player_mute_repository import MuteType, PlayerMute, PlayerMuteRepository
from ..structured_logging.enhanced_logging_config import get_logger
from .chat_logger import ChatLogger, chat_logger

logger: BoundLogger = get_logger("communications.user_manager")


class UserManager:  # pylint: disable=too-many-instance-attributes  # Reason: User manager requires many state tracking and configuration attributes
    """
    Comprehensive user management for chat system.

    Handles player muting, channel muting, permissions, and user state
    tracking with integration to AI logging systems.
    """

    chat_logger: ChatLogger
    _async_persistence: AsyncPersistenceLayer | None
    _mute_repository: PlayerMuteRepository

    def __init__(
        self,
        async_persistence: AsyncPersistenceLayer | None = None,
        mute_repository: PlayerMuteRepository | None = None,
    ) -> None:
        """
        Initialize the user manager.

        Mutes live in the player_mutes table (#681). The dicts below are an in-memory index
        filled once by load_all_mutes() at startup, so the (sync) mute checks on the chat hot
        path never touch the database; mute/unmute write through to the database first.

        Args:
            async_persistence: Optional async persistence layer for admin-status lookups (#679:
                injected by GameBundle instead of reached via ApplicationContainer.get_instance())
            mute_repository: Durable mute store (defaults to PlayerMuteRepository)
        """
        self._async_persistence = async_persistence
        self._mute_repository = mute_repository or PlayerMuteRepository()
        # Player mute storage: {player_id: {target_id: mute_info}}
        # Using UUID objects as keys for type safety and consistency
        self._player_mutes: dict[uuid.UUID, dict[uuid.UUID, dict[str, object]]] = {}

        # Channel mute storage: {player_id: {channel: mute_info}}
        # Using UUID objects as keys for type safety and consistency
        self._channel_mutes: dict[uuid.UUID, dict[str, dict[str, object]]] = {}

        # Global mute storage: {player_id: mute_info}
        # Using UUID objects as keys for type safety and consistency
        self._global_mutes: dict[uuid.UUID, dict[str, object]] = {}

        # Admin players (immune to mutes)
        # Using UUID objects for type safety and consistency
        self._admin_players: set[uuid.UUID] = set()

        # Chat logger for AI processing
        self.chat_logger = chat_logger

        logger.info("UserManager initialized with database mute persistence")

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

    async def add_admin(self, player_id: uuid.UUID | str, player_name: str | None = None) -> bool:
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
            ap_layer = self._async_persistence
            if ap_layer:
                persistence = ap_layer
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
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Unexpected error adding admin status", error=str(e), error_type=type(e).__name__)
            return False

    async def remove_admin(self, player_id: uuid.UUID | str, player_name: str | None = None) -> bool:
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
            ap_layer_rm = self._async_persistence
            if ap_layer_rm:
                persistence = ap_layer_rm
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
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
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
            ap_layer_admin = self._async_persistence
            if ap_layer_admin:
                persistence = ap_layer_admin
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
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error(
                "Unexpected error checking admin status in database", error=str(e), error_type=type(e).__name__
            )

        return False

    @staticmethod
    def _new_mute(
        mute_type: MuteType,
        muter_id: uuid.UUID,
        muter_name: str,
        target: tuple[uuid.UUID, str] | None,
        channel: str | None,
        duration_minutes: int | None,
        reason: str,
    ) -> PlayerMute:
        """Build a mute record starting now; duration None (or 0) means permanent."""
        now = datetime.now(UTC)
        return PlayerMute(
            mute_type=mute_type,
            muter_id=muter_id,
            muter_name=muter_name,
            target_id=target[0] if target else None,
            target_name=target[1] if target else None,
            channel=channel,
            reason=reason,
            muted_at=now,
            expires_at=now + timedelta(minutes=duration_minutes) if duration_minutes else None,
        )

    @staticmethod
    def _mute_info(mute: PlayerMute) -> dict[str, object]:
        """In-memory mute record (the shape readers such as get_player_mutes expose)."""
        common: dict[str, object] = {
            "muted_at": mute.muted_at,
            "expires_at": mute.expires_at,
            "reason": mute.reason,
            "is_permanent": mute.expires_at is None,
        }
        if mute.mute_type == "channel":
            return {"channel": mute.channel, **common}
        return {
            "target_id": mute.target_id,
            "target_name": mute.target_name,
            "muted_by": mute.muter_id,
            "muted_by_name": mute.muter_name,
            **common,
        }

    def _index_mute(self, mute: PlayerMute) -> None:
        """Add a persisted mute to the in-memory index."""
        info = self._mute_info(mute)
        if mute.mute_type == "channel" and mute.channel is not None:
            self._channel_mutes.setdefault(mute.muter_id, {})[mute.channel] = info
        elif mute.target_id is None:
            logger.warning("Ignoring mute without target", mute_type=mute.mute_type, muter_id=mute.muter_id)
        elif mute.mute_type == "player":
            self._player_mutes.setdefault(mute.muter_id, {})[mute.target_id] = info
        else:
            self._global_mutes[mute.target_id] = info

    async def load_all_mutes(self) -> int:
        """Replace the in-memory index with every active mute from the database. Returns the count."""
        mutes = await self._mute_repository.load_active()
        self._player_mutes.clear()
        self._channel_mutes.clear()
        self._global_mutes.clear()
        for mute in mutes:
            self._index_mute(mute)
        logger.info("Player mutes loaded from database", count=len(mutes))
        return len(mutes)

    def _log_mute_applied(
        self,
        muter_id_uuid: uuid.UUID,
        muter_name: str,
        target_id_uuid: uuid.UUID,
        target_name: str,
        duration_minutes: int | None,
        reason: str,
    ) -> None:
        """Log the applied mute to the chat log and structured logger."""
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

    async def mute_player(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Player muting requires many parameters for context and mute operations
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

            mute = self._new_mute(
                "player", muter_id_uuid, muter_name, (target_id_uuid, target_name), None, duration_minutes, reason
            )
            await self._mute_repository.upsert(mute)
            self._index_mute(mute)

            self._log_mute_applied(muter_id_uuid, muter_name, target_id_uuid, target_name, duration_minutes, reason)

            return True

        except OSError as e:
            logger.error("File system error muting player", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError) as e:
            logger.error("Data validation error muting player", error=str(e), error_type=type(e).__name__)
            return False
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Unexpected error muting player", error=str(e), error_type=type(e).__name__)
            return False

    async def unmute_player(
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

            # Check if mute exists
            if unmuter_id_uuid in self._player_mutes and target_id_uuid in self._player_mutes[unmuter_id_uuid]:
                _ = await self._mute_repository.delete("player", unmuter_id_uuid, target_id_uuid, None)
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

                return True
            # Expected no-op (idempotent cleanup unmutes), not a fault; the command layer replies to the player.
            logger.debug("Attempted to unmute non-muted player", unmuter_id=unmuter_id_uuid, target_id=target_id_uuid)
            return False

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Error unmuting player", error=str(e), unmuter_id=unmuter_id, target_id=target_id)
            return False

    async def mute_channel(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Channel muting requires many parameters for context and mute operations
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

            mute = self._new_mute("channel", player_id_uuid, player_name, None, channel, duration_minutes, reason)
            await self._mute_repository.upsert(mute)
            self._index_mute(mute)

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

            return True

        except OSError as e:
            logger.error("File system error muting channel", error=str(e), error_type=type(e).__name__)
            return False
        except (ValueError, TypeError) as e:
            logger.error("Data validation error muting channel", error=str(e), error_type=type(e).__name__)
            return False
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Unexpected error muting channel", error=str(e), error_type=type(e).__name__)
            return False

    async def unmute_channel(self, player_id: uuid.UUID | str, player_name: str, channel: str) -> bool:
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
                _ = await self._mute_repository.delete("channel", player_id_uuid, None, channel)
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

                return True
            logger.debug("Attempted to unmute non-muted channel", player_id=player_id_uuid, channel=channel)
            return False

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Error unmuting channel", error=str(e), player_id=player_id, channel=channel)
            return False

    async def mute_global(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Global muting requires many parameters for context and mute operations
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
            if self.is_admin_sync(target_id_uuid):
                logger.warning(
                    "Attempted to globally mute admin player", muter_id=muter_id_uuid, target_id=target_id_uuid
                )
                return False

            mute = self._new_mute(
                "global", muter_id_uuid, muter_name, (target_id_uuid, target_name), None, duration_minutes, reason
            )
            await self._mute_repository.upsert(mute)
            self._index_mute(mute)

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

            return True

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Error applying global mute", error=str(e), muter_id=muter_id, target_id=target_id)
            return False

    async def unmute_global(
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

            # Check if global mute exists
            if target_id_uuid in self._global_mutes:
                _ = await self._mute_repository.delete("global", None, target_id_uuid, None)
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

                return True
            logger.warning(
                "Attempted to remove non-existent global mute", unmuter_id=unmuter_id_uuid, target_id=target_id_uuid
            )
            return False

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error(
                "Error removing global mute",
                error=str(e),
                unmuter_id=unmuter_id,
                target_id=target_id,
            )
            return False

    def _resolve_player_mute_vs_target(
        self, player_id_uuid: uuid.UUID, target_id_uuid: uuid.UUID
    ) -> Literal["active", "expired", "absent"]:
        """
        Classify mute state for (player_id -> target_id). Removes expired entries.

        AI: Extracted from is_player_muted to keep cyclomatic complexity within tooling limits.
        """
        if player_id_uuid not in self._player_mutes:
            return "absent"
        bucket = self._player_mutes[player_id_uuid]
        if target_id_uuid not in bucket:
            return "absent"
        mute_info = bucket[target_id_uuid]
        ex_chk = mute_info.get("expires_at")
        if isinstance(ex_chk, datetime) and ex_chk < datetime.now(UTC):
            logger.info(
                "=== USER MANAGER: Mute is EXPIRED ===",
                player_id=str(player_id_uuid),
                target_id=str(target_id_uuid),
                expires_at=ex_chk,
            )
            del bucket[target_id_uuid]
            if not bucket:
                del self._player_mutes[player_id_uuid]
            return "expired"
        return "active"

    def is_player_muted(  # lizard: allow nloc (structured debug-log checkpoints, not branching; CCN 8, see #787)
        self, player_id: uuid.UUID | str, target_id: uuid.UUID | str
    ) -> bool:
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

            has_bucket = player_id_uuid in self._player_mutes

            if has_bucket:
                muted_players = list(self._player_mutes[player_id_uuid].keys())
                logger.info(
                    "=== USER MANAGER: Player's muted players list ===",
                    player_id=str(player_id_uuid),
                    muted_players=[str(p) for p in muted_players],
                    target_id=str(target_id_uuid),
                    target_in_list=target_id_uuid in self._player_mutes[player_id_uuid],
                )

            outcome = self._resolve_player_mute_vs_target(player_id_uuid, target_id_uuid)
            if outcome == "active":
                mute_info = self._player_mutes[player_id_uuid][target_id_uuid]
                logger.info(
                    "=== USER MANAGER: Mute EXISTS and is VALID ===",
                    player_id=str(player_id_uuid),
                    target_id=str(target_id_uuid),
                    mute_info=mute_info,
                )
                return True

            if has_bucket and outcome == "absent":
                logger.info(
                    "=== USER MANAGER: Target NOT in muted players list ===",
                    player_id=str(player_id_uuid),
                    target_id=str(target_id_uuid),
                    muted_players=[str(p) for p in self._player_mutes[player_id_uuid].keys()],
                )

            logger.info(
                "=== USER MANAGER: Returning False (not muted) ===",
                player_id=str(player_id_uuid),
                target_id=str(target_id_uuid),
            )
            return False

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error(
                "Error checking player mute",
                error=str(e),
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                target_id=target_id,
            )
            return False

    async def is_player_muted_async(self, player_id: uuid.UUID | str, target_id: uuid.UUID | str) -> bool:
        """Async-compatible alias of is_player_muted (mutes are already indexed in memory)."""
        return self.is_player_muted(player_id, target_id)

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
                ex_ch = mute_info.get("expires_at")
                if isinstance(ex_ch, datetime) and ex_ch < datetime.now(UTC):
                    # Remove expired mute
                    del self._channel_mutes[player_id_uuid][channel]
                    if not self._channel_mutes[player_id_uuid]:
                        del self._channel_mutes[player_id_uuid]
                    return False

                return True

            return False

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
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
                ex_gl = mute_info.get("expires_at")
                if isinstance(ex_gl, datetime) and ex_gl < datetime.now(UTC):
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
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Unexpected error checking global mute", error=str(e), error_type=type(e).__name__)
            return False

    def can_send_message(
        self, sender_id: uuid.UUID | str, _target_id: uuid.UUID | str | None = None, channel: str | None = None
    ) -> bool:
        """
        Check if a player can send a message.

        Args:
            sender_id: Sender player ID
            _target_id: Target player ID (for whispers) - unused, kept for API compatibility
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

    def _get_active_player_mutes(
        self, player_id_uuid: uuid.UUID, current_time: datetime
    ) -> dict[uuid.UUID, dict[str, object]]:
        """Get active player mutes for a player."""
        active_mutes: dict[uuid.UUID, dict[str, object]] = {}
        if player_id_uuid in self._player_mutes:
            for target_id_uuid, mute_info in self._player_mutes[player_id_uuid].items():
                expires_raw = mute_info.get("expires_at")
                if isinstance(expires_raw, datetime) and expires_raw <= current_time:
                    continue
                active_mutes[target_id_uuid] = mute_info
        return active_mutes

    def _get_active_channel_mutes(
        self, player_id_uuid: uuid.UUID, current_time: datetime
    ) -> dict[str, dict[str, object]]:
        """Get active channel mutes for a player."""
        active_mutes: dict[str, dict[str, object]] = {}
        if player_id_uuid in self._channel_mutes:
            for channel, mute_info in self._channel_mutes[player_id_uuid].items():
                expires_raw = mute_info.get("expires_at")
                if isinstance(expires_raw, datetime) and expires_raw <= current_time:
                    continue
                active_mutes[channel] = mute_info
        return active_mutes

    def _get_active_global_mutes(
        self, player_id_uuid: uuid.UUID, current_time: datetime
    ) -> dict[uuid.UUID, dict[str, object]]:
        """Get active global mutes applied by a player."""
        active_mutes: dict[uuid.UUID, dict[str, object]] = {}
        for target_id_uuid, mute_info in self._global_mutes.items():
            if mute_info["muted_by"] == player_id_uuid:
                expires_raw = mute_info.get("expires_at")
                if isinstance(expires_raw, datetime) and expires_raw <= current_time:
                    continue
                active_mutes[target_id_uuid] = mute_info
        return active_mutes

    def get_player_mutes(self, player_id: uuid.UUID | str) -> dict[str, object]:
        """
        Get all mutes applied by a player.

        Args:
            player_id: Player ID

        Returns:
            Dictionary with mute information
        """
        try:
            player_id_uuid = self._normalize_to_uuid(player_id)
            current_time = datetime.now(UTC)

            mutes: dict[str, object] = {
                "player_mutes": self._get_active_player_mutes(player_id_uuid, current_time),
                "channel_mutes": self._get_active_channel_mutes(player_id_uuid, current_time),
                "global_mutes": self._get_active_global_mutes(player_id_uuid, current_time),
            }

            return mutes

        except OSError as e:
            logger.error("File system error getting player mutes", error=str(e), error_type=type(e).__name__)
            return {
                "player_mutes": cast(dict[uuid.UUID, dict[str, object]], {}),
                "channel_mutes": cast(dict[str, dict[str, object]], {}),
                "global_mutes": cast(dict[uuid.UUID, dict[str, object]], {}),
            }
        except (ValueError, TypeError) as e:
            logger.error("Data validation error getting player mutes", error=str(e), error_type=type(e).__name__)
            return {
                "player_mutes": cast(dict[uuid.UUID, dict[str, object]], {}),
                "channel_mutes": cast(dict[str, dict[str, object]], {}),
                "global_mutes": cast(dict[uuid.UUID, dict[str, object]], {}),
            }
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Unexpected error getting player mutes", error=str(e), error_type=type(e).__name__)
            return {
                "player_mutes": cast(dict[uuid.UUID, dict[str, object]], {}),
                "channel_mutes": cast(dict[str, dict[str, object]], {}),
                "global_mutes": cast(dict[uuid.UUID, dict[str, object]], {}),
            }

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

            muted_by: list[tuple[str, str]] = []

            # Check global mutes
            if player_id_uuid in self._global_mutes:
                mute_info = self._global_mutes[player_id_uuid]
                muter_name = str(mute_info.get("muted_by_name", "Unknown"))
                muted_by.append((muter_name, "global"))

            # Check personal mutes
            for _muter_id_uuid, mutes in self._player_mutes.items():
                if player_id_uuid in mutes:
                    mute_info = mutes[player_id_uuid]
                    muter_name = str(mute_info.get("muted_by_name", "Unknown"))
                    muted_by.append((muter_name, "personal"))

            return muted_by
        except (ValueError, TypeError):
            return []

    def get_system_stats(self) -> dict[str, object]:
        """
        Get system-wide user management statistics.

        Returns:
            Dictionary with system statistics
        """
        try:
            # Clean up expired mutes first
            self._cleanup_expired_mutes()

            stats: dict[str, object] = {
                "total_players_with_mutes": len(self._player_mutes),
                "total_channel_mutes": sum(len(mutes) for mutes in self._channel_mutes.values()),
                "total_global_mutes": len(self._global_mutes),
                "total_admin_players": len(self._admin_players),
                "admin_players": [str(pid) for pid in self._admin_players],  # Convert UUIDs to strings for JSON
            }

            return stats

        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Error getting system stats", error=str(e))
            return cast(dict[str, object], {})

    def _cleanup_player_mutes(self, current_time: datetime) -> None:
        """Clean up expired player mutes."""
        for player_id in list(self._player_mutes.keys()):
            for target_id in list(self._player_mutes[player_id].keys()):
                mute_info = self._player_mutes[player_id][target_id]
                ex_p = mute_info.get("expires_at")
                if isinstance(ex_p, datetime) and ex_p < current_time:
                    del self._player_mutes[player_id][target_id]

            if not self._player_mutes[player_id]:
                del self._player_mutes[player_id]

    def _cleanup_channel_mutes(self, current_time: datetime) -> None:
        """Clean up expired channel mutes."""
        for player_id in list(self._channel_mutes.keys()):
            for channel in list(self._channel_mutes[player_id].keys()):
                mute_info = self._channel_mutes[player_id][channel]
                ex_c = mute_info.get("expires_at")
                if isinstance(ex_c, datetime) and ex_c < current_time:
                    del self._channel_mutes[player_id][channel]

            if not self._channel_mutes[player_id]:
                del self._channel_mutes[player_id]

    def _cleanup_global_mutes(self, current_time: datetime) -> None:
        """Clean up expired global mutes."""
        for player_id in list(self._global_mutes.keys()):
            mute_info = self._global_mutes[player_id]
            ex_g = mute_info.get("expires_at")
            if isinstance(ex_g, datetime) and ex_g < current_time:
                del self._global_mutes[player_id]

    def _cleanup_expired_mutes(self) -> None:
        """Clean up expired mutes from all storage."""
        try:
            current_time = datetime.now(UTC)
            self._cleanup_player_mutes(current_time)
            self._cleanup_channel_mutes(current_time)
            self._cleanup_global_mutes(current_time)
        except Exception as e:  # pylint: disable=broad-except  # Catch-all for unexpected errors
            logger.error("Error cleaning up expired mutes", error=str(e))
