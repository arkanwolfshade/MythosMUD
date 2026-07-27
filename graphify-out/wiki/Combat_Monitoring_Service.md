# Combat Monitoring Service

> 80 nodes · cohesion 0.03

## Key Concepts

- **test_combat_monitoring_service.py** (50 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **get_combat_monitoring()** (5 connections) — `server/services/combat_monitoring_service.py`
- **test_get_combat_monitoring()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **mock_combat_config()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **mock_feature_flags()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test _check_resource_thresholds generates alert for high memory.** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_add_alert_callback()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_alert_to_dict()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_error_threshold()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_performance_threshold()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_resource_thresholds_cpu()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_resource_thresholds_memory()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_clear_resolved_alerts()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_combat_monitoring_service_init()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_end_combat_monitoring_failure()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_end_combat_monitoring_not_found()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_end_combat_monitoring_success()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_end_turn_monitoring()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_end_turn_monitoring_not_found()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_generate_alert()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_generate_alert_callback_error()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_active_alerts()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_all_alerts()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_current_metrics()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_metrics_history()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- *... and 55 more nodes in this community*

## Relationships

- [[Services Combat Service]] (6 shared connections)
- [[Combat Monitoring Service]] (5 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 173 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
