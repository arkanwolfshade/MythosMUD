"""Room broadcast / mute / dampening mixin for NATSMessageHandler.

Extracted to keep nats_message_handler.py under the Lizard file-nloc limit.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any

from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger
from .message_formatters import format_message_content
from .nats_message_handler_base import NATSMessageHandlerMixinBase

if TYPE_CHECKING:
    from ..services.user_manager import UserManager

logger = get_logger("communications.nats_message_handler")

# Echo channels for sender (mirrors ECHO_SENDER_CHANNELS on main module)
ECHO_SENDER_CHANNELS = frozenset({"say", "local", "emote", "pose"})


class NATSMessageBroadcastMixin(NATSMessageHandlerMixinBase):
    """Mixin: room filtering, mute checks, dampening, and personal send."""

    def _collect_room_targets(self, room_id: str) -> set[str]:
        """Collect all players subscribed to a room (canonical and original IDs)."""
        return self._filtering_helper.collect_room_targets(room_id)

    async def _preload_receiver_mute_data(self, user_manager: UserManager, targets: set[str], sender_id: str) -> None:
        """Pre-load mute data for all potential receivers."""
        await self._filtering_helper.preload_receiver_mute_data(user_manager, targets, sender_id)

    def _extract_chat_event_info(
        self, chat_event: dict[str, Any]
    ) -> tuple[str | None, dict[str, Any], str | None, bool]:
        """Extract information from chat event."""
        return self._filtering_helper.extract_chat_event_info(chat_event)

    def _should_apply_mute_check(self, channel: str, message_id: str | None) -> bool:
        """Determine if mute check should be applied for a channel."""
        return self._filtering_helper.should_apply_mute_check(channel, message_id)

    async def _check_player_mute_status(
        self, user_manager: UserManager, player_id: str, sender_id: str, channel: str, chat_event_data: dict[str, Any]
    ) -> bool:
        """Check if a player has muted the sender."""
        return await self._filtering_helper.check_player_mute_status(
            user_manager, player_id, sender_id, channel, chat_event_data, self
        )

    async def _filter_target_players(
        self,
        targets: set[str],
        sender_id: str,
        room_id: str,
        channel: str,
        message_id: str | None,
        user_manager: UserManager,
        chat_event_data: dict[str, Any],
    ) -> list[str]:
        """Filter target players based on room location and mute status."""
        return await self._filtering_helper.filter_target_players(
            targets, sender_id, room_id, channel, message_id, user_manager, chat_event_data, self
        )

    async def _send_messages_to_players(
        self, filtered_targets: list[str], chat_event: dict[str, Any], room_id: str, sender_id: str, channel: str
    ) -> None:
        """
        Send messages to filtered target players, applying communication dampening per receiver.

        Args:
            filtered_targets: List of filtered player IDs
            chat_event: Chat event to send
            room_id: Room ID
            sender_id: Sender player ID
            channel: Channel type
        """
        # Get original content and sender info from chat event
        event_data = chat_event.get("data", {})
        original_content = event_data.get("original_content", "")
        sender_name = event_data.get("player_name", "")

        if not original_content:
            # Fallback: try to extract from formatted message (less reliable)
            formatted_message = event_data.get("message", "")
            logger.warning(
                "Original content not found in chat_event, using formatted message",
                sender_id=sender_id,
                channel=channel,
            )
            original_content = formatted_message

        # Get sender tier once (used for all receivers)
        sender_tier = await self._get_player_lucidity_tier(sender_id)

        # Apply communication dampening per receiver (function handles both outgoing and incoming effects)
        from ..services.lucidity_communication_dampening import apply_communication_dampening

        # Send message to each receiver with per-receiver dampening
        for player_id in filtered_targets:
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Sending message to player ===",
                room_id=room_id,
                sender_id=sender_id,
                target_player_id=player_id,
                channel=channel,
            )
            try:
                # Get receiver tier for incoming dampening
                receiver_tier = await self._get_player_lucidity_tier(player_id)

                # Apply communication dampening (handles both outgoing sender effects and incoming receiver effects)
                dampening_result = apply_communication_dampening(original_content, sender_tier, receiver_tier, channel)

                if dampening_result["blocked"]:
                    # Message blocked (e.g., Deranged player trying to shout)
                    logger.debug("Message blocked by communication dampening", receiver_id=player_id, channel=channel)
                    continue

                # Create modified chat event for this receiver
                receiver_content = dampening_result["message"]
                receiver_formatted = self._format_message_for_receiver(channel, sender_name, receiver_content)

                # Create copy of chat_event with modified message
                receiver_event = chat_event.copy()
                receiver_event["data"] = event_data.copy()
                receiver_event["data"]["message"] = receiver_formatted

                # Add tags if any (e.g., 'strained', 'muffled', 'scrambled')
                if dampening_result.get("tags"):
                    receiver_event["data"]["tags"] = dampening_result["tags"]

                player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
                await self.connection_manager.send_personal_message(player_id_uuid, receiver_event)
            except (ValueError, AttributeError, TypeError) as e:
                logger.warning(
                    "Invalid player_id format for send_personal_message",
                    player_id=player_id,
                    error=str(e),
                )

    def _should_echo_to_sender(
        self,
        channel: str,
        event_type: str | None,
        message_id: str | None,
        filtered_targets: list[str],
        sender_already_notified: bool,
    ) -> bool:
        """
        Determine if message should be echoed to sender.

        Args:
            channel: Channel type
            event_type: Event type
            message_id: Message ID
            filtered_targets: List of filtered targets
            sender_already_notified: Whether sender was already notified

        Returns:
            True if message should be echoed to sender
        """
        should_echo_sender = channel in ECHO_SENDER_CHANNELS and event_type == "chat_message" and message_id is not None

        if not should_echo_sender:
            return False

        if filtered_targets:
            return True

        return not sender_already_notified

    async def _echo_message_to_sender(
        self,
        sender_id: str,
        chat_event: dict[str, Any],
        room_id: str,
        channel: str,
        chat_event_data: dict[str, Any],
        message_id: str | None,
    ) -> None:
        """
        Echo message back to sender.

        Args:
            sender_id: Sender player ID
            chat_event: Chat event to echo
            room_id: Room ID
            channel: Channel type
            chat_event_data: Chat event data dictionary
            message_id: Message ID
        """
        if isinstance(chat_event_data, dict):
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Chat event data keys ===",
                data_keys=list(chat_event_data.keys()),
                message_id=message_id,
            )

        try:
            sender_id_uuid = uuid.UUID(sender_id) if isinstance(sender_id, str) else sender_id
            await self.connection_manager.send_personal_message(sender_id_uuid, chat_event)
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Echoed message to sender ===",
                room_id=room_id,
                sender_id=sender_id,
                channel=channel,
            )
        except (NATSError, RuntimeError) as echo_error:
            logger.warning(
                "Failed to echo message to sender",
                sender_id=sender_id,
                room_id=room_id,
                channel=channel,
                error=str(echo_error),
            )

    async def _broadcast_to_room_with_filtering(
        self, room_id: str, chat_event: dict[str, Any], sender_id: str, channel: str
    ) -> None:
        """
        Broadcast room-based messages with server-side filtering.

        This method ensures that players only receive messages from their current room,
        reducing network traffic and client load by filtering on the server side.

        Args:
            room_id: Room ID where the message originated
            chat_event: WebSocket event to broadcast
            sender_id: Sender player ID
            channel: Channel type (say, local, emote, pose)
        """
        logger.debug(
            "=== BROADCAST FILTERING DEBUG: Starting room broadcast ===",
            room_id=room_id,
            sender_id=sender_id,
            channel=channel,
        )

        try:
            targets = self._collect_room_targets(room_id)

            user_manager = self._get_user_manager()
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Created UserManager instance ===",
                room_id=room_id,
                sender_id=sender_id,
                channel=channel,
            )

            await self._preload_receiver_mute_data(user_manager, targets, sender_id)

            event_type, chat_event_data, message_id, sender_already_notified = self._extract_chat_event_info(chat_event)

            filtered_targets = await self._filter_target_players(
                targets, sender_id, room_id, channel, message_id, user_manager, chat_event_data
            )

            await self._send_messages_to_players(filtered_targets, chat_event, room_id, sender_id, channel)

            if self._should_echo_to_sender(channel, event_type, message_id, filtered_targets, sender_already_notified):
                await self._echo_message_to_sender(sender_id, chat_event, room_id, channel, chat_event_data, message_id)

            logger.info(
                "Room message broadcasted with server-side filtering",
                channel=channel,
                room_id=room_id,
                sender_id=sender_id,
                total_subscribers=len(targets),
                filtered_recipients=len(filtered_targets),
                excluded_count=len(targets) - len(filtered_targets) - 1,  # -1 for sender
            )

        except (NATSError, RuntimeError) as e:
            logger.error(
                "Error in server-side room message filtering",
                error=str(e),
                room_id=room_id,
                sender_id=sender_id,
                channel=channel,
            )

    def _get_user_manager(self) -> UserManager:
        """Return the user manager instance to use for mute lookups."""
        if self.user_manager is not None:
            return self.user_manager

        from ..services.user_manager import user_manager as global_user_manager

        return global_user_manager

    def _format_message_for_receiver(self, channel: str, sender_name: str, content: str) -> str:
        """
        Format message content for a receiver (after dampening applied).

        For whisper channel, formats as "X whispers to you: Y" so the recipient
        sees a clear private-message format.

        Args:
            channel: Channel type
            sender_name: Name of the message sender
            content: Message content (may have been modified by dampening)

        Returns:
            Formatted message content with sender name
        """
        return format_message_content(channel, sender_name, content, for_recipient=channel == "whisper")

    async def _apply_dampening_and_send_message(
        self, chat_event: dict[str, Any], sender_id: str, receiver_id: str, channel: str
    ) -> None:
        """
        Apply communication dampening and send message to a single receiver.

        Helper method for sending messages with dampening applied.
        Used for whisper messages and can be used for other single-receiver scenarios.

        Args:
            chat_event: Original chat event
            sender_id: Sender player ID (string)
            receiver_id: Receiver player ID (string)
            channel: Channel type
        """
        try:
            # Get original content and sender info from chat event
            event_data = chat_event.get("data", {})
            original_content = event_data.get("original_content", "")
            sender_name = event_data.get("player_name", "")

            if not original_content:
                # Fallback: try to extract from formatted message
                formatted_message = event_data.get("message", "")
                logger.warning(
                    "Original content not found in chat_event for dampening, using formatted message",
                    sender_id=sender_id,
                    receiver_id=receiver_id,
                    channel=channel,
                )
                original_content = formatted_message

            # Get sender and receiver tiers
            sender_tier = await self._get_player_lucidity_tier(sender_id)
            receiver_tier = await self._get_player_lucidity_tier(receiver_id)

            # Apply communication dampening
            from ..services.lucidity_communication_dampening import apply_communication_dampening

            dampening_result = apply_communication_dampening(original_content, sender_tier, receiver_tier, channel)

            if dampening_result["blocked"]:
                # Message blocked (e.g., Deranged player trying to shout)
                logger.debug(
                    "Message blocked by communication dampening",
                    receiver_id=receiver_id,
                    channel=channel,
                )
                return

            # Create modified chat event for receiver
            receiver_content = dampening_result["message"]
            receiver_formatted = self._format_message_for_receiver(channel, sender_name, receiver_content)

            # Create copy of chat_event with modified message
            receiver_event = chat_event.copy()
            receiver_event["data"] = event_data.copy()
            receiver_event["data"]["message"] = receiver_formatted

            # Add tags if any (e.g., 'strained', 'muffled', 'scrambled')
            if dampening_result.get("tags"):
                receiver_event["data"]["tags"] = dampening_result["tags"]

            receiver_id_uuid = uuid.UUID(receiver_id) if isinstance(receiver_id, str) else receiver_id
            await self.connection_manager.send_personal_message(receiver_id_uuid, receiver_event)

        except (ValueError, AttributeError, TypeError) as e:
            logger.warning(
                "Error applying dampening and sending message",
                sender_id=sender_id,
                receiver_id=receiver_id,
                error=str(e),
            )

    async def _get_player_lucidity_tier(self, player_id: str) -> str:
        """
        Get a player's current lucidity tier from database.

        Args:
            player_id: Player ID (string or UUID)

        Returns:
            Lucidity tier string (defaults to 'lucid' if not found)
        """
        try:
            from ..database import get_async_session
            from ..services.lucidity_service import LucidityService

            player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id

            async for session in get_async_session():
                try:
                    lucidity_service = LucidityService(session)
                    lucidity_record = await lucidity_service.get_player_lucidity(player_id_uuid)
                    tier = lucidity_record.current_tier if lucidity_record else "lucid"
                    return tier
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Lucidity tier retrieval errors unpredictable, optional metadata
                    logger.debug(
                        "Error getting player lucidity tier",
                        player_id=player_id,
                        error=str(e),
                        error_type=type(e).__name__,
                    )
                    return "lucid"

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Session creation errors unpredictable, must return fallback
            logger.debug(
                "Error in _get_player_lucidity_tier (session creation)",
                player_id=player_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            return "lucid"

        return "lucid"

    def _compare_canonical_rooms(self, player_room_id: str, message_room_id: str) -> bool:
        """Compare two room IDs using canonical room ID resolution."""
        return self._filtering_helper.compare_canonical_rooms(player_room_id, message_room_id)

    def _get_player_room_from_online_players(self, player_id: str) -> str | None:
        """Get player's current room ID from online players cache."""
        return self._filtering_helper.get_player_room_from_online_players(player_id)

    async def _get_player_room_from_persistence(self, player_id: str) -> str | None:
        """Get player's current room ID from async persistence layer."""
        return await self._filtering_helper.get_player_room_from_persistence(player_id)

    async def _is_player_in_room(self, player_id: str, room_id: str) -> bool:
        """Check if a player is currently in the specified room."""
        return await self._filtering_helper.is_player_in_room(player_id, room_id)

    def _is_player_muted_by_receiver(self, receiver_id: str, sender_id: str) -> bool:
        """Check if a receiving player has muted the sender."""
        return self._filtering_helper.is_player_muted_by_receiver(receiver_id, sender_id)

    async def _is_player_muted_by_receiver_with_user_manager(
        self, user_manager: UserManager, receiver_id: str, sender_id: str
    ) -> bool:
        """Check if a receiving player has muted the sender using a provided UserManager instance."""
        return await self._filtering_helper.is_player_muted_by_receiver_with_user_manager(
            user_manager, receiver_id, sender_id
        )
