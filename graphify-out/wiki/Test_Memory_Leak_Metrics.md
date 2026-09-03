# Test Memory Leak Metrics

> 78 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (28 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_memory_leak_metrics.py** (26 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Any** (11 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (6 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
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
- **test_calculate_growth_rates()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates_insufficient_history()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_cache_capacity()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_closed_websockets_threshold()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_no_alerts()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- *... and 53 more nodes in this community*

## Relationships

- [Application Container Bundles](Application_Container_Bundles.md) (5 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (2 shared connections)
- [Exception Tracker](Exception_Tracker.md) (1 shared connections)
- [Performance Monitor](Performance_Monitor.md) (1 shared connections)
- [Monitoring Dashboard](Monitoring_Dashboard.md) (1 shared connections)
- [Cache Service](Cache_Service.md) (1 shared connections)
- [Test Lifespan Event Subscriptions](Test_Lifespan_Event_Subscriptions.md) (1 shared connections)
- [Task Registry](Task_Registry.md) (1 shared connections)
- [Mythos Mud Mapbuilder](Mythos_Mud_Mapbuilder.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 115 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*