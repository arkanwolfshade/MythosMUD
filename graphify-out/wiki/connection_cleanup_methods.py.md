# connection_cleanup_methods.py

> 55 nodes · cohesion 0.09

## Key Concepts

- **test_chat_nats_publisher.py** (35 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **chat_nats_publisher.py** (34 connections) — `server/game/chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (31 connections) — `server/game/chat_nats_publisher.py`
- **_message()** (24 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **build_nats_subject()** (13 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (11 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (8 connections) — `server/game/chat_nats_publisher.py`
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **_nats_service_ready()** (8 connections) — `server/game/chat_nats_publisher.py`
- **Any** (8 connections)
- **_extract_subzone_from_room()** (7 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **asyncio** (5 connections)
- **test_publish_chat_message_to_nats_handles_publish_error()** (5 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
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

- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (11 shared connections)
- [deque](deque.md) (6 shared connections)
- [magic_service.py](magic_service.py.md) (5 shared connections)
- [test_skill_service_graded.py](test_skill_service_graded.py.md) (5 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (5 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (4 shared connections)
- [test_lint_raw_sql_in_python.py](test_lint_raw_sql_in_python.py.md) (3 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [TestCombatConfiguration](TestCombatConfiguration.md) (2 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (2 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/tests/unit/game/test_chat_nats_publisher.py`

## Audit Trail

- EXTRACTED: 173 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*