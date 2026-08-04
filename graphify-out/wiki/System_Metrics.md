# System Metrics

> 49 nodes

## Key Concepts

- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **__init__.py** (10 connections) — `server/api/__init__.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
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
- **.mock_dashboard()** (2 connections) — `server/tests/unit/test_main.py`
- *... and 24 more nodes in this community*

## Relationships

- [health models rationale](health_models_rationale.md) (13 shared connections)
- [Exception Containers](Exception_Containers.md) (12 shared connections)
- [room cache services](room_cache_services.md) (6 shared connections)
- [command combat models](command_combat_models.md) (5 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [player preferences services](player_preferences_services.md) (1 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (1 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)
- [combat commands handler](combat_commands_handler.md) (1 shared connections)
- [room game service](room_game_service.md) (1 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (1 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 172 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*