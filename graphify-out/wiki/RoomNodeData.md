# RoomNodeData

> 63 nodes · cohesion 0.07

## Key Concepts

- **test_container_websocket_events.py** (32 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **container_websocket_events.py** (19 connections) — `server/services/container_websocket_events.py`
- **asyncio** (16 connections)
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **_async_attr()** (14 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **emit_container_updated()** (13 connections) — `server/services/container_websocket_events.py`
- **ContainerConnectionManagerLike** (12 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (11 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_to_room()** (11 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **emit_container_created()** (7 connections) — `server/services/container_websocket_events.py`
- **UUID** (7 connections)
- **test_emit_container_created()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_created_payload_is_json_serializable()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room_with_owner()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated_no_room_id()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated_payload_is_json_serializable()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed()** (5 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed_no_room_id()** (5 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed_returns_stats()** (5 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_decayed()** (5 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_returns_delivery_status()** (5 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- *... and 38 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (24 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (10 shared connections)
- [.publish_with_pool](publish_with_pool.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [Room](Room.md) (2 shared connections)

## Source Files

- `server/services/container_websocket_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 161 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*