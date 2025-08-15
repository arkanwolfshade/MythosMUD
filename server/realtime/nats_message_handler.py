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
            "chat.local.*",  # Local messages per room
            "chat.global",  # Global messages
            "chat.party.*",  # Party messages per party
            "chat.whisper.*",  # Whisper messages per player
            "chat.system",  # System messages
            "chat.admin",  # Admin messages
        ]

        for subject in subjects:
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
            logger.debug("Received NATS message", message_data=message_data)

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

            # Create WebSocket event
            chat_event = build_event(
                "chat_message",
                {
                    "sender_id": str(sender_id),
                    "player_name": sender_name,
                    "channel": channel,
                    "message": content,
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
        Broadcast message based on channel type.

        Args:
            channel: Channel type (say, local, global, party, whisper, system, admin)
            chat_event: WebSocket event to broadcast
            room_id: Room ID for room-based channels
            party_id: Party ID for party-based channels
            target_player_id: Target player ID for whisper messages
            sender_id: Sender player ID
        """
        try:
            if channel in ["say", "local"]:
                # Room-based channels - implement server-side filtering
                if room_id:
                    await self._broadcast_to_room_with_filtering(room_id, chat_event, sender_id, channel)
                    logger.debug(
                        "Broadcasted room message with server-side filtering",
                        channel=channel,
                        room_id=room_id,
                        sender_id=sender_id,
                    )
                else:
                    logger.warning("Room-based message missing room_id", channel=channel)

            elif channel == "global":
                # Global channel - broadcast to all connected players
                await connection_manager.broadcast_to_all(chat_event, exclude_player=sender_id)
                logger.debug("Broadcasted global message", sender_id=sender_id)

            elif channel == "party":
                # Party channel - broadcast to party members
                if party_id:
                    # TODO: Implement party-based broadcasting when party system is available
                    logger.debug("Party message received", party_id=party_id, sender_id=sender_id)
                else:
                    logger.warning("Party message missing party_id")

            elif channel == "whisper":
                # Whisper channel - send to specific player
                if target_player_id:
                    await connection_manager.send_to_player(target_player_id, chat_event)
                    logger.debug(
                        "Sent whisper message",
                        sender_id=sender_id,
                        target_player_id=target_player_id,
                    )
                else:
                    logger.warning("Whisper message missing target_player_id")

            elif channel in ["system", "admin"]:
                # System/Admin channels - broadcast to all players
                await connection_manager.broadcast_to_all(chat_event, exclude_player=sender_id)
                logger.debug(f"Broadcasted {channel} message", sender_id=sender_id)

            else:
                logger.warning("Unknown channel type", channel=channel)

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
            channel: Channel type (say, local)
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
