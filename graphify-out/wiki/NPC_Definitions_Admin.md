# NPC Definitions Admin

> 205 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_connection_manager()** (10 connections) — `server/dependencies.py`
- **get_async_persistence()** (10 connections) — `server/dependencies.py`
- **get_combat_service()** (10 connections) — `server/dependencies.py`
- **get_player_service_for_testing()** (9 connections) — `server/dependencies.py`
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
- *... and 180 more nodes in this community*

## Relationships

- [Player Stats](Player_Stats.md) (30 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (12 shared connections)
- [System Metrics](System_Metrics.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (8 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (7 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (7 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (6 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (5 shared connections)
- [Exception Containers](Exception_Containers.md) (4 shared connections)
- [nats services service](nats_services_service.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (4 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 789 (87%)
- INFERRED: 114 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*