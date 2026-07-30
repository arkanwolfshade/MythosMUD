# correct patterns

> 22 nodes

## Key Concepts

- **NATSUnsubscribeError** (12 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **Exception** (6 connections)
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **test_unsubscribe_from_subject_not_found()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_not_found()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **Raised when unsubscribe operations fail.** (1 connections) — `server/services/nats_exceptions.py`
- **Raised when request/response operations fail.** (1 connections) — `server/services/nats_exceptions.py`
- **Test _unsubscribe_from_subject() handles subscription not found.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test unsubscribe() raises NATSUnsubscribeError when subscription not found.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test unsubscribe() raises NATSUnsubscribeError on unsubscribe errors.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test request() raises NATSRequestError when not connected.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test request() raises NATSRequestError on timeout.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test request() raises NATSRequestError on errors.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [BaseUserManager](BaseUserManager.md) (7 shared connections)
- [test combat persistence handler events](test_combat_persistence_handler_events.md) (6 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [connection state machine](connection_state_machine.md) (2 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (2 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 62 (84%)
- INFERRED: 12 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*