# connection state machine

> 109 nodes

## Key Concepts

- **NATSConnectionStateMachine** (58 connections) — `server/realtime/connection_state_machine.py`
- **test_connection_state_machine.py** (39 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **nats_service.py** (24 connections) — `server/services/nats_service.py`
- **connection_state_machine.py** (10 connections) — `server/realtime/connection_state_machine.py`
- **ConnectionEvent** (4 connections) — `server/realtime/connection_state_machine.py`
- **.on_connection_failed()** (3 connections) — `server/realtime/connection_state_machine.py`
- **test_nats_connection_state_machine_init()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_nats_connection_state_machine_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connect_transition()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connected_successfully_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_connection_failed_from_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_disconnect_from_degraded()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_start_reconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_degrade()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_recover()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_open_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_close_circuit()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_disconnected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_circuit_open()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **test_can_attempt_connection_reconnecting()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- *... and 84 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [combat commands handler](combat_commands_handler.md) (6 shared connections)
- [commands communication say](commands_communication_say.md) (3 shared connections)
- [combat validator validators](combat_validator_validators.md) (3 shared connections)
- [service combat services](service_combat_services.md) (2 shared connections)
- [target resolution service](target_resolution_service.md) (2 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (1 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [subject admin controller](subject_admin_controller.md) (1 shared connections)
- [commands inventory put](commands_inventory_put.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 323 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*