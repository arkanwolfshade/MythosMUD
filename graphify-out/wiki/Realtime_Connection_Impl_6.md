# Realtime Connection Impl

> 5 nodes · cohesion 0.50

## Key Concepts

- **handle_new_login_impl()** (8 connections) — `server/realtime/connection_helpers.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **test_handle_new_login_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Handle a new login by terminating all existing connections.      Args:         p** (2 connections) — `server/realtime/connection_helpers.py`
- **Test handle_new_login_impl() handles new login.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [[Realtime Connection Impl]] (4 shared connections)
- [[Room Occupant Events]] (3 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
