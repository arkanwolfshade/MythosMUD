# server realtime connection delegates delegate

> 45 nodes

## Key Concepts

- **connection_manager_health_cleanup.py** (29 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **delegate_connection_cleaner()** (16 connections) — `server/realtime/connection_delegates.py`
- **Any** (15 connections)
- **age_off_disconnected_sessions()** (13 connections) — `server/realtime/player_disconnect_handlers.py`
- **delegate_connection_cleaner_sync()** (12 connections) — `server/realtime/connection_delegates.py`
- **UUID** (8 connections)
- **check_connection_health_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **check_and_cleanup_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_dead_connections_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_orphaned_data_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **detect_and_handle_error_state_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_authentication_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_security_violation_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_websocket_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **recover_from_error_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_ghost_players_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **force_cleanup_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **_periodic_health_check_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **prune_stale_players_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **start_health_checks_impl()** (4 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **stop_health_checks_impl()** (3 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **_session_ids_past_age_off()** (3 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_delegate_connection_cleaner_sync_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Generic delegate for connection cleaner methods. Args: connection_cleaner:…** (1 connections) — `server/realtime/connection_delegates.py`
- **Generic delegate for synchronous connection cleaner methods. Args:…** (1 connections) — `server/realtime/connection_delegates.py`
- *... and 20 more nodes in this community*

## Relationships

- [server realtime connection cleanup methods](server_realtime_connection_cleanup_methods.md) (10 shared connections)
- [server realtime connection delegates](server_realtime_connection_delegates.md) (10 shared connections)
- [server realtime connection delegates cleanup](server_realtime_connection_delegates_cleanup.md) (6 shared connections)
- [server realtime connection delegates delegate](server_realtime_connection_delegates_delegate.md) (6 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server realtime maintenance connection cleaner](server_realtime_maintenance_connection_cleaner.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 118 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*