# container

> 8 nodes

## Key Concepts

- **monitoring_service()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **fixture** (4 connections)
- **mock_combat_config()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **mock_feature_flags()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **mock_config()** (2 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Create mock feature flags.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Create mock combat config.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Create CombatMonitoringService instance with mocked dependencies.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`

## Relationships

- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (4 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 11 (92%)
- INFERRED: 1 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*