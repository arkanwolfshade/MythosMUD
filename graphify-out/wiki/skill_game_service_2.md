# skill game service

> 10 nodes

## Key Concepts

- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **Raised when request/response operations fail.** (1 connections) — `server/services/nats_exceptions.py`
- **Send a request to a NATS subject and wait for a response.          Args:** (1 connections) — `server/services/nats_service.py`
- **Test request() raises NATSRequestError when not connected.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test request() raises NATSRequestError on timeout.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test request() raises NATSRequestError on errors.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [combat commands handler](combat_commands_handler.md) (4 shared connections)
- [combat validator validators](combat_validator_validators.md) (3 shared connections)
- [game chat service](game_chat_service.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [player event state](player_event_state.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 22 (76%)
- INFERRED: 7 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*