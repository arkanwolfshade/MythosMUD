from fastapi import FastAPI, HTTPException
import asyncio
import logging
from server.world_loader import load_rooms
from server.player_manager import PlayerManager
from server.models import Player
from typing import List
from server.auth import router as auth_router
from server.command_handler import router as command_router
from contextlib import asynccontextmanager


TICK_INTERVAL = 1.0  # seconds


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    app.state.rooms = load_rooms()
    app.state.player_manager = PlayerManager()
    asyncio.create_task(game_tick_loop(app))
    yield
    # (Optional) Add shutdown logic here


app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
app.include_router(command_router)


async def game_tick_loop(app: FastAPI):
    tick_count = 0
    while True:
        app.state.player_manager.process_status_effects(tick_count)
        logging.info(f"Game tick {tick_count}!")
        tick_count += 1
        await asyncio.sleep(TICK_INTERVAL)


@app.get("/")
def read_root():
    return {"message": "Welcome to MythosMUD!"}


@app.get("/rooms/{room_id}")
def get_room(room_id: str):
    room = app.state.rooms.get(room_id)
    if not room:
        return {"error": "Room not found"}
    return room


# Player management endpoints
@app.post("/players", response_model=Player)
def create_player(name: str, starting_room_id: str = "arkham_001"):
    """Create a new player character."""
    # Check if player name already exists
    existing_player = app.state.player_manager.get_player_by_name(name)
    if existing_player:
        raise HTTPException(status_code=400, detail="Player name already exists")

    player = app.state.player_manager.create_player(name, starting_room_id)
    return player


@app.get("/players", response_model=List[Player])
def list_players():
    """Get a list of all players."""
    return app.state.player_manager.list_players()


@app.get("/players/{player_id}", response_model=Player)
def get_player(player_id: str):
    """Get a specific player by ID."""
    player = app.state.player_manager.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.get("/players/name/{player_name}", response_model=Player)
def get_player_by_name(player_name: str):
    """Get a specific player by name."""
    player = app.state.player_manager.get_player_by_name(player_name)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.delete("/players/{player_id}")
def delete_player(player_id: str):
    """Delete a player character."""
    success = app.state.player_manager.delete_player(player_id)
    if not success:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"message": "Player deleted successfully"}


# Player stats and effects endpoints
@app.post("/players/{player_id}/sanity-loss")
def apply_sanity_loss(player_id: str, amount: int, source: str = "unknown"):
    """Apply sanity loss to a player."""
    player = app.state.player_manager.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.player_manager.apply_sanity_loss(player, amount, source)
    return {"message": f"Applied {amount} sanity loss to {player.name}"}


@app.post("/players/{player_id}/fear")
def apply_fear(player_id: str, amount: int, source: str = "unknown"):
    """Apply fear to a player."""
    player = app.state.player_manager.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.player_manager.apply_fear(player, amount, source)
    return {"message": f"Applied {amount} fear to {player.name}"}


@app.post("/players/{player_id}/corruption")
def apply_corruption(player_id: str, amount: int, source: str = "unknown"):
    """Apply corruption to a player."""
    player = app.state.player_manager.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.player_manager.apply_corruption(player, amount, source)
    return {"message": f"Applied {amount} corruption to {player.name}"}


@app.post("/players/{player_id}/occult-knowledge")
def gain_occult_knowledge(player_id: str, amount: int, source: str = "unknown"):
    """Gain occult knowledge (with sanity loss)."""
    player = app.state.player_manager.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.player_manager.gain_occult_knowledge(player, amount, source)
    return {"message": f"Gained {amount} occult knowledge for {player.name}"}


@app.post("/players/{player_id}/heal")
def heal_player(player_id: str, amount: int):
    """Heal a player's health."""
    player = app.state.player_manager.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.player_manager.heal_player(player, amount)
    return {"message": f"Healed {player.name} for {amount} health"}


@app.post("/players/{player_id}/damage")
def damage_player(player_id: str, amount: int, damage_type: str = "physical"):
    """Damage a player's health."""
    player = app.state.player_manager.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.player_manager.damage_player(player, amount, damage_type)
    return {"message": f"Damaged {player.name} for {amount} {damage_type} damage"}
