# server container bundles combat combatbundle

> 66 nodes

## Key Concepts

- **CatatoniaRegistry** (42 connections) — `server/services/catatonia_registry.py`
- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
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
- **.test_on_catatonia_entered_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- *... and 41 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server app lifespan protocols nats](server_app_lifespan_protocols_nats.md) (1 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (1 shared connections)
- [server dependencies](server_dependencies.md) (1 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (1 shared connections)
- [server models lucidity](server_models_lucidity.md) (1 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (1 shared connections)
- [server services combat service types](server_services_combat_service_types.md) (1 shared connections)
- [server constants spawn defaults](server_constants_spawn_defaults.md) (1 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (1 shared connections)
- [passivelucidityfluxservice](passivelucidityfluxservice.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 112 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*