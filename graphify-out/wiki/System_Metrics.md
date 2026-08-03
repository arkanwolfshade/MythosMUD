# System Metrics

> 51 nodes

## Key Concepts

- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **Request** (5 connections)
- **.test_health_check_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_not_found()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.mock_app()** (2 connections) — `server/tests/unit/test_main.py`
- *... and 26 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (15 shared connections)
- [command combat models](command_combat_models.md) (11 shared connections)
- [room cache services](room_cache_services.md) (5 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [message nats handler](message_nats_handler.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [commands inventory put](commands_inventory_put.md) (2 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 201 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*