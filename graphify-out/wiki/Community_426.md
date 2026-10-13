# Community 426

> 41 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (26 connections) — `server/monitoring/memory_leak_metrics.py`
- **bundles/monitoring.py** (14 connections) — `server/container/bundles/monitoring.py`
- **MonitoringBundle** (12 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (11 connections) — `server/container/bundles/monitoring.py`
- **Any** (11 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (6 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.shutdown()** (3 connections) — `server/container/bundles/monitoring.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **Monitoring bundle: performance monitor, exception tracker, dashboard, log…** (1 connections) — `server/container/bundles/monitoring.py`
- **Monitoring and observability services.** (1 connections) — `server/container/bundles/monitoring.py`
- **Initialize monitoring services. Depends on Core/Realtime/Game for injected deps.** (1 connections) — `server/container/bundles/monitoring.py`
- **Shutdown log aggregator.** (1 connections) — `server/container/bundles/monitoring.py`
- *... and 16 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Community 201](Community_201.md) (6 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (4 shared connections)
- [Community 285](Community_285.md) (4 shared connections)
- [Community 95](Community_95.md) (4 shared connections)
- [Community 211](Community_211.md) (4 shared connections)
- [Community 400](Community_400.md) (4 shared connections)
- [Community 371](Community_371.md) (4 shared connections)
- [Community 1444](Community_1444.md) (2 shared connections)
- [Community 118](Community_118.md) (2 shared connections)
- [Community 1177](Community_1177.md) (1 shared connections)
- [Community 695](Community_695.md) (1 shared connections)

## Source Files

- `server/container/bundles/monitoring.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 96 (88%)
- INFERRED: 13 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*