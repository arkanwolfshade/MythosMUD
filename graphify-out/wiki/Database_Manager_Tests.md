# Database Manager Tests

> 26 nodes

## Key Concepts

- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
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
- **mock_connection_manager()** (2 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Unit tests for container WebSocket events.  Tests the container WebSocket event** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Create mock connection manager.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_opened handles container with owner.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_opened_to_room broadcasts to room.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_closed emits close event.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_opened handles container with owner_id.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_opened_to_room handles container with owner.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_updated broadcasts update event.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_updated handles empty diff.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_decayed broadcasts decay event.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_opened returns delivery status.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test emit_container_opened_to_room returns broadcast stats.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- *... and 1 more nodes in this community*

## Relationships

- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (17 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (1 shared connections)
- [test_emit_container_opened](test_emit_container_opened.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*