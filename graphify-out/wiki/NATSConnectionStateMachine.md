# NATSConnectionStateMachine

> 26 nodes

## Key Concepts

- **NATSConnectionStateMachine** (58 connections) — `server/realtime/connection_state_machine.py`
- **.can_attempt_connection()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.__init__()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_close_circuit()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_connect()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_connected_successfully()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_degrade()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_disconnect()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_open_circuit()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_recover()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_start_reconnect()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.reset()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.should_open_circuit()** (2 connections) — `server/realtime/connection_state_machine.py`
- **Initialize connection state machine. Args: connection_id: Unique identifier for…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connect transition. Resets reconnection counter and prepares for…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for successful connection. Records connection time and increments…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for disconnection. Increments disconnection counter. AI: Track…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for starting reconnection. Checks if circuit breaker should be…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for circuit breaker opening. Logs circuit open event for alerting. AI:…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for circuit breaker closing. Resets failure counters. AI: Circuit…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connection degradation. Logs degraded state for monitoring. AI:…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for recovery from degraded state. Logs recovery for monitoring. AI:…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Check if connection attempt is allowed in current state. Returns: True if…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Check if circuit breaker should be opened. Returns: True if max attempts…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Reset state machine to initial state. Clears all counters and metadata. AI: For…** (1 connections) — `server/realtime/connection_state_machine.py`
- *... and 1 more nodes in this community*

## Relationships

- [test_connection_state_machine.py](test_connection_state_machine.py.md) (13 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [connection_state_machine.py](connection_state_machine.py.md) (2 shared connections)
- [.on_enter_state](on_enter_state.md) (2 shared connections)
- [test_can_attempt_connection_circuit_open](test_can_attempt_connection_circuit_open.md) (1 shared connections)
- [test_can_attempt_connection_connected](test_can_attempt_connection_connected.md) (1 shared connections)
- [test_can_attempt_connection_reconnecting](test_can_attempt_connection_reconnecting.md) (1 shared connections)
- [test_close_circuit](test_close_circuit.md) (1 shared connections)
- [test_connect_transition](test_connect_transition.md) (1 shared connections)
- [test_connected_successfully_from_connecting](test_connected_successfully_from_connecting.md) (1 shared connections)
- [test_connection_failed_from_connecting](test_connection_failed_from_connecting.md) (1 shared connections)
- [test_degrade](test_degrade.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 69 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*