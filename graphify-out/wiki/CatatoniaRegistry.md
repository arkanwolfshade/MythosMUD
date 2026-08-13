# CatatoniaRegistry

> 11 nodes

## Key Concepts

- **CatatoniaRegistry** (42 connections) — `server/services/catatonia_registry.py`
- **.test_is_catatonic_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_callback_exception()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_debounced_does_not_invoke_callback_twice()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_without_callback()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.__init__()** (1 connections) — `server/services/catatonia_registry.py`
- **Track players who have entered catatonia and coordinate failover hooks.** (1 connections) — `server/services/catatonia_registry.py`
- **Test on_sanitarium_failover without callback.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test on_sanitarium_failover handles callback exceptions.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test is_catatonic with UUID player_id.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Second on_sanitarium_failover within debounce window does not invoke callback.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`

## Relationships

- [TestCatatoniaRegistry](TestCatatoniaRegistry.md) (11 shared connections)
- [catatonia_registry.py](catatonia_registry.py.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [test_catatonia_registry.py](test_catatonia_registry.py.md) (2 shared connections)
- [.test_get_snapshot_with_players](test_get_snapshot_with_players.md) (1 shared connections)
- [.test_init_with_failover_callback](test_init_with_failover_callback.md) (1 shared connections)
- [.test_is_catatonic_after_cleared](test_is_catatonic_after_cleared.md) (1 shared connections)
- [.test_is_catatonic_with_string](test_is_catatonic_with_string.md) (1 shared connections)
- [.test_multiple_players_catatonic](test_multiple_players_catatonic.md) (1 shared connections)
- [.test_on_catatonia_cleared_not_registered](test_on_catatonia_cleared_not_registered.md) (1 shared connections)
- [.test_on_catatonia_cleared_with_string](test_on_catatonia_cleared_with_string.md) (1 shared connections)
- [.test_on_catatonia_cleared_with_uuid](test_on_catatonia_cleared_with_uuid.md) (1 shared connections)

## Source Files

- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 48 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*