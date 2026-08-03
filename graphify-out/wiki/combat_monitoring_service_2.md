# combat monitoring service

> 30 nodes

## Key Concepts

- **CombatMonitoringService** (32 connections) — `server/services/combat_monitoring_service.py`
- **.end_combat_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_turn_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.add_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.remove_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_turn_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
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
- **Add alert callback function.          Args:             callback: Function to ca** (1 connections) — `server/services/combat_monitoring_service.py`
- **Remove alert callback function.          Args:             callback: Function to** (1 connections) — `server/services/combat_monitoring_service.py`
- **Resolve an alert.          Args:             alert_id: Alert identifier** (1 connections) — `server/services/combat_monitoring_service.py`
- **Clear resolved alerts.          Returns:             int: Number of alerts clear** (1 connections) — `server/services/combat_monitoring_service.py`
- **Update timing metrics with new combat duration.** (1 connections) — `server/services/combat_monitoring_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [logoutHandler logger App](logoutHandler_logger_App.md) (6 shared connections)
- [main rationale failure()](main_rationale_failure%28%29.md) (4 shared connections)
- [monitoring combat service](monitoring_combat_service.md) (4 shared connections)
- [event bus events](event_bus_events.md) (3 shared connections)
- [combat monitoring service](combat_monitoring_service.md) (2 shared connections)
- [skill game service](skill_game_service.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 84 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*