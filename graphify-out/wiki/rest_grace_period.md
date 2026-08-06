# rest grace period

> 129 nodes

## Key Concepts

- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **handle_rest_command()** (21 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (19 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (11 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **MockPersistence** (7 connections) — `server/tests/unit/commands/test_rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **test_unintentional_disconnect_starts_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_intentional_disconnect_no_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 104 more nodes in this community*

## Relationships

- [alias storage rationale](alias_storage_rationale.md) (9 shared connections)
- [npc combat base](npc_combat_base.md) (7 shared connections)
- [commands command rationale](commands_command_rationale.md) (5 shared connections)
- [subject admin controller](subject_admin_controller.md) (5 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (3 shared connections)
- [instance game manager](instance_game_manager.md) (3 shared connections)
- [movement monitor game](movement_monitor_game.md) (3 shared connections)
- [realtime real time](realtime_real_time.md) (2 shared connections)
- [position player service](position_player_service.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [invite models rationale](invite_models_rationale.md) (2 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 453 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*