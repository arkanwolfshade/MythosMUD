# database helpers infrastructure

> 97 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_get_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **_handle_get_from_room()** (17 connections) — `server/commands/inventory_get_command.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **GetCommandRuntime** (12 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (12 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- *... and 72 more nodes in this community*

## Relationships

- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (32 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (26 shared connections)
- [task registry app](task_registry_app.md) (14 shared connections)
- [game weapon player](game_weapon_player.md) (14 shared connections)
- [player room realtime](player_room_realtime.md) (12 shared connections)
- [commands npc admin](commands_npc_admin.md) (11 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (5 shared connections)
- [player cache rationale](player_cache_rationale.md) (4 shared connections)
- [game rationale schemas](game_rationale_schemas.md) (4 shared connections)
- [models profession rationale](models_profession_rationale.md) (3 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 524 (89%)
- INFERRED: 65 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*