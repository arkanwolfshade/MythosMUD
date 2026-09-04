"""Read the running FastAPI app without a static import of server.main.

A static ``from server.main import app`` closes the factory -> lifespan -> container
-> realtime -> main -> factory cycle (basedpyright reportImportCycles).
"""

from __future__ import annotations

import importlib
from typing import Protocol, cast


class _MainModule(Protocol):
    app: object


def connection_manager_from_running_app() -> object | None:
    """Return app.state.container.connection_manager, or None if unavailable."""
    loaded = cast(object, importlib.import_module("server.main"))
    main_mod = cast(_MainModule, loaded)
    app = main_mod.app
    state = getattr(app, "state", None)
    container = getattr(state, "container", None) if state is not None else None
    if container is None:
        return None
    return getattr(container, "connection_manager", None)
