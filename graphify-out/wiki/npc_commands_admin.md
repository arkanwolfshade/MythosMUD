# npc commands admin

> 34 nodes

## Key Concepts

- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **communication_commands_support.py** (16 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (15 connections) — `server/commands/communication_commands_support.py`
- **primary_id()** (13 connections) — `server/commands/communication_commands_support.py`
- **app_from_request()** (12 connections) — `server/commands/communication_commands_support.py`
- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
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
- **test_message_id_from_result_nested()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_message_id_from_result_no_id()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- *... and 9 more nodes in this community*

## Relationships

- [commands communication flows](commands_communication_flows.md) (38 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (7 shared connections)
- [inventory commands command](inventory_commands_command.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [realtime game state](realtime_game_state.md) (2 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 142 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*