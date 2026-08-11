# Rate Limiter Service

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

- [UI Animation Testing Standards](UI_Animation_Testing_Standards.md) (5 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (4 shared connections)
- [Dual Connection Troubleshooting](Dual_Connection_Troubleshooting.md) (2 shared connections)
- [E 2 E Runtime Multiplayer](E_2_E_Runtime_Multiplayer.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [test_build_room_objects_debug_logging](test_build_room_objects_debug_logging.md) (1 shared connections)
- [test_process_exit_rows_zone_single_part](test_process_exit_rows_zone_single_part.md) (1 shared connections)
- [test_build_room_objects_with_dict_attributes](test_build_room_objects_with_dict_attributes.md) (1 shared connections)
- [test_process_room_rows_with_partial_room_id](test_process_room_rows_with_partial_room_id.md) (1 shared connections)
- [test_load_room_cache_success](test_load_room_cache_success.md) (1 shared connections)
- [test_process_room_rows_empty_list](test_process_room_rows_empty_list.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 126 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*