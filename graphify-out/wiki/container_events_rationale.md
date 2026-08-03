# container events rationale

> 44 nodes

## Key Concepts

- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **UUID** (6 connections)
- **Any** (5 connections)
- **datetime** (3 connections)
- **test_emit_container_opened()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_with_owner()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_with_owner_id()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room_with_owner()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated_empty_diff()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_decayed()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_returns_delivery_status()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room_returns_stats()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed_returns_stats()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **ContainerComponent** (2 connections)
- **mock_connection_manager()** (2 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Container WebSocket event emission for unified container system.  As documented** (1 connections) — `server/services/container_websocket_events.py`
- *... and 19 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (13 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [invite models rationale](invite_models_rationale.md) (1 shared connections)
- [services npc startup](services_npc_startup.md) (1 shared connections)

## Source Files

- `server/services/container_websocket_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 167 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*