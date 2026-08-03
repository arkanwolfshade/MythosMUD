# chat game message

> 128 nodes

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **ChatMessage** (32 connections) — `server/game/chat_message.py`
- **chat_npc_system.py** (32 connections) — `server/game/chat_npc_system.py`
- **chat_nats_publisher.py** (29 connections) — `server/game/chat_nats_publisher.py`
- **chat_message_senders.py** (26 connections) — `server/game/chat_message_senders.py`
- **publish_chat_message_to_nats()** (24 connections) — `server/game/chat_nats_publisher.py`
- **chat_message.py** (14 connections) — `server/game/chat_message.py`
- **chat_pose_helpers.py** (14 connections) — `server/game/chat_pose_helpers.py`
- **send_global_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
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
- **_build_standardized_subject()** (9 connections) — `server/game/chat_nats_publisher.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **chat_validator.py** (9 connections) — `server/game/chat_validator.py`
- *... and 103 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (31 shared connections)
- [quest chat game](quest_chat_game.md) (24 shared connections)
- [chat service game](chat_service_game.md) (21 shared connections)
- [chat moderation game](chat_moderation_game.md) (3 shared connections)
- [emote game service](emote_game_service.md) (2 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (2 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (2 shared connections)
- [game chat whisper](game_chat_whisper.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)
- [dialogue service game](dialogue_service_game.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_npc_system.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/game/chat_validator.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 650 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*