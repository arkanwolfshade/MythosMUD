# commands inventory command

> 125 nodes

## Key Concepts

- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_equip_command.py** (36 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **equipment_helpers.py** (29 connections) — `server/commands/equipment_helpers.py`
- **test_equipment_helpers.py** (25 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **handle_equip_command()** (16 connections) — `server/commands/inventory_equip_command.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **resolve_unequip_slot()** (14 connections) — `server/commands/equipment_helpers.py`
- **resolve_equip_item_index()** (13 connections) — `server/commands/equipment_helpers.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **_sample_work()** (13 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **_equip_run_mutation()** (12 connections) — `server/commands/inventory_equip_command.py`
- **normalize_inventory_slots()** (10 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (10 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_equip()** (10 connections) — `server/commands/equipment_helpers.py`
- **find_equipped_item_after_equip()** (9 connections) — `server/commands/equipment_helpers.py`
- **_equip_target_slot_or_error()** (9 connections) — `server/commands/inventory_equip_command.py`
- **_equip_success_payload()** (9 connections) — `server/commands/inventory_equip_command.py`
- **_equip_persist_or_rollback()** (8 connections) — `server/commands/inventory_equip_command.py`
- **_player()** (8 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **CommandResponse** (7 connections)
- *... and 100 more nodes in this community*

## Relationships

- [retry nats handler](retry_nats_handler.md) (37 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (26 shared connections)
- [inventory commands command](inventory_commands_command.md) (15 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (12 shared connections)
- [world models rationale](world_models_rationale.md) (11 shared connections)
- [stats game generator](stats_game_generator.md) (6 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [commands position system](commands_position_system.md) (1 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_equipment_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`

## Audit Trail

- EXTRACTED: 632 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*