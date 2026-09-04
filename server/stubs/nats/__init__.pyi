"""
Type stubs for nats-py library.

This stub file provides type hints for the NATS Python client library
to enable proper mypy type checking and IDE autocomplete.
"""

from collections.abc import Awaitable, Callable
from typing import Any

class Client:
    """NATS client for publishing and subscribing to messages."""

    async def connect(
        self,
        servers: str | list[str] = ...,
        **kwargs: Any,
    ) -> None: ...
    async def close(self) -> None: ...
    async def publish(
        self,
        subject: str,
        payload: bytes = ...,
        reply: str = ...,
        headers: dict[str, str] | None = ...,
    ) -> None: ...
    async def subscribe(
        self,
        subject: str,
        queue: str = ...,
        cb: Callable[[Any], Awaitable[None]] | None = ...,
        future: Any = ...,
        max_msgs: int = ...,
        pending_msgs_limit: int = ...,
        pending_bytes_limit: int = ...,
    ) -> Subscription: ...
    async def request(
        self,
        subject: str,
        payload: bytes = ...,
        timeout: float = ...,
        old_style: bool = ...,
        headers: dict[str, str] | None = ...,
    ) -> Msg: ...
    async def flush(self, timeout: float = ...) -> None: ...
    async def drain(self) -> None: ...
    def add_error_listener(self, cb: Callable[[Exception], None]) -> None: ...
    def add_disconnect_listener(self, cb: Callable[[], None]) -> None: ...
    def add_reconnect_listener(self, cb: Callable[[], None]) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_reconnecting(self) -> bool: ...
    @property
    def is_draining(self) -> bool: ...

class Subscription:
    """NATS subscription object."""

    async def unsubscribe(self, limit: int = ...) -> None: ...
    async def drain(self) -> None: ...
    @property
    def subject(self) -> str: ...
    @property
    def queue(self) -> str: ...
    @property
    def pending_msgs(self) -> int: ...
    @property
    def pending_bytes(self) -> int: ...

class Msg:
    """NATS message object."""

    subject: str
    reply: str
    data: bytes
    headers: dict[str, str] | None

    def __init__(
        self,
        subject: str = ...,
        reply: str = ...,
        data: bytes = ...,
        headers: dict[str, str] | None = ...,
    ) -> None: ...
    async def respond(self, data: bytes) -> None: ...

async def connect(
    servers: str | list[str] = ...,
    **kwargs: Any,
) -> Client: ...

# Type alias for backward compatibility (nats.NATS is Client)
NATS = Client

class NatsError(Exception):
    """Base exception for NATS errors."""

    ...

class ConnectionClosedError(NatsError):
    """Connection was closed."""

    ...

class TimeoutError(NatsError):
    """Operation timed out."""

    ...

class NoServersError(NatsError):
    """No servers available."""

    ...
