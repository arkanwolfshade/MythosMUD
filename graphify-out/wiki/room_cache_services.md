# room cache services

> 62 nodes

## Key Concepts

- **MonitoringDashboard** (33 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **LogAggregationStats** (12 connections) — `server/structured_logging/log_aggregator.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **SystemHealth** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
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
- **.get_alert_history()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._determine_health_status()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_active_users()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_system_load()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 37 more nodes in this community*

## Relationships

- [models lucidity rationale](models_lucidity_rationale.md) (11 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (7 shared connections)
- [command combat models](command_combat_models.md) (7 shared connections)
- [log structured logging](log_structured_logging.md) (6 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [world loader room](world_loader_room.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [commands inventory put](commands_inventory_put.md) (1 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 251 (89%)
- INFERRED: 32 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*