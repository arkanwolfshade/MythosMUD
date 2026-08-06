# alias command models

> 54 nodes

## Key Concepts

- **test_chat_nats_publisher.py** (35 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **chat_nats_publisher.py** (30 connections) — `server/game/chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (30 connections) — `server/game/chat_nats_publisher.py`
- **_message()** (24 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **build_nats_subject()** (13 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (11 connections) — `server/game/chat_nats_publisher.py`
- **_build_standardized_subject()** (9 connections) — `server/game/chat_nats_publisher.py`
- **Any** (8 connections)
- **_nats_service_ready()** (8 connections) — `server/game/chat_nats_publisher.py`
- **_extract_subzone_from_room()** (7 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_unexpected_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_handles_publish_error()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_say_includes_room()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_local_uses_subzone()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_global()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_whisper_with_target()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_party_without_id()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_nats_subject_uses_subject_manager_when_available()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_nats_message_data_includes_optional_fields()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_nats_service_ready_false_when_missing()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- *... and 29 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (11 shared connections)
- [quest chat game](quest_chat_game.md) (9 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (6 shared connections)
- [app tick game](app_tick_game.md) (5 shared connections)
- [combat messaging service](combat_messaging_service.md) (3 shared connections)
- [subject validation services](subject_validation_services.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (2 shared connections)
- [chat service game](chat_service_game.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/tests/unit/game/test_chat_nats_publisher.py`

## Audit Trail

- EXTRACTED: 284 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*