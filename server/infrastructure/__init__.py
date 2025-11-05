"""
Infrastructure layer for MythosMUD.

This package contains abstractions for external dependencies like messaging systems,
caching, and other infrastructure concerns. Following hexagonal architecture principles,
the domain layer depends on these abstractions, not concrete implementations.

As noted in the restricted archives: "The domain must remain pure, untainted
by the specifics of the infrastructure that supports it."
"""

from .message_broker import MessageBroker, MessageHandler

__all__ = ["MessageBroker", "MessageHandler"]
