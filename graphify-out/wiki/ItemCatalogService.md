# ItemCatalogService

> 32 nodes

## Key Concepts

- **ItemCatalogService** (35 connections) — `server/game/item_catalog_service.py`
- **test_catalog_commands.py** (29 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **handle_catalog_command()** (14 connections) — `server/commands/catalog_commands.py`
- **parse_catalog_args()** (11 connections) — `server/commands/catalog_commands.py`
- **_player_response()** (9 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_container_without_service_attr()** (9 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_request_with()** (8 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_success()** (7 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_admin_from_player()** (6 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_player_object_user_without_get()** (6 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **asyncio** (6 connections)
- **_CatalogAppStateStub** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogAppStub** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_admin_from_user_flags()** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogContainerStub** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogRequestStub** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_failure()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **.__init__()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **.__init__()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **.__init__()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_parse_catalog_args_defaults()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_parse_catalog_args_explicit_search_wins_over_bare()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_parse_catalog_args_filters_and_bare_search()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_parse_catalog_args_invalid_page_and_page_size()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_parse_catalog_args_skips_blank_unknown_keys_become_bare_search()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- *... and 7 more nodes in this community*

## Relationships

- [catalog_commands.py](catalog_commands.py.md) (23 shared connections)
- [test_item_catalog.py](test_item_catalog.py.md) (11 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (8 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/commands/catalog_commands.py`
- `server/game/item_catalog_service.py`
- `server/tests/unit/commands/test_catalog_commands.py`

## Audit Trail

- EXTRACTED: 99 (83%)
- INFERRED: 20 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*