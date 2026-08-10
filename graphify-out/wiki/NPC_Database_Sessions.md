# NPC Database Sessions

> 96 nodes

## Key Concepts

- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **_resolve_summon_context()** (11 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **handle_summon_command()** (10 connections) — `server/commands/admin_summon_command.py`
- **_broadcast_and_log_summon_success()** (7 connections) — `server/commands/admin_summon_command.py`
- **_complete_summon()** (7 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (6 connections) — `server/commands/admin_summon_command.py`
- **test_inventory_commands_state_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **_parse_summon_command_data()** (5 connections) — `server/commands/admin_summon_command.py`
- **_validate_summon_prerequisites()** (4 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (4 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (4 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (4 connections) — `server/commands/admin_summon_command.py`
- **test_persist_player_validation_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_resolve_state_with_app()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_state_no_app()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_state_no_state()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_player_success()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_player_no_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_player_not_found()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_with_connection_manager()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- *... and 71 more nodes in this community*

## Relationships

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (30 shared connections)
- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (6 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (4 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (3 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Typography Layout Spec](Typography_Layout_Spec.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (2 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 328 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*