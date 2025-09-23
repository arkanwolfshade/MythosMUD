"""
NPC Admin API endpoints for MythosMUD server.

This module provides administrative API endpoints for managing NPCs,
including CRUD operations for NPC definitions, instance management,
population monitoring, and relationship management.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.
"""

import json
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

# from ...auth.dependencies import get_current_superuser  # Not used yet
from ...auth.users import get_current_user
from ...database import get_async_session
from ...exceptions import LoggedHTTPException
from ...logging_config import get_logger
from ...models.npc import NPCDefinition, NPCDefinitionType, NPCRelationship, NPCRelationshipType, NPCSpawnRule
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...services.npc_instance_service import get_npc_instance_service
from ...services.npc_service import npc_service
from ...utils.error_logging import create_context_from_request

logger = get_logger(__name__)

# Create NPC admin router
npc_router = APIRouter(prefix="/admin/npc", tags=["admin", "npc"])

logger.info("NPC Admin API router initialized", prefix="/admin/npc")


# --- Pydantic Models for API ---


class NPCDefinitionCreate(BaseModel):
    """Model for creating NPC definitions."""

    name: str = Field(..., min_length=1, max_length=100)
    npc_type: NPCDefinitionType
    sub_zone_id: str = Field(..., min_length=1, max_length=100)
    room_id: str = Field(..., min_length=1, max_length=100)
    base_stats: dict[str, Any] = Field(default_factory=dict)
    behavior_config: dict[str, Any] = Field(default_factory=dict)
    ai_integration_stub: dict[str, Any] = Field(default_factory=dict)


class NPCDefinitionUpdate(BaseModel):
    """Model for updating NPC definitions."""

    name: str | None = Field(None, min_length=1, max_length=100)
    npc_type: NPCDefinitionType | None = None
    sub_zone_id: str | None = Field(None, min_length=1, max_length=100)
    room_id: str | None = Field(None, min_length=1, max_length=100)
    base_stats: dict[str, Any] | None = None
    behavior_config: dict[str, Any] | None = None
    ai_integration_stub: dict[str, Any] | None = None


class NPCDefinitionResponse(BaseModel):
    """Model for NPC definition responses."""

    id: int
    name: str
    npc_type: str
    sub_zone_id: str
    room_id: str | None
    base_stats: dict[str, Any]
    behavior_config: dict[str, Any]
    ai_integration_stub: dict[str, Any]

    @classmethod
    def from_orm(cls, npc_def: NPCDefinition) -> "NPCDefinitionResponse":
        """Create response from ORM object."""
        return cls(
            id=npc_def.id,
            name=npc_def.name,
            npc_type=npc_def.npc_type,  # npc_type is stored as string, not enum
            sub_zone_id=npc_def.sub_zone_id,
            room_id=npc_def.room_id,
            base_stats=json.loads(npc_def.base_stats) if isinstance(npc_def.base_stats, str) else npc_def.base_stats,
            behavior_config=json.loads(npc_def.behavior_config)
            if isinstance(npc_def.behavior_config, str)
            else npc_def.behavior_config,
            ai_integration_stub=json.loads(npc_def.ai_integration_stub)
            if isinstance(npc_def.ai_integration_stub, str)
            else npc_def.ai_integration_stub,
        )


class NPCSpawnRequest(BaseModel):
    """Model for NPC spawn requests."""

    definition_id: int = Field(..., gt=0)
    room_id: str = Field(..., min_length=1, max_length=100)


class NPCMoveRequest(BaseModel):
    """Model for NPC movement requests."""

    room_id: str = Field(..., min_length=1, max_length=100)


class NPCRelationshipCreate(BaseModel):
    """Model for creating NPC relationships."""

    npc_id_1: int = Field(..., gt=0)
    npc_id_2: int = Field(..., gt=0)
    relationship_type: NPCRelationshipType
    relationship_strength: float = Field(..., ge=0.0, le=1.0)


class NPCRelationshipResponse(BaseModel):
    """Model for NPC relationship responses."""

    id: int
    npc_id_1: int
    npc_id_2: int
    relationship_type: str
    relationship_strength: float

    @classmethod
    def from_orm(cls, relationship: NPCRelationship) -> "NPCRelationshipResponse":
        """Create response from ORM object."""
        return cls(
            id=relationship.id,
            npc_id_1=relationship.npc_id_1,
            npc_id_2=relationship.npc_id_2,
            relationship_type=relationship.relationship_type,
            relationship_strength=relationship.relationship_strength,
        )


