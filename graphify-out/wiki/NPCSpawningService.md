# NPCSpawningService

> 145 nodes

## Key Concepts

- **LoggedHTTPException** (271 connections) — `server/exceptions.py`
- **players.py** (73 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (56 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (25 connections)
- **get_player_quests()** (18 connections) — `server/api/players.py`
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **select_character()** (15 connections) — `server/api/players.py`
- **test_players_quests.py** (14 connections) — `server/tests/unit/api/test_players_quests.py`
- **delete_player()** (13 connections) — `server/api/players.py`
- **get_player_skills()** (13 connections) — `server/api/players.py`
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **delete_character()** (12 connections) — `server/api/players.py`
- **get_player()** (12 connections) — `server/api/players.py`
- **create_player()** (11 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (11 connections) — `server/api/players.py`
- **list_players()** (11 connections) — `server/api/players.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **get_available_classes()** (10 connections) — `server/api/players.py`
- **get_player_by_name()** (10 connections) — `server/api/players.py`
- **get_user_characters()** (10 connections) — `server/api/players.py`
- **start_login_grace_period_endpoint()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- *... and 120 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (64 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (44 shared connections)
- [maps.py](maps.py.md) (29 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (28 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (18 shared connections)
- [ChatService](ChatService.md) (15 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (15 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (14 shared connections)
- [test_look_container.py](test_look_container.py.md) (14 shared connections)
- [test_player_position_service.py](test_player_position_service.py.md) (13 shared connections)
- [ValidationError](ValidationError.md) (12 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (11 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/players.py`
- `server/commands/admin_shutdown_command.py`
- `server/exceptions.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 630 (85%)
- INFERRED: 110 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*