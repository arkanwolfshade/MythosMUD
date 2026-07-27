# Realtime Connection State

> 26 nodes · cohesion 0.08

## Key Concepts

- **test_connection_state_machine.py** (38 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_circuit_open()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_close_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_degraded()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_last_error_set()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_open_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_reconnect_attempts_reset_on_success()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_should_open_circuit_under_threshold()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test can_attempt_connection() returns False when connected.** (2 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connected_successfully() transition from connecting to connected.** (2 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_event_enum()** (2 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Unit tests for connection state machine.  Tests the NATSConnectionStateMachine c** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test disconnect() transition from connected to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test disconnect() transition from degraded to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test open_circuit() transition from reconnecting to circuit_open.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test ConnectionEvent enum values.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test close_circuit() transition from circuit_open to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test should_open_circuit() returns False when under threshold.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test get_stats() returns comprehensive statistics.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test reconnect_attempts resets on successful connection.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- *... and 1 more nodes in this community*

## Relationships

- [[Realtime Connection State]] (22 shared connections)
- [[NATS Connection State Machine]] (13 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 90 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
