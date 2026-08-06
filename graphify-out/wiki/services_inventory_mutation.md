# services inventory mutation

> 185 nodes

## Key Concepts

- **LoggedHTTPException** (474 connections) — `server/exceptions.py`
- **ContainerServiceError** (68 connections) — `server/services/container_service_helpers.py`
- **container_service.py** (33 connections) — `server/services/container_service.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **ContainerNotFoundError** (31 connections) — `server/services/container_service_helpers.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (26 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **player_respawn.py** (25 connections) — `server/api/player_respawn.py`
- **ContainerCapacityError** (23 connections) — `server/services/container_service_helpers.py`
- **handle_close_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (19 connections) — `server/api/container_exception_handlers.py`
- **ContainerLockedError** (18 connections) — `server/services/container_service_helpers.py`
- **test_player_respawn_api.py** (17 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **TestHandleTransferItemsExceptions** (13 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **TestHandleOpenContainerExceptions** (11 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleLootAllExceptions** (11 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **TestHandleCloseContainerExceptions** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleTransferItemsExceptionsEdgeCases** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 160 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (118 shared connections)
- [task registry app](task_registry_app.md) (66 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (62 shared connections)
- [player requests schemas](player_requests_schemas.md) (58 shared connections)
- [Player Stats](Player_Stats.md) (35 shared connections)
- [add used user](add_used_user.md) (28 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (28 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (22 shared connections)
- [alias storage commands](alias_storage_commands.md) (21 shared connections)
- [Loot Generation](Loot_Generation.md) (19 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (16 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (14 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/maps.py`
- `server/api/player_respawn.py`
- `server/exceptions.py`
- `server/schemas/players/player_respawn.py`
- `server/services/container_service.py`
- `server/services/container_service_helpers.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 933 (65%)
- INFERRED: 510 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*