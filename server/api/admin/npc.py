"""
NPC Admin API endpoints for MythosMUD server.

This module provides administrative API endpoints for managing NPCs,
including CRUD operations for NPC definitions, instance management,
population monitoring, and relationship management.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.
"""

# pylint: disable=too-many-lines  # Reason: NPC admin API requires extensive endpoint handlers for comprehensive NPC management operations

import json
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.ext.asyncio import AsyncSession

# from ...auth.dependencies import get_current_superuser  # Not used yet
from ...auth.users import get_current_user
from ...database import get_async_session
from ...exceptions import LoggedHTTPException
from ...models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from ...models.user import User
from ...npc_database import get_npc_session
from ...schemas.npc_admin import (
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
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...services.npc_instance_service import get_npc_instance_service
from ...services.npc_service import npc_service
from ...structured_logging.enhanced_logging_config import get_logger
from ...utils.error_logging import create_context_from_request

logger = get_logger(__name__)

# Create NPC admin router
npc_router = APIRouter(prefix="/admin/npc", tags=["admin", "npc"])

logger.info("NPC Admin API router initialized")


# --- Pydantic Models for API ---


class NPCBaseStatsModel(BaseModel):
    """Model for NPC base statistics."""

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for flexibility in stats
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    determination_points: int | None = Field(default=None, ge=0, description="Current determination points (DP)")
    max_dp: int | None = Field(default=None, ge=0, description="Maximum determination points")
    magic_points: int | None = Field(default=None, ge=0, description="Current magic points (MP)")
    max_mp: int | None = Field(default=None, ge=0, description="Maximum magic points")
    strength: int | None = Field(default=None, ge=0, description="Strength attribute")
    dexterity: int | None = Field(default=None, ge=0, description="Dexterity attribute")
    constitution: int | None = Field(default=None, ge=0, description="Constitution attribute")
    # Allow other stat fields via extra="allow"


class NPCBehaviorConfigModel(BaseModel):
    """Model for NPC behavior configuration."""

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for flexible behavior config
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    aggression_level: int | None = Field(default=None, ge=0, le=10, description="Aggression level (0-10)")
    wander_radius: int | None = Field(default=None, ge=0, description="Maximum wander radius")
    idle_behavior: str | None = Field(default=None, description="Idle behavior type")
    # Allow other behavior fields via extra="allow"


class NPCAIIntegrationModel(BaseModel):
    """Model for NPC AI integration stub configuration."""

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for future AI integration
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    ai_enabled: bool | None = Field(default=None, description="Whether AI integration is enabled")
    ai_provider: str | None = Field(default=None, description="AI provider identifier")
    # Allow other AI config fields via extra="allow"


class NPCSpawnConditionsModel(BaseModel):
    """Model for NPC spawn conditions."""

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for flexible spawn conditions
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    time_of_day: list[str] | None = Field(default=None, description="Allowed times of day for spawning")
    weather_conditions: list[str] | None = Field(default=None, description="Required weather conditions")
    room_tags: list[str] | None = Field(default=None, description="Required room tags")
    # Allow other condition fields via extra="allow"


class NPCDefinitionCreate(BaseModel):
    """Model for creating NPC definitions."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    name: str = Field(..., min_length=1, max_length=100)
    npc_type: NPCDefinitionType
    sub_zone_id: str = Field(..., min_length=1, max_length=100)
    room_id: str = Field(..., min_length=1, max_length=100)
    base_stats: NPCBaseStatsModel = Field(default_factory=NPCBaseStatsModel)
    behavior_config: NPCBehaviorConfigModel = Field(default_factory=NPCBehaviorConfigModel)
    ai_integration_stub: NPCAIIntegrationModel = Field(default_factory=NPCAIIntegrationModel)


class NPCDefinitionUpdate(BaseModel):
    """Model for updating NPC definitions."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    name: str | None = Field(None, min_length=1, max_length=100)
    npc_type: NPCDefinitionType | None = None
    sub_zone_id: str | None = Field(None, min_length=1, max_length=100)
    room_id: str | None = Field(None, min_length=1, max_length=100)
    base_stats: NPCBaseStatsModel | None = None
    behavior_config: NPCBehaviorConfigModel | None = None
    ai_integration_stub: NPCAIIntegrationModel | None = None


class NPCDefinitionResponse(BaseModel):
    """Model for NPC definition responses."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    npc_type: str
    sub_zone_id: str
    room_id: str | None
    base_stats: NPCBaseStatsModel
    behavior_config: NPCBehaviorConfigModel
    ai_integration_stub: NPCAIIntegrationModel

    @classmethod
    def from_orm(cls, npc_def: NPCDefinition) -> "NPCDefinitionResponse":  # pylint: disable=arguments-renamed  # Reason: Parameter renamed for clarity, parent class uses 'obj'
        """Create response from ORM object."""
        # Parse JSON fields if they're strings
        # At runtime, ORM columns return their actual values (strings), but mypy sees Column[str] types
        # We always convert to string first, then parse JSON
        base_stats_str = str(npc_def.base_stats)
        base_stats_raw = json.loads(base_stats_str) if base_stats_str else {}
        behavior_config_str = str(npc_def.behavior_config)
        behavior_config_raw = json.loads(behavior_config_str) if behavior_config_str else {}
        ai_integration_stub_str = str(npc_def.ai_integration_stub)
        ai_integration_stub_raw = json.loads(ai_integration_stub_str) if ai_integration_stub_str else {}

        # json.loads() always returns a dict (or raises), so we can use it directly
        # Type annotations help mypy understand the types
        base_stats_dict: dict[str, Any] = base_stats_raw if isinstance(base_stats_raw, dict) else {}
        behavior_config_dict: dict[str, Any] = behavior_config_raw if isinstance(behavior_config_raw, dict) else {}
        ai_integration_stub_dict: dict[str, Any] = (
            ai_integration_stub_raw if isinstance(ai_integration_stub_raw, dict) else {}
        )

        return cls(
            id=int(npc_def.id),
            name=str(npc_def.name),
            npc_type=str(npc_def.npc_type),
            sub_zone_id=str(npc_def.sub_zone_id),
            room_id=str(npc_def.room_id),
            base_stats=NPCBaseStatsModel(**base_stats_dict),
            behavior_config=NPCBehaviorConfigModel(**behavior_config_dict),
            ai_integration_stub=NPCAIIntegrationModel(**ai_integration_stub_dict),
        )


class NPCSpawnRequest(BaseModel):
    """Model for NPC spawn requests."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    definition_id: int = Field(..., gt=0)
    room_id: str = Field(..., min_length=1, max_length=100)


class NPCMoveRequest(BaseModel):
    """Model for NPC movement requests."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    room_id: str = Field(..., min_length=1, max_length=100)


class NPCSpawnRuleCreate(BaseModel):
    """Model for creating NPC spawn rules."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    npc_definition_id: int = Field(..., gt=0)
    sub_zone_id: str = Field(..., min_length=1, max_length=50)
    min_population: int = Field(default=0, ge=0)
    max_population: int = Field(default=999, ge=0)
    spawn_conditions: NPCSpawnConditionsModel = Field(default_factory=NPCSpawnConditionsModel)


class NPCSpawnRuleResponse(BaseModel):
    """Model for NPC spawn rule responses."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    npc_definition_id: int
    sub_zone_id: str
    min_population: int
    max_population: int
    spawn_conditions: NPCSpawnConditionsModel

    @classmethod
    def from_orm(cls, spawn_rule: NPCSpawnRule) -> "NPCSpawnRuleResponse":  # pylint: disable=arguments-renamed  # Reason: Parameter renamed for clarity, parent class uses 'obj'
        """Create response from ORM object."""
        # At runtime, ORM columns return their actual values (strings), but mypy sees Column[str] types
        # We always convert to string first, then parse JSON
        spawn_conditions_str = str(spawn_rule.spawn_conditions)
        spawn_conditions_raw = json.loads(spawn_conditions_str) if spawn_conditions_str else {}
        # json.loads() always returns a dict (or raises), so we can use it directly
        # Type annotation helps mypy understand the type
        spawn_conditions_dict: dict[str, Any] = spawn_conditions_raw if isinstance(spawn_conditions_raw, dict) else {}
        return cls(
            id=int(spawn_rule.id),
            npc_definition_id=int(spawn_rule.npc_definition_id),
            sub_zone_id=str(spawn_rule.sub_zone_id),
            min_population=int(spawn_rule.min_population),
            max_population=int(spawn_rule.max_population),
            spawn_conditions=NPCSpawnConditionsModel(**spawn_conditions_dict),
        )


# --- Helper Functions ---


def validate_admin_permission(
    current_user: User | None,
    action: AdminAction,
    request: Request,
) -> None:
    """Validate that the current user has admin permissions for the specified action."""
    auth_service = get_admin_auth_service()
    auth_service.validate_permission(current_user, action, request)


# --- NPC Definition Endpoints ---


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

        # Get NPC definitions from the primary application database session
        definitions = await npc_service.get_npc_definitions(session)

        # Convert to response models
        response_definitions = [NPCDefinitionResponse.from_orm(defn) for defn in definitions]

        return response_definitions

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving NPC definitions", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC definitions",
            context=context,
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
            "NPC definition creation requested", user=auth_service.get_username(current_user), name=npc_data.name
        )

        # Create NPC definition in database using NPC database session
        async for npc_session in get_npc_session():
            # Convert Pydantic models to dicts for service layer
            # These are always Pydantic models (NPCBaseStatsModel, etc.), so call model_dump() directly
            base_stats_dict: dict[str, Any] = npc_data.base_stats.model_dump()
            behavior_config_dict: dict[str, Any] = npc_data.behavior_config.model_dump()
            ai_integration_stub_dict: dict[str, Any] = npc_data.ai_integration_stub.model_dump()
            definition = await npc_service.create_npc_definition(
                session=npc_session,
                name=npc_data.name,
                description=None,  # Not in create model yet
                npc_type=npc_data.npc_type.value,
                sub_zone_id=npc_data.sub_zone_id,
                room_id=npc_data.room_id,
                base_stats=base_stats_dict,
                behavior_config=behavior_config_dict,
                ai_integration_stub=ai_integration_stub_dict,
            )
            break

        # Commit the transaction
        await npc_session.commit()  # pylint: disable=undefined-loop-variable  # Reason: Loop always executes once due to break, npc_session is always defined

        return NPCDefinitionResponse.from_orm(definition)

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC creation errors unpredictable, must create error context
        # Rollback is handled by the session context manager
        context = create_context_from_request(request)
        logger.error("Error creating NPC definition", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating NPC definition", context=context
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
            "NPC definition requested", user=auth_service.get_username(current_user), definition_id=definition_id
        )

        # Get NPC definition from the primary application database session
        definition = await npc_service.get_npc_definition(session, definition_id)

        if not definition:
            context = create_context_from_request(request)
            context.metadata["operation"] = "get_npc_definition"
            context.metadata["definition_id"] = definition_id
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NPC definition not found", context=context
            )

        return NPCDefinitionResponse.from_orm(definition)

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving NPC definition", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving NPC definition", context=context
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
    try:
        validate_admin_permission(current_user, AdminAction.UPDATE_NPC_DEFINITION, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC definition update requested", user=auth_service.get_username(current_user), definition_id=definition_id
        )

        # Update NPC definition in database
        # Convert Pydantic models to dicts for service layer (handle None values)
        # These are always Pydantic models when not None, so call model_dump() directly
        base_stats_dict: dict[str, Any] | None = npc_data.base_stats.model_dump() if npc_data.base_stats else None
        behavior_config_dict: dict[str, Any] | None = (
            npc_data.behavior_config.model_dump() if npc_data.behavior_config else None
        )
        ai_integration_stub_dict: dict[str, Any] | None = (
            npc_data.ai_integration_stub.model_dump() if npc_data.ai_integration_stub else None
        )
        definition = await npc_service.update_npc_definition(
            session=session,
            definition_id=definition_id,
            name=npc_data.name,
            description=None,  # Not in update model yet
            npc_type=npc_data.npc_type.value if npc_data.npc_type else None,
            sub_zone_id=npc_data.sub_zone_id,
            room_id=npc_data.room_id,
            base_stats=base_stats_dict,
            behavior_config=behavior_config_dict,
            ai_integration_stub=ai_integration_stub_dict,
        )

        if not definition:
            context = create_context_from_request(request)
            context.user_id = str(current_user.id) if current_user else None
            context.metadata["operation"] = "update_npc_definition"
            context.metadata["definition_id"] = definition_id
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NPC definition not found", context=context
            )

        # Commit the transaction
        await session.commit()

        return NPCDefinitionResponse.from_orm(definition)

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC update errors unpredictable, must rollback and create error context
        await session.rollback()
        context = create_context_from_request(request)
        logger.error("Error updating NPC definition", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error updating NPC definition", context=context
        ) from e


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

        # Delete NPC definition from database
        deleted = await npc_service.delete_npc_definition(session, definition_id)

        if not deleted:
            context = create_context_from_request(request)
            context.user_id = str(current_user.id) if current_user else None
            context.metadata["operation"] = "delete_npc_definition"
            context.metadata["definition_id"] = definition_id
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NPC definition not found", context=context
            )

        # Commit the transaction
        await session.commit()

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC deletion errors unpredictable, must rollback and create error context
        await session.rollback()
        context = create_context_from_request(request)
        logger.error("Error deleting NPC definition", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting NPC definition", context=context
        ) from e


# --- NPC Instance Management Endpoints ---


@npc_router.get("/instances")
async def get_npc_instances(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> list[dict[str, Any]]:
    """Get all active NPC instances."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_NPC_INSTANCES, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC instances requested", user=auth_service.get_username(current_user))

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Retrieve all active NPC instances
        instances = await instance_service.get_npc_instances()

        logger.info("Retrieved NPC instances", user=auth_service.get_username(current_user))

        return instances

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC instance retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving NPC instances", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving NPC instances", context=context
        ) from e


