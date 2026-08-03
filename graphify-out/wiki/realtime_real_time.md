# realtime real time

> 74 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (25 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pray_command()** (21 connections) — `server/commands/lucidity_recovery_commands.py`
- **_perform_recovery_action()** (15 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_meditate_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (8 connections)
- **handle_therapy_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
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
- **test_handle_pray_command_no_room()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_success()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_with_mp_restoration()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 49 more nodes in this community*

## Relationships

- [combat services persistence](combat_services_persistence.md) (15 shared connections)
- [commands position system](commands_position_system.md) (7 shared connections)
- [commands npc admin](commands_npc_admin.md) (7 shared connections)
- [combat npc services](combat_npc_services.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)
- [regeneration service magic](regeneration_service_magic.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 267 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*