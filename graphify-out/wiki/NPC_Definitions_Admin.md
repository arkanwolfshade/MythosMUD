# NPC Definitions Admin

> 233 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **LevelService** (13 connections) — `server/game/level_service.py`
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
- *... and 208 more nodes in this community*

## Relationships

- [player service game](player_service_game.md) (48 shared connections)
- [NPC Combat](NPC_Combat.md) (12 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [game models player](game_models_player.md) (5 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (5 shared connections)
- [spell game magic](spell_game_magic.md) (5 shared connections)
- [profession game service](profession_game_service.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [room game service](room_game_service.md) (3 shared connections)

## Source Files

- `server/dependencies.py`
- `server/game/level_service.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 830 (88%)
- INFERRED: 109 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*