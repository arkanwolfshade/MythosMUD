# Loot Generation

> 209 nodes

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestHandleContainerServiceErrorEdgeCases** (15 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **container_models.py** (12 connections) — `server/api/container_models.py`
- **validate_user_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **register_loot_endpoints()** (8 connections) — `server/api/container_endpoints_loot.py`
- **Any** (6 connections)
- **UUID** (6 connections)
- **.test_loot_all_items_container_not_found()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- *... and 184 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (77 shared connections)
- [container events rationale](container_events_rationale.md) (58 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (48 shared connections)
- [alias storage commands](alias_storage_commands.md) (20 shared connections)
- [task registry app](task_registry_app.md) (18 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (12 shared connections)
- [command inventory factories](command_inventory_factories.md) (8 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (6 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (4 shared connections)
- [logging file setup](logging_file_setup.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 894 (90%)
- INFERRED: 103 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*