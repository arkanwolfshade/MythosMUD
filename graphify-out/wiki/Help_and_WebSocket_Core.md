# Help and WebSocket Core

> 102 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **MonitoringDashboard** (33 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceMonitor** (25 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_performance_stats()** (7 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **Any** (6 connections)
- *... and 77 more nodes in this community*

## Relationships

- [NATS Subject Metrics](NATS_Subject_Metrics.md) (13 shared connections)
- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (9 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (9 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (7 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (6 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (6 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (5 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (4 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (4 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (4 shared connections)
- [End-to-End Validation](End-to-End_Validation.md) (4 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (2 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 419 (89%)
- INFERRED: 54 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*