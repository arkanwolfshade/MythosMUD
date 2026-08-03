# quest chat game

> 87 nodes

## Key Concepts

- **test_chat_npc_system.py** (46 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (33 connections) — `server/game/chat_npc_system.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
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
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **npc_sender_id()** (5 connections) — `server/game/chat_npc_system.py`
- **_on_npc_spoke()** (5 connections) — `server/game/chat_npc_system.py`
- *... and 62 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (20 shared connections)
- [quest game service](quest_game_service.md) (13 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (11 shared connections)
- [item models rationale](item_models_rationale.md) (8 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [chat service game](chat_service_game.md) (2 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 388 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*