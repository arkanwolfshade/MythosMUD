# combat_turn_participant_actions.py

> 72 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **inventory_command_contracts.py** (11 connections) — `server/commands/inventory_command_contracts.py`
- **Player** (11 connections)
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupAfterExtract** (8 connections) — `server/commands/inventory_pickup_command.py`
- **add_pickup_to_inventory()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupEnvironment** (7 connections) — `server/commands/inventory_pickup_command.py`
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (7 connections)
- **FloorPickupPayload** (6 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_finish_after_persist()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_pickup_broadcast_success()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **CommandResponse** (6 connections)
- *... and 47 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (44 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (14 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (7 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (6 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (6 shared connections)
- [ChatHistoryPanel.tsx](ChatHistoryPanel.tsx.md) (5 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (5 shared connections)
- [GameLogPanel.tsx](GameLogPanel.tsx.md) (5 shared connections)
- [CombatParticipant](CombatParticipant.md) (4 shared connections)
- [Any](Any.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`

## Audit Trail

- EXTRACTED: 215 (91%)
- INFERRED: 22 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*