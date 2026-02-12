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
from ..structured_logging.enhanced_logging_config import get_logger
from .player_helpers import create_error_context
from .players import player_router

logger = get_logger(__name__)


@player_router.post("/{player_id}/lucidity-loss", response_model=EffectResponse)
async def apply_lucidity_loss(
    player_id: uuid.UUID,
    request_data: LucidityLossRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Apply lucidity loss to a player."""
    try:
        result = await player_service.apply_lucidity_loss(player_id, request_data.amount, request_data.source)
        return EffectResponse(**result)
    except ValidationError as e:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/fear", response_model=EffectResponse)
async def apply_fear(
    player_id: uuid.UUID,
    request_data: FearRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Apply fear to a player."""
    try:
        result = await player_service.apply_fear(player_id, request_data.amount, request_data.source)
        return EffectResponse(**result)
    except ValidationError as e:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/corruption", response_model=EffectResponse)
async def apply_corruption(
    player_id: uuid.UUID,
    request_data: CorruptionRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Apply corruption to a player."""
    try:
        result = await player_service.apply_corruption(player_id, request_data.amount, request_data.source)
        return EffectResponse(**result)
    except ValidationError as e:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/occult-knowledge", response_model=EffectResponse)
async def gain_occult_knowledge(
    player_id: uuid.UUID,
    request_data: OccultKnowledgeRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Gain occult knowledge (with lucidity loss)."""
    try:
        result = await player_service.gain_occult_knowledge(player_id, request_data.amount, request_data.source)
        return EffectResponse(**result)
    except ValidationError as e:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/heal", response_model=EffectResponse)
async def heal_player(
    player_id: uuid.UUID,
    request_data: HealRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Heal a player's health."""
    try:
        result = await player_service.heal_player(player_id, request_data.amount)
        return EffectResponse(**result)
    except ValidationError as e:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/damage", response_model=EffectResponse)
async def damage_player(
    player_id: uuid.UUID,
    request_data: DamageRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> EffectResponse:
    """Damage a player's health."""
    try:
        result = await player_service.damage_player(player_id, request_data.amount, request_data.damage_type)
        return EffectResponse(**result)
    except ValidationError as e:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e
