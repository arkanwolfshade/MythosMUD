# handle_new_login_impl

> 8 nodes

## Key Concepts

- **handle_new_login_impl()** (10 connections) — `server/realtime/connection_helpers.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **test_handle_new_login_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl_cancels_orphan_rest_countdown()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Handle a new login by terminating all existing connections. Args: player_id:…** (1 connections) — `server/realtime/connection_helpers.py`
- **Handle a new login by terminating all existing connections for the player.** (1 connections) — `server/realtime/connection_manager.py`
- **Test handle_new_login_impl() handles new login.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **New login must cancel /rest countdown so it cannot kill the new session.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*