# NPC Definitions Admin

> 66 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_combat_service()** (10 connections) — `server/dependencies.py`
- **get_connection_manager()** (9 connections) — `server/dependencies.py`
- **get_async_persistence()** (9 connections) — `server/dependencies.py`
- **get_player_respawn_service()** (9 connections) — `server/dependencies.py`
- **get_player_combat_service()** (9 connections) — `server/dependencies.py`
- **get_player_death_service()** (9 connections) — `server/dependencies.py`
- **get_magic_service()** (9 connections) — `server/dependencies.py`
- **get_spell_registry()** (9 connections) — `server/dependencies.py`
- **get_spell_targeting_service()** (9 connections) — `server/dependencies.py`
- **get_spell_effects()** (9 connections) — `server/dependencies.py`
- **get_spell_learning_service()** (9 connections) — `server/dependencies.py`
- **get_mp_regeneration_service()** (9 connections) — `server/dependencies.py`
- **get_npc_lifecycle_manager()** (9 connections) — `server/dependencies.py`
- **get_npc_spawning_service()** (9 connections) — `server/dependencies.py`
- **get_npc_population_controller()** (9 connections) — `server/dependencies.py`
- **get_catatonia_registry()** (9 connections) — `server/dependencies.py`
- **get_passive_lucidity_flux_service()** (9 connections) — `server/dependencies.py`
- **get_mythos_time_consumer()** (9 connections) — `server/dependencies.py`
- *... and 41 more nodes in this community*

## Relationships

- [room infrastructure persistence](room_infrastructure_persistence.md) (32 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (24 shared connections)
- [persistence container extended](persistence_container_extended.md) (17 shared connections)
- [Error Conversion](Error_Conversion.md) (12 shared connections)
- [room cache infrastructure](room_cache_infrastructure.md) (12 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (6 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (5 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (4 shared connections)
- [nats services service](nats_services_service.md) (4 shared connections)
- [conftest eslint config](conftest_eslint_config.md) (4 shared connections)

## Source Files

- `server/database.py`
- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 458 (85%)
- INFERRED: 82 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*