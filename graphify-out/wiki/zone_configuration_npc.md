# zone configuration npc

> 81 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (25 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pray_command()** (21 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionOnCooldownError** (18 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (15 connections) — `server/commands/lucidity_recovery_commands.py`
- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **handle_meditate_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (8 connections)
- **handle_therapy_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionError** (7 connections) — `server/services/active_lucidity_service.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_restore_mp_for_action()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_expiry()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_cooldown_object()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_naive_datetime()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_group_solace_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **_format_recovery_success_message()** (3 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_handle_pray_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 56 more nodes in this community*

## Relationships

- [auth endpoints rationale](auth_endpoints_rationale.md) (16 shared connections)
- [commands npc admin](commands_npc_admin.md) (8 shared connections)
- [character creation service](character_creation_service.md) (6 shared connections)
- [npc population control](npc_population_control.md) (4 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (3 shared connections)
- [task registry app](task_registry_app.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)
- [regeneration service magic](regeneration_service_magic.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 304 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*