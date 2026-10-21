# deprecated_patterns.py

> 39 nodes · cohesion 0.12

## Key Concepts

- **test_bank_commands.py** (28 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **handle_deposit_command()** (18 connections) — `server/commands/bank_commands.py`
- **handle_withdraw_command()** (17 connections) — `server/commands/bank_commands.py`
- **_bank_world()** (14 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **handle_bank_command()** (13 connections) — `server/commands/bank_commands.py`
- **_run()** (13 connections) — `server/tests/unit/commands/test_bank_commands.py`
- **_enter_bank()** (12 connections) — `server/commands/bank_commands.py`
- **asyncio** (10 connections)
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
- **_BankVisit** (4 connections) — `server/commands/bank_commands.py`
- **CommandResponse** (4 connections)
- **.box_id()** (3 connections) — `server/commands/bank_commands.py`
- **_display_name()** (3 connections) — `server/commands/bank_commands.py`
- **_coin()** (3 connections) — `server/tests/unit/commands/test_bank_commands.py`
- *... and 14 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (13 shared connections)
- [TargetMatch](TargetMatch.md) (11 shared connections)
- [command_parser.py](command_parser.py.md) (9 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (7 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (3 shared connections)
- [✅ Phase 2 Async Persistence Migration - COMPLETE](✅_Phase_2_Async_Persistence_Migration_-_COMPLETE.md) (2 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (2 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (2 shared connections)
- [GameClientV2.tsx](GameClientV2.tsx.md) (2 shared connections)
- [_RecordingRoom](_RecordingRoom.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/commands/bank_commands.py`
- `server/tests/unit/commands/test_bank_commands.py`

## Audit Trail

- EXTRACTED: 126 (85%)
- INFERRED: 23 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*