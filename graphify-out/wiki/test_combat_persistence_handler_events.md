# test combat persistence handler events

> 81 nodes

## Key Concepts

- **nats_exceptions.py** (33 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSError** (9 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (7 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_publish_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_subscribe_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_health_check_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_exception_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **test_subscribe_to_subject_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **.test_nats_error_creation()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_nats_error_inheritance()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_with_url()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_with_original_error()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- *... and 56 more nodes in this community*

## Relationships

- [Any](Any.md) (30 shared connections)
- [Player](Player.md) (9 shared connections)
- [BaseUserManager](BaseUserManager.md) (7 shared connections)
- [correct patterns](correct_patterns.md) (6 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (6 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [connection state machine](connection_state_machine.md) (3 shared connections)
- [test combat persistence handler persistence](test_combat_persistence_handler_persistence.md) (1 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (1 shared connections)
- [.model dump()](model_dump%28%29.md) (1 shared connections)
- [test nats message handler chat](test_nats_message_handler_chat.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 267 (78%)
- INFERRED: 75 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*