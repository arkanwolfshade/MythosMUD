# CatatoniaRegistry

> 14 nodes

## Key Concepts

- **CatatoniaRegistry** (42 connections) — `server/services/catatonia_registry.py`
- **UUID** (6 connections)
- **.is_catatonic()** (4 connections) — `server/services/catatonia_registry.py`
- **datetime** (4 connections)
- **.get_snapshot()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_cleared()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_entered()** (3 connections) — `server/services/catatonia_registry.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_sanitarium_failover()** (2 connections) — `server/services/catatonia_registry.py`
- **.__init__()** (1 connections) — `server/services/catatonia_registry.py`
- **Return True if the player is currently registered as catatonic.** (1 connections) — `server/services/catatonia_registry.py`
- **Return a shallow copy of the current registry for diagnostics.** (1 connections) — `server/services/catatonia_registry.py`
- **Track players who have entered catatonia and coordinate failover hooks.** (1 connections) — `server/services/catatonia_registry.py`
- **Return True if we should trigger sanitarium failover for this player (not…** (1 connections) — `server/services/catatonia_registry.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [TestCatatoniaRegistry](TestCatatoniaRegistry.md) (7 shared connections)
- [test_catatonia_registry.py](test_catatonia_registry.py.md) (2 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (1 shared connections)
- [.test_get_snapshot_is_copy](test_get_snapshot_is_copy.md) (1 shared connections)
- [.test_get_snapshot_with_players](test_get_snapshot_with_players.md) (1 shared connections)
- [.test_init](test_init.md) (1 shared connections)
- [.test_init_with_failover_callback](test_init_with_failover_callback.md) (1 shared connections)
- [.test_is_catatonic_after_cleared](test_is_catatonic_after_cleared.md) (1 shared connections)
- [.test_multiple_players_catatonic](test_multiple_players_catatonic.md) (1 shared connections)
- [.test_on_catatonia_cleared_not_registered](test_on_catatonia_cleared_not_registered.md) (1 shared connections)
- [.test_on_catatonia_cleared_with_string](test_on_catatonia_cleared_with_string.md) (1 shared connections)

## Source Files

- `server/services/catatonia_registry.py`

## Audit Trail

- EXTRACTED: 53 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*