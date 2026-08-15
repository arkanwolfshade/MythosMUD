# handle_unequip_command

> 17 nodes

## Key Concepts

- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **test_inventory_unequip_command.py** (12 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
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
- **Player** (3 connections)
- **Unequip an item into the player's inventory.** (1 connections) — `server/commands/inventory_unequip_command.py`
- **Unit tests for inventory_unequip_command module.** (1 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`

## Relationships

- [server/services/__init__.py](server-services-__init__.py.md) (11 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (4 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (3 shared connections)
- [command_result_text](command_result_text.md) (2 shared connections)
- [inventory_commands.py](inventory_commands.py.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_unequip_command.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`

## Audit Trail

- EXTRACTED: 60 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*