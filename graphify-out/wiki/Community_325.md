# Community 325

> 51 nodes

## Key Concepts

- **test_chat_npc_system.py** (27 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **asyncio** (10 connections)
- **_mock_chat_service()** (9 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **.send_npc_say_to_room()** (5 connections) — `server/game/chat_service.py`
- **.send_personal_system_message()** (5 connections) — `server/game/chat_service.py`
- **test_send_npc_say_publish_failure()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_rejects_empty_message_and_room()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_personal_system_message_targets_player()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_personal_system_rejects_empty()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **test_chat_service_npc_and_personal_wrappers()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_fake_npc_whisper_rejects_empty()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_fake_npc_whisper_targets_player_as_whisper()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **_reset_chat_npc_wiring()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_when_chat_service_unwired()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **register_npc_display_name()** (2 connections) — `server/npc/npc_display_names.py`
- **test_chat_message_to_dict_includes_speaker_kind()** (2 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_emit_quest_npc_say_and_templates()** (2 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (2 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_npc_spoke_handler_schedules_room_speech()** (2 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_resolve_npc_display_name()** (2 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_should_notify_quest_progress_milestones()** (2 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_subscribe_npc_spoke_to_chat_once()** (2 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 26 more nodes in this community*

## Relationships

- [Chat Service](Chat_Service.md) (5 shared connections)
- [Community 301](Community_301.md) (3 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (1 shared connections)
- [Community 568](Community_568.md) (1 shared connections)
- [Game Event Types](Game_Event_Types.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 75 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*