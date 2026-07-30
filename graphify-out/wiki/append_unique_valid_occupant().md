# append unique valid occupant()

> 208 nodes

## Key Concepts

- **PlayerService** (140 connections) — `server/game/player_service.py`
- **players.py** (66 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **Any** (11 connections)
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
- **CharacterInfo** (10 connections) — `server/schemas/players/player.py`
- **get_player_skills()** (9 connections) — `server/api/players.py`
- *... and 183 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (49 shared connections)
- [Player](Player.md) (34 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (22 shared connections)
- [metrics](metrics.md) (21 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (20 shared connections)
- [message handler factory](message_handler_factory.md) (17 shared connections)
- [.initialize()](initialize%28%29.md) (13 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (12 shared connections)
- [Room](Room.md) (10 shared connections)
- [real time](real_time.md) (7 shared connections)
- [login grace period](login_grace_period.md) (7 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (6 shared connections)

## Source Files

- `server/api/players.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/game/test_player_service_mutations.py`
- `server/tests/unit/schemas/test_player_schemas.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 969 (90%)
- INFERRED: 107 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*