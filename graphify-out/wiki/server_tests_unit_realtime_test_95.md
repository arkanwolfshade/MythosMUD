# server tests unit realtime test

> 21 nodes

## Key Concepts

- **test_connection_state_machine.py** (40 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_circuit_open()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connect_transition()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats_no_connected_time()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats_no_error()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_recover()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_start_reconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test can_attempt_connection() returns False when connected.** (2 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Unit tests for connection state machine. Tests the NATSConnectionStateMachine…** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test disconnect() transition from connected to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test start_reconnect() transition from disconnected to reconnecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test recover() transition from degraded to connected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test can_attempt_connection() returns True when connecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test get_stats() handles None error.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test get_stats() handles None connected time.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connect() transition from disconnected to connecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connection_failed() transition from reconnecting to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (24 shared connections)
- [server realtime connection state machine](server_realtime_connection_state_machine.md) (14 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 50 (83%)
- INFERRED: 10 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*