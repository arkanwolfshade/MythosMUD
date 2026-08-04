# nats exceptions services

> 85 nodes

## Key Concepts

- **NATSPublishError** (35 connections) — `server/services/nats_exceptions.py`
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
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (7 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **Exception** (6 connections)
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_publish_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_subscribe_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_health_check_error_creation()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_exception_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **test_subscribe_to_subject_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 60 more nodes in this community*

## Relationships

- [combat validator validators](combat_validator_validators.md) (21 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (20 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [nats message handler](nats_message_handler.md) (3 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)
- [alias command models](alias_command_models.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 261 (78%)
- INFERRED: 75 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*