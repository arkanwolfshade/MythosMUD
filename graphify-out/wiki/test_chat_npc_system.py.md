# test_chat_npc_system.py

> 97 nodes

## Key Concepts

- **test_chat_npc_system.py** (50 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (36 connections) — `server/game/chat_npc_system.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **NPCSpoke** (14 connections) — `server/events/event_types.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **send_fake_npc_whisper()** (11 connections) — `server/game/chat_npc_system.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **deliver_fake_npc_whisper()** (10 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (10 connections) — `server/game/chat_npc_system.py`
- **asyncio** (10 connections)
- **subscribe_npc_spoke_to_chat()** (9 connections) — `server/game/chat_npc_system.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **_mock_chat_service()** (9 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **_ChatDeliveryService** (8 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **npc_sender_id()** (7 connections) — `server/game/chat_npc_system.py`
- **emit_quest_npc_say()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 72 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (15 shared connections)
- [quest_commands.py](quest_commands.py.md) (12 shared connections)
- [QuestService](QuestService.md) (10 shared connections)
- [NPCBase](NPCBase.md) (7 shared connections)
- [hallucinations.py](hallucinations.py.md) (6 shared connections)
- [should_notify_quest_progress](should_notify_quest_progress.md) (6 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (5 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_base.py`
- `server/npc/npc_display_names.py`
- `server/services/corruption_service.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 281 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*