# server async persistence asyncpersistencelayer

> 118 nodes

## Key Concepts

- **AsyncPersistenceLayer** (167 connections) — `server/async_persistence.py`
- **Player** (19 connections)
- **Any** (17 connections)
- **UUID** (15 connections)
- **profession_service.py** (13 connections) — `server/game/profession_service.py`
- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **infrastructure/conftest.py** (6 connections) — `server/tests/unit/infrastructure/conftest.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.add_player_effect()** (4 connections) — `server/async_persistence.py`
- **.create_container()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.get_user_by_username_case_insensitive()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- *... and 93 more nodes in this community*

## Relationships

- [server async persistence](server_async_persistence.md) (29 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (4 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (4 shared connections)
- [server api container events](server_api_container_events.md) (4 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (4 shared connections)
- [server services container service](server_services_container_service.md) (4 shared connections)
- [server game mechanics](server_game_mechanics.md) (4 shared connections)
- [server game movement helpers](server_game_movement_helpers.md) (3 shared connections)
- [server events event types npcdied](server_events_event_types_npcdied.md) (3 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (3 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/game/profession_service.py`
- `server/tests/unit/infrastructure/conftest.py`

## Audit Trail

- EXTRACTED: 275 (88%)
- INFERRED: 37 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*