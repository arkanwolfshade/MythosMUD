# properties

> 41 nodes · cohesion 0.12

## Key Concepts

- **ItemCatalogService** (35 connections) — `server/game/item_catalog_service.py`
- **test_catalog_commands.py** (34 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **handle_catalog_command()** (15 connections) — `server/commands/catalog_commands.py`
- **resolve_is_admin()** (12 connections) — `server/commands/catalog_commands.py`
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
- **_as_catalog_request()** (4 connections) — `server/commands/catalog_commands.py`
- **_get_catalog_service()** (4 connections) — `server/commands/catalog_commands.py`
- **_CatalogContainerStub** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_CatalogRequestStub** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_handle_catalog_command_failure()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_falls_back_to_flags_when_the_lookup_fails()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_persistence_returning()** (3 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_resolve_is_admin_without_a_request_reads_only_the_user_flags()** (3 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- *... and 16 more nodes in this community*

## Relationships

- [send_system_message](send_system_message.md) (24 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (11 shared connections)
- [command_parser.py](command_parser.py.md) (4 shared connections)
- [test_game_state_provider_hallucination.py](test_game_state_provider_hallucination.py.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [._get_npc_display_name](_get_npc_display_name.md) (3 shared connections)
- [MessageBatcher](MessageBatcher.md) (1 shared connections)
- [FollowService](FollowService.md) (1 shared connections)
- [Communities (10 total, 2 thin omitted)](Communities_10_total,_2_thin_omitted.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)

## Source Files

- `server/commands/catalog_commands.py`
- `server/game/item_catalog_service.py`
- `server/tests/unit/commands/test_catalog_commands.py`

## Audit Trail

- EXTRACTED: 128 (86%)
- INFERRED: 21 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*