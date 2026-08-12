# Who Command Tests

> 62 nodes

## Key Concepts

- **chat_service.py** (33 connections) — `server/game/chat_service.py`
- **ChatMessage** (27 connections) — `server/game/chat_message.py`
- **chat_nats_publisher.py** (21 connections) — `server/game/chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (16 connections) — `server/game/chat_nats_publisher.py`
- **chat_pose_helpers.py** (14 connections) — `server/game/chat_pose_helpers.py`
- **chat_message.py** (13 connections) — `server/game/chat_message.py`
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **set_player_pose()** (8 connections) — `server/game/chat_pose_helpers.py`
- **chat_validator.py** (8 connections) — `server/game/chat_validator.py`
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_extract_subzone_from_room()** (5 connections) — `server/game/chat_nats_publisher.py`
- **Any** (5 connections)
- **Any** (5 connections)
- **get_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **clear_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **validate_chat_message()** (5 connections) — `server/game/chat_validator.py`
- **_subject_whisper_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **normalize_player_id()** (4 connections) — `server/game/chat_pose_helpers.py`
- **UUID** (4 connections)
- **get_room_poses()** (4 connections) — `server/game/chat_pose_helpers.py`
- **validate_room_access()** (4 connections) — `server/game/chat_validator.py`
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **contains_malicious_content()** (3 connections) — `server/game/chat_validator.py`
- *... and 37 more nodes in this community*

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (26 shared connections)
- [Client Event Store](Client_Event_Store.md) (17 shared connections)
- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (13 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (2 shared connections)
- [Cursor Setup Guide](Cursor_Setup_Guide.md) (2 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (2 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (2 shared connections)
- [Structured Error Logging Tasks](Structured_Error_Logging_Tasks.md) (2 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/game/chat_validator.py`
- `server/tests/unit/game/test_chat_service.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 265 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*