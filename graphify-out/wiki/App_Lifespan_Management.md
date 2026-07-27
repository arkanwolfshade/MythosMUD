# App Lifespan Management

> 92 nodes · cohesion 0.04

## Key Concepts

- **lifespan.py** (39 connections) — `server/app/lifespan.py`
- **ExceptionTracker** (24 connections) — `server/monitoring/exception_tracker.py`
- **monitoring_dashboard.py** (21 connections) — `server/monitoring/monitoring_dashboard.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **lifespan()** (13 connections) — `server/app/lifespan.py`
- **performance_monitor.py** (13 connections) — `server/monitoring/performance_monitor.py`
- **exception_tracker.py** (12 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_performance_monitor()** (12 connections) — `server/monitoring/performance_monitor.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **memory_leak_metrics.py** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **track_exception_with_context()** (8 connections) — `server/monitoring/exception_tracker.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **get_performance_stats()** (7 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **record_performance_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **Any** (6 connections) — `server/monitoring/performance_monitor.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **_cleanup_container_on_error()** (5 connections) — `server/app/lifespan.py`
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **reset_performance_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- *... and 67 more nodes in this community*

## Relationships

- [[Memory Leak Metrics]] (21 shared connections)
- [[Performance Monitor Metrics]] (13 shared connections)
- [[Lifespan Startup Hooks]] (9 shared connections)
- [[NPC Admin API]] (9 shared connections)
- [[Monitoring Bundle Services]] (8 shared connections)
- [[System Monitoring API]] (7 shared connections)
- [[FastAPI Auth Integration]] (5 shared connections)
- [[Game Tick Processing]] (4 shared connections)
- [[App Lifespan Shutdown]] (3 shared connections)
- [[Logging Correct Patterns]] (3 shared connections)
- [[FastAPI App Factory]] (2 shared connections)
- [[Application DI Bundles]] (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 400 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
