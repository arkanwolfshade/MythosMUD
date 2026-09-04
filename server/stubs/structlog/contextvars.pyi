"""Type stubs for structlog.contextvars module."""

from collections.abc import MutableMapping
from typing import Any

def clear_contextvars() -> None:
    """Clear all context variables."""
    ...

def bind_contextvars(**kwargs: Any) -> None:
    """Bind new key-value pairs to context variables."""
    ...

def unbind_contextvars(*keys: str) -> None:
    """Unbind specified keys from context variables."""
    ...

def get_contextvars() -> dict[str, Any]:
    """Get current context variables."""
    ...

def merge_contextvars(
    logger: Any,
    name: str,
    event_dict: MutableMapping[str, Any],
) -> MutableMapping[str, Any]:
    """Merge context variables into the event dictionary."""
    ...
