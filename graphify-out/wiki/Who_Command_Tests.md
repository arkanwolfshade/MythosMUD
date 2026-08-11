# Who Command Tests

> 41 nodes

## Key Concepts

- **chat_service.py** (33 connections) — `server/game/chat_service.py`
- **ChatMessage** (27 connections) — `server/game/chat_message.py`
- **chat_pose_helpers.py** (14 connections) — `server/game/chat_pose_helpers.py`
- **chat_message.py** (13 connections) — `server/game/chat_message.py`
- **set_player_pose()** (8 connections) — `server/game/chat_pose_helpers.py`
- **Any** (5 connections)
- **get_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **clear_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **normalize_player_id()** (4 connections) — `server/game/chat_pose_helpers.py`
- **UUID** (4 connections)
- **get_room_poses()** (4 connections) — `server/game/chat_pose_helpers.py`
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **test_chat_message_init()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_init_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_log_message()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_echo_sent()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **.__init__()** (2 connections) — `server/game/chat_message.py`
- **UUID** (2 connections)
- **.log_message()** (2 connections) — `server/game/chat_message.py`
- **vulture_allowlist.py** (2 connections) — `vulture_allowlist.py`
- **Any** (1 connections)
- **Chat message model for MythosMUD.  This module provides the ChatMessage class wh** (1 connections) — `server/game/chat_message.py`
- **Represents a chat message with metadata.** (1 connections) — `server/game/chat_message.py`
- *... and 16 more nodes in this community*

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (16 shared connections)
- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (13 shared connections)
- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Typography Layout Spec](Typography_Layout_Spec.md) (7 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (2 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (1 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 169 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*