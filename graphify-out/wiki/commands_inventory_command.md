# commands inventory command

> 248 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_helpers.py** (38 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_inventory_equip_command.py** (36 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **equipment_helpers.py** (29 connections) — `server/commands/equipment_helpers.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **test_equipment_helpers.py** (25 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **inventory_put_command.py** (22 connections) — `server/commands/inventory_put_command.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **handle_equip_command()** (16 connections) — `server/commands/inventory_equip_command.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **resolve_unequip_slot()** (14 connections) — `server/commands/equipment_helpers.py`
- **resolve_equip_item_index()** (13 connections) — `server/commands/equipment_helpers.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- *... and 223 more nodes in this community*

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (40 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (29 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (29 shared connections)
- [inventory commands command](inventory_commands_command.md) (27 shared connections)
- [combat models rationale](combat_models_rationale.md) (18 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [Exception Containers](Exception_Containers.md) (8 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (8 shared connections)
- [logging file setup](logging_file_setup.md) (6 shared connections)
- [stats game generator](stats_game_generator.md) (6 shared connections)
- [commands whisper command](commands_whisper_command.md) (5 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_equipment_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 1165 (98%)
- INFERRED: 18 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*