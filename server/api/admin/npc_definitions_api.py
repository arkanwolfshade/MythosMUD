"""
NPC definition admin endpoints for MythosMUD.

Split out from server.api.admin.npc to keep that file's NLOC under complexity limits
while preserving the public router import path.
"""

from __future__ import annotations

from typing import Any

from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...auth.users import get_current_user
from ...database import get_async_session
from ...exceptions import LoggedHTTPException
from ...models.user import User
from ...npc_database import get_npc_session
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...services.npc_service import npc_service
from ...structured_logging.enhanced_logging_config import get_logger
from .npc_router_core import npc_router, validate_admin_permission
from .npc_schemas import (
    NPCDefinitionCreate,
    NPCDefinitionResponse,
    NPCDefinitionUpdate,
    build_update_params_from_model,
)

logger = get_logger(__name__)


async def _update_npc_definition_internal(
    definition_id: int,
    npc_data: NPCDefinitionUpdate,
    request: Request,
    current_user: User | None,
    session: AsyncSession,
) -> NPCDefinitionResponse:
    """Internal handler for NPC definition update with full error handling."""
    try:
        validate_admin_permission(current_user, AdminAction.UPDATE_NPC_DEFINITION, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition update requested",
            user=auth_service.get_username(current_user),
            definition_id=definition_id,
        )
        update_params = build_update_params_from_model(npc_data)
        definition = await npc_service.update_npc_definition(
            session=session,
            definition_id=definition_id,
            params=update_params,
        )
        if not definition:
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="NPC definition not found",
                user_id=str(current_user.id) if current_user else None,
                operation="update_npc_definition",
                definition_id=definition_id,
            )
        await session.commit()
        return NPCDefinitionResponse.from_orm(definition)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        await session.rollback()
        logger.error("Error updating NPC definition", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating NPC definition",
        ) from e


@npc_router.get("/definitions", response_model=list[NPCDefinitionResponse])
async def get_npc_definitions(
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> list[NPCDefinitionResponse]:
    """Get all NPC definitions."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_NPC_DEFINITIONS, request)
        auth_service = get_admin_auth_service()
        logger.info("NPC definitions requested", user=auth_service.get_username(current_user))
        definitions = await npc_service.get_npc_definitions(session)
        return [NPCDefinitionResponse.from_orm(defn) for defn in definitions]
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC retrieval errors unpredictable
        logger.error("Error retrieving NPC definitions", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC definitions",
        ) from e


@npc_router.post("/definitions", response_model=NPCDefinitionResponse, status_code=status.HTTP_201_CREATED)
async def create_npc_definition(
    npc_data: NPCDefinitionCreate,
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> NPCDefinitionResponse:
    """Create a new NPC definition."""
    try:
        validate_admin_permission(current_user, AdminAction.CREATE_NPC_DEFINITION, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition creation requested",
            user=auth_service.get_username(current_user),
            name=npc_data.name,
        )
        async for npc_session in get_npc_session():
            base_stats_dict: dict[str, Any] = npc_data.base_stats.model_dump()
            behavior_config_dict: dict[str, Any] = npc_data.behavior_config.model_dump()
            ai_integration_stub_dict: dict[str, Any] = npc_data.ai_integration_stub.model_dump()
            definition = await npc_service.create_npc_definition(
                npc_session,
                {
                    "name": npc_data.name,
                    "description": None,
                    "npc_type": npc_data.npc_type.value,
                    "sub_zone_id": npc_data.sub_zone_id,
                    "room_id": npc_data.room_id,
                    "base_stats": base_stats_dict,
                    "behavior_config": behavior_config_dict,
                    "ai_integration_stub": ai_integration_stub_dict,
                },
            )
            break
        await npc_session.commit()  # pylint: disable=undefined-loop-variable
        return NPCDefinitionResponse.from_orm(definition)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC creation errors unpredictable
        logger.error("Error creating NPC definition", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating NPC definition",
        ) from e


@npc_router.get("/definitions/{definition_id}", response_model=NPCDefinitionResponse)
async def get_npc_definition(
    definition_id: int,
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> NPCDefinitionResponse:
    """Get a specific NPC definition by ID."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_NPC_DEFINITIONS, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition requested",
            user=auth_service.get_username(current_user),
            definition_id=definition_id,
        )
        definition = await npc_service.get_npc_definition(session, definition_id)
        if not definition:
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="NPC definition not found",
                operation="get_npc_definition",
                definition_id=definition_id,
            )
        return NPCDefinitionResponse.from_orm(definition)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC retrieval errors unpredictable
        logger.error("Error retrieving NPC definition", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC definition",
        ) from e


@npc_router.put("/definitions/{definition_id}", response_model=NPCDefinitionResponse)
async def update_npc_definition(
    definition_id: int,
    npc_data: NPCDefinitionUpdate,
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> NPCDefinitionResponse:
    """Update an existing NPC definition."""
    return await _update_npc_definition_internal(definition_id, npc_data, request, current_user, session)


@npc_router.delete("/definitions/{definition_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_npc_definition(
    definition_id: int,
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> None:
    """Delete an NPC definition."""
    try:
        validate_admin_permission(current_user, AdminAction.DELETE_NPC_DEFINITION, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition deletion requested",
            user=auth_service.get_username(current_user),
            definition_id=definition_id,
        )
        deleted = await npc_service.delete_npc_definition(session, definition_id)
        if not deleted:
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="NPC definition not found",
                user_id=str(current_user.id) if current_user else None,
                operation="delete_npc_definition",
                definition_id=definition_id,
            )
        await session.commit()
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC deletion errors unpredictable
        await session.rollback()
        logger.error("Error deleting NPC definition", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting NPC definition",
        ) from e
