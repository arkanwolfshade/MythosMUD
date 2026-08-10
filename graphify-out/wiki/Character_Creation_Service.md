# Character Creation Service

> 59 nodes

## Key Concepts

- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **inventory_command_prototype.py** (12 connections) — `server/commands/inventory_command_prototype.py`
- **handle_equip_command()** (12 connections) — `server/commands/inventory_equip_command.py`
- **_unequip_run_mutation()** (12 connections) — `server/commands/inventory_unequip_command.py`
- **infer_equip_slot_from_prototype()** (9 connections) — `server/commands/inventory_command_prototype.py`
- **normalize_inventory_slots()** (8 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **_equip_run_mutation()** (8 connections) — `server/commands/inventory_equip_command.py`
- **resolve_equip_item_index()** (7 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_equip()** (7 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **EquipCommandWork** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **_equip_try_inventory_swap()** (7 connections) — `server/commands/inventory_equip_command.py`
- **_equip_success_payload()** (7 connections) — `server/commands/inventory_equip_command.py`
- **find_equipped_item_after_equip()** (6 connections) — `server/commands/equipment_helpers.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_persist_or_rollback()** (5 connections) — `server/commands/inventory_equip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_stack_from_inventory_index()** (4 connections) — `server/commands/equipment_helpers.py`
- **InventoryStack** (4 connections)
- *... and 34 more nodes in this community*

## Relationships

- [Async Task Registry](Async_Task_Registry.md) (25 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (15 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (15 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (10 shared connections)
- [Game Client Container](Game_Client_Container.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (4 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (4 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (2 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_prototype.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`

## Audit Trail

- EXTRACTED: 324 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*