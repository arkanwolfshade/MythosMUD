# test_websocket_helpers.py

> 199 nodes · cohesion 0.02

## Key Concepts

- **models/player.py** (122 connections) — `server/models/player.py`
- **inventory_command_helpers.py** (54 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (39 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_unequip_command.py** (37 connections) — `server/commands/inventory_unequip_command.py`
- **persist_player()** (34 connections) — `server/commands/inventory_command_helpers.py`
- **container_service_transfer_to.py** (34 connections) — `server/services/container_service_transfer_to.py`
- **inventory_service.py** (34 connections) — `server/services/inventory_service.py`
- **bank_commands.py** (33 connections) — `server/commands/bank_commands.py`
- **inventory_use_command.py** (33 connections) — `server/commands/inventory_use_command.py`
- **inventory_commands.py** (32 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (29 connections) — `server/commands/inventory_drop_command.py`
- **container_service_transfer_from.py** (28 connections) — `server/services/container_service_transfer_from.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **resolve_state_and_player()** (23 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **clone_inventory()** (20 connections) — `server/commands/inventory_command_helpers.py`
- **InventoryCapacityError** (20 connections) — `server/services/inventory_service.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_websocket_events.py** (18 connections) — `server/services/inventory_websocket_events.py`
- **handle_drop_command()** (17 connections) — `server/commands/inventory_drop_command.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **asyncio** (15 connections)
- **inventory_command_contracts.py** (14 connections) — `server/commands/inventory_command_contracts.py`
- *... and 174 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (40 shared connections)
- [TargetMatch](TargetMatch.md) (37 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (29 shared connections)
- [Room](Room.md) (28 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (26 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (23 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (17 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (13 shared connections)
- [deprecated_patterns.py](deprecated_patterns.py.md) (13 shared connections)
- [FollowService](FollowService.md) (13 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (13 shared connections)
- [Protocol](Protocol.md) (10 shared connections)

## Source Files

- `server/commands/bank_commands.py`
- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_unequip_command.py`
- `server/commands/inventory_use_command.py`
- `server/models/player.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/services/inventory_service.py`
- `server/services/inventory_websocket_events.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 843 (96%)
- INFERRED: 32 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*