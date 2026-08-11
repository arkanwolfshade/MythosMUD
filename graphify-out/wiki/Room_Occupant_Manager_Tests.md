# Room Occupant Manager Tests

> 49 nodes

## Key Concepts

- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **Request** (5 connections)
- **.test_health_check_failure()** (4 connections) — `server/tests/unit/test_main.py`
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
- **.mock_dashboard()** (2 connections) — `server/tests/unit/test_main.py`
- *... and 24 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (26 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (9 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (7 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (4 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (2 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (2 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (1 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 172 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*