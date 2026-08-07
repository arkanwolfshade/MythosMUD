# quest chat game

> 84 nodes

## Key Concepts

- **test_chat_npc_system.py** (46 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **ChatMessage** (41 connections) — `server/game/chat_message.py`
- **chat_npc_system.py** (33 connections) — `server/game/chat_npc_system.py`
- **chat_message.py** (17 connections) — `server/game/chat_message.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **chat_message_helpers.py** (12 connections) — `server/game/chat_message_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **npc_sender_id()** (5 connections) — `server/game/chat_npc_system.py`
- **_on_npc_spoke()** (5 connections) — `server/game/chat_npc_system.py`
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **test_send_personal_system_message_targets_player()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 59 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (27 shared connections)
- [quest game service](quest_game_service.md) (16 shared connections)
- [chat service game](chat_service_game.md) (14 shared connections)
- [alias command models](alias_command_models.md) (9 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (7 shared connections)
- [nats services service](nats_services_service.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (5 shared connections)
- [app tick game](app_tick_game.md) (5 shared connections)
- [player helpers error](player_helpers_error.md) (5 shared connections)
- [combat messaging service](combat_messaging_service.md) (3 shared connections)
- [services nats service](services_nats_service.md) (3 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_npc_system.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 394 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*