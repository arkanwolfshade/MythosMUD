# Player Name Validation

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
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (2 shared connections)
- [Cursor Skills Animate](Cursor_Skills_Animate.md) (1 shared connections)
- [Cursor Agents Readme](Cursor_Agents_Readme.md) (1 shared connections)
- [Api Player](Api_Player.md) (1 shared connections)
- [Logger Client Add To](Logger_Client_Add_To.md) (1 shared connections)
- [test_build_room_objects_without_environment_in_attributes](test_build_room_objects_without_environment_in_attributes.md) (1 shared connections)
- [test_invite_repr](test_invite_repr.md) (1 shared connections)
- [test_invite_use_invite](test_invite_use_invite.md) (1 shared connections)
- [Services Combat Attack](Services_Combat_Attack.md) (1 shared connections)
- [Design Cursor Skills](Design_Cursor_Skills.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 87 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*