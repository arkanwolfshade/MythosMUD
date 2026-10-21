# container_endpoints_basic.py

> 508 nodes · cohesion 0.01

## Key Concepts

- **_Request** (200 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **server/dependencies.py** (112 connections) — `server/dependencies.py`
- **api/character_creation.py** (66 connections) — `server/api/character_creation.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **player_service.py** (55 connections) — `server/game/player_service.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **PlayerRead** (47 connections) — `server/schemas/players/player.py`
- **test_player_model.py** (47 connections) — `server/tests/unit/models/test_player_model.py`
- **SkillService** (45 connections) — `server/game/skill_service.py`
- **server/models/game.py** (42 connections) — `server/models/game.py`
- **get_container()** (40 connections) — `server/dependencies.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (25 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **player_schema_converter.py** (22 connections) — `server/game/player_schema_converter.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **professions.py** (20 connections) — `server/api/professions.py`
- **players/player.py** (20 connections) — `server/schemas/players/player.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **PositionState** (17 connections) — `server/models/game.py`
- **player_creation_service.py** (16 connections) — `server/game/player_creation_service.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- *... and 483 more nodes in this community*

## Relationships

- [test_security_validator.py](test_security_validator.py.md) (80 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (45 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (42 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (35 shared connections)
- [testing_examples.py](testing_examples.py.md) (33 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (29 shared connections)
- [Room](Room.md) (27 shared connections)
- [Player](Player.md) (21 shared connections)
- [AttributeError](AttributeError.md) (19 shared connections)
- [test_look_player.py](test_look_player.py.md) (16 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (14 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/professions.py`
- `server/dependencies.py`
- `server/game/level_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/player_creation_service.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/models/game.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_professions_endpoints.py`

## Audit Trail

- EXTRACTED: 1571 (98%)
- INFERRED: 35 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*