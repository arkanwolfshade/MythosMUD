"""
Player management API endpoints for MythosMUD server.

This module handles all player-related API operations including
creation, retrieval, listing, and deletion of player characters.
"""

from fastapi import APIRouter, Depends, HTTPException, Request

from ..auth.users import get_current_user
from ..game.player_service import PlayerService
from ..schemas.player import PlayerRead

# Create player router
player_router = APIRouter(prefix="/players", tags=["players"])


@player_router.post("/", response_model=PlayerRead)
def create_player(
    name: str,
    starting_room_id: str = "arkham_001",
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Create a new player character."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    try:
        return player_service.create_player(name, starting_room_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None


@player_router.get("/", response_model=list[PlayerRead])
def list_players(
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get a list of all players."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)
    return player_service.list_players()


@player_router.get("/{player_id}", response_model=PlayerRead)
def get_player(
    player_id: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get a specific player by ID."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    player = player_service.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player


@player_router.get("/name/{player_name}", response_model=PlayerRead)
def get_player_by_name(
    player_name: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get a specific player by name."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    player = player_service.get_player_by_name(player_name)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player


@player_router.delete("/{player_id}")
def delete_player(
    player_id: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Delete a player character."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    success, message = player_service.delete_player(player_id)
    if not success:
        raise HTTPException(status_code=404, detail=message)

    return {"message": message}


# Player stats and effects endpoints
@player_router.post("/{player_id}/sanity-loss")
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


@player_router.post("/{player_id}/fear")
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


@player_router.post("/{player_id}/corruption")
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


@player_router.post("/{player_id}/occult-knowledge")
def gain_occult_knowledge(
    player_id: str,
    amount: int,
    source: str = "unknown",
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Gain occult knowledge (with sanity loss)."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.gain_occult_knowledge(player, amount, source)
    return {"message": f"Gained {amount} occult knowledge for {player.name}"}


@player_router.post("/{player_id}/heal")
def heal_player(
    player_id: str,
    amount: int,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Heal a player's health."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.heal_player(player, amount)
    return {"message": f"Healed {player.name} for {amount} health"}


@player_router.post("/{player_id}/damage")
def damage_player(
    player_id: str,
    amount: int,
    damage_type: str = "physical",
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Damage a player's health."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    persistence.damage_player(player, amount, damage_type)
    return {"message": f"Damaged {player.name} for {amount} {damage_type} damage"}
