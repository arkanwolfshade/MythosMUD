"""Access the DI container's live AsyncPersistenceLayer singleton."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Protocol, cast

if TYPE_CHECKING:
    from server.async_persistence import AsyncPersistenceLayer


class _ContainerWithPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Container singleton surface needed for persistence lookup."""

    async_persistence: AsyncPersistenceLayer | None


class _ApplicationContainerType(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """ApplicationContainer.get_instance without importing container.main."""

    @staticmethod
    def get_instance() -> _ContainerWithPersistence: ...  # pylint: disable=missing-function-docstring  # Reason: Protocol stub


def get_container_async_persistence() -> AsyncPersistenceLayer:
    """
    Return the container-backed AsyncPersistenceLayer instance.

    Uses importlib for ApplicationContainer so this module does not statically
    import container.main (basedpyright import cycle through combat/DI bundles).
    """
    loaded = importlib.import_module("server.container.main")
    app_container = cast(_ApplicationContainerType, loaded.ApplicationContainer)
    container = app_container.get_instance()
    if container.async_persistence is None:
        raise RuntimeError("AsyncPersistenceLayer not initialized in container")
    return container.async_persistence
