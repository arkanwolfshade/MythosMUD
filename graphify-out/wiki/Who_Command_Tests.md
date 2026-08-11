# Who Command Tests

> 50 nodes

## Key Concepts

- **chat_service.py** (33 connections) — `server/game/chat_service.py`
- **ChatMessage** (27 connections) — `server/game/chat_message.py`
- **chat_nats_publisher.py** (21 connections) — `server/game/chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (16 connections) — `server/game/chat_nats_publisher.py`
- **chat_pose_helpers.py** (14 connections) — `server/game/chat_pose_helpers.py`
- **chat_message.py** (13 connections) — `server/game/chat_message.py`
- **set_player_pose()** (8 connections) — `server/game/chat_pose_helpers.py`
- **chat_validator.py** (8 connections) — `server/game/chat_validator.py`
- **Any** (5 connections)
- **get_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **clear_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **validate_chat_message()** (5 connections) — `server/game/chat_validator.py`
- **normalize_player_id()** (4 connections) — `server/game/chat_pose_helpers.py`
- **UUID** (4 connections)
- **get_room_poses()** (4 connections) — `server/game/chat_pose_helpers.py`
- **validate_room_access()** (4 connections) — `server/game/chat_validator.py`
- **contains_malicious_content()** (3 connections) — `server/game/chat_validator.py`
- **test_chat_message_init()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_init_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_log_message()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_echo_sent()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **.__init__()** (2 connections) — `server/game/chat_message.py`
- **UUID** (2 connections)
- *... and 25 more nodes in this community*

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (22 shared connections)
- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (17 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (12 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (8 shared connections)
- [Health Endpoint Spec](Health_Endpoint_Spec.md) (4 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (2 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (2 shared connections)
- [Cursor Skills Delight](Cursor_Skills_Delight.md) (1 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Container Open Events](Container_Open_Events.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/game/chat_validator.py`
- `server/tests/unit/game/test_chat_service.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 227 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*