# Test Admin Summon Command

> 53 nodes

## Key Concepts

- **admin_summon_command.py** (35 connections) — `server/commands/admin_summon_command.py`
- **test_admin_summon_command.py** (34 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **_resolve_summon_context()** (14 connections) — `server/commands/admin_summon_command.py`
- **asyncio** (13 connections)
- **handle_summon_command()** (12 connections) — `server/commands/admin_summon_command.py`
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

- [Item Factory](Item_Factory.md) (6 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (5 shared connections)
- [Test Inventory Helpers Extended](Test_Inventory_Helpers_Extended.md) (4 shared connections)
- [Test Envelope](Test_Envelope.md) (3 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (3 shared connections)
- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (3 shared connections)
- [Test Admin Permission Utils](Test_Admin_Permission_Utils.md) (3 shared connections)
- [Admin Actions Logger](Admin_Actions_Logger.md) (3 shared connections)
- [Performance Monitor](Performance_Monitor.md) (3 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 147 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*