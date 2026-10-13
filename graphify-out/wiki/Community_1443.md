# Community 1443

> 6 nodes

## Key Concepts

- **handle_new_login_impl()** (9 connections) — `server/realtime/connection_helpers.py`
- **test_handle_new_login_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl_cancels_orphan_rest_countdown()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Handle a new login by terminating all existing connections. Args: player_id:…** (1 connections) — `server/realtime/connection_helpers.py`
- **Test handle_new_login_impl() handles new login.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **New login must cancel /rest countdown so it cannot kill the new session.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [Community 472](Community_472.md) (3 shared connections)
- [Community 634](Community_634.md) (2 shared connections)
- [Community 787](Community_787.md) (2 shared connections)
- [Community 76](Community_76.md) (1 shared connections)
- [Community 188](Community_188.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*