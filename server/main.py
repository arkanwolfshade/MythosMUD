import asyncio
import datetime
import logging
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from server.auth import router as auth_router
from server.command_handler import router as command_router
from server.models import Player, Stats
from server.persistence import get_persistence

TICK_INTERVAL = 1.0  # seconds


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    app.state.persistence = get_persistence()
    asyncio.create_task(game_tick_loop(app))
    yield
    # (Optional) Add shutdown logic here


app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
app.include_router(command_router)


async def game_tick_loop(app: FastAPI):
    tick_count = 0
    while True:
        # TODO: Implement status/effect ticks using persistence layer
        logging.info(f"Game tick {tick_count}!")
        tick_count += 1
        await asyncio.sleep(TICK_INTERVAL)


@app.get("/")
def read_root():
    return {"message": "Welcome to MythosMUD!"}


@app.get("/rooms/{room_id}")
def get_room(room_id: str):
    room = app.state.persistence.get_room(room_id)
    if not room:
        return {"error": "Room not found"}
    return room


# Player management endpoints
@app.post("/players", response_model=Player)
def create_player(name: str, starting_room_id: str = "arkham_001"):
    """Create a new player character."""
    existing_player = app.state.persistence.get_player_by_name(name)
    if existing_player:
        raise HTTPException(status_code=400, detail="Player name already exists")
    player = Player(
        id=str(uuid.uuid4()),
        name=name,
        stats=Stats(),
        current_room_id=starting_room_id,
        created_at=datetime.datetime.utcnow(),
        last_active=datetime.datetime.utcnow(),
        experience_points=0,
        level=1,
    )
    app.state.persistence.save_player(player)
    return player


@app.get("/players", response_model=list[Player])
def list_players():
    """Get a list of all players."""
    return app.state.persistence.list_players()


@app.get("/players/{player_id}", response_model=Player)
def get_player(player_id: str):
    """Get a specific player by ID."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.get("/players/name/{player_name}", response_model=Player)
def get_player_by_name(player_name: str):
    """Get a specific player by name."""
    player = app.state.persistence.get_player_by_name(player_name)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.delete("/players/{player_id}")
def delete_player(player_id: str):
    """Delete a player character."""
    # TODO: Implement delete_player in PersistenceLayer
    # For now, raise NotImplementedError
    raise NotImplementedError("delete_player not yet implemented in PersistenceLayer")


# Player stats and effects endpoints
@app.post("/players/{player_id}/sanity-loss")
def apply_sanity_loss(player_id: str, amount: int, source: str = "unknown"):
    """Apply sanity loss to a player."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.apply_sanity_loss(player, amount, source)
    return {"message": f"Applied {amount} sanity loss to {player.name}"}


@app.post("/players/{player_id}/fear")
def apply_fear(player_id: str, amount: int, source: str = "unknown"):
    """Apply fear to a player."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.apply_fear(player, amount, source)
    return {"message": f"Applied {amount} fear to {player.name}"}


@app.post("/players/{player_id}/corruption")
def apply_corruption(player_id: str, amount: int, source: str = "unknown"):
    """Apply corruption to a player."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.apply_corruption(player, amount, source)
    return {"message": f"Applied {amount} corruption to {player.name}"}


@app.post("/players/{player_id}/occult-knowledge")
def gain_occult_knowledge(player_id: str, amount: int, source: str = "unknown"):
    """Gain occult knowledge (with sanity loss)."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.gain_occult_knowledge(player, amount, source)
    return {"message": f"Gained {amount} occult knowledge for {player.name}"}


@app.post("/players/{player_id}/heal")
def heal_player(player_id: str, amount: int):
    """Heal a player's health."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.heal_player(player, amount)
    return {"message": f"Healed {player.name} for {amount} health"}


@app.post("/players/{player_id}/damage")
def damage_player(player_id: str, amount: int, damage_type: str = "physical"):
    """Damage a player's health."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.damage_player(player, amount, damage_type)
    return {"message": f"Damaged {player.name} for {amount} {damage_type} damage"}
