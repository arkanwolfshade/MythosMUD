"""
NATS message handler for MythosMUD chat system.

This module handles incoming NATS messages and broadcasts them to WebSocket clients.
It replaces the previous Redis message handler with NATS-based messaging.
"""

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines  # Reason: NATS handler requires many state tracking attributes and complex message processing logic. NATS message handler requires extensive message handling logic for comprehensive real-time messaging system.

from datetime import timedelta
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any

from ..middleware.metrics_collector import metrics_collector
from ..realtime.circuit_breaker import CircuitBreaker
from ..realtime.dead_letter_queue import DeadLetterQueue
from ..realtime.nats_retry_handler import NATSRetryHandler
from ..services.nats_exceptions import NATSError, NATSSubscribeError
from ..structured_logging.enhanced_logging_config import get_logger
from .connection_manager import resolve_connection_manager as _resolve_connection_manager
from .event_handlers import EventHandler
from .message_filtering import MessageFilteringHelper
from .nats_message_handler_broadcast import NATSMessageBroadcastMixin
from .nats_message_handler_processing import NATSMessageProcessingMixin
from .nats_message_handler_subscriptions import NATSMessageSubscriptionMixin

logger = get_logger("communications.nats_message_handler")

if TYPE_CHECKING:
    from ..realtime.connection_manager import ConnectionManager
    from ..services.nats_service import NATSService
    from ..services.nats_subject_manager import NATSSubjectManager
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


class NATSMessageHandler(
    NATSMessageProcessingMixin,
    NATSMessageBroadcastMixin,
    NATSMessageSubscriptionMixin,
):
    """
    Handler for processing NATS messages and broadcasting to WebSocket clients.

    This handler subscribes to NATS subjects for chat messages and broadcasts
    them to the appropriate WebSocket clients based on room and channel.
    """

    def __init__(
        self,
        nats_service: "NATSService | None" = None,
        subject_manager: "NATSSubjectManager | None" = None,
        connection_manager: "ConnectionManager | None" = None,
        user_manager: "UserManager | None" = None,
    ) -> None:
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
    def connection_manager(self) -> Any:
        """Get the connection manager instance.

        Returns:
            The connection manager, preferring explicitly injected manager
            over the container's default manager.
        """
        # Prefer explicitly injected manager
        if self._connection_manager is not None:
            try:
                resolved = _resolve_connection_manager(self._connection_manager)
                if resolved is not None:
                    return resolved
            except (RuntimeError, AttributeError):
                # Resolution error - fall through to fallback
                pass

        # Try to resolve from container as fallback
        try:
            fallback = _resolve_connection_manager(None)
            if fallback is not None:
                return fallback
        except (RuntimeError, AttributeError):
            # Resolution error - fall through to legacy stub
            pass

        # No concrete manager available; return the stub so patched methods remain usable
        return _LEGACY_CONNECTION_MANAGER_STUB

    @connection_manager.setter
    def connection_manager(self, value: Any) -> None:
        self._connection_manager = value
        # Update filtering helper's connection_manager reference
        if hasattr(self, "_filtering_helper"):
            self._filtering_helper.connection_manager = value
        # Update event handler's connection_manager reference
        if hasattr(self, "_event_handler"):
            self._event_handler.connection_manager = value

    async def start(self, enable_event_subscriptions: bool = True) -> bool:
        """
        Start the NATS message handler and subscribe to subjects.

        Args:
            enable_event_subscriptions: Whether to subscribe to event subjects

        Returns:
            True if started successfully, False otherwise
        """
        try:
            logger.debug("Subscribing to chat subjects")
            # Subscribe to chat message subjects
            await self._subscribe_to_chat_subjects()
            logger.debug("Chat subject subscription complete")

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

    async def stop(self) -> bool:
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

    async def _subscribe_to_chat_subjects(self) -> None:
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

    async def _subscribe_to_standardized_chat_subjects(self) -> None:
        """
        Subscribe to chat subjects using NATSSubjectManager patterns.

        This method retrieves subscription patterns from the subject manager
        to ensure consistency with the pattern definitions and reduces
        the risk of typos or mismatches between publishing and subscribing.

        AI: Uses subject manager to generate subscription patterns dynamically.
        AI: Includes legacy patterns for backward compatibility during migration.
        """
        logger.debug("Starting standardized chat subject subscriptions")

        # Get standardized chat subscription patterns from subject manager
        if self.subject_manager is None:
            raise RuntimeError("NATSSubjectManager is required for chat subject subscriptions")
        subscription_patterns = self.subject_manager.get_chat_subscription_patterns()

        logger.info(
            "Subscribing to chat subjects using NATSSubjectManager patterns",
            pattern_count=len(subscription_patterns),
        )

        for pattern in subscription_patterns:
            logger.debug("Subscribing to pattern", pattern=pattern)
            try:
                await self._subscribe_to_subject(pattern)
            except (NATSError, RuntimeError) as e:
                logger.error(
                    "Failed to subscribe to pattern, continuing with other patterns",
                    pattern=pattern,
                    error=str(e),
                )
                # Continue with other patterns even if one fails
                continue

        logger.debug("Finished standardized chat subject subscriptions")

    async def _subscribe_to_subject(self, subject: str) -> bool:
        """
        Subscribe to a specific NATS subject.

        Args:
            subject: Subject string to subscribe to (built by caller using NATSSubjectManager)

        Raises:
            NATSSubscribeError: If subscription fails
        """
        try:
            logger.debug("Subscribing to NATS subject", subject=subject)
            if self.nats_service is None:
                logger.error("NATSService is required for subscriptions", subject=subject)
                return False
            # subscribe() now raises exceptions instead of returning False
            await self.nats_service.subscribe(subject, self._handle_nats_message)
            self.subscriptions[subject] = True
            logger.debug("Subscribed to NATS subject", subject=subject)
            return True
        except NATSSubscribeError:
            # Re-raise NATSSubscribeError as documented in docstring
            raise
        except (NATSError, RuntimeError) as e:
            logger.error("Error subscribing to NATS subject", subject=subject, error=str(e))
            return False

    async def _unsubscribe_from_subject(self, subject: str) -> bool:
        """
        Unsubscribe from a specific NATS subject.

        Returns:
            True if unsubscribed successfully, False if error occurred

        AI: Handles NATSUnsubscribeError exceptions and returns False for backward compatibility.
        """
        try:
            if self.nats_service is None:
                logger.error("NATSService is required for unsubscriptions", subject=subject)
                return False
            await self.nats_service.unsubscribe(subject)
            if subject in self.subscriptions:
                del self.subscriptions[subject]
            logger.info("Unsubscribed from NATS subject", subject=subject)
            return True
        except (NATSError, RuntimeError) as e:
            logger.error("Error unsubscribing from NATS subject", subject=subject, error=str(e))
            return False
