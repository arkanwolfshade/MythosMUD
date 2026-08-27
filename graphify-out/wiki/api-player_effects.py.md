# api/player_effects.py

> 32 nodes

## Key Concepts

- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (26 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **asyncio** (10 connections)
- **GetCommandRuntime** (8 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (8 connections) — `server/commands/inventory_get_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **test_get_from_container_path_item_not_in_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_from_container_path_missing_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_uses_pickup_wiring()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **CommandResponse** (5 connections)
- **_container_transfer_messages()** (4 connections) — `server/commands/inventory_get_command.py`
- **test_get_transfer_out_of_container_error()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_not_success()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_success()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_index_error()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_invalid_quantity()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_unresolved_index()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_container_transfer_messages()** (2 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **Player** (2 connections)
- **UUID** (2 connections)
- *... and 7 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (18 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (14 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (5 shared connections)
- [GameLogPanel.tsx](GameLogPanel.tsx.md) (5 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (3 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (2 shared connections)

## Source Files

- `server/commands/inventory_get_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 109 (81%)
- INFERRED: 25 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*