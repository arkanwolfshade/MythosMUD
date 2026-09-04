"""
Event serialization for distributed EventBus over NATS.

Serializes and deserializes domain events to/from JSON-compatible dicts for
cross-instance distribution. Handles UUID, datetime, and nested structures.
"""

from __future__ import annotations

from dataclasses import Field, asdict, is_dataclass
from datetime import datetime
from types import ModuleType, NoneType  # pylint: disable=unused-import  # Used in generator on line 84
from typing import TypeVar, cast, get_args
from uuid import UUID

from .event_types import BaseEvent

T = TypeVar("T", bound=BaseEvent)

# Registry: event_type string -> event class for deserialization.
# Combat events are published directly to NATS via CombatEventPublisher, not EventBus.
_EVENT_CLASS_REGISTRY: dict[str, type[BaseEvent]] = {}


def _register_event_class(registry: dict[str, type[BaseEvent]], obj: object) -> None:
    if not (isinstance(obj, type) and issubclass(obj, BaseEvent) and obj is not BaseEvent):
        return
    try:
        inst = obj.__new__(obj)
        if hasattr(inst, "event_type") and inst.event_type:
            registry[inst.event_type] = obj
        else:
            registry[obj.__name__] = obj
    except (TypeError, AttributeError):
        registry[obj.__name__] = obj


def _register_module_events(module: ModuleType, registry: dict[str, type[BaseEvent]], *, include_base: bool) -> None:
    for name in dir(module):
        obj = cast(object, getattr(module, name))  # getattr is typed Any
        if include_base:
            if isinstance(obj, type) and issubclass(obj, BaseEvent):
                registry[obj.__name__] = obj
        else:
            _register_event_class(registry, obj)


def _register_event_types() -> None:
    """Populate the event class registry. Lazy import to avoid circular deps."""
    if _EVENT_CLASS_REGISTRY:
        return

    from . import combat_events, event_types

    _register_module_events(event_types, _EVENT_CLASS_REGISTRY, include_base=False)

    # PlayerXPAwardEvent's event_type ("player_xp_awarded") is set in __post_init__, which the
    # reflective scan's __new__()-without-__init__() probe never runs — so that scan registers it
    # under its class name only. Register the serialized-key lookup explicitly.
    _EVENT_CLASS_REGISTRY["player_xp_awarded"] = event_types.PlayerXPAwardEvent

    _register_module_events(combat_events, _EVENT_CLASS_REGISTRY, include_base=True)


def _copy_public_event_attrs(event: BaseEvent) -> dict[str, object]:
    data: dict[str, object] = {}
    for field_name in dir(event):
        if field_name.startswith("_") or field_name in ("event_type",):
            continue
        try:
            value = cast(object, getattr(event, field_name))  # getattr is typed Any
            if not callable(value) and not isinstance(value, type):
                data[field_name] = value
        except (AttributeError, TypeError):
            pass
    return data


def _extract_event_fields(event: BaseEvent) -> dict[str, object]:
    if is_dataclass(event) and not isinstance(event, type):
        return asdict(event)
    data = _copy_public_event_attrs(event)
    if hasattr(event, "event_type"):
        data["event_type"] = getattr(event, "event_type", type(event).__name__)
    return data


def _convert_value_for_json(value: object) -> object:
    """Convert a value to JSON-serializable form."""
    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, dict):
        mapping = cast(dict[object, object], value)
        return {key: _convert_value_for_json(nested) for key, nested in mapping.items()}
    if isinstance(value, list | tuple):
        sequence = cast(list[object] | tuple[object, ...], value)
        return [_convert_value_for_json(nested) for nested in sequence]
    return value


def _unwrap_optional_type(field_type: object) -> object:
    optional_args = get_args(field_type)
    if not optional_args:
        return field_type
    typed_args = cast(tuple[object, ...], optional_args)
    real_type: object | None = None
    for type_arg in typed_args:
        if type_arg is not NoneType:
            real_type = type_arg
            break
    return field_type if real_type is None else real_type


def _parse_typed_json_value(value: object, field_type: object) -> object:
    if field_type is UUID:
        return UUID(value) if isinstance(value, str) else value
    if field_type is datetime and isinstance(value, str):
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    return value


def _convert_value_from_json(value: object, field_type: object) -> object:
    """Convert a JSON value back to the expected Python type."""
    if value is None:
        return None
    unwrapped = _unwrap_optional_type(field_type)
    if unwrapped is not field_type:
        return _convert_value_from_json(value, unwrapped)
    return _parse_typed_json_value(value, field_type)


def serialize_event(event: object) -> dict[str, object]:
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
        data = _extract_event_fields(event)
    except (TypeError, AttributeError):
        data = {"event_type": type(event).__name__}

    data["_event_type"] = getattr(event, "event_type", type(event).__name__)
    converted = _convert_value_for_json(data)
    # Cast: converter returns object; dict input always yields a dict of JSON-safe values.
    return cast(dict[str, object], converted)


def _event_class_from_payload(data: dict[str, object]) -> type[BaseEvent]:
    event_type_name = data.get("_event_type")
    if not isinstance(event_type_name, str) or not event_type_name:
        raise ValueError("Missing _event_type in event data")
    cls = _EVENT_CLASS_REGISTRY.get(event_type_name)
    if not cls:
        raise ValueError(f"Unknown event type: {event_type_name}")
    return cls


def _init_kwargs_from_event_data(cls: type[BaseEvent], data: dict[str, object]) -> dict[str, object]:
    kwargs: dict[str, object] = {}
    raw_fields = cast(dict[str, Field[object]], cls.__dataclass_fields__)
    init_fields = {name: field for name, field in raw_fields.items() if field.init}
    for key, value in list(data.items()):
        if key == "_event_type" or key not in init_fields:
            continue
        try:
            kwargs[key] = _convert_value_from_json(value, init_fields[key].type)
        except (StopIteration, TypeError):
            kwargs[key] = value
    return kwargs


def deserialize_event(data: dict[str, object]) -> BaseEvent:
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
    cls = _event_class_from_payload(data)
    return cls(**_init_kwargs_from_event_data(cls, data))
