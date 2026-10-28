# test_command_alias.py

> 40 nodes · cohesion 0.09

## Key Concepts

- **equipment_helpers.py** (32 connections) — `server/commands/equipment_helpers.py`
- **test_equipment_helpers.py** (27 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **resolve_equip_item_index()** (16 connections) — `server/commands/equipment_helpers.py`
- **resolve_unequip_slot()** (15 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (10 connections) — `server/commands/equipment_helpers.py`
- **find_equipped_item_after_equip()** (9 connections) — `server/commands/equipment_helpers.py`
- **_player()** (8 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **_equip_stack_from_inventory_index()** (4 connections) — `server/commands/equipment_helpers.py`
- **InventoryStack** (4 connections)
- **test_handle_wearable_container_on_equip_creates()** (4 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_handle_wearable_container_on_equip_no_inner()** (4 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_usage()** (4 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **_find_equipped_by_item_id()** (3 connections) — `server/commands/equipment_helpers.py`
- **Player** (3 connections)
- **_try_resolve_unequip_by_search()** (3 connections) — `server/commands/equipment_helpers.py`
- **test_resolve_equip_by_index()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_by_search_term()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_index_out_of_range()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_search_no_match()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_unequip_usage()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **_try_resolve_unequip_slot_key()** (2 connections) — `server/commands/equipment_helpers.py`
- **_unequip_usage_missing_slot()** (2 connections) — `server/commands/equipment_helpers.py`
- **asyncio** (2 connections)
- **test_find_equipped_item_after_equip_by_item_id()** (2 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- *... and 15 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (19 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (10 shared connections)
- [TargetType](TargetType.md) (9 shared connections)
- [command_parser.py](command_parser.py.md) (4 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [Protocol](Protocol.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (1 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (1 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/tests/unit/commands/test_equipment_helpers.py`

## Audit Trail

- EXTRACTED: 124 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*