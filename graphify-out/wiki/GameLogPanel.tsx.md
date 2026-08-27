# GameLogPanel.tsx

> 64 nodes

## Key Concepts

- **command_result_text()** (41 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_put_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **inventory_put_command.py** (22 connections) — `server/commands/inventory_put_command.py`
- **test_inventory_commands.py** (21 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **handle_put_command()** (16 connections) — `server/commands/inventory_put_command.py`
- **asyncio** (14 connections)
- **_put_resolve_container_id()** (13 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (13 connections) — `server/commands/inventory_put_command.py`
- **asyncio** (12 connections)
- **_put_run_validated()** (10 connections) — `server/commands/inventory_put_command.py`
- **PutCommandRuntime** (7 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (7 connections) — `server/commands/inventory_put_command.py`
- **test_put_run_validated_container_error()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_run_validated_success()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_handle_drop_command_broadcasts_room_event_after_persist()** (6 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **remove_item_from_inventory()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **test_handle_drop_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_equip_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_get_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_inventory_command_no_persistence()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_put_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_unequip_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_put_command_success()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_handle_put_command_validation_error()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_resolve_container_missing_id()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- *... and 39 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (26 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (12 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (12 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (5 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (5 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (3 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_put_command.py`

## Audit Trail

- EXTRACTED: 186 (85%)
- INFERRED: 33 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*