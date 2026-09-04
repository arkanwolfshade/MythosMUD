# Mythos Mud Mapbuilder

> 53 nodes

## Key Concepts

- **deque** (25 connections)
- **mythos_mud_mapbuilder.py** (22 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Coord** (14 connections)
- **RoomID** (12 connections)
- **Room** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
- **infer_coordinates()** (11 connections) — `data/local/mythos_mud_mapbuilder.py`
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
- **_record_explicit_coords()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **render_text()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_select_start_room_if_needed()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Any** (6 connections)
- **load_rooms_from_dir()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **run_validator_on_rooms()** (5 connections) — `data/local/mythos_mud_mapbuilder.py`
- **example_validator()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_load_tileset()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- *... and 28 more nodes in this community*

## Relationships

- [Test Message Queue](Test_Message_Queue.md) (10 shared connections)
- [Personal Message Sender](Personal_Message_Sender.md) (2 shared connections)
- [Performance Monitor](Performance_Monitor.md) (1 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (1 shared connections)
- [Test Metrics](Test_Metrics.md) (1 shared connections)
- [Error Monitoring](Error_Monitoring.md) (1 shared connections)
- [Test Memory Leak Metrics](Test_Memory_Leak_Metrics.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Test Combat Monitoring Service](Test_Combat_Monitoring_Service.md) (1 shared connections)
- [Coordinate Generator](Coordinate_Generator.md) (1 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`
- `server/monitoring/performance_monitor.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`

## Audit Trail

- EXTRACTED: 114 (84%)
- INFERRED: 21 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*