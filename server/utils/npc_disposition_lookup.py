"""
Resolve and wrap an NPC's wire disposition (#1025, #1036).

A leaf module (it imports only constants and logging, and reaches the NPC lifecycle lazily) so the realtime layer, the
combat services and the chat layer can all use it without creating an import cycle. ``realtime/connection_utils``
re-exports these names for the callers that already import them from there.
"""

import importlib
from collections.abc import Callable, Mapping
from typing import Protocol, cast

from ..constants.npc_disposition import DEFAULT_NPC_DISPOSITION, NpcDisposition, NpcOccupant
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def npc_disposition_from_type(npc_type: object, npc_id: str = "") -> NpcDisposition:
    """
    Map an NPC instance's ``npc_type`` (an ``NPCDefinitionType`` value) to its wire disposition.

    A missing or unrecognised type falls back to ``passive_mob`` with a warning: one bad definition row must
    not empty a room's whole occupant list, and combat still reaches the player through combat lines.
    """
    try:
        return NpcDisposition(str(npc_type))
    except ValueError:
        logger.warning("Unrecognised NPC type, using default disposition", npc_id=npc_id, npc_type=str(npc_type))
        return DEFAULT_NPC_DISPOSITION


def npc_disposition_from_row(row: Mapping[str, object]) -> NpcDisposition:
    """Disposition carried on an NPC occupant row (``disposition``); the NPC id is read only for the warning."""
    return npc_disposition_from_type(row.get("disposition"), str(row.get("npc_id") or row.get("player_id") or ""))


def npc_occupant(name: str, disposition: NpcDisposition) -> NpcOccupant:
    """One entry of a payload's ``npcs`` list."""
    return {"name": name, "disposition": disposition}


class _LifecycleManager(Protocol):
    """The slice of the NPC lifecycle manager this lookup reads."""

    active_npcs: Mapping[str, object]


class _NpcInstanceService(Protocol):
    """The slice of the NPC instance service this lookup reads."""

    lifecycle_manager: _LifecycleManager | None


def _npc_instance_service() -> _NpcInstanceService:
    """
    The NPC instance service, imported on demand.

    Uses importlib so this leaf module does not statically import ``services.npc_instance_service`` (basedpyright
    import cycle through the NPC lifecycle and combat modules back to the chat layer), the same technique as
    ``container.async_persistence_access``.
    """
    loaded = importlib.import_module("server.services.npc_instance_service")
    getter = cast(Callable[[], _NpcInstanceService], loaded.get_npc_instance_service)
    return getter()


def get_npc_disposition_from_instance(npc_id: str) -> NpcDisposition:
    """Disposition of the live NPC instance ``npc_id``; the default when the instance cannot be found."""
    try:
        lifecycle_manager = _npc_instance_service().lifecycle_manager
        if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
            npc_type: object = getattr(lifecycle_manager.active_npcs[npc_id], "npc_type", None)
            return npc_disposition_from_type(npc_type, npc_id)
    except (AttributeError, ValueError, TypeError, RuntimeError) as e:
        logger.debug("Error getting NPC disposition from instance", npc_id=npc_id, error=str(e))
    return DEFAULT_NPC_DISPOSITION
