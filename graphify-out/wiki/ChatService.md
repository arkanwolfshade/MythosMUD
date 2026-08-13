# ChatService

> 70 nodes

## Key Concepts

- **ChatService** (82 connections) — `server/game/chat_service.py`
- **UUID** (26 connections)
- **Any** (14 connections)
- **.get_player_mutes()** (4 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (4 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_local_message()** (4 connections) — `server/game/chat_service.py`
- **.send_party_message()** (4 connections) — `server/game/chat_service.py`
- **.send_predefined_emote()** (4 connections) — `server/game/chat_service.py`
- **.send_say_message()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **.set_player_pose()** (4 connections) — `server/game/chat_service.py`
- **.add_admin()** (3 connections) — `server/game/chat_service.py`
- **.clear_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.get_mute_status()** (3 connections) — `server/game/chat_service.py`
- **.get_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.get_room_messages()** (3 connections) — `server/game/chat_service.py`
- **.get_user_management_stats()** (3 connections) — `server/game/chat_service.py`
- **.is_admin()** (3 connections) — `server/game/chat_service.py`
- **.is_channel_muted()** (3 connections) — `server/game/chat_service.py`
- **.is_globally_muted()** (3 connections) — `server/game/chat_service.py`
- **.is_player_muted()** (3 connections) — `server/game/chat_service.py`
- **.mute_channel()** (3 connections) — `server/game/chat_service.py`
- **.mute_global()** (3 connections) — `server/game/chat_service.py`
- *... and 45 more nodes in this community*

## Relationships

- [test_chat_service.py](test_chat_service.py.md) (28 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [chat_service.py](chat_service.py.md) (4 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (4 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (1 shared connections)
- [ChatModeration](ChatModeration.md) (1 shared connections)
- [UserManagerProtocol](UserManagerProtocol.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`

## Audit Trail

- EXTRACTED: 147 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*