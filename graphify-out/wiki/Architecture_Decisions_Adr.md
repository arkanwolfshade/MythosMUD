# Architecture Decisions Adr

> 32 nodes

## Key Concepts

- **deque** (24 connections)
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
- **.__init__()** (2 connections) — `server/services/nats_metrics.py`
- **MythosMUD Map Builder & Renderer --------------------------------  Single-fil** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Represents a room in the MUD world with its ID, exits, and metadata.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Load all .json files in a directory and return a map of RoomID -> Room** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Run user-provided validator function over rooms. It should return a list     of** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Record explicit coordinates from rooms.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Select start room if needed. Returns (start_room, should_early_return).** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Initialize BFS queue with start room.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- *... and 7 more nodes in this community*

## Relationships

- [E 2 E Di Migration](E_2_E_Di_Migration.md) (18 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (9 shared connections)
- [Mythos Map Builder](Mythos_Map_Builder.md) (1 shared connections)
- [Enhanced Logging Guide](Enhanced_Logging_Guide.md) (1 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (1 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (1 shared connections)
- [Migration Testing Guide](Migration_Testing_Guide.md) (1 shared connections)
- [Archive Environment Contamination](Archive_Environment_Contamination.md) (1 shared connections)
- [UI Animation Testing Standards](UI_Animation_Testing_Standards.md) (1 shared connections)
- [Zone Coordinate Generator](Zone_Coordinate_Generator.md) (1 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (1 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (1 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`
- `server/services/nats_metrics.py`

## Audit Trail

- EXTRACTED: 159 (89%)
- INFERRED: 20 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*