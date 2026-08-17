# server api players

> 142 nodes

## Key Concepts

- **PlayerService** (103 connections) — `server/game/player_service.py`
- **players.py** (73 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (56 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (25 connections)
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **select_character()** (15 connections) — `server/api/players.py`
- **UUID** (14 connections)
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
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **Any** (11 connections)
- **get_available_classes()** (10 connections) — `server/api/players.py`
- **get_player_by_name()** (10 connections) — `server/api/players.py`
- **get_user_characters()** (10 connections) — `server/api/players.py`
- **start_login_grace_period_endpoint()** (10 connections) — `server/api/players.py`
- *... and 117 more nodes in this community*

## Relationships

- [server api character creation](server_api_character_creation.md) (43 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (33 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (25 shared connections)
- [server api players get player](server_api_players_get_player.md) (13 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [leveluphook](leveluphook.md) (10 shared connections)
- [server api player effects](server_api_player_effects.md) (8 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (5 shared connections)
- [server game player creation service](server_game_player_creation_service.md) (5 shared connections)
- [server api skills get skills](server_api_skills_get_skills.md) (5 shared connections)
- [server game magic spell materials](server_game_magic_spell_materials.md) (4 shared connections)

## Source Files

- `server/api/players.py`
- `server/app/game_tick_processing.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_service.py`
- `server/schemas/players/player.py`
- `server/tests/unit/api/test_players_api_coverage.py`

## Audit Trail

- EXTRACTED: 508 (93%)
- INFERRED: 39 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*