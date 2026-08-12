# inventory_equip_command.py

> 42 nodes

## Key Concepts

- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **inventory_command_prototype.py** (12 connections) — `server/commands/inventory_command_prototype.py`
- **handle_equip_command()** (11 connections) — `server/commands/inventory_equip_command.py`
- **infer_equip_slot_from_prototype()** (9 connections) — `server/commands/inventory_command_prototype.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **normalize_inventory_slots()** (8 connections) — `server/commands/equipment_helpers.py`
- **_equip_run_mutation()** (8 connections) — `server/commands/inventory_equip_command.py`
- **handle_wearable_container_on_equip()** (7 connections) — `server/commands/equipment_helpers.py`
- **_equip_success_payload()** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **EquipCommandWork** (6 connections) — `server/commands/inventory_equip_command.py`
- **find_equipped_item_after_equip()** (6 connections) — `server/commands/equipment_helpers.py`
- **_equip_persist_or_rollback()** (5 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandInventoryStep** (4 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandRuntime** (4 connections) — `server/commands/inventory_equip_command.py`
- **prototype_from_registry()** (4 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_registry_from_request()** (4 connections) — `server/commands/inventory_command_prototype.py`
- **_equip_inventory_rollback_snapshot()** (4 connections) — `server/commands/inventory_equip_command.py`
- **_equip_target_slot_or_error()** (4 connections) — `server/commands/inventory_equip_command.py`
- **_equip_try_inventory_swap()** (4 connections) — `server/commands/inventory_equip_command.py`
- **InventoryStack** (4 connections)
- **_find_equipped_by_item_id()** (3 connections) — `server/commands/equipment_helpers.py`
- **_first_normalized_wear_slot()** (3 connections) — `server/commands/inventory_command_prototype.py`
- **.__init__()** (3 connections) — `server/commands/inventory_equip_command.py`
- *... and 17 more nodes in this community*

## Relationships

- [test_inventory_helpers.py](test_inventory_helpers.py.md) (17 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (15 shared connections)
- [inventory_commands.py](inventory_commands.py.md) (6 shared connections)
- [persist_player](persist_player.md) (6 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_prototype.py`
- `server/commands/inventory_equip_command.py`

## Audit Trail

- EXTRACTED: 211 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*