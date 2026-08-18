# ConnectionManager

> 96 nodes

## Key Concepts

- **ConnectionManager** (168 connections) — `server/realtime/connection_manager.py`
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **.canonical_room_id()** (4 connections) — `server/realtime/connection_manager.py`
- **manager()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_broadcast_and_health_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_disconnect_and_session_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_room_subscription_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_safe_close_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **asyncio** (4 connections)
- **._check_and_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **.disconnect_connection_by_id()** (3 connections) — `server/realtime/connection_manager.py`
- **._get_event_bus()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_presence_statistics()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_session_stats()** (3 connections) — `server/realtime/connection_manager.py`
- **._reconcile_room_presence()** (3 connections) — `server/realtime/connection_manager.py`
- **.set_event_bus()** (3 connections) — `server/realtime/connection_manager.py`
- **.set_player_combat_service()** (3 connections) — `server/realtime/connection_manager.py`
- **test_connection_manager_init_sets_components()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_player_connection_lookup_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_presence_and_online_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_set_async_persistence_and_services()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_stats_and_rate_limit_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_websocket_lifecycle_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **.broadcast_global()** (2 connections) — `server/realtime/connection_manager.py`
- *... and 71 more nodes in this community*

## Relationships

- [UUID](UUID.md) (33 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [build_event](build_event.md) (10 shared connections)
- [asyncio](asyncio.md) (6 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (5 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (5 shared connections)
- [.connect_websocket](connect_websocket.md) (4 shared connections)
- [delegate_error_handler](delegate_error_handler.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [test_container_events_loot.py](test_container_events_loot.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 204 (83%)
- INFERRED: 43 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*