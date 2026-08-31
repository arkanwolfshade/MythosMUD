# CatatoniaRegistry

> 69 nodes

## Key Concepts

- **CatatoniaRegistry** (42 connections) — `server/services/catatonia_registry.py`
- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **catatonia_registry.py** (13 connections) — `server/services/catatonia_registry.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **UUID** (6 connections)
- **test_catatonia_registry.py** (6 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.is_catatonic()** (4 connections) — `server/services/catatonia_registry.py`
- **.test_on_sanitarium_failover_with_async_callback()** (4 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **datetime** (4 connections)
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
- *... and 44 more nodes in this community*

## Relationships

- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [LucidityService](LucidityService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (1 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (1 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 121 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*