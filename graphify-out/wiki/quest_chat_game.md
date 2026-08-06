# quest chat game

> 51 nodes

## Key Concepts

- **test_chat_npc_system.py** (46 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (33 connections) — `server/game/chat_npc_system.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **npc_sender_id()** (5 connections) — `server/game/chat_npc_system.py`
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **test_send_personal_system_message_targets_player()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **UUID** (4 connections)
- **reset_npc_spoke_subscription_for_tests()** (4 connections) — `server/game/chat_npc_system.py`
- **_reset_chat_npc_wiring()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_rejects_empty_message_and_room()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_publish_failure()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_personal_system_rejects_empty()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_when_chat_service_unwired()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_resolve_npc_display_name()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_subscribe_npc_spoke_to_chat_once()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 26 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (17 shared connections)
- [game chat moderation](game_chat_moderation.md) (13 shared connections)
- [services ascii map](services_ascii_map.md) (12 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (6 shared connections)
- [chat game message](chat_game_message.md) (5 shared connections)
- [alias command models](alias_command_models.md) (4 shared connections)
- [chat service game](chat_service_game.md) (2 shared connections)
- [dialogue service game](dialogue_service_game.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [skill service game](skill_service_game.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 240 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*