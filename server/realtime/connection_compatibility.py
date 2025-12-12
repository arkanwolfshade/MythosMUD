"""
Compatibility helpers for connection manager.

This module provides compatibility properties and methods that delegate
to internal components for backward compatibility with existing tests.
"""

from typing import Any

# For properties, we need to use a different approach - attach them directly to the class
# This will be called during class definition


def attach_compatibility_properties(cls: type[Any]) -> None:
    """Attach compatibility properties to the ConnectionManager class."""

    # Room subscriptions
    def room_subscriptions_getter(self: Any) -> Any:
        return self.room_manager.room_subscriptions

    def room_subscriptions_setter(self: Any, value: Any) -> None:
        self.room_manager.room_subscriptions = value

    def room_subscriptions_deleter(self: Any) -> None:
        self.room_manager.room_subscriptions.clear()

    cls.room_subscriptions = property(room_subscriptions_getter, room_subscriptions_setter, room_subscriptions_deleter)

    # Room occupants
    def room_occupants_getter(self: Any) -> Any:
        return self.room_manager.room_occupants

    def room_occupants_setter(self: Any, value: Any) -> None:
        self.room_manager.room_occupants = value

    def room_occupants_deleter(self: Any) -> None:
        self.room_manager.room_occupants.clear()

    cls.room_occupants = property(room_occupants_getter, room_occupants_setter, room_occupants_deleter)

    # Connection attempts
    def connection_attempts_getter(self: Any) -> Any:
        return self.rate_limiter.connection_attempts

    def connection_attempts_setter(self: Any, value: Any) -> None:
        self.rate_limiter.connection_attempts = value

    def connection_attempts_deleter(self: Any) -> None:
        self.rate_limiter.connection_attempts.clear()

    cls.connection_attempts = property(
        connection_attempts_getter, connection_attempts_setter, connection_attempts_deleter
    )

    # Pending messages
    def pending_messages_getter(self: Any) -> Any:
        return self.message_queue.pending_messages

    def pending_messages_setter(self: Any, value: Any) -> None:
        self.message_queue.pending_messages = value

    def pending_messages_deleter(self: Any) -> None:
        self.message_queue.pending_messages.clear()

    cls.pending_messages = property(pending_messages_getter, pending_messages_setter, pending_messages_deleter)

    # Max connection attempts (read-only)
    cls.max_connection_attempts = property(lambda self: self.rate_limiter.max_connection_attempts)

    # Connection window (read-only)
    cls.connection_window = property(lambda self: self.rate_limiter.connection_window)
