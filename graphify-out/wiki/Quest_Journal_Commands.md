# Quest Journal Commands

> 64 nodes

## Key Concepts

- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **communication_commands_support.py** (15 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (15 connections) — `server/commands/communication_commands_support.py`
- **primary_id()** (11 connections) — `server/commands/communication_commands_support.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **app_from_request()** (10 connections) — `server/commands/communication_commands_support.py`
- **_system_send_if_admin()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_whisper_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **get_pose_persistence()** (9 connections) — `server/commands/communication_commands_support.py`
- **_deliver_whisper_message()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_reply_to_last_whisper()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_system_services_triple()** (7 connections) — `server/commands/communication_commands_flows.py`
- **UserManagerProtocol** (7 connections) — `server/commands/communication_commands_support.py`
- **_player_id_bundle()** (6 connections) — `server/commands/communication_commands_flows.py`
- **AsyncPersistenceForPose** (6 connections) — `server/commands/communication_commands_support.py`
- **Protocol** (5 connections)
- **PlayerWithPose** (4 connections) — `server/commands/communication_commands_support.py`
- **test_app_from_request_with_app()** (3 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- *... and 39 more nodes in this community*

## Relationships

- [Schedule Service Loader](Schedule_Service_Loader.md) (49 shared connections)
- [Container Open Events](Container_Open_Events.md) (10 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (2 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (2 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (2 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 315 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*