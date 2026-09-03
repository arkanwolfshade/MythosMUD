# Test Rest Command

> 106 nodes

## Key Concepts

- **test_rest_command.py** (42 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (30 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (25 connections) — `server/commands/rest_command.py`
- **asyncio** (23 connections)
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **MockPersistence** (20 connections) — `server/tests/unit/commands/test_rest_command.py`
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (13 connections) — `server/commands/rest_command.py`
- **Any** (13 connections)
- **check_player_in_combat()** (11 connections) — `server/commands/rest_command.py`
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (11 connections)
- **_begin_seated_rest_countdown()** (10 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (7 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (7 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (7 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **rest_countdown_seconds()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_delayed_disconnect_player_intentionally()** (5 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (5 connections) — `server/commands/rest_command.py`
- **test_check_rest_location_false()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_room()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_true()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_disconnect_player_intentionally()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 81 more nodes in this community*

## Relationships

- [Test Rest And Grace Period](Test_Rest_And_Grace_Period.md) (9 shared connections)
- [Test Go Command](Test_Go_Command.md) (5 shared connections)
- [Test Magic Commands](Test_Magic_Commands.md) (5 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Rest Countdown Task](Rest_Countdown_Task.md) (5 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (4 shared connections)
- [Posture Notify](Posture_Notify.md) (4 shared connections)
- [Test Player Presence Tracker](Test_Player_Presence_Tracker.md) (4 shared connections)
- [Test Combat Service Modules](Test_Combat_Service_Modules.md) (4 shared connections)
- [Test Logout Commands](Test_Logout_Commands.md) (4 shared connections)
- [Combat Handler](Combat_Handler.md) (2 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/commands/rest_countdown_task.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 273 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*