# Test Connection Disconnection

> 9 nodes

## Key Concepts

- **mock_manager()** (6 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **fixture** (4 connections)
- **remove_player_data_mock()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **remove_player_from_all_rooms_mock()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **remove_player_messages_mock()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Typed mock for RateLimiter.remove_player_data.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Typed mock for MessageQueue.remove_player_messages.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Typed mock for room_manager.remove_player_from_all_rooms.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`

## Relationships

- [Test Connection Disconnection](Test_Connection_Disconnection.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Test Connection Rate Limiter](Test_Connection_Rate_Limiter.md) (1 shared connections)
- [Test Message Queue](Test_Message_Queue.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_disconnection.py`

## Audit Trail

- EXTRACTED: 12 (80%)
- INFERRED: 3 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*