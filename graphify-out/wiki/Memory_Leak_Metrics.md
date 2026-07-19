# Memory Leak Metrics

> 86 nodes · cohesion 0.04

## Key Concepts

- **MemoryLeakMetricsCollector** (35 connections) — `server/monitoring/memory_leak_metrics.py`
- **MonitoringDashboard** (32 connections) — `server/monitoring/monitoring_dashboard.py`
- **ExceptionStats** (16 connections) — `server/monitoring/exception_tracker.py`
- **PerformanceStats** (15 connections) — `server/monitoring/performance_monitor.py`
- **LogAggregationStats** (13 connections) — `server/structured_logging/log_aggregator.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (10 connections) — `server/monitoring/memory_leak_metrics.py`
- **Any** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **ExceptionStats** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **LogAggregationStats** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 61 more nodes in this community*

## Relationships

- [[App Lifespan Management]] (21 shared connections)
- [[Monitoring Bundle Services]] (7 shared connections)
- [[Monitoring API Endpoints]] (4 shared connections)
- [[System Monitoring API]] (3 shared connections)
- [[Logging Correct Patterns]] (3 shared connections)
- [[Memory Leak Metrics Tests]] (2 shared connections)
- [[Inventory Service Helpers]] (2 shared connections)
- [[Performance Monitor Metrics]] (2 shared connections)
- [[Services Service Room]] (1 shared connections)
- [[Lifespan Startup Hooks]] (1 shared connections)
- [[Message Queue Cleanup]] (1 shared connections)
- [[Cache and NPC Cache]] (1 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 297 (79%)
- INFERRED: 78 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
