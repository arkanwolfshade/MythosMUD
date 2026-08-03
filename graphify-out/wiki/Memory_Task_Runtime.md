# Memory Task Runtime

> 162 nodes

## Key Concepts

- **RateLimitError** (76 connections) — `server/exceptions.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **TestTransferItems** (20 connections) — `server/tests/unit/api/test_containers.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **TestHandleContainerServiceError** (13 connections) — `server/tests/unit/api/test_container_helpers.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **execute_transfer()** (12 connections) — `server/api/container_helpers.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestCreateErrorContext** (12 connections) — `server/tests/unit/api/test_container_helpers.py`
- **_convert_inventory_list_to_inventory_stacks()** (11 connections) — `server/api/container_endpoints_basic.py`
- **Request** (11 connections)
- **TestGetPlayerIdFromUser** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForOpenContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForOpenContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestExecuteTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForCloseContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForCloseContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForLootAll** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForLootAll** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **validate_user_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- *... and 137 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (97 shared connections)
- [Loot Generation](Loot_Generation.md) (48 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (46 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (25 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (20 shared connections)
- [alias storage commands](alias_storage_commands.md) (19 shared connections)
- [container events rationale](container_events_rationale.md) (18 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [command handler unified](command_handler_unified.md) (5 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [profession game service](profession_game_service.md) (3 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 648 (77%)
- INFERRED: 198 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*