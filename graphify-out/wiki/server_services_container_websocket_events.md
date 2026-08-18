# server services container websocket events

> 44 nodes

## Key Concepts

- **test_container_websocket_events.py** (24 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **container_websocket_events.py** (16 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **asyncio** (12 connections)
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **UUID** (6 connections)
- **Any** (5 connections)
- **test_emit_container_closed()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed_returns_stats()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_decayed()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_returns_delivery_status()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room_returns_stats()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room_with_owner()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_with_owner()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_with_owner_id()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated_empty_diff()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **datetime** (3 connections)
- **Test emit_container_opened handles container with owner.** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- *... and 19 more nodes in this community*

## Relationships

- [server api container events](server_api_container_events.md) (12 shared connections)
- [server container main get container](server_container_main_get_container.md) (3 shared connections)
- [server app game tick corpses](server_app_game_tick_corpses.md) (2 shared connections)
- [server models container containercomponent](server_models_container_containercomponent.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/services/container_websocket_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 109 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*