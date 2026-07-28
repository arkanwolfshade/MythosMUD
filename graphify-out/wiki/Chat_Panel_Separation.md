# Chat Panel Separation

> 28 nodes · cohesion 0.07

## Key Concepts

- **test_connection_state_machine.py** (39 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_last_error_set()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_nats_connection_state_machine_init()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_nats_connection_state_machine_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_reconnect_attempts_increment()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_recover()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_start_reconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_total_connections_increment()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_event_enum()** (2 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Unit tests for connection state machine.  Tests the NATSConnectionStateMachine c** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test disconnect() transition from connected to disconnected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test start_reconnect() transition from disconnected to reconnecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test recover() transition from degraded to connected.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test ConnectionEvent enum values.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test get_stats() returns comprehensive statistics.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test reconnect_attempts increments on connection failures.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test NATSConnectionStateMachine initialization.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test total_connections increments on successful connection.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test last_error is set on connection failure.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test NATSConnectionStateMachine initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- *... and 3 more nodes in this community*

## Relationships

- [Community 1929](Community_1929.md) (13 shared connections)
- [Archive Combat Health](Archive_Combat_Health.md) (2 shared connections)
- [Commands Go Command](Commands_Go_Command.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Messagebatcher Message Batcher](Messagebatcher_Message_Batcher.md) (1 shared connections)
- [Planning Archive Argon 2](Planning_Archive_Argon_2.md) (1 shared connections)
- [Archive Party System](Archive_Party_System.md) (1 shared connections)
- [Documentation Updates Archive](Documentation_Updates_Archive.md) (1 shared connections)
- [Security Archive Dual](Security_Archive_Dual.md) (1 shared connections)
- [Archive Planning Multiplayer](Archive_Planning_Multiplayer.md) (1 shared connections)
- [Archive Dual Connection](Archive_Dual_Connection.md) (1 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 91 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*