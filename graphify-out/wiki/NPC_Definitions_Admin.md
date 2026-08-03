# NPC Definitions Admin

> 72 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
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
- *... and 47 more nodes in this community*

## Relationships

- [game models player](game_models_player.md) (12 shared connections)
- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (9 shared connections)
- [profession game service](profession_game_service.md) (8 shared connections)
- [NPC Combat](NPC_Combat.md) (8 shared connections)
- [command inventory models](command_inventory_models.md) (7 shared connections)
- [room game service](room_game_service.md) (7 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (6 shared connections)
- [nats services service](nats_services_service.md) (5 shared connections)
- [npc realtime occupant](npc_realtime_occupant.md) (5 shared connections)

## Source Files

- `server/database.py`
- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 489 (85%)
- INFERRED: 83 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*