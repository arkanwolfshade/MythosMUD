"""
Shared Starlette/FastAPI-shaped protocols for combat command modules.

Keeps ``AppWithState`` in one place so ``combat_handler`` and ``combat_flee`` agree
without importing each other.
"""

from __future__ import annotations

from typing import Protocol


class AppWithState(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Application object with a ``state`` namespace (dynamic attributes)."""

    state: object
