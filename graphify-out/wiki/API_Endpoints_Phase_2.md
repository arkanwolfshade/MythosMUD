# API Endpoints (Phase 2)

> 10 nodes

## Key Concepts

- **_FakeMessageQueue** (4 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_FakeRateLimiter** (4 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_FakeRoomManager** (4 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **.__init__()** (4 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **.__init__()** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **.remove_player_messages()** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **.__init__()** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **.remove_player_data()** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **.__init__()** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **.remove_player_from_all_rooms()** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`

## Relationships

- [population_control.py](population_control.py.md) (4 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*