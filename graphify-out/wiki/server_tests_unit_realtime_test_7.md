# server tests unit realtime test

> 9 nodes

## Key Concepts

- **fixture** (4 connections)
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **remove_player_data_mock()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **remove_player_from_all_rooms_mock()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **remove_player_messages_mock()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Typed mock for RateLimiter.remove_player_data.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Typed mock for MessageQueue.remove_player_messages.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Typed mock for room_manager.remove_player_from_all_rooms.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`

## Relationships

- [server realtime connection disconnection](server_realtime_connection_disconnection.md) (4 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_disconnection.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*