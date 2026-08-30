"""Read the running FastAPI app's container without a static import that would cycle.

A static ``from server.services.combat_service import get_combat_service`` (called from
``server/npc/``) or ``from server.services.npc_instance_service import get_npc_instance_service``
closes the container -> bundles -> npc -> services -> npc cycle at the point ``npc/`` reaches
back into ``services/`` (ADR-001 layer direction; #757). Mirrors
``server/realtime/running_app.py``'s established, already-reviewed pattern for the identical
shape of problem.
"""

from __future__ import annotations

import importlib
from typing import Protocol, cast


class _MainModule(Protocol):
    app: object


def _container_from_running_app() -> object | None:
    """Return app.state.container, or None if unavailable."""
    loaded = cast(object, importlib.import_module("server.main"))
    main_mod = cast(_MainModule, loaded)
    app = main_mod.app
    state = getattr(app, "state", None)
    return getattr(state, "container", None) if state is not None else None


def combat_service_from_running_app() -> object | None:
    """Return app.state.container.combat_service, or None if unavailable."""
    container = _container_from_running_app()
    if container is None:
        return None
    return getattr(container, "combat_service", None)


def npc_instance_service_from_running_app() -> object | None:
    """Return the process-wide NPC instance service singleton, or None if unavailable.

    Not a container attribute (server/services/npc_instance_service.py holds it as its own
    module-level singleton, initialized via initialize_npc_instance_service in
    server/container/bundles/npc.py) — loaded via importlib for the same cycle-avoidance
    reason as combat_service_from_running_app above, not routed through the container.
    """
    module = cast(object, importlib.import_module("server.services.npc_instance_service"))
    getter = getattr(module, "get_npc_instance_service", None)
    if not callable(getter):
        return None
    try:
        return cast(object, getter())
    except RuntimeError:
        return None
