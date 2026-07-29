# connection state machine

> 101 nodes

## Key Concepts

- **NATSConnectionStateMachine** (58 connections) — `server/realtime/connection_state_machine.py`
- **test_connection_state_machine.py** (39 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **connection_state_machine.py** (10 connections) — `server/realtime/connection_state_machine.py`
- **ConnectionEvent** (4 connections) — `server/realtime/connection_state_machine.py`
- **.on_connection_failed()** (3 connections) — `server/realtime/connection_state_machine.py`
- **test_nats_connection_state_machine_init()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_nats_connection_state_machine_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connect_transition()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_degraded()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_start_reconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_degrade()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_recover()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_open_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_close_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_disconnected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_circuit_open()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_should_open_circuit_under_threshold()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- *... and 76 more nodes in this community*

## Relationships

- [nats config()](nats_config%28%29.md) (5 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [.get stats()](get_stats%28%29.md) (2 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [NATS](NATS.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 298 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*