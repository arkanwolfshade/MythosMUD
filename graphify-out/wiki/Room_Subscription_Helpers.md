# Room Subscription Helpers

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

- [Player Name Validation](Player_Name_Validation.md) (12 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (2 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)
- [Cursor Skills Animate](Cursor_Skills_Animate.md) (1 shared connections)
- [Cursor Agents Readme](Cursor_Agents_Readme.md) (1 shared connections)
- [Api Player](Api_Player.md) (1 shared connections)
- [Logger Client Add To](Logger_Client_Add_To.md) (1 shared connections)
- [test_build_room_objects_without_environment_in_attributes](test_build_room_objects_without_environment_in_attributes.md) (1 shared connections)
- [test_invite_repr](test_invite_repr.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 99 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*