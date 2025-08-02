"""
Player management API endpoints for MythosMUD server.

This module handles all player-related API operations including
creation, retrieval, listing, and deletion of player characters.
"""

import datetime
import uuid

from fastapi import APIRouter, Depends, HTTPException, Request

from ..alias_storage import AliasStorage
from ..auth.users import get_current_user
from ..models.player import Player
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
    existing_player = persistence.get_player_by_name(name)
    if existing_player:
        raise HTTPException(status_code=400, detail="Player name already exists")

    # For now, create a temporary user_id - in a real app this would come
    # from authentication
    temp_user_id = uuid.uuid4()
    current_time = datetime.datetime.now()
    player = Player(
        player_id=uuid.uuid4(),
        user_id=temp_user_id,
        name=name,
        current_room_id=starting_room_id,
        experience_points=0,
        level=1,
        created_at=current_time,
        last_active=current_time,
    )
    persistence.save_player(player)

    # Convert Player model to PlayerRead schema format
    return PlayerRead(
        id=player.player_id,
        user_id=player.user_id,
        name=player.name,
        current_room_id=player.current_room_id,
        experience_points=player.experience_points,
        level=player.level,
        stats=player.get_stats(),
        inventory=player.get_inventory(),
        status_effects=player.get_status_effects(),
        created_at=player.created_at,
        last_active=player.last_active,
    )


@player_router.get("/", response_model=list[PlayerRead])
def list_players(
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get a list of all players."""
    persistence = request.app.state.persistence
    players = persistence.list_players()
    result = []
    for player in players:
        if hasattr(player, "player_id"):  # Player object
            result.append(
                PlayerRead(
                    id=player.player_id,
                    user_id=player.user_id,
                    name=player.name,
                    current_room_id=player.current_room_id,
                    experience_points=player.experience_points,
                    level=player.level,
                    stats=player.get_stats(),
                    inventory=player.get_inventory(),
                    status_effects=player.get_status_effects(),
                    created_at=player.created_at,
                    last_active=player.last_active,
                )
            )
        else:  # Dictionary
            result.append(
                PlayerRead(
                    id=player["player_id"],
                    user_id=player["user_id"],
                    name=player["name"],
                    current_room_id=player["current_room_id"],
                    experience_points=player["experience_points"],
                    level=player["level"],
                    stats=player["stats"],
                    inventory=player["inventory"],
                    status_effects=player["status_effects"],
                    created_at=player["created_at"],
                    last_active=player["last_active"],
                )
            )
    return result


@player_router.get("/{player_id}", response_model=PlayerRead)
def get_player(
    player_id: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get a specific player by ID."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    if hasattr(player, "player_id"):  # Player object
        return PlayerRead(
            id=player.player_id,
            user_id=player.user_id,
            name=player.name,
            current_room_id=player.current_room_id,
            experience_points=player.experience_points,
            level=player.level,
            stats=player.get_stats(),
            inventory=player.get_inventory(),
            status_effects=player.get_status_effects(),
            created_at=player.created_at,
            last_active=player.last_active,
        )
    else:  # Dictionary
        return PlayerRead(
            id=player["player_id"],
            user_id=player["user_id"],
            name=player["name"],
            current_room_id=player["current_room_id"],
            experience_points=player["experience_points"],
            level=player["level"],
            stats=player["stats"],
            inventory=player["inventory"],
            status_effects=player["status_effects"],
            created_at=player["created_at"],
            last_active=player["last_active"],
        )


@player_router.get("/name/{player_name}", response_model=PlayerRead)
def get_player_by_name(
    player_name: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Get a specific player by name."""
    persistence = request.app.state.persistence
    player = persistence.get_player_by_name(player_name)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    if hasattr(player, "player_id"):  # Player object
        return PlayerRead(
            id=player.player_id,
            user_id=player.user_id,
            name=player.name,
            current_room_id=player.current_room_id,
            experience_points=player.experience_points,
            level=player.level,
            stats=player.get_stats(),
            inventory=player.get_inventory(),
            status_effects=player.get_status_effects(),
            created_at=player.created_at,
            last_active=player.last_active,
        )
    else:  # Dictionary
        return PlayerRead(
            id=player["player_id"],
            user_id=player["user_id"],
            name=player["name"],
            current_room_id=player["current_room_id"],
            experience_points=player["experience_points"],
            level=player["level"],
            stats=player["stats"],
            inventory=player["inventory"],
            status_effects=player["status_effects"],
            created_at=player["created_at"],
            last_active=player["last_active"],
        )


@player_router.delete("/{player_id}")
def delete_player(
    player_id: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Delete a player character."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    # Delete the player from the database
    success = persistence.delete_player(player_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete player")

    # Delete player aliases if they exist
    alias_storage = AliasStorage()
    alias_storage.delete_player_aliases(player.name)

    return {"message": f"Player {player.name} has been deleted"}
