# Any

> 31 nodes

## Key Concepts

- **SlotValidationError** (21 connections) — `server/services/equipment_service.py`
- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **test_inventory_unequip_command.py** (13 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_run_mutation()** (9 connections) — `server/commands/inventory_unequip_command.py`
- **test_handle_unequip_command_slot_validation_error()** (7 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **test_handle_unequip_command_mutation_suppressed()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_persist_rollback()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_success()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **_mutation_cm()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_player_with_equipped()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_request_wiring()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **CommandResponse** (4 connections)
- **asyncio** (4 connections)
- **test_equip_from_inventory_invalid_slot_index()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_no_slot_type()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_slot_mismatch()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_slot_type_inventory_requires_target_slot()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_empty_slot()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_no_slot_type()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **Player** (3 connections)
- **Unequip an item into the player's inventory.** (1 connections) — `server/commands/inventory_unequip_command.py`
- **Raised when requested slots or inventory positions are invalid.** (1 connections) — `server/services/equipment_service.py`
- **Unit tests for inventory_unequip_command module.** (1 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- *... and 6 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (28 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (5 shared connections)
- [.__init__](__init__.md) (2 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (2 shared connections)
- [GameLogPanel.tsx](GameLogPanel.tsx.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)

## Source Files

- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 85 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*