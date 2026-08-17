# PlayerService

> 350 nodes

## Key Concepts

- **PlayerService** (106 connections) — `server/game/player_service.py`
- **players.py** (73 connections) — `server/api/players.py`
- **server/schemas/__init__.py** (70 connections) — `server/schemas/__init__.py`
- **test_players_api_coverage.py** (56 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **player_service.py** (49 connections) — `server/game/player_service.py`
- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
- **StatusEffect** (31 connections) — `server/models/game.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (25 connections)
- **test_player_schemas.py** (23 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player_schema_converter.py** (22 connections) — `server/game/player_schema_converter.py`
- **players/player.py** (21 connections) — `server/schemas/players/player.py`
- **test_player_schema_converter_weapon.py** (20 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **get_player_quests()** (18 connections) — `server/api/players.py`
- **InventoryItem** (17 connections) — `server/models/game.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **select_character()** (15 connections) — `server/api/players.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **UUID** (14 connections)
- **test_players_quests.py** (14 connections) — `server/tests/unit/api/test_players_quests.py`
- *... and 325 more nodes in this community*

## Relationships

- [User](User.md) (49 shared connections)
- [get_logger](get_logger.md) (45 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (43 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (26 shared connections)
- [TargetMatch](TargetMatch.md) (22 shared connections)
- [ValidationError](ValidationError.md) (16 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (15 shared connections)
- [Player](Player.md) (14 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (13 shared connections)
- [Stats](Stats.md) (13 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (11 shared connections)
- [schemas/admin/__init__.py](schemas-admin-__init__.py.md) (11 shared connections)

## Source Files

- `server/api/players.py`
- `server/app/game_tick_processing.py`
- `server/commands/combat_handler.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/models/game.py`
- `server/schemas/__init__.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`

## Audit Trail

- EXTRACTED: 1157 (96%)
- INFERRED: 52 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*