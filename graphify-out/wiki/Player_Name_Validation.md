# Player Name Validation

> 26 nodes

## Key Concepts

- **test_connection_state_machine.py** (39 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connect_transition()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_degraded()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_start_reconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_open_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_circuit_open()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_should_open_circuit_under_threshold()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_last_connected_time_set()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_on_enter_state_logs()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_invalid_transition_raises_error()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_event_enum()** (2 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Unit tests for connection state machine.  Tests the NATSConnectionStateMachine c** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test ConnectionEvent enum values.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connect() transition from disconnected to connecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connected_successfully() transition from connecting to connected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test disconnect() transition from degraded to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test start_reconnect() transition from disconnected to reconnecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test open_circuit() transition from reconnecting to circuit_open.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test can_attempt_connection() returns True when connecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test can_attempt_connection() returns False when circuit is open.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test should_open_circuit() returns False when under threshold.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test last_connected_time is set on successful connection.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test on_enter_state() logs state transitions.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- *... and 1 more nodes in this community*

## Relationships

- [Room Subscription Helpers](Room_Subscription_Helpers.md) (12 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (2 shared connections)
- [Cursor Agents Readme](Cursor_Agents_Readme.md) (1 shared connections)
- [Agents Guardrails Critical Section](Agents_Guardrails_Critical_Section.md) (1 shared connections)
- [Api Player](Api_Player.md) (1 shared connections)
- [Logger Client Add To](Logger_Client_Add_To.md) (1 shared connections)
- [Easy Coverage Wins](Easy_Coverage_Wins.md) (1 shared connections)
- [test_invite_use_invite](test_invite_use_invite.md) (1 shared connections)
- [Fastapi Code Review](Fastapi_Code_Review.md) (1 shared connections)
- [Services Combat Attack](Services_Combat_Attack.md) (1 shared connections)
- [Design Cursor Skills](Design_Cursor_Skills.md) (1 shared connections)
- [Archive Planning Cursor](Archive_Planning_Cursor.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 87 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*