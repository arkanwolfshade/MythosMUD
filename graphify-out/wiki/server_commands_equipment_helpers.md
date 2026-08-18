# server commands equipment helpers

> 40 nodes

## Key Concepts

- **equipment_helpers.py** (29 connections) — `server/commands/equipment_helpers.py`
- **test_equipment_helpers.py** (26 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **resolve_unequip_slot()** (14 connections) — `server/commands/equipment_helpers.py`
- **resolve_equip_item_index()** (13 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_equip()** (10 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (10 connections) — `server/commands/equipment_helpers.py`
- **find_equipped_item_after_equip()** (9 connections) — `server/commands/equipment_helpers.py`
- **_player()** (8 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **_equip_stack_from_inventory_index()** (4 connections) — `server/commands/equipment_helpers.py`
- **test_handle_wearable_container_on_equip_creates()** (4 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_handle_wearable_container_on_equip_no_inner()** (4 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **InventoryStack** (4 connections)
- **_find_equipped_by_item_id()** (3 connections) — `server/commands/equipment_helpers.py`
- **_try_resolve_unequip_by_search()** (3 connections) — `server/commands/equipment_helpers.py`
- **test_resolve_equip_by_index()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_by_search_term()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_index_out_of_range()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_search_no_match()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_usage()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **Player** (3 connections)
- **_try_resolve_unequip_slot_key()** (2 connections) — `server/commands/equipment_helpers.py`
- **_unequip_usage_missing_slot()** (2 connections) — `server/commands/equipment_helpers.py`
- **test_find_equipped_item_after_equip_by_item_id()** (2 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_find_equipped_item_after_equip_preferred_slot()** (2 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_normalize_equipped_items()** (2 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- *... and 15 more nodes in this community*

## Relationships

- [server commands equipment helpers normalize](server_commands_equipment_helpers_normalize.md) (12 shared connections)
- [server commands inventory item matching](server_commands_inventory_item_matching.md) (9 shared connections)
- [dropresolved](dropresolved.md) (8 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (3 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [server async persistence](server_async_persistence.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/tests/unit/commands/test_equipment_helpers.py`

## Audit Trail

- EXTRACTED: 115 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*