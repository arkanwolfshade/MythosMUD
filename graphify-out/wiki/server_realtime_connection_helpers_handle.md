# server realtime connection helpers handle

> 6 nodes

## Key Concepts

- **handle_new_login_impl()** (8 connections) — `server/realtime/connection_helpers.py`
- **test_handle_new_login_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl_cancels_orphan_rest_countdown()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Handle a new login by terminating all existing connections. Args: player_id:…** (1 connections) — `server/realtime/connection_helpers.py`
- **Test handle_new_login_impl() handles new login.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **New login must cancel /rest countdown so it cannot kill the new session.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [server realtime connection helpers convert](server_realtime_connection_helpers_convert.md) (3 shared connections)
- [server realtime connection helpers](server_realtime_connection_helpers.md) (2 shared connections)
- [server realtime connection helpers rationale](server_realtime_connection_helpers_rationale.md) (2 shared connections)
- [server commands rest command](server_commands_rest_command.md) (1 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*