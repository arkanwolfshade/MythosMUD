# Any

> 35 nodes

## Key Concepts

- **.get_room()** (11 connections) — `server/game/room_service.py`
- **Any** (10 connections)
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **.filter_rooms_by_exploration()** (5 connections) — `server/game/room_service.py`
- **.get_local_chat_scope()** (4 connections) — `server/game/room_service.py`
- **.get_room_occupants()** (4 connections) — `server/game/room_service.py`
- **.get_room_exits()** (4 connections) — `server/game/room_service.py`
- **.get_room_by_name()** (3 connections) — `server/game/room_service.py`
- **.list_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **.validate_room_exists()** (3 connections) — `server/game/room_service.py`
- **.validate_exit_exists()** (3 connections) — `server/game/room_service.py`
- **.validate_player_in_room()** (3 connections) — `server/game/room_service.py`
- **.list_rooms()** (3 connections) — `server/game/room_service.py`
- **.get_environment_state()** (3 connections) — `server/game/room_service.py`
- **.search_rooms_by_name()** (3 connections) — `server/game/room_service.py`
- **.get_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **UUID** (2 connections)
- **AsyncSession** (1 connections)
- **Get room information by room ID with caching.          Args:             room_id** (1 connections) — `server/game/room_service.py`
- **Get room information by room name.          Args:             room_name: The roo** (1 connections) — `server/game/room_service.py`
- **Get a list of all rooms in a specific zone.          Args:             zone_id:** (1 connections) — `server/game/room_service.py`
- **Get a list of rooms adjacent to the specified room.          Args:             r** (1 connections) — `server/game/room_service.py`
- **Get the scope of rooms for local chat (current room + adjacent rooms).** (1 connections) — `server/game/room_service.py`
- **Validate that a room exists using cached data.          Args:             room_i** (1 connections) — `server/game/room_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [AsyncSession](AsyncSession.md) (16 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/game/room_service.py`

## Audit Trail

- EXTRACTED: 97 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*