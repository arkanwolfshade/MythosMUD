"""
NATS message handler for MythosMUD chat system.

This module handles incoming NATS messages and broadcasts them to WebSocket clients.
It replaces the previous Redis message handler with NATS-based messaging.
"""

import uuid
from collections.abc import Callable
from datetime import UTC, datetime
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any

from ..middleware.metrics_collector import metrics_collector
from ..realtime.circuit_breaker import CircuitBreaker, CircuitBreakerOpen
from ..realtime.dead_letter_queue import DeadLetterMessage, DeadLetterQueue
from ..realtime.envelope import build_event
from ..realtime.nats_retry_handler import NATSRetryHandler
from ..schemas.nats_messages import validate_message
from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger
from .connection_manager import resolve_connection_manager as _resolve_connection_manager
from .event_handlers import EventHandler
from .message_filtering import MessageFilteringHelper
from .message_formatters import format_message_content

logger = get_logger("communications.nats_message_handler")

if TYPE_CHECKING:
    from ..services.user_manager import UserManager


# Legacy compatibility scaffolding --------------------------------------------------
# Several older test suites still patch module-level attributes instead of using the
# container injector. We expose a placeholder object whose methods can be monkey
# patched while the runtime falls back to the live connection manager when present.


# Human reader: Centralize channel policy sets to keep mute filtering consistent with
# the teachings of the Arkham communications thesis.
# AI reader: Shared constants ensure mute/echo logic stays synchronized across helpers.
# Note: MUTE_SENSITIVE_CHANNELS and SUPPRESS_ECHO_MESSAGE_IDS are now in message_filtering.py
ECHO_SENDER_CHANNELS = frozenset({"say", "local", "emote", "pose"})


async def _not_configured_async(*_args: Any, **_kwargs: Any) -> None:
    """
    Placeholder coroutine used when no connection manager has been registered.

    Human reader: ensures legacy tests that patch individual methods still have a
    concrete attribute to override instead of encountering AttributeError.
    """
    raise RuntimeError("Connection manager has not been configured")


_LEGACY_CONNECTION_MANAGER_STUB = SimpleNamespace(
    broadcast_global=_not_configured_async,
    broadcast_global_event=_not_configured_async,
    broadcast_room_event=_not_configured_async,
    send_personal_message=_not_configured_async,
)


