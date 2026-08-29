"""
Player effects API endpoints.

This module handles endpoints for applying various effects to players,
including lucidity loss, fear, corruption, occult knowledge, healing, and damage.
"""

import uuid

from fastapi import Depends
from fastapi import Request as FastAPIRequest

from ..auth.users import get_current_user
from ..dependencies import PlayerServiceDep
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException, ValidationError
from ..game.player_service import PlayerService
from ..models.user import User
from ..schemas.players import (
    CorruptionRequest,
    DamageRequest,
    EffectResponse,
    FearRequest,
    HealRequest,
    LucidityLossRequest,
    OccultKnowledgeRequest,
)
from ..services.admin_auth_service import AdminAction, get_admin_auth_service
from ..structured_logging.enhanced_logging_config import get_logger
from .player_router import player_router

logger = get_logger(__name__)


@player_router.post("/{player_id}/lucidity-loss", response_model=EffectResponse)
async def apply_lucidity_loss(
    player_id: uuid.UUID,
    request_data: LucidityLossRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Apply lucidity loss to a player.

    Admin-only (#734): no client caller applies effects via this REST surface — real gameplay
    effects (combat, spells, status ticks) call the service layer directly in-process. This
    endpoint is an ops/debug tool and was previously reachable by any bearer of a valid or
    even absent token, with no ownership or role check at all.
    """
    get_admin_auth_service().validate_permission(current_user, AdminAction.APPLY_PLAYER_EFFECT, request)
    try:
        result = await player_service.apply_lucidity_loss(player_id, request_data.amount, request_data.source)
        return EffectResponse(**result)
    except ValidationError as e:
        raise LoggedHTTPException(
            status_code=404,
            detail=ErrorMessages.PLAYER_NOT_FOUND,
            user_id=str(current_user.id) if current_user else None,
            requested_player_id=str(player_id),
        ) from e


@player_router.post("/{player_id}/fear", response_model=EffectResponse)
async def apply_fear(
    player_id: uuid.UUID,
    request_data: FearRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Apply fear to a player. Admin-only (#734) — see apply_lucidity_loss."""
    get_admin_auth_service().validate_permission(current_user, AdminAction.APPLY_PLAYER_EFFECT, request)
    try:
        result = await player_service.apply_fear(player_id, request_data.amount, request_data.source)
        return EffectResponse(**result)
    except ValidationError as e:
        raise LoggedHTTPException(
            status_code=404,
            detail=ErrorMessages.PLAYER_NOT_FOUND,
            user_id=str(current_user.id) if current_user else None,
            requested_player_id=str(player_id),
        ) from e


@player_router.post("/{player_id}/corruption", response_model=EffectResponse)
async def apply_corruption(
    player_id: uuid.UUID,
    request_data: CorruptionRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Apply corruption to a player. Admin-only (#734) — see apply_lucidity_loss."""
    get_admin_auth_service().validate_permission(current_user, AdminAction.APPLY_PLAYER_EFFECT, request)
    try:
        result = await player_service.apply_corruption(player_id, request_data.amount, request_data.source)
        return EffectResponse(**result)
    except ValidationError as e:
        raise LoggedHTTPException(
            status_code=404,
            detail=ErrorMessages.PLAYER_NOT_FOUND,
            user_id=str(current_user.id) if current_user else None,
            requested_player_id=str(player_id),
        ) from e


@player_router.post("/{player_id}/occult-knowledge", response_model=EffectResponse)
async def gain_occult_knowledge(
    player_id: uuid.UUID,
    request_data: OccultKnowledgeRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Gain occult knowledge (with lucidity loss). Admin-only (#734) — see apply_lucidity_loss."""
    get_admin_auth_service().validate_permission(current_user, AdminAction.APPLY_PLAYER_EFFECT, request)
    try:
        result = await player_service.gain_occult_knowledge(player_id, request_data.amount, request_data.source)
        return EffectResponse(**result)
    except ValidationError as e:
        raise LoggedHTTPException(
            status_code=404,
            detail=ErrorMessages.PLAYER_NOT_FOUND,
            user_id=str(current_user.id) if current_user else None,
            requested_player_id=str(player_id),
        ) from e


@player_router.post("/{player_id}/heal", response_model=EffectResponse)
async def heal_player(
    player_id: uuid.UUID,
    request_data: HealRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Heal a player's health. Admin-only (#734) — see apply_lucidity_loss."""
    get_admin_auth_service().validate_permission(current_user, AdminAction.APPLY_PLAYER_EFFECT, request)
    try:
        result = await player_service.heal_player(player_id, request_data.amount)
        return EffectResponse(**result)
    except ValidationError as e:
        raise LoggedHTTPException(
            status_code=404,
            detail=ErrorMessages.PLAYER_NOT_FOUND,
            user_id=str(current_user.id) if current_user else None,
            requested_player_id=str(player_id),
        ) from e


@player_router.post("/{player_id}/damage", response_model=EffectResponse)
async def damage_player(
    player_id: uuid.UUID,
    request_data: DamageRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Damage a player's health. Admin-only (#734) — see apply_lucidity_loss."""
    get_admin_auth_service().validate_permission(current_user, AdminAction.APPLY_PLAYER_EFFECT, request)
    try:
        result = await player_service.damage_player(player_id, request_data.amount, request_data.damage_type)
        return EffectResponse(**result)
    except ValidationError as e:
        raise LoggedHTTPException(
            status_code=404,
            detail=ErrorMessages.PLAYER_NOT_FOUND,
            user_id=str(current_user.id) if current_user else None,
            requested_player_id=str(player_id),
        ) from e
