# Player

> 473 nodes

## Key Concepts

- **ConnectionManager** (221 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (160 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (79 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **UUID** (41 connections)
- **connection_delegates.py** (38 connections) — `server/realtime/connection_delegates.py`
- **UUID** (21 connections)
- **ConnectionMetadata** (21 connections) — `server/realtime/connection_models.py`
- **connection_cleanup_methods.py** (18 connections) — `server/realtime/connection_cleanup_methods.py`
- **canonical_room_id_impl()** (17 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **validate_token_impl()** (15 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **UUID** (10 connections)
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **connection_error_methods.py** (10 connections) — `server/realtime/connection_error_methods.py`
- **safe_close_websocket_impl()** (10 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_connection_message_impl()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- *... and 448 more nodes in this community*

## Relationships

- [connection disconnection](connection_disconnection.md) (21 shared connections)
- [Any](Any.md) (20 shared connections)
- [circuit breaker](circuit_breaker.md) (19 shared connections)
- [world](world.md) (17 shared connections)
- [real time](real_time.md) (15 shared connections)
- [UUID](UUID.md) (13 shared connections)
- [test nats message handler](test_nats_message_handler.md) (12 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (9 shared connections)
- [test command factories exploration](test_command_factories_exploration.md) (9 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (9 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (8 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_error_methods.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_models.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_connection_delegates.py`
- `server/tests/unit/realtime/test_connection_models.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 2001 (97%)
- INFERRED: 53 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*