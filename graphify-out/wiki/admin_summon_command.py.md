# admin_summon_command.py

> 53 nodes

## Key Concepts

- **admin_summon_command.py** (35 connections) — `server/commands/admin_summon_command.py`
- **test_admin_summon_command.py** (34 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **_resolve_summon_context()** (15 connections) — `server/commands/admin_summon_command.py`
- **handle_summon_command()** (13 connections) — `server/commands/admin_summon_command.py`
- **asyncio** (13 connections)
- **_complete_summon()** (10 connections) — `server/commands/admin_summon_command.py`
- **_parse_summon_command_data()** (10 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **_broadcast_and_log_summon_success()** (8 connections) — `server/commands/admin_summon_command.py`
- **_validate_summon_prerequisites()** (8 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (6 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (6 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (6 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (5 connections) — `server/commands/admin_summon_command.py`
- **test_complete_summon_factory_error()** (4 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_swallows_db_error()** (4 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_broadcast_and_log_summon_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_no_instance_without_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_create_summon_item_instance_factory_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_none()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_parse_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- *... and 28 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (6 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (5 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [.state](state.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [validate_admin_permission](validate_admin_permission.md) (3 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (3 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 146 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*