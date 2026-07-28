# Server Infrastructure

> 242 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (36 connections)
- **Request** (29 connections)
- **game.py** (25 connections) — `server/api/game.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_combat_service()** (10 connections) — `server/dependencies.py`
- **LevelService** (10 connections) — `server/game/level_service.py`
- **get_player_service_for_testing()** (9 connections) — `server/dependencies.py`
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
- *... and 217 more nodes in this community*

## Relationships

- [Server Api (3)](Server_Api_%283%29.md) (42 shared connections)
- [Server Api (4)](Server_Api_%284%29.md) (16 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (12 shared connections)
- [Server Game (8)](Server_Game_%288%29.md) (12 shared connections)
- [Server Admin](Server_Admin.md) (11 shared connections)
- [Server Api (7)](Server_Api_%287%29.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (8 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (6 shared connections)
- [Server App](Server_App.md) (5 shared connections)
- [Server Game (9)](Server_Game_%289%29.md) (5 shared connections)
- [Server Services](Server_Services.md) (4 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (3 shared connections)

## Source Files

- `server/api/game.py`
- `server/dependencies.py`
- `server/game/level_service.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 945 (88%)
- INFERRED: 126 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*