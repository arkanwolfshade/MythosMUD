# communication commands support

> 38 nodes

## Key Concepts

- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **communication_commands_support.py** (15 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (15 connections) — `server/commands/communication_commands_support.py`
- **primary_id()** (11 connections) — `server/commands/communication_commands_support.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **app_from_request()** (10 connections) — `server/commands/communication_commands_support.py`
- **get_pose_persistence()** (9 connections) — `server/commands/communication_commands_support.py`
- **UserManagerProtocol** (7 connections) — `server/commands/communication_commands_support.py`
- **AsyncPersistenceForPose** (6 connections) — `server/commands/communication_commands_support.py`
- **Protocol** (5 connections)
- **PlayerWithPose** (4 connections) — `server/commands/communication_commands_support.py`
- **test_app_from_request_with_app()** (3 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_services_from_container_via_container()** (3 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_services_from_container_state_fallback()** (3 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_pose_persistence_from_container()** (3 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_pose_persistence_state_fallback()** (3 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **.get_player_by_name()** (2 connections) — `server/commands/communication_commands_support.py`
- **.save_player()** (2 connections) — `server/commands/communication_commands_support.py`
- **test_app_from_request_none()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_primary_id_prefers_id()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_primary_id_falls_back_to_player_id()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_services_from_container_no_app()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_chat_result_map_dict()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_chat_result_map_non_dict()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- *... and 13 more nodes in this community*

## Relationships

- [communication commands](communication_commands.md) (29 shared connections)
- [chat send with room bundle()](chat_send_with_room_bundle%28%29.md) (13 shared connections)
- [Any](Any.md) (3 shared connections)
- [handle global command()](handle_global_command%28%29.md) (2 shared connections)
- [.state()](state%28%29.md) (2 shared connections)
- [admin summon command](admin_summon_command.md) (1 shared connections)
- [DropResolved](DropResolved.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 159 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*