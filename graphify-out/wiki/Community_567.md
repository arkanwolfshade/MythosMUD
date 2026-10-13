# Community 567

> 30 nodes

## Key Concepts

- **test_admin_summon_command.py** (33 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **_parse_summon_command_data()** (10 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **_broadcast_and_log_summon_success()** (8 connections) — `server/commands/admin_summon_command.py`
- **_validate_summon_prerequisites()** (8 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (6 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (6 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (5 connections) — `server/commands/admin_summon_command.py`
- **test_broadcast_and_log_summon_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_create_summon_item_instance_factory_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_create_summon_item_instance_success()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_log_summon_success()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_item_ok()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_missing_prototype()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_npc_stub()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_quantity_spike()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_room_manager_missing_at_execution()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_summon_npc_stub_response()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_summon_npc_stub_response_item_type()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_validate_summon_prerequisites_missing_item_services()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_validate_summon_prerequisites_missing_room_manager()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_validate_summon_prerequisites_ok()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_validate_summon_prerequisites_room_manager_no_add_drop()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **Parse and validate command_data; optionally record quantity spike; check NPC…** (1 connections) — `server/commands/admin_summon_command.py`
- **Broadcast admin_summon event to room, then record success logs.** (1 connections) — `server/commands/admin_summon_command.py`
- *... and 5 more nodes in this community*

## Relationships

- [Community 783](Community_783.md) (21 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (8 shared connections)
- [Community 253](Community_253.md) (2 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (2 shared connections)
- [Community 41](Community_41.md) (1 shared connections)
- [Community 131](Community_131.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 80 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*