# Connection State Machine

> 29 nodes

## Key Concepts

- **NATSConnectionStateMachine** (58 connections) — `server/realtime/connection_state_machine.py`
- **.on_connection_failed()** (3 connections) — `server/realtime/connection_state_machine.py`
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
- **Exception** (1 connections)
- **Initialize connection state machine. Args: connection_id: Unique identifier for…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connect transition. Resets reconnection counter and prepares for…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for successful connection. Records connection time and increments…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connection failure. Records error and increments failure counter.…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for disconnection. Increments disconnection counter. AI: Track…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for starting reconnection. Checks if circuit breaker should be…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for circuit breaker opening. Logs circuit open event for alerting. AI:…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for circuit breaker closing. Resets failure counters. AI: Circuit…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connection degradation. Logs degraded state for monitoring. AI:…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for recovery from degraded state. Logs recovery for monitoring. AI:…** (1 connections) — `server/realtime/connection_state_machine.py`
- *... and 4 more nodes in this community*

## Relationships

- [Test Connection State Machine](Test_Connection_State_Machine.md) (35 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (4 shared connections)
- [Connection State Machine](Connection_State_Machine.md) (4 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*