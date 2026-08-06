# room cache services

> 99 nodes

## Key Concepts

- **MonitoringDashboard** (33 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **LogAggregationStats** (12 connections) — `server/structured_logging/log_aggregator.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **SystemHealth** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 74 more nodes in this community*

## Relationships

- [task registry app](task_registry_app.md) (13 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (8 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (8 shared connections)
- [services chat logger](services_chat_logger.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (7 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (6 shared connections)
- [log structured logging](log_structured_logging.md) (6 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (3 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [app factory rationale](app_factory_rationale.md) (3 shared connections)
- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (2 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/services/inventory_mutation_guard.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 382 (89%)
- INFERRED: 45 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*