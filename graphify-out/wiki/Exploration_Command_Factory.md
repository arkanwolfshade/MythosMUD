# Exploration Command Factory

> 26 nodes

## Key Concepts

- **test_connection_state_machine.py** (39 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_start_reconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_open_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_disconnected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_should_open_circuit_under_threshold()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats_no_connected_time()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_reconnect_attempts_reset_on_success()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_total_connections_increment()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_last_error_set()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_event_enum()** (2 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Unit tests for connection state machine.  Tests the NATSConnectionStateMachine c** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test ConnectionEvent enum values.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connected_successfully() transition from reconnecting to connected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connection_failed() transition from reconnecting to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test start_reconnect() transition from disconnected to reconnecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test open_circuit() transition from reconnecting to circuit_open.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test can_attempt_connection() returns True when disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test can_attempt_connection() returns True when connecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test should_open_circuit() returns False when under threshold.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test get_stats() handles None connected time.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test reconnect_attempts resets on successful connection.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test total_connections increments on successful connection.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- *... and 1 more nodes in this community*

## Relationships

- [Room Subscription Helpers](Room_Subscription_Helpers.md) (12 shared connections)
- [Realtime Connection](Realtime_Connection.md) (2 shared connections)
- [test_can_attempt_connection_circuit_open](test_can_attempt_connection_circuit_open.md) (1 shared connections)
- [test_can_attempt_connection_connected](test_can_attempt_connection_connected.md) (1 shared connections)
- [test_can_attempt_connection_reconnecting](test_can_attempt_connection_reconnecting.md) (1 shared connections)
- [test_close_circuit](test_close_circuit.md) (1 shared connections)
- [test_connect_transition](test_connect_transition.md) (1 shared connections)
- [test_connected_successfully_from_connecting](test_connected_successfully_from_connecting.md) (1 shared connections)
- [test_connection_failed_from_connecting](test_connection_failed_from_connecting.md) (1 shared connections)
- [test_degrade](test_degrade.md) (1 shared connections)
- [test_disconnect_from_connected](test_disconnect_from_connected.md) (1 shared connections)
- [test_disconnect_from_degraded](test_disconnect_from_degraded.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 87 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*