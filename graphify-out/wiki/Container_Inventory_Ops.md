# Container Inventory Ops

> 87 nodes

## Key Concepts

- **test_container_helpers_inventory_ops.py** (52 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **container_helpers_inventory.py** (31 connections) — `server/commands/container_helpers_inventory.py`
- **container_helpers_inventory_ops.py** (29 connections) — `server/commands/container_helpers_inventory_ops.py`
- **transfer_item_to_container()** (20 connections) — `server/commands/container_helpers_inventory_ops.py`
- **transfer_item_from_container()** (18 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_player_with_inventory()** (17 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **UUID** (12 connections)
- **validate_put_command_inputs()** (12 connections) — `server/commands/container_helpers_inventory_ops.py`
- **parse_container_items()** (11 connections) — `server/commands/container_helpers_inventory_ops.py`
- **extract_items_from_container()** (10 connections) — `server/commands/container_helpers_inventory_ops.py`
- **parse_json_string_items()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **resolve_container_id()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_coerce_transfer_quantity()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_int_transfer_qty()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **Player** (8 connections)
- **filter_valid_items()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **find_item_in_container()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **validate_get_command_inputs()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ensure_mutation_token()** (6 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ContainerSvcTokenOnly** (6 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **update_equipped_with_container_info()** (4 connections) — `server/commands/container_helpers_inventory_display.py`
- **_app_state_container_service()** (4 connections) — `server/commands/container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_no_transfer_to_method()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_no_transfer_from()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_inventory_rows_fallback_non_dict_result()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- *... and 62 more nodes in this community*

## Relationships

- [Container Inventory Finders](Container_Inventory_Finders.md) (15 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (7 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (4 shared connections)
- [AnyIO vs Asyncio Guide](AnyIO_vs_Asyncio_Guide.md) (4 shared connections)
- [Player Effects API](Player_Effects_API.md) (3 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (2 shared connections)
- [NATS Connection State Machine](NATS_Connection_State_Machine.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory.py`
- `server/commands/container_helpers_inventory_display.py`
- `server/commands/container_helpers_inventory_ops.py`
- `server/tests/unit/commands/test_container_helpers_inventory_ops.py`

## Audit Trail

- EXTRACTED: 417 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*