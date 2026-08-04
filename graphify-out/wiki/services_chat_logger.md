# services chat logger

> 42 nodes

## Key Concepts

- **PerformanceTracker** (25 connections) — `server/realtime/monitoring/performance_tracker.py`
- **health_monitor.py** (14 connections) — `server/realtime/monitoring/health_monitor.py`
- **performance_tracker.py** (11 connections) — `server/realtime/monitoring/performance_tracker.py`
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **PerformanceStats** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_connection_establishment()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_message_delivery()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_disconnection()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_session_switch()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_health_check()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.get_stats()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **test_record_events_increase_counters()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_trim_samples_keeps_max_samples()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_empty_returns_zeros()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_calculates_averages()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_non_websocket_connections_excluded_from_websocket_stats()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_error_path_returns_error_dict()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Monitoring components for connection management.  This package provides modular** (1 connections) — `server/realtime/monitoring/__init__.py`
- **Health monitoring for connection management.  This module provides comprehensive** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **TypedDict** (1 connections)
- **Any** (1 connections)
- **Performance tracking for connection management.  This module provides comprehens** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- *... and 17 more nodes in this community*

## Relationships

- [health monitor realtime](health_monitor_realtime.md) (5 shared connections)
- [services npc startup](services_npc_startup.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (3 shared connections)
- [event realtime publisher](event_realtime_publisher.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [persistence rationale room](persistence_rationale_room.md) (2 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`

## Audit Trail

- EXTRACTED: 133 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*