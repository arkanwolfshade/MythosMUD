# mythos mud mapbuilder

> 55 nodes

## Key Concepts

- **deque** (26 connections)
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
- *... and 30 more nodes in this community*

## Relationships

- [spell models rationale](spell_models_rationale.md) (14 shared connections)
- [error monitoring scripts](error_monitoring_scripts.md) (1 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (1 shared connections)
- [combat monitoring service](combat_monitoring_service.md) (1 shared connections)
- [coordinate services generator](coordinate_services_generator.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [combat commands handler](combat_commands_handler.md) (1 shared connections)
- [subject validation services](subject_validation_services.md) (1 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`

## Audit Trail

- EXTRACTED: 228 (89%)
- INFERRED: 27 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*