# server commands equipment helpers normalize

> 47 nodes

## Key Concepts

- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_equip_command.py** (37 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **SlotValidationError** (21 connections) — `server/services/equipment_service.py`
- **handle_equip_command()** (15 connections) — `server/commands/inventory_equip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **_sample_work()** (13 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **_equip_run_mutation()** (12 connections) — `server/commands/inventory_equip_command.py`
- **normalize_inventory_slots()** (10 connections) — `server/commands/equipment_helpers.py`
- **asyncio** (10 connections)
- **_equip_success_payload()** (9 connections) — `server/commands/inventory_equip_command.py`
- **_equip_target_slot_or_error()** (9 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandWork** (8 connections) — `server/commands/inventory_equip_command.py`
- **_equip_persist_or_rollback()** (8 connections) — `server/commands/inventory_equip_command.py`
- **_equip_try_inventory_swap()** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **EquipCommandInventoryStep** (6 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandRuntime** (6 connections) — `server/commands/inventory_equip_command.py`
- **_equip_inventory_rollback_snapshot()** (6 connections) — `server/commands/inventory_equip_command.py`
- **test_equip_run_mutation_swap_error()** (6 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_handle_equip_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_equip_run_mutation_suppressed()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_success_payload()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_try_inventory_swap_rejected()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_handle_equip_command_invalid_selected_stack()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_handle_equip_command_mutation_error()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- *... and 22 more nodes in this community*

## Relationships

- [abstractcontextmanager](abstractcontextmanager.md) (22 shared connections)
- [dropresolved](dropresolved.md) (15 shared connections)
- [server commands inventory command helpers](server_commands_inventory_command_helpers.md) (15 shared connections)
- [server commands equipment helpers](server_commands_equipment_helpers.md) (12 shared connections)
- [server async persistence](server_async_persistence.md) (9 shared connections)
- [server commands inventory item matching](server_commands_inventory_item_matching.md) (4 shared connections)
- [server commands inventory command prototype](server_commands_inventory_command_prototype.md) (3 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [aliaspayload](aliaspayload.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`

## Audit Trail

- EXTRACTED: 195 (93%)
- INFERRED: 15 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*