class NPCSpawnRuleCreate(BaseModel):
    """Model for creating NPC spawn rules."""

    npc_definition_id: int = Field(..., gt=0)
    spawn_probability: float = Field(..., ge=0.0, le=1.0)
    max_population: int = Field(..., ge=0)
    spawn_conditions: dict[str, Any] = Field(default_factory=dict)
    required_npc: bool = False


class NPCSpawnRuleResponse(BaseModel):
    """Model for NPC spawn rule responses."""

    id: int
    npc_definition_id: int
    spawn_probability: float
    max_population: int
    spawn_conditions: dict[str, Any]
    required_npc: bool

    @classmethod
    def from_orm(cls, spawn_rule: NPCSpawnRule) -> "NPCSpawnRuleResponse":
        """Create response from ORM object."""
        return cls(
            id=spawn_rule.id,
            npc_definition_id=spawn_rule.npc_definition_id,
            spawn_probability=spawn_rule.spawn_probability,
            max_population=spawn_rule.max_population,
            spawn_conditions=json.loads(spawn_rule.spawn_conditions)
            if isinstance(spawn_rule.spawn_conditions, str)
            else spawn_rule.spawn_conditions,
            required_npc=spawn_rule.required_npc,
        )


# --- Helper Functions ---


def validate_admin_permission(current_user, action: AdminAction, request: Request = None) -> None:
    """Validate that the current user has admin permissions for the specified action."""
    auth_service = get_admin_auth_service()
    auth_service.validate_permission(current_user, action, request)


# --- NPC Definition Endpoints ---


@npc_router.get("/definitions", response_model=list[NPCDefinitionResponse])
async def get_npc_definitions(
    current_user=Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Get all NPC definitions."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_NPC_DEFINITIONS, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC definitions requested", user=auth_service.get_username(current_user))

        # Get NPC definitions from database
        definitions = await npc_service.get_npc_definitions(session)

        # Convert to response models
        response_definitions = [NPCDefinitionResponse.from_orm(defn) for defn in definitions]

        return response_definitions

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC definitions: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC definitions",
            context=context,
        ) from e


