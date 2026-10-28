# test_look_npc.py

> 74 nodes · cohesion 0.05

## Key Concepts

- **test_lucidity_recovery_commands.py** (32 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionOnCooldownError** (24 connections) — `server/services/active_lucidity_service.py`
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
- *... and 49 more nodes in this community*

## Relationships

- [scripts](scripts.md) (8 shared connections)
- [command_parser.py](command_parser.py.md) (7 shared connections)
- [items/catalog_dml.py](items-catalog_dml.py.md) (5 shared connections)
- [gen_arena_migration_sql.py](gen_arena_migration_sql.py.md) (4 shared connections)
- [.get_memory_status_report](get_memory_status_report.md) (4 shared connections)
- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (3 shared connections)
- [test_health_service.py](test_health_service.py.md) (3 shared connections)
- [ItemFactory](ItemFactory.md) (2 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 176 (92%)
- INFERRED: 16 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*