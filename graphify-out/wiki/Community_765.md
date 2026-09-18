# Community 765

> 22 nodes

## Key Concepts

- **test_websocket_room_updates_fanout.py** (12 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **test_broadcast_room_update_personalizes_for_hallucinating_viewer()** (9 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **test_broadcast_room_update_no_hallucinators_uses_broadcast()** (6 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **_make_mock_room()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **mock_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **_setup_hallucinating_room()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **_has_phantom_for()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **_phantom_data_for()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **_same_room_data()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **_sent_events()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **asyncio** (2 connections)
- **fixture** (1 connections)
- **Unit tests for the per-viewer room-payload fan-out (#714). Split out of…** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **The fast path: an empty phantom roster still broadcasts once, unchanged (#714).** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **Pass room_data through unchanged -- stands in for real UUID-to-name conversion.** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **Shared phantom data fixture for the hallucinating-viewer fan-out test.** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **Build a mock Room with its attributes set via constructor kwargs, not post-hoc…** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **side_effect for get_active_phantoms: only_player_id sees one phantom, nobody…** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **Read back (recipient_id, event) pairs from send_personal_message's call history.** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **Wire mock_connection_manager for a room where only `player_id` sees a phantom.** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **#714: a room with an active phantom fans out per-viewer instead of one…** (1 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`

## Relationships

- [Community 222](Community_222.md) (3 shared connections)
- [Community 38](Community_38.md) (2 shared connections)
- [Community 200](Community_200.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`

## Audit Trail

- EXTRACTED: 32 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*