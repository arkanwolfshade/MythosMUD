# handle global command()

> 94 nodes

## Key Concepts

- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_whisper_command()** (21 connections) — `server/commands/communication_commands.py`
- **handle_say_command()** (17 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_whisper_reply.py** (17 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **test_whisper_command.py** (13 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **handle_reply_command()** (11 connections) — `server/commands/communication_commands.py`
- **handle_me_command()** (8 connections) — `server/commands/communication_commands.py`
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_handle_say_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_delegates_broadcast_to_chat_service_with_ids()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_clear_pose()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_set_pose()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_room()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_player_id()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_chat_service_failure()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_exception()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_whisper_command_target_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_whisper_to_self()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- *... and 69 more nodes in this community*

## Relationships

- [Player Position Service](Player_Position_Service.md) (30 shared connections)
- [chat send with room bundle()](chat_send_with_room_bundle%28%29.md) (16 shared connections)
- [Any](Any.md) (11 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (4 shared connections)
- [benchmark model memory usage()](benchmark_model_memory_usage%28%29.md) (4 shared connections)
- [DropResolved](DropResolved.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (1 shared connections)
- [Validate that player is in](Validate_that_player_is_in.md) (1 shared connections)
- [disconnect player connections()](disconnect_player_connections%28%29.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`

## Audit Trail

- EXTRACTED: 377 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*