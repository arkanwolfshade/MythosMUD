# connection_manager.py

> 204 nodes

## Key Concepts

- **connection_manager.py** (130 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (95 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (38 connections) — `server/realtime/connection_delegates.py`
- **asyncio** (27 connections)
- **statistics_aggregator.py** (25 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
- **canonical_room_id_impl()** (16 connections) — `server/realtime/connection_room_utils.py`
- **health_monitor.py** (16 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **performance_tracker.py** (14 connections) — `server/realtime/monitoring/performance_tracker.py`
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **connection_models.py** (13 connections) — `server/realtime/connection_models.py`
- **test_connection_event_helpers.py** (13 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **connection_statistics.py** (11 connections) — `server/realtime/connection_statistics.py`
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **subscribe_to_room_events_impl()** (10 connections) — `server/realtime/connection_event_helpers.py`
- **unsubscribe_from_room_events_impl()** (10 connections) — `server/realtime/connection_event_helpers.py`
- *... and 179 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (52 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (20 shared connections)
- [ConnectionManager](ConnectionManager.md) (20 shared connections)
- [asyncio](asyncio.md) (16 shared connections)
- [test_connection_manager_methods.py](test_connection_manager_methods.py.md) (13 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (13 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (12 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (12 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (11 shared connections)
- [RateLimiter](RateLimiter.md) (7 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (7 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (7 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_models.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/connection_statistics.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_delegates.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 691 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*