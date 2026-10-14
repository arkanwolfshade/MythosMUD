# test_admin_summon_command.py

> 50 nodes

## Key Concepts

- **test_admin_summon_command.py** (33 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **_resolve_summon_context()** (15 connections) — `server/commands/admin_summon_command.py`
- **handle_summon_command()** (14 connections) — `server/commands/admin_summon_command.py`
- **asyncio** (13 connections)
- **_complete_summon()** (11 connections) — `server/commands/admin_summon_command.py`
- **_parse_summon_command_data()** (11 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **_validate_summon_prerequisites()** (9 connections) — `server/commands/admin_summon_command.py`
- **_broadcast_and_log_summon_success()** (8 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (7 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (6 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (6 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (5 connections) — `server/commands/admin_summon_command.py`
- **test_complete_summon_factory_error()** (4 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_swallows_db_error()** (4 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_broadcast_and_log_summon_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_no_instance_without_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_none()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_parse_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_permission_denied()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_player_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- *... and 25 more nodes in this community*

## Relationships

- [alias_storage.py](alias_storage.py.md) (14 shared connections)
- [command_error](command_error.md) (8 shared connections)
- [test_item_factory.py](test_item_factory.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 127 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*