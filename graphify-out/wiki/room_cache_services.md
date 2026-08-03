# room cache services

> 73 nodes

## Key Concepts

- **MonitoringDashboard** (33 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **LogAggregationStats** (12 connections) — `server/structured_logging/log_aggregator.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **SystemHealth** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **.reset_records()** (3 connections) — `server/monitoring/exception_tracker.py`
- *... and 48 more nodes in this community*

## Relationships

- [websocket examples logging](websocket_examples_logging.md) (8 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (8 shared connections)
- [message nats handler](message_nats_handler.md) (6 shared connections)
- [log structured logging](log_structured_logging.md) (6 shared connections)
- [System Metrics](System_Metrics.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [commands inventory put](commands_inventory_put.md) (1 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 282 (87%)
- INFERRED: 43 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*