class NATSMessageHandler:
    """
    Handler for processing NATS messages and broadcasting to WebSocket clients.

    This handler subscribes to NATS subjects for chat messages and broadcasts
    them to the appropriate WebSocket clients based on room and channel.
    """

    def __init__(
        self,
        nats_service,
        subject_manager=None,
        connection_manager=None,
        user_manager: "UserManager | None" = None,
    ):
        """
        Initialize NATS message handler with error boundaries.

        Args:
            nats_service: NATS service instance for subscribing to subjects
            subject_manager: NATSSubjectManager instance for standardized subscription patterns
            connection_manager: ConnectionManager instance for broadcasting to WebSocket clients
            user_manager: UserManager instance used for mute lookups (defaults to global singleton)

        AI: Initializes retry handler, DLQ, and circuit breaker for resilience.
        AI Agent: connection_manager injected via constructor to eliminate global singleton dependency
        """
        logger.info("NATSMessageHandler __init__ called - ENHANCED LOGGING TEST")
        self.nats_service = nats_service
        self.subject_manager = subject_manager
        self._connection_manager = connection_manager  # AI Agent: Injected dependency, not global
        self.user_manager = user_manager
        self.subscriptions: dict[str, bool] = {}

        # Sub-zone subscription tracking for local channels
        self.subzone_subscriptions: dict[str, int] = {}  # subzone -> subscription_count
        self.player_subzone_subscriptions: dict[str, str] = {}  # player_id -> subzone

        # NEW: Error boundary components (CRITICAL-4)
        # AI: These components work together to provide resilient message delivery
        from datetime import timedelta

        self.retry_handler = NATSRetryHandler(max_retries=3, base_delay=1.0, max_delay=30.0)
        self.dead_letter_queue = DeadLetterQueue()  # Uses environment-aware path
        self.circuit_breaker = CircuitBreaker(failure_threshold=5, timeout=timedelta(seconds=60), success_threshold=2)
        self.metrics = metrics_collector  # Shared global metrics instance

        # Initialize helper classes for extracted functionality
        self._filtering_helper = MessageFilteringHelper(self.connection_manager, user_manager)
        self._event_handler = EventHandler(self.connection_manager)

        logger.info(
            "NATS message handler initialized with error boundaries",
            retry_max_attempts=3,
            circuit_failure_threshold=5,
            # DLQ path is environment-aware via DeadLetterQueue initialization
        )

    @property
    def connection_manager(self):
        # Prefer explicitly injected manager
        if self._connection_manager is not None:
            resolved = _resolve_connection_manager(self._connection_manager)
            if resolved is not None:
                return resolved

        # Try to resolve from container as fallback
        fallback = _resolve_connection_manager(None)
        if fallback is not None:
            return fallback

        # No concrete manager available; return the stub so patched methods remain usable
        return _LEGACY_CONNECTION_MANAGER_STUB

    @connection_manager.setter
    def connection_manager(self, value):
        self._connection_manager = value
        # Update filtering helper's connection_manager reference
        if hasattr(self, "_filtering_helper"):
            self._filtering_helper.connection_manager = value
        # Update event handler's connection_manager reference
        if hasattr(self, "_event_handler"):
            self._event_handler.connection_manager = value

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
        except (NATSError, RuntimeError) as e:
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
        except (NATSError, RuntimeError) as e:
            logger.error("Error stopping NATS message handler", error=str(e))
            return False

    async def _subscribe_to_chat_subjects(self):
        """
        Subscribe to all chat-related NATS subjects using NATSSubjectManager patterns.

        AI: All subscriptions now use standardized patterns from NATSSubjectManager.
            Legacy hardcoded patterns have been removed. Subject manager is required.
        """
        if not self.subject_manager:
            logger.error(
                "NATSSubjectManager not available - cannot subscribe to chat subjects",
                handler_initialized=hasattr(self, "nats_service"),
            )
            raise RuntimeError("NATSSubjectManager is required for chat subject subscriptions")

        # Use NATSSubjectManager for standardized subscription patterns
        await self._subscribe_to_standardized_chat_subjects()

    async def _subscribe_to_standardized_chat_subjects(self):
        """
        Subscribe to chat subjects using NATSSubjectManager patterns.

        This method retrieves subscription patterns from the subject manager
        to ensure consistency with the pattern definitions and reduces
        the risk of typos or mismatches between publishing and subscribing.

        AI: Uses subject manager to generate subscription patterns dynamically.
        AI: Includes legacy patterns for backward compatibility during migration.
        """
        logger.info(
            "Starting _subscribe_to_standardized_chat_subjects - subscribing to standardized chat subjects", debug=True
        )

        # Get standardized chat subscription patterns from subject manager
        subscription_patterns = self.subject_manager.get_chat_subscription_patterns()

        logger.info(
            "Subscribing to chat subjects using NATSSubjectManager patterns",
            pattern_count=len(subscription_patterns),
        )

        for pattern in subscription_patterns:
            logger.info("About to subscribe to pattern", pattern=pattern, debug=True)
            try:
                await self._subscribe_to_subject(pattern)
            except (NATSError, RuntimeError) as e:
                logger.error(
                    "Failed to subscribe to pattern, continuing with other patterns",
                    pattern=pattern,
                    error=str(e),
                    debug=True,
                )
                # Continue with other patterns even if one fails
                continue

        logger.info("Finished _subscribe_to_standardized_chat_subjects", debug=True)

    async def _subscribe_to_subject(self, subject: str):
        """
        Subscribe to a specific NATS subject.

        Args:
            subject: Subject string to subscribe to (built by caller using NATSSubjectManager)

        Raises:
            NATSSubscribeError: If subscription fails
        """
        try:
            logger.info("Attempting to subscribe to NATS subject", subject=subject, debug=True)
            # subscribe() now raises exceptions instead of returning False
            await self.nats_service.subscribe(subject, self._handle_nats_message)
            self.subscriptions[subject] = True
            logger.info("Successfully subscribed to NATS subject", subject=subject, debug=True)
        except (NATSError, RuntimeError) as e:
            logger.error("Error subscribing to NATS subject", subject=subject, error=str(e), debug=True)
            # Re-raise to propagate error
            raise

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
        except (NATSError, RuntimeError) as e:
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
            # Validate incoming message schema
            # Determine message type from channel or data structure
            message_type = "chat"
            if "event_type" in message_data or "event_data" in message_data:
                message_type = "event"
            # Validate message - fail if validation fails
            validate_message(message_data, message_type=message_type)

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

        except (NATSError, RuntimeError) as e:
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
        logger.debug(
            "NATS message received",
            message_data=message_data,
            message_type=type(message_data).__name__,
            message_keys=list(message_data.keys()) if isinstance(message_data, dict) else None,
        )

        # Check if this is an event message
        if message_data.get("event_type"):
            await self._event_handler.handle_event_message(message_data)
            return

        # Handle chat messages
        chat_fields = self._extract_chat_message_fields(message_data)
        self._validate_chat_message_fields(chat_fields, message_data)

        # Format message content based on channel type
        formatted_message = format_message_content(
            chat_fields["channel"], chat_fields["sender_name"], chat_fields["content"]
        )

        # Create WebSocket event
        chat_event = self._build_chat_event(chat_fields, formatted_message)

        # Convert IDs to UUIDs and broadcast
        sender_id_uuid, target_player_id_uuid = self._convert_ids_to_uuids(
            chat_fields["sender_id"], chat_fields["target_player_id"]
        )

        await self._broadcast_by_channel_type(
            chat_fields["channel"],
            chat_event,
            chat_fields["room_id"] or "",
            chat_fields["party_id"] or "",
            target_player_id_uuid,
            sender_id_uuid,
        )

    def _extract_chat_message_fields(self, message_data: dict[str, Any]) -> dict[str, Any]:
        """
        Extract and normalize chat message fields from message data.

        Args:
            message_data: Raw message data from NATS

        Returns:
            Dictionary containing extracted and normalized fields
        """
        channel = message_data.get("channel")
        target_player_id = message_data.get("target_player_id")
        target_id = message_data.get("target_id")

        # For whisper messages, ensure target_player_id is set from target_id
        # (chat_service publishes "target_id" but broadcasting expects "target_player_id")
        if channel == "whisper" and target_id and not target_player_id:
            target_player_id = target_id

        return {
            "channel": channel,
            "room_id": message_data.get("room_id"),
            "party_id": message_data.get("party_id"),
            "target_player_id": target_player_id,
            "sender_id": message_data.get("sender_id"),
            "sender_name": message_data.get("sender_name"),
            "content": message_data.get("content"),
            "message_id": message_data.get("message_id"),
            "timestamp": message_data.get("timestamp"),
            "target_id": target_id,
            "target_name": message_data.get("target_name"),
        }

    def _validate_chat_message_fields(self, chat_fields: dict[str, Any], message_data: dict[str, Any]) -> None:
        """
        Validate that all required chat message fields are present.

        Args:
            chat_fields: Extracted chat message fields
            message_data: Original message data for logging

        Raises:
            ValueError: If required fields are missing
        """
        channel = chat_fields["channel"]
        sender_id = chat_fields["sender_id"]
        sender_name = chat_fields["sender_name"]
        content = chat_fields["content"]
        message_id = chat_fields["message_id"]

        if not channel or not sender_id or not sender_name or not content or not message_id:
            logger.warning("Invalid NATS message - missing required fields", message_data=message_data)
            raise ValueError("Missing required message fields")

        # Type narrowing for mypy - validate fields
        if not isinstance(channel, str):
            raise TypeError("channel must be str")
        if not isinstance(sender_name, str):
            raise TypeError("sender_name must be str")
        if not isinstance(content, str):
            raise TypeError("content must be str")
        if not isinstance(sender_id, str):
            raise TypeError("sender_id must be str")

    def _build_chat_event(self, chat_fields: dict[str, Any], formatted_message: str) -> dict[str, Any]:
        """
        Build a WebSocket chat event from chat fields and formatted message.

        Args:
            chat_fields: Extracted chat message fields
            formatted_message: Formatted message content

        Returns:
            WebSocket chat event dictionary
        """
        event_data = {
            "sender_id": str(chat_fields["sender_id"]),
            "player_name": chat_fields["sender_name"],
            "channel": chat_fields["channel"],
            "message": formatted_message,
            "message_id": chat_fields["message_id"],
            "timestamp": chat_fields["timestamp"],
            "target_id": chat_fields["target_id"],
            "target_name": chat_fields["target_name"],
            # Store original content for communication dampening processing
            "original_content": chat_fields["content"],
        }
        return build_event(
            "chat_message",
            event_data,
            player_id=str(chat_fields["sender_id"]),
        )

    def _convert_ids_to_uuids(self, sender_id: str, target_player_id: str | None) -> tuple[uuid.UUID, uuid.UUID | None]:
        """
        Convert string IDs to UUIDs for broadcasting.

        Args:
            sender_id: Sender player ID (string or UUID)
            target_player_id: Target player ID (string, UUID, or None)

        Returns:
            Tuple of (sender_id_uuid, target_player_id_uuid)
        """
        sender_id_uuid = uuid.UUID(sender_id) if isinstance(sender_id, str) else sender_id
        target_player_id_uuid: uuid.UUID | None = None
        if target_player_id:
            target_player_id_uuid = (
                uuid.UUID(target_player_id) if isinstance(target_player_id, str) else target_player_id
            )
        return sender_id_uuid, target_player_id_uuid

    async def _broadcast_by_channel_type(
        self,
        channel: str,
        chat_event: dict,
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
    ):
        """
        Broadcast message based on channel type using strategy pattern.

        Args:
            channel: Channel type (say, local, emote, pose, global, party, whisper, system, admin)
            chat_event: WebSocket event to broadcast
            room_id: Room ID for room-based channels
            party_id: Party ID for party-based channels
            target_player_id: Target player ID for whisper messages (UUID or None)
            sender_id: Sender player ID (UUID)
        """
        try:
            # Import here to avoid circular imports
            from .channel_broadcasting_strategies import channel_strategy_factory

            # Get strategy for channel type and execute broadcast
            strategy = channel_strategy_factory.get_strategy(channel)
            await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, self)

        except (NATSError, RuntimeError, ValueError, AttributeError, TypeError) as e:
            logger.error(
                "Error broadcasting message by channel type",
                error=str(e),
                channel=channel,
                room_id=room_id,
                party_id=party_id,
                target_player_id=target_player_id,
            )

    def _collect_room_targets(self, room_id: str) -> set[str]:
        """Collect all players subscribed to a room (canonical and original IDs)."""
        return self._filtering_helper.collect_room_targets(room_id)

    async def _preload_receiver_mute_data(self, user_manager: "UserManager", targets: set[str], sender_id: str) -> None:
        """Pre-load mute data for all potential receivers."""
        await self._filtering_helper.preload_receiver_mute_data(user_manager, targets, sender_id)

    def _extract_chat_event_info(self, chat_event: dict) -> tuple[str | None, dict, str | None, bool]:
        """Extract information from chat event."""
        return self._filtering_helper.extract_chat_event_info(chat_event)

    def _should_apply_mute_check(self, channel: str, message_id: str | None) -> bool:
        """Determine if mute check should be applied for a channel."""
        return self._filtering_helper.should_apply_mute_check(channel, message_id)

    async def _check_player_mute_status(
        self, user_manager: "UserManager", player_id: str, sender_id: str, channel: str, chat_event_data: dict
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
        user_manager: "UserManager",
        chat_event_data: dict,
    ) -> list[str]:
        """Filter target players based on room location and mute status."""
        return await self._filtering_helper.filter_target_players(
            targets, sender_id, room_id, channel, message_id, user_manager, chat_event_data, self
        )

    async def _send_messages_to_players(
        self, filtered_targets: list[str], chat_event: dict, room_id: str, sender_id: str, channel: str
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
        chat_event: dict,
        room_id: str,
        channel: str,
        chat_event_data: dict,
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

    def _get_user_manager(self) -> "UserManager":
        """Return the user manager instance to use for mute lookups."""
        if self.user_manager is not None:
            return self.user_manager

        from ..services.user_manager import user_manager as global_user_manager

        return global_user_manager

    def _format_message_for_receiver(self, channel: str, sender_name: str, content: str) -> str:
        """
        Format message content for a receiver (after dampening applied).

        Args:
            channel: Channel type
            sender_name: Name of the message sender
            content: Message content (may have been modified by dampening)

        Returns:
            Formatted message content with sender name
        """
        return format_message_content(channel, sender_name, content)

    async def _apply_dampening_and_send_message(
        self, chat_event: dict, sender_id: str, receiver_id: str, channel: str
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
                except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Lucidity tier retrieval errors unpredictable, optional metadata
                    logger.debug(
                        "Error getting player lucidity tier",
                        player_id=player_id,
                        error=str(e),
                        error_type=type(e).__name__,
                    )
                    return "lucid"

        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Session creation errors unpredictable, must return fallback
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
        self, user_manager, receiver_id: str, sender_id: str
    ) -> bool:
        """Check if a receiving player has muted the sender using a provided UserManager instance."""
        return await self._filtering_helper.is_player_muted_by_receiver_with_user_manager(
            user_manager, receiver_id, sender_id
        )

    async def subscribe_to_room(self, room_id: str):
        """
        Subscribe to chat messages for a specific room.

        Args:
            room_id: Room ID to subscribe to

        Raises:
            RuntimeError: If subject manager is not available

        AI: Uses subject manager to build standardized subscription subjects.
            Subject manager is required - no legacy fallback.
        """
        if not self.subject_manager:
            raise RuntimeError("NATSSubjectManager is required for room subscriptions")

        # Build subjects using standardized patterns
        subjects = [
            self.subject_manager.build_subject("chat_say_room", room_id=room_id),
        ]

        for subject in subjects:
            if subject not in self.subscriptions:
                await self._subscribe_to_subject(subject)

    async def unsubscribe_from_room(self, room_id: str):
        """
        Unsubscribe from chat messages for a specific room.

        Args:
            room_id: Room ID to unsubscribe from

        Raises:
            RuntimeError: If subject manager is not available

        AI: Uses subject manager to build standardized unsubscription subjects.
            Subject manager is required - no legacy fallback.
        """
        if not self.subject_manager:
            raise RuntimeError("NATSSubjectManager is required for room unsubscriptions")

        # Build subjects using standardized patterns
        subjects = [
            self.subject_manager.build_subject("chat_say_room", room_id=room_id),
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
            # Build subject using standardized pattern - subject manager required
            if not self.subject_manager:
                raise RuntimeError("NATSSubjectManager is required for subzone subscriptions")
            subzone_subject = self.subject_manager.build_subject("chat_local_subzone", subzone=subzone)

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

        except NATSError as e:
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
            # Build subject using standardized pattern - subject manager required
            if not self.subject_manager:
                raise RuntimeError("NATSSubjectManager is required for subzone unsubscriptions")
            subzone_subject = self.subject_manager.build_subject("chat_local_subzone", subzone=subzone)

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

        except NATSError as e:
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

        except NATSError as e:
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

        except NATSError as e:
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

        except NATSError as e:
            logger.error(
                "Error handling player movement",
                error=str(e),
                player_id=player_id,
                old_room_id=old_room_id,
                new_room_id=new_room_id,
            )

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

        except NATSError as e:
            logger.error("Error cleaning up empty sub-zone subscriptions", error=str(e))

    # Event subscription methods
    async def subscribe_to_event_subjects(self) -> bool:
        """
        Subscribe to all event-related NATS subjects using standardized patterns.

        Raises:
            RuntimeError: If subject manager is not available

        AI: Uses subject manager to generate event subscription patterns dynamically.
            Subject manager is required - no legacy fallback.
        """
        if not self.subject_manager:
            raise RuntimeError("NATSSubjectManager is required for event subscriptions")

        try:
            # Use standardized event subscription patterns from subject manager
            event_subjects = self.subject_manager.get_event_subscription_patterns()
            logger.info(
                "Subscribing to event subjects using standardized patterns",
                pattern_count=len(event_subjects),
            )

            logger.debug("Event subscription patterns", subjects=event_subjects)

            success_count = 0
            for subject in event_subjects:
                try:
                    await self._subscribe_to_subject(subject)
                    success_count += 1
                except NATSError as e:
                    logger.error(
                        "Failed to subscribe to event subject",
                        subject=subject,
                        error=str(e),
                    )

            if success_count == len(event_subjects):
                logger.info("Successfully subscribed to all event subjects", count=success_count)
                return True
            else:
                logger.warning(
                    "Partial success subscribing to event subjects", successful=success_count, total=len(event_subjects)
                )
                return success_count == len(event_subjects)

        except NATSError as e:
            logger.error("Error subscribing to event subjects", error=str(e))
            return False

    async def unsubscribe_from_event_subjects(self) -> bool:
        """
        Unsubscribe from all event-related NATS subjects using standardized patterns.

        Raises:
            RuntimeError: If subject manager is not available

        Returns:
            True if all unsubscriptions successful, False otherwise

        AI: Uses subject manager to get event subscription patterns dynamically.
            Subject manager is required - no legacy fallback.
        """
        if not self.subject_manager:
            raise RuntimeError("NATSSubjectManager is required for event unsubscriptions")

        try:
            # Use standardized event subscription patterns from subject manager
            event_subjects = self.subject_manager.get_event_subscription_patterns()
            logger.info(
                "Unsubscribing from event subjects using standardized patterns",
                pattern_count=len(event_subjects),
            )

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

        except NATSError as e:
            logger.error("Error unsubscribing from event subjects", error=str(e))
            return False

    def _get_event_handler_map(self) -> dict[str, Callable[[dict[str, Any]], Any]]:
        """Get mapping of event types to their handler methods."""
        return self._event_handler.get_event_handler_map()

    def _validate_event_message(self, event_type: str | None, data: dict[str, Any]) -> bool:
        """Validate that event message has required fields."""
        return self._event_handler.validate_event_message(event_type, data)

    async def _handle_event_message(self, message_data: dict[str, Any]):
        """Handle incoming event messages from NATS."""
        await self._event_handler.handle_event_message(message_data)

    async def _handle_player_entered_event(self, data: dict[str, Any]):
        """Handle player_entered event."""
        await self._event_handler.handle_player_entered_event(data)

    async def _handle_player_left_event(self, data: dict[str, Any]):
        """Handle player_left event."""
        await self._event_handler.handle_player_left_event(data)

    async def _handle_game_tick_event(self, data: dict[str, Any]):
        """Handle game_tick event."""
        await self._event_handler.handle_game_tick_event(data)

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
        await self._event_handler.handle_combat_started_event(data)

    async def _handle_combat_ended_event(self, data: dict[str, Any]):
        """Handle combat_ended event."""
        await self._event_handler.handle_combat_ended_event(data)

    async def _handle_player_attacked_event(self, data: dict[str, Any]):
        """Handle player_attacked event."""
        await self._event_handler.handle_player_attacked_event(data)

    async def _handle_npc_attacked_event(self, data: dict[str, Any]):
        """Handle npc_attacked event."""
        await self._event_handler.handle_npc_attacked_event(data)

    async def _handle_npc_took_damage_event(self, data: dict[str, Any]):
        """Handle npc_took_damage event."""
        await self._event_handler.handle_npc_took_damage_event(data)

    async def _handle_npc_died_event(self, data: dict[str, Any]):
        """Handle npc_died event - NATS to EventBus bridge pattern."""
        await self._event_handler.handle_npc_died_event(data)


# AI Agent: Global singleton removed - use ApplicationContainer.nats_message_handler instead
# Migration complete: All code now uses dependency injection via container
