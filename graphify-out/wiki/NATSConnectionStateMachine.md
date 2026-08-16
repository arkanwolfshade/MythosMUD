# NATSConnectionStateMachine

> 107 nodes

## Key Concepts

- **NATSConnectionStateMachine** (58 connections) — `server/realtime/connection_state_machine.py`
- **test_connection_state_machine.py** (40 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **connection_state_machine.py** (10 connections) — `server/realtime/connection_state_machine.py`
- **ConnectionEvent** (5 connections) — `server/realtime/connection_state_machine.py`
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
- **test_connection_event_enum()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_degrade()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_degraded()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats_no_connected_time()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats_no_error()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats_with_error()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_invalid_transition_raises_error()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- *... and 82 more nodes in this community*

## Relationships

- [NATSConfig](NATSConfig.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (2 shared connections)
- [.on_enter_state](on_enter_state.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 121 (77%)
- INFERRED: 36 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*