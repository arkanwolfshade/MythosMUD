"""Attribute stubs for NATSMessageHandler mixins (mypy attr-defined).

Mirrors server/services/combat_messaging/base.py HasConnectionManager pattern.
"""

# Stub-only attrs are provided by NATSMessageHandler at runtime; no class-body defaults
# (mutable dicts) and no Protocol base (would poison the concrete handler MRO).
# pyright: reportUninitializedInstanceVariable=false

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..middleware.metrics_collector import MetricsCollector
    from ..services.user_manager import UserManager
    from .circuit_breaker import CircuitBreaker
    from .dead_letter_queue import DeadLetterQueue
    from .event_handlers import EventHandler
    from .message_filtering import MessageFilteringHelper
    from .nats_retry_handler import NATSRetryHandler


class NATSMessageHandlerMixinBase:
    """Attrs/methods provided by NATSMessageHandler when mixed in."""

    subject_manager: Any
    subscriptions: dict[str, bool]
    subzone_subscriptions: dict[str, int]
    player_subzone_subscriptions: dict[str, str]
    _event_handler: EventHandler
    _filtering_helper: MessageFilteringHelper
    connection_manager: Any
    user_manager: UserManager | None
    circuit_breaker: CircuitBreaker
    metrics: MetricsCollector
    dead_letter_queue: DeadLetterQueue
    retry_handler: NATSRetryHandler

    # Concrete stubs for mypy (ellipsis + non-None return triggers empty-body).
    # Real impl on NATSMessageHandler. Do not raise NotImplementedError — pylint W0223.
    async def _subscribe_to_subject(self, _subject: str) -> bool:
        return False

    async def _unsubscribe_from_subject(self, _subject: str) -> bool:
        return False
