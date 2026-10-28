# test_security_validator.py

> 214 nodes · cohesion 0.02

## Key Concepts

- **LoggedHTTPException** (379 connections) — `server/exceptions.py`
- **PlayerService** (113 connections) — `server/game/player_service.py`
- **players.py** (77 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (59 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_user()** (32 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (30 connections)
- **api/player_respawn.py** (28 connections) — `server/api/player_respawn.py`
- **get_player_quests()** (18 connections) — `server/api/players.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **test_player_respawn_api.py** (17 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **FastAPIRequest** (16 connections)
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **delete_player()** (15 connections) — `server/api/players.py`
- **get_player()** (15 connections) — `server/api/players.py`
- **select_character()** (15 connections) — `server/api/players.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **create_player()** (13 connections) — `server/api/players.py`
- **delete_character()** (13 connections) — `server/api/players.py`
- **get_player_skills()** (13 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- *... and 189 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (80 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (61 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (60 shared connections)
- [test_look_player.py](test_look_player.py.md) (24 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (22 shared connections)
- [Player](Player.md) (19 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (19 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (17 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (16 shared connections)
- [AttributeError](AttributeError.md) (15 shared connections)
- [CombatParticipant](CombatParticipant.md) (15 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (15 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/api/players.py`
- `server/api/skills.py`
- `server/exceptions.py`
- `server/game/player_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/players/skill.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 938 (83%)
- INFERRED: 186 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*