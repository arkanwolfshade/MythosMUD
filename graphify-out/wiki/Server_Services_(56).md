# Server Services (56)

> 28 nodes

## Key Concepts

- **CombatMonitoringService** (32 connections) — `server/services/combat_monitoring_service.py`
- **.end_combat_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_turn_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_turn_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._save_metrics_snapshot()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_monitoring_service.py`
- **monitoring_service()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_start_combat_monitoring_disabled()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_record_combat_error_disabled()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **.start_combat_monitoring()** (2 connections) — `server/services/combat_monitoring_service.py`
- **.start_turn_monitoring()** (2 connections) — `server/services/combat_monitoring_service.py`
- **.resolve_alert()** (2 connections) — `server/services/combat_monitoring_service.py`
- **.clear_resolved_alerts()** (2 connections) — `server/services/combat_monitoring_service.py`
- **Comprehensive combat monitoring and alerting service.      Tracks combat system** (1 connections) — `server/services/combat_monitoring_service.py`
- **Start monitoring a combat instance.          Args:             combat_id: Unique** (1 connections) — `server/services/combat_monitoring_service.py`
- **End monitoring a combat instance.          Args:             combat_id: Unique c** (1 connections) — `server/services/combat_monitoring_service.py`
- **Start monitoring a combat turn.          Args:             combat_id: Unique com** (1 connections) — `server/services/combat_monitoring_service.py`
- **End monitoring a combat turn.          Args:             combat_id: Unique comba** (1 connections) — `server/services/combat_monitoring_service.py`
- **Resolve an alert.          Args:             alert_id: Alert identifier** (1 connections) — `server/services/combat_monitoring_service.py`
- **Clear resolved alerts.          Returns:             int: Number of alerts clear** (1 connections) — `server/services/combat_monitoring_service.py`
- **Update timing metrics with new combat duration.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Update turn timing metrics.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Save current metrics as a snapshot.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Refresh configuration from source.** (1 connections) — `server/services/combat_monitoring_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [Server Services (93)](Server_Services_%2893%29.md) (6 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (5 shared connections)
- [Server Services (92)](Server_Services_%2892%29.md) (4 shared connections)
- [Server Services (39)](Server_Services_%2839%29.md) (4 shared connections)
- [Server Services (115)](Server_Services_%28115%29.md) (2 shared connections)
- [Server Services (116)](Server_Services_%28116%29.md) (2 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 80 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*