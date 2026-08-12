# test_lucidity_recovery_commands.py

> 83 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pray_command()** (22 connections) — `server/commands/lucidity_recovery_commands.py`
- **asyncio** (21 connections)
- **LucidityActionOnCooldownError** (15 connections) — `server/services/active_lucidity_service.py`
- **UnknownLucidityActionError** (11 connections) — `server/services/active_lucidity_service.py`
- **handle_meditate_command()** (11 connections) — `server/commands/lucidity_recovery_commands.py`
- **_perform_recovery_action()** (11 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_therapy_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (9 connections)
- **_run_recovery_session()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **_restore_mp_for_action()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_handle_group_solace_command_unknown_action()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_cooldown()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_naive_datetime()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_cooldown_object()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_expiry()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_unknown_action()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_handle_folk_tonic_command_delegates()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 58 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (18 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (13 shared connections)
- [database.py](database.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [LucidityService](LucidityService.md) (2 shared connections)
- [debrief_command.py](debrief_command.py.md) (1 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 354 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*