@npc_router.post("/definitions", response_model=NPCDefinitionResponse, status_code=status.HTTP_201_CREATED)
async def create_npc_definition(
    npc_data: NPCDefinitionCreate,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Create a new NPC definition."""
    try:
        validate_admin_permission(current_user, AdminAction.CREATE_NPC_DEFINITION, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition creation requested", user=auth_service.get_username(current_user), name=npc_data.name
        )

        # Create NPC definition in database
        definition = await npc_service.create_npc_definition(
            session=session,
            name=npc_data.name,
            description=None,  # Not in create model yet
            npc_type=npc_data.npc_type.value,
            sub_zone_id=npc_data.sub_zone_id,
            room_id=npc_data.room_id,
            base_stats=npc_data.base_stats,
            behavior_config=npc_data.behavior_config,
            ai_integration_stub=npc_data.ai_integration_stub,
        )

        # Commit the transaction
        await session.commit()

        return NPCDefinitionResponse.from_orm(definition)

    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        context = create_context_from_request(request)
        logger.error(f"Error creating NPC definition: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating NPC definition", context=context
        ) from e


@npc_router.get("/definitions/{definition_id}", response_model=NPCDefinitionResponse)
async def get_npc_definition(
    definition_id: int,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Get a specific NPC definition by ID."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_NPC_DEFINITIONS, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition requested", user=auth_service.get_username(current_user), definition_id=definition_id
        )

        # Get NPC definition from database
        definition = await npc_service.get_npc_definition(session, definition_id)

        if not definition:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NPC definition not found")

        return NPCDefinitionResponse.from_orm(definition)

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC definition: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving NPC definition", context=context
        ) from e


@npc_router.put("/definitions/{definition_id}", response_model=NPCDefinitionResponse)
async def update_npc_definition(
    definition_id: int,
    npc_data: NPCDefinitionUpdate,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Update an existing NPC definition."""
    try:
        validate_admin_permission(current_user, AdminAction.UPDATE_NPC_DEFINITION, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition update requested", user=auth_service.get_username(current_user), definition_id=definition_id
        )

        # Update NPC definition in database
        definition = await npc_service.update_npc_definition(
            session=session,
            definition_id=definition_id,
            name=npc_data.name,
            description=None,  # Not in update model yet
            npc_type=npc_data.npc_type.value if npc_data.npc_type else None,
            sub_zone_id=npc_data.sub_zone_id,
            room_id=npc_data.room_id,
            base_stats=npc_data.base_stats,
            behavior_config=npc_data.behavior_config,
            ai_integration_stub=npc_data.ai_integration_stub,
        )

        if not definition:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NPC definition not found")

        # Commit the transaction
        await session.commit()

        return NPCDefinitionResponse.from_orm(definition)

    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        context = create_context_from_request(request)
        logger.error(f"Error updating NPC definition: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error updating NPC definition", context=context
        ) from e


@npc_router.delete("/definitions/{definition_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_npc_definition(
    definition_id: int,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Delete an NPC definition."""
    try:
        validate_admin_permission(current_user, AdminAction.DELETE_NPC_DEFINITION, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition deletion requested",
            user=auth_service.get_username(current_user),
            definition_id=definition_id,
        )

        # Delete NPC definition from database
        deleted = await npc_service.delete_npc_definition(session, definition_id)

        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NPC definition not found")

        # Commit the transaction
        await session.commit()

    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        context = create_context_from_request(request)
        logger.error(f"Error deleting NPC definition: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting NPC definition", context=context
        ) from e


# --- NPC Instance Management Endpoints ---


@npc_router.get("/instances")
async def get_npc_instances(
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get all active NPC instances."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_NPC_INSTANCES, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC instances requested", user=auth_service.get_username(current_user))

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Retrieve all active NPC instances
        instances = await instance_service.get_npc_instances()

        logger.info("Retrieved NPC instances", count=len(instances), user=current_user.get("username"))
        return instances

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC instances: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving NPC instances", context=context
        ) from e


@npc_router.post("/instances/spawn")
async def spawn_npc_instance(
    spawn_data: NPCSpawnRequest,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
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

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Spawn the NPC instance
        result = await instance_service.spawn_npc_instance(
            definition_id=spawn_data.definition_id,
            room_id=spawn_data.room_id,
            reason="admin_spawn",
        )

        logger.info(
            "NPC spawned successfully",
            user=current_user.get("username"),
            npc_id=result["npc_id"],
            definition_id=spawn_data.definition_id,
            room_id=spawn_data.room_id,
        )

        return result

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error spawning NPC instance: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error spawning NPC instance", context=context
        ) from e


@npc_router.delete("/instances/{npc_id}")
async def despawn_npc_instance(
    npc_id: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Despawn an NPC instance."""
    try:
        validate_admin_permission(current_user, AdminAction.DESPAWN_NPC, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC despawn requested", user=auth_service.get_username(current_user), npc_id=npc_id)

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Despawn the NPC instance
        result = await instance_service.despawn_npc_instance(
            npc_id=npc_id,
            reason="admin_despawn",
        )

        logger.info(
            "NPC despawned successfully",
            user=current_user.get("username"),
            npc_id=npc_id,
            npc_name=result.get("npc_name"),
        )

        return result

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error despawning NPC instance: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error despawning NPC instance", context=context
        ) from e


@npc_router.put("/instances/{npc_id}/move")
async def move_npc_instance(
    npc_id: str,
    move_data: NPCMoveRequest,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Move an NPC instance to a different room."""
    try:
        validate_admin_permission(current_user, AdminAction.MOVE_NPC, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC move requested", user=auth_service.get_username(current_user), npc_id=npc_id, room_id=move_data.room_id
        )

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Move the NPC instance
        result = await instance_service.move_npc_instance(
            npc_id=npc_id,
            new_room_id=move_data.room_id,
            reason="admin_move",
        )

        logger.info(
            "NPC moved successfully",
            user=current_user.get("username"),
            npc_id=npc_id,
            npc_name=result.get("npc_name"),
            old_room_id=result.get("old_room_id"),
            new_room_id=result.get("new_room_id"),
        )

        return result

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error moving NPC instance: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error moving NPC instance", context=context
        ) from e


@npc_router.get("/instances/{npc_id}/stats")
async def get_npc_stats(
    npc_id: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get stats for a specific NPC instance."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_NPC_STATS, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC stats requested", user=auth_service.get_username(current_user), npc_id=npc_id)

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get NPC stats
        stats = await instance_service.get_npc_stats(npc_id)

        logger.info(
            "Retrieved NPC stats",
            user=current_user.get("username"),
            npc_id=npc_id,
            npc_name=stats.get("name"),
        )

        return stats

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC stats: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving NPC stats", context=context
        ) from e


# --- Population Monitoring Endpoints ---


@npc_router.get("/population")
async def get_npc_population_stats(
    current_user=Depends(get_current_user),
    request: Request = None,
):
    """Get NPC population statistics."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_POPULATION_STATS, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC population stats requested", user=auth_service.get_username(current_user))

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get population statistics
        stats = await instance_service.get_population_stats()

        logger.info(
            "Retrieved NPC population stats",
            user=auth_service.get_username(current_user),
            total_npcs=stats.get("total_npcs"),
        )

        return stats

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC population stats: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC population stats",
            context=context,
        ) from e


@npc_router.get("/zones")
async def get_npc_zone_stats(
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get NPC zone statistics."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_ZONE_STATS, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC zone stats requested", user=auth_service.get_username(current_user))

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get zone statistics
        stats = await instance_service.get_zone_stats()

        logger.info(
            "Retrieved NPC zone stats",
            user=current_user.get("username"),
            total_zones=stats.get("total_zones"),
            total_npcs=stats.get("total_npcs"),
        )

        return stats

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC zone stats: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving NPC zone stats", context=context
        ) from e


