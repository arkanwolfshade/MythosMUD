# Test Combat Monitoring Service

> 160 nodes

## Key Concepts

- **test_combat_monitoring_service.py** (53 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **CombatMonitoringService** (32 connections) — `server/services/combat_monitoring_service.py`
- **combat_monitoring_service.py** (21 connections) — `server/services/combat_monitoring_service.py`
- **AlertType** (15 connections) — `server/services/combat_monitoring_service.py`
- **AlertSeverity** (12 connections) — `server/services/combat_monitoring_service.py`
- **CombatMetrics** (11 connections) — `server/services/combat_monitoring_service.py`
- **._generate_alert()** (9 connections) — `server/services/combat_monitoring_service.py`
- **Any** (9 connections)
- **.__init__()** (7 connections) — `server/services/combat_monitoring_service.py`
- **Alert** (5 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_metrics()** (5 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_monitoring()** (5 connections) — `server/services/combat_monitoring_service.py`
- **._check_error_threshold()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._check_resource_thresholds()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.record_combat_error()** (4 connections) — `server/services/combat_monitoring_service.py`
- **monitoring_service()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_alert_to_dict()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_clear_resolved_alerts()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_generate_alert()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_generate_alert_callback_error()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_active_alerts()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_all_alerts()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_combat_metrics()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_combat_monitoring()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_resolve_alert()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- *... and 135 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Test Config Init](Test_Config_Init.md) (3 shared connections)
- [Test Feature Flag Service](Test_Feature_Flag_Service.md) (3 shared connections)
- [Test Combat Configuration Service](Test_Combat_Configuration_Service.md) (3 shared connections)
- [Mythos Mud Mapbuilder](Mythos_Mud_Mapbuilder.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 214 (90%)
- INFERRED: 23 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*