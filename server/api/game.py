"""
Game mechanics API endpoints for MythosMUD server.

This module handles all game mechanics-related API operations including
sanity, fear, corruption, healing, and damage mechanics.
"""

from fastapi import APIRouter, Depends, HTTPException, Request

from ..auth.users import get_current_user

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
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.apply_sanity_loss(player, amount, source)
    return {"message": f"Applied {amount} sanity loss to {player.name}"}


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
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.apply_fear(player, amount, source)
    return {"message": f"Applied {amount} fear to {player.name}"}


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
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.apply_corruption(player, amount, source)
    return {"message": f"Applied {amount} corruption to {player.name}"}


@game_router.post("/{player_id}/occult-knowledge")
def gain_occult_knowledge(
    player_id: str,
    amount: int,
    source: str = "unknown",
    request: Request = None,
):
    """Gain occult knowledge (with sanity loss)."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.gain_occult_knowledge(player, amount, source)
    return {"message": f"Gained {amount} occult knowledge for {player.name}"}


@game_router.post("/{player_id}/heal")
def heal_player(
    player_id: str,
    amount: int,
    request: Request = None,
):
    """Heal a player's health."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.heal_player(player, amount)
    return {"message": f"Healed {player.name} for {amount} health"}


@game_router.post("/{player_id}/damage")
def damage_player(
    player_id: str,
    amount: int,
    damage_type: str = "physical",
    request: Request = None,
):
    """Damage a player's health."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.damage_player(player, amount, damage_type)
    return {"message": f"Damaged {player.name} for {amount} {damage_type} damage"}
