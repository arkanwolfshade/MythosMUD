# commands inventory pickup

> 89 nodes

## Key Concepts

- **command_result_text()** (41 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_put_command.py** (24 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_inventory_commands.py** (20 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **PickupTestWiring** (19 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_commands_pickup.py** (17 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **handle_put_command()** (16 connections) — `server/commands/inventory_put_command.py`
- **handle_inventory_command()** (13 connections) — `server/commands/inventory_commands.py`
- **_put_resolve_container_id()** (13 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (13 connections) — `server/commands/inventory_put_command.py`
- **_put_run_validated()** (10 connections) — `server/commands/inventory_put_command.py`
- **inventory_commands_test_support.py** (10 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **PutCommandRuntime** (7 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (7 connections) — `server/commands/inventory_put_command.py`
- **test_handle_pickup_command()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **sample_floor_item_stack()** (6 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_put_run_validated_container_error()** (6 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_run_validated_success()** (6 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **inventory_has_named_item()** (5 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_drop_command_broadcasts_room_event_after_persist()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_pickup_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_room_manager()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_invalid_index()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- *... and 64 more nodes in this community*

## Relationships

- [commands inventory command](commands_inventory_command.md) (29 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (14 shared connections)
- [combat models rationale](combat_models_rationale.md) (13 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (5 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [commands whisper command](commands_whisper_command.md) (2 shared connections)
- [container inventory display](container_inventory_display.md) (2 shared connections)
- [services admin auth](services_admin_auth.md) (2 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (1 shared connections)
- [logout command commands](logout_command_commands.md) (1 shared connections)
- [container find inventory](container_find_inventory.md) (1 shared connections)

## Source Files

- `server/commands/inventory_commands.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`
- `server/tests/unit/commands/test_inventory_get_command.py`
- `server/tests/unit/commands/test_inventory_put_command.py`

## Audit Trail

- EXTRACTED: 376 (91%)
- INFERRED: 37 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*