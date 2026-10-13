# Community 366

> 47 nodes

## Key Concepts

- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **test_connection_cleanup_methods.py** (16 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_connections_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **check_and_cleanup_impl()** (7 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (7 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **force_cleanup_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (6 connections) — `server/realtime/connection_cleanup_methods.py`
- **Any** (6 connections)
- **asyncio** (5 connections)
- **test_delegate_connection_cleaner_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **_session_ids_past_age_off()** (3 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_check_and_cleanup_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_dead_connections_default_when_cleaner_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_dead_connections_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_cleanup_orphaned_data_impl_ages_sessions()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_force_cleanup_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_delegate_connection_cleaner_sync_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_sync_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_age_off_disconnected_sessions_keeps_recent()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_missing_attrs_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_removes_expired()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 22 more nodes in this community*

## Relationships

- [Community 90](Community_90.md) (12 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (9 shared connections)
- [Community 221](Community_221.md) (4 shared connections)
- [Community 591](Community_591.md) (2 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- `server/tests/unit/realtime/test_connection_delegates.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*