"""
NATS message handler for MythosMUD chat system.

This module handles incoming NATS messages and broadcasts them to WebSocket clients.
It replaces the previous Redis message handler with NATS-based messaging.
"""

from typing import Any

from ..logging_config import get_logger
from ..realtime.connection_manager import connection_manager
from ..realtime.envelope import build_event

logger = get_logger("communications.nats_message_handler")


class NATSMessageHandler:
    """
    Handler for processing NATS messages and broadcasting to WebSocket clients.

    This handler subscribes to NATS subjects for chat messages and broadcasts
    them to the appropriate WebSocket clients based on room and channel.
    """

    def __init__(self, nats_service):
        """
        Initialize NATS message handler.

        Args:
            nats_service: NATS service instance for subscribing to subjects
        """
        self.nats_service = nats_service
        self.subscriptions = {}

        # Sub-zone subscription tracking for local channels
        self.subzone_subscriptions = {}  # subzone -> subscription_count
        self.player_subzone_subscriptions = {}  # player_id -> subzone

        logger.info("NATS message handler initialized")

    async def start(self):
        """Start the NATS message handler and subscribe to chat subjects."""
        try:
            # Subscribe to chat message subjects
            await self._subscribe_to_chat_subjects()
            logger.info("NATS message handler started successfully")
        except Exception as e:
            logger.error("Failed to start NATS message handler", error=str(e))

    async def stop(self):
        """Stop the NATS message handler and unsubscribe from subjects."""
        try:
            # Unsubscribe from all subjects
            for subject in list(self.subscriptions.keys()):
                await self._unsubscribe_from_subject(subject)
            logger.info("NATS message handler stopped successfully")
        except Exception as e:
            logger.error("Error stopping NATS message handler", error=str(e))

    async def _subscribe_to_chat_subjects(self):
        """Subscribe to all chat-related NATS subjects."""
        subjects = [
            "chat.say.*",  # Say messages per room
            "chat.local.subzone.*",  # Local messages per subzone
            "chat.emote.*",  # Emote messages per room
            "chat.pose.*",  # Pose messages per room
            "chat.global",  # Global messages
            "chat.party.*",  # Party messages per party
            "chat.whisper.*",  # Whisper messages per player
            "chat.system",  # System messages
            "chat.admin",  # Admin messages
        ]

        logger.debug("=== NATS MESSAGE HANDLER DEBUG: Subscribing to subjects ===")
        for subject in subjects:
            logger.debug(f"Attempting to subscribe to: {subject}")
            await self._subscribe_to_subject(subject)

    async def _subscribe_to_subject(self, subject: str):
        """Subscribe to a specific NATS subject."""
        try:
            success = await self.nats_service.subscribe(subject, self._handle_nats_message)
            if success:
                self.subscriptions[subject] = True
                logger.info("Subscribed to NATS subject", subject=subject)
            else:
                logger.error("Failed to subscribe to NATS subject", subject=subject)
        except Exception as e:
            logger.error("Error subscribing to NATS subject", subject=subject, error=str(e))

    async def _unsubscribe_from_subject(self, subject: str):
        """Unsubscribe from a specific NATS subject."""
        try:
            success = await self.nats_service.unsubscribe(subject)
            if success:
                if subject in self.subscriptions:
                    del self.subscriptions[subject]
                logger.info("Unsubscribed from NATS subject", subject=subject)
            else:
                logger.error("Failed to unsubscribe from NATS subject", subject=subject)
        except Exception as e:
            logger.error("Error unsubscribing from NATS subject", subject=subject, error=str(e))

    async def _handle_nats_message(self, message_data: dict[str, Any]):
        """
        Handle incoming NATS message and broadcast to WebSocket clients.

        Args:
            message_data: Message data from NATS
        """
        try:
            logger.debug("=== NATS MESSAGE HANDLER DEBUG: Received NATS message ===")
            logger.debug(f"Message data: {message_data}")
            logger.debug(f"Message type: {type(message_data)}")
            logger.debug(
                f"Message keys: {list(message_data.keys()) if isinstance(message_data, dict) else 'Not a dict'}"
            )

            # Extract message details
            channel = message_data.get("channel")
            room_id = message_data.get("room_id")
            party_id = message_data.get("party_id")
            target_player_id = message_data.get("target_player_id")
            sender_id = message_data.get("sender_id")
            sender_name = message_data.get("sender_name")
            content = message_data.get("content")
            message_id = message_data.get("message_id")
            timestamp = message_data.get("timestamp")

            # Validate required fields
            if not all([channel, sender_id, sender_name, content, message_id]):
                logger.warning("Invalid NATS message - missing required fields", message_data=message_data)
                return

            # Format message content based on channel type
            formatted_message = self._format_message_content(channel, sender_name, content)

            # Create WebSocket event
            chat_event = build_event(
                "chat_message",
                {
                    "sender_id": str(sender_id),
                    "player_name": sender_name,
                    "channel": channel,
                    "message": formatted_message,
                    "message_id": message_id,
                    "timestamp": timestamp,
                },
                player_id=str(sender_id),
            )

            # Broadcast based on channel type
            await self._broadcast_by_channel_type(channel, chat_event, room_id, party_id, target_player_id, sender_id)

        except Exception as e:
            logger.error("Error handling NATS message", error=str(e), message_data=message_data)

    async def _broadcast_by_channel_type(
        self, channel: str, chat_event: dict, room_id: str, party_id: str, target_player_id: str, sender_id: str
    ):
        """
        Broadcast message based on channel type using strategy pattern.

        Args:
            channel: Channel type (say, local, emote, pose, global, party, whisper, system, admin)
            chat_event: WebSocket event to broadcast
            room_id: Room ID for room-based channels
            party_id: Party ID for party-based channels
            target_player_id: Target player ID for whisper messages
            sender_id: Sender player ID
        """
        try:
            # Import here to avoid circular imports
            from .channel_broadcasting_strategies import channel_strategy_factory

            # Get strategy for channel type and execute broadcast
            strategy = channel_strategy_factory.get_strategy(channel)
            await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, self)

        except Exception as e:
            logger.error(
                "Error broadcasting message by channel type",
                error=str(e),
                channel=channel,
                room_id=room_id,
                party_id=party_id,
                target_player_id=target_player_id,
            )

    async def _broadcast_to_room_with_filtering(self, room_id: str, chat_event: dict, sender_id: str, channel: str):
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
        try:
            # Get all players subscribed to this room
            canonical_id = connection_manager._canonical_room_id(room_id) or room_id
            targets: set[str] = set()

            if canonical_id in connection_manager.room_subscriptions:
                targets.update(connection_manager.room_subscriptions[canonical_id])
            if room_id != canonical_id and room_id in connection_manager.room_subscriptions:
                targets.update(connection_manager.room_subscriptions[room_id])

            # Filter players based on their current room and mute status
            filtered_targets = []
            for player_id in targets:
                if player_id == sender_id:
                    continue  # Skip sender

                # Check if player is currently in the message's room
                if not self._is_player_in_room(player_id, room_id):
                    logger.debug(
                        "Filtered out player not in room",
                        player_id=player_id,
                        message_room_id=room_id,
                        channel=channel,
                    )
                    continue

                # Check if the receiving player has muted the sender
                if self._is_player_muted_by_receiver(player_id, sender_id):
                    logger.debug(
                        "Filtered out message due to mute",
                        receiver_id=player_id,
                        sender_id=sender_id,
                        channel=channel,
                    )
                    continue

                filtered_targets.append(player_id)

            # Send message only to filtered players
            for player_id in filtered_targets:
                await connection_manager.send_personal_message(player_id, chat_event)

            logger.info(
                "Room message broadcasted with server-side filtering",
                channel=channel,
                room_id=room_id,
                sender_id=sender_id,
                total_subscribers=len(targets),
                filtered_recipients=len(filtered_targets),
                excluded_count=len(targets) - len(filtered_targets) - 1,  # -1 for sender
            )

        except Exception as e:
            logger.error(
                "Error in server-side room message filtering",
                error=str(e),
                room_id=room_id,
                sender_id=sender_id,
                channel=channel,
            )

    def _is_player_in_room(self, player_id: str, room_id: str) -> bool:
        """
        Check if a player is currently in the specified room.

        Args:
            player_id: Player ID to check
            room_id: Room ID to check against

        Returns:
            bool: True if player is in the room, False otherwise
        """
        try:
            # Get player's current room from connection manager's online players
            if player_id in connection_manager.online_players:
                player_info = connection_manager.online_players[player_id]
                player_room_id = player_info.get("current_room_id")

                if player_room_id:
                    # Use canonical room ID for comparison
                    canonical_player_room = connection_manager._canonical_room_id(player_room_id) or player_room_id
                    canonical_message_room = connection_manager._canonical_room_id(room_id) or room_id

                    return canonical_player_room == canonical_message_room

            # Fallback: check persistence layer
            if connection_manager.persistence:
                player = connection_manager.persistence.get_player(player_id)
                if player and player.current_room_id:
                    canonical_player_room = (
                        connection_manager._canonical_room_id(player.current_room_id) or player.current_room_id
                    )
                    canonical_message_room = connection_manager._canonical_room_id(room_id) or room_id

                    return canonical_player_room == canonical_message_room

            return False

        except Exception as e:
            logger.error(
                "Error checking if player is in room",
                error=str(e),
                player_id=player_id,
                room_id=room_id,
            )
            return False

    def _is_player_muted_by_receiver(self, receiver_id: str, sender_id: str) -> bool:
        """
        Check if a receiving player has muted the sender.

        Args:
            receiver_id: Player ID of the message receiver
            sender_id: Player ID of the message sender

        Returns:
            bool: True if receiver has muted sender, False otherwise
        """
        try:
            # Import UserManager to check mute status
            from ..services.user_manager import UserManager

            user_manager = UserManager()

            # Load the receiver's mute data before checking
            user_manager.load_player_mutes(receiver_id)

            # Check if receiver has muted sender (personal mute)
            if user_manager.is_player_muted(receiver_id, sender_id):
                logger.debug(
                    "Player muted by receiver (personal mute)",
                    receiver_id=receiver_id,
                    sender_id=sender_id,
                )
                return True

            # Load global mutes and check if sender is globally muted by anyone
            # Only apply global mute if receiver is not an admin (admins can see globally muted players)
            if user_manager.is_player_muted_by_others(sender_id) and not user_manager.is_admin(receiver_id):
                logger.debug(
                    "Player muted by receiver (global mute)",
                    receiver_id=receiver_id,
                    sender_id=sender_id,
                )
                return True

            return False

        except Exception as e:
            logger.error(
                "Error checking mute status",
                error=str(e),
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            return False

    async def subscribe_to_room(self, room_id: str):
        """
        Subscribe to chat messages for a specific room.

        Args:
            room_id: Room ID to subscribe to
        """
        subjects = [
            f"chat.say.{room_id}",
            f"chat.local.{room_id}",
        ]

        for subject in subjects:
            if subject not in self.subscriptions:
                await self._subscribe_to_subject(subject)

    async def unsubscribe_from_room(self, room_id: str):
        """
        Unsubscribe from chat messages for a specific room.

        Args:
            room_id: Room ID to unsubscribe from
        """
        subjects = [
            f"chat.say.{room_id}",
            f"chat.local.{room_id}",
        ]

        for subject in subjects:
            if subject in self.subscriptions:
                await self._unsubscribe_from_subject(subject)

    def get_subscription_count(self) -> int:
        """Get the number of active subscriptions."""
        return len(self.subscriptions)

    def get_active_subjects(self) -> list[str]:
        """Get list of active subscription subjects."""
        return list(self.subscriptions.keys())

    async def subscribe_to_subzone(self, subzone: str) -> bool:
        """
        Subscribe to local channel messages for a specific sub-zone.

        Args:
            subzone: Sub-zone name to subscribe to

        Returns:
            True if subscribed successfully, False otherwise
        """
        try:
            subzone_subject = f"chat.local.subzone.{subzone}"

            # Check if already subscribed
            if subzone_subject in self.subscriptions:
                self.subzone_subscriptions[subzone] = self.subzone_subscriptions.get(subzone, 0) + 1
                logger.debug(
                    "Sub-zone subscription count increased", subzone=subzone, count=self.subzone_subscriptions[subzone]
                )
                return True

            # Subscribe to sub-zone subject
            success = await self._subscribe_to_subject(subzone_subject)
            if success:
                self.subzone_subscriptions[subzone] = 1
                logger.info("Subscribed to sub-zone local channel", subzone=subzone, subject=subzone_subject)
                return True
            else:
                logger.error("Failed to subscribe to sub-zone local channel", subzone=subzone, subject=subzone_subject)
                return False

        except Exception as e:
            logger.error("Error subscribing to sub-zone local channel", error=str(e), subzone=subzone)
            return False

    async def unsubscribe_from_subzone(self, subzone: str) -> bool:
        """
        Unsubscribe from local channel messages for a specific sub-zone.

        Args:
            subzone: Sub-zone name to unsubscribe from

        Returns:
            True if unsubscribed successfully, False otherwise
        """
        try:
            subzone_subject = f"chat.local.subzone.{subzone}"

            # Decrease subscription count
            if subzone in self.subzone_subscriptions:
                self.subzone_subscriptions[subzone] -= 1
                count = self.subzone_subscriptions[subzone]

                if count <= 0:
                    # No more subscribers, unsubscribe from NATS
                    success = await self._unsubscribe_from_subject(subzone_subject)
                    if success:
                        del self.subzone_subscriptions[subzone]
                        logger.info(
                            "Unsubscribed from sub-zone local channel", subzone=subzone, subject=subzone_subject
                        )
                        return True
                    else:
                        logger.error(
                            "Failed to unsubscribe from sub-zone local channel",
                            subzone=subzone,
                            subject=subzone_subject,
                        )
                        return False
                else:
                    logger.debug("Sub-zone subscription count decreased", subzone=subzone, count=count)
                    return True
            else:
                logger.warning("Not subscribed to sub-zone local channel", subzone=subzone)
                return False

        except Exception as e:
            logger.error("Error unsubscribing from sub-zone local channel", error=str(e), subzone=subzone)
            return False

    def track_player_subzone_subscription(self, player_id: str, subzone: str) -> None:
        """
        Track a player's sub-zone subscription for local channels.

        Args:
            player_id: Player ID
            subzone: Sub-zone name
        """
        try:
            # Update player's sub-zone subscription
            old_subzone = self.player_subzone_subscriptions.get(player_id)
            if old_subzone and old_subzone != subzone:
                # Player moved to different sub-zone, decrease count for old sub-zone
                if old_subzone in self.subzone_subscriptions:
                    self.subzone_subscriptions[old_subzone] = max(0, self.subzone_subscriptions[old_subzone] - 1)
                    logger.debug(
                        "Player moved to different sub-zone",
                        player_id=player_id,
                        old_subzone=old_subzone,
                        new_subzone=subzone,
                    )

            self.player_subzone_subscriptions[player_id] = subzone
            logger.debug("Tracked player sub-zone subscription", player_id=player_id, subzone=subzone)

        except Exception as e:
            logger.error(
                "Error tracking player sub-zone subscription", error=str(e), player_id=player_id, subzone=subzone
            )

    def get_players_in_subzone(self, subzone: str) -> list[str]:
        """
        Get list of players currently in a specific sub-zone.

        Args:
            subzone: Sub-zone name

        Returns:
            List of player IDs in the sub-zone
        """
        try:
            players = []
            for player_id, player_subzone in self.player_subzone_subscriptions.items():
                if player_subzone == subzone:
                    players.append(player_id)
            return players

        except Exception as e:
            logger.error("Error getting players in sub-zone", error=str(e), subzone=subzone)
            return []

    async def handle_player_movement(self, player_id: str, old_room_id: str, new_room_id: str) -> None:
        """
        Handle player movement between rooms and update sub-zone subscriptions.

        Args:
            player_id: Player ID
            old_room_id: Previous room ID
            new_room_id: New room ID
        """
        try:
            from ..utils.room_utils import extract_subzone_from_room_id

            old_subzone = extract_subzone_from_room_id(old_room_id) if old_room_id else None
            new_subzone = extract_subzone_from_room_id(new_room_id) if new_room_id else None

            if old_subzone != new_subzone:
                # Player moved to different sub-zone
                if old_subzone:
                    await self.unsubscribe_from_subzone(old_subzone)

                if new_subzone:
                    await self.subscribe_to_subzone(new_subzone)
                    self.track_player_subzone_subscription(player_id, new_subzone)

                logger.info(
                    "Player moved between sub-zones",
                    player_id=player_id,
                    old_subzone=old_subzone,
                    new_subzone=new_subzone,
                    old_room_id=old_room_id,
                    new_room_id=new_room_id,
                )
            else:
                # Player moved within same sub-zone, just update tracking
                if new_subzone:
                    self.track_player_subzone_subscription(player_id, new_subzone)

        except Exception as e:
            logger.error(
                "Error handling player movement",
                error=str(e),
                player_id=player_id,
                old_room_id=old_room_id,
                new_room_id=new_room_id,
            )

    def _format_message_content(self, channel: str, sender_name: str, content: str) -> str:
        """
        Format message content based on channel type and sender name.

        Args:
            channel: Channel type (say, local, emote, pose, global, party, whisper, system, admin)
            sender_name: Name of the message sender
            content: Raw message content

        Returns:
            Formatted message content with sender name
        """
        try:
            if channel == "say":
                return f"{sender_name} says: {content}"
            elif channel == "local":
                return f"{sender_name} (local): {content}"
            elif channel == "global":
                return f"{sender_name} (global): {content}"
            elif channel == "emote":
                return f"{sender_name} {content}"
            elif channel == "pose":
                return f"{sender_name} {content}"
            elif channel == "whisper":
                return f"{sender_name} whispers: {content}"
            elif channel == "system":
                return f"[SYSTEM] {content}"
            elif channel == "admin":
                return f"[ADMIN] {sender_name}: {content}"
            else:
                # Default format for unknown channels
                return f"{sender_name} ({channel}): {content}"

        except Exception as e:
            logger.error("Error formatting message content", error=str(e), channel=channel, sender_name=sender_name)
            return content  # Return original content if formatting fails

    async def cleanup_empty_subzone_subscriptions(self) -> None:
        """Clean up sub-zone subscriptions that have no active players."""
        try:
            subzones_to_cleanup = []

            for subzone, count in self.subzone_subscriptions.items():
                players_in_subzone = self.get_players_in_subzone(subzone)
                if not players_in_subzone and count <= 0:
                    subzones_to_cleanup.append(subzone)

            for subzone in subzones_to_cleanup:
                await self.unsubscribe_from_subzone(subzone)
                logger.info("Cleaned up empty sub-zone subscription", subzone=subzone)

        except Exception as e:
            logger.error("Error cleaning up empty sub-zone subscriptions", error=str(e))


# Global NATS message handler instance
nats_message_handler = None


def get_nats_message_handler(nats_service=None):
    """
    Get or create the global NATS message handler instance.

    Args:
        nats_service: NATS service instance (optional, for testing)

    Returns:
        NATSMessageHandler instance
    """
    global nats_message_handler
    if nats_message_handler is None and nats_service is not None:
        nats_message_handler = NATSMessageHandler(nats_service)
    return nats_message_handler
