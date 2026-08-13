# lifespan.py

> 96 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (32 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_memory_leak_metrics.py** (23 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **memory_leak_metrics.py** (12 connections) — `server/monitoring/memory_leak_metrics.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **Any** (10 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **_cleanup_container_on_error()** (5 connections) — `server/app/lifespan.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **_calculate_metrics_delta()** (4 connections) — `server/app/lifespan.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (4 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (4 connections) — `server/app/lifespan.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 71 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (18 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (14 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (6 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (5 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [MythosChronicle](MythosChronicle.md) (3 shared connections)
- [lifespan_shutdown.py](lifespan_shutdown.py.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (2 shared connections)
- [deque](deque.md) (1 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 211 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*