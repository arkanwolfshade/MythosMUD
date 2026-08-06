# commands inventory put

> 14 nodes

## Key Concepts

- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **Exception** (6 connections)
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **Raised when request/response operations fail.** (1 connections) — `server/services/nats_exceptions.py`
- **Test request() raises NATSRequestError when not connected.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test request() raises NATSRequestError on timeout.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test request() raises NATSRequestError on errors.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [commands communication say](commands_communication_say.md) (5 shared connections)
- [combat commands handler](combat_commands_handler.md) (4 shared connections)
- [game chat service](game_chat_service.md) (2 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [connection state machine](connection_state_machine.md) (1 shared connections)
- [target resolution service](target_resolution_service.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 42 (86%)
- INFERRED: 7 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*