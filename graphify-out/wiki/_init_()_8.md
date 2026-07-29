# . init ()

> 64 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **get_player_service()** (12 connections) — `server/dependencies.py`
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
- **get_chat_service()** (9 connections) — `server/dependencies.py`
- *... and 39 more nodes in this community*

## Relationships

- [get room service()](get_room_service%28%29.md) (26 shared connections)
- [character creation](character_creation.md) (18 shared connections)
- [. init ()](_init_%28%29.md) (18 shared connections)
- [main()](main%28%29.md) (15 shared connections)
- [Connection Manager](Connection_Manager.md) (8 shared connections)
- [.initialize()](initialize%28%29.md) (7 shared connections)
- [Tests for get spell targeting](Tests_for_get_spell_targeting.md) (6 shared connections)
- [get nats message handler()](get_nats_message_handler%28%29.md) (5 shared connections)
- [get skill repository()](get_skill_repository%28%29.md) (5 shared connections)
- [BaseUserManager](BaseUserManager.md) (4 shared connections)
- [.shutdown()](shutdown%28%29.md) (4 shared connections)
- [. repr ()](_repr_%28%29.md) (4 shared connections)

## Source Files

- `server/database.py`
- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 453 (85%)
- INFERRED: 82 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*