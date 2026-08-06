# chat service game

> 131 nodes

## Key Concepts

- **ChatService** (91 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (43 connections) — `server/tests/unit/game/test_chat_service.py`
- **UUID** (27 connections)
- **.send_local_message()** (4 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_party_message()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_personal_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **.set_player_pose()** (4 connections) — `server/game/chat_service.py`
- **.send_predefined_emote()** (4 connections) — `server/game/chat_service.py`
- **.get_player_mutes()** (4 connections) — `server/game/chat_service.py`
- **.send_npc_say_to_room()** (3 connections) — `server/game/chat_service.py`
- **.get_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.clear_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.mute_channel()** (3 connections) — `server/game/chat_service.py`
- **.unmute_channel()** (3 connections) — `server/game/chat_service.py`
- **.is_channel_muted()** (3 connections) — `server/game/chat_service.py`
- **.mute_player()** (3 connections) — `server/game/chat_service.py`
- **.unmute_player()** (3 connections) — `server/game/chat_service.py`
- **.is_player_muted()** (3 connections) — `server/game/chat_service.py`
- **.mute_global()** (3 connections) — `server/game/chat_service.py`
- **.unmute_global()** (3 connections) — `server/game/chat_service.py`
- **.is_globally_muted()** (3 connections) — `server/game/chat_service.py`
- **.add_admin()** (3 connections) — `server/game/chat_service.py`
- *... and 106 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (20 shared connections)
- [services ascii map](services_ascii_map.md) (11 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (3 shared connections)
- [game chat whisper](game_chat_whisper.md) (3 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [chat moderation game](chat_moderation_game.md) (2 shared connections)
- [quest chat game](quest_chat_game.md) (2 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 410 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*