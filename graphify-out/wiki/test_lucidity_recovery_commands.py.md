# test_lucidity_recovery_commands.py

> 78 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (27 connections) — `server/commands/lucidity_recovery_commands.py`
- **asyncio** (21 connections)
- **handle_pray_command()** (20 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionOnCooldownError** (17 connections) — `server/services/active_lucidity_service.py`
- **UnknownLucidityActionError** (11 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (11 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (11 connections)
- **handle_meditate_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **_run_recovery_session()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (7 connections) — `server/commands/lucidity_recovery_commands.py`
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
- *... and 53 more nodes in this community*

## Relationships

- [active_lucidity_service.py](active_lucidity_service.py.md) (8 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [debrief_command.py](debrief_command.py.md) (3 shared connections)
- [mock_persistence](mock_persistence.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 181 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*