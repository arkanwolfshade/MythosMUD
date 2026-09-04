"""
Compatibility helpers for connection manager.

This module provides compatibility properties and methods that delegate
to internal components for backward compatibility with existing tests.
"""

from typing import Any

# For properties, we need to use a different approach - attach them directly to the class
# This will be called during class definition


def _create_property_with_accessors(
    getter_attr: str, setter_attr: str | None = None, deleter_clear: bool = True
) -> tuple[Any, Any, Any]:
    """
    Create getter, setter, and deleter functions for a property.

    Args:
        getter_attr: Attribute path for getter (e.g., "room_manager.room_subscriptions")
        setter_attr: Attribute path for setter (if None, uses getter_attr)
        deleter_clear: Whether deleter should clear the attribute (True) or set to empty dict/list

    Returns:
        Tuple of (getter, setter, deleter) functions
    """
    attr_path = setter_attr if setter_attr else getter_attr

    def getter(self: Any) -> Any:
        obj = self
        for part in getter_attr.split("."):
            obj = getattr(obj, part)
        return obj

    def setter(self: Any, value: Any) -> None:
        obj = self
        parts = attr_path.split(".")
        for part in parts[:-1]:
            obj = getattr(obj, part)
        setattr(obj, parts[-1], value)

    def deleter(self: Any) -> None:
        if deleter_clear:
            obj = self
            parts = getter_attr.split(".")
            for part in parts[:-1]:
                obj = getattr(obj, part)
            getattr(obj, parts[-1]).clear()
        else:
            obj = self
            parts = attr_path.split(".")
            for part in parts[:-1]:
                obj = getattr(obj, part)
            setattr(obj, parts[-1], {})

    return getter, setter, deleter


def _attach_room_properties(cls: type[Any]) -> None:
    """Attach room-related compatibility properties."""
    room_subscriptions_getter, room_subscriptions_setter, room_subscriptions_deleter = _create_property_with_accessors(
        "room_manager.room_subscriptions"
    )
    cls.room_subscriptions = property(room_subscriptions_getter, room_subscriptions_setter, room_subscriptions_deleter)

    room_occupants_getter, room_occupants_setter, room_occupants_deleter = _create_property_with_accessors(
        "room_manager.room_occupants"
    )
    cls.room_occupants = property(room_occupants_getter, room_occupants_setter, room_occupants_deleter)


def _attach_connection_properties(cls: type[Any]) -> None:
    """Attach connection-related compatibility properties."""
    connection_attempts_getter, connection_attempts_setter, connection_attempts_deleter = (
        _create_property_with_accessors("rate_limiter.connection_attempts")
    )
    cls.connection_attempts = property(
        connection_attempts_getter, connection_attempts_setter, connection_attempts_deleter
    )

    cls.max_connection_attempts = property(lambda self: self.rate_limiter.max_connection_attempts)
    cls.connection_window = property(lambda self: self.rate_limiter.connection_window)


def _attach_message_properties(cls: type[Any]) -> None:
    """Attach message-related compatibility properties."""
    pending_messages_getter, pending_messages_setter, pending_messages_deleter = _create_property_with_accessors(
        "message_queue.pending_messages"
    )
    cls.pending_messages = property(pending_messages_getter, pending_messages_setter, pending_messages_deleter)


def attach_compatibility_properties(cls: type[Any]) -> None:
    """Attach compatibility properties to the ConnectionManager class."""
    _attach_room_properties(cls)
    _attach_connection_properties(cls)
    _attach_message_properties(cls)
