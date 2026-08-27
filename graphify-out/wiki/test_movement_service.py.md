# test_movement_service.py

> 70 nodes

## Key Concepts

- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_support.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **ChatCommandsProtocol** (19 connections) — `server/commands/communication_commands_support.py`
- **communication_commands_support.py** (16 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (15 connections) — `server/commands/communication_commands_support.py`
- **app_from_request()** (13 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (13 connections) — `server/commands/communication_commands_support.py`
- **primary_id()** (13 connections) — `server/commands/communication_commands_support.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_system_send_if_admin()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_whisper_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_str_error_from_chat_result()** (9 connections) — `server/commands/communication_commands_flows.py`
- **UserManagerProtocol** (8 connections) — `server/commands/communication_commands_support.py`
- **_deliver_reply_to_last_whisper()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_whisper_message()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_system_services_triple()** (8 connections) — `server/commands/communication_commands_flows.py`
- **AsyncPersistenceForPose** (6 connections) — `server/commands/communication_commands_support.py`
- **_player_id_bundle()** (6 connections) — `server/commands/communication_commands_flows.py`
- *... and 45 more nodes in this community*

## Relationships

- [RoomDataValidator](RoomDataValidator.md) (45 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (10 shared connections)
- [TestHierarchicalSchema](TestHierarchicalSchema.md) (7 shared connections)
- [validate_room_data](validate_room_data.md) (6 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (6 shared connections)
- [apply_communication_dampening](apply_communication_dampening.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (1 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 214 (90%)
- INFERRED: 25 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*