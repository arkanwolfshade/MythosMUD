"""
NPC management service for MythosMUD.

This package provides comprehensive NPC management including CRUD operations
for NPC definitions, spawn rules, relationships, and instance management.
Uses PostgreSQL stored procedures for all database access.
"""

from ...structured_logging.enhanced_logging_config import get_logger
from ..npc_service_models import (
    CreateNPCDefinitionInput,
    NPCDefinitionCreateParams,
    NPCDefinitionUpdateParams,
)
from .definition_crud import NPCDefinitionCRUDMixin
from .queries import NPCQueryMixin
from .spawn_rule_crud import NPCSpawnRuleCRUDMixin

logger = get_logger("services.npc_service")


class NPCService(NPCDefinitionCRUDMixin, NPCSpawnRuleCRUDMixin, NPCQueryMixin):
    """
    Comprehensive NPC management service.

    Handles CRUD operations for NPC definitions, spawn rules, relationships,
    and provides integration with the NPC subsystem.
    """

    def __init__(self) -> None:
        """Initialize the NPC service."""
        logger.info("NPCService initialized")


npc_service = NPCService()

__all__ = [
    "NPCService",
    "npc_service",
    "CreateNPCDefinitionInput",
    "NPCDefinitionCreateParams",
    "NPCDefinitionUpdateParams",
]
