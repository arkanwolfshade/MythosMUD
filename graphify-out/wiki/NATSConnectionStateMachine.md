# NATSConnectionStateMachine

> 115 nodes

## Key Concepts

- **NATSConnectionStateMachine** (57 connections) — `server/realtime/connection_state_machine.py`
- **test_connection_state_machine.py** (39 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **nats_service.py** (24 connections) — `server/services/nats_service.py`
- **connection_state_machine.py** (10 connections) — `server/realtime/connection_state_machine.py`
- **ConnectionEvent** (4 connections) — `server/realtime/connection_state_machine.py`
- **.on_enter_state()** (4 connections) — `server/realtime/connection_state_machine.py`
- **.get_stats()** (3 connections) — `server/realtime/connection_state_machine.py`
- **.on_connection_failed()** (3 connections) — `server/realtime/connection_state_machine.py`
- **test_can_attempt_connection_circuit_open()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_disconnected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_close_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connect_transition()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_degrade()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_degraded()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats_no_connected_time()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats_no_error()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- *... and 90 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (4 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [NATSConfig](NATSConfig.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [NATSMetrics](NATSMetrics.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [SubjectValidator](SubjectValidator.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 182 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*