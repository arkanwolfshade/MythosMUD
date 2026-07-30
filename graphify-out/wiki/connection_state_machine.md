# connection state machine

> 29 nodes

## Key Concepts

- **NATSConnectionStateMachine** (58 connections) — `server/realtime/connection_state_machine.py`
- **.on_connection_failed()** (3 connections) — `server/realtime/connection_state_machine.py`
- **.__init__()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_connect()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_connected_successfully()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_disconnect()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_start_reconnect()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_open_circuit()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_close_circuit()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_degrade()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.on_recover()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.can_attempt_connection()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.should_open_circuit()** (2 connections) — `server/realtime/connection_state_machine.py`
- **.reset()** (2 connections) — `server/realtime/connection_state_machine.py`
- **Exception** (1 connections)
- **State machine for NATS connection lifecycle.      States:     - disconnected: No** (1 connections) — `server/realtime/connection_state_machine.py`
- **Initialize connection state machine.          Args:             connection_id: U** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connect transition.          Resets reconnection counter and prepare** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for successful connection.          Records connection time and incremen** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connection failure.          Records error and increments failure co** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for disconnection.          Increments disconnection counter.          A** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for starting reconnection.          Checks if circuit breaker should be** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for circuit breaker opening.          Logs circuit open event for alerti** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for circuit breaker closing.          Resets failure counters.** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connection degradation.          Logs degraded state for monitoring.** (1 connections) — `server/realtime/connection_state_machine.py`
- *... and 4 more nodes in this community*

## Relationships

- [enhance player ids()](enhance_player_ids%28%29.md) (12 shared connections)
- [BaseUserManager](BaseUserManager.md) (3 shared connections)
- [Test process room rows with](Test_process_room_rows_with.md) (2 shared connections)
- [Test build room objects handles](Test_build_room_objects_handles.md) (2 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [test_can_attempt_connection_circuit_open](test_can_attempt_connection_circuit_open.md) (1 shared connections)
- [test_can_attempt_connection_connected](test_can_attempt_connection_connected.md) (1 shared connections)
- [test_can_attempt_connection_reconnecting](test_can_attempt_connection_reconnecting.md) (1 shared connections)
- [test_close_circuit](test_close_circuit.md) (1 shared connections)
- [Domain Model Anemic Anti Pattern](Domain_Model_Anemic_Anti_Pattern.md) (1 shared connections)
- [Async Code Review Post Migration](Async_Code_Review_Post_Migration.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 99 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*