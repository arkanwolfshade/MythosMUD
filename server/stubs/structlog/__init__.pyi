"""
Type stubs for structlog library.

This stub file provides type hints for the structlog structured logging library
to enable proper mypy type checking and IDE autocomplete.
"""

from collections.abc import Callable, Iterable, Mapping, MutableMapping
from typing import Any, Protocol, TypeVar

_T = TypeVar("_T")

class BoundLoggerBase(Protocol):
    """Protocol for bound logger objects."""

    def bind(self, **kwargs: Any) -> BoundLoggerBase: ...
    def unbind(self, *keys: str) -> BoundLoggerBase: ...
    def try_unbind(self, *keys: str) -> BoundLoggerBase: ...
    def new(self, **kwargs: Any) -> BoundLoggerBase: ...
    def debug(self, event: str, **kwargs: Any) -> Any: ...
    def info(self, event: str, **kwargs: Any) -> Any: ...
    def warning(self, event: str, **kwargs: Any) -> Any: ...
    def error(self, event: str, **kwargs: Any) -> Any: ...
    def critical(self, event: str, **kwargs: Any) -> Any: ...
    def exception(self, event: str, **kwargs: Any) -> Any: ...
    def log(self, level: int | str, event: str, **kwargs: Any) -> Any: ...

class BoundLogger(BoundLoggerBase):
    """Concrete bound logger implementation."""

    def __init__(
        self,
        logger: Any,
        processors: Iterable[Any],
        context: MutableMapping[str, Any],
        **kwargs: Any,
    ) -> None: ...
    def bind(self, **kwargs: Any) -> BoundLogger: ...
    def unbind(self, *keys: str) -> BoundLogger: ...
    def try_unbind(self, *keys: str) -> BoundLogger: ...
    def new(self, **kwargs: Any) -> BoundLogger: ...

class PrintLogger:
    """Logger that prints to stdout."""

    def __call__(self, level: str, event: str, **kwargs: Any) -> None: ...
    def debug(self, event: str, **kwargs: Any) -> None: ...
    def info(self, event: str, **kwargs: Any) -> None: ...
    def warning(self, event: str, **kwargs: Any) -> None: ...
    def error(self, event: str, **kwargs: Any) -> None: ...
    def critical(self, event: str, **kwargs: Any) -> None: ...

class PrintLoggerFactory:
    """Factory for creating print loggers."""

    def __init__(self, file: Any = ...) -> None: ...
    def __call__(self, *args: Any) -> PrintLogger: ...

def configure(
    processors: Any = ...,  # Too complex to type precisely
    wrapper_class: Any = ...,
    context_class: Any = ...,
    logger_factory: Any = ...,
    cache_logger_on_first_use: bool = ...,
) -> None: ...
def wrap_logger(logger: Any, **kwargs: Any) -> BoundLogger: ...
def get_logger(*args: Any, **kwargs: Any) -> BoundLogger: ...
def get_config() -> dict[str, Any]: ...
def configure_once(
    processors: Iterable[Any] | None = ...,
    wrapper_class: type[BoundLoggerBase] | None = ...,
    context_class: type[MutableMapping[str, Any]] = ...,
    logger_factory: Callable[..., Any] | None = ...,
    cache_logger_on_first_use: bool = ...,
) -> None: ...

# Processor functions
class ProcessorFormatter:
    """Base class for processor formatters."""

    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> Mapping[str, Any] | str | bytes: ...

def add_log_level(
    logger: Any,
    name: str,
    event_dict: MutableMapping[str, Any],
) -> MutableMapping[str, Any]: ...
def add_logger_name(
    logger: Any,
    name: str,
    event_dict: MutableMapping[str, Any],
) -> MutableMapping[str, Any]: ...

class TimeStamper:
    """Processor that adds timestamps."""

    def __init__(self, fmt: str | None = ..., utc: bool = ..., key: str = ...) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

class CallsiteParameterAdder:
    """Processor that adds callsite information."""

    def __init__(
        self,
        parameters: Iterable[Any] = ...,
        additional_ignores: Iterable[str] | None = ...,
    ) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

class ExceptionRenderer:
    """Processor that renders exceptions."""

    def __init__(self, exception_formatter: Callable[[Exception], str] = ...) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

class JSONRenderer:
    """Processor that renders to JSON."""

    def __init__(self, **dumps_kw: Any) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: Mapping[str, Any],
    ) -> bytes: ...

class KeyValueRenderer:
    """Processor that renders to key-value format."""

    def __init__(
        self,
        key_order: Iterable[str] | None = ...,
        drop_missing: bool = ...,
        sort_keys: bool = ...,
    ) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: Mapping[str, Any],
    ) -> str: ...

class ConsoleRenderer:
    """Processor that renders for console output."""

    def __init__(self, **kwargs: Any) -> None: ...
    def __call__(
        self,
        logger: Any,
        name: str,
        event_dict: Mapping[str, Any],
    ) -> str: ...

# Context management (moved to contextvars module)
def clear_contextvars() -> None: ...
def bind_contextvars(**kwargs: Any) -> None: ...
def unbind_contextvars(*keys: str) -> None: ...
def merge_contextvars(
    logger: Any,
    name: str,
    event_dict: MutableMapping[str, Any],
) -> MutableMapping[str, Any]: ...
def get_contextvars() -> dict[str, Any]:
    """Get current context variables."""
    ...

# Processor module exports
processors: Any  # Allow any processor access
