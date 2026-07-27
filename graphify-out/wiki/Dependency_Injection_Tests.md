# Dependency Injection Tests

> 139 nodes · cohesion 0.02

## Key Concepts

- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **Request** (29 connections) — `server/dependencies.py`
- **test_dependency_injection.py** (15 connections) — `server/tests/unit/test_dependency_injection.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_async_persistence()** (9 connections) — `server/dependencies.py`
- **get_combat_service()** (9 connections) — `server/dependencies.py`
- **get_chat_service()** (8 connections) — `server/dependencies.py`
- **get_exploration_service()** (8 connections) — `server/dependencies.py`
- **get_magic_service()** (8 connections) — `server/dependencies.py`
- **get_mp_regeneration_service()** (8 connections) — `server/dependencies.py`
- **get_mythos_time_consumer()** (8 connections) — `server/dependencies.py`
- **get_npc_lifecycle_manager()** (8 connections) — `server/dependencies.py`
- **get_player_combat_service()** (8 connections) — `server/dependencies.py`
- **get_player_death_service()** (8 connections) — `server/dependencies.py`
- **get_player_respawn_service()** (8 connections) — `server/dependencies.py`
- **get_profession_service()** (8 connections) — `server/dependencies.py`
- **get_spell_registry()** (8 connections) — `server/dependencies.py`
- **TestGetContainer** (8 connections) — `server/tests/unit/test_dependency_injection.py`
- **Tests for get_player_service dependency function.** (7 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetContainer** (6 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_level_service()** (6 connections) — `server/dependencies.py`
- **get_quest_service()** (6 connections) — `server/dependencies.py`
- **get_skill_service()** (6 connections) — `server/dependencies.py`
- *... and 114 more nodes in this community*

## Relationships

- [[Dependencies Infrastructure]] (36 shared connections)
- [[NPC Admin API]] (22 shared connections)
- [[Combat Command Handler]] (19 shared connections)
- [[Database Manager Tests]] (18 shared connections)
- [[Character Stats Generator]] (9 shared connections)
- [[Dependency Injection Dependencies]] (8 shared connections)
- [[Async Persistence Layer]] (7 shared connections)
- [[Maps API Endpoints]] (2 shared connections)
- [[Application DI Bundles]] (1 shared connections)
- [[Players API Endpoints]] (1 shared connections)
- [[Argon2 Password Hashing]] (1 shared connections)
- [[Game Profession Service]] (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 533 (92%)
- INFERRED: 44 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
