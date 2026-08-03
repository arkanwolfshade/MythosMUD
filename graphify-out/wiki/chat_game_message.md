# chat game message

> 85 nodes

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **ChatMessage** (33 connections) — `server/game/chat_message.py`
- **chat_message_senders.py** (26 connections) — `server/game/chat_message_senders.py`
- **publish_chat_message_to_nats()** (24 connections) — `server/game/chat_nats_publisher.py`
- **chat_message.py** (14 connections) — `server/game/chat_message.py`
- **chat_pose_helpers.py** (14 connections) — `server/game/chat_pose_helpers.py`
- **chat_logger.py** (14 connections) — `server/services/chat_logger.py`
- **send_global_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (12 connections) — `server/game/chat_message_senders.py`
- **chat_message_helpers.py** (11 connections) — `server/game/chat_message_helpers.py`
- **create_and_log_chat_message()** (11 connections) — `server/game/chat_message_helpers.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **send_predefined_emote()** (10 connections) — `server/game/chat_message_senders.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **store_message_in_room_history()** (9 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (9 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (9 connections) — `server/game/chat_message_senders.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **rate_limiter.py** (9 connections) — `server/services/rate_limiter.py`
- **set_player_pose()** (8 connections) — `server/game/chat_pose_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- *... and 60 more nodes in this community*

## Relationships

- [chat service game](chat_service_game.md) (21 shared connections)
- [quest chat game](quest_chat_game.md) (20 shared connections)
- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (16 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [chat moderation game](chat_moderation_game.md) (3 shared connections)
- [game chat whisper](game_chat_whisper.md) (2 shared connections)
- [services user manager](services_user_manager.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [rate limiter services](rate_limiter_services.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/services/chat_logger.py`
- `server/services/rate_limiter.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 474 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*