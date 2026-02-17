"""Admin domain schemas: NPC admin API responses."""

from .npc_admin import (
    AdminAuditLogResponse,
    AdminCleanupSessionsResponse,
    AdminSessionsResponse,
    NPCDespawnResponse,
    NPCMoveResponse,
    NPCPopulationStatsResponse,
    NPCSpawnResponse,
    NPCStatsResponse,
    NPCSystemStatusResponse,
    NPCZoneStatsResponse,
)

__all__ = [
    "AdminAuditLogResponse",
    "AdminCleanupSessionsResponse",
    "AdminSessionsResponse",
    "NPCDespawnResponse",
    "NPCMoveResponse",
    "NPCPopulationStatsResponse",
    "NPCSpawnResponse",
    "NPCStatsResponse",
    "NPCSystemStatusResponse",
    "NPCZoneStatsResponse",
]
