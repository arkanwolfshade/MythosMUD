# test_nats_message_handler_subzone_events.py

> 30 nodes · cohesion 0.17

## Key Concepts

- **inventory_put_command.py** (26 connections) — `server/commands/inventory_put_command.py`
- **test_inventory_put_command.py** (24 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **handle_put_command()** (17 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (15 connections) — `server/commands/inventory_put_command.py`
- **_put_resolve_container_id()** (14 connections) — `server/commands/inventory_put_command.py`
- **asyncio** (12 connections)
- **_put_run_validated()** (10 connections) — `server/commands/inventory_put_command.py`
- **PutCommandRuntime** (7 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (7 connections) — `server/commands/inventory_put_command.py`
- **test_put_run_validated_container_error()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_run_validated_success()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_handle_put_command_success()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_handle_put_command_validation_error()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_resolve_container_missing_id()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_resolve_container_not_found()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_transfer_finish_error()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_transfer_finish_not_success()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_transfer_finish_persist_error()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_transfer_finish_success()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **CommandResponse** (4 connections)
- **test_handle_put_command_no_player()** (4 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_resolve_container_id_room_container()** (4 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **UUID** (3 connections)
- **Player** (2 connections)
- **Put command: move inventory items into a container.** (1 connections) — `server/commands/inventory_put_command.py`
- *... and 5 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (14 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (13 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (13 shared connections)
- [command_parser.py](command_parser.py.md) (8 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (4 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [SuccessLevel](SuccessLevel.md) (2 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_put_command.py`

## Audit Trail

- EXTRACTED: 112 (84%)
- INFERRED: 22 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*