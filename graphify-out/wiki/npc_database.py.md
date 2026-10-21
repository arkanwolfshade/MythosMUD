# npc_database.py

> 53 nodes · cohesion 0.08

## Key Concepts

- **admin_summon_command.py** (37 connections) — `server/commands/admin_summon_command.py`
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
- **test_create_summon_item_instance_factory_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_none()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_parse_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- *... and 28 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (15 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (7 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (6 shared connections)
- [test_metrics.py](test_metrics.py.md) (6 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 154 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*