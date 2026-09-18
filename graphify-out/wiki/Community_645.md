# Community 645

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

- [Community 734](Community_734.md) (12 shared connections)
- [NATS Configuration](NATS_Configuration.md) (2 shared connections)
- [Community 1649](Community_1649.md) (2 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (2 shared connections)
- [Community 1300](Community_1300.md) (2 shared connections)
- [Community 1421](Community_1421.md) (2 shared connections)
- [Community 1853](Community_1853.md) (1 shared connections)
- [Community 1854](Community_1854.md) (1 shared connections)
- [Community 1852](Community_1852.md) (1 shared connections)
- [Community 1867](Community_1867.md) (1 shared connections)
- [Community 1868](Community_1868.md) (1 shared connections)
- [Community 1869](Community_1869.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 69 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*