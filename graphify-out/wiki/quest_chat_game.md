# quest chat game

> 55 nodes

## Key Concepts

- **test_chat_npc_system.py** (46 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **subscribe_npc_spoke_to_chat()** (10 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **npc_sender_id()** (5 connections) — `server/game/chat_npc_system.py`
- **_on_npc_spoke()** (5 connections) — `server/game/chat_npc_system.py`
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **test_send_personal_system_message_targets_player()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **schedule_coro()** (4 connections) — `server/game/chat_npc_system.py`
- **reset_npc_spoke_subscription_for_tests()** (4 connections) — `server/game/chat_npc_system.py`
- **_reset_chat_npc_wiring()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_rejects_empty_message_and_room()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_publish_failure()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_personal_system_rejects_empty()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_when_chat_service_unwired()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_npc_spoke_handler_schedules_room_speech()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_resolve_npc_display_name()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 30 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (27 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (12 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (8 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (5 shared connections)
- [nats services service](nats_services_service.md) (4 shared connections)
- [chat service game](chat_service_game.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_npc_system.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 218 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*