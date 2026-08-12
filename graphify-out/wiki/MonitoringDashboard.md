# MonitoringDashboard

> 70 nodes

## Key Concepts

- **MonitoringDashboard** (32 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **log_aggregator.py** (14 connections) — `server/structured_logging/log_aggregator.py`
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
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **aggregate_log_entry()** (5 connections) — `server/structured_logging/log_aggregator.py`
- *... and 45 more nodes in this community*

## Relationships

- [fastapi_integration.py](fastapi_integration.py.md) (16 shared connections)
- [lifespan.py](lifespan.py.md) (12 shared connections)
- [LogAggregator](LogAggregator.md) (8 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (1 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (1 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 283 (90%)
- INFERRED: 33 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*