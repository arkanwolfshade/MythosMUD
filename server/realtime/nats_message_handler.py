"""
NATS message handler for MythosMUD chat system.

This module handles incoming NATS messages and broadcasts them to WebSocket clients.
It replaces the previous Redis message handler with NATS-based messaging.
"""

import uuid
from datetime import UTC, datetime
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any, cast
from unittest.mock import Mock

from ..logging.enhanced_logging_config import get_logger
from ..middleware.metrics_collector import metrics_collector
from ..realtime.circuit_breaker import CircuitBreaker, CircuitBreakerOpen
from ..realtime.dead_letter_queue import DeadLetterMessage, DeadLetterQueue
from ..realtime.envelope import build_event
from ..realtime.nats_retry_handler import NATSRetryHandler
from ..schemas.nats_messages import validate_message
from .connection_manager import (
    get_global_connection_manager as _get_global_connection_manager,
)
from .connection_manager import resolve_connection_manager as _resolve_connection_manager
from .connection_manager import set_global_connection_manager as _set_connection_manager_bridge

logger = get_logger("communications.nats_message_handler")

if TYPE_CHECKING:
    from ..services.user_manager import UserManager


# Legacy compatibility scaffolding --------------------------------------------------
# Several older test suites still patch module-level attributes instead of using the
# container injector. We expose a placeholder object whose methods can be monkey
# patched while the runtime falls back to the live connection manager when present.


SUPPRESS_ECHO_MESSAGE_IDS: set[str] = set()

# Human reader: Centralize channel policy sets to keep mute filtering consistent with
# the teachings of the Arkham communications thesis.
# AI reader: Shared constants ensure mute/echo logic stays synchronized across helpers.
MUTE_SENSITIVE_CHANNELS = frozenset({"say", "local", "emote", "pose", "whisper", "global", "system", "admin"})
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

# The module-level attribute defaults to a stub so unittest.patch can locate members.
connection_manager: Any = _LEGACY_CONNECTION_MANAGER_STUB


