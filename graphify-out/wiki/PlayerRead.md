# PlayerRead

> 61 nodes

## Key Concepts

- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **.resolve_player_name()** (4 connections) — `server/game/player_search_service.py`
- **test_player_create_custom_stats()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read_defaults()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_search_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_search_service.py`
- **.validate_player_name()** (3 connections) — `server/game/player_search_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_service.py`
- **.get_player_by_name()** (3 connections) — `server/game/player_service.py`
- **.list_players()** (3 connections) — `server/game/player_service.py`
- **.resolve_player_name()** (3 connections) — `server/game/player_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_service.py`
- **.resolve_player_name()** (3 connections) — `server/services/target_resolution_service.py`
- **test_character_info()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_character_info_defaults()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_base()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_base_rejects_extra_fields()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- *... and 36 more nodes in this community*

## Relationships

- [players.py](players.py.md) (24 shared connections)
- [PlayerService](PlayerService.md) (19 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (6 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (5 shared connections)
- [player_schema_converter.py](player_schema_converter.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [Stats](Stats.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [players/__init__.py](players-__init__.py.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/player.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 133 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*