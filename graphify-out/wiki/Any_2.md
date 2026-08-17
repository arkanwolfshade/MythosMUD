# Any

> 35 nodes

## Key Concepts

- **Any** (13 connections)
- **.get_room()** (8 connections) — `server/game/room_service.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **.filter_rooms_by_exploration()** (6 connections) — `server/game/room_service.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **.list_rooms()** (5 connections) — `server/game/room_service.py`
- **.get_local_chat_scope()** (4 connections) — `server/game/room_service.py`
- **.get_room_exits()** (4 connections) — `server/game/room_service.py`
- **.get_room_occupants()** (4 connections) — `server/game/room_service.py`
- **._extract_occupants_from_room()** (3 connections) — `server/game/room_service.py`
- **.get_environment_state()** (3 connections) — `server/game/room_service.py`
- **.get_room_by_name()** (3 connections) — `server/game/room_service.py`
- **.get_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **.list_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **._lookup_explored_stable_ids()** (3 connections) — `server/game/room_service.py`
- **._prepare_room_for_list()** (3 connections) — `server/game/room_service.py`
- **._room_matches_zone_filters()** (3 connections) — `server/game/room_service.py`
- **.search_rooms_by_name()** (3 connections) — `server/game/room_service.py`
- **.validate_exit_exists()** (3 connections) — `server/game/room_service.py`
- **AsyncSession** (2 connections)
- **UUID** (2 connections)
- **Get a list of rooms adjacent to the specified room. Args: room_id: The room's…** (1 connections) — `server/game/room_service.py`
- **Get the scope of rooms for local chat (current room + adjacent rooms). Args:…** (1 connections) — `server/game/room_service.py`
- **Validate that there's a valid exit from one room to another. Args:…** (1 connections) — `server/game/room_service.py`
- **Get all occupants (players and NPCs) currently in a room using cached data.…** (1 connections) — `server/game/room_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (19 shared connections)

## Source Files

- `server/game/room_service.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*