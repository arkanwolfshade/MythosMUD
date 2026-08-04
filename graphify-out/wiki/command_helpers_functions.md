# command helpers functions

> 30 nodes

## Key Concepts

- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **test_handle_rescue_command()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_target()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_state()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_target()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_rescuer_not_found()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_not_found()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_different_rooms()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_rescuer_room()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_lucidity_record_not_found()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Delegate rescue handling to the RescueService for testable, real logic.** (1 connections) — `server/commands/rescue_commands.py`
- **Unit tests for rescue command handlers.  Tests the rescue command functionality.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_rescue_command() delegates to RescueService.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_rescue_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_rescue_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_rescue_command() accepts target_player key.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_rescue_command() handles missing app.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_rescue_command() handles missing app.state.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_ground_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_ground_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 5 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (17 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [command player state](command_player_state.md) (1 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (1 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 89 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*