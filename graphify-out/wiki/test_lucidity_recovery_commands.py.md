# test_lucidity_recovery_commands.py

> 86 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (35 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pray_command()** (21 connections) — `server/commands/lucidity_recovery_commands.py`
- **asyncio** (21 connections)
- **LucidityActionOnCooldownError** (17 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (12 connections) — `server/commands/lucidity_recovery_commands.py`
- **UnknownLucidityActionError** (11 connections) — `server/services/active_lucidity_service.py`
- **handle_meditate_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (9 connections)
- **handle_folk_tonic_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_therapy_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **_run_recovery_session()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionError** (6 connections) — `server/services/active_lucidity_service.py`
- **_validate_recovery_context()** (6 connections) — `server/commands/lucidity_recovery_commands.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **_restore_mp_for_action()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_handle_group_solace_command_unknown_action()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_cooldown()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_naive_datetime()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_cooldown_object()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_expiry()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_unknown_action()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- *... and 61 more nodes in this community*

## Relationships

- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (18 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [command_service.py](command_service.py.md) (6 shared connections)
- [.state](state.md) (2 shared connections)
- [mp_regeneration_service](mp_regeneration_service.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 190 (91%)
- INFERRED: 19 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*