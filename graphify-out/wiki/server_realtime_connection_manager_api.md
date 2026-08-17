# server realtime connection manager api

> 43 nodes

## Key Concepts

- **connection_manager_api.py** (21 connections) — `server/realtime/connection_manager_api.py`
- **test_connection_manager_api.py** (11 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (8 connections) — `server/realtime/connection_manager_utils.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_game_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (7 connections) — `server/realtime/connection_manager_utils.py`
- **asyncio** (7 connections)
- **UUID** (6 connections)
- **send_player_status_update()** (5 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (5 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (5 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (5 connections) — `server/realtime/connection_manager_api.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **test_broadcast_game_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_require_manager_raises_when_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_game_event_with_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_player_status_update()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_room_description()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_room_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_system_notification()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **.send_personal_message()** (2 connections) — `server/realtime/connection_manager_api.py`
- **mock_manager()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- *... and 18 more nodes in this community*

## Relationships

- [followtargetvalue](followtargetvalue.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (3 shared connections)
- [server events event types mythoshourtickevent](server_events_event_types_mythoshourtickevent.md) (1 shared connections)
- [server api monitoring](server_api_monitoring.md) (1 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (1 shared connections)
- [server app game tick processing](server_app_game_tick_processing.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`

## Audit Trail

- EXTRACTED: 89 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*