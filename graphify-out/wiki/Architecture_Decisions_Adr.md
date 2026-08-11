# Architecture Decisions Adr

> 32 nodes

## Key Concepts

- **mythos_mud_mapbuilder.py** (22 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Coord** (14 connections)
- **RoomID** (12 connections)
- **Room** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **infer_coordinates()** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_process_exit()** (10 connections) — `data/local/mythos_mud_mapbuilder.py`
- **build_tile_grid()** (7 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_record_explicit_coords()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_select_start_room_if_needed()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_initialize_bfs_queue()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_unknown_direction()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_coordinate_conflict()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_spatial_collision()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_check_disconnected_rooms()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **load_rooms_from_dir()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **run_validator_on_rooms()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **example_validator()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- **MythosMUD Map Builder & Renderer --------------------------------  Single-fil** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Represents a room in the MUD world with its ID, exits, and metadata.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Load all .json files in a directory and return a map of RoomID -> Room** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Run user-provided validator function over rooms. It should return a list     of** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Record explicit coordinates from rooms.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Select start room if needed. Returns (start_room, should_early_return).** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Initialize BFS queue with start room.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Handle unknown direction by keeping same coordinates.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- *... and 7 more nodes in this community*

## Relationships

- [Chat Logger Service Tests](Chat_Logger_Service_Tests.md) (17 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (5 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`

## Audit Trail

- EXTRACTED: 157 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*