# Container Open Events

> 52 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **handle_pray_command()** (22 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionOnCooldownError** (16 connections) — `server/services/active_lucidity_service.py`
- **test_handle_pray_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_expiry()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_cooldown_object()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_naive_datetime()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_no_room()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_success()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_with_mp_restoration()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_delegates()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_group_solace_command_delegates()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_therapy_command_delegates()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_folk_tonic_command_delegates()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_os_error()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_negative_delta()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_with_mp_restoration()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_mp_restored_zero()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_no_app()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_perform_recovery_action_on_cooldown()** (3 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 27 more nodes in this community*

## Relationships

- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (15 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (5 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (4 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (2 shared connections)
- [WebSocket Message Validator](WebSocket_Message_Validator.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 165 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*