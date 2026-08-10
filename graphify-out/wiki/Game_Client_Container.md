# Game Client Container

> 41 nodes

## Key Concepts

- **SlotValidationError** (22 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **equipment_service.py** (21 connections) — `server/services/equipment_service.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentServiceError** (10 connections) — `server/services/equipment_service.py`
- **_resolve_effective_equip_slot()** (4 connections) — `server/services/equipment_service.py`
- **equipment_service()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_invalid_slot_index()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_no_slot_type()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_slot_mismatch()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_slot_type_inventory_requires_target_slot()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_capacity_error()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_empty_slot()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_no_slot_type()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_capacity_error()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_success()** (2 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_slot_type_inventory_with_target_slot()** (2 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_quantity_split()** (2 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_swap_item()** (2 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_success()** (2 connections) — `server/tests/unit/services/test_equipment_service.py`
- **Exception** (1 connections)
- **Equipment service providing equip/unequip helpers built atop inventory logic.** (1 connections) — `server/services/equipment_service.py`
- **Base error for equipment service operations.** (1 connections) — `server/services/equipment_service.py`
- **Raised when requested slots or inventory positions are invalid.** (1 connections) — `server/services/equipment_service.py`
- **Raised when an equip/unequip operation would exceed inventory capacity.** (1 connections) — `server/services/equipment_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [Chat Service Whispers](Chat_Service_Whispers.md) (23 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (10 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (8 shared connections)
- [NATS Subject Patterns](NATS_Subject_Patterns.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Application Container Analysis](Application_Container_Analysis.md) (1 shared connections)

## Source Files

- `server/services/equipment_service.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 122 (79%)
- INFERRED: 32 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*