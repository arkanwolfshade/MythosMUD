"""
NPC instance admin endpoints (spawn, despawn, move, stats).

Split out from server.api.admin.npc to keep file NLOC under complexity limits.
"""

from typing import Any

from fastapi import Depends, HTTPException, Request, status

from ...auth.users import get_current_user
from ...exceptions import LoggedHTTPException
from ...schemas.admin import NPCDespawnResponse, NPCMoveResponse, NPCSpawnResponse, NPCStatsResponse
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...services.npc_instance_service import get_npc_instance_service
from ...structured_logging.enhanced_logging_config import get_logger
from .npc_router_core import npc_router, validate_admin_permission
from .npc_schemas import NPCMoveRequest, NPCSpawnRequest

logger = get_logger(__name__)


@npc_router.get("/instances")
async def get_npc_instances(
    request: Request,
    current_user: Any = Depends(get_current_user),
) -> list[dict[str, Any]]:
    """Get all active NPC instances."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_NPC_INSTANCES, request)
        auth_service = get_admin_auth_service()
        logger.info("NPC instances requested", user=auth_service.get_username(current_user))
        instance_service = get_npc_instance_service()
        instances = await instance_service.get_npc_instances()
        logger.info("Retrieved NPC instances", user=auth_service.get_username(current_user))
        return instances
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error retrieving NPC instances", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC instances",
        ) from e


@npc_router.post("/instances/spawn", response_model=NPCSpawnResponse)
async def spawn_npc_instance(
    spawn_data: NPCSpawnRequest,
    request: Request,
    current_user: Any = Depends(get_current_user),
) -> NPCSpawnResponse:
    """Spawn a new NPC instance."""
    try:
        validate_admin_permission(current_user, AdminAction.SPAWN_NPC, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "NPC spawn requested",
            user=auth_service.get_username(current_user),
            definition_id=spawn_data.definition_id,
            room_id=spawn_data.room_id,
        )
        instance_service = get_npc_instance_service()
        result = await instance_service.spawn_npc_instance(
            definition_id=spawn_data.definition_id,
            room_id=spawn_data.room_id,
            reason="admin_spawn",
        )
        logger.info(
            "NPC spawned successfully",
            user=auth_service.get_username(current_user),
            npc_id=result["npc_id"],
            definition_id=spawn_data.definition_id,
            room_id=spawn_data.room_id,
        )
        return NPCSpawnResponse(**result)
    except ValueError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
            user_id=str(current_user.id) if current_user else None,
            operation="spawn_npc_instance",
            definition_id=spawn_data.definition_id,
            room_id=spawn_data.room_id,
        ) from e
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error spawning NPC instance", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error spawning NPC instance",
        ) from e


@npc_router.delete("/instances/{npc_id}", response_model=NPCDespawnResponse)
async def despawn_npc_instance(
    npc_id: str,
    request: Request,
    current_user: Any = Depends(get_current_user),
) -> NPCDespawnResponse:
    """Despawn an NPC instance."""
    try:
        validate_admin_permission(current_user, AdminAction.DESPAWN_NPC, request)
        auth_service = get_admin_auth_service()
        logger.info("NPC despawn requested", user=auth_service.get_username(current_user), npc_id=npc_id)
        instance_service = get_npc_instance_service()
        result = await instance_service.despawn_npc_instance(npc_id=npc_id, reason="admin_despawn")
        logger.info(
            "NPC despawned successfully",
            user=auth_service.get_username(current_user),
            npc_id=npc_id,
            npc_name=result.get("npc_name"),
        )
        return NPCDespawnResponse(**result)
    except ValueError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
            user_id=str(current_user.id) if current_user else None,
            operation="despawn_npc_instance",
            npc_id=npc_id,
        ) from e
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error despawning NPC instance", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error despawning NPC instance",
        ) from e


@npc_router.put("/instances/{npc_id}/move", response_model=NPCMoveResponse)
async def move_npc_instance(
    npc_id: str,
    move_data: NPCMoveRequest,
    request: Request,
    current_user: Any = Depends(get_current_user),
) -> NPCMoveResponse:
    """Move an NPC instance to a different room."""
    try:
        validate_admin_permission(current_user, AdminAction.MOVE_NPC, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "NPC move requested",
            user=auth_service.get_username(current_user),
            npc_id=npc_id,
            room_id=move_data.room_id,
        )
        instance_service = get_npc_instance_service()
        result = await instance_service.move_npc_instance(
            npc_id=npc_id,
            new_room_id=move_data.room_id,
            reason="admin_move",
        )
        logger.info(
            "NPC moved successfully",
            user=auth_service.get_username(current_user),
            npc_id=npc_id,
            npc_name=result.get("npc_name"),
            old_room_id=result.get("old_room_id"),
            new_room_id=result.get("new_room_id"),
        )
        return NPCMoveResponse(**result)
    except ValueError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
            user_id=str(current_user.id) if current_user else None,
            operation="move_npc_instance",
            npc_id=npc_id,
            room_id=move_data.room_id,
        ) from e
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error moving NPC instance", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error moving NPC instance",
        ) from e


@npc_router.get("/instances/{npc_id}/stats", response_model=NPCStatsResponse)
async def get_npc_stats(
    npc_id: str,
    request: Request,
    current_user: Any = Depends(get_current_user),
) -> NPCStatsResponse:
    """Get stats for a specific NPC instance."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_NPC_STATS, request)
        auth_service = get_admin_auth_service()
        logger.info("NPC stats requested", user=auth_service.get_username(current_user))
        instance_service = get_npc_instance_service()
        stats = await instance_service.get_npc_stats(npc_id)
        logger.info(
            "Retrieved NPC stats",
            user=auth_service.get_username(current_user),
            npc_id=npc_id,
            npc_name=stats.get("name"),
        )
        return NPCStatsResponse(**stats)
    except ValueError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
            user_id=str(current_user.id) if current_user else None,
            operation="get_npc_stats",
            npc_id=npc_id,
        ) from e
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error retrieving NPC stats", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC stats",
        ) from e
