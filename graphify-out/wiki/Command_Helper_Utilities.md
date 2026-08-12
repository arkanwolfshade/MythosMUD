# Command Helper Utilities

> 64 nodes

## Key Concepts

- **connection_manager_health_cleanup.py** (30 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **Any** (15 connections)
- **Any** (13 connections)
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **check_connection_health_impl()** (8 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **UUID** (8 connections)
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **detect_and_handle_error_state_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_websocket_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_authentication_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_security_violation_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **recover_from_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_dead_connections_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **check_and_cleanup_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_orphaned_data_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **_periodic_health_check_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **start_health_checks_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **force_cleanup_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_ghost_players_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **prune_stale_players_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **stop_health_checks_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- *... and 39 more nodes in this community*

## Relationships

- [Container Exception Handlers](Container_Exception_Handlers.md) (28 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (17 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (15 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (3 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (2 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 276 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*