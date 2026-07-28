# Mythos Map Builder

> 53 nodes · cohesion 0.08

## Key Concepts

- **deque** (24 connections)
- **mythos_mud_mapbuilder.py** (22 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Coord** (14 connections)
- **RoomID** (12 connections)
- **infer_coordinates()** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Room** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **main()** (10 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_process_exit()** (10 connections) — `data/local/mythos_mud_mapbuilder.py`
- **render_with_tcod()** (8 connections) — `data/local/mythos_mud_mapbuilder.py`
- **build_tile_grid()** (7 connections) — `data/local/mythos_mud_mapbuilder.py`
- **compute_bounds()** (7 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_check_disconnected_rooms()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **dump_ascii_to_file()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_coordinate_conflict()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_spatial_collision()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_unknown_direction()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_initialize_bfs_queue()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Any** (6 connections)
- **_record_explicit_coords()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **render_text()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_select_start_room_if_needed()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **load_rooms_from_dir()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **run_validator_on_rooms()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **example_validator()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_load_tileset()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- *... and 28 more nodes in this community*

## Relationships

- [Message Queue Cleanup](Message_Queue_Cleanup.md) (10 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (2 shared connections)
- [Error Monitor Service](Error_Monitor_Service.md) (1 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (1 shared connections)
- [Whisper Work Remaining](Whisper_Work_Remaining.md) (1 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (1 shared connections)
- [Zone Coordinate Generator](Zone_Coordinate_Generator.md) (1 shared connections)
- [Community 2205](Community_2205.md) (1 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`

## Audit Trail

- EXTRACTED: 225 (90%)
- INFERRED: 24 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*