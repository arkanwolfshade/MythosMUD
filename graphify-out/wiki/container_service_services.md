# container service services

> 54 nodes

## Key Concepts

- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **test_connection_cleanup_methods.py** (16 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_connections_impl()** (10 connections) — `server/realtime/connection_cleanup_methods.py`
- **check_and_cleanup_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **CleanupContext** (9 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **force_cleanup_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_ghost_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **Any** (6 connections)
- **.prune_stale_players()** (3 connections) — `server/realtime/connection_manager.py`
- **.cleanup_orphaned_data()** (3 connections) — `server/realtime/connection_manager.py`
- **._cleanup_ghost_players()** (3 connections) — `server/realtime/connection_manager.py`
- **._check_and_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **.force_cleanup()** (3 connections) — `server/realtime/connection_manager.py`
- **test_check_and_cleanup_skips_when_not_due()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_delegate_connection_cleaner_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_sync_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_sync_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **UUID** (2 connections)
- **test_cleanup_dead_connections_impl_delegates()** (2 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- *... and 29 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (13 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (11 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (4 shared connections)
- [emote game service](emote_game_service.md) (3 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 193 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*