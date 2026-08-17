# AlertType

> 25 nodes

## Key Concepts

- **AlertType** (15 connections) — `server/services/combat_monitoring_service.py`
- **AlertSeverity** (12 connections) — `server/services/combat_monitoring_service.py`
- **test_alert_to_dict()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_clear_resolved_alerts()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_generate_alert()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_generate_alert_callback_error()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_active_alerts()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_all_alerts()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_resolve_alert()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_error_threshold()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_resource_thresholds_cpu()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_check_resource_thresholds_memory()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Enum** (3 connections)
- **Alert severity levels.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Alert types for combat monitoring.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Test get_active_alerts returns unresolved alerts.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test get_all_alerts returns all alerts.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test resolve_alert resolves an alert.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test clear_resolved_alerts removes resolved alerts.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test _check_error_threshold generates alert when exceeded.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test _check_resource_thresholds generates alert for high memory.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test _check_resource_thresholds generates alert for high CPU.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test _generate_alert creates and dispatches alert.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test _generate_alert handles callback errors gracefully.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test Alert.to_dict converts to dictionary.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`

## Relationships

- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (12 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (3 shared connections)
- [._generate_alert](_generate_alert.md) (2 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 31 (65%)
- INFERRED: 17 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*