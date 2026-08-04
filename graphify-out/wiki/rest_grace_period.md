# rest grace period

> 87 nodes

## Key Concepts

- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (21 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (19 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (11 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **test_rest_interrupts_combat_action()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_handle_rest_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_in_combat()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rest_location_instant()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_starts_countdown()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 62 more nodes in this community*

## Relationships

- [player disconnect handlers](player_disconnect_handlers.md) (9 shared connections)
- [commands command rationale](commands_command_rationale.md) (5 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [commands party examples](commands_party_examples.md) (4 shared connections)
- [instance game manager](instance_game_manager.md) (3 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [position player service](position_player_service.md) (2 shared connections)
- [connection establishment realtime](connection_establishment_realtime.md) (2 shared connections)
- [combat helpers commands](combat_helpers_commands.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 336 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*