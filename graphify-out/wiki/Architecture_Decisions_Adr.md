# Architecture Decisions Adr

> 50 nodes

## Key Concepts

- **deque** (24 connections)
- **mythos_mud_mapbuilder.py** (22 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Coord** (14 connections)
- **RoomID** (12 connections)
- **Room** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **infer_coordinates()** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_process_exit()** (10 connections) — `data/local/mythos_mud_mapbuilder.py`
- **main()** (10 connections) — `data/local/mythos_mud_mapbuilder.py`
- **render_with_tcod()** (8 connections) — `data/local/mythos_mud_mapbuilder.py`
- **build_tile_grid()** (7 connections) — `data/local/mythos_mud_mapbuilder.py`
- **compute_bounds()** (7 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_record_explicit_coords()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_select_start_room_if_needed()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_initialize_bfs_queue()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_unknown_direction()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_coordinate_conflict()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_spatial_collision()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_check_disconnected_rooms()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Any** (6 connections)
- **render_text()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **dump_ascii_to_file()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **load_rooms_from_dir()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **run_validator_on_rooms()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_load_tileset()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- **example_validator()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- *... and 25 more nodes in this community*

## Relationships

- [NATS Subject Patterns](NATS_Subject_Patterns.md) (8 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Mythos Map Builder](Mythos_Map_Builder.md) (1 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (1 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Archive Environment Contamination](Archive_Environment_Contamination.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Zone Coordinate Generator](Zone_Coordinate_Generator.md) (1 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (1 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`
- `server/realtime/message_queue.py`

## Audit Trail

- EXTRACTED: 221 (91%)
- INFERRED: 22 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*