@npc_router.post("/instances/spawn", response_model=NPCSpawnResponse)
async def spawn_npc_instance(
    spawn_data: NPCSpawnRequest,
    request: Request,
    current_user: User | None = Depends(get_current_user),
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

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Spawn the NPC instance
        result = await instance_service.spawn_npc_instance(
            definition_id=spawn_data.definition_id,
            room_id=spawn_data.room_id,
            reason="admin_spawn",
        )

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC spawned successfully",
            user=auth_service.get_username(current_user),
            npc_id=result["npc_id"],
            definition_id=spawn_data.definition_id,
            room_id=spawn_data.room_id,
        )

        return NPCSpawnResponse(**result)

    except ValueError as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "spawn_npc_instance"
        context.metadata["definition_id"] = spawn_data.definition_id
        context.metadata["room_id"] = spawn_data.room_id
        raise LoggedHTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e), context=context) from e
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error spawning NPC instance", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error spawning NPC instance", context=context
        ) from e


@npc_router.delete("/instances/{npc_id}", response_model=NPCDespawnResponse)
async def despawn_npc_instance(
    npc_id: str,
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> NPCDespawnResponse:
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

        auth_service = get_admin_auth_service()
        logger.info(
            "NPC despawned successfully",
            user=auth_service.get_username(current_user),
            npc_id=npc_id,
            npc_name=result.get("npc_name"),
        )

        return NPCDespawnResponse(**result)

    except ValueError as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "despawn_npc_instance"
        context.metadata["npc_id"] = npc_id
        raise LoggedHTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e), context=context) from e
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC despawn errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error despawning NPC instance", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error despawning NPC instance", context=context
        ) from e


@npc_router.put("/instances/{npc_id}/move", response_model=NPCMoveResponse)
async def move_npc_instance(
    npc_id: str,
    move_data: NPCMoveRequest,
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> NPCMoveResponse:
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

        auth_service = get_admin_auth_service()
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
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "move_npc_instance"
        context.metadata["npc_id"] = npc_id
        context.metadata["room_id"] = move_data.room_id
        raise LoggedHTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e), context=context) from e
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC movement errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error moving NPC instance", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error moving NPC instance", context=context
        ) from e


@npc_router.get("/instances/{npc_id}/stats", response_model=NPCStatsResponse)
async def get_npc_stats(
    npc_id: str,
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> NPCStatsResponse:
    """Get stats for a specific NPC instance."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_NPC_STATS, request)

        auth_service = get_admin_auth_service()
        logger.info("NPC stats requested", user=auth_service.get_username(current_user))

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get NPC stats
        stats = await instance_service.get_npc_stats(npc_id)

        auth_service = get_admin_auth_service()
        logger.info(
            "Retrieved NPC stats",
            user=auth_service.get_username(current_user),
            npc_id=npc_id,
            npc_name=stats.get("name"),
        )

        return NPCStatsResponse(**stats)

    except ValueError as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "get_npc_stats"
        context.metadata["npc_id"] = npc_id
        raise LoggedHTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e), context=context) from e
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC stats retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving NPC stats", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving NPC stats", context=context
        ) from e


# --- Population Monitoring Endpoints ---


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

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get population statistics
        stats = await instance_service.get_population_stats()

        logger.info(
            "Retrieved NPC population stats",
            user=auth_service.get_username(current_user),
            total_npcs=stats.get("total_npcs"),
        )

        return NPCPopulationStatsResponse(**stats)

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC population stats errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving NPC population stats", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC population stats",
            context=context,
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

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get zone statistics
        stats = await instance_service.get_zone_stats()

        auth_service = get_admin_auth_service()
        logger.info(
            "Retrieved NPC zone stats",
            user=auth_service.get_username(current_user),
            total_zones=stats.get("total_zones"),
            total_npcs=stats.get("total_npcs"),
        )

        return NPCZoneStatsResponse(**stats)

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC zone stats errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving NPC zone stats", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving NPC zone stats", context=context
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

        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get system status
        system_status = await instance_service.get_system_stats()

        auth_service = get_admin_auth_service()
        logger.info(
            "Retrieved NPC system status",
            user=auth_service.get_username(current_user),
            system_status=system_status.get("system_status"),
            active_npcs=system_status.get("active_npcs"),
        )

        return NPCSystemStatusResponse(**system_status)

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC system status errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving NPC system status", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC system status",
            context=context,
        ) from e


# --- NPC Spawn Rule Endpoints ---


@npc_router.get("/spawn-rules", response_model=list[NPCSpawnRuleResponse])
async def get_npc_spawn_rules(
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> list[NPCSpawnRuleResponse]:
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
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn rule retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving NPC spawn rules", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC spawn rules",
            context=context,
        ) from e


@npc_router.post("/spawn-rules", response_model=NPCSpawnRuleResponse, status_code=status.HTTP_201_CREATED)
async def create_npc_spawn_rule(
    spawn_rule_data: NPCSpawnRuleCreate,
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> NPCSpawnRuleResponse:
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
            min_population=0,  # Not in create model yet
            max_population=999,  # Not in create model yet
            # spawn_conditions is always a Pydantic model (NPCSpawnConditionsModel), so call model_dump() directly
            spawn_conditions=spawn_rule_data.spawn_conditions.model_dump(),
        )

        # Commit the transaction
        await session.commit()

        return NPCSpawnRuleResponse.from_orm(spawn_rule)

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn rule creation errors unpredictable, must rollback and create error context
        await session.rollback()
        context = create_context_from_request(request)
        logger.error("Error creating NPC spawn rule", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating NPC spawn rule", context=context
        ) from e


@npc_router.delete("/spawn-rules/{spawn_rule_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_npc_spawn_rule(
    spawn_rule_id: int,
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> None:
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
            context = create_context_from_request(request)
            context.user_id = str(current_user.id) if current_user else None
            context.metadata["operation"] = "delete_npc_spawn_rule"
            context.metadata["spawn_rule_id"] = spawn_rule_id
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NPC spawn rule not found", context=context
            )

        # Commit the transaction
        await session.commit()

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn rule deletion errors unpredictable, must rollback and create error context
        await session.rollback()
        context = create_context_from_request(request)
        logger.error("Error deleting NPC spawn rule", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting NPC spawn rule", context=context
        ) from e


# --- Admin Management Endpoints ---


@npc_router.get("/admin/sessions", response_model=AdminSessionsResponse)
async def get_admin_sessions(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> AdminSessionsResponse:
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

        return AdminSessionsResponse(sessions=sessions, count=len(sessions))

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Admin session retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving admin sessions", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving admin sessions", context=context
        ) from e


@npc_router.get("/admin/audit-log", response_model=AdminAuditLogResponse)
async def get_admin_audit_log(
    request: Request,
    limit: int = 100,
    current_user: User | None = Depends(get_current_user),
) -> AdminAuditLogResponse:
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

        return AdminAuditLogResponse(audit_log=audit_log, count=len(audit_log))

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Admin audit log retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error retrieving admin audit log", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving admin audit log",
            context=context,
        ) from e


@npc_router.post("/admin/cleanup-sessions", response_model=AdminCleanupSessionsResponse)
async def cleanup_admin_sessions(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> AdminCleanupSessionsResponse:
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

        return AdminCleanupSessionsResponse(
            message=f"Cleaned up {cleaned_count} expired sessions", cleaned_count=cleaned_count
        )

    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Admin session cleanup errors unpredictable, must create error context
        context = create_context_from_request(request)
        logger.error("Error cleaning up admin sessions", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error cleaning up admin sessions",
            context=context,
        ) from e
