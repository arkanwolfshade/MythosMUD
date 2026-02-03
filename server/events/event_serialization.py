"""
Event serialization for distributed EventBus over NATS.

Serializes and deserializes domain events to/from JSON-compatible dicts for
cross-instance distribution. Handles UUID, datetime, and nested structures.
"""

from __future__ import annotations

from dataclasses import asdict, fields, is_dataclass
from datetime import datetime
from types import NoneType  # pylint: disable=unused-import  # Used in generator on line 84
from typing import Any, TypeVar, cast
from uuid import UUID

from .event_types import BaseEvent

T = TypeVar("T", bound=BaseEvent)

# Registry: event_type string -> event class for deserialization.
# Combat events are published directly to NATS via CombatEventPublisher, not EventBus.
_EVENT_CLASS_REGISTRY: dict[str, type[BaseEvent]] = {}


def _register_event_types() -> None:
    """Populate the event class registry. Lazy import to avoid circular deps."""
    if _EVENT_CLASS_REGISTRY:
        return

    from . import combat_events, event_types

    for name in dir(event_types):
        obj = getattr(event_types, name)
        if isinstance(obj, type) and issubclass(obj, BaseEvent) and obj is not BaseEvent:
            # Use event_type from class default, or class name
            try:
                inst = obj.__new__(obj)
                if hasattr(inst, "event_type") and inst.event_type:
                    _EVENT_CLASS_REGISTRY[inst.event_type] = obj
                else:
                    _EVENT_CLASS_REGISTRY[obj.__name__] = obj
            except (TypeError, AttributeError):
                _EVENT_CLASS_REGISTRY[obj.__name__] = obj

    # PlayerXPAwardEvent has event_type "player_xp_awarded" - lazy import to avoid pulling config
    try:
        from ..services.player_combat_service import PlayerXPAwardEvent

        _EVENT_CLASS_REGISTRY["player_xp_awarded"] = PlayerXPAwardEvent
        _EVENT_CLASS_REGISTRY["PlayerXPAwardEvent"] = PlayerXPAwardEvent
    except Exception:  # pylint: disable=broad-exception-caught  # Config/import may fail in isolation
        pass

    # Combat events (in case any are ever published to EventBus)
    for name in dir(combat_events):
        obj = getattr(combat_events, name)
        if isinstance(obj, type) and issubclass(obj, BaseEvent):
            _EVENT_CLASS_REGISTRY[obj.__name__] = obj


def _convert_value_for_json(value: Any) -> Any:
    """Convert a value to JSON-serializable form."""
    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _convert_value_for_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_convert_value_for_json(v) for v in value]
    return value


def _convert_value_from_json(value: Any, field_type: Any) -> Any:
    """Convert a JSON value back to the expected Python type."""
    if value is None:
        return None

    # Resolve Optional/Union to the first non-None type
    import typing

    args = getattr(typing, "get_args", lambda t: ())(field_type)
    if args:
        real_type = next((a for a in args if a is not NoneType), None)
        if real_type is not None:
            return _convert_value_from_json(value, real_type)

    if field_type is UUID:
        return UUID(value) if isinstance(value, str) else value
    if field_type is datetime:
        if isinstance(value, str):
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        return value
    return value


def serialize_event(event: BaseEvent) -> dict[str, Any]:
    """
    Serialize a BaseEvent to a JSON-compatible dict.

    Args:
        event: Domain event to serialize

    Returns:
        Dict with keys: _event_type, and all event fields (UUID/datetime as strings)
    """
    if not isinstance(event, BaseEvent):
        raise ValueError("Event must inherit from BaseEvent")

    _register_event_types()

    try:
        if is_dataclass(event) and not isinstance(event, type):
            data = asdict(event)
        else:
            data = {}
            for f in dir(event):
                if f.startswith("_") or f in ("event_type",):
                    continue
                try:
                    v = getattr(event, f)
                    if not callable(v) and not isinstance(v, type):
                        data[f] = v
                except (AttributeError, TypeError):
                    pass
            if hasattr(event, "event_type"):
                data["event_type"] = getattr(event, "event_type", type(event).__name__)
    except (TypeError, AttributeError):
        data = {"event_type": type(event).__name__}

    data["_event_type"] = getattr(event, "event_type", type(event).__name__)
    # cast: _convert_value_for_json returns Any; for dict input we always get dict[str, Any]
    return cast(dict[str, Any], _convert_value_for_json(data))


def deserialize_event(data: dict[str, Any]) -> BaseEvent:
    """
    Deserialize a dict back to a BaseEvent instance.

    Args:
        data: Dict from serialize_event (must include _event_type)

    Returns:
        Reconstructed event instance

    Raises:
        ValueError: If event type unknown or deserialization fails
    """
    _register_event_types()

    event_type_name = data.get("_event_type")
    if not event_type_name:
        raise ValueError("Missing _event_type in event data")

    cls = _EVENT_CLASS_REGISTRY.get(event_type_name)
    if not cls:
        raise ValueError(f"Unknown event type: {event_type_name}")

    # Build kwargs from data - only include fields that are in __init__ (init=True)
    kwargs: dict[str, Any] = {}
    init_fields = {f.name: f for f in fields(cls) if f.init}

    for key, value in list(data.items()):
        if key == "_event_type":
            continue
        if key in init_fields:
            try:
                field = init_fields[key]
                kwargs[key] = _convert_value_from_json(value, field.type)
            except (StopIteration, TypeError):
                kwargs[key] = value

    return cls(**kwargs)
