# TestHierarchicalSchema

> 41 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (23 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **asyncio** (15 connections)
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **handle_me_command()** (7 connections) — `server/commands/communication_commands.py`
- **test_handle_pose_command_clear_pose()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_set_pose()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_chat_service_failure()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_delegates_broadcast_to_chat_service_with_ids()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_exception()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_player_id()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_room()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_handle_me_command_no_action()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_me_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_services()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Test handle_say_command when player has no current room.** (2 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Room-wide say; returns user-facing result dict.** (1 connections) — `server/commands/communication_commands.py`
- **Set or clear persistent pose text.** (1 connections) — `server/commands/communication_commands.py`
- *... and 16 more nodes in this community*

## Relationships

- [validate_room_data](validate_room_data.md) (9 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (8 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`

## Audit Trail

- EXTRACTED: 112 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*