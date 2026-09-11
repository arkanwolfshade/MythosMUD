# get_player_impl

> 9 nodes

## Key Concepts

- **get_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **test_get_player_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_players_batch_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **Player** (3 connections)
- **Get a player from the persistence layer (async version).** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Get multiple players from the persistence layer in a single batch operation.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Send initial game_state event to a newly connected player.** (1 connections) — `server/realtime/connection_manager_methods.py`

## Relationships

- [connection_manager.py](connection_manager.py.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [test_connection_manager_methods.py](test_connection_manager_methods.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*