# models profession rationale

> 13 nodes

## Key Concepts

- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **test_inventory_unequip_command.py** (12 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_slot_validation_error()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_mutation_cm()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_player_with_equipped()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_request_wiring()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_success()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_mutation_suppressed()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_persist_rollback()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Unequip an item into the player's inventory.** (1 connections) — `server/commands/inventory_unequip_command.py`
- **Test handle_unequip_command() unequips item.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Unit tests for inventory_unequip_command module.** (1 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`

## Relationships

- [task registry app](task_registry_app.md) (9 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [player cache rationale](player_cache_rationale.md) (1 shared connections)

## Source Files

- `server/commands/inventory_unequip_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`

## Audit Trail

- EXTRACTED: 69 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*