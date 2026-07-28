# Server Game (16)

> 57 nodes

## Key Concepts

- **test_chat_npc_system.py** (43 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (28 connections) — `server/game/chat_npc_system.py`
- **send_npc_say_to_room()** (12 connections) — `server/game/chat_npc_system.py`
- **send_personal_system_message()** (10 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (9 connections) — `server/game/chat_npc_system.py`
- **Any** (8 connections)
- **deliver_personal_system()** (8 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (7 connections) — `server/game/chat_npc_system.py`
- **subscribe_npc_spoke_to_chat()** (7 connections) — `server/game/chat_npc_system.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **set_chat_service_for_npc_system()** (6 connections) — `server/game/chat_npc_system.py`
- **_on_npc_spoke()** (6 connections) — `server/game/chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **npc_sender_id()** (5 connections) — `server/game/chat_npc_system.py`
- **schedule_coro()** (5 connections) — `server/game/chat_npc_system.py`
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **UUID** (4 connections)
- **test_send_npc_say_rejects_empty_message_and_room()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_publish_failure()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_personal_system_message_targets_player()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_personal_system_rejects_empty()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_when_chat_service_unwired()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 32 more nodes in this community*

## Relationships

- [Server Game (27)](Server_Game_%2827%29.md) (19 shared connections)
- [Server Game (11)](Server_Game_%2811%29.md) (9 shared connections)
- [Server Game (22)](Server_Game_%2822%29.md) (8 shared connections)
- [Server Events](Server_Events.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Game (12)](Server_Game_%2812%29.md) (2 shared connections)
- [Server Npc (3)](Server_Npc_%283%29.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 255 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*