@npc_router.get("/status")
async def get_npc_system_status(
    current_user=Depends(get_current_user),
    request: Request = None,
):
    """Get NPC system status."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_SYSTEM_STATUS, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC system status requested", user=auth_service.get_username(current_user))

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get system status
        status = await instance_service.get_system_stats()

        logger.info(
            "Retrieved NPC system status",
            user=current_user.get("username"),
            system_status=status.get("system_status"),
            active_npcs=status.get("active_npcs"),
        )

        return status

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC system status: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC system status",
            context=context,
        ) from e


# --- NPC Relationship Endpoints ---


@npc_router.get("/relationships", response_model=list[NPCRelationshipResponse])
async def get_npc_relationships(
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Get all NPC relationships."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_NPC_RELATIONSHIPS, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC relationships requested", user=auth_service.get_username(current_user))

        # Get NPC relationships from database
        relationships = await npc_service.get_relationships(session)

        # Convert to response models
        response_relationships = [NPCRelationshipResponse.from_orm(rel) for rel in relationships]

        return response_relationships

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC relationships: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC relationships",
            context=context,
        ) from e


@npc_router.post("/relationships", response_model=NPCRelationshipResponse, status_code=status.HTTP_201_CREATED)
async def create_npc_relationship(
    relationship_data: NPCRelationshipCreate,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Create a new NPC relationship."""
    try:
        validate_admin_permission(current_user, AdminAction.CREATE_NPC_RELATIONSHIP, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC relationship creation requested",
            user=auth_service.get_username(current_user),
            npc_id_1=relationship_data.npc_id_1,
            npc_id_2=relationship_data.npc_id_2,
        )

        # Create NPC relationship in database
        relationship = await npc_service.create_relationship(
            session=session,
            npc_id_1=relationship_data.npc_id_1,
            npc_id_2=relationship_data.npc_id_2,
            relationship_type=relationship_data.relationship_type.value,
            relationship_strength=relationship_data.relationship_strength,
        )

        # Commit the transaction
        await session.commit()

        return NPCRelationshipResponse.from_orm(relationship)

    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        context = create_context_from_request(request)
        logger.error(f"Error creating NPC relationship: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating NPC relationship", context=context
        ) from e


