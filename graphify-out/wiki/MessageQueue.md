# MessageQueue

> 131 nodes

## Key Concepts

- **MessageQueue** (58 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (26 connections)
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
- *... and 106 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (8 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (5 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (2 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [mock_manager](mock_manager.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [ErrorMonitor](ErrorMonitor.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`
- `server/realtime/message_queue.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 208 (78%)
- INFERRED: 57 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*