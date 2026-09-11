# ConnectionManager

> 95 nodes

## Key Concepts

- **ConnectionManager** (180 connections) — `server/realtime/connection_manager.py`
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.canonical_room_id()** (4 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **manager()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_broadcast_and_health_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_disconnect_and_session_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_room_subscription_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_safe_close_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **WebSocket** (4 connections)
- **asyncio** (4 connections)
- **.get_connection_id_from_websocket()** (3 connections) — `server/realtime/connection_manager.py`
- **._get_event_bus()** (3 connections) — `server/realtime/connection_manager.py`
- **._reconcile_room_presence()** (3 connections) — `server/realtime/connection_manager.py`
- **.set_event_bus()** (3 connections) — `server/realtime/connection_manager.py`
- **test_connection_manager_init_sets_components()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_player_connection_lookup_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_presence_and_online_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_set_async_persistence_and_services()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_stats_and_rate_limit_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_websocket_lifecycle_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **.broadcast_global()** (2 connections) — `server/realtime/connection_manager.py`
- *... and 70 more nodes in this community*

## Relationships

- [UUID](UUID.md) (30 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (12 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (7 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (7 shared connections)
- [build_event](build_event.md) (7 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (6 shared connections)
- [.broadcast_connection_message](broadcast_connection_message.md) (5 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [follow_movement.py](follow_movement.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 209 (80%)
- INFERRED: 51 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*