"""Stubs for fastapi_users.authentication (aligns with package import path)."""

from collections.abc import Callable
from typing import Generic, TypeVar

from starlette.responses import Response

from .strategy.base import Strategy

UP = TypeVar("UP")
ID = TypeVar("ID")

class BearerTransport:
    def __init__(self, tokenUrl: str) -> None: ...

class AuthenticationBackend(Generic[UP, ID]):
    """Authentication backend used by FastAPIUsers and app imports."""

    def __init__(
        self,
        name: str,
        transport: BearerTransport,
        get_strategy: Callable[..., Strategy[UP, ID]],
    ) -> None: ...
    async def login(self, strategy: Strategy[UP, ID], user: UP) -> Response: ...

__all__ = ["AuthenticationBackend", "BearerTransport", "Strategy"]
