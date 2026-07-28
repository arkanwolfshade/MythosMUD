# Commands Rest Countdown

> 110 nodes · cohesion 0.03

## Key Concepts

- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (17 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **Any** (11 connections)
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **MockPersistence** (7 connections) — `server/tests/unit/commands/test_rest_command.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **UUID** (6 connections)
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- *... and 85 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (15 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (9 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (5 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (4 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (4 shared connections)
- [Loot All Endpoint](Loot_All_Endpoint.md) (2 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/commands/rest_command.py`
- `server/commands/rest_countdown_task.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 409 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*