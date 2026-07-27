# Community 1929

> 27 nodes · cohesion 0.07

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
- **StateMachine** (2 connections)
- **Initialize connection state machine.          Args:             connection_id: U** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connect transition.          Resets reconnection counter and prepare** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for successful connection.          Records connection time and incremen** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for disconnection.          Increments disconnection counter.          A** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for starting reconnection.          Checks if circuit breaker should be** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for circuit breaker opening.          Logs circuit open event for alerti** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for circuit breaker closing.          Resets failure counters.** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for connection degradation.          Logs degraded state for monitoring.** (1 connections) — `server/realtime/connection_state_machine.py`
- **Handler for recovery from degraded state.          Logs recovery for monitoring.** (1 connections) — `server/realtime/connection_state_machine.py`
- **Check if connection attempt is allowed in current state.          Returns:** (1 connections) — `server/realtime/connection_state_machine.py`
- **Check if circuit breaker should be opened.          Returns:             True if** (1 connections) — `server/realtime/connection_state_machine.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_connection_state_machine.py](test_connection_state_machine.py.md) (13 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Community 1497](Community_1497.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (2 shared connections)
- [Community 1979](Community_1979.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [test_get_player_info_player_not_found](test_get_player_info_player_not_found.md) (1 shared connections)
- [test_get_player_info_invalid_player_id](test_get_player_info_invalid_player_id.md) (1 shared connections)
- [mock_name_extractor](mock_name_extractor.md) (1 shared connections)
- [mock_logger](mock_logger.md) (1 shared connections)
- [test_normalize_event_ids_both_provided](test_normalize_event_ids_both_provided.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 96 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*