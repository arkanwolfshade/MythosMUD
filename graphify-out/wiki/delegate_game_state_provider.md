# delegate_game_state_provider

> 11 nodes

## Key Concepts

- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **get_room_occupants_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **convert_room_players_uuids_to_names_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **test_delegate_game_state_provider_none()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_game_state_provider_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_get_room_occupants_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **Generic delegate for game state provider methods. Args: game_state_provider:…** (1 connections) — `server/realtime/connection_delegates.py`
- **Convert player UUIDs and NPC IDs in room_data to names.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Get list of occupants in a room.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Test delegate_game_state_provider() successfully delegates to provider.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test delegate_game_state_provider() returns default when provider is None.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`

## Relationships

- [test_connection_delegates.py](test_connection_delegates.py.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [asyncio](asyncio.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_delegates.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*