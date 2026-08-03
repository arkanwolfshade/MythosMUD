# rest grace period

> 131 nodes

## Key Concepts

- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (21 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (19 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **Any** (11 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **MockPersistence** (7 connections) — `server/tests/unit/commands/test_rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **UUID** (6 connections)
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- *... and 106 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (18 shared connections)
- [look helpers commands](look_helpers_commands.md) (9 shared connections)
- [services combat sync](services_combat_sync.md) (9 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [commands command rationale](commands_command_rationale.md) (5 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [commands position system](commands_position_system.md) (3 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [position player service](position_player_service.md) (2 shared connections)
- [player event state](player_event_state.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/commands/rest_countdown_task.py`
- `server/services/combat_service_start.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/commands/test_rest_command.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 477 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*