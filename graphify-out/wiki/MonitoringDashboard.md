# MonitoringDashboard

> 91 nodes

## Key Concepts

- **MonitoringDashboard** (32 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **exception_tracker.py** (20 connections) — `server/monitoring/exception_tracker.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **PerformanceStats** (10 connections) — `server/monitoring/performance_monitor.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **track_exception_with_context()** (6 connections) — `server/monitoring/exception_tracker.py`
- **__getattr__()** (6 connections) — `server/monitoring/__init__.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- *... and 66 more nodes in this community*

## Relationships

- [lifespan.py](lifespan.py.md) (18 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (13 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (9 shared connections)
- [LogAggregator](LogAggregator.md) (7 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (6 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (5 shared connections)
- [testing_examples.py](testing_examples.py.md) (4 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (3 shared connections)
- [prototype_registry.py](prototype_registry.py.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 233 (91%)
- INFERRED: 24 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*