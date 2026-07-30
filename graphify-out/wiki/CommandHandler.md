# CommandHandler

> 80 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (25 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pray_command()** (22 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionOnCooldownError** (16 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (15 connections) — `server/commands/lucidity_recovery_commands.py`
- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **handle_meditate_command()** (11 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_therapy_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (8 connections)
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
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
- *... and 55 more nodes in this community*

## Relationships

- [UUID](UUID.md) (14 shared connections)
- [test magic commands](test_magic_commands.md) (7 shared connections)
- [DropResolved](DropResolved.md) (6 shared connections)
- [Player Position Service](Player_Position_Service.md) (5 shared connections)
- [monitoring](monitoring.md) (4 shared connections)
- [test player preferences service](test_player_preferences_service.md) (2 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [Lock](Lock.md) (2 shared connections)
- [AuthSlice](AuthSlice.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 300 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*