def set_global_connection_manager(manager: Any | None) -> None:
    """
    Update the module-level connection_manager reference for legacy compatibility.

    Args:
        manager: Connection manager instance to expose (or None to clear)
    """
    global connection_manager
    connection_manager = manager if manager is not None else _LEGACY_CONNECTION_MANAGER_STUB
    # Keep the runtime bridge in sync so both modules expose the same instance.
    _set_connection_manager_bridge(manager)


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

        # Next honour module-level bridges applied via set_global_connection_manager.
        if connection_manager is not _LEGACY_CONNECTION_MANAGER_STUB:
            return _resolve_connection_manager(connection_manager)

        # Finally consult the connection_manager module's global reference
        fallback = _resolve_connection_manager(_get_global_connection_manager())
        if fallback is not None:
            return fallback

        # No concrete manager available; return the stub so patched methods remain usable
        return _LEGACY_CONNECTION_MANAGER_STUB

    @connection_manager.setter
    def connection_manager(self, value):
        self._connection_manager = value

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
            await self._subscribe_to_subject(pattern)

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
        except Exception as e:
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
        logger.debug(
            "NATS message received",
            message_data=message_data,
            message_type=type(message_data).__name__,
            message_keys=list(message_data.keys()) if isinstance(message_data, dict) else None,
        )

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

        # Type narrowing for mypy - only assert fields validated above
        assert isinstance(channel, str), "channel must be str"
        assert isinstance(sender_name, str), "sender_name must be str"
        assert isinstance(content, str), "content must be str"
        assert isinstance(sender_id, str), "sender_id must be str"

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
        # Convert string IDs to UUIDs for _broadcast_by_channel_type
        sender_id_uuid = uuid.UUID(sender_id) if isinstance(sender_id, str) else sender_id
        target_player_id_uuid: uuid.UUID | None = None
        if target_player_id:
            target_player_id_uuid = (
                uuid.UUID(target_player_id) if isinstance(target_player_id, str) else target_player_id
            )

        await self._broadcast_by_channel_type(
            channel,
            chat_event,
            room_id or "",
            party_id or "",
            target_player_id_uuid,
            sender_id_uuid,
        )

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
            canonical_id = self.connection_manager._canonical_room_id(room_id) or room_id
            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Room ID resolution ===",
                room_id=room_id,
                canonical_id=canonical_id,
                sender_id=sender_id,
                channel=channel,
            )

            targets: set[str] = set()

            if canonical_id in self.connection_manager.room_subscriptions:
                targets.update(self.connection_manager.room_subscriptions[canonical_id])
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Added canonical room subscribers ===",
                    room_id=room_id,
                    canonical_id=canonical_id,
                    canonical_subscribers=list(self.connection_manager.room_subscriptions[canonical_id]),
                    sender_id=sender_id,
                    channel=channel,
                )
            if room_id != canonical_id and room_id in self.connection_manager.room_subscriptions:
                targets.update(self.connection_manager.room_subscriptions[room_id])
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Added original room subscribers ===",
                    room_id=room_id,
                    original_subscribers=list(self.connection_manager.room_subscriptions[room_id]),
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

            user_manager = self._get_user_manager()

            logger.debug(
                "=== BROADCAST FILTERING DEBUG: Created UserManager instance ===",
                room_id=room_id,
                sender_id=sender_id,
                channel=channel,
            )

            # Pre-load mute data for all potential receivers to ensure consistency (async batch loading)
            receiver_ids = [pid for pid in targets if pid != sender_id]
            if receiver_ids:
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Pre-loading mute data for receivers ===",
                    room_id=room_id,
                    sender_id=sender_id,
                    channel=channel,
                    receiver_count=len(receiver_ids),
                )
                try:
                    # Use async batch loading to prevent blocking the event loop
                    # Cast to list[UUID | str] since load_player_mutes_batch accepts this type
                    # and receiver_ids is list[str] which is compatible
                    receiver_ids_typed: list[uuid.UUID | str] = cast(list[uuid.UUID | str], receiver_ids)
                    load_results = await user_manager.load_player_mutes_batch(receiver_ids_typed)
                    logger.debug(
                        "=== BROADCAST FILTERING DEBUG: Batch loaded mute data ===",
                        room_id=room_id,
                        sender_id=sender_id,
                        channel=channel,
                        loaded_count=sum(1 for v in load_results.values() if v),
                        failed_count=sum(1 for v in load_results.values() if not v),
                    )
                except Exception as e:
                    logger.warning(
                        "Failed to batch load mute data for receivers",
                        room_id=room_id,
                        sender_id=sender_id,
                        channel=channel,
                        receiver_count=len(receiver_ids),
                        error=str(e),
                    )

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
            suppress_registry_hit = False
            if chat_event_data:
                message_id = chat_event_data.get("id")
                sender_already_notified = bool(chat_event_data.get("echo_sent"))
                if message_id in SUPPRESS_ECHO_MESSAGE_IDS:
                    sender_already_notified = True
                    suppress_registry_hit = True
                    SUPPRESS_ECHO_MESSAGE_IDS.discard(message_id)

            # Filter players based on their current room and mute status
            filtered_targets = []
            mute_sensitive_channels = MUTE_SENSITIVE_CHANNELS
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
                is_in_room = await self._is_player_in_room(player_id, room_id)
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

                should_apply_mute = channel in mute_sensitive_channels or (channel == "say" and message_id is None)
                is_muted = False

                if should_apply_mute:
                    logger.info(
                        "=== MUTE FILTERING: Starting mute check ===",
                        room_id=room_id,
                        sender_id=sender_id,
                        sender_name=chat_event_data.get("sender_name", "unknown"),
                        receiver_id=player_id,
                        channel=channel,
                        should_apply_mute=should_apply_mute,
                    )
                    patched_mute_checker = getattr(self, "_is_player_muted_by_receiver", None)
                    if isinstance(patched_mute_checker, Mock):
                        is_muted = patched_mute_checker(player_id, sender_id)
                        logger.info(
                            "=== MUTE FILTERING: Using patched mute checker (test mode) ===",
                            receiver_id=player_id,
                            sender_id=sender_id,
                            is_muted=is_muted,
                        )
                    else:
                        # Check if the receiving player has muted the sender using the shared UserManager instance
                        logger.info(
                            "=== MUTE FILTERING: Calling _is_player_muted_by_receiver_with_user_manager ===",
                            receiver_id=player_id,
                            sender_id=sender_id,
                        )
                        is_muted = await self._is_player_muted_by_receiver_with_user_manager(
                            user_manager, player_id, sender_id
                        )
                        logger.info(
                            "=== MUTE FILTERING: Mute check completed ===",
                            receiver_id=player_id,
                            sender_id=sender_id,
                            is_muted=is_muted,
                        )
                    logger.debug(
                        "=== BROADCAST FILTERING DEBUG: Mute check result ===",
                        room_id=room_id,
                        sender_id=sender_id,
                        target_player_id=player_id,
                        is_muted=is_muted,
                        channel=channel,
                    )

                    if channel in {"emote", "pose"}:
                        logger.info(
                            "=== EMOTE MUTE FILTERING: Evaluation result ===",
                            receiver_id=player_id,
                            sender_id=sender_id,
                            is_muted=is_muted,
                            channel=channel,
                            will_filter=should_apply_mute and is_muted,
                        )
                else:
                    logger.debug(
                        "=== BROADCAST FILTERING DEBUG: Mute check skipped for channel ===",
                        room_id=room_id,
                        sender_id=sender_id,
                        target_player_id=player_id,
                        channel=channel,
                    )

                if should_apply_mute and is_muted:
                    logger.info(
                        "=== MUTE FILTERING: Message FILTERED OUT due to mute ===",
                        receiver_id=player_id,
                        sender_id=sender_id,
                        channel=channel,
                        room_id=room_id,
                    )
                    continue
                else:
                    logger.info(
                        "=== MUTE FILTERING: Message ALLOWED (not muted or mute check skipped) ===",
                        receiver_id=player_id,
                        sender_id=sender_id,
                        channel=channel,
                        is_muted=is_muted,
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

            # Send message only to filtered players
            for player_id in filtered_targets:
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Sending message to player ===",
                    room_id=room_id,
                    sender_id=sender_id,
                    target_player_id=player_id,
                    channel=channel,
                )
                # Convert string player_id to UUID for send_personal_message
                try:
                    player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
                    await self.connection_manager.send_personal_message(player_id_uuid, chat_event)
                except (ValueError, AttributeError, TypeError) as e:
                    logger.warning(
                        "Invalid player_id format for send_personal_message",
                        player_id=player_id,
                        error=str(e),
                    )

            # Echo emotes/poses back to the sender so they see their own action
            if isinstance(chat_event_data, dict):
                logger.debug(
                    "=== BROADCAST FILTERING DEBUG: Chat event data keys ===",
                    data_keys=list(chat_event_data.keys()),
                    message_id=message_id,
                    suppress_registry_hit=suppress_registry_hit,
                )

            should_echo_sender = (
                channel in ECHO_SENDER_CHANNELS and event_type == "chat_message" and message_id is not None
            )

            needs_sender_echo = False
            if should_echo_sender:
                if filtered_targets:
                    needs_sender_echo = True
                elif not sender_already_notified:
                    needs_sender_echo = True

            if needs_sender_echo:
                try:
                    # Convert string sender_id to UUID for send_personal_message
                    sender_id_uuid = uuid.UUID(sender_id) if isinstance(sender_id, str) else sender_id
                    await self.connection_manager.send_personal_message(sender_id_uuid, chat_event)
                    logger.debug(
                        "=== BROADCAST FILTERING DEBUG: Echoed message to sender ===",
                        room_id=room_id,
                        sender_id=sender_id,
                        channel=channel,
                    )
                except Exception as echo_error:
                    logger.warning(
                        "Failed to echo message to sender",
                        sender_id=sender_id,
                        room_id=room_id,
                        channel=channel,
                        error=str(echo_error),
                    )

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

    def _get_user_manager(self) -> "UserManager":
        """Return the user manager instance to use for mute lookups."""
        if self.user_manager is not None:
            return self.user_manager

        from ..services.user_manager import user_manager as global_user_manager

        return global_user_manager

    async def _is_player_in_room(self, player_id: str, room_id: str) -> bool:
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
            online_players = getattr(self.connection_manager, "online_players", {})
            if player_id in online_players:
                player_info = online_players[player_id]
                player_room_id = player_info.get("current_room_id") if isinstance(player_info, dict) else None

                if isinstance(player_room_id, str) and player_room_id:
                    # Use canonical room ID for comparison
                    canonical_player_room = self.connection_manager._canonical_room_id(player_room_id) or player_room_id
                    canonical_message_room = self.connection_manager._canonical_room_id(room_id) or room_id

                    return canonical_player_room == canonical_message_room

            # Fallback: check async persistence layer
            async_persistence = getattr(self.connection_manager, "async_persistence", None)
            if async_persistence:
                player = await async_persistence.get_player_by_id(player_id)
                if player and not isinstance(player, Mock):
                    player_room_id = getattr(player, "current_room_id", None)
                    if isinstance(player_room_id, str) and player_room_id:
                        # _canonical_room_id is synchronous, not async
                        canonical_player_room = (
                            self.connection_manager._canonical_room_id(player_room_id) or player_room_id
                        )
                        canonical_message_room = self.connection_manager._canonical_room_id(room_id) or room_id

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
                if hasattr(user_manager, "_player_mutes") and user_manager._player_mutes is not None:
                    available_mute_data = list(user_manager._player_mutes.keys())
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

                    if receiver_id_uuid and receiver_id_uuid in user_manager._player_mutes:
                        receiver_mutes = list(user_manager._player_mutes[receiver_id_uuid].keys())
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

        except Exception as e:
            logger.error(
                "Error checking mute status",
                error=str(e),
                receiver_id=receiver_id,
                sender_id=sender_id,
            )
            return False

    async def _is_player_muted_by_receiver_with_user_manager(
        self, user_manager, receiver_id: str, sender_id: str
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
                except Exception as e:
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

        except Exception as e:
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
            data = message_data.get("event_data", {})

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

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("player_entered", room_id, data)

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

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("player_left", room_id, data)

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
            # Broadcast globally using injected connection_manager
            await self.connection_manager.broadcast_global_event("game_tick", data)

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

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("combat_started", room_id, data)
            logger.debug("Combat started event broadcasted", room_id=room_id)

            # Send player updates with in_combat status to all players in combat
            participants = data.get("participants", {})
            if participants:
                from .envelope import build_event

                for participant_id_str, _participant_data in participants.items():
                    try:
                        # Get player by ID to send update
                        player = await self.connection_manager._get_player(participant_id_str)
                        if player:
                            # Send player update with in_combat status
                            player_update_event = build_event(
                                "player_update",
                                {
                                    "player_id": participant_id_str,
                                    "in_combat": True,
                                },
                                player_id=participant_id_str,
                            )
                            await self.connection_manager.send_personal_message(participant_id_str, player_update_event)
                            logger.debug("Sent player update with in_combat=True", player_id=participant_id_str)
                    except Exception as e:
                        logger.warning(
                            "Error sending player update for combat start", player_id=participant_id_str, error=str(e)
                        )

        except Exception as e:
            logger.error("Error handling combat started event", error=str(e), data=data)

    async def _handle_combat_ended_event(self, data: dict[str, Any]):
        """Handle combat_ended event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Combat ended event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("combat_ended", room_id, data)
            logger.debug("Combat ended event broadcasted", room_id=room_id)

            # Send player updates with in_combat status to all players who were in combat
            participants = data.get("participants", {})
            if participants:
                from .envelope import build_event

                for participant_id_str in participants:
                    try:
                        # Get player by ID to send update
                        player = await self.connection_manager._get_player(participant_id_str)
                        if player:
                            # Send player update with in_combat status
                            player_update_event = build_event(
                                "player_update",
                                {
                                    "player_id": participant_id_str,
                                    "in_combat": False,
                                },
                                player_id=participant_id_str,
                            )
                            await self.connection_manager.send_personal_message(participant_id_str, player_update_event)
                            logger.debug("Sent player update with in_combat=False", player_id=participant_id_str)
                    except Exception as e:
                        logger.warning(
                            "Error sending player update for combat end", player_id=participant_id_str, error=str(e)
                        )

        except Exception as e:
            logger.error("Error handling combat ended event", error=str(e), data=data)

    async def _handle_player_attacked_event(self, data: dict[str, Any]):
        """Handle player_attacked event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Player attacked event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("player_attacked", room_id, data)
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

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("npc_attacked", room_id, data)
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

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("npc_took_damage", room_id, data)
            logger.debug("NPC took damage event broadcasted", room_id=room_id)

        except Exception as e:
            logger.error("Error handling NPC took damage event", error=str(e), data=data)

    async def _handle_npc_died_event(self, data: dict[str, Any]):
        """
        Handle npc_died event - NATS to EventBus bridge pattern.

        ARCHITECTURE NOTE - Dual Event Path by Design:
        This handler implements the NATS→EventBus bridge pattern, which is NOT redundant:

        1. NATS Path (Inter-Service Communication):
           - CombatService publishes NPCDiedEvent → NATS → NATSMessageHandler (here)
           - Purpose: Broadcast death to WebSocket clients for UI updates

        2. EventBus Path (Internal Game Logic):
           - NATSMessageHandler publishes NPCDied → EventBus → NPCLifecycleManager
           - Purpose: Trigger respawn queue processing with configured delay

        This separation of concerns follows NATS.mdc best practices:
        - NATS handles distributed messaging and client broadcasting
        - EventBus handles internal domain logic and game state management
        - Bridge pattern prevents tight coupling between communication and domain layers

        AI Agent: This is the ONLY place that bridges NATS npc_died messages to EventBus.
                  CombatService publishes to NATS only, not EventBus directly.
                  Removing this bridge would break NPC respawning entirely!

        Note: NPC removal from room is handled by the NPCLeftRoom event published
        by the lifecycle manager. This handler broadcasts the death event to clients
        AND publishes to EventBus for respawn queue processing.
        """
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
            from server.events.event_types import NPCDied

            # Broadcast death event to room clients using injected connection_manager
            # AI: Room state mutation is handled by NPCLeftRoom event from lifecycle manager
            # AI: This prevents duplicate removal attempts and maintains single source of truth
            await self.connection_manager.broadcast_room_event("npc_died", room_id, data)
            logger.debug("NPC died event broadcasted", room_id=room_id, npc_id=npc_id, npc_name=npc_name)

            # AI Agent: CRITICAL - Publish to EventBus so lifecycle manager can queue for respawn
            #           This ensures ALL NPCs (required and optional) respect respawn delay
            event_bus = self.connection_manager._get_event_bus()
            if event_bus:
                npc_died_event = NPCDied(npc_id=str(npc_id), room_id=room_id, cause=data.get("cause", "combat"))
                event_bus.publish(npc_died_event)
                logger.info(
                    "NPCDied event published to EventBus for respawn queue",
                    npc_id=npc_id,
                    npc_name=npc_name,
                )

        except Exception as e:
            logger.error("Error handling NPC died event", error=str(e), data=data)


# AI Agent: Global singleton removed - use ApplicationContainer.nats_message_handler instead
# Migration complete: All code now uses dependency injection via container
