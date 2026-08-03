# System Metrics

> 45 nodes

## Key Concepts

- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **Request** (5 connections)
- **.test_health_check_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_not_found()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_initialization_failure()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.mock_app()** (2 connections) — `server/tests/unit/test_main.py`
- **.mock_dashboard()** (2 connections) — `server/tests/unit/test_main.py`
- **Enhanced health check endpoint using monitoring dashboard.** (1 connections) — `server/api/system_monitoring.py`
- **Get comprehensive monitoring summary.** (1 connections) — `server/api/system_monitoring.py`
- *... and 20 more nodes in this community*

## Relationships

- [command combat models](command_combat_models.md) (14 shared connections)
- [Exception Containers](Exception_Containers.md) (13 shared connections)
- [time service rationale](time_service_rationale.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [health models rationale](health_models_rationale.md) (1 shared connections)
- [room cache services](room_cache_services.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 157 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*