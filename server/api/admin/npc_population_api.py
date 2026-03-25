"""
NPC population and system status admin endpoints.

Split out from server.api.admin.npc to keep file NLOC under complexity limits.
"""

from fastapi import Depends, HTTPException, Request, status

from ...auth.users import get_current_user
from ...exceptions import LoggedHTTPException
from ...models.user import User
from ...schemas.admin import (
    NPCPopulationStatsResponse,
    NPCSystemStatusResponse,
    NPCZoneStatsResponse,
)
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...services.npc_instance_service import get_npc_instance_service
from ...structured_logging.enhanced_logging_config import get_logger
from .npc_router_core import npc_router, validate_admin_permission

logger = get_logger(__name__)


@npc_router.get("/population", response_model=NPCPopulationStatsResponse)
async def get_npc_population_stats(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> NPCPopulationStatsResponse:
    """Get NPC population statistics."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_POPULATION_STATS, request)
        auth_service = get_admin_auth_service()
        logger.info("NPC population stats requested", user=auth_service.get_username(current_user))
        instance_service = get_npc_instance_service()
        stats = await instance_service.get_population_stats()
        logger.info(
            "Retrieved NPC population stats",
            user=auth_service.get_username(current_user),
            total_npcs=stats.get("total_npcs"),
        )
        return NPCPopulationStatsResponse(**stats)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error retrieving NPC population stats", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC population stats",
        ) from e


@npc_router.get("/zones", response_model=NPCZoneStatsResponse)
async def get_npc_zone_stats(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> NPCZoneStatsResponse:
    """Get NPC zone statistics."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_ZONE_STATS, request)
        auth_service = get_admin_auth_service()
        logger.info("NPC zone stats requested", user=auth_service.get_username(current_user))
        instance_service = get_npc_instance_service()
        stats = await instance_service.get_zone_stats()
        logger.info(
            "Retrieved NPC zone stats",
            user=auth_service.get_username(current_user),
            total_zones=stats.get("total_zones"),
            total_npcs=stats.get("total_npcs"),
        )
        return NPCZoneStatsResponse(**stats)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error retrieving NPC zone stats", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC zone stats",
        ) from e


@npc_router.get("/status", response_model=NPCSystemStatusResponse)
async def get_npc_system_status(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> NPCSystemStatusResponse:
    """Get NPC system status."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_SYSTEM_STATUS, request)
        auth_service = get_admin_auth_service()
        logger.info("NPC system status requested", user=auth_service.get_username(current_user))
        instance_service = get_npc_instance_service()
        system_status = await instance_service.get_system_stats()
        logger.info(
            "Retrieved NPC system status",
            user=auth_service.get_username(current_user),
            system_status=system_status.get("system_status"),
            active_npcs=system_status.get("active_npcs"),
        )
        return NPCSystemStatusResponse(**system_status)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error retrieving NPC system status", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC system status",
        ) from e
