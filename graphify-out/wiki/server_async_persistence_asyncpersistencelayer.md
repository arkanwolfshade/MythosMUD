# server async persistence asyncpersistencelayer

> 117 nodes

## Key Concepts

- **AsyncPersistenceLayer** (165 connections) — `server/async_persistence.py`
- **Player** (19 connections)
- **Any** (17 connections)
- **UUID** (15 connections)
- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **fetch_professions()** (8 connections) — `server/async_persistence_direct_queries.py`
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
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **async_persistence_layer()** (4 connections) — `server/tests/unit/infrastructure/conftest.py`
- *... and 92 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (49 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (7 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (5 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (4 shared connections)
- [server events event bus](server_events_event_bus.md) (4 shared connections)
- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [characterinfo](characterinfo.md) (3 shared connections)
- [server game movement helpers](server_game_movement_helpers.md) (3 shared connections)
- [maprooms](maprooms.md) (2 shared connections)
- [server api monitoring](server_api_monitoring.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/tests/unit/infrastructure/conftest.py`

## Audit Trail

- EXTRACTED: 260 (86%)
- INFERRED: 42 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*