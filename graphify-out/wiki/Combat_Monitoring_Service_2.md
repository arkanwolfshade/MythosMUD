# Combat Monitoring Service

> 73 nodes · cohesion 0.04

## Key Concepts

- **CombatMonitoringService** (32 connections) — `server/services/combat_monitoring_service.py`
- **combat_monitoring_service.py** (21 connections) — `server/services/combat_monitoring_service.py`
- **._generate_alert()** (9 connections) — `server/services/combat_monitoring_service.py`
- **Any** (9 connections)
- **.to_dict()** (7 connections) — `server/services/combat_monitoring_service.py`
- **Alert** (6 connections) — `server/services/combat_monitoring_service.py`
- **AlertSeverity** (5 connections) — `server/services/combat_monitoring_service.py`
- **AlertType** (5 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_monitoring()** (5 connections) — `server/services/combat_monitoring_service.py`
- **._check_error_threshold()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._check_resource_thresholds()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_active_alerts()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_all_alerts()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_metrics_history()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_monitoring_summary()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.record_combat_error()** (4 connections) — `server/services/combat_monitoring_service.py`
- **test_get_combat_monitoring()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **.to_dict()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.add_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._check_performance_threshold()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_combat_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_turn_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.remove_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.update_resource_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- *... and 48 more nodes in this community*

## Relationships

- [Circuit Breaker Core](Circuit_Breaker_Core.md) (9 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Combat Feature Flags](Combat_Feature_Flags.md) (2 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 220 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*