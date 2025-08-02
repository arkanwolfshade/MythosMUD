"""
Game mechanics API endpoints for MythosMUD server.

This module handles all game mechanics-related API operations including
sanity, fear, corruption, healing, and damage mechanics.
"""

from fastapi import APIRouter, Depends, HTTPException, Request

from ..auth.users import get_current_user
from ..game.mechanics import GameMechanicsService

# Create game router
game_router = APIRouter(prefix="/players", tags=["game"])


@game_router.post("/{player_id}/sanity-loss")
def apply_sanity_loss(
    player_id: str,
    amount: int,
    source: str = "unknown",
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Apply sanity loss to a player."""
    persistence = request.app.state.persistence
    mechanics_service = GameMechanicsService(persistence)

    success, message = mechanics_service.apply_sanity_loss(player_id, amount, source)
    if not success:
        raise HTTPException(status_code=404, detail=message)

    return {"message": message}


@game_router.post("/{player_id}/fear")
def apply_fear(
    player_id: str,
    amount: int,
    source: str = "unknown",
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Apply fear to a player."""
    persistence = request.app.state.persistence
    mechanics_service = GameMechanicsService(persistence)

    success, message = mechanics_service.apply_fear(player_id, amount, source)
    if not success:
        raise HTTPException(status_code=404, detail=message)

    return {"message": message}


@game_router.post("/{player_id}/corruption")
def apply_corruption(
    player_id: str,
    amount: int,
    source: str = "unknown",
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Apply corruption to a player."""
    persistence = request.app.state.persistence
    mechanics_service = GameMechanicsService(persistence)

    success, message = mechanics_service.apply_corruption(player_id, amount, source)
    if not success:
        raise HTTPException(status_code=404, detail=message)

    return {"message": message}


@game_router.post("/{player_id}/occult-knowledge")
def gain_occult_knowledge(
    player_id: str,
    amount: int,
    source: str = "unknown",
    request: Request = None,
):
    """Gain occult knowledge (with sanity loss)."""
    persistence = request.app.state.persistence
    mechanics_service = GameMechanicsService(persistence)

    success, message = mechanics_service.gain_occult_knowledge(player_id, amount, source)
    if not success:
        raise HTTPException(status_code=404, detail=message)

    return {"message": message}


@game_router.post("/{player_id}/heal")
def heal_player(
    player_id: str,
    amount: int,
    request: Request = None,
):
    """Heal a player's health."""
    persistence = request.app.state.persistence
    mechanics_service = GameMechanicsService(persistence)

    success, message = mechanics_service.heal_player(player_id, amount)
    if not success:
        raise HTTPException(status_code=404, detail=message)

    return {"message": message}


@game_router.post("/{player_id}/damage")
def damage_player(
    player_id: str,
    amount: int,
    damage_type: str = "physical",
    request: Request = None,
):
    """Damage a player's health."""
    persistence = request.app.state.persistence
    mechanics_service = GameMechanicsService(persistence)

    success, message = mechanics_service.damage_player(player_id, amount, damage_type)
    if not success:
        raise HTTPException(status_code=404, detail=message)

    return {"message": message}
