# Community 301

> 55 nodes

## Key Concepts

- **chat_npc_system.py** (37 connections) — `server/game/chat_npc_system.py`
- **ChatMessage** (23 connections) — `server/game/chat_message.py`
- **chat_message.py** (20 connections) — `server/game/chat_message.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **_ChatDeliveryService** (8 connections) — `server/game/chat_npc_system.py`
- **create_and_log_chat_message()** (8 connections) — `server/game/chat_message_helpers.py`
- **deliver_fake_npc_whisper()** (8 connections) — `server/game/chat_npc_system.py`
- **send_fake_npc_whisper()** (8 connections) — `server/game/chat_npc_system.py`
- **send_npc_say_to_room()** (8 connections) — `server/game/chat_npc_system.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **send_personal_system_message()** (7 connections) — `server/game/chat_npc_system.py`
- **store_message_in_room_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **UUID** (6 connections)
- **create_and_log_say_message()** (5 connections) — `server/game/chat_message_helpers.py`
- **deliver_npc_room_speech()** (5 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (5 connections) — `server/game/chat_npc_system.py`
- **store_global_message_in_history()** (4 connections) — `server/game/chat_message_helpers.py`
- **npc_sender_id()** (4 connections) — `server/game/chat_npc_system.py`
- **schedule_coro()** (4 connections) — `server/game/chat_npc_system.py`
- **resolve_npc_display_name()** (4 connections) — `server/npc/npc_display_names.py`
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **test_create_and_log_chat_message()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_store_global_message_in_history_trims()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_store_message_in_room_history_creates_and_trims()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- *... and 30 more nodes in this community*

## Relationships

- [Community 302](Community_302.md) (10 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (9 shared connections)
- [Community 54](Community_54.md) (8 shared connections)
- [Community 612](Community_612.md) (5 shared connections)
- [Community 319](Community_319.md) (5 shared connections)
- [Community 451](Community_451.md) (4 shared connections)
- [Game Event Types](Game_Event_Types.md) (4 shared connections)
- [Community 568](Community_568.md) (4 shared connections)
- [Community 629](Community_629.md) (3 shared connections)
- [Community 325](Community_325.md) (3 shared connections)
- [Chat Service](Chat_Service.md) (2 shared connections)
- [Community 794](Community_794.md) (2 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_npc_system.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_message_helpers.py`

## Audit Trail

- EXTRACTED: 154 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*