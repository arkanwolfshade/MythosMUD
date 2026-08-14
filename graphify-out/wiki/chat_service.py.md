# chat_service.py

> 139 nodes

## Key Concepts

- **chat_service.py** (59 connections) — `server/game/chat_service.py`
- **ChatMessage** (48 connections) — `server/game/chat_message.py`
- **test_chat_npc_system.py** (46 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (33 connections) — `server/game/chat_npc_system.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **ChatUserManager** (14 connections) — `server/game/chat_channel_message_senders.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **ChatRateLimiter** (13 connections) — `server/game/chat_channel_message_senders.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **ChatLogger** (12 connections) — `server/game/chat_channel_message_senders.py`
- **ChatPlayerService** (12 connections) — `server/game/chat_channel_message_senders.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **.send_say_message()** (11 connections) — `server/game/chat_service.py`
- **subscribe_npc_spoke_to_chat()** (9 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **asyncio** (8 connections)
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- *... and 114 more nodes in this community*

## Relationships

- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (40 shared connections)
- [ChatService](ChatService.md) (27 shared connections)
- [test_chat_message_senders.py](test_chat_message_senders.py.md) (24 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (14 shared connections)
- [quest_chat_notify.py](quest_chat_notify.py.md) (14 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (8 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)
- [quest_commands.py](quest_commands.py.md) (7 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_npc_system.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 420 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*