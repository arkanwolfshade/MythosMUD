"""
Utility functions for connection management.

This module provides helper functions used by the connection manager
for various utility operations.
"""

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


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
                    return name

        return None
    except (AttributeError, ValueError, TypeError) as e:
        logger.debug("Error getting NPC name from instance", npc_id=npc_id, error=str(e))
        return None
