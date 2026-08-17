# server models player playerchannelpreferences

> 91 nodes

## Key Concepts

- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **PlayerInventory** (16 connections) — `server/models/player.py`
- **PlayerChannelPreferences** (15 connections) — `server/models/player.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **PlayerExploration** (10 connections) — `server/models/player.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.update_player_last_active()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **UUID** (6 connections)
- **.delete_player()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.soft_delete_player()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **Any** (5 connections)
- **_coerce_row_stats()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_numerics()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- *... and 66 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (32 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (12 shared connections)
- [server game skill service](server_game_skill_service.md) (5 shared connections)
- [server persistence repositories player repository](server_persistence_repositories_player_repository.md) (5 shared connections)
- [server tests unit persistence test](server_tests_unit_persistence_test.md) (5 shared connections)
- [f](f.md) (3 shared connections)
- [server services player preferences service](server_services_player_preferences_service.md) (2 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (2 shared connections)
- [server persistence container data](server_persistence_container_data.md) (1 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 183 (86%)
- INFERRED: 29 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*