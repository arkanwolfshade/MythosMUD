# mythos mud mapbuilder

> 24 nodes

## Key Concepts

- **Coord** (14 connections)
- **RoomID** (12 connections)
- **Room** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **infer_coordinates()** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_process_exit()** (10 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_record_explicit_coords()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_select_start_room_if_needed()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_initialize_bfs_queue()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_unknown_direction()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_coordinate_conflict()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_spatial_collision()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_check_disconnected_rooms()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **run_validator_on_rooms()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Represents a room in the MUD world with its ID, exits, and metadata.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Run user-provided validator function over rooms. It should return a list     of** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Record explicit coordinates from rooms.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Select start room if needed. Returns (start_room, should_early_return).** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Initialize BFS queue with start room.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Handle unknown direction by keeping same coordinates.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Handle when destination already has different coordinates.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Handle when coordinate is already claimed by another room.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Process a single exit during BFS.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Check for disconnected rooms and add warning if found.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **If rooms have coords already, those are used. If some rooms lack coords and** (1 connections) — `data/local/mythos_mud_mapbuilder.py`

## Relationships

- [player room realtime](player_room_realtime.md) (23 shared connections)
- [message nats handler](message_nats_handler.md) (5 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*