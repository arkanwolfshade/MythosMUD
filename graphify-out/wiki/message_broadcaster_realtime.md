# message broadcaster realtime

> 14 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_before_timeout()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.reset()** (2 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker for NATS message processing.      Implements Martin Fowler's cir** (1 connections) — `server/realtime/circuit_breaker.py`
- **Manually reset circuit breaker to CLOSED state.          Clears all counters and** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test CircuitBreaker initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() opens circuit after failure threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() opens circuit at threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False before timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_state() returns current state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [circuit breaker realtime](circuit_breaker_realtime.md) (13 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (7 shared connections)
- [event bus events](event_bus_events.md) (7 shared connections)
- [events event bus](events_event_bus.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [uuid services npc](uuid_services_npc.md) (1 shared connections)
- [commands rest command](commands_rest_command.md) (1 shared connections)
- [message nats handler](message_nats_handler.md) (1 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (1 shared connections)
- [event events bus](event_events_bus.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 65 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*