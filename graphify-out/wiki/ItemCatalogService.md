# ItemCatalogService

> 36 nodes

## Key Concepts

- **ItemCatalogService** (35 connections) — `server/game/item_catalog_service.py`
- **test_catalog_commands.py** (34 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **parse_catalog_args()** (11 connections) — `server/commands/catalog_commands.py`
- **_request_with()** (11 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **asyncio** (10 connections)
- **_player_response()** (9 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_container_without_service_attr()** (9 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_success()** (7 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_admin_from_player()** (6 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_player_object_user_without_get()** (6 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogAppStateStub** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogAppStub** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_admin_from_user_flags()** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_is_false_for_a_plain_player_with_no_flags()** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_trusts_the_stored_player_over_the_user_flags()** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogContainerStub** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogRequestStub** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_format_catalog_output_player()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_failure()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_falls_back_to_flags_when_the_lookup_fails()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_persistence_returning()** (3 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_without_a_request_reads_only_the_user_flags()** (3 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **.__init__()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **.__init__()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **.__init__()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- *... and 11 more nodes in this community*

## Relationships

- [catalog_commands.py](catalog_commands.py.md) (15 shared connections)
- [ItemCatalogResponse](ItemCatalogResponse.md) (13 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (10 shared connections)
- [test_item_catalog.py](test_item_catalog.py.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)

## Source Files

- `server/commands/catalog_commands.py`
- `server/game/item_catalog_service.py`
- `server/tests/unit/commands/test_catalog_commands.py`

## Audit Trail

- EXTRACTED: 113 (86%)
- INFERRED: 19 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*