# monitoring combat service

> 51 nodes

## Key Concepts

- **test_combat_monitoring_service.py** (52 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **mock_combat_config()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_end_combat_monitoring_success()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_end_combat_monitoring_failure()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_end_combat_monitoring_not_found()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_start_turn_monitoring()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_record_combat_error_validation()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_record_combat_error_system()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_update_resource_metrics()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_remove_alert_callback()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_active_alerts()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_all_alerts()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_resolve_alert()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_resolve_alert_not_found()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_clear_resolved_alerts()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_monitoring_summary()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_error_threshold()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_resource_thresholds_cpu()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_performance_threshold()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_generate_alert()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_generate_alert_callback_error()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_save_metrics_snapshot()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_refresh_configuration()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_metrics_to_dict()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_update_turn_timing_metrics()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- *... and 26 more nodes in this community*

## Relationships

- [combat monitoring service](combat_monitoring_service.md) (9 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (3 shared connections)
- [realtime nats message](realtime_nats_message.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (2 shared connections)
- [skill game service](skill_game_service.md) (2 shared connections)
- [subzone realtime nats](subzone_realtime_nats.md) (2 shared connections)
- [message chat realtime](message_chat_realtime.md) (1 shared connections)
- [message realtime nats](message_realtime_nats.md) (1 shared connections)
- [realtime npc event](realtime_npc_event.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 126 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*