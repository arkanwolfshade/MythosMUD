# test_communication_commands_flows.py

> 134 nodes · cohesion 0.02

## Key Concepts

- **test_command_inventory.py** (65 connections) — `server/tests/unit/models/test_command_inventory.py`
- **EquipCommand** (23 connections) — `server/models/command_inventory.py`
- **PickupCommand** (22 connections) — `server/models/command_inventory.py`
- **UnequipCommand** (22 connections) — `server/models/command_inventory.py`
- **command_inventory.py** (18 connections) — `server/models/command_inventory.py`
- **DropCommand** (12 connections) — `server/models/command_inventory.py`
- **GetCommand** (12 connections) — `server/models/command_inventory.py`
- **PutCommand** (12 connections) — `server/models/command_inventory.py`
- **InventoryCommand** (8 connections) — `server/models/command_inventory.py`
- **ReadCommand** (8 connections) — `server/models/command_inventory.py`
- **field_validator** (6 connections)
- **.validate_slot()** (4 connections) — `server/models/command_inventory.py`
- **.validate_search_term()** (3 connections) — `server/models/command_inventory.py`
- **.validate_search_term()** (3 connections) — `server/models/command_inventory.py`
- **.validate_search_term()** (3 connections) — `server/models/command_inventory.py`
- **.validate_slot()** (3 connections) — `server/models/command_inventory.py`
- **.validate_search_term()** (3 connections) — `server/models/command_inventory.py`
- **test_drop_command_index_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_missing_index()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_quantity_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_with_quantity()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_index_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_search_term_max_length()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_target_slot_max_length()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- *... and 109 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (30 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (4 shared connections)
- [RoomBasedChannelStrategy](RoomBasedChannelStrategy.md) (2 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 245 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*