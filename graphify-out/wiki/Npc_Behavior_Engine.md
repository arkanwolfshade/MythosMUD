# Npc Behavior Engine

> 11 nodes

## Key Concepts

- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **LucidityActionError** (7 connections) — `server/services/active_lucidity_service.py`
- **test_handle_pray_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_group_solace_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_perform_recovery_action_unknown_action()** (3 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **RuntimeError** (2 connections)
- **Base error for lucidity action operations.** (1 connections) — `server/services/active_lucidity_service.py`
- **Raised when an unrecognised recovery action is requested.** (1 connections) — `server/services/active_lucidity_service.py`
- **Test handle_pray_command with unknown action.** (1 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **Test handle_group_solace_command with unknown action.** (1 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **Test perform_recovery_action() raises error for unknown action.** (1 connections) — `server/tests/unit/services/test_active_lucidity_service.py`

## Relationships

- [Container Open Events](Container_Open_Events.md) (5 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (4 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (2 shared connections)
- [WebSocket Message Validator](WebSocket_Message_Validator.md) (2 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 33 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*