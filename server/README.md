# MythosMUD Server

The backend server for MythosMUD, a Lovecraftian horror MUD game.

## Features

### Core Systems
- **World Loading**: Loads room data from JSON files organized by zones (now in `data/rooms/`)
- **Player Management**: Complete player character system with stats and persistence
- **Real-time Game Loop**: Tick-based game loop for processing game events
- **Status Effects**: Dynamic status effect system for horror mechanics

### Player Data Storage (NEW)
- Player data is stored as individual files in `data/players/player_<GUID>.json`.
- There is no longer a single `players.json` file.
- The server dynamically loads player data from these files after authentication.
- Example: `data/players/player_3ff4b997-1bed-42b9-a96e-0892c9e25357.json`
- A sample player file for tests is provided as `data/players/player_test-id-123.json`.

### Player Stats System

The game features a comprehensive stats system with Lovecraftian horror elements:

#### Core Attributes (1-20 scale)
- **Physical**: Strength, Dexterity, Constitution
- **Mental**: Intelligence, Wisdom, Charisma

#### Horror-Specific Attributes (0-100 scale)
- **Sanity**: Mental stability (0 = complete madness)
- **Occult Knowledge**: Forbidden lore knowledge (causes sanity loss)
- **Fear**: Susceptibility to terror and panic
- **Corruption**: Taint from dark forces
- **Cult Affiliation**: Ties to cults and secret societies

#### Status Effects
- **Stunned**: Unable to act
- **Poisoned**: Damage over time
- **Hallucinating**: Visual/auditory disturbances
- **Paranoid**: Mental instability
- **Trembling**: Reduced dexterity
- **Corrupted**: Physical/mental changes
- **Insane**: Complete mental breakdown

## API Endpoints

### World
- `GET /rooms/{room_id}` - Get room information

### Player Management
- `POST /players` - Create a new player
- `GET /players` - List all players
- `GET /players/{player_id}` - Get player by ID
- `GET /players/name/{player_name}` - Get player by name
- `DELETE /players/{player_id}` - Delete a player

### Player Stats & Effects
- `POST /players/{player_id}/sanity-loss` - Apply sanity loss
- `POST /players/{player_id}/fear` - Apply fear
- `POST /players/{player_id}/corruption` - Apply corruption
- `POST /players/{player_id}/occult-knowledge` - Gain occult knowledge
- `POST /players/{player_id}/heal` - Heal player
- `POST /players/{player_id}/damage` - Damage player

## Running the Server

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Start the server:
   ```bash
   uv run uvicorn main:app --reload
   ```

3. The server will be available at `http://localhost:54731`

## Testing

Run the test script to verify the player stats system:

```bash
python test_player_stats.py
```

## Data Storage

- Player data is stored as individual files in `data/players/player_<GUID>.json`.
- Room data is stored in `data/rooms/`.
- The system automatically creates these directories and handles data persistence.

## Game Mechanics

### Sanity System
- Players start with 100 sanity
- Encountering horrors, reading forbidden texts, or learning occult knowledge reduces sanity
- Low sanity triggers status effects (paranoia, hallucinations, insanity)
- Sanity can be recovered through rest, therapy, or certain items

### Fear System
- Fear accumulates from terrifying encounters
- High fear levels cause trembling and reduced effectiveness
- Fear can be reduced through courage, experience, or certain items

### Corruption System
- Corruption represents taint from dark forces
- High corruption can lead to physical/mental changes
- Corruption is difficult to remove and may be permanent

### Occult Knowledge
- Learning forbidden lore increases occult knowledge
- Each point of occult knowledge gained costs 0.5 sanity
- High occult knowledge provides access to powerful abilities but increases vulnerability

## Development

The server uses:
- **FastAPI** for the web framework
- **Pydantic** for data validation and serialization
- **JSON** for data persistence (can be upgraded to database later)
- **Asyncio** for the game loop

## Future Enhancements

- Database integration (PostgreSQL/DynamoDB)
- WebSocket support for real-time communication
- Combat system integration
- NPC AI and behavior
- Quest system
- Inventory and item management
