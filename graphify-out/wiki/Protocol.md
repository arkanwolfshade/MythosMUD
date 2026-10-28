# Protocol

> 19 nodes · cohesion 0.27

## Key Concepts

- **handle_unequip_command()** (20 connections) — `server/commands/inventory_unequip_command.py`
- **test_inventory_unequip_command.py** (13 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_run_mutation()** (9 connections) — `server/commands/inventory_unequip_command.py`
- **_unequip_success_payload()** (7 connections) — `server/commands/inventory_unequip_command.py`
- **test_handle_unequip_command_emits_inventory_updated()** (7 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_slot_validation_error()** (7 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_mutation_cm()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_player_with_equipped()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_request_wiring()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_mutation_suppressed()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_persist_rollback()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_success()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **asyncio** (5 connections)
- **CommandResponse** (4 connections)
- **Player** (3 connections)
- **Unequip an item into the player's inventory.** (1 connections) — `server/commands/inventory_unequip_command.py`
- **Unit tests for inventory_unequip_command module.** (1 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **A successful unequip pushes inventory_updated so a GUI inventory panel stays in…** (1 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (10 shared connections)
- [TargetMatch](TargetMatch.md) (8 shared connections)
- [test_command_alias.py](test_command_alias.py.md) (3 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (1 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (1 shared connections)

## Source Files

- `server/commands/inventory_unequip_command.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`

## Audit Trail

- EXTRACTED: 69 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*