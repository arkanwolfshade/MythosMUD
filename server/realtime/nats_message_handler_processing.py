"""Chat message processing mixin for NATSMessageHandler.

Extracted to keep nats_message_handler.py under the Lizard file-nloc limit.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import Any

from ..realtime.circuit_breaker import CircuitBreakerOpen
from ..realtime.dead_letter_queue import DeadLetterMessage
from ..realtime.envelope import build_event
from ..schemas.realtime import validate_message
from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger
from .message_formatters import format_message_content
from .nats_message_handler_base import NATSMessageHandlerMixinBase

logger = get_logger("communications.nats_message_handler")


class NATSMessageProcessingMixin(NATSMessageHandlerMixinBase):
    """Mixin: NATS message ingest, retry, chat field extract/validate, channel broadcast."""

    async def _handle_nats_message(self, message_data: dict[str, Any]) -> None:
        """
        Handle incoming NATS message with error boundaries.

        Wraps message processing with retry logic, circuit breaker,
        and dead letter queue for resilient delivery.

        Args:
            message_data: Message data from NATS

        AI: Entry point with full error boundary protection.
        """
        logger.debug(
            "NATS message received", message_keys=list(message_data.keys()) if isinstance(message_data, dict) else None
        )
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

        except (ValueError, NATSError, RuntimeError, AttributeError) as e:
            # Handle validation errors and other unexpected errors
            # Validation errors from validate_message should be caught and handled gracefully
            logger.error(
                "Error in message processing",
                message_id=message_id,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )

            # Add to DLQ as last resort (use async version to avoid blocking)
            dlq_message = DeadLetterMessage(
                subject=channel,
                data=message_data,
                error=str(e),
                timestamp=datetime.now(UTC),
                retry_count=0,
                original_headers={"reason": "unhandled_exception"},
            )
            await self.dead_letter_queue.enqueue_async(dlq_message)

            self.metrics.record_message_failed(channel, type(e).__name__)

    async def _process_message_with_retry(self, message_data: dict[str, Any]) -> None:
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
            await self.dead_letter_queue.enqueue_async(dlq_message)

            self.metrics.record_message_dlq(channel)
            self.metrics.record_message_failed(channel, type(result).__name__)

            # Re-raise to trigger circuit breaker
            raise result

    async def _process_single_message(self, message_data: dict[str, Any]) -> None:
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

        # Check if this is an event message (either event_type or event_data indicates event message)
        if message_data.get("event_type") or message_data.get("event_data"):
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

        # Whisper / personal system publish "target_id"; broadcasting expects "target_player_id".
        if channel in ("whisper", "system") and target_id and not target_player_id:
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
            "speaker_kind": message_data.get("speaker_kind"),
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
        speaker_kind = chat_fields.get("speaker_kind")
        if speaker_kind:
            event_data["speaker_kind"] = speaker_kind
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
        chat_event: dict[str, Any],
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
    ) -> None:
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
