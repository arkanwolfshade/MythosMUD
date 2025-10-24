"""
NATS message handler for MythosMUD chat system.

This module handles incoming NATS messages and broadcasts them to WebSocket clients.
It replaces the previous Redis message handler with NATS-based messaging.
"""

from datetime import UTC, datetime
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from ..middleware.metrics_collector import metrics_collector
from ..realtime.circuit_breaker import CircuitBreaker, CircuitBreakerOpen
from ..realtime.connection_manager import connection_manager
from ..realtime.dead_letter_queue import DeadLetterMessage, DeadLetterQueue
from ..realtime.envelope import build_event
from ..realtime.nats_retry_handler import NATSRetryHandler

logger = get_logger("communications.nats_message_handler")


class NATSMessageHandler:
    """
    Handler for processing NATS messages and broadcasting to WebSocket clients.

    This handler subscribes to NATS subjects for chat messages and broadcasts
    them to the appropriate WebSocket clients based on room and channel.
    """

    def __init__(self, nats_service):
        """
        Initialize NATS message handler with error boundaries.

        Args:
            nats_service: NATS service instance for subscribing to subjects

        AI: Initializes retry handler, DLQ, and circuit breaker for resilience.
        """
        logger.info("NATSMessageHandler __init__ called - ENHANCED LOGGING TEST")
        self.nats_service = nats_service
        self.subscriptions = {}

        # Sub-zone subscription tracking for local channels
        self.subzone_subscriptions = {}  # subzone -> subscription_count
        self.player_subzone_subscriptions = {}  # player_id -> subzone

        # NEW: Error boundary components (CRITICAL-4)
        # AI: These components work together to provide resilient message delivery
        from datetime import timedelta

        self.retry_handler = NATSRetryHandler(max_retries=3, base_delay=1.0, max_delay=30.0)
        self.dead_letter_queue = DeadLetterQueue()  # Uses environment-aware path
        self.circuit_breaker = CircuitBreaker(failure_threshold=5, timeout=timedelta(seconds=60), success_threshold=2)
        self.metrics = metrics_collector  # Shared global metrics instance

        logger.info(
            "NATS message handler initialized with error boundaries",
            retry_max_attempts=3,
            circuit_failure_threshold=5,
            # DLQ path is environment-aware via DeadLetterQueue initialization
        )

    async def start(self, enable_event_subscriptions: bool = True):
        """
        Start the NATS message handler and subscribe to subjects.

        Args:
            enable_event_subscriptions: Whether to subscribe to event subjects

        Returns:
            True if started successfully, False otherwise
        """
        logger.info("NATS message handler start() called - ENHANCED LOGGING TEST")
        try:
            logger.info("About to call _subscribe_to_chat_subjects()", debug=True)
            # Subscribe to chat message subjects
            await self._subscribe_to_chat_subjects()
            logger.info("Finished _subscribe_to_chat_subjects()", debug=True)

            # Subscribe to event subjects if enabled
            if enable_event_subscriptions:
                await self.subscribe_to_event_subjects()

            logger.info(
                "NATS message handler started successfully", event_subscriptions_enabled=enable_event_subscriptions
            )
            return True
        except Exception as e:
            logger.error("Failed to start NATS message handler", error=str(e))
            return False

    async def stop(self):
        """
        Stop the NATS message handler and unsubscribe from subjects.

        Returns:
            True if stopped successfully, False otherwise
        """
        try:
            # Unsubscribe from all subjects
            for subject in list(self.subscriptions.keys()):
                await self._unsubscribe_from_subject(subject)
            logger.info("NATS message handler stopped successfully")
            return True
        except Exception as e:
            logger.error("Error stopping NATS message handler", error=str(e))
            return False

    async def _subscribe_to_chat_subjects(self):
        """Subscribe to all chat-related NATS subjects."""
        subjects = [
            "chat.say.*",  # Say messages per room
            "chat.local.*",  # Local messages per room (for backward compatibility)
            "chat.local.subzone.*",  # Local messages per subzone
            "chat.emote.*",  # Emote messages per room
            "chat.pose.*",  # Pose messages per room
            "chat.global",  # Global messages
            "chat.party.*",  # Party messages per party
            "chat.whisper.*",  # Whisper messages per player
            "chat.system",  # System messages
            "chat.admin",  # Admin messages
            # Combat event subjects
            "combat.started.*",  # Combat started events per room
            "combat.ended.*",  # Combat ended events per room
            "combat.player_attacked.*",  # Player attack events per room
            "combat.npc_attacked.*",  # NPC attack events per room
            "combat.npc_took_damage.*",  # NPC damage events per room
            "combat.npc_died.*",  # NPC death events per room
        ]

        logger.info("Starting _subscribe_to_chat_subjects - subscribing to chat and combat subjects", debug=True)
        for subject in subjects:
            logger.info("About to subscribe to subject", subject=subject, debug=True)
            await self._subscribe_to_subject(subject)
        logger.info("Finished _subscribe_to_chat_subjects", debug=True)

    async def _subscribe_to_subject(self, subject: str):
        """Subscribe to a specific NATS subject."""
        try:
            logger.info("Attempting to subscribe to NATS subject", subject=subject, debug=True)
            success = await self.nats_service.subscribe(subject, self._handle_nats_message)
            if success:
                self.subscriptions[subject] = True
                logger.info("Successfully subscribed to NATS subject", subject=subject, debug=True)
                return True
            else:
                logger.error("Failed to subscribe to NATS subject", subject=subject, debug=True)
                return False
        except Exception as e:
            logger.error("Error subscribing to NATS subject", subject=subject, error=str(e), debug=True)
            return False

    async def _unsubscribe_from_subject(self, subject: str):
        """Unsubscribe from a specific NATS subject."""
        try:
            success = await self.nats_service.unsubscribe(subject)
            if success:
                if subject in self.subscriptions:
                    del self.subscriptions[subject]
                logger.info("Unsubscribed from NATS subject")
                return True
            else:
                logger.error("Failed to unsubscribe from NATS subject")
                return False
        except Exception as e:
            logger.error("Error unsubscribing from NATS subject", subject=subject, error=str(e))
            return False

    async def _handle_nats_message(self, message_data: dict[str, Any]):
        """
        Handle incoming NATS message with error boundaries.

        Wraps message processing with retry logic, circuit breaker,
        and dead letter queue for resilient delivery.

        Args:
            message_data: Message data from NATS

        AI: Entry point with full error boundary protection.
        """
        logger.info("_handle_nats_message called", message_data=message_data, debug=True)
        channel = message_data.get("channel", "unknown")
        message_id = message_data.get("message_id", "unknown")

        try:
            # Process through circuit breaker
            # AI: Circuit breaker fails fast when service is degraded
            await self.circuit_breaker.call(self._process_message_with_retry, message_data)

            # Record successful processing
            self.metrics.record_message_processed(channel)

        except CircuitBreakerOpen as e:
            # Circuit is open, add to DLQ immediately
            logger.error("Circuit breaker open, message added to DLQ", message_id=message_id, error=str(e))

            dlq_message = DeadLetterMessage(
                subject=channel,
                data=message_data,
                error=str(e),
                timestamp=datetime.now(UTC),
                retry_count=0,
                original_headers={"reason": "circuit_open"},
            )
            self.dead_letter_queue.enqueue(dlq_message)

            self.metrics.record_message_dlq(channel)

        except Exception as e:
            # Unexpected error - should not happen if retry logic works correctly
            logger.critical(
                "Unhandled error in message processing - this indicates a bug!",
                message_id=message_id,
                error=str(e),
                exc_info=True,
            )

            # Add to DLQ as last resort
            dlq_message = DeadLetterMessage(
                subject=channel,
                data=message_data,
                error=str(e),
                timestamp=datetime.now(UTC),
                retry_count=0,
                original_headers={"reason": "unhandled_exception"},
            )
            self.dead_letter_queue.enqueue(dlq_message)

            self.metrics.record_message_failed(channel, type(e).__name__)

    async def _process_message_with_retry(self, message_data: dict[str, Any]):
        """
        Process message with retry logic.

        Attempts message processing with exponential backoff on failures.
        If all retries fail, adds message to dead letter queue.

        Args:
            message_data: Message data to process

        Raises:
            Exception: If message processing fails after all retries

        AI: This method is called by circuit breaker, retries on transient failures.
        """
        channel = message_data.get("channel", "unknown")

        # Attempt processing with retry
        success, result = await self.retry_handler.retry_with_backoff(self._process_single_message, message_data)

        if not success:
            # All retries exhausted, add to DLQ
            logger.error(
                "Message failed after all retries, adding to DLQ",
                message_id=message_data.get("message_id"),
                error=str(result),
            )

            dlq_message = DeadLetterMessage(
                subject=channel,
                data=message_data,
                error=str(result),
                timestamp=datetime.now(UTC),
                retry_count=self.retry_handler.max_retries,
                original_headers={"channel": channel},
            )
            self.dead_letter_queue.enqueue(dlq_message)

            self.metrics.record_message_dlq(channel)
            self.metrics.record_message_failed(channel, type(result).__name__)

            # Re-raise to trigger circuit breaker
            raise result

    async def _process_single_message(self, message_data: dict[str, Any]):
        """
        Process a single NATS message (original logic, can raise exceptions).

        Args:
            message_data: Message data from NATS

        Raises:
            ValueError: If required fields are missing
            Exception: Any processing error

        AI: This is the core processing logic - exceptions trigger retries.
        """
        logger.debug("=== NATS MESSAGE HANDLER DEBUG: Processing message ===")
        logger.debug(f"Message data: {message_data}")
        logger.debug(f"Message type: {type(message_data)}")
        logger.debug(f"Message keys: {list(message_data.keys()) if isinstance(message_data, dict) else 'Not a dict'}")

        # Check if this is an event message
        if message_data.get("event_type"):
            await self._handle_event_message(message_data)
            return

        # Handle chat messages (existing logic)
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
        target_id = message_data.get("target_id")
        target_name = message_data.get("target_name")

        # For whisper messages, ensure target_player_id is set from target_id
        # (chat_service publishes "target_id" but broadcasting expects "target_player_id")
        if channel == "whisper" and target_id and not target_player_id:
            target_player_id = target_id

        # Validate required fields
        if not all([channel, sender_id, sender_name, content, message_id]):
            logger.warning("Invalid NATS message - missing required fields", message_data=message_data)
            raise ValueError("Missing required message fields")

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
                "target_id": target_id,
                "target_name": target_name,
            },
            player_id=str(sender_id),
        )

        # Broadcast based on channel type
        # AI: This can raise exceptions if broadcasting fails
        await self._broadcast_by_channel_type(channel, chat_event, room_id, party_id, target_player_id, sender_id)

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
        logger.debug(
            "=== BROADCAST FILTERING DEBUG: Starting room broadcast ===",
            room_id=room_id,
            sender_id=sender_id,
            channel=channel,
        )

        try:
            # Get all players subscribed to this room
            canonical_id = connection_manager._canonical_room_id(room_id) or room_id
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Room ID resolution ===",
                room_id=room_id,
                canonical_id=canonical_id,
                sender_id=sender_id,
                channel=channel,
            )

            targets: set[str] = set()

            if canonical_id in connection_manager.room_subscriptions:
                targets.update(connection_manager.room_subscriptions[canonical_id])
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Added canonical room subscribers ===",
                    room_id=room_id,
                    canonical_id=canonical_id,
                    canonical_subscribers=list(connection_manager.room_subscriptions[canonical_id]),
                    sender_id=sender_id,
                    channel=channel,
                )
            if room_id != canonical_id and room_id in connection_manager.room_subscriptions:
                targets.update(connection_manager.room_subscriptions[room_id])
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Added original room subscribers ===",
                    room_id=room_id,
                    original_subscribers=list(connection_manager.room_subscriptions[room_id]),
                    sender_id=sender_id,
                    channel=channel,
                )

            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Total targets before filtering ===",
                room_id=room_id,
                sender_id=sender_id,
                channel=channel,
                total_targets=list(targets),
                target_count=len(targets),
            )

            # Use the global UserManager instance for all mute checks to improve efficiency
            from ..services.user_manager import user_manager

            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Created UserManager instance ===",
                room_id=room_id,
                sender_id=sender_id,
                channel=channel,
            )

            # Pre-load mute data for all potential receivers to ensure consistency
            receiver_ids = [pid for pid in targets if pid != sender_id]
            if receiver_ids:
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Pre-loading mute data for receivers ===",
                    room_id=room_id,
                    sender_id=sender_id,
                    channel=channel,
                    receiver_count=len(receiver_ids),
                )
                for receiver_id in receiver_ids:
                    try:
                        user_manager.load_player_mutes(receiver_id)
                        logger.debug(
                            "=== BROADCAST FILTERING DEBUG: Loaded mute data for receiver ===",
                            room_id=room_id,
                            sender_id=sender_id,
                            channel=channel,
                            receiver_id=receiver_id,
                        )
                    except Exception as e:
                        logger.warning(
                            "Failed to load mute data for receiver",
                            room_id=room_id,
                            sender_id=sender_id,
                            channel=channel,
                            receiver_id=receiver_id,
                            error=str(e),
                        )

            # Filter players based on their current room and mute status
            filtered_targets = []
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
                    continue  # Skip sender

                # Check if player is currently in the message's room
                is_in_room = self._is_player_in_room(player_id, room_id)
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

                # Check if the receiving player has muted the sender using the shared UserManager instance
                is_muted = self._is_player_muted_by_receiver_with_user_manager(user_manager, player_id, sender_id)
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Mute check result ===",
                    room_id=room_id,
                    sender_id=sender_id,
                    target_player_id=player_id,
                    is_muted=is_muted,
                    channel=channel,
                )

                if is_muted:
                    logger.debug(
                        "Filtered out message due to mute",
                        receiver_id=player_id,
                        sender_id=sender_id,
                        channel=channel,
                    )
                    continue

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

            # Send message only to filtered players
            for player_id in filtered_targets:
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Sending message to player ===",
                    room_id=room_id,
                    sender_id=sender_id,
                    target_player_id=player_id,
                    channel=channel,
                )
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
        logger.debug(
            "=== MUTE FILTERING DEBUG: Starting mute check ===",
            receiver_id=receiver_id,
            sender_id=sender_id,
        )

        try:
            # Use the global UserManager instance to check mute status
            from ..services.user_manager import user_manager

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
                if hasattr(user_manager, "_player_mutes") and user_manager._player_mutes is not None:
                    available_mute_data = list(user_manager._player_mutes.keys())
                    logger.debug(
                        "=== MUTE FILTERING DEBUG: Available mute data ===",
                        receiver_id=receiver_id,
                        sender_id=sender_id,
                        available_mute_data=available_mute_data,
                    )

                    if receiver_id in user_manager._player_mutes:
                        receiver_mutes = list(user_manager._player_mutes[receiver_id].keys())
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
            except Exception as debug_error:
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
            is_receiver_admin = user_manager.is_admin(receiver_id)

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

            logger.debug(
                "=== MUTE FILTERING DEBUG: No mute found, allowing message ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            return False

        except Exception as e:
            logger.error(
                "Error checking mute status",
                error=str(e),
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            return False

    def _is_player_muted_by_receiver_with_user_manager(self, user_manager, receiver_id: str, sender_id: str) -> bool:
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
            # Load the receiver's mute data before checking (if not already loaded)
            mute_load_result = user_manager.load_player_mutes(receiver_id)
            logger.debug(
                "=== MUTE FILTERING DEBUG: Mute data load result ===",
                receiver_id=receiver_id,
                sender_id=sender_id,
                mute_load_result=mute_load_result,
            )

            # Check what mute data is available (only for debugging, not for logic)
            try:
                if hasattr(user_manager, "_player_mutes") and user_manager._player_mutes is not None:
                    available_mute_data = list(user_manager._player_mutes.keys())
                    logger.debug(
                        "=== MUTE FILTERING DEBUG: Available mute data ===",
                        receiver_id=receiver_id,
                        sender_id=sender_id,
                        available_mute_data=available_mute_data,
                    )

                    if receiver_id in user_manager._player_mutes:
                        receiver_mutes = list(user_manager._player_mutes[receiver_id].keys())
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
            except Exception as debug_error:
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
            is_receiver_admin = user_manager.is_admin(receiver_id)

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

            logger.debug(
                "Player not muted by receiver",
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            return False
        except Exception as e:
            logger.error(
                "Error checking mute status with provided UserManager",
                receiver_id=receiver_id,
                sender_id=sender_id,
                error=str(e),
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

    # Event subscription methods
    async def subscribe_to_event_subjects(self) -> bool:
        """
        Subscribe to all event-related NATS subjects.

        Returns:
            True if all subscriptions successful, False otherwise
        """
        try:
            event_subjects = [
                "events.player_entered.*",  # Player entered events per room
                "events.player_left.*",  # Player left events per room
                "events.game_tick",  # Global game tick events
                "combat.attack.*",  # Combat attack events per room
                "combat.npc_attacked.*",  # NPC attack events per room
                "combat.npc_action.*",  # NPC action events per room
                "combat.started.*",  # Combat started events per room
                "combat.ended.*",  # Combat ended events per room
                "combat.npc_died.*",  # NPC death events per room
            ]

            logger.debug("Subscribing to event subjects", subjects=event_subjects)

            success_count = 0
            for subject in event_subjects:
                success = await self._subscribe_to_subject(subject)
                if success:
                    success_count += 1

            if success_count == len(event_subjects):
                logger.info("Successfully subscribed to all event subjects", count=success_count)
                return True
            else:
                logger.warning(
                    "Partial success subscribing to event subjects", successful=success_count, total=len(event_subjects)
                )
                return success_count == len(event_subjects)

        except Exception as e:
            logger.error("Error subscribing to event subjects", error=str(e))
            return False

    async def unsubscribe_from_event_subjects(self) -> bool:
        """
        Unsubscribe from all event-related NATS subjects.

        Returns:
            True if all unsubscriptions successful, False otherwise
        """
        try:
            event_subjects = [
                "events.player_entered.*",
                "events.player_left.*",
                "events.game_tick",
                "combat.attack.*",
                "combat.npc_action.*",
                "combat.started.*",
                "combat.ended.*",
            ]

            logger.debug("Unsubscribing from event subjects", subjects=event_subjects)

            success_count = 0
            for subject in event_subjects:
                if subject in self.subscriptions:
                    success = await self._unsubscribe_from_subject(subject)
                    if success:
                        success_count += 1

            if success_count == len(event_subjects):
                logger.info("Successfully unsubscribed from all event subjects", count=success_count)
                return True
            else:
                logger.warning(
                    "Partial success unsubscribing from event subjects",
                    successful=success_count,
                    total=len(event_subjects),
                )
                return success_count == len(event_subjects)

        except Exception as e:
            logger.error("Error unsubscribing from event subjects", error=str(e))
            return False

    async def _handle_event_message(self, message_data: dict[str, Any]):
        """
        Handle incoming event messages from NATS.

        Args:
            message_data: Event message data from NATS
        """
        try:
            logger.info("Handling event message", message_data=message_data)

            # Extract event details
            event_type = message_data.get("event_type")
            data = message_data.get("data", {})

            # Debug logging for all messages
            logger.debug("NATS message received", event_type=event_type, data=data)

            # Validate required fields
            if not event_type or not data:
                logger.warning("Invalid event message - missing required fields", message_data=message_data)
                return

            # Route event based on type
            if event_type == "player_entered":
                await self._handle_player_entered_event(data)
            elif event_type == "player_left":
                await self._handle_player_left_event(data)
            elif event_type == "game_tick":
                await self._handle_game_tick_event(data)
            elif event_type == "combat_started":
                await self._handle_combat_started_event(data)
            elif event_type == "combat_ended":
                await self._handle_combat_ended_event(data)
            elif event_type == "player_attacked":
                await self._handle_player_attacked_event(data)
            elif event_type == "npc_attacked":
                logger.debug("NPC attacked event received in NATS handler", data=data)
                await self._handle_npc_attacked_event(data)
            elif event_type == "npc_took_damage":
                await self._handle_npc_took_damage_event(data)
            elif event_type == "npc_died":
                await self._handle_npc_died_event(data)
            else:
                logger.debug("Unknown event type received", event_type=event_type)

        except Exception as e:
            logger.error("Error handling event message", error=str(e), message_data=message_data)

    async def _handle_player_entered_event(self, data: dict[str, Any]):
        """
        Handle player_entered event.

        Args:
            data: Event data containing player and room information
        """
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Player entered event missing room_id", data=data)
                return

            # Import here to avoid circular imports
            from .connection_manager import connection_manager

            # Broadcast to room
            await connection_manager.broadcast_room_event("player_entered", room_id, data)

            logger.debug(
                "Player entered event broadcasted",
                room_id=room_id,
                player_id=data.get("player_id"),
            )

        except Exception as e:
            logger.error("Error handling player entered event", error=str(e), data=data)

    async def _handle_player_left_event(self, data: dict[str, Any]):
        """
        Handle player_left event.

        Args:
            data: Event data containing player and room information
        """
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Player left event missing room_id", data=data)
                return

            # Import here to avoid circular imports
            from .connection_manager import connection_manager

            # Broadcast to room
            await connection_manager.broadcast_room_event("player_left", room_id, data)

            logger.debug(
                "Player left event broadcasted",
                room_id=room_id,
                player_id=data.get("player_id"),
            )

        except Exception as e:
            logger.error("Error handling player left event", error=str(e), data=data)

    async def _handle_game_tick_event(self, data: dict[str, Any]):
        """
        Handle game_tick event.

        Args:
            data: Event data containing tick information
        """
        try:
            # Import here to avoid circular imports
            from .connection_manager import connection_manager

            # Broadcast globally
            await connection_manager.broadcast_global_event("game_tick", data)

            logger.debug(
                "Game tick event broadcasted",
                tick_number=data.get("tick_number"),
            )

        except Exception as e:
            logger.error("Error handling game tick event", error=str(e), data=data)

    def get_event_subscription_count(self) -> int:
        """
        Get the number of active event subscriptions.

        Returns:
            Number of active event subscriptions
        """
        event_subjects = [
            "events.player_entered.*",
            "events.player_left.*",
            "events.game_tick",
        ]

        count = 0
        for subject in event_subjects:
            if subject in self.subscriptions:
                count += 1

        return count

    def is_event_subscription_active(self, subject: str) -> bool:
        """
        Check if a specific event subscription is active.

        Args:
            subject: NATS subject to check

        Returns:
            True if subscription is active, False otherwise
        """
        return subject in self.subscriptions

    async def _handle_combat_started_event(self, data: dict[str, Any]):
        """Handle combat_started event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Combat started event missing room_id", data=data)
                return

            # Import here to avoid circular imports
            from .connection_manager import connection_manager

            # Broadcast to room
            await connection_manager.broadcast_room_event("combat_started", room_id, data)
            logger.debug("Combat started event broadcasted", room_id=room_id)

        except Exception as e:
            logger.error("Error handling combat started event", error=str(e), data=data)

    async def _handle_combat_ended_event(self, data: dict[str, Any]):
        """Handle combat_ended event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Combat ended event missing room_id", data=data)
                return

            # Import here to avoid circular imports
            from .connection_manager import connection_manager

            # Broadcast to room
            await connection_manager.broadcast_room_event("combat_ended", room_id, data)
            logger.debug("Combat ended event broadcasted", room_id=room_id)

        except Exception as e:
            logger.error("Error handling combat ended event", error=str(e), data=data)

    async def _handle_player_attacked_event(self, data: dict[str, Any]):
        """Handle player_attacked event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Player attacked event missing room_id", data=data)
                return

            # Import here to avoid circular imports
            from .connection_manager import connection_manager

            # Broadcast to room
            await connection_manager.broadcast_room_event("player_attacked", room_id, data)
            logger.debug("Player attacked event broadcasted", room_id=room_id)

        except Exception as e:
            logger.error("Error handling player attacked event", error=str(e), data=data)

    async def _handle_npc_attacked_event(self, data: dict[str, Any]):
        """Handle npc_attacked event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("NPC attacked event missing room_id", data=data)
                return

            # Import here to avoid circular imports
            from .connection_manager import connection_manager

            # Broadcast to room
            await connection_manager.broadcast_room_event("npc_attacked", room_id, data)
            logger.debug("NPC attacked event broadcasted", room_id=room_id)

        except Exception as e:
            logger.error("Error handling NPC attacked event", error=str(e), data=data)

    async def _handle_npc_took_damage_event(self, data: dict[str, Any]):
        """Handle npc_took_damage event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("NPC took damage event missing room_id", data=data)
                return

            # Import here to avoid circular imports
            from .connection_manager import connection_manager

            # Broadcast to room
            await connection_manager.broadcast_room_event("npc_took_damage", room_id, data)
            logger.debug("NPC took damage event broadcasted", room_id=room_id)

        except Exception as e:
            logger.error("Error handling NPC took damage event", error=str(e), data=data)

    async def _handle_npc_died_event(self, data: dict[str, Any]):
        """Handle npc_died event."""
        try:
            room_id = data.get("room_id")
            npc_id = data.get("npc_id")
            npc_name = data.get("npc_name")
            
            if not room_id:
                logger.warning("NPC died event missing room_id", data=data)
                return
                
            if not npc_id:
                logger.warning("NPC died event missing npc_id", data=data)
                return

            # Import here to avoid circular imports
            from .connection_manager import connection_manager
            from ..persistence import get_persistence

            # Remove NPC from room occupants on server side
            try:
                persistence = get_persistence()
                room = persistence.get_room(room_id)
                if room:
                    room.npc_left(npc_id)
                    logger.info("NPC removed from room occupants", npc_id=npc_id, npc_name=npc_name, room_id=room_id)
                else:
                    logger.warning("Room not found for NPC death", room_id=room_id, npc_id=npc_id)
            except Exception as e:
                logger.error("Error removing NPC from room", error=str(e), npc_id=npc_id, room_id=room_id)

            # Broadcast to room
            await connection_manager.broadcast_room_event("npc_died", room_id, data)
            logger.debug("NPC died event broadcasted", room_id=room_id)

        except Exception as e:
            logger.error("Error handling NPC died event", error=str(e), data=data)


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
    logger.info(
        "get_nats_message_handler called",
        nats_service_provided=nats_service is not None,
        global_handler_exists=nats_message_handler is not None,
    )
    if nats_message_handler is None and nats_service is not None:
        logger.info("Creating new NATSMessageHandler instance")
        nats_message_handler = NATSMessageHandler(nats_service)
    else:
        logger.info("Using existing global NATSMessageHandler instance")
    return nats_message_handler
