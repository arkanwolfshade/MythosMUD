"""Stubs for fastapi_users.authentication.strategy.base."""

from typing import Generic, TypeVar

UP = TypeVar("UP")
ID = TypeVar("ID")

class Strategy(Generic[UP, ID]):
    """JWT/DB strategy base used by AuthenticationBackend.login overrides."""

__all__ = ["Strategy"]
