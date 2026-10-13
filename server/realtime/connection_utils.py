"""
Utility functions for connection management.

This module provides helper functions used by the connection manager
for various utility operations.
"""

from collections.abc import Mapping
from typing import cast

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


def get_npc_disposition_from_instance(npc_id: str) -> NpcDisposition:
    """Disposition of the live NPC instance ``npc_id``; the default when the instance cannot be found."""
    try:
        from ..services.npc_instance_service import get_npc_instance_service

        lifecycle_manager = get_npc_instance_service().lifecycle_manager
        if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
            return npc_disposition_from_type(getattr(lifecycle_manager.active_npcs[npc_id], "npc_type", None), npc_id)
    except (AttributeError, ValueError, TypeError, RuntimeError) as e:
        logger.debug("Error getting NPC disposition from instance", npc_id=npc_id, error=str(e))
    return DEFAULT_NPC_DISPOSITION


def get_npc_name_from_instance(npc_id: str) -> str | None:
    """
    Get NPC name from the actual NPC instance, preserving original case from database.

    This is the proper way to get NPC names - directly from the database via the NPC instance.

    Args:
        npc_id: The NPC ID

    Returns:
        NPC name from the database, or None if instance not found
    """
    try:
        # Get the NPC instance from the lifecycle manager (single source of truth)
        from ..services.npc_instance_service import get_npc_instance_service

        npc_instance_service = get_npc_instance_service()
        if hasattr(npc_instance_service, "lifecycle_manager"):
            lifecycle_manager = npc_instance_service.lifecycle_manager
            if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                npc_instance = lifecycle_manager.active_npcs[npc_id]
                name = getattr(npc_instance, "name", None)
                if name:
                    result: str = cast(str, name)
                    return result

        return None
    except (AttributeError, ValueError, TypeError, RuntimeError) as e:
        logger.debug("Error getting NPC name from instance", npc_id=npc_id, error=str(e))
        return None