@npc_router.delete("/relationships/{relationship_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_npc_relationship(
    relationship_id: int,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Delete an NPC relationship."""
    try:
        validate_admin_permission(current_user, AdminAction.DELETE_NPC_RELATIONSHIP, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC relationship deletion requested",
            user=auth_service.get_username(current_user),
            relationship_id=relationship_id,
        )

        # Delete NPC relationship from database
        deleted = await npc_service.delete_relationship(session, relationship_id)

        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NPC relationship not found")

        # Commit the transaction
        await session.commit()

    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        context = create_context_from_request(request)
        logger.error(f"Error deleting NPC relationship: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting NPC relationship", context=context
        ) from e


# --- NPC Spawn Rule Endpoints ---


@npc_router.get("/spawn-rules", response_model=list[NPCSpawnRuleResponse])
async def get_npc_spawn_rules(
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Get all NPC spawn rules."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_SPAWN_RULES, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC spawn rules requested", user=auth_service.get_username(current_user))

        # Get NPC spawn rules from database
        spawn_rules = await npc_service.get_spawn_rules(session)

        # Convert to response models
        response_spawn_rules = [NPCSpawnRuleResponse.from_orm(rule) for rule in spawn_rules]

        return response_spawn_rules

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving NPC spawn rules: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC spawn rules",
            context=context,
        ) from e


@npc_router.post("/spawn-rules", response_model=NPCSpawnRuleResponse, status_code=status.HTTP_201_CREATED)
async def create_npc_spawn_rule(
    spawn_rule_data: NPCSpawnRuleCreate,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Create a new NPC spawn rule."""
    try:
        validate_admin_permission(current_user, AdminAction.CREATE_SPAWN_RULE, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC spawn rule creation requested",
            user=auth_service.get_username(current_user),
            npc_definition_id=spawn_rule_data.npc_definition_id,
        )

        # Create NPC spawn rule in database
        spawn_rule = await npc_service.create_spawn_rule(
            session=session,
            npc_definition_id=spawn_rule_data.npc_definition_id,
            sub_zone_id="default",  # Not in create model yet
            min_players=0,  # Not in create model yet
            max_players=999,  # Not in create model yet
            spawn_conditions=spawn_rule_data.spawn_conditions,
        )

        # Commit the transaction
        await session.commit()

        return NPCSpawnRuleResponse.from_orm(spawn_rule)

    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        context = create_context_from_request(request)
        logger.error(f"Error creating NPC spawn rule: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating NPC spawn rule", context=context
        ) from e


@npc_router.delete("/spawn-rules/{spawn_rule_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_npc_spawn_rule(
    spawn_rule_id: int,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    request: Request = None,
):
    """Delete an NPC spawn rule."""
    try:
        validate_admin_permission(current_user, AdminAction.DELETE_SPAWN_RULE, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC spawn rule deletion requested",
            user=auth_service.get_username(current_user),
            spawn_rule_id=spawn_rule_id,
        )

        # Delete NPC spawn rule from database
        deleted = await npc_service.delete_spawn_rule(session, spawn_rule_id)

        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NPC spawn rule not found")

        # Commit the transaction
        await session.commit()

    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        context = create_context_from_request(request)
        logger.error(f"Error deleting NPC spawn rule: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting NPC spawn rule", context=context
        ) from e


# --- Admin Management Endpoints ---


@npc_router.get("/admin/sessions")
async def get_admin_sessions(
    current_user=Depends(get_current_user),
    request: Request = None,
):
    """Get active admin sessions."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_SYSTEM_STATUS, request)

        auth_service = get_admin_auth_service()
        sessions = auth_service.get_active_sessions()

        logger.info(
            "Retrieved admin sessions",
            user=auth_service.get_username(current_user),
            session_count=len(sessions),
        )

        return {"sessions": sessions, "count": len(sessions)}

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving admin sessions: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving admin sessions", context=context
        ) from e


@npc_router.get("/admin/audit-log")
async def get_admin_audit_log(
    limit: int = 100,
    current_user=Depends(get_current_user),
    request: Request = None,
):
    """Get admin audit log."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_SYSTEM_STATUS, request)

        auth_service = get_admin_auth_service()
        audit_log = auth_service.get_audit_log(limit)

        logger.info(
            "Retrieved admin audit log",
            user=auth_service.get_username(current_user),
            limit=limit,
            entries=len(audit_log),
        )

        return {"audit_log": audit_log, "count": len(audit_log)}

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error retrieving admin audit log: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving admin audit log",
            context=context,
        ) from e


@npc_router.post("/admin/cleanup-sessions")
async def cleanup_admin_sessions(
    current_user=Depends(get_current_user),
    request: Request = None,
):
    """Clean up expired admin sessions."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_SYSTEM_STATUS, request)

        auth_service = get_admin_auth_service()
        cleaned_count = auth_service.cleanup_expired_sessions()

        logger.info(
            "Cleaned up admin sessions",
            user=auth_service.get_username(current_user),
            cleaned_count=cleaned_count,
        )

        return {"message": f"Cleaned up {cleaned_count} expired sessions", "cleaned_count": cleaned_count}

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        logger.error(f"Error cleaning up admin sessions: {str(e)}", context=context)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error cleaning up admin sessions",
            context=context,
        ) from e
