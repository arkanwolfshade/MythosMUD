# exceptions.py

> 279 nodes · cohesion 0.01

## Key Concepts

- **exceptions.py** (194 connections) — `server/exceptions.py`
- **PlayerService** (138 connections) — `server/game/player_service.py`
- **players.py** (66 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **player_service.py** (44 connections) — `server/game/player_service.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **player_respawn_wrapper.py** (14 connections) — `server/game/player_respawn_wrapper.py`
- **UUID** (14 connections)
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- *... and 254 more nodes in this community*

## Relationships

- [__init__.py](__init__.py.md) (50 shared connections)
- [User](User.md) (35 shared connections)
- [dependencies.py](dependencies.py.md) (35 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (34 shared connections)
- [get_logger](get_logger.md) (32 shared connections)
- [ValidationError](ValidationError.md) (30 shared connections)
- [BaseCommand](BaseCommand.md) (27 shared connections)
- [DatabaseError](DatabaseError.md) (22 shared connections)
- [Player](Player.md) (17 shared connections)
- [CombatService](CombatService.md) (16 shared connections)
- [character_creation.py](character_creation.py.md) (15 shared connections)
- [MythosMUDError](MythosMUDError.md) (11 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/base.py`
- `server/api/players.py`
- `server/api/skills.py`
- `server/exceptions.py`
- `server/game/magic/spell_costs.py`
- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 1477 (93%)
- INFERRED: 110 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*