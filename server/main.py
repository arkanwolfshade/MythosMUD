from fastapi import FastAPI
import asyncio
import logging
from world_loader import load_rooms

app = FastAPI()

TICK_INTERVAL = 1.0  # seconds


@app.on_event("startup")
async def start_game_tick_loop():
    # Load all rooms at startup and store in app state
    app.state.rooms = load_rooms()
    asyncio.create_task(game_tick_loop())


async def game_tick_loop():
    while True:
        # Placeholder: Insert game logic here (combat, NPCs, etc.)
        logging.info("Game tick!")
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
