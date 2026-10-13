# Community 302

> 55 nodes

## Key Concepts

- **test_chat_nats_publisher.py** (35 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **chat_nats_publisher.py** (33 connections) — `server/game/chat_nats_publisher.py`
- **_message()** (24 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (21 connections) — `server/game/chat_nats_publisher.py`
- **build_nats_subject()** (13 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (11 connections) — `server/game/chat_nats_publisher.py`
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **_nats_service_ready()** (8 connections) — `server/game/chat_nats_publisher.py`
- **Any** (8 connections)
- **_extract_subzone_from_room()** (7 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_handles_publish_error()** (5 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **asyncio** (5 connections)
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_unexpected_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_room_access_failure()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_success()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_unexpected_error()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_validation_failure()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_global()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_local_uses_subzone()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_party_with_id()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- *... and 30 more nodes in this community*

## Relationships

- [Community 301](Community_301.md) (10 shared connections)
- [Community 612](Community_612.md) (5 shared connections)
- [Community 96](Community_96.md) (4 shared connections)
- [Community 629](Community_629.md) (3 shared connections)
- [Community 54](Community_54.md) (3 shared connections)
- [Community 460](Community_460.md) (2 shared connections)
- [Community 218](Community_218.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 63](Community_63.md) (2 shared connections)
- [Community 794](Community_794.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/tests/unit/game/test_chat_nats_publisher.py`

## Audit Trail

- EXTRACTED: 160 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*