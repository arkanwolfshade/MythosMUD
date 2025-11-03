"""Type stubs for structlog.stdlib module."""

from collections.abc import Callable, MutableMapping
from typing import Any

# Re-export BoundLogger from main structlog module
from structlog import BoundLogger as BoundLogger

class LoggerFactory:
    """Factory for creating loggers."""

    def __call__(self, *args: Any) -> Any: ...

class BoundLoggerLazyProxy:
    """Lazy proxy for bound loggers."""

    def __init__(self, logger: Any) -> None: ...
    def bind(self, **kwargs: Any) -> BoundLogger: ...

def filter_by_level(
    logger: Any,
    name: str,
    event_dict: MutableMapping[str, Any],
) -> MutableMapping[str, Any]:
    """Filter log entries by level."""
    ...

def add_log_level(
    logger: Any,
    name: str,
    event_dict: dict[str, Any],
) -> dict[str, Any]:
    """Add log level to event dictionary."""
    ...

def add_logger_name(
    logger: Any,
    name: str,
    event_dict: dict[str, Any],
) -> dict[str, Any]:
    """Add logger name to event dictionary."""
    ...

class PositionalArgumentsFormatter:
    """Formatter for positional arguments."""

    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

class ProcessorFormatter:
    """Formatter that uses structlog processors."""

    def __init__(
        self,
        processor: Callable[[Any, str, dict[str, Any]], str | bytes],
        foreign_pre_chain: list[Callable[[Any, str, dict[str, Any]], dict[str, Any]]] | None = ...,
    ) -> None: ...
