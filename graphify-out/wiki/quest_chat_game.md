# quest chat game

> 93 nodes

## Key Concepts

- **test_chat_npc_system.py** (46 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (33 connections) — `server/game/chat_npc_system.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **NPCSpoke** (16 connections) — `server/events/event_types.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **subscribe_npc_spoke_to_chat()** (10 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 68 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (21 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (13 shared connections)
- [quest game service](quest_game_service.md) (13 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (9 shared connections)
- [nats services service](nats_services_service.md) (4 shared connections)
- [chat service game](chat_service_game.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [command exploration models](command_exploration_models.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [player cache rationale](player_cache_rationale.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/events/event_types.py`
- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 424 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*