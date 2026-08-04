# chat service game

> 148 nodes

## Key Concepts

- **ChatService** (91 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (43 connections) — `server/tests/unit/game/test_chat_service.py`
- **UUID** (27 connections)
- **Any** (16 connections)
- **.send_local_message()** (4 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_party_message()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_personal_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **.set_player_pose()** (4 connections) — `server/game/chat_service.py`
- **.send_predefined_emote()** (4 connections) — `server/game/chat_service.py`
- **.get_player_mutes()** (4 connections) — `server/game/chat_service.py`
- **test_get_room_messages()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
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
- *... and 123 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (21 shared connections)
- [quest chat game](quest_chat_game.md) (4 shared connections)
- [game chat whisper](game_chat_whisper.md) (4 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (3 shared connections)
- [player death service](player_death_service.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [command exploration models](command_exploration_models.md) (2 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [player helpers error](player_helpers_error.md) (1 shared connections)
- [dialogue schemas tree](dialogue_schemas_tree.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 459 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*