# playercombatservice

> 100 nodes

## Key Concepts

- **ConnectionManager** (161 connections) — `server/realtime/connection_manager.py`
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **manager()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_broadcast_and_health_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_disconnect_and_session_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_room_subscription_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_safe_close_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **asyncio** (4 connections)
- **.canonical_room_id()** (3 connections) — `server/realtime/connection_manager.py`
- **.disconnect_connection_by_id()** (3 connections) — `server/realtime/connection_manager.py`
- **.set_player_combat_service()** (3 connections) — `server/realtime/connection_manager.py`
- **test_connection_manager_init_sets_components()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_player_connection_lookup_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_presence_and_online_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_set_async_persistence_and_services()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_stats_and_rate_limit_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_websocket_lifecycle_helpers()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **.broadcast_global()** (2 connections) — `server/realtime/connection_manager.py`
- **.broadcast_global_event()** (2 connections) — `server/realtime/connection_manager.py`
- **.broadcast_room_event()** (2 connections) — `server/realtime/connection_manager.py`
- **._check_and_cleanup()** (2 connections) — `server/realtime/connection_manager.py`
- **._cleanup_ghost_players()** (2 connections) — `server/realtime/connection_manager.py`
- **.cleanup_orphaned_data()** (2 connections) — `server/realtime/connection_manager.py`
- **.convert_room_players_uuids_to_names()** (2 connections) — `server/realtime/connection_manager.py`
- *... and 75 more nodes in this community*

## Relationships

- [newgamesessionresult](newgamesessionresult.md) (39 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (7 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (6 shared connections)
- [server realtime connection manager connectionmanager](server_realtime_connection_manager_connectionmanager.md) (6 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (4 shared connections)
- [server api container events emit](server_api_container_events_emit.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (3 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (3 shared connections)
- [room](room.md) (3 shared connections)
- [eventbus](eventbus.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 198 (84%)
- INFERRED: 37 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*