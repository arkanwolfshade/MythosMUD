# Room Occupant Manager Tests

> 51 nodes

## Key Concepts

- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **SystemMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
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

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (14 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (13 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (7 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (2 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (2 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (2 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 200 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*