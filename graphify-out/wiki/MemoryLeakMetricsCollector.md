# MemoryLeakMetricsCollector

> 87 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (28 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_memory_leak_metrics.py** (26 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **.event_bus()** (14 connections) — `server/realtime/connection_manager.py`
- **memory_leak_metrics.py** (12 connections) — `server/monitoring/memory_leak_metrics.py`
- **.initialize()** (11 connections) — `server/container/bundles/monitoring.py`
- **Any** (11 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **.collect_event_metrics()** (6 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **collector()** (4 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_collect_event_metrics_uses_injected_event_bus()** (3 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_nats_metrics_uses_injected_nats_service()** (3 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- *... and 62 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (2 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)
- [NPCBase](NPCBase.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [QuestService](QuestService.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 146 (90%)
- INFERRED: 16 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*