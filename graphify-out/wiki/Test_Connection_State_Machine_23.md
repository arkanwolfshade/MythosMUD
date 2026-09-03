# Test Connection State Machine

> 23 nodes

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
- **test_nats_connection_state_machine_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
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
- **Test NATSConnectionStateMachine initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connect() transition from disconnected to connecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connection_failed() transition from reconnecting to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`

## Relationships

- [Test Connection State Machine](Test_Connection_State_Machine.md) (23 shared connections)
- [Connection State Machine](Connection_State_Machine.md) (15 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*