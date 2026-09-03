# Test Container Websocket Events

> 45 nodes

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
- **mock_container()** (4 connections) — `server/tests/unit/services/test_container_websocket_events.py`
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
- *... and 20 more nodes in this community*

## Relationships

- [Test Container Events](Test_Container_Events.md) (9 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (8 shared connections)
- [Test Envelope](Test_Envelope.md) (3 shared connections)
- [Test Game Tick Death](Test_Game_Tick_Death.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/services/container_websocket_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 110 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*