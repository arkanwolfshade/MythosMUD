# player.ts

> 66 nodes · cohesion 0.05

## Key Concepts

- **CatatoniaRegistry** (42 connections) — `server/services/catatonia_registry.py`
- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **catatonia_registry.py** (12 connections) — `server/services/catatonia_registry.py`
- **UUID** (6 connections)
- **test_catatonia_registry.py** (5 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.is_catatonic()** (4 connections) — `server/services/catatonia_registry.py`
- **datetime** (4 connections)
- **.test_on_sanitarium_failover_callback_exception()** (4 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_with_async_callback()** (4 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.get_snapshot()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_cleared()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_entered()** (3 connections) — `server/services/catatonia_registry.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/catatonia_registry.py`
- **.test_get_snapshot_empty()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_get_snapshot_is_copy()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_get_snapshot_with_players()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_init_with_failover_callback()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_is_catatonic_after_cleared()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_is_catatonic_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_is_catatonic_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_multiple_players_catatonic()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_not_registered()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- *... and 41 more nodes in this community*

## Relationships

- [Room](Room.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [PopulationStats](PopulationStats.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (1 shared connections)
- [go_command.py](go_command.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 113 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*