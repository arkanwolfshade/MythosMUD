"""
NPC spawn rule admin endpoints.

Split out from server.api.admin.npc to keep file NLOC under complexity limits.
"""

from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...auth.users import get_current_user
from ...database import get_async_session
from ...exceptions import LoggedHTTPException
from ...models.user import User
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...services.npc_service import npc_service
from ...structured_logging.enhanced_logging_config import get_logger
from .npc_router_core import npc_router, validate_admin_permission
from .npc_schemas import NPCSpawnRuleCreate, NPCSpawnRuleResponse

logger = get_logger(__name__)


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
        spawn_rules = await npc_service.get_spawn_rules(session)
        return [NPCSpawnRuleResponse.from_orm(rule) for rule in spawn_rules]
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error retrieving NPC spawn rules", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving NPC spawn rules",
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
        spawn_rule = await npc_service.create_spawn_rule(
            session=session,
            npc_definition_id=spawn_rule_data.npc_definition_id,
            sub_zone_id=spawn_rule_data.sub_zone_id,
            min_population=spawn_rule_data.min_population,
            max_population=spawn_rule_data.max_population,
            spawn_conditions=spawn_rule_data.spawn_conditions.model_dump(),
        )
        await session.commit()
        return NPCSpawnRuleResponse.from_orm(spawn_rule)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        await session.rollback()
        logger.error("Error creating NPC spawn rule", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating NPC spawn rule",
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
        deleted = await npc_service.delete_spawn_rule(session, spawn_rule_id)
        if not deleted:
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="NPC spawn rule not found",
                user_id=str(current_user.id) if current_user else None,
                operation="delete_npc_spawn_rule",
                spawn_rule_id=spawn_rule_id,
            )
        await session.commit()
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        await session.rollback()
        logger.error("Error deleting NPC spawn rule", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting NPC spawn rule",
        ) from e
