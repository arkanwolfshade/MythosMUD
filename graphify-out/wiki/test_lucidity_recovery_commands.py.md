# test_lucidity_recovery_commands.py

> 79 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (32 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pray_command()** (20 connections) — `server/commands/lucidity_recovery_commands.py`
- **asyncio** (20 connections)
- **UnknownLucidityActionError** (13 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (10 connections)
- **handle_meditate_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **_run_recovery_session()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_therapy_command()** (7 connections) — `server/commands/lucidity_recovery_commands.py`
- **_handle_recovery_cooldown_error()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
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
- **_resolve_catatonia_observer()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_handle_group_solace_command_delegates()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_delegates()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 54 more nodes in this community*

## Relationships

- [active_lucidity_service.py](active_lucidity_service.py.md) (11 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (3 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (2 shared connections)
- [lucidity.py](lucidity.py.md) (2 shared connections)
- [mp_regeneration_service](mp_regeneration_service.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 170 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*