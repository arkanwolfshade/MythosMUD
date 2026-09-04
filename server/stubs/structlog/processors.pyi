"""Type stubs for structlog.processors module."""

from collections.abc import Callable, Mapping, MutableMapping
from typing import Any

class TimeStamper:
    """Processor that adds timestamps to log entries."""

    def __init__(self, fmt: str | None = ..., utc: bool = ..., key: str = ...) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

class StackInfoRenderer:
    """Processor that renders stack information."""

    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

def format_exc_info(
    logger: Any,
    name: str,
    event_dict: MutableMapping[str, Any],
) -> MutableMapping[str, Any]:
    """Format exception information."""
    ...

class UnicodeDecoder:
    """Processor that decodes unicode strings."""

    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

class KeyValueRenderer:
    """Processor that renders events as key-value pairs."""

    def __init__(
        self,
        key_order: list[str] | None = ...,
        drop_missing: bool = ...,
        sort_keys: bool = ...,
    ) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: Mapping[str, Any],
    ) -> str: ...

class JSONRenderer:
    """Processor that renders events as JSON."""

    def __init__(self, **dumps_kw: Any) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: Mapping[str, Any],
    ) -> bytes: ...

class ConsoleRenderer:
    """Processor that renders events for console output."""

    def __init__(self, **kwargs: Any) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: Mapping[str, Any],
    ) -> str: ...

class ExceptionRenderer:
    """Processor that renders exceptions."""

    def __init__(self, exception_formatter: Callable[[Exception], str] = ...) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

class CallsiteParameterAdder:
    """Processor that adds call site parameters."""

    def __init__(
        self,
        parameters: list[Any] = ...,
        additional_ignores: list[str] | None = ...,
    ) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...
