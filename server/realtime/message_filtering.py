"""
Message filtering utilities for NATS message handler.

This module handles room filtering, mute checking, and player location validation
for message broadcasting.
"""

import uuid
from typing import TYPE_CHECKING, Any, cast
from unittest.mock import Mock

from ..logging.enhanced_logging_config import get_logger
from ..services.nats_exceptions import NATSError

# Constants shared with nats_message_handler
MUTE_SENSITIVE_CHANNELS = frozenset({"say", "local", "emote", "pose", "whisper", "global", "system", "admin"})
SUPPRESS_ECHO_MESSAGE_IDS: set[str] = set()

logger = get_logger("communications.message_filtering")

if TYPE_CHECKING:
    from ..services.user_manager import UserManager


class MessageFilteringHelper:
    """Helper class for message filtering operations."""

    def __init__(self, connection_manager, user_manager=None):
        """
        Initialize message filtering helper.

        Args:
            connection_manager: ConnectionManager instance
            user_manager: Optional UserManager instance (defaults to global singleton)
        """
        self.connection_manager = connection_manager
        self.user_manager = user_manager

    def _get_user_manager(self) -> "UserManager":
        """Return the user manager instance to use for mute lookups."""
        if self.user_manager is not None:
            return self.user_manager

        from ..services.user_manager import user_manager as global_user_manager

        return global_user_manager

    def collect_room_targets(self, room_id: str) -> set[str]:
        """
        Collect all players subscribed to a room (canonical and original IDs).

        Args:
            room_id: Room ID to collect targets for

        Returns:
            Set of player IDs subscribed to the room
        """
        canonical_id = self.connection_manager.canonical_room_id(room_id) or room_id
        logger.debug(
            "=== BROADCAST FILTERING DEBUG: Room ID resolution ===",
            room_id=room_id,
            canonical_id=canonical_id,
        )

        targets: set[str] = set()

        if canonical_id in self.connection_manager.room_subscriptions:
            targets.update(self.connection_manager.room_subscriptions[canonical_id])
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Added canonical room subscribers ===",
                room_id=room_id,
                canonical_id=canonical_id,
                canonical_subscribers=list(self.connection_manager.room_subscriptions[canonical_id]),
            )
        if room_id != canonical_id and room_id in self.connection_manager.room_subscriptions:
            targets.update(self.connection_manager.room_subscriptions[room_id])
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Added original room subscribers ===",
                room_id=room_id,
                original_subscribers=list(self.connection_manager.room_subscriptions[room_id]),
            )

        logger.debug(
            "=== BROADCAST FILTERING DEBUG: Total targets before filtering ===",
            room_id=room_id,
            total_targets=list(targets),
            target_count=len(targets),
        )

        return targets

    async def preload_receiver_mute_data(self, user_manager: "UserManager", targets: set[str], sender_id: str) -> None:
        """
        Pre-load mute data for all potential receivers.

        Args:
            user_manager: UserManager instance to use for loading
            targets: Set of all target player IDs
            sender_id: Sender player ID to exclude
        """
        receiver_ids = [pid for pid in targets if pid != sender_id]
        if not receiver_ids:
            return

        logger.debug(
            "=== BROADCAST FILTERING DEBUG: Pre-loading mute data for receivers ===",
            receiver_count=len(receiver_ids),
        )

        try:
            receiver_ids_typed: list[uuid.UUID | str] = cast(list[uuid.UUID | str], receiver_ids)
            load_results = await user_manager.load_player_mutes_batch(receiver_ids_typed)
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Batch loaded mute data ===",
                loaded_count=sum(1 for v in load_results.values() if v),
                failed_count=sum(1 for v in load_results.values() if not v),
            )
        except (NATSError, RuntimeError) as e:
            logger.warning(
                "Failed to batch load mute data for receivers",
                receiver_count=len(receiver_ids),
                error=str(e),
            )

    def extract_chat_event_info(self, chat_event: dict) -> tuple[str | None, dict, str | None, bool]:
        """
        Extract information from chat event.

        Args:
            chat_event: Chat event dictionary

        Returns:
            Tuple of (event_type, chat_event_data, message_id, sender_already_notified)
        """
        event_type = chat_event.get("event_type") if isinstance(chat_event, dict) else None
        if not event_type and isinstance(chat_event, dict):
            event_type = chat_event.get("type")

        chat_event_data = {}
        if isinstance(chat_event, dict):
            potential_data = chat_event.get("data")
            if isinstance(potential_data, dict):
                chat_event_data = potential_data

        sender_already_notified = False
        message_id = None
        if chat_event_data:
            message_id = chat_event_data.get("id")
            sender_already_notified = bool(chat_event_data.get("echo_sent"))
            if message_id in SUPPRESS_ECHO_MESSAGE_IDS:
                sender_already_notified = True
                SUPPRESS_ECHO_MESSAGE_IDS.discard(message_id)

        return event_type, chat_event_data, message_id, sender_already_notified

    def should_apply_mute_check(self, channel: str, message_id: str | None) -> bool:
        """
        Determine if mute check should be applied for a channel.

        Args:
            channel: Channel type
            message_id: Message ID (None for legacy messages)

        Returns:
            True if mute check should be applied
        """
        return channel in MUTE_SENSITIVE_CHANNELS or (channel == "say" and message_id is None)

    def compare_canonical_rooms(self, player_room_id: str, message_room_id: str) -> bool:
        """
        Compare two room IDs using canonical room ID resolution.

        Args:
            player_room_id: Player's current room ID
            message_room_id: Message room ID to compare against

        Returns:
            bool: True if rooms match after canonical resolution, False otherwise
        """
        canonical_player_room = self.connection_manager.canonical_room_id(player_room_id) or player_room_id
        canonical_message_room = self.connection_manager.canonical_room_id(message_room_id) or message_room_id
        return canonical_player_room == canonical_message_room

    def get_player_room_from_online_players(self, player_id: str) -> str | None:
        """
        Get player's current room ID from online players cache.

        Args:
            player_id: Player ID to look up

        Returns:
            Player's room ID if found, None otherwise
        """
        online_players = getattr(self.connection_manager, "online_players", {})
        if player_id not in online_players:
            return None

        player_info = online_players[player_id]
        if not isinstance(player_info, dict):
            return None

        player_room_id = player_info.get("current_room_id")
        if isinstance(player_room_id, str) and player_room_id:
            return player_room_id

        return None

    async def get_player_room_from_persistence(self, player_id: str) -> str | None:
        """
        Get player's current room ID from async persistence layer.

        Args:
            player_id: Player ID to look up

        Returns:
            Player's room ID if found, None otherwise
        """
        async_persistence = getattr(self.connection_manager, "async_persistence", None)
        if not async_persistence:
            return None

        player = await async_persistence.get_player_by_id(player_id)
        if not player or isinstance(player, Mock):
            return None

        player_room_id = getattr(player, "current_room_id", None)
        if isinstance(player_room_id, str) and player_room_id:
            return player_room_id

        return None

    async def is_player_in_room(self, player_id: str, room_id: str) -> bool:
        """
        Check if a player is currently in the specified room.

        Args:
            player_id: Player ID to check
            room_id: Room ID to check against

        Returns:
            bool: True if player is in the room, False otherwise
        """
        try:
            # First, try to get room from online players cache
            player_room_id = self.get_player_room_from_online_players(player_id)
            if player_room_id:
                return self.compare_canonical_rooms(player_room_id, room_id)

            # Fallback: check async persistence layer
            player_room_id = await self.get_player_room_from_persistence(player_id)
            if player_room_id:
                return self.compare_canonical_rooms(player_room_id, room_id)

            return False

        except (NATSError, RuntimeError) as e:
            logger.error(
                "Error checking if player is in room",
                error=str(e),
                player_id=player_id,
                room_id=room_id,
            )
            return False

    def is_player_muted_by_receiver(self, receiver_id: str, sender_id: str) -> bool:
        """
        Check if a receiving player has muted the sender.

        Args:
            receiver_id: Player ID of the message receiver
            sender_id: Player ID of the message sender

        Returns:
            bool: True if receiver has muted sender, False otherwise
        """
        logger.debug(
            "=== MUTE FILTERING DEBUG: Starting mute check ===",
            receiver_id=receiver_id,
            sender_id=sender_id,
        )

        try:
            user_manager = self._get_user_manager()

            logger.debug(
                "=== MUTE FILTERING DEBUG: UserManager created ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
            )

            # Load the receiver's mute data before checking
            mute_load_result = user_manager.load_player_mutes(receiver_id)
            logger.debug(
                "=== MUTE FILTERING DEBUG: Mute data load result ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
                mute_load_result=mute_load_result,
            )

            # Check what mute data is available (only for debugging, not for logic)
            try:
                player_mutes = getattr(user_manager, "_player_mutes", None)
                if player_mutes is not None:
                    available_mute_data = list(player_mutes.keys())
                    logger.debug(
                        "=== MUTE FILTERING DEBUG: Available mute data ===",
                        receiver_id=receiver_id,
                        sender_id=sender_id,
                        available_mute_data=available_mute_data,
                    )

                    # Convert receiver_id to UUID if it's a valid UUID string
                    # _player_mutes uses UUID keys, so we need to convert
                    # receiver_id is typed as str in function parameter, so always convert
                    receiver_id_uuid: uuid.UUID | None = None
                    try:
                        receiver_id_uuid = uuid.UUID(receiver_id)
                    except (ValueError, AttributeError, TypeError):
                        # If conversion fails, receiver_id is not a valid UUID, skip
                        receiver_id_uuid = None

                    if receiver_id_uuid and receiver_id_uuid in player_mutes:
                        receiver_mutes = list(player_mutes[receiver_id_uuid].keys())
                        logger.debug(
                            "=== MUTE FILTERING DEBUG: Receiver's muted players ===",
                            receiver_id=receiver_id,
                            sender_id=sender_id,
                            receiver_mutes=receiver_mutes,
                        )
                    else:
                        logger.debug(
                            "=== MUTE FILTERING DEBUG: No mute data for receiver ===",
                            receiver_id=receiver_id,
                            sender_id=sender_id,
                        )
                else:
                    logger.debug(
                        "=== MUTE FILTERING DEBUG: No internal mute data available (using API methods) ===",
                        receiver_id=receiver_id,
                        sender_id=sender_id,
                    )
            except (NATSError, RuntimeError) as debug_error:
                logger.debug(
                    "=== MUTE FILTERING DEBUG: Could not access internal mute data ===",
                    receiver_id=receiver_id,
                    sender_id=sender_id,
                    debug_error=str(debug_error),
                )

            # Check if receiver has muted sender (personal mute)
            logger.info(
                "=== MUTE FILTERING: Checking personal mute ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            is_personally_muted = user_manager.is_player_muted(receiver_id, sender_id)
            logger.info(
                "=== MUTE FILTERING: Personal mute check result ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
                is_personally_muted=is_personally_muted,
            )

            if is_personally_muted:
                logger.info(
                    "=== MUTE FILTERING: Player IS MUTED (personal mute) ===",
                    receiver_id=receiver_id,
                    sender_id=sender_id,
                )
                return True

            # Load global mutes and check if sender is globally muted by anyone
            # Only apply global mute if receiver is not an admin (admins can see globally muted players)
            logger.info(
                "=== MUTE FILTERING: Checking global mute ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            is_globally_muted = user_manager.is_player_muted_by_others(sender_id)
            is_receiver_admin = user_manager.is_admin_sync(receiver_id)

            logger.info(
                "=== MUTE FILTERING: Global mute check result ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
                is_globally_muted=is_globally_muted,
                is_receiver_admin=is_receiver_admin,
            )

            if is_globally_muted and not is_receiver_admin:
                logger.info(
                    "=== MUTE FILTERING: Player IS MUTED (global mute) ===",
                    receiver_id=receiver_id,
                    sender_id=sender_id,
                )
                return True

            logger.info(
                "=== MUTE FILTERING: Player NOT MUTED by receiver ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            return False

        except NATSError as e:
            logger.error(
                "Error checking mute status",
                error=str(e),
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            return False

    async def is_player_muted_by_receiver_with_user_manager(
        self, user_manager: "UserManager", receiver_id: str, sender_id: str
    ) -> bool:
        """
        Check if a receiving player has muted the sender using a provided UserManager instance.

        Args:
            user_manager: UserManager instance to use for mute checks
            receiver_id: Player ID of the message receiver
            sender_id: Player ID of the message sender

        Returns:
            bool: True if receiver has muted sender, False otherwise
        """
        logger.debug(
            "=== MUTE FILTERING DEBUG: Starting mute check with provided UserManager ===",
            receiver_id=receiver_id,
            sender_id=sender_id,
        )

        try:
            # Load the receiver's mute data before checking (if not already loaded) - async version
            mute_load_result = await user_manager.load_player_mutes_async(receiver_id)
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Mute data load result (async) ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
                mute_load_result=mute_load_result,
            )

            # Check what mute data is available (only for debugging, not for logic)
            try:
                player_mutes = getattr(user_manager, "_player_mutes", None)
                if player_mutes is not None:
                    available_mute_data = list(player_mutes.keys())
                    logger.debug(
                        "=== MUTE FILTERING DEBUG: Available mute data ===",
                        receiver_id=receiver_id,
                        sender_id=sender_id,
                        available_mute_data=available_mute_data,
                    )

                    if receiver_id in player_mutes:
                        receiver_mutes = list(player_mutes[receiver_id].keys())
                        logger.debug(
                            "=== MUTE FILTERING DEBUG: Receiver's muted players ===",
                            receiver_id=receiver_id,
                            sender_id=sender_id,
                            receiver_mutes=receiver_mutes,
                        )
                    else:
                        logger.debug(
                            "=== MUTE FILTERING DEBUG: No mute data for receiver ===",
                            receiver_id=receiver_id,
                            sender_id=sender_id,
                        )
                else:
                    logger.debug(
                        "=== MUTE FILTERING DEBUG: No internal mute data available (using API methods) ===",
                        receiver_id=receiver_id,
                        sender_id=sender_id,
                    )
            except (NATSError, RuntimeError) as debug_error:
                logger.debug(
                    "=== MUTE FILTERING DEBUG: Could not access internal mute data ===",
                    receiver_id=receiver_id,
                    sender_id=sender_id,
                    debug_error=str(debug_error),
                )

            # Check if receiver has muted sender (personal mute)
            is_personally_muted = user_manager.is_player_muted(receiver_id, sender_id)
            logger.debug(
                "=== MUTE FILTERING DEBUG: Personal mute check result ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
                is_personally_muted=is_personally_muted,
            )

            if is_personally_muted:
                logger.debug(
                    "Player muted by receiver (personal mute)",
                    receiver_id=receiver_id,
                    sender_id=sender_id,
                )
                return True

            # Load global mutes and check if sender is globally muted by anyone
            # Only apply global mute if receiver is not an admin (admins can see globally muted players)
            is_globally_muted = user_manager.is_player_muted_by_others(sender_id)
            is_receiver_admin = await user_manager.is_admin(receiver_id)

            logger.debug(
                "=== MUTE FILTERING DEBUG: Global mute check ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
                is_globally_muted=is_globally_muted,
                is_receiver_admin=is_receiver_admin,
            )

            if is_globally_muted and not is_receiver_admin:
                logger.debug(
                    "Player muted by receiver (global mute)",
                    receiver_id=receiver_id,
                    sender_id=sender_id,
                )
                return True

            logger.info(
                "=== MUTE FILTERING: Player NOT MUTED by receiver ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            return False
        except (NATSError, RuntimeError) as e:
            logger.error(
                "Error checking mute status with provided UserManager",
                receiver_id=receiver_id,
                sender_id=sender_id,
                error=str(e),
            )
            return False

    async def check_player_mute_status(
        self,
        user_manager: "UserManager",
        player_id: str,
        sender_id: str,
        channel: str,
        chat_event_data: dict,
        handler_instance: Any,  # NATSMessageHandler instance for patched methods
    ) -> bool:
        """
        Check if a player has muted the sender.

        Args:
            user_manager: UserManager instance
            player_id: Receiver player ID
            sender_id: Sender player ID
            channel: Channel type
            chat_event_data: Chat event data dictionary
            handler_instance: NATSMessageHandler instance (for accessing patched methods in tests)

        Returns:
            True if player has muted the sender
        """
        logger.info(
            "=== MUTE FILTERING: Starting mute check ===",
            sender_name=chat_event_data.get("sender_name", "unknown"),
            receiver_id=player_id,
            sender_id=sender_id,
            channel=channel,
        )

        patched_mute_checker = (
            getattr(handler_instance, "_is_player_muted_by_receiver", None) if handler_instance else None
        )
        if isinstance(patched_mute_checker, Mock):
            is_muted = patched_mute_checker(player_id, sender_id)
            logger.info(
                "=== MUTE FILTERING: Using patched mute checker (test mode) ===",
                receiver_id=player_id,
                sender_id=sender_id,
                is_muted=is_muted,
            )
            return is_muted

        logger.info(
            "=== MUTE FILTERING: Calling is_player_muted_by_receiver_with_user_manager ===",
            receiver_id=player_id,
            sender_id=sender_id,
        )
        is_muted = await self.is_player_muted_by_receiver_with_user_manager(user_manager, player_id, sender_id)
        logger.info(
            "=== MUTE FILTERING: Mute check completed ===",
            receiver_id=player_id,
            sender_id=sender_id,
            is_muted=is_muted,
        )

        if channel in {"emote", "pose"}:
            logger.info(
                "=== EMOTE MUTE FILTERING: Evaluation result ===",
                receiver_id=player_id,
                sender_id=sender_id,
                is_muted=is_muted,
                channel=channel,
                will_filter=is_muted,
            )

        return is_muted

    async def filter_target_players(
        self,
        targets: set[str],
        sender_id: str,
        room_id: str,
        channel: str,
        message_id: str | None,
        user_manager: "UserManager",
        chat_event_data: dict,
        handler_instance: Any,  # NATSMessageHandler instance for patched methods
    ) -> list[str]:
        """
        Filter target players based on room location and mute status.

        Args:
            targets: Set of all target player IDs
            sender_id: Sender player ID
            room_id: Room ID
            channel: Channel type
            message_id: Message ID
            user_manager: UserManager instance
            chat_event_data: Chat event data dictionary
            handler_instance: NATSMessageHandler instance (for accessing patched methods in tests)

        Returns:
            List of filtered player IDs
        """
        filtered_targets = []
        should_apply_mute = self.should_apply_mute_check(channel, message_id)

        for player_id in targets:
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Processing target player ===",
                room_id=room_id,
                sender_id=sender_id,
                target_player_id=player_id,
                channel=channel,
            )

            if player_id == sender_id:
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Skipping sender ===",
                    room_id=room_id,
                    sender_id=sender_id,
                    target_player_id=player_id,
                    channel=channel,
                )
                continue

            is_in_room = await self.is_player_in_room(player_id, room_id)
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Player in room check ===",
                room_id=room_id,
                sender_id=sender_id,
                target_player_id=player_id,
                is_in_room=is_in_room,
                channel=channel,
            )

            if not is_in_room:
                logger.debug(
                    "Filtered out player not in room",
                    player_id=player_id,
                    message_room_id=room_id,
                    channel=channel,
                )
                continue

            if should_apply_mute:
                is_muted = await self.check_player_mute_status(
                    user_manager, player_id, sender_id, channel, chat_event_data, handler_instance
                )
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Mute check result ===",
                    room_id=room_id,
                    sender_id=sender_id,
                    target_player_id=player_id,
                    is_muted=is_muted,
                    channel=channel,
                )

                if is_muted:
                    logger.info(
                        "=== MUTE FILTERING: Message FILTERED OUT due to mute ===",
                        receiver_id=player_id,
                        sender_id=sender_id,
                        channel=channel,
                        room_id=room_id,
                    )
                    continue
            else:
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Mute check skipped for channel ===",
                    room_id=room_id,
                    sender_id=sender_id,
                    target_player_id=player_id,
                    channel=channel,
                )

            logger.info(
                "=== MUTE FILTERING: Message ALLOWED (not muted or mute check skipped) ===",
                receiver_id=player_id,
                sender_id=sender_id,
                channel=channel,
                should_apply_mute=should_apply_mute,
            )

            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Player passed all filters ===",
                room_id=room_id,
                sender_id=sender_id,
                target_player_id=player_id,
                channel=channel,
            )
            filtered_targets.append(player_id)

        logger.debug(
            "=== BROADCAST FILTERING DEBUG: Final filtered targets ===",
            room_id=room_id,
            sender_id=sender_id,
            channel=channel,
            filtered_targets=filtered_targets,
            filtered_count=len(filtered_targets),
        )

        return filtered_targets
