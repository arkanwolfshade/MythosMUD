# Community 390

> 44 nodes

## Key Concepts

- **test_catalog_commands.py** (30 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **handle_catalog_command()** (14 connections) — `server/commands/catalog_commands.py`
- **resolve_is_admin()** (12 connections) — `server/commands/catalog_commands.py`
- **_request_with()** (11 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **parse_catalog_args()** (10 connections) — `server/commands/catalog_commands.py`
- **asyncio** (10 connections)
- **_player_response()** (9 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_container_without_service_attr()** (8 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_success()** (7 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_admin_from_player()** (6 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogAppStateStub** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogAppStub** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_player_object_user_without_get()** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_is_false_for_a_plain_player_with_no_flags()** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_trusts_the_stored_player_over_the_user_flags()** (5 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **ItemCatalogPlayerItem** (5 connections)
- **_CatalogRequestStub** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_format_catalog_output_next_page_hint()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_format_catalog_output_player()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_admin_from_user_flags()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_falls_back_to_flags_when_the_lookup_fails()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **ItemCatalogResponse** (4 connections)
- **ItemCatalogService** (4 connections)
- **_CatalogContainerStub** (3 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_persistence_returning()** (3 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- *... and 19 more nodes in this community*

## Relationships

- [Community 533](Community_533.md) (14 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 289](Community_289.md) (2 shared connections)
- [Community 42](Community_42.md) (1 shared connections)
- [Community 441](Community_441.md) (1 shared connections)
- [Community 751](Community_751.md) (1 shared connections)
- [Channel Commands](Channel_Commands.md) (1 shared connections)

## Source Files

- `server/commands/catalog_commands.py`
- `server/tests/unit/commands/test_catalog_commands.py`

## Audit Trail

- EXTRACTED: 112 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*