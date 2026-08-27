# game_tick_status_effects.py

> 44 nodes

## Key Concepts

- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_equip_command.py** (37 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **handle_equip_command()** (15 connections) — `server/commands/inventory_equip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **_sample_work()** (13 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **_equip_run_mutation()** (12 connections) — `server/commands/inventory_equip_command.py`
- **normalize_inventory_slots()** (10 connections) — `server/commands/equipment_helpers.py`
- **asyncio** (10 connections)
- **_equip_success_payload()** (9 connections) — `server/commands/inventory_equip_command.py`
- **_equip_target_slot_or_error()** (9 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandWork** (8 connections) — `server/commands/inventory_equip_command.py`
- **_equip_persist_or_rollback()** (8 connections) — `server/commands/inventory_equip_command.py`
- **_equip_try_inventory_swap()** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **EquipCommandInventoryStep** (6 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandRuntime** (6 connections) — `server/commands/inventory_equip_command.py`
- **_equip_inventory_rollback_snapshot()** (6 connections) — `server/commands/inventory_equip_command.py`
- **test_equip_run_mutation_swap_error()** (6 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_run_mutation_suppressed()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_success_payload()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_try_inventory_swap_rejected()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_handle_equip_command_invalid_selected_stack()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_handle_equip_command_mutation_error()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_handle_equip_command_success()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_persist_or_rollback_failure()** (4 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- *... and 19 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (31 shared connections)
- [GameLogPanel.tsx](GameLogPanel.tsx.md) (12 shared connections)
- [.__init__](__init__.md) (10 shared connections)
- [Any](Any.md) (5 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (5 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (4 shared connections)
- [command_input.py](command_input.py.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/tests/unit/commands/test_equipment_helpers.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`

## Audit Trail

- EXTRACTED: 182 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*