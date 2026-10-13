# Community 414

> 42 nodes

## Key Concepts

- **test_bank_commands.py** (28 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **handle_deposit_command()** (16 connections) — `server/commands/bank_commands.py`
- **handle_withdraw_command()** (16 connections) — `server/commands/bank_commands.py`
- **_bank_world()** (14 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **handle_bank_command()** (13 connections) — `server/commands/bank_commands.py`
- **_run()** (13 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **asyncio** (10 connections)
- **_enter_bank()** (9 connections) — `server/commands/bank_commands.py`
- **test_bank_lists_numbered_stacks_with_the_slot_count()** (8 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_withdraw_takes_the_named_stack_out_of_the_players_box()** (8 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **_lamp()** (7 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_bank_shows_an_over_filled_box_honestly()** (7 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_deposit_into_a_full_box_leaves_the_inventory_alone()** (7 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_deposit_moves_the_item_into_the_players_own_box()** (7 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_every_bank_command_refuses_outside_a_bank()** (7 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_withdraw_of_something_not_in_the_box_says_so_and_moves_nothing()** (7 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_withdraw_surfaces_a_transfer_error()** (7 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_bank_reports_an_empty_box()** (6 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **test_deposit_of_an_item_the_player_lacks_is_reported_by_the_validator()** (6 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **Bank** (5 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **.remove_item_from_inventory()** (5 connections) — `server/npc/npc_base.py`
- **_BankVisit** (4 connections) — `server/commands/bank_commands.py`
- **CommandResponse** (4 connections)
- **.box_id()** (3 connections) — `server/commands/bank_commands.py`
- **_display_name()** (3 connections) — `server/commands/bank_commands.py`
- *... and 17 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (19 shared connections)
- [Community 239](Community_239.md) (13 shared connections)
- [Community 78](Community_78.md) (7 shared connections)
- [Community 42](Community_42.md) (3 shared connections)
- [Community 179](Community_179.md) (3 shared connections)
- [Community 443](Community_443.md) (2 shared connections)
- [Community 332](Community_332.md) (2 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (1 shared connections)
- [Community 341](Community_341.md) (1 shared connections)

## Source Files

- `server/commands/bank_commands.py`
- `server/npc/npc_base.py`
- `server/tests/unit/commands/test_bank_commands.py`

## Audit Trail

- EXTRACTED: 122 (83%)
- INFERRED: 25 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*