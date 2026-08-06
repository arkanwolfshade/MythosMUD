# monitoring endpoints rationale

> 325 nodes

## Key Concepts

- **alias_storage.py** (75 connections) — `server/alias_storage.py`
- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **command_result_text()** (41 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **admin_summon_command.py** (35 connections) — `server/commands/admin_summon_command.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_unequip_command.py** (33 connections) — `server/commands/inventory_unequip_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_get_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_inventory_put_command.py** (24 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **inventory_put_command.py** (22 connections) — `server/commands/inventory_put_command.py`
- **InventorySchemaValidationError** (20 connections) — `server/schemas/shared/inventory_schema.py`
- **test_inventory_commands.py** (20 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **PickupTestWiring** (19 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **_handle_get_from_room()** (17 connections) — `server/commands/inventory_get_command.py`
- *... and 300 more nodes in this community*

## Relationships

- [player cache rationale](player_cache_rationale.md) (54 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (29 shared connections)
- [Error Conversion](Error_Conversion.md) (19 shared connections)
- [player room realtime](player_room_realtime.md) (18 shared connections)
- [task registry app](task_registry_app.md) (17 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (16 shared connections)
- [realtime real time](realtime_real_time.md) (15 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (10 shared connections)
- [command parser helpers](command_parser_helpers.md) (8 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [commands npc admin](commands_npc_admin.md) (6 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (5 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/admin_summon_command.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_put_command.py`
- `server/commands/inventory_unequip_command.py`
- `server/models/alias.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_get_command.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 1579 (93%)
- INFERRED